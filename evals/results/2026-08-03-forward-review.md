# Fresh-context forward review — 2026-08-03

Three read-only sub-agents independently reviewed the current skills, eval suite, installer, registries, docs, and workflows. This was a static forward review, not a paired runtime A/B.

## Material findings corrected

- Added explicit safety and authorization bounds to debugging reproduction and verification checks.
- Replaced the blanket embedded timeout rule with deadline/liveness-based bounded behavior.
- Prevented architecture workflow from re-confirming already approved choices.
- Narrowed evidence and architecture triggers to reduce local-only false positives.
- Kept `minimal-implementation` strict opt-in and made all triggering fixtures invoke `$minimal-implementation`.
- Made knowledge retrieval least-disclosure and categorically excluded credentials/API keys from notes.
- Replaced stale hard-coded note dates and aligned confidence to `verified`, `inferred`, or `unverified`.
- Added expected participants and lead skill to every overlap case.
- Closed profile path traversal; added profile/registry schema checks, source containment, symlink rejection, controlled errors, full conflict preflight, staging/digest verification, rollback, and a global draft gate.
- Clarified that profiles are additive distribution manifests and that v1 claims Antigravity IDE, not Antigravity CLI.
- Split automated validation claims from required manual security/license/freshness review.

## Remaining evidence gap

No skill has paired A/B evidence on Codex, Claude Code, or Antigravity IDE. The static review improves the draft but does not graduate it.
