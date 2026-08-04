---
name: verify-before-completion
description: Verify that requested work is complete before claiming success. Use after code, configuration, documentation, migration, generated artifacts, or multi-file changes, and whenever test output, exit status, rendering, or runtime behavior must support a completion claim.
---

# Verify Before Completion

Completion is an evidence claim.

## Workflow

1. Re-read the request, acceptance criteria, approved scope, and non-goals.
2. Inspect the actual changed files and only external state already authorized by the task.
3. Check for unintended, generated, sensitive, or unrelated changes.
4. Run the narrowest relevant safe, non-destructive checks already authorized by the task. Do not deploy, flash hardware, migrate data, write external state, or contact production services without explicit approval.
5. Inspect both exit status and meaningful output. A zero exit code is not enough when the tool can mask failures.
6. Confirm expected artifacts exist and are usable, not merely that a command ran.
7. Classify each acceptance criterion as passed, failed, or inconclusive.
8. State anything not tested and why.

Use [references/verification-matrix.md](references/verification-matrix.md) to select checks for unfamiliar artifact types.

## Claim Discipline

- Say **verified** only for checks actually run or observations actually made.
- Say **implemented, not runtime-verified** when execution is unavailable.
- Do not call work stable, production-ready, secure, or cross-runtime compatible without evidence for that exact claim.
- Never hide a failed or inconclusive check behind a successful unrelated test.
