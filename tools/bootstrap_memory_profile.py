#!/usr/bin/env python3
"""Project a reviewed AI Workflow memory profile into an existing project."""

from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import shutil
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "project-templates" / "agent-control-plane" / "memory-profiles"
PROFILES = ("none", "balanced", "deep")


def profile_template(profile: str) -> Path:
    path = (TEMPLATES / profile).resolve()
    if not path.is_dir() or path.parent != TEMPLATES.resolve():
        raise ValueError(f"Unknown memory profile: {profile}")
    return path


def project_root(value: str) -> Path:
    path = Path(value).resolve()
    if not path.is_dir():
        raise ValueError(f"Target project root does not exist: {path}")
    return path


def manifest(profile: str) -> str:
    data: dict[str, object] = {
        "schema_version": "1.0",
        "profile": profile,
        "source": "AI Workflow OS",
        "installed_on": date.today().isoformat(),
        "write_policy": "proposal-and-explicit-approval",
        "raw_chat_storage": "forbidden",
        "source_material": "reference-by-default",
        "network_policy": "local-only-until-action-time-approval",
    }
    if profile == "deep":
        data["semantic_index"] = {
            "state": "not-configured",
            "update": "manual-only",
            "authority": "derived-index-not-source-of-truth",
            "hook_capture": "forbidden",
        }
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def planned_paths(target: Path, profile: str) -> list[Path]:
    result = [target / ".agents" / "memory-profile.json"]
    if profile != "none":
        result.append(target / "knowledge")
    return result


def ensure_absent(paths: list[Path]) -> None:
    existing = [str(path) for path in paths if path.exists()]
    if existing:
        raise ValueError("Refusing to overwrite existing path(s): " + ", ".join(existing))


def apply(target: Path, profile: str) -> None:
    ensure_absent(planned_paths(target, profile))
    stage = Path(tempfile.mkdtemp(prefix=".aiwf-memory-stage-", dir=target.parent))
    created: list[Path] = []
    try:
        stage_agents = stage / ".agents"
        stage_agents.mkdir(parents=True)
        (stage_agents / "memory-profile.json").write_text(manifest(profile), encoding="utf-8", newline="\n")
        if profile != "none":
            shutil.copytree(profile_template("balanced") / "knowledge", stage / "knowledge")
            if profile == "deep":
                shutil.copytree(profile_template("deep") / "knowledge", stage / "knowledge", dirs_exist_ok=True)
        if profile != "none":
            (stage / "knowledge").replace(target / "knowledge")
            created.append(target / "knowledge")
        (stage_agents / "memory-profile.json").replace(target / ".agents" / "memory-profile.json")
        created.append(target / ".agents" / "memory-profile.json")
    except Exception:
        for path in reversed(created):
            if path.is_dir():
                shutil.rmtree(path)
            elif path.exists():
                path.unlink()
        raise
    finally:
        shutil.rmtree(stage, ignore_errors=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, help="Existing project root; --apply requires .agents/")
    parser.add_argument("--profile", required=True, choices=PROFILES)
    parser.add_argument("--apply", action="store_true", help="Create the reviewed projection; otherwise print a dry run")
    args = parser.parse_args()
    try:
        target = project_root(args.target)
        paths = planned_paths(target, args.profile)
        ensure_absent(paths)
        print(f"Profile: {args.profile}")
        print(f"Target: {target}")
        has_control_plane = (target / ".agents").is_dir()
        if not has_control_plane:
            print("PREREQUISITE: target has no .agents control plane; bootstrap it before --apply.")
        for path in paths:
            print(f"{'CREATE' if args.apply else 'WOULD CREATE'} {path.relative_to(target)}")
        if not args.apply:
            print("Dry run only. Review the plan and rerun with --apply after explicit approval.")
            return 0
        if not has_control_plane:
            raise ValueError(f"Target has no .agents control plane: {target}")
        apply(target, args.profile)
        print("Memory profile projection created.")
        return 0
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
