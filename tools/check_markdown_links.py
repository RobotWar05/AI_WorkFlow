#!/usr/bin/env python3
"""Check relative Markdown links in maintained documentation."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = (ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "THIRD_PARTY_NOTICES.md")
ROOTS = (
    ROOT / ".agents" / "skills",
    ROOT / "adapters",
    ROOT / "contracts",
    ROOT / "backend",
    ROOT / "domains",
    ROOT / "docs",
    ROOT / "frontend",
    ROOT / "orchestration",
    ROOT / "personalization",
    ROOT / "profiles",
    ROOT / "project-templates",
    ROOT / "workflows",
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def markdown_files():
    yield from (path for path in ROOT_FILES if path.is_file())
    for folder in ROOTS:
        if folder.is_dir():
            yield from folder.rglob("*.md")


def main() -> int:
    errors: list[str] = []
    for source in markdown_files():
        for raw in LINK_RE.findall(source.read_text(encoding="utf-8")):
            value = raw.strip().split()[0].strip("<>")
            target = unquote(value.split("#", 1)[0])
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (source.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{source.relative_to(ROOT)} -> {raw}")
    if errors:
        print("Broken Markdown links:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Markdown link check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
