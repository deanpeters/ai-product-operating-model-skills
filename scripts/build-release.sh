#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_dir"

./scripts/test-library.sh

python3 - <<'PY'
from pathlib import Path
import shutil
import zipfile

root = Path.cwd()
version = (root / "VERSION").read_text().strip()
dist = root / "dist"
release = dist / f"aipom-skills-v{version}"
archive = dist / f"aipom-skills-v{version}.zip"
stable_archive = dist / "aipom-skills.zip"

if release.exists():
    shutil.rmtree(release)
if archive.exists():
    archive.unlink()
if stable_archive.exists():
    stable_archive.unlink()

release.mkdir(parents=True)

for filename in [
    "AGENTS.md",
    "README.md",
    "ROADMAP.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "VERSION",
    "CITATION.cff",
    "SECURITY.md",
    "LICENSE",
    "requirements-dev.txt",
    "create-starter-pack.sh",
    "create-starter-pack.ps1",
]:
    shutil.copy2(root / filename, release / filename)

for dirname in [".github", "assessments", "catalog", "commands", "docs", "scripts", "skills", "starter-packs", "tests"]:
    shutil.copytree(
        root / dirname,
        release / dirname,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )

with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
    for path in sorted(release.rglob("*")):
        if path.is_file():
            bundle.write(path, path.relative_to(dist))

shutil.copy2(archive, stable_archive)
print(f"Built {archive.relative_to(root)}")
PY

python3 - <<'PY'
from pathlib import Path
import subprocess
import tempfile
import zipfile

root = Path.cwd()
version = (root / "VERSION").read_text().strip()
archive = root / "dist" / f"aipom-skills-v{version}.zip"

with tempfile.TemporaryDirectory(prefix="verify-aipom-release-") as temporary:
    destination = Path(temporary)
    with zipfile.ZipFile(archive) as bundle:
        bad_file = bundle.testzip()
        if bad_file:
            raise SystemExit(f"Corrupt canonical release member: {bad_file}")
        bundle.extractall(destination)
        for info in bundle.infolist():
            target = destination / info.filename
            permissions = (info.external_attr >> 16) & 0o777
            if target.exists() and permissions:
                target.chmod(permissions)
    release = destination / f"aipom-skills-v{version}"
    required = [
        "create-starter-pack.sh",
        "create-starter-pack.ps1",
        "scripts/create-starter-pack.py",
        "scripts/build-starter-pack-release.py",
        "starter-packs/schema/starter-pack.schema.yaml",
    ]
    missing = [name for name in required if not (release / name).is_file()]
    if missing:
        raise SystemExit(f"Canonical release is missing Starter Pack files: {missing}")
    if len(list((release / "starter-packs" / "manifests").glob("*.yaml"))) != 5:
        raise SystemExit("Canonical release does not contain five Starter Pack manifests")
    subprocess.run(
        ["python3", "scripts/create-starter-pack.py", "--list"],
        cwd=release,
        check=True,
        capture_output=True,
        text=True,
    )
    subprocess.run(
        ["bash", "scripts/test-library.sh"],
        cwd=release,
        check=True,
    )

print(f"Verified clean extraction and Starter Pack tooling in {archive.relative_to(root)}")
PY

python3 scripts/build-codex-release.py
python3 scripts/build-starter-pack-release.py
python3 scripts/test-starter-pack-cold-start.py

python3 - <<'PY'
from hashlib import sha256
from pathlib import Path

root = Path.cwd()
version = (root / "VERSION").read_text().strip()
dist = root / "dist"
archives = [
    dist / f"aipom-skills-v{version}.zip",
    dist / f"aipom-codex-skills-v{version}.zip",
] + sorted(dist.glob(f"aipom-starter-pack-*-v{version}.zip"))
lines = [f"{sha256(path.read_bytes()).hexdigest()}  {path.name}" for path in archives]
(dist / "SHA256SUMS").write_text("\n".join(lines) + "\n")
print("Built dist/SHA256SUMS")
PY
