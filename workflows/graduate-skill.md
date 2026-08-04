# Graduate a skill

1. Select one skill and record its current tree hash, source pin, owner, dependencies, and reviewed files.
2. Pass `py tools/validate_all.py` and the official skill validator.
3. Complete manual security, license, factual-freshness, and token-scope review.
4. Run positive, negative, overlap, adversarial, and cold-start cases in a fresh context.
5. Run paired A/B on representative work for one named runtime; preserve the reviewed result summary.
6. Move `draft` to `trial`, then to `stable:<runtime>` only when that runtime's gate passes.
7. Use global `stable` only after independent Codex, Claude Code, and Antigravity IDE evidence passes the documented gate.
8. Update `registry/skills.json` in a reviewed diff. A source pin or install smoke test alone never changes lifecycle status.

If a hard guardrail fails, keep the current state or quarantine the skill. Do not average a safety failure away with better style or token metrics.
