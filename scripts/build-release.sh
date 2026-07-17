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
version = (root / "VERSION").read_text().strip()
dist = root / "dist"
release = dist / f"aipom-skills-v{version}"
archive = dist / f"aipom-skills-v{version}.zip"
stable_archive = dist / "aipom-skills.zip"

if release.exists():
    shutil.rmtree(release)
if archive.exists():
    archive.unlink()
if stable_archive.exists():
    stable_archive.unlink()

release.mkdir(parents=True)

for filename in ["AGENTS.md", "README.md", "ROADMAP.md", "CONTRIBUTING.md", "CHANGELOG.md", "VERSION", "CITATION.cff", "SECURITY.md", "LICENSE"]:
    shutil.copy2(root / filename, release / filename)

for dirname in ["assessments", "catalog", "commands", "docs", "skills"]:
    shutil.copytree(root / dirname, release / dirname)

with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
    for path in sorted(release.rglob("*")):
        if path.is_file():
            bundle.write(path, path.relative_to(dist))

shutil.copy2(archive, stable_archive)
print(f"Built {archive.relative_to(root)}")
PY

python3 scripts/build-codex-release.py

python3 - <<'PY'
from hashlib import sha256
from pathlib import Path

root = Path.cwd()
version = (root / "VERSION").read_text().strip()
dist = root / "dist"
archives = [
    dist / f"aipom-skills-v{version}.zip",
    dist / f"aipom-codex-skills-v{version}.zip",
]
lines = [f"{sha256(path.read_bytes()).hexdigest()}  {path.name}" for path in archives]
(dist / "SHA256SUMS").write_text("\n".join(lines) + "\n")
print("Built dist/SHA256SUMS")
PY
