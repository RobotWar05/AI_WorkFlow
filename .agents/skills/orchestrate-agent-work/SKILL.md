---
name: orchestrate-agent-work
description: Route and coordinate a technical task across single-agent, parent-managed sub-agent, or multi-agent execution with bounded authority, context, ownership, handoffs, integration, and verification. Use when deciding whether to delegate, defining agent roles or write scopes, supervising parallel work, recovering a failed agent run, or integrating results. Do not use for a small direct task that has one clear owner and no coordination risk.
---

# Orchestrate Agent Work

Keep single-owner execution as the baseline. Add agents only when independent work and measurable benefit justify coordination cost.

## Workflow

1. Validate the work item: objective, scope, non-goals, risk, deliverables, acceptance and authority.
2. Choose the smallest viable mode. Read [references/mode-selection.md](references/mode-selection.md) for delegated or parallel work.
3. Build a dependency graph. Delegate outcomes with typed return contracts, not vague activities.
4. Assign one owner per writable path. Require a Git baseline before worktree isolation.
5. Bound context, turns, time, tools, children, concurrency, retries and external effects.
6. Keep one authoritative task state and one integrator/final-answer owner.
7. Validate handoff schema, base revision, write scope, artifact and evidence before integration.
8. Verify acceptance with deterministic evidence first. Record failed or inconclusive criteria explicitly.
9. Compare delegated/multi-agent outcome and overhead with the single-agent baseline before making the mode a default.

## Hard Boundaries

- Default workers to read-only; grant writes explicitly and exclusively.
- Never let two workers edit the same file in one attempt.
- Never expand approval through delegation.
- Never treat worker self-report or model reflection as completion evidence.
- Never let a worker close the parent task.
- Preserve partial artifacts after failure; retry only with a new bounded attempt.

Use repository contracts under `contracts/schemas/v1/`, policies under `orchestration/policies/`, and the matching annex under `domains/`. Load only the files needed by the current branch.
