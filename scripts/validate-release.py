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
    "aipom-establish-technical-readiness-bar.md",
    "aipom-evaluate-initiative.md",
    "aipom-redesign-workflow.md",
    "aipom-set-product-direction.md",
}
REPRESENTATIVE_SKILLS = {
    "aipom-operating-model-assessment",
    "aipom-strategy-thesis-advisor",
    "aipom-use-case-triage",
    "aipom-autonomy-boundary-designer",
    "aipom-initiative-readiness-review",
    "aipom-portfolio-quarterly-review",
}
VALIDATION_KIT = {
    "docs/validation/README.md",
    "docs/validation/v0.5-field-validation-plan.md",
    "docs/validation/v0.5-participant-brief.md",
    "docs/validation/v0.5-facilitator-runbook.md",
    "docs/validation/v0.5-session-capture.md",
    "docs/validation/v0.5-calibration-scenarios.md",
    "docs/validation/v0.5-findings-register.md",
    "docs/validation/v0.5-forward-test-report.md",
}
PUBLIC_PREVIEW_FILES = {
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/facilitation-feedback.yml",
    ".github/ISSUE_TEMPLATE/unsafe-recommendation.yml",
    ".github/ISSUE_TEMPLATE/field-session-report.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "CITATION.cff",
    "SECURITY.md",
    "docs/EVIDENCE-STATUS.md",
    "docs/PUBLIC-PREVIEW.md",
    "docs/POST-RELEASE-ROADMAP.md",
    "docs/releases/v0.5.md",
    "docs/releases/v0.5-release-audit.md",
}
PUBLIC_EXPERIENCE_FILES = {
    "docs/README.md",
    "docs/HANDOFF.md",
    "docs/TARGET-PERSONAS.md",
    "docs/personas/PRODUCT-OPERATIONS.md",
    "docs/personas/PRODUCT-MANAGER.md",
    "docs/personas/TEAM-LEAD.md",
    "docs/personas/HEAD-OF-PRODUCT.md",
    "docs/personas/CTO.md",
    "docs/journeys/ASSESS-AN-ORGANIZATION.md",
    "docs/journeys/EVALUATE-AN-AI-INITIATIVE.md",
    "docs/journeys/REDESIGN-A-PRODUCT-TEAM-WORKFLOW.md",
    "docs/journeys/SET-AI-PRODUCT-DIRECTION.md",
    "docs/journeys/ESTABLISH-AI-TECHNICAL-READINESS-BAR.md",
    "docs/adoption-packages/README.md",
    "docs/adoption-packages/EXECUTIVE-ALIGNMENT.md",
    "docs/adoption-packages/AI-INVESTMENT-DECISION.md",
    "docs/adoption-packages/INITIATIVE-READINESS.md",
    "docs/adoption-packages/HUMAN-AI-WORKFLOW-PILOT.md",
    "docs/adoption-packages/GOVERNANCE-AND-ACCOUNTABILITY.md",
    "docs/adoption-packages/QUARTERLY-AI-PORTFOLIO-REVIEW.md",
    "catalog/skills-by-persona.md",
    "catalog/skills-by-starter-pack.md",
    "catalog/starter-packs-index.yaml",
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
    "create-starter-pack.sh",
    "create-starter-pack.ps1",
    "scripts/build-starter-pack-release.py",
    "scripts/create-starter-pack.py",
    "scripts/test-starter-pack-cold-start.py",
    "scripts/validate-starter-packs.py",
    "starter-packs/README.md",
    "starter-packs/schema/starter-pack.schema.yaml",
    "docs/validation/starter-pack-cold-start-report.md",
} | VALIDATION_KIT | PUBLIC_PREVIEW_FILES | PUBLIC_EXPERIENCE_FILES


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
    elif not re.search(rf"^## \[{re.escape(version)}\] - \d{{4}}-\d{{2}}-\d{{2}}$", (ROOT / "CHANGELOG.md").read_text(), re.MULTILINE):
        errors.append(f"CHANGELOG.md must contain a dated release section for {version}")

    readme = (ROOT / "README.md").read_text() if (ROOT / "README.md").exists() else ""
    if "v0.5 public preview" not in readme or "synthetically forward-tested" not in readme:
        errors.append("README.md must display the v0.5 synthetic public-preview evidence label")

    evidence_status = ROOT / "docs" / "EVIDENCE-STATUS.md"
    if evidence_status.exists():
        evidence_text = evidence_status.read_text()
        for phrase in ["Human field validation", "Not yet completed", "Demonstrated organizational adoption", "Not established"]:
            if phrase not in evidence_text:
                errors.append(f"docs/EVIDENCE-STATUS.md is missing required disclosure: {phrase}")

    for issue_form in sorted((ROOT / ".github" / "ISSUE_TEMPLATE").glob("*.yml")):
        try:
            yaml.safe_load(issue_form.read_text())
        except yaml.YAMLError as exc:
            errors.append(f"{issue_form.relative_to(ROOT)}: invalid YAML: {exc}")

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
        if data.get("name") in REPRESENTATIVE_SKILLS:
            worked_words = len(worked.read_text().split()) if worked.exists() else 0
            weak = folder / "examples" / "weak-example.md"
            weak_words = len(weak.read_text().split()) if weak.exists() else 0
            if worked_words < 300:
                errors.append(f"{worked.relative_to(ROOT)}: representative worked example must contain at least 300 words")
            if weak_words < 120:
                errors.append(f"{weak.relative_to(ROOT)}: representative weak example must contain at least 120 words")

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
