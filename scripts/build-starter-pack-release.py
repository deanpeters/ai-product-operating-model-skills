#!/usr/bin/env python3
"""Build and verify deterministic release archives for every Starter Pack."""

from __future__ import annotations

import hashlib
import importlib.util
import shutil
import stat
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

import yaml


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PROJECTS = DIST / "starter-packs"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
GENERATOR_PATH = ROOT / "scripts" / "create-starter-pack.py"
FIXED_ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)


def load_generator():
    spec = importlib.util.spec_from_file_location("create_starter_pack", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load the Starter Pack generator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def deterministic_zip(source: Path, archive: Path, archive_root: str) -> None:
    with zipfile.ZipFile(
        archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as bundle:
        for path in sorted(item for item in source.rglob("*") if item.is_file()):
            relative = path.relative_to(source).as_posix()
            info = zipfile.ZipInfo(f"{archive_root}/{relative}", FIXED_ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            permissions = path.stat().st_mode & 0o777
            info.external_attr = (stat.S_IFREG | permissions) << 16
            bundle.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def safe_member(name: str, archive_root: str) -> bool:
    path = PurePosixPath(name)
    return (
        not path.is_absolute()
        and ".." not in path.parts
        and len(path.parts) > 1
        and path.parts[0] == archive_root
    )


def verify_archive(archive: Path, archive_root: str, pack_id: str, generator) -> None:
    with zipfile.ZipFile(archive) as bundle:
        bad_file = bundle.testzip()
        if bad_file:
            raise RuntimeError(f"{archive.name}: corrupt member {bad_file}")
        unsafe = [name for name in bundle.namelist() if not safe_member(name, archive_root)]
        if unsafe:
            raise RuntimeError(f"{archive.name}: unsafe archive members: {unsafe}")
        with tempfile.TemporaryDirectory(prefix=f"verify-{pack_id}-") as temporary:
            destination = Path(temporary)
            bundle.extractall(destination)
            project = destination / archive_root
            required = [
                "README.md",
                "AGENTS.md",
                "CLAUDE.md",
                "LICENSE",
                "PACK-LOCK.yaml",
                "CONTEXT-LEDGER.md",
                "DECISION-LOG.md",
                ".agents/skills/aipom-start/SKILL.md",
                ".agents/skills/aipom-start/agents/openai.yaml",
                ".claude/skills/aipom-start/SKILL.md",
            ]
            missing = [name for name in required if not (project / name).is_file()]
            if missing:
                raise RuntimeError(f"{archive.name}: missing required files: {missing}")
            lock = yaml.safe_load((project / "PACK-LOCK.yaml").read_text(encoding="utf-8"))
            if lock["pack"]["id"] != pack_id:
                raise RuntimeError(f"{archive.name}: lockfile pack id does not match")
            if lock["generation"]["platform"] != "both":
                raise RuntimeError(f"{archive.name}: release pack must support both platforms")
            generator.validate_generated_links(project)


def build() -> list[Path]:
    generator = load_generator()
    manifests = generator.validate_and_load_manifests()

    if PROJECTS.exists():
        shutil.rmtree(PROJECTS)
    PROJECTS.mkdir(parents=True)
    for stale in DIST.glob("aipom-starter-pack-*.zip"):
        stale.unlink()

    archives: list[Path] = []
    for pack_id in sorted(manifests):
        manifest = manifests[pack_id]
        project = PROJECTS / pack_id
        generator.generate_pack(manifest, "both", project, dry_run=False)

        archive_root = f"aipom-starter-pack-{pack_id}-v{VERSION}"
        archive = DIST / f"{archive_root}.zip"
        deterministic_zip(project, archive, archive_root)

        reproducibility_check = DIST / f".{archive_root}.repro.zip"
        deterministic_zip(project, reproducibility_check, archive_root)
        if archive.read_bytes() != reproducibility_check.read_bytes():
            raise RuntimeError(f"{archive.name}: deterministic rebuild did not match")
        reproducibility_check.unlink()

        verify_archive(archive, archive_root, pack_id, generator)
        archives.append(archive)
        print(f"Built and verified {archive.relative_to(ROOT)}")

    checksum_file = DIST / "STARTER-PACK-SHA256SUMS"
    checksum_file.write_text(
        "\n".join(f"{sha256(path)}  {path.name}" for path in archives) + "\n",
        encoding="utf-8",
    )
    print(f"Built {checksum_file.relative_to(ROOT)}")
    return archives


def main() -> int:
    build()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
