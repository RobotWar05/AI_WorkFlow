#!/usr/bin/env python3
"""Run every static repository validator and preserve each exit code."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
COMMANDS = (
    (sys.executable, "-B", "tools/manage_skills.py", "validate"),
    (sys.executable, "-B", "tools/validate_evals.py"),
    (sys.executable, "-B", "tools/workflowctl.py", "validate"),
    (sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"),
    (sys.executable, "-B", "tools/check_markdown_links.py"),
)


def main() -> int:
    failed = False
    for command in COMMANDS:
        print(f"\n> {' '.join(command)}", flush=True)
        result = subprocess.run(command, cwd=ROOT, check=False)
        failed = failed or result.returncode != 0
    print("\nStatic validation failed." if failed else "\nAll static validation passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
