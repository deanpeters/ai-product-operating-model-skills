#!/usr/bin/env python3
"""Adapt canonical AIPOM skills to Codex-compatible skill packages."""

from __future__ import annotations

import re
import shutil
import zipfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text().strip()
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"
OUTPUT = DIST / "aipom-codex-skills"
ARCHIVE = DIST / f"aipom-codex-skills-v{VERSION}.zip"
STABLE_ARCHIVE = DIST / "aipom-codex-skills.zip"

INTERFACE = {
    "aipom-autonomy-boundary-designer": {
        "display_name": "Autonomy Boundary Designer",
        "short_description": "Set accountable boundaries for AI autonomy",
        "default_prompt": "Use $aipom-autonomy-boundary-designer to define what this AI system may do independently, with approval, or never.",
    },
    "aipom-strategy-thesis-advisor": {
        "display_name": "AI Strategy Thesis Advisor",
        "short_description": "Turn AI ambition into strategic choices",
        "default_prompt": "Use $aipom-strategy-thesis-advisor to develop an evidence-aware AI product strategy thesis.",
    },
    "aipom-operating-model-assessment": {
        "display_name": "AIPOM Operating Model Assessment",
        "short_description": "Assess AI product operating-model maturity",
        "default_prompt": "Use $aipom-operating-model-assessment to assess our current operating model and identify the next consequential intervention.",
    },
}


def split_skill(text: str) -> tuple[dict, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        raise ValueError("Missing canonical frontmatter")
    return yaml.safe_load(match.group(1)), text[match.end() :]


def quoted(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def derived_interface(name: str, description: str, body: str) -> dict[str, str]:
    heading = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    display_name = heading.group(1).removeprefix("AIPOM ") if heading else name.replace("-", " ").title()
    first_sentence = description.split(".", 1)[0].strip()
    short_description = first_sentence
    if len(short_description) > 64:
        short_description = short_description[:61].rsplit(" ", 1)[0] + "..."
    default_prompt = f"Use ${name} to {first_sentence[:1].lower() + first_sentence[1:]}."
    return {
        "display_name": display_name,
        "short_description": short_description,
        "default_prompt": default_prompt,
    }


def adapt_skill(source: Path) -> None:
    data, body = split_skill((source / "SKILL.md").read_text())
    name = data["name"]
    target = OUTPUT / name
    shutil.copytree(source, target)

    body = body.replace(
        "../../assessments/aipom-operating-model-assessment.md",
        "references/aipom-operating-model-assessment.md",
    ).replace(
        "../../assessments/evidence-rubric.md",
        "references/evidence-rubric.md",
    ).replace(
        "../../assessments/scoring-model.md",
        "references/scoring-model.md",
    )

    codex_frontmatter = {
        "name": name,
        "description": data["description"],
        "license": "CC-BY-NC-SA-4.0",
    }
    rendered_frontmatter = yaml.safe_dump(codex_frontmatter, sort_keys=False, allow_unicode=True).strip()
    (target / "SKILL.md").write_text(f"---\n{rendered_frontmatter}\n---\n\n{body}")

    if name == "aipom-operating-model-assessment":
        references = target / "references"
        references.mkdir()
        for filename in [
            "aipom-operating-model-assessment.md",
            "evidence-rubric.md",
            "scoring-model.md",
        ]:
            shutil.copy2(ROOT / "assessments" / filename, references / filename)

    interface = INTERFACE.get(name) or derived_interface(name, data["description"], body)
    agents = target / "agents"
    agents.mkdir()
    content = ["interface:"]
    for key in ["display_name", "short_description", "default_prompt"]:
        content.append(f"  {key}: {quoted(interface[key])}")
    (agents / "openai.yaml").write_text("\n".join(content) + "\n")


def main() -> int:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    if ARCHIVE.exists():
        ARCHIVE.unlink()
    if STABLE_ARCHIVE.exists():
        STABLE_ARCHIVE.unlink()
    OUTPUT.mkdir(parents=True)

    skill_dirs = sorted(path.parent for path in SKILLS.glob("*/SKILL.md"))
    for source in skill_dirs:
        adapt_skill(source)

    for filename in ["README.md", "LICENSE", "CITATION.cff", "SECURITY.md"]:
        shutil.copy2(ROOT / filename, OUTPUT / filename)

    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for path in sorted(OUTPUT.rglob("*")):
            if path.is_file():
                bundle.write(path, path.relative_to(DIST))

    shutil.copy2(ARCHIVE, STABLE_ARCHIVE)
    print(f"Built Codex packages for {len(skill_dirs)} skill(s): {ARCHIVE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
