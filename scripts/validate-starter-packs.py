#!/usr/bin/env python3
"""Validate canonical AIPOM Starter Pack manifests and dependency closure."""

from __future__ import annotations

import re
from pathlib import Path, PurePosixPath

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = ROOT / "starter-packs" / "manifests"
SCHEMA = ROOT / "starter-packs" / "schema" / "starter-pack.schema.yaml"
SKILLS = ROOT / "skills"
STARTER_PACK_README = ROOT / "starter-packs" / "README.md"
STARTER_PACK_CONTRACT = ROOT / "docs" / "STARTER-PACKS.md"

FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def load_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: expected a YAML mapping")
    return data


def load_skills() -> dict[str, dict]:
    records: dict[str, dict] = {}
    for path in sorted(SKILLS.glob("*/SKILL.md")):
        match = FRONTMATTER.match(path.read_text())
        if not match:
            raise ValueError(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        data = yaml.safe_load(match.group(1)) or {}
        name = data.get("name")
        if not isinstance(name, str):
            raise ValueError(f"{path.relative_to(ROOT)}: missing skill name")
        records[name] = data
    return records


def format_schema_error(path: Path, error) -> str:
    location = ".".join(str(part) for part in error.absolute_path) or "manifest"
    return f"{path.relative_to(ROOT)}: {location}: {error.message}"


def repository_path_error(value: str) -> str | None:
    pure = PurePosixPath(value)
    if pure.is_absolute() or ".." in pure.parts or "\\" in value:
        return "must be a normalized repository-relative POSIX path"
    target = (ROOT / pure).resolve()
    if not target.is_relative_to(ROOT.resolve()):
        return "resolves outside the repository"
    if not target.is_file():
        return "does not resolve to a repository file"
    return None


def dependency_closure(
    roots: list[str], skills: dict[str, dict]
) -> tuple[set[str], list[str]]:
    resolved: set[str] = set()
    visiting: list[str] = []
    errors: list[str] = []

    def visit(name: str) -> None:
        if name in resolved:
            return
        if name in visiting:
            cycle = " -> ".join(visiting[visiting.index(name) :] + [name])
            errors.append(f"dependency cycle: {cycle}")
            return
        record = skills.get(name)
        if record is None:
            errors.append(f"unknown skill '{name}'")
            return
        visiting.append(name)
        dependencies = record.get("depends_on", [])
        if not isinstance(dependencies, list):
            errors.append(f"{name}: depends_on must be a list")
        else:
            for dependency in dependencies:
                if not isinstance(dependency, str):
                    errors.append(f"{name}: dependency names must be strings")
                else:
                    visit(dependency)
        visiting.pop()
        resolved.add(name)

    for root in roots:
        visit(root)
    return resolved, errors


def documented_total(path: Path, key: str) -> int | None:
    for line in path.read_text().splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.split("|")[1:-1]]
        if len(cells) >= 3 and key in cells[0] and cells[2].isdigit():
            return int(cells[2])
    return None


def validate_documented_total(data: dict, resolved: set[str]) -> list[str]:
    errors: list[str] = []
    checks = [
        (STARTER_PACK_README, f"`{data['id']}`"),
        (STARTER_PACK_CONTRACT, data["title"]),
    ]
    for path, key in checks:
        total = documented_total(path, key)
        relative = path.relative_to(ROOT)
        if total is None:
            errors.append(f"{relative}: missing numeric total for {key}")
        elif total != len(resolved):
            errors.append(
                f"{relative}: {key} documents {total} resolved skills; manifest resolves {len(resolved)}"
            )
    return errors


def validate_manifest(
    path: Path,
    data: dict,
    schema_validator: Draft202012Validator,
    skills: dict[str, dict],
) -> tuple[list[str], set[str]]:
    errors = [
        format_schema_error(path, error)
        for error in sorted(
            schema_validator.iter_errors(data),
            key=lambda item: tuple(str(part) for part in item.absolute_path),
        )
    ]
    if errors:
        return errors, set()

    pack_id = data["id"]
    if path.stem != pack_id:
        errors.append(
            f"{path.relative_to(ROOT)}: filename must match manifest id '{pack_id}'"
        )

    repository_paths = [
        data["entrypoint"]["persona_guide"],
        data["entrypoint"]["journey"],
        data["entrypoint"]["command"],
        *data["supporting_content"],
        data["license"]["file"],
    ]
    for value in repository_paths:
        message = repository_path_error(value)
        if message:
            errors.append(f"{path.relative_to(ROOT)}: '{value}' {message}")

    mutable_paths = [
        *data["workspace"]["input_directories"],
        *data["workspace"]["output_directories"],
        *data["workspace"]["ledgers"],
    ]
    for value in mutable_paths:
        pure = PurePosixPath(value)
        if pure.is_absolute() or ".." in pure.parts or "\\" in value:
            errors.append(
                f"{path.relative_to(ROOT)}: workspace path '{value}' must be normalized and relative"
            )
    if len(mutable_paths) != len(set(mutable_paths)):
        errors.append(f"{path.relative_to(ROOT)}: workspace paths must not overlap by name")

    explicit = data["skills"]["include"]
    resolved, dependency_errors = dependency_closure(explicit, skills)
    for message in dependency_errors:
        errors.append(f"{path.relative_to(ROOT)}: {message}")

    return errors, resolved


def main() -> int:
    if not SCHEMA.is_file():
        print("ERROR: missing starter-packs/schema/starter-pack.schema.yaml")
        return 1

    try:
        schema = load_yaml(SCHEMA)
        Draft202012Validator.check_schema(schema)
        schema_validator = Draft202012Validator(schema)
        skills = load_skills()
    except (ValueError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}")
        return 1

    manifest_paths = sorted(MANIFESTS.glob("*.yaml"))
    if not manifest_paths:
        print("ERROR: no Starter Pack manifests found")
        return 1

    errors: list[str] = []
    ids: dict[str, Path] = {}
    summaries: list[str] = []

    for path in manifest_paths:
        try:
            data = load_yaml(path)
        except (ValueError, yaml.YAMLError) as exc:
            errors.append(str(exc))
            continue

        pack_id = data.get("id")
        if isinstance(pack_id, str):
            if pack_id in ids:
                errors.append(
                    f"{path.relative_to(ROOT)}: duplicate id also used by {ids[pack_id].relative_to(ROOT)}"
                )
            else:
                ids[pack_id] = path

        manifest_errors, resolved = validate_manifest(
            path, data, schema_validator, skills
        )
        errors.extend(manifest_errors)
        if not manifest_errors:
            errors.extend(validate_documented_total(data, resolved))
            summaries.append(
                f"{data['id']} ({len(data['skills']['include'])} explicit, {len(resolved)} resolved skills)"
            )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"Validated {len(manifest_paths)} Starter Pack manifest(s):")
    for summary in summaries:
        print(f"- {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
