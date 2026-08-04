---
name: systematic-debugging
description: Diagnose a concrete observed failure, regression, flaky behavior, log, trace, timing fault, or reproducible mismatch through controlled hypotheses. Use for incident-specific debugging and root-cause analysis; do not use for generic explanations of error categories without an actual incident or artifact.
---

# Systematic Debugging

Diagnose before prescribing. If the user asked only for diagnosis, do not implement a fix.

## Workflow

1. Define expected behavior, observed behavior, impact, and last known good state.
2. Attempt the smallest safe reproduction only when it is non-destructive, within approved scope, and does not risk hardware, data, credentials, users, or production. Otherwise preserve evidence, state why reproduction is unsafe or unavailable, and design an isolated or simulated reproduction.
3. Preserve exact errors, timestamps, versions, inputs, and environmental conditions.
4. Trace the relevant data path and control path from source to failure.
5. Identify the earliest confirmed divergence, not merely the final symptom.
6. Rank hypotheses by evidence and discriminating power.
7. Test one hypothesis at a time with the smallest safe, authorized observation or experiment. Ask before expanding access or causing external effects.
8. Record what each result rules in or rules out.
9. State the root cause only when evidence supports the causal chain.
10. Propose the smallest robust fix and regression checks if implementation is authorized.

After repeated failed hypotheses, stop stacking speculative patches. Recheck reproduction, assumptions, interfaces, and architecture.

For firmware, timing, concurrency, or hardware faults, read [references/embedded-debugging.md](references/embedded-debugging.md).

## Output

Report severity, evidence, root cause or current best hypothesis, confidence, fix direction, regression risk, and missing data. Separate confirmed facts from inference.
