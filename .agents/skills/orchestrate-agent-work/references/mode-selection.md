# Mode selection

| Signal | Single owner | Parent + workers | Isolated parallel |
|---|---|---|---|
| Shared context | High | Medium | Low |
| Dependencies | Sequential | Bounded branches | Independent DAG branches |
| Writes | Same files | Read-only or disjoint | Disjoint worktrees |
| Communication | None | Parent-child | Artifact-mediated |
| Final owner | Same agent | Parent/integrator | Integrator |

Use peer teams only as an experimental runtime feature when peer communication creates measurable value. Stop parallelization when write scopes overlap, the contract is unstable, no integrator exists, or coordination overhead exceeds the expected gain.
