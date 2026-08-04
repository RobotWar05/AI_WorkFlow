---
name: architecture-first
description: Design the structure of a medium or large technical change before implementation. Use when boundaries, ownership, interfaces, persistence, several components, or safety-critical runtime architecture require a decision. Do not use for a local edit whose structure and behavior are already decided.
---

# Architecture First

Scale the analysis to the risk. Do not turn a small local edit into a design ceremony.

## Workflow

1. Define the real outcome, users, constraints, and acceptance criteria.
2. Inspect the current system and identify authoritative files and interfaces.
3. Draw the boundary: what changes, what stays unchanged, and who owns each responsibility.
4. Describe data flow, control flow, state transitions, dependencies, and external effects.
5. Budget critical resources such as time, memory, storage, bandwidth, power, and operator attention.
6. Enumerate failure modes, degraded behavior, recovery, observability, and rollback.
7. Compare viable options using explicit tradeoffs. Recommend one and state when it is a poor fit.
8. Divide implementation into independently verifiable stages.
9. Surface unresolved decisions that materially change architecture, data, runtime behavior, or safety for confirmation. Do not re-confirm choices already approved; record them and proceed.

Read [references/architecture-checklist.md](references/architecture-checklist.md) for a design review or a multi-runtime agent workflow.

## Applicable Output

Include only what the risk requires. At minimum, state boundaries and interfaces, failure and recovery behavior, and staged verification. Add requirements, component maps, state models, and option tradeoffs when they influence the decision.

Keep assumptions visible. Do not present a diagram or named pattern as evidence that the design is sound.
