# Static validation — 2026-08-03

## Scope

- 10 v1 skills and their references/UI metadata.
- 5 profiles.
- 80 trigger-case fixtures with explicit overlap participants and lead skill.
- Maintained Markdown links.
- Claude workspace adapter install into an isolated temporary directory.

## Results

| Check | Result |
|---|---|
| `py tools/manage_skills.py validate` | Pass |
| `py tools/validate_evals.py` | Pass: 80 cases across 10 skills |
| `py tools/check_markdown_links.py` | Pass |
| `py tools/validate_all.py` | Pass; preserves each child exit code |
| Official `skill-creator` `quick_validate.py` | Pass for all 10 skills |
| Python bytecode compilation | Pass for all three tools |
| Claude adapter smoke install | Pass: four engineering-core skills copied |
| Repeated identical install | Pass: all four skipped without overwrite |
| Profile path traversal | Pass: malformed `..\registry\sources` rejected with exit 2 |
| Transaction preflight | Pass: conflict in second skill left first skill uncopied |
| Draft global gate | Pass: blocked without `--allow-draft` |
| Runtime destination dry-runs | Pass for Codex, Claude, and Antigravity IDE user paths |

## Limits

The trigger cases currently prove coverage of the evaluation design, not model behavior. No paired A/B run has been completed on Codex, Claude Code, or Antigravity. Every v1 skill therefore remains `draft`; none is `stable`.
