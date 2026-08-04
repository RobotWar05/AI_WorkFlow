---
name: minimal-implementation
description: Deliberately minimize an implementation to the smallest complete solution and defer speculative extensibility. Use only when the user explicitly asks for a minimal, MVP, YAGNI, or Ponytail-style implementation, or when comparing a deliberately small option against a broader design.
---

# Minimal Implementation

Minimize accidental complexity, not required correctness.

## Decision Ladder

For every proposed abstraction, dependency, option, state, or layer, ask:

1. Is it required by an acceptance criterion or current constraint?
2. Does current evidence show more than one real variation?
3. Would omitting it create material safety, data-loss, security, accessibility, or operability risk?
4. Is the cost of adding it later demonstrably higher than adding it now?

Keep it when the answer supports current need. Otherwise defer it and record the trigger that would justify adding it.

Read [references/decision-ladder.md](references/decision-ladder.md) for design reviews.

## Non-Negotiable Floor

Do not remove required validation, error handling, timeouts, authorization checks, data protection, accessibility, observability, hardware calibration, or regression tests in the name of simplicity.

## Output

State the smallest complete scope, what is deliberately deferred, the evidence for each deferral, and the future condition that would reopen it. Verify the minimal solution against the full acceptance criteria.
