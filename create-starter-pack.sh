#!/usr/bin/env bash
set -euo pipefail

starter_pack_repo="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
generator="$starter_pack_repo/scripts/create-starter-pack.py"

if command -v python3 >/dev/null 2>&1; then
  exec python3 "$generator" "$@"
fi

if command -v python >/dev/null 2>&1; then
  exec python "$generator" "$@"
fi

echo "ERROR: Python 3 is required to create an AIPOM Starter Pack." >&2
echo "Install Python 3, then run this command again." >&2
exit 1
