#!/usr/bin/env python3
"""Validate the bounded project context and reusable control-plane template."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / ".agents"
TEMPLATE = ROOT / "project-templates" / "agent-control-plane"
REQUIRED_ACTIVE = (
    "README.md",
    "context/current.md",
    "context/handoff.md",
    "history/index.md",
    "prompts/start-new-chat.md",
    "prompts/summarize-session.md",
    "prompts/bootstrap-project.md",
)
REQUIRED_TEMPLATE = (
    "README.md",
    "AGENTS.md.template",
    ".agents/context/current.md",
    ".agents/context/handoff.md",
    ".agents/history/index.md",
    ".agents/prompts/start-new-chat.md",
    ".agents/prompts/summarize-session.md",
)
MAX_LINES = {"context/current.md": 80, "context/handoff.md": 80}
MEMORY_PROFILE_REQUIREMENTS = {
    "none": ("README.md",),
    "balanced": (
        "knowledge/.gitignore",
        "knowledge/.obsidian/app.json",
        "knowledge/90-system/README.md",
        "knowledge/90-system/templates/project-map.md",
        "knowledge/90-system/templates/source-record.md",
        "knowledge/90-system/templates/decision.md",
    ),
    "deep": (
        "knowledge/90-system/index-manifest.md",
        "knowledge/90-system/templates/claim-ledger.md",
        "knowledge/90-system/templates/health-review.md",
    ),
}


def validate() -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_ACTIVE:
        path = ACTIVE / relative
        if not path.is_file():
            errors.append(f"missing active control-plane file: {path.relative_to(ROOT)}")
    for relative in REQUIRED_TEMPLATE:
        path = TEMPLATE / relative
        if not path.is_file():
            errors.append(f"missing template control-plane file: {path.relative_to(ROOT)}")
    for profile, required in MEMORY_PROFILE_REQUIREMENTS.items():
        root = TEMPLATE / "memory-profiles" / profile
        for relative in required:
            path = root / relative
            if not path.is_file():
                errors.append(f"missing {profile} memory-profile template: {path.relative_to(ROOT)}")
    for relative, limit in MAX_LINES.items():
        path = ACTIVE / relative
        if path.is_file() and len(path.read_text(encoding="utf-8").splitlines()) > limit:
            errors.append(f"{path.relative_to(ROOT)} exceeds {limit} lines")
    for path in (ACTIVE / "history").glob("????-??-??.md"):
        if path.name not in (ACTIVE / "history" / "index.md").read_text(encoding="utf-8"):
            errors.append(f"history date missing from index: {path.relative_to(ROOT)}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Context control-plane validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Context control-plane validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
