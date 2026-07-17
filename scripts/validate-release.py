#!/usr/bin/env python3
"""Validate release metadata, package completeness, entry paths, and source traceability."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = 41
EXPECTED_COMMANDS = {
    "aipom-assess-organization.md",
    "aipom-evaluate-initiative.md",
    "aipom-redesign-workflow.md",
}
REQUIRED_FILES = {
    "VERSION",
    "CHANGELOG.md",
    "LICENSE",
    "README.md",
    "ROADMAP.md",
    "docs/RELEASE-PLAN.md",
    "docs/RELEASE-READINESS.md",
    "docs/STARTING-PATHS.md",
}


def split_skill(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        raise ValueError(f"{path.relative_to(ROOT)}: missing YAML frontmatter")
    return yaml.safe_load(match.group(1)) or {}, text[match.end() :]


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    missing_files = sorted(path for path in REQUIRED_FILES if not (ROOT / path).exists())
    if missing_files:
        errors.append(f"missing release files: {', '.join(missing_files)}")

    version = (ROOT / "VERSION").read_text().strip() if (ROOT / "VERSION").exists() else ""
    if not re.fullmatch(r"0\.\d+", version):
        errors.append("VERSION must use the pre-1.0 form 0.x")
    elif f"## [{version}] - Unreleased" not in (ROOT / "CHANGELOG.md").read_text():
        errors.append(f"CHANGELOG.md must contain an Unreleased section for {version}")

    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if len(skill_files) != EXPECTED_SKILLS:
        errors.append(f"expected {EXPECTED_SKILLS} skills, found {len(skill_files)}")

    source_urls = 0
    sourced_skills = 0
    for skill_file in skill_files:
        data, body = split_skill(skill_file)
        folder = skill_file.parent
        for relative in ["template.md", "examples/worked-example.md", "examples/weak-example.md"]:
            if not (folder / relative).exists():
                errors.append(f"{folder.relative_to(ROOT)}: missing {relative}")
        sources = data.get("sources", [])
        if sources:
            sourced_skills += 1
        for source in sources:
            source_urls += 1
            if not isinstance(source, str) or not source.startswith("https://"):
                errors.append(f"{skill_file.relative_to(ROOT)}: source must be an HTTPS URL")
            elif source not in body:
                errors.append(f"{skill_file.relative_to(ROOT)}: frontmatter source is not cited in the Sources section: {source}")
        worked = folder / "examples" / "worked-example.md"
        if worked.exists() and "synthetic" not in worked.read_text().lower():
            warnings.append(f"{worked.relative_to(ROOT)}: confirm that the example is visibly labeled synthetic")

    command_files = {path.name for path in (ROOT / "commands").glob("aipom-*.md")}
    if command_files != EXPECTED_COMMANDS:
        errors.append(
            "entry-path commands do not match expected set: "
            + ", ".join(sorted(EXPECTED_COMMANDS))
        )

    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")

    if errors:
        print(f"Release validation failed with {len(errors)} error(s).")
        return 1

    print(
        f"Validated release {version}: {len(skill_files)} skills, "
        f"{len(command_files)} entry paths, {source_urls} source URL(s) across {sourced_skills} skill(s)."
    )
    if warnings:
        print(f"Release validation completed with {len(warnings)} example-label warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
