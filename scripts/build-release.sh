#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_dir"

./scripts/test-library.sh

python3 - <<'PY'
from pathlib import Path
import shutil
import zipfile

root = Path.cwd()
dist = root / "dist"
release = dist / "aipom-skills"
archive = dist / "aipom-skills.zip"

if release.exists():
    shutil.rmtree(release)
if archive.exists():
    archive.unlink()

release.mkdir(parents=True)

for filename in ["AGENTS.md", "README.md", "ROADMAP.md", "CONTRIBUTING.md", "LICENSE"]:
    shutil.copy2(root / filename, release / filename)

for dirname in ["assessments", "catalog", "commands", "docs", "skills"]:
    shutil.copytree(root / dirname, release / dirname)

with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
    for path in sorted(release.rglob("*")):
        if path.is_file():
            bundle.write(path, path.relative_to(dist))

print(f"Built {archive.relative_to(root)}")
PY

python3 scripts/build-codex-release.py
