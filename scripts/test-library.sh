#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_dir"

python3 scripts/validate-skills.py
python3 scripts/check-links.py
python3 scripts/validate-release.py

catalog_snapshot="$(mktemp -d)"
trap 'rm -rf "$catalog_snapshot"' EXIT
cp -R catalog "$catalog_snapshot/catalog"

python3 scripts/generate-catalog.py

if ! diff -qr "$catalog_snapshot/catalog" catalog >/dev/null 2>&1; then
  echo "ERROR: generated catalog was stale. Review and include the regenerated catalog changes."
  diff -ru "$catalog_snapshot/catalog" catalog || true
  exit 1
fi

echo "AIPOM library checks passed."
