#!/usr/bin/env python3
"""Fail static validation when high-confidence secret formats enter the workspace.

The checker reports locations and pattern names only; it never prints a matched value.
It is a guardrail, not a replacement for a reviewed secret-management system.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SCAN_SUFFIXES = {".bat", ".cmd", ".json", ".md", ".ps1", ".py", ".sh", ".toml", ".txt", ".yaml", ".yml"}
SKIP_DIRS = {".git", ".aiwf", ".venv", "venv", "node_modules", "__pycache__"}
PATTERNS = {
    "private-key": re.compile(r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----"),
    "aws-access-key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "github-token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "openai-style-key": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b"),
}


def should_scan(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return not any(part in SKIP_DIRS for part in relative.parts) and (path.suffix.lower() in SCAN_SUFFIXES or path.name.startswith(".env"))


def findings_for_text(text: str) -> set[str]:
    return {name for name, pattern in PATTERNS.items() if pattern.search(text)}


def main() -> int:
    findings: list[tuple[Path, set[str]]] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or not should_scan(path):
            continue
        try:
            matches = findings_for_text(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            continue
        if matches:
            findings.append((path.relative_to(ROOT), matches))
    if findings:
        print("Sensitive-data check failed:")
        for path, matches in findings:
            print(f"- {path}: {', '.join(sorted(matches))}")
        return 1
    print("Sensitive-data check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
