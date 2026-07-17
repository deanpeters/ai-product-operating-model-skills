#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_dir"

python3 scripts/validate-skills.py
python3 scripts/check-links.py
python3 scripts/validate-release.py
python3 scripts/generate-catalog.py

if ! git diff --exit-code -- catalog >/dev/null 2>&1; then
  if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    echo "ERROR: generated catalog is stale. Review and include the regenerated catalog changes."
    git diff -- catalog
    exit 1
  fi
fi

echo "AIPOM library checks passed."
