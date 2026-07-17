#!/usr/bin/env python3
"""Check relative Markdown links in canonical repository files."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def markdown_files() -> list[Path]:
    ignored = {"dist"}
    return sorted(path for path in ROOT.rglob("*.md") if not ignored.intersection(path.relative_to(ROOT).parts))


def main() -> int:
    errors: list[str] = []
    checked = 0
    for source in markdown_files():
        text = source.read_text()
        for match in LINK.finditer(text):
            raw = match.group(1).strip().strip("<>")
            if raw.startswith(SKIP_PREFIXES):
                continue
            destination = unquote(raw.split("#", 1)[0])
            if not destination:
                continue
            checked += 1
            target = (source.parent / destination).resolve()
            try:
                target.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: link leaves repository: {raw}")
                continue
            if not target.exists():
                line = text.count("\n", 0, match.start()) + 1
                errors.append(f"{source.relative_to(ROOT)}:{line}: missing target: {raw}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Link check failed with {len(errors)} error(s).")
        return 1

    print(f"Checked {checked} relative Markdown link(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

