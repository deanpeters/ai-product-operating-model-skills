#!/usr/bin/env python3
"""Validate canonical AIPOM skill metadata, structure, and references."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Run: python3 -m pip install -r requirements-dev.txt")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
ASSESSMENT = ROOT / "assessments" / "aipom-operating-model-assessment.md"
ROADMAP = ROOT / "ROADMAP.md"

REQUIRED_FIELDS = {
    "name",
    "description",
    "type",
    "category",
    "phase",
    "status",
    "operating_level",
    "audience",
    "best_for",
    "evidence_required",
    "produces",
    "assessment_questions",
    "maturity_move",
    "estimated_time",
    "group_size",
    "depends_on",
    "combine_with",
    "sources",
}

NONEMPTY_LIST_FIELDS = {
    "operating_level",
    "audience",
    "best_for",
    "evidence_required",
    "produces",
    "assessment_questions",
}

LIST_FIELDS = NONEMPTY_LIST_FIELDS | {"depends_on", "combine_with", "sources"}

TYPES = {"component", "interactive", "workflow"}
CATEGORIES = {
    "strategy-and-economic-outcomes",
    "portfolio-and-investment-choices",
    "product-team-workflows",
    "context-knowledge-and-data",
    "evaluation-and-evidence",
    "governance-and-accountability",
    "capability-adoption-and-reuse",
    "cross-category",
}
STATUSES = {"planned", "drafting", "review", "active"}
OPERATING_LEVELS = {"organization", "portfolio", "product-team", "initiative"}
MATURITY = {"absent", "emerging", "repeatable", "operationalized", "compounding"}

BASE_SECTIONS = [
    "What Is It",
    "Why Use It",
    "When to Use It",
    "What It Produces",
    "Who Should Participate",
    "Evidence to Bring",
    "How to Do It",
    "Key Concepts",
    "Organizational Applications",
    "Common Pitfalls",
    "Combine With",
    "Assets and Templates",
    "Sources",
]

ADAPTIVE_SECTIONS = ["Facilitation Protocol", "Decision Logic", "Completion Criteria"]


def frontmatter(text: str, path: Path) -> tuple[dict, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        raise ValueError(f"{path}: missing YAML frontmatter")
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"{path}: invalid YAML frontmatter: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path}: frontmatter must be a mapping")
    return data, text[match.end() :]


def assessment_ids() -> set[str]:
    if not ASSESSMENT.exists():
        return set()
    return set(re.findall(r"\|\s*((?:STR|POR|WFL|CTX|EVAL|GOV|CAP)-\d{2})\s*\|", ASSESSMENT.read_text()))


def validate_skill(path: Path, valid_ids: set[str], roadmap_text: str) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(ROOT)
    try:
        data, body = frontmatter(path.read_text(), relative)
    except ValueError as exc:
        return [str(exc)]

    missing = sorted(REQUIRED_FIELDS - data.keys())
    if missing:
        errors.append(f"{relative}: missing fields: {', '.join(missing)}")

    name = data.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append(f"{relative}: name must be lowercase kebab-case")
    else:
        if name != path.parent.name:
            errors.append(f"{relative}: name must match folder '{path.parent.name}'")
        if len(name) > 64:
            errors.append(f"{relative}: name exceeds 64 characters")
        if f"`{name}`" not in roadmap_text:
            errors.append(f"{relative}: name is not listed in ROADMAP.md")
        else:
            roadmap_row = re.search(
                rf"^\|[^\n|]+\|\s*`{re.escape(name)}`\s*\|[^\n|]+\|\s*([^\s|]+)\s*\|$",
                roadmap_text,
                re.MULTILINE,
            )
            if roadmap_row and data.get("status") != roadmap_row.group(1):
                errors.append(
                    f"{relative}: status '{data.get('status')}' does not match "
                    f"ROADMAP.md status '{roadmap_row.group(1)}'"
                )

    description = data.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{relative}: description must be non-empty text")
    elif len(description) > 200:
        errors.append(f"{relative}: description exceeds 200 characters")

    if data.get("type") not in TYPES:
        errors.append(f"{relative}: invalid type '{data.get('type')}'")
    if data.get("category") not in CATEGORIES:
        errors.append(f"{relative}: invalid category '{data.get('category')}'")
    if data.get("status") not in STATUSES:
        errors.append(f"{relative}: invalid status '{data.get('status')}'")
    if data.get("phase") not in {1, 2, 3, 4}:
        errors.append(f"{relative}: phase must be an integer from 1 to 4")

    for field in LIST_FIELDS:
        value = data.get(field)
        if not isinstance(value, list):
            errors.append(f"{relative}: {field} must be a YAML list")
        elif field in NONEMPTY_LIST_FIELDS and not value:
            errors.append(f"{relative}: {field} must not be empty")

    levels = data.get("operating_level", [])
    if isinstance(levels, list):
        invalid = sorted(set(levels) - OPERATING_LEVELS)
        if invalid:
            errors.append(f"{relative}: invalid operating levels: {', '.join(invalid)}")

    questions = data.get("assessment_questions", [])
    if isinstance(questions, list):
        invalid = sorted(set(questions) - valid_ids)
        if invalid:
            errors.append(f"{relative}: unknown assessment IDs: {', '.join(invalid)}")

    move = data.get("maturity_move")
    if not isinstance(move, dict) or set(move) != {"from", "to"}:
        errors.append(f"{relative}: maturity_move must contain exactly 'from' and 'to'")
    elif move["from"] not in MATURITY or move["to"] not in MATURITY:
        errors.append(f"{relative}: maturity_move uses an invalid maturity label")

    for field in ("depends_on", "combine_with"):
        refs = data.get(field, [])
        if isinstance(refs, list):
            for ref in refs:
                if not isinstance(ref, str):
                    errors.append(f"{relative}: {field} values must be skill names")
                elif not (SKILLS_DIR / ref / "SKILL.md").exists() and f"`{ref}`" not in roadmap_text:
                    errors.append(f"{relative}: unresolved {field} reference '{ref}'")

    headings = [(match.group(1), match.start()) for match in re.finditer(r"^## (.+?)\s*$", body, re.MULTILINE)]
    positions = {heading: position for heading, position in headings}
    missing_sections = [section for section in BASE_SECTIONS if section not in positions]
    if missing_sections:
        errors.append(f"{relative}: missing sections: {', '.join(missing_sections)}")
    present_base = [positions[section] for section in BASE_SECTIONS if section in positions]
    if present_base != sorted(present_base):
        errors.append(f"{relative}: required sections are out of order")

    if data.get("type") in {"interactive", "workflow"}:
        missing_adaptive = [section for section in ADAPTIVE_SECTIONS if section not in positions]
        if missing_adaptive:
            errors.append(f"{relative}: missing adaptive sections: {', '.join(missing_adaptive)}")
        elif "How to Do It" in positions and "Key Concepts" in positions:
            for section in ADAPTIVE_SECTIONS:
                if not positions["How to Do It"] < positions[section] < positions["Key Concepts"]:
                    errors.append(f"{relative}: {section} must appear between How to Do It and Key Concepts")

    if not re.search(r"^# (?!#).+", body, re.MULTILINE):
        errors.append(f"{relative}: missing H1 skill title")

    if data.get("status") == "active":
        worked = path.parent / "examples" / "worked-example.md"
        if not worked.exists():
            errors.append(f"{relative}: active skill requires examples/worked-example.md")
        if data.get("type") == "component" and not (path.parent / "template.md").exists():
            errors.append(f"{relative}: active component requires template.md")

    return errors


def main() -> int:
    valid_ids = assessment_ids()
    if len(valid_ids) != 35:
        print(f"ERROR: canonical assessment contains {len(valid_ids)} stable IDs; expected 35")
        return 1
    roadmap_text = ROADMAP.read_text() if ROADMAP.exists() else ""
    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))
    errors: list[str] = []
    for path in skill_files:
        errors.extend(validate_skill(path, valid_ids, roadmap_text))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Validation failed with {len(errors)} error(s).")
        return 1

    print(f"Validated {len(skill_files)} skill(s) and 35 assessment IDs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
