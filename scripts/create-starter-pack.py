#!/usr/bin/env python3
"""Generate a self-contained, platform-neutral AIPOM Starter Pack project."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote, unquote

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = ROOT / "starter-packs" / "manifests"
SCHEMA = ROOT / "starter-packs" / "schema" / "starter-pack.schema.yaml"
TEMPLATES = ROOT / "starter-packs" / "templates"
ADAPTERS = ROOT / "starter-packs" / "adapters"
SKILLS = ROOT / "skills"
VERSION_FILE = ROOT / "VERSION"
GENERATOR_VERSION = "0.2.0"
CANONICAL_REPOSITORY = (
    "https://github.com/deanpeters/ai-product-operating-model-skills"
)

FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
MARKDOWN_LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
PLACEHOLDER = re.compile(r"{{([A-Z0-9_]+)}}")
SKIP_LINK_PREFIXES = ("http://", "https://", "mailto:", "#")


class PackError(RuntimeError):
    """Raised when a Starter Pack cannot be generated safely."""


def read_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise PackError(f"{path.relative_to(ROOT)} must contain a YAML mapping")
    return data


def load_skill_records() -> dict[str, dict]:
    records: dict[str, dict] = {}
    for path in sorted(SKILLS.glob("*/SKILL.md")):
        match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
        if not match:
            raise PackError(f"{path.relative_to(ROOT)} is missing YAML frontmatter")
        data = yaml.safe_load(match.group(1)) or {}
        name = data.get("name")
        if not isinstance(name, str):
            raise PackError(f"{path.relative_to(ROOT)} is missing a skill name")
        records[name] = data
    return records


def dependency_closure(
    explicit: list[str], records: dict[str, dict]
) -> tuple[list[str], dict[str, str]]:
    resolved: set[str] = set()
    visiting: list[str] = []
    inclusion: dict[str, str] = {}

    def visit(name: str, reason: str) -> None:
        if name in resolved:
            if reason == "explicit":
                inclusion[name] = reason
            return
        if name in visiting:
            cycle = " -> ".join(visiting[visiting.index(name) :] + [name])
            raise PackError(f"skill dependency cycle: {cycle}")
        record = records.get(name)
        if record is None:
            raise PackError(f"unknown skill dependency: {name}")
        visiting.append(name)
        dependencies = record.get("depends_on", [])
        if not isinstance(dependencies, list) or not all(
            isinstance(item, str) for item in dependencies
        ):
            raise PackError(f"{name}: depends_on must be a list of skill names")
        for dependency in dependencies:
            visit(dependency, "dependency")
        visiting.pop()
        resolved.add(name)
        inclusion[name] = reason

    for name in explicit:
        visit(name, "explicit")
    return sorted(resolved), inclusion


def validate_and_load_manifests() -> dict[str, dict]:
    if not SCHEMA.is_file():
        raise PackError("Starter Pack schema is missing")
    schema = read_yaml(SCHEMA)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    records = load_skill_records()
    manifests: dict[str, dict] = {}

    for path in sorted(MANIFESTS.glob("*.yaml")):
        data = read_yaml(path)
        errors = sorted(
            validator.iter_errors(data),
            key=lambda error: tuple(str(part) for part in error.absolute_path),
        )
        if errors:
            error = errors[0]
            location = ".".join(str(part) for part in error.absolute_path) or "manifest"
            raise PackError(
                f"{path.relative_to(ROOT)}: {location}: {error.message}"
            )
        if data["id"] != path.stem:
            raise PackError(f"{path.relative_to(ROOT)} filename does not match its id")
        for value in canonical_file_paths(data):
            candidate = PurePosixPath(value)
            if candidate.is_absolute() or ".." in candidate.parts or "\\" in value:
                raise PackError(f"unsafe canonical path in {path.name}: {value}")
            if not (ROOT / candidate).is_file():
                raise PackError(f"missing canonical file in {path.name}: {value}")
        resolved, inclusion = dependency_closure(data["skills"]["include"], records)
        data["_path"] = path
        data["_resolved_skills"] = resolved
        data["_skill_inclusion"] = inclusion
        manifests[data["id"]] = data

    if not manifests:
        raise PackError("no Starter Pack manifests were found")
    return manifests


def canonical_file_paths(manifest: dict) -> list[str]:
    return [
        manifest["entrypoint"]["persona_guide"],
        manifest["entrypoint"]["journey"],
        manifest["entrypoint"]["command"],
        *manifest["supporting_content"],
        manifest["license"]["file"],
    ]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_directory(path: Path) -> str:
    digest = hashlib.sha256()
    for file_path in sorted(item for item in path.rglob("*") if item.is_file()):
        relative = file_path.relative_to(path).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(file_path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def source_commit() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "unknown"
    return result.stdout.strip() or "unknown"


def source_is_dirty() -> bool | str:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "unknown"
    return bool(result.stdout.strip())


def library_version() -> str:
    return VERSION_FILE.read_text(encoding="utf-8").strip()


def render(template: str, values: dict[str, str], source: Path) -> str:
    missing = sorted(set(PLACEHOLDER.findall(template)) - values.keys())
    if missing:
        raise PackError(f"{source.relative_to(ROOT)} has unknown placeholders: {missing}")
    rendered = PLACEHOLDER.sub(lambda match: values[match.group(1)], template)
    leftovers = PLACEHOLDER.findall(rendered)
    if leftovers:
        raise PackError(f"{source.relative_to(ROOT)} has unresolved placeholders: {leftovers}")
    return rendered


def bullet_list(items: list[str], formatter=lambda item: item) -> str:
    return "\n".join(f"- {formatter(item)}" for item in items)


def template_values(manifest: dict, platform: str) -> dict[str, str]:
    entrypoint = manifest["entrypoint"]
    platform_labels = {
        "codex": "Codex",
        "claude-code": "Claude Code",
        "both": "Codex or Claude Code",
    }
    platform_start = {
        "codex": (
            "2. Open a terminal in this folder and start Codex.\n"
            "3. Invoke `$aipom-start`. You can also ask: `Use $aipom-start to begin in context-dump mode.`"
        ),
        "claude-code": (
            "2. Open a terminal in this folder and start Claude Code.\n"
            "3. Invoke `/aipom-start`. You can add your preference: `/aipom-start begin in context-dump mode`."
        ),
        "both": (
            "2. Open a terminal in this folder and start Codex or Claude Code.\n"
            "3. In Codex, invoke `$aipom-start`. In Claude Code, invoke `/aipom-start`. "
            "Add `begin in context-dump mode` when you already supplied substantial material."
        ),
    }
    return {
        "TITLE": manifest["title"],
        "PERSONA": manifest["persona"],
        "DESCRIPTION": manifest["description"],
        "TRIGGER": manifest["scenario"]["trigger"],
        "DECISION": manifest["scenario"]["decision"],
        "PLATFORM_LABEL": platform_labels[platform],
        "PLATFORM_START": platform_start[platform],
        "COMPLETION_RESULT": manifest["completion"]["result"],
        "REQUIRED_OUTPUTS": bullet_list(manifest["completion"]["required_outputs"]),
        "AUTHORITY_BOUNDARY": manifest["completion"]["authority_boundary"],
        "PERSONA_GUIDE": f"library/{entrypoint['persona_guide']}",
        "JOURNEY": f"library/{entrypoint['journey']}",
        "COMMAND": f"library/{entrypoint['command']}",
        "JOURNEY_SOURCE": entrypoint["journey"],
        "COMMAND_SOURCE": entrypoint["command"],
        "SKILL_LIST": bullet_list(
            manifest["_resolved_skills"],
            lambda name: f"[`{name}`](library/skills/{name}/SKILL.md)",
        ),
        "PACK_ID": manifest["id"],
        "PACK_VERSION": manifest["version"],
        "LIBRARY_VERSION": library_version(),
    }


def copy_canonical_content(manifest: dict, destination: Path) -> dict[str, str]:
    source_files: dict[str, str] = {}
    library = destination / "library"
    for value in sorted(set(canonical_file_paths(manifest))):
        source = ROOT / value
        target = destination / value if value == manifest["license"]["file"] else library / value
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        source_files[value] = sha256_file(source)

    for name in manifest["_resolved_skills"]:
        source_dir = SKILLS / name
        target_dir = library / "skills" / name
        shutil.copytree(source_dir, target_dir)
        for source in sorted(item for item in source_dir.rglob("*") if item.is_file()):
            source_files[source.relative_to(ROOT).as_posix()] = sha256_file(source)
    return source_files


def render_shared_shell(manifest: dict, platform: str, destination: Path) -> None:
    values = template_values(manifest, platform)
    for source in sorted(TEMPLATES.rglob("*.tmpl")):
        relative = source.relative_to(TEMPLATES)
        target = destination / relative.with_suffix("")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            render(source.read_text(encoding="utf-8"), values, source),
            encoding="utf-8",
        )


def render_platform_adapters(manifest: dict, platform: str, destination: Path) -> None:
    values = template_values(manifest, platform)
    skill_template = ADAPTERS / "aipom-start" / "SKILL.md.tmpl"
    targets: list[Path] = []
    if platform in {"codex", "both"}:
        targets.append(destination / ".agents" / "skills" / "aipom-start" / "SKILL.md")
    if platform in {"claude-code", "both"}:
        targets.append(destination / ".claude" / "skills" / "aipom-start" / "SKILL.md")
    for target in targets:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            render(skill_template.read_text(encoding="utf-8"), values, skill_template),
            encoding="utf-8",
        )

    if platform in {"codex", "both"}:
        metadata_template = ADAPTERS / "codex" / "openai.yaml.tmpl"
        metadata_target = (
            destination
            / ".agents"
            / "skills"
            / "aipom-start"
            / "agents"
            / "openai.yaml"
        )
        metadata_target.parent.mkdir(parents=True, exist_ok=True)
        metadata_target.write_text(
            render(
                metadata_template.read_text(encoding="utf-8"),
                values,
                metadata_template,
            ),
            encoding="utf-8",
        )


def split_link(raw: str) -> tuple[str, str]:
    cleaned = raw.strip().strip("<>")
    if "#" not in cleaned:
        return cleaned, ""
    path, fragment = cleaned.split("#", 1)
    return path, f"#{fragment}"


def rewrite_unpacked_links(destination: Path, commit: str) -> None:
    """Point canonical links omitted from the pack to the pinned upstream source."""
    library = destination / "library"
    source_ref = commit if commit != "unknown" else "main"
    for generated in sorted(library.rglob("*.md")):
        source_relative = generated.relative_to(library)
        canonical_source = ROOT / source_relative
        text = generated.read_text(encoding="utf-8")

        def replace(match: re.Match) -> str:
            label, raw = match.groups()
            stripped = raw.strip().strip("<>")
            if stripped.startswith(SKIP_LINK_PREFIXES):
                return match.group(0)
            path_part, fragment = split_link(raw)
            if not path_part:
                return match.group(0)
            canonical_target = (canonical_source.parent / unquote(path_part)).resolve()
            try:
                target_relative = canonical_target.relative_to(ROOT.resolve())
            except ValueError:
                raise PackError(
                    f"canonical link leaves the repository: {source_relative}: {raw}"
                )
            packaged_target = library / target_relative
            if packaged_target.exists():
                return match.group(0)
            if not canonical_target.exists():
                raise PackError(
                    f"canonical link target is missing: {source_relative}: {raw}"
                )
            url = (
                f"{CANONICAL_REPOSITORY}/blob/{source_ref}/"
                f"{quote(target_relative.as_posix(), safe='/')}{fragment}"
            )
            return f"[{label}]({url})"

        generated.write_text(MARKDOWN_LINK.sub(replace, text), encoding="utf-8")


def validate_generated_links(destination: Path) -> int:
    checked = 0
    for source in sorted(destination.rglob("*.md")):
        text = source.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            raw = match.group(2).strip().strip("<>")
            if raw.startswith(SKIP_LINK_PREFIXES):
                continue
            path_part, _fragment = split_link(raw)
            if not path_part:
                continue
            checked += 1
            target = (source.parent / unquote(path_part)).resolve()
            try:
                target.relative_to(destination.resolve())
            except ValueError as exc:
                raise PackError(f"generated link leaves the project: {source}: {raw}") from exc
            if not target.exists():
                raise PackError(f"generated link target is missing: {source}: {raw}")
    return checked


def project_file_hashes(destination: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for path in sorted(item for item in destination.rglob("*") if item.is_file()):
        if path.name == "PACK-LOCK.yaml":
            continue
        hashes[path.relative_to(destination).as_posix()] = sha256_file(path)
    return hashes


def write_lockfile(
    manifest: dict,
    platform: str,
    destination: Path,
    commit: str,
    source_files: dict[str, str],
) -> None:
    manifest_path = manifest["_path"]
    lock = {
        "schema_version": 1,
        "pack": {
            "id": manifest["id"],
            "version": manifest["version"],
            "title": manifest["title"],
            "persona": manifest["persona"],
            "scenario": manifest["scenario"]["id"],
        },
        "generation": {
            "generator_version": GENERATOR_VERSION,
            "platform": platform,
        },
        "library": {
            "version": library_version(),
            "source_repository": CANONICAL_REPOSITORY,
            "source_commit": commit,
            "source_worktree_dirty": source_is_dirty(),
        },
        "manifest": {
            "source": manifest_path.relative_to(ROOT).as_posix(),
            "sha256": sha256_file(manifest_path),
        },
        "entrypoint": manifest["entrypoint"],
        "skills": [
            {
                "name": name,
                "included_by": manifest["_skill_inclusion"][name],
                "source_sha256": sha256_directory(SKILLS / name),
            }
            for name in manifest["_resolved_skills"]
        ],
        "canonical_source_files": source_files,
        "generated_project_files": project_file_hashes(destination),
        "notice": (
            "Files under library/ are generated dependencies. Regenerate the pack "
            "to adopt canonical changes instead of editing them as source."
        ),
    }
    (destination / "PACK-LOCK.yaml").write_text(
        yaml.safe_dump(lock, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def generation_plan(manifest: dict, platform: str, output: Path) -> str:
    return (
        f"Starter Pack: {manifest['title']}\n"
        f"Pack ID: {manifest['id']}\n"
        f"Platform: {platform}\n"
        f"Output: {output}\n"
        f"Skills: {len(manifest['_resolved_skills'])} "
        f"({len(manifest['skills']['include'])} explicit, "
        f"{len(manifest['_resolved_skills']) - len(manifest['skills']['include'])} dependencies)"
    )


def generate_pack(manifest: dict, platform: str, output: Path, dry_run: bool) -> Path:
    output = output.expanduser().resolve()
    if platform != "both" and platform not in manifest["platforms"]:
        raise PackError(f"{manifest['id']} does not support platform '{platform}'")
    if output.exists():
        raise PackError(
            f"destination already exists; choose a new directory: {output}"
        )
    if dry_run:
        print(generation_plan(manifest, platform, output))
        return output

    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(
        tempfile.mkdtemp(prefix=f".{manifest['id']}-", dir=output.parent)
    )
    try:
        source_files = copy_canonical_content(manifest, temporary)
        render_shared_shell(manifest, platform, temporary)
        render_platform_adapters(manifest, platform, temporary)
        commit = source_commit()
        rewrite_unpacked_links(temporary, commit)
        checked = validate_generated_links(temporary)
        write_lockfile(manifest, platform, temporary, commit, source_files)
        os.replace(temporary, output)
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise

    print(generation_plan(manifest, platform, output))
    print(f"Checked {checked} generated relative Markdown link(s).")
    print(f"\nCreated {output}")
    print(f"Next: cd {output}")
    if platform == "claude-code":
        print("Then start Claude Code and invoke /aipom-start.")
    elif platform == "codex":
        print("Then start Codex and invoke $aipom-start.")
    else:
        print("Then invoke $aipom-start in Codex or /aipom-start in Claude Code.")
    return output


def list_manifests(manifests: dict[str, dict]) -> None:
    print("Available AIPOM Starter Packs:\n")
    for pack_id in sorted(manifests):
        manifest = manifests[pack_id]
        print(f"{pack_id}\n  {manifest['title']}\n  {manifest['description']}\n")


def describe_manifest(manifest: dict) -> None:
    print(f"{manifest['title']} ({manifest['id']} v{manifest['version']})")
    print(f"Persona: {manifest['persona']}")
    print(f"Trigger: {manifest['scenario']['trigger']}")
    print(f"Decision: {manifest['scenario']['decision']}")
    print(f"Result: {manifest['completion']['result']}")
    print(f"Resolved skills: {len(manifest['_resolved_skills'])}")


def prompt_choice(prompt: str, options: list[str], default: int = 1) -> str:
    while True:
        print(prompt)
        for index, option in enumerate(options, 1):
            marker = " (default)" if index == default else ""
            print(f"  {index}. {option}{marker}")
        response = input("> ").strip()
        if not response:
            return options[default - 1]
        if response.isdigit() and 1 <= int(response) <= len(options):
            return options[int(response) - 1]
        print(f"Enter a number from 1 to {len(options)}.")


def interactive_selection(manifests: dict[str, dict]) -> tuple[dict, str, Path]:
    print("AIPOM Starter Pack generator\n")
    ids = sorted(manifests)
    labels = [f"{manifests[item]['title']} — {manifests[item]['description']}" for item in ids]
    selected_label = prompt_choice("Choose the job you want to do:", labels)
    manifest = manifests[ids[labels.index(selected_label)]]
    platform_label = prompt_choice(
        "Which coding-agent environment will you use?",
        ["Codex", "Claude Code", "Both / decide later"],
        default=3,
    )
    platform = {
        "Codex": "codex",
        "Claude Code": "claude-code",
        "Both / decide later": "both",
    }[platform_label]
    default_output = Path.cwd() / f"{manifest['id']}-workspace"
    response = input(f"Output directory [{default_output}]: ").strip()
    output = Path(response) if response else default_output
    print("\n" + generation_plan(manifest, platform, output.expanduser().resolve()))
    confirmation = input("Create this working project? [Y/n]: ").strip().lower()
    if confirmation not in {"", "y", "yes"}:
        raise PackError("generation cancelled")
    return manifest, platform, output


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Generate a self-contained AIPOM Starter Pack working project. "
            "Run without arguments for an interactive wizard."
        )
    )
    parser.add_argument("--list", action="store_true", help="list available packs")
    parser.add_argument("--describe", metavar="PACK_ID", help="describe one pack")
    parser.add_argument("--pack", metavar="PACK_ID", help="pack to generate")
    parser.add_argument(
        "--platform",
        choices=("codex", "claude-code", "both"),
        default="both",
        help="intended coding-agent environment (default: both)",
    )
    parser.add_argument("--output", type=Path, help="new output directory")
    parser.add_argument(
        "--dry-run", action="store_true", help="show the resolved plan without writing"
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="fail instead of prompting for missing generation arguments",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {GENERATOR_VERSION}"
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    arguments = sys.argv[1:] if argv is None else argv
    parser = build_parser()
    args = parser.parse_args(arguments)
    try:
        manifests = validate_and_load_manifests()
        if args.list:
            list_manifests(manifests)
            return 0
        if args.describe:
            if args.describe not in manifests:
                raise PackError(f"unknown Starter Pack: {args.describe}")
            describe_manifest(manifests[args.describe])
            return 0

        if not arguments:
            manifest, platform, output = interactive_selection(manifests)
        else:
            if not args.pack:
                parser.error("--pack is required for generation")
            if args.pack not in manifests:
                raise PackError(f"unknown Starter Pack: {args.pack}")
            if not args.output:
                if args.non_interactive:
                    raise PackError("--output is required with --non-interactive")
                args.output = Path.cwd() / f"{args.pack}-workspace"
            manifest, platform, output = manifests[args.pack], args.platform, args.output
        generate_pack(manifest, platform, output, args.dry_run)
        return 0
    except (PackError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
