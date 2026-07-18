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
STARTER_PACK_MANIFESTS = ROOT / "starter-packs" / "manifests"

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

TARGET_PERSONAS = {
    "Head of Product": {"Head of Product", "CPO", "VP Product"},
    "CTO": {"CTO"},
    "Product Operations": {"Product Operations"},
    "Product Manager": {"Product Manager"},
    "Team Lead": {"Team Lead"},
}

STARTER_PACK_ORDER = {
    "head-of-product-direction": 1,
    "cto-technical-readiness": 2,
    "product-operations-assessment": 3,
    "product-manager-initiative": 4,
    "team-lead-workflow": 5,
}


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


def resolve_dependencies(roots: list[str], skills: dict[str, dict]) -> set[str]:
    resolved: set[str] = set()
    visiting: list[str] = []

    def visit(name: str) -> None:
        if name in resolved:
            return
        if name in visiting:
            cycle = " -> ".join(visiting[visiting.index(name) :] + [name])
            raise ValueError(f"Starter Pack dependency cycle: {cycle}")
        record = skills.get(name)
        if record is None:
            raise ValueError(f"Starter Pack references unknown skill '{name}'")
        visiting.append(name)
        for dependency in record.get("depends_on", []):
            visit(dependency)
        visiting.pop()
        resolved.add(name)

    for root in roots:
        visit(root)
    return resolved


def load_starter_packs(records: list[dict]) -> list[dict]:
    skills = {record["name"]: record for record in records}
    packs: list[dict] = []
    for path in sorted(STARTER_PACK_MANIFESTS.glob("*.yaml")):
        data = yaml.safe_load(path.read_text()) or {}
        primary = data.get("skills", {}).get("include", [])
        resolved = resolve_dependencies(primary, skills)
        packs.append({
            "id": data["id"],
            "version": data["version"],
            "title": data["title"],
            "persona": data["persona"],
            "description": data["description"],
            "decision": data["scenario"]["decision"],
            "result": data["completion"]["result"],
            "manifest": str(path.relative_to(ROOT)),
            "primary_skills": sorted(primary),
            "dependency_skills": sorted(resolved - set(primary)),
            "resolved_skills": sorted(resolved),
        })
    return sorted(packs, key=lambda pack: (STARTER_PACK_ORDER.get(pack["id"], 99), pack["id"]))


def link(record: dict) -> str:
    return f"[`{record['name']}`](../{record['path']})"


def generate_index(records: list[dict], packs: list[dict]) -> str:
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
        "Browse skills by [category](skills-by-category.md), [type](skills-by-type.md), [phase](skills-by-phase.md), or [target persona](skills-by-persona.md).",
        "",
        f"Compare the {len(packs)} generated working-project recipes in [Skills by Starter Pack](skills-by-starter-pack.md).",
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
    for persona, aliases in TARGET_PERSONAS.items():
        matches = [
            record
            for record in records
            if aliases.intersection(record.get("audience", []))
        ]
        alias_note = ""
        if persona == "Head of Product":
            alias_note = " This role family includes CPO, SVP of Product, and equivalent senior product authorities."
        elif persona == "CTO":
            alias_note = " This role family includes equivalent accountable senior technology executives."
        lines.extend([
            f"## {persona}",
            "",
            f"{len(matches)} of {len(records)} skills identify this persona or an equivalent role in their audience metadata.{alias_note}",
            "",
            "| Skill | Description | Type |",
            "|---|---|---|",
        ])
        for record in matches:
            lines.append(f"| {link(record)} | {record.get('description', '')} | {record.get('type', '')} |")
        lines.append("")
    return "\n".join(lines)


def starter_pack_page(records: list[dict], packs: list[dict]) -> str:
    lines = [
        "# Skills by Starter Pack",
        "",
        "Generated from canonical Starter Pack manifests and each skill's `depends_on` metadata. Do not edit directly.",
        "",
        "Starter Packs share a working-project shell, but each pack contains a different job-specific method set. `P` means the manifest selects the skill as a primary method. `D` means the skill is included as a required dependency. A blank cell means the skill is not packaged.",
        "",
        "## Package Summary",
        "",
        "| Starter Pack | Persona | Primary | Dependencies | Total | Decision |",
        "|---|---|---:|---:|---:|---|",
    ]
    for pack in packs:
        lines.append(
            f"| {pack['title']} (`{pack['manifest']}`) | {pack['persona']} | "
            f"{len(pack['primary_skills'])} | {len(pack['dependency_skills'])} | "
            f"{len(pack['resolved_skills'])} | {pack['decision']} |"
        )

    lines.extend([
        "",
        "## Skill Membership Matrix",
        "",
        "| Skill | " + " | ".join(pack["persona"] for pack in packs) + " |",
        "|---|" + "---:|" * len(packs),
    ])
    membership = {
        pack["id"]: {
            **{name: "D" for name in pack["dependency_skills"]},
            **{name: "P" for name in pack["primary_skills"]},
        }
        for pack in packs
    }
    for record in sorted(records, key=lambda item: item["name"]):
        cells = [membership[pack["id"]].get(record["name"], "") for pack in packs]
        lines.append(f"| {link(record)} | " + " | ".join(cells) + " |")

    lines.extend([
        "",
        "## Source Boundary",
        "",
        "Package membership is intentionally not stored in skill frontmatter. The manifests own package composition; skill frontmatter owns reusable method metadata and dependency relationships. This generated view is the inverse index across those two canonical sources.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    records = load_skills()
    packs = load_starter_packs(records)
    CATALOG.mkdir(parents=True, exist_ok=True)
    (CATALOG / "INDEX.md").write_text(generate_index(records, packs))
    (CATALOG / "skills-index.yaml").write_text(yaml.safe_dump({"skills": records}, sort_keys=False, allow_unicode=True))
    (CATALOG / "starter-packs-index.yaml").write_text(yaml.safe_dump({"starter_packs": packs}, sort_keys=False, allow_unicode=True))
    (CATALOG / "skills-by-category.md").write_text(grouped_page("Skills by Category", records, "category", CATEGORY_LABELS))
    (CATALOG / "skills-by-type.md").write_text(grouped_page("Skills by Type", records, "type"))
    (CATALOG / "skills-by-persona.md").write_text(persona_page(records))
    (CATALOG / "skills-by-starter-pack.md").write_text(starter_pack_page(records, packs))
    phase_labels = {1: "Phase 1", 2: "Phase 2", 3: "Phase 3", 4: "Phase 4"}
    (CATALOG / "skills-by-phase.md").write_text(grouped_page("Skills by Phase", records, "phase", phase_labels))
    print(f"Generated catalog for {len(records)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
