#!/usr/bin/env python3
"""Run synthetic clean-room cold-start checks against released Starter Pack ZIPs."""

from __future__ import annotations

import hashlib
import importlib.util
import tempfile
import zipfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
CATALOG = ROOT / "catalog" / "starter-packs-index.yaml"
REPORT = DIST / "STARTER-PACK-COLD-START.yaml"
BUILDER_PATH = ROOT / "scripts" / "build-starter-pack-release.py"

FIRST_MOTIONS = {
    "head-of-product-direction": "Bound the product-direction decision, decision owner, horizon, and consequence before drafting a strategy thesis.",
    "cto-technical-readiness": "Define the consequence classes that require different technical evidence and recovery expectations.",
    "product-operations-assessment": "Bound the organizational assessment and establish what evidence and perspectives already exist.",
    "product-manager-initiative": "Frame the opportunity and current condition before evaluating the proposed AI initiative.",
    "team-lead-workflow": "Choose one recurring decision or productive motion and establish its observed baseline before redesigning it.",
}


def load_builder():
    spec = importlib.util.spec_from_file_location("build_starter_pack_release", BUILDER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load the Starter Pack release builder")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def inspect_pack(pack: dict, builder) -> dict:
    pack_id = pack["id"]
    archive_root = f"aipom-starter-pack-{pack_id}-v{VERSION}"
    archive = DIST / f"{archive_root}.zip"
    require(archive.is_file(), f"missing archive: {archive.relative_to(ROOT)}")
    manifest = yaml.safe_load((ROOT / pack["manifest"]).read_text(encoding="utf-8"))

    with tempfile.TemporaryDirectory(prefix=f"cold-start-{pack_id}-") as temporary:
        destination = Path(temporary)
        with zipfile.ZipFile(archive) as bundle:
            require(bundle.testzip() is None, f"{archive.name}: archive integrity failed")
            require(
                all(builder.safe_member(name, archive_root) for name in bundle.namelist()),
                f"{archive.name}: unsafe or unexpected archive member",
            )
            bundle.extractall(destination)

        project = destination / archive_root
        readme = (project / "README.md").read_text(encoding="utf-8")
        agents = (project / "AGENTS.md").read_text(encoding="utf-8")
        claude = (project / "CLAUDE.md").read_text(encoding="utf-8")
        codex_skill = (
            project / ".agents" / "skills" / "aipom-start" / "SKILL.md"
        ).read_text(encoding="utf-8")
        claude_skill = (
            project / ".claude" / "skills" / "aipom-start" / "SKILL.md"
        ).read_text(encoding="utf-8")
        codex_metadata = yaml.safe_load(
            (
                project
                / ".agents"
                / "skills"
                / "aipom-start"
                / "agents"
                / "openai.yaml"
            ).read_text(encoding="utf-8")
        )
        lock = yaml.safe_load((project / "PACK-LOCK.yaml").read_text(encoding="utf-8"))

        require(manifest["title"] in readme, f"{pack_id}: README does not identify the pack")
        require(manifest["persona"] in readme, f"{pack_id}: README does not identify the persona")
        require(manifest["scenario"]["decision"] in readme, f"{pack_id}: README omits the decision")
        require(manifest["completion"]["authority_boundary"] in readme, f"{pack_id}: README omits authority boundary")
        require("$aipom-start" in readme and "/aipom-start" in readme, f"{pack_id}: README omits native start commands")
        require("context/" in readme and "evidence/" in readme and "outputs/" in readme, f"{pack_id}: README omits workspace map")
        for output in manifest["completion"]["required_outputs"]:
            require(output in readme and output in agents, f"{pack_id}: required output is not visible: {output}")

        require(manifest["scenario"]["decision"] in agents, f"{pack_id}: working contract omits the decision")
        require("context-dump mode" in agents.lower(), f"{pack_id}: working contract omits context-dump mode")
        require("AGENTS.md" in claude, f"{pack_id}: CLAUDE.md does not route to the shared contract")
        require(codex_skill == claude_skill, f"{pack_id}: native start skills have drifted")
        require("Inspect `context/` and `evidence/`" in codex_skill, f"{pack_id}: start skill does not inspect supplied material")
        require("context-dump mode" in codex_skill.lower(), f"{pack_id}: start skill does not select a mode")
        require(
            codex_metadata["interface"]["default_prompt"].startswith("Use $aipom-start"),
            f"{pack_id}: Codex discovery prompt is incorrect",
        )

        require(lock["pack"]["id"] == pack_id, f"{pack_id}: lockfile id mismatch")
        require(lock["generation"]["platform"] == "both", f"{pack_id}: release is not cross-platform")
        locked_skills = sorted(item["name"] for item in lock["skills"])
        require(locked_skills == pack["resolved_skills"], f"{pack_id}: lockfile skill closure differs from catalog")
        for relative, expected in lock["generated_project_files"].items():
            path = project / relative
            require(path.is_file(), f"{pack_id}: locked project file is missing: {relative}")
            require(sha256(path) == expected, f"{pack_id}: locked project file changed: {relative}")

        journey = project / "library" / manifest["entrypoint"]["journey"]
        command = project / "library" / manifest["entrypoint"]["command"]
        require(journey.is_file() and command.is_file(), f"{pack_id}: journey or command is missing")

        synthetic_context = project / "context" / "SYNTHETIC-COLD-START.md"
        synthetic_evidence = project / "evidence" / "SYNTHETIC-EVIDENCE.md"
        synthetic_context.write_text(
            f"# Synthetic Cold Start\n\nPersona: {pack['persona']}\n\nTrigger: {manifest['scenario']['trigger']}\n",
            encoding="utf-8",
        )
        synthetic_evidence.write_text(
            "# Synthetic Evidence\n\nNo demonstrated organizational-use evidence is supplied. Treat all proposed conditions as assumptions.\n",
            encoding="utf-8",
        )
        require("context-dump mode" in codex_skill.lower(), f"{pack_id}: seeded context would not trigger context-dump guidance")

        return {
            "id": pack_id,
            "persona": pack["persona"],
            "archive": archive.name,
            "primary_skills": len(pack["primary_skills"]),
            "dependency_skills": len(pack["dependency_skills"]),
            "resolved_skills": len(pack["resolved_skills"]),
            "expected_first_motion": FIRST_MOTIONS[pack_id],
            "result": "pass",
            "checks": [
                "clean extraction",
                "persona and decision recognition",
                "plain-language start instructions",
                "context and evidence intake",
                "required outputs",
                "authority boundary",
                "Codex discovery",
                "Claude Code discovery",
                "lockfile integrity",
                "resolved dependency closure",
            ],
        }


def main() -> int:
    builder = load_builder()
    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    results = [inspect_pack(pack, builder) for pack in data["starter_packs"]]
    report = {
        "schema_version": 1,
        "library_version": VERSION,
        "evidence_type": "automated-synthetic-clean-room",
        "field_validation": False,
        "packs_tested": len(results),
        "result": "pass",
        "packs": results,
        "limitations": [
            "No representative human attempted the workflow.",
            "No Codex or Claude model response was evaluated.",
            "The checks establish packaging and cold-start instruction readiness, not decision quality, adoption, impact, or compliance.",
        ],
    }
    REPORT.write_text(yaml.safe_dump(report, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"Synthetic cold-start gate passed for {len(results)} Starter Packs.")
    for result in results:
        print(f"- {result['id']}: {result['resolved_skills']} skills, Codex + Claude Code")
    print(f"Wrote {REPORT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
