"""Focused tests for the AIPOM Starter Pack generator."""

from __future__ import annotations

import importlib.util
import io
import shutil
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "create-starter-pack.py"
SPEC = importlib.util.spec_from_file_location("create_starter_pack", SCRIPT)
assert SPEC and SPEC.loader
generator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(generator)


class StarterPackGeneratorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifests = generator.validate_and_load_manifests()

    def test_dependency_closure_is_resolved(self) -> None:
        manifest = self.manifests["product-manager-initiative"]
        self.assertEqual(18, len(manifest["_resolved_skills"]))
        self.assertEqual(
            "dependency",
            manifest["_skill_inclusion"]["aipom-evaluation-strategy-advisor"],
        )
        self.assertEqual(
            "explicit", manifest["_skill_inclusion"]["aipom-initiative-readiness-review"]
        )

    def test_leadership_packs_are_bounded_and_dependency_complete(self) -> None:
        head_of_product = self.manifests["head-of-product-direction"]
        cto = self.manifests["cto-technical-readiness"]
        self.assertEqual("Head of Product", head_of_product["persona"])
        self.assertEqual(2, len(head_of_product["_resolved_skills"]))
        self.assertEqual("CTO", cto["persona"])
        self.assertEqual(14, len(cto["_resolved_skills"]))
        self.assertIn("aipom-platform-dependency-audit", cto["_resolved_skills"])
        self.assertIn("aipom-accountability-charter", cto["_resolved_skills"])

    def test_generates_platform_neutral_working_project(self) -> None:
        manifest = self.manifests["team-lead-workflow"]
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "team-lead-pack"
            with redirect_stdout(io.StringIO()):
                generator.generate_pack(manifest, "both", output, dry_run=False)

            self.assertTrue((output / "README.md").is_file())
            self.assertTrue((output / "AGENTS.md").is_file())
            self.assertTrue((output / "CLAUDE.md").is_file())
            self.assertTrue((output / "CONTEXT-LEDGER.md").is_file())
            self.assertTrue((output / "DECISION-LOG.md").is_file())
            self.assertTrue((output / "context" / "README.md").is_file())
            self.assertTrue((output / "evidence" / "README.md").is_file())
            self.assertTrue((output / "outputs" / "README.md").is_file())
            codex_skill = output / ".agents" / "skills" / "aipom-start" / "SKILL.md"
            claude_skill = output / ".claude" / "skills" / "aipom-start" / "SKILL.md"
            self.assertTrue(codex_skill.is_file())
            self.assertTrue(claude_skill.is_file())
            self.assertTrue(
                (
                    output
                    / ".agents"
                    / "skills"
                    / "aipom-start"
                    / "agents"
                    / "openai.yaml"
                ).is_file()
            )
            for skill in (codex_skill, claude_skill):
                match = generator.FRONTMATTER.match(skill.read_text())
                self.assertIsNotNone(match)
                metadata = yaml.safe_load(match.group(1))
                self.assertEqual("aipom-start", metadata["name"])

            lock = yaml.safe_load((output / "PACK-LOCK.yaml").read_text())
            self.assertEqual("team-lead-workflow", lock["pack"]["id"])
            self.assertEqual("both", lock["generation"]["platform"])
            self.assertEqual(6, len(lock["skills"]))
            self.assertGreater(generator.validate_generated_links(output), 0)

    def test_platform_selection_limits_native_adapters(self) -> None:
        manifest = self.manifests["product-operations-assessment"]
        with tempfile.TemporaryDirectory() as temporary:
            codex_output = Path(temporary) / "codex"
            claude_output = Path(temporary) / "claude"
            with redirect_stdout(io.StringIO()):
                generator.generate_pack(manifest, "codex", codex_output, dry_run=False)
                generator.generate_pack(
                    manifest, "claude-code", claude_output, dry_run=False
                )
            self.assertTrue((codex_output / ".agents" / "skills").is_dir())
            self.assertFalse((codex_output / ".claude").exists())
            self.assertTrue((claude_output / ".claude" / "skills").is_dir())
            self.assertFalse((claude_output / ".agents").exists())

    def test_refuses_existing_destination(self) -> None:
        manifest = self.manifests["product-operations-assessment"]
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "existing"
            output.mkdir()
            with self.assertRaises(generator.PackError):
                generator.generate_pack(manifest, "codex", output, dry_run=False)

    def test_dry_run_writes_nothing(self) -> None:
        manifest = self.manifests["product-operations-assessment"]
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "dry-run"
            with redirect_stdout(io.StringIO()):
                generator.generate_pack(manifest, "codex", output, dry_run=True)
            self.assertFalse(output.exists())

    def test_bash_wrapper_forwards_arguments(self) -> None:
        result = subprocess.run(
            [str(ROOT / "create-starter-pack.sh"), "--version"],
            cwd=Path(tempfile.gettempdir()),
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("create-starter-pack.py 0.2.0", result.stdout)

    @unittest.skipUnless(shutil.which("pwsh"), "PowerShell is not installed")
    def test_powershell_wrapper_forwards_arguments(self) -> None:
        result = subprocess.run(
            ["pwsh", "-NoProfile", "-File", str(ROOT / "create-starter-pack.ps1"), "--version"],
            cwd=Path(tempfile.gettempdir()),
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("create-starter-pack.py 0.2.0", result.stdout)


if __name__ == "__main__":
    unittest.main()
