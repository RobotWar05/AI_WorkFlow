#!/usr/bin/env python3
"""Validate trigger-evaluation schema and coverage; do not score model behavior."""

from collections import Counter, defaultdict
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUITE = ROOT / "evals" / "cases" / "v1-trigger-suite.json"
REQUIRED = {"positive": 3, "negative_or_boundary": 3, "overlap": 1, "adversarial": 1}
KINDS = {"positive", "negative", "boundary", "overlap", "adversarial"}
EXPECTED = {"trigger", "do-not-trigger", "overlap"}


def main() -> int:
    data = json.loads(SUITE.read_text(encoding="utf-8"))
    cases = data.get("cases")
    if not isinstance(cases, list):
        print("Eval coverage failed:\n- cases must be a list")
        return 1
    skill_dirs = {path.name for path in (ROOT / ".agents" / "skills").iterdir() if path.is_dir()}
    registry = json.loads((ROOT / "registry" / "skills.json").read_text(encoding="utf-8"))
    explicit_only = {item["name"] for item in registry["skills"] if item.get("implicit") is False}
    counts: dict[str, Counter] = defaultdict(Counter)
    ids: set[str] = set()
    prompts: set[tuple[str, str]] = set()
    errors: list[str] = []
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"case {index}: must be an object")
            continue
        missing = {"id", "skill", "kind", "expected", "prompt"} - set(case)
        if missing:
            errors.append(f"case {index}: missing fields {sorted(missing)}")
            continue
        if any(not isinstance(case[field], str) or not case[field].strip() for field in ("id", "skill", "kind", "expected", "prompt")):
            errors.append(f"case {index}: required fields must be non-empty strings")
            continue
        case_id, skill, kind, expected, prompt = (case[field] for field in ("id", "skill", "kind", "expected", "prompt"))
        if case_id in ids:
            errors.append(f"duplicate id: {case_id}")
        ids.add(case_id)
        prompt_key = (skill, prompt.casefold())
        if prompt_key in prompts:
            errors.append(f"{case_id}: duplicate prompt for {skill}")
        prompts.add(prompt_key)
        if skill not in skill_dirs:
            errors.append(f"{case_id}: unknown skill {skill}")
        if kind not in KINDS:
            errors.append(f"{case_id}: invalid kind {kind}")
        if expected not in EXPECTED:
            errors.append(f"{case_id}: invalid expected {expected}")
        if kind in {"negative", "boundary"} and expected != "do-not-trigger":
            errors.append(f"{case_id}: {kind} must expect do-not-trigger")
        if kind in {"positive", "adversarial"} and expected != "trigger":
            errors.append(f"{case_id}: {kind} must expect trigger")
        if kind == "overlap":
            expected_skills = case.get("expected_skills")
            lead = case.get("lead_skill")
            if expected != "overlap" or not isinstance(expected_skills, list) or len(expected_skills) < 2:
                errors.append(f"{case_id}: overlap requires expected_skills with at least two skills")
            elif any(item not in skill_dirs for item in expected_skills) or len(expected_skills) != len(set(expected_skills)):
                errors.append(f"{case_id}: expected_skills contains unknown or duplicate skills")
            elif skill not in expected_skills or lead not in expected_skills:
                errors.append(f"{case_id}: skill and lead_skill must be in expected_skills")
        if skill in explicit_only and expected in {"trigger", "overlap"} and f"${skill}" not in prompt:
            errors.append(f"{case_id}: explicit-only skill must be invoked as ${skill}")
        bucket = "negative_or_boundary" if kind in {"negative", "boundary"} else kind
        counts[skill][bucket] += 1
    for skill in sorted(skill_dirs):
        if skill not in counts:
            errors.append(f"{skill}: no cases")
            continue
        for bucket, minimum in REQUIRED.items():
            if counts[skill][bucket] < minimum:
                errors.append(f"{skill}: {bucket} has {counts[skill][bucket]}, needs {minimum}")
    if errors:
        print("Eval coverage failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Eval coverage passed: {len(ids)} cases across {len(counts)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
