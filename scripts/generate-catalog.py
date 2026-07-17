#!/usr/bin/env python3
"""Generate AIPOM catalog navigation from canonical SKILL.md metadata."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
CATALOG = ROOT / "catalog"

CATEGORY_LABELS = {
    "strategy-and-economic-outcomes": "Strategy and Economic Outcomes",
    "portfolio-and-investment-choices": "Portfolio and Investment Choices",
    "product-team-workflows": "Product-Team Workflows",
    "context-knowledge-and-data": "Context, Knowledge, and Data",
    "evaluation-and-evidence": "Evaluation and Evidence",
    "governance-and-accountability": "Governance and Accountability",
    "capability-adoption-and-reuse": "Capability, Adoption, and Reuse",
    "cross-category": "Cross-Category",
}

TARGET_PERSONAS = ["Product Operations", "Product Manager", "Team Lead"]


def load_skills() -> list[dict]:
    records: list[dict] = []
    for path in sorted(SKILLS.glob("*/SKILL.md")):
        text = path.read_text()
        match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
        if not match:
            continue
        data = yaml.safe_load(match.group(1)) or {}
        data["path"] = str(path.relative_to(ROOT))
        records.append(data)
    return sorted(records, key=lambda item: (item.get("phase", 99), item.get("category", ""), item.get("name", "")))


def link(record: dict) -> str:
    return f"[`{record['name']}`](../{record['path']})"


def generate_index(records: list[dict]) -> str:
    active = sum(record.get("status") == "active" for record in records)
    library_status = "Complete library: 41 active skills" if active == 41 else "Planned library: 41 skills"
    return "\n".join([
        "# AIPOM Skill Catalog",
        "",
        "This directory is generated from canonical skill metadata. Do not edit generated catalog files directly.",
        "",
        f"- Skills present: {len(records)}",
        f"- Active skills: {active}",
        f"- {library_status}",
        "",
        "Browse by [category](skills-by-category.md), [type](skills-by-type.md), [phase](skills-by-phase.md), or [target persona](skills-by-persona.md).",
        "",
    ])


def grouped_page(title: str, records: list[dict], key: str, labels: dict | None = None) -> str:
    groups: dict[object, list[dict]] = defaultdict(list)
    for record in records:
        groups[record.get(key, "unspecified")].append(record)
    lines = [f"# {title}", "", "Generated from canonical `SKILL.md` metadata. Do not edit directly.", ""]
    if not groups:
        lines.extend(["No skills have been added yet.", ""])
        return "\n".join(lines)
    for group in sorted(groups, key=str):
        label = labels.get(group, str(group).replace("-", " ").title()) if labels else str(group).replace("-", " ").title()
        lines.extend([f"## {label}", "", "| Skill | Description | Status |", "|---|---|---|"])
        for record in groups[group]:
            lines.append(f"| {link(record)} | {record.get('description', '')} | {record.get('status', '')} |")
        lines.append("")
    return "\n".join(lines)


def persona_page(records: list[dict]) -> str:
    lines = [
        "# Skills by Target Persona",
        "",
        "Generated from canonical `SKILL.md` audience metadata. Do not edit directly.",
        "",
        "Audience inclusion means the role performs, coordinates, decides, facilitates, or acts on the skill. It does not transfer specialist or executive authority.",
        "",
    ]
    for persona in TARGET_PERSONAS:
        matches = [record for record in records if persona in record.get("audience", [])]
        lines.extend([
            f"## {persona}",
            "",
            f"{len(matches)} of {len(records)} skills identify this persona in their audience metadata.",
            "",
            "| Skill | Description | Type |",
            "|---|---|---|",
        ])
        for record in matches:
            lines.append(f"| {link(record)} | {record.get('description', '')} | {record.get('type', '')} |")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    records = load_skills()
    CATALOG.mkdir(parents=True, exist_ok=True)
    (CATALOG / "INDEX.md").write_text(generate_index(records))
    (CATALOG / "skills-index.yaml").write_text(yaml.safe_dump({"skills": records}, sort_keys=False, allow_unicode=True))
    (CATALOG / "skills-by-category.md").write_text(grouped_page("Skills by Category", records, "category", CATEGORY_LABELS))
    (CATALOG / "skills-by-type.md").write_text(grouped_page("Skills by Type", records, "type"))
    (CATALOG / "skills-by-persona.md").write_text(persona_page(records))
    phase_labels = {1: "Phase 1", 2: "Phase 2", 3: "Phase 3", 4: "Phase 4"}
    (CATALOG / "skills-by-phase.md").write_text(grouped_page("Skills by Phase", records, "phase", phase_labels))
    print(f"Generated catalog for {len(records)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
