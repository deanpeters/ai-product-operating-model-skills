#!/usr/bin/env python3
"""Validate the repository-root Claude Code plugin and marketplace contract."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_PATH = ROOT / ".claude-plugin" / "plugin.json"
MARKETPLACE_PATH = ROOT / ".claude-plugin" / "marketplace.json"
EXPECTED_SKILLS = 41
EXPECTED_COMMANDS = 5


def load_json(path: Path, errors: list[str]) -> dict:
    if not path.is_file():
        errors.append(f"missing {path.relative_to(ROOT)}")
        return {}
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return {}


def main() -> int:
    errors: list[str] = []
    plugin = load_json(PLUGIN_PATH, errors)
    marketplace = load_json(MARKETPLACE_PATH, errors)

    version = (ROOT / "VERSION").read_text().strip()
    plugin_version = f"{version}.0"

    if plugin.get("name") != "aipom":
        errors.append("plugin.json name must be 'aipom'")
    if plugin.get("version") != plugin_version:
        errors.append(
            f"plugin.json version must be {plugin_version} to match VERSION={version}"
        )

    if marketplace.get("name") != "aipom-skills":
        errors.append("marketplace.json name must be 'aipom-skills'")
    if marketplace.get("metadata", {}).get("version") != plugin_version:
        errors.append(
            f"marketplace metadata version must be {plugin_version} to match VERSION={version}"
        )

    entries = marketplace.get("plugins", [])
    if len(entries) != 1:
        errors.append("marketplace.json must expose exactly one complete AIPOM plugin")
    elif entries[0].get("name") != "aipom" or entries[0].get("source") != ".":
        errors.append("marketplace plugin must be named 'aipom' with repository-root source '.'")
    elif entries[0].get("version") != plugin_version:
        errors.append(
            f"marketplace plugin version must be {plugin_version} to match VERSION={version}"
        )

    skill_count = len(list((ROOT / "skills").glob("*/SKILL.md")))
    if skill_count != EXPECTED_SKILLS:
        errors.append(f"expected {EXPECTED_SKILLS} plugin skills, found {skill_count}")

    command_count = len(list((ROOT / "commands").glob("aipom-*.md")))
    if command_count != EXPECTED_COMMANDS:
        errors.append(f"expected {EXPECTED_COMMANDS} plugin commands, found {command_count}")

    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"Claude plugin validation failed with {len(errors)} error(s).")
        return 1

    print(
        f"Validated Claude plugin {plugin_version}: "
        f"{skill_count} skills and {command_count} workflow commands."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
