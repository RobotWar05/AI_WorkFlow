# Skill Governance

## Lifecycle

```text
candidate -> quarantined | draft -> trial -> stable:<runtime> -> stable -> deprecated
```

- `candidate`: discovered but not trusted.
- `quarantined`: security, license, scope, or quality gate failed.
- `draft`: source reviewed and local behavior written.
- `trial`: static/trigger checks pass; empirical evaluation incomplete.
- `stable:<runtime>`: passes on one named runtime.
- `stable`: passes on Codex, Claude Code, and Antigravity.

## Admission gate

- One bounded job with clear positive and negative triggers.
- Provenance, license, revision, dependencies, and owner recorded.
- Every script/hook/installer read before use.
- No silent network calls, telemetry, auto-mutation, or self-update.
- No unresolved overlap with active skills.
- Context cost justified by measured benefit.

## Update policy

Pin the reviewed revision. When upstream changes, inspect the diff, repeat license/security review, and rerun affected regression. Never follow latest automatically.

## Lessons from references

The VINQA reference demonstrates useful routing and eval ideas, but also why quantity is not maturity: duplicated libraries, broad triggers, broken links, unimplemented MCP claims, and approval-free mutation must not be imported.

Current lifecycle state is machine-readable in [`registry/skills.json`](../registry/skills.json). A source pin proves which input was reviewed; it does not prove the derived skill is stable.
