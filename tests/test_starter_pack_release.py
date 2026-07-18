"""Focused tests for deterministic Starter Pack release archives."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "build-starter-pack-release.py"
SPEC = importlib.util.spec_from_file_location("build_starter_pack_release", SCRIPT)
assert SPEC and SPEC.loader
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)


class StarterPackReleaseTests(unittest.TestCase):
    def test_deterministic_zip_is_reproducible(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            source.mkdir()
            (source / "README.md").write_text("hello\n", encoding="utf-8")
            nested = source / ".agents" / "skills" / "aipom-start"
            nested.mkdir(parents=True)
            (nested / "SKILL.md").write_text("skill\n", encoding="utf-8")
            first = root / "first.zip"
            second = root / "second.zip"

            builder.deterministic_zip(source, first, "pack")
            builder.deterministic_zip(source, second, "pack")

            self.assertEqual(first.read_bytes(), second.read_bytes())
            with zipfile.ZipFile(first) as archive:
                self.assertEqual(
                    ["pack/.agents/skills/aipom-start/SKILL.md", "pack/README.md"],
                    archive.namelist(),
                )

    def test_archive_member_safety(self) -> None:
        self.assertTrue(builder.safe_member("pack/README.md", "pack"))
        self.assertFalse(builder.safe_member("../README.md", "pack"))
        self.assertFalse(builder.safe_member("other/README.md", "pack"))
        self.assertFalse(builder.safe_member("/pack/README.md", "pack"))


if __name__ == "__main__":
    unittest.main()
