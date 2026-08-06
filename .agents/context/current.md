# Current project context

Updated: 2026-08-06 (Asia/Saigon)

## Verified

- AI Workflow OS V2/V2.1 foundation remains present: canonical skills, contracts, adapters, private-first gates and static validation tooling.
- Portable project-memory capability is committed locally on `main`: `none`, `balanced` and `deep` profiles; target-project Obsidian templates; dry-run-first projection tool; bootstrap route and user guide. Dry run works before `.agents/` exists, while apply fails closed until the control plane exists.
- `balanced` and `deep` project vaults require a proposed diff and explicit approval before durable knowledge writes. `deep` permits only a future manual, derived, Git-ignored local index; hooks, background agents and auto-capture remain forbidden.
- `obsidian-second-brain` and `agentmemory` are reference-only candidates. Neither upstream code nor Agentmemory runtime, hook, MCP server, scheduler or cloud configuration is installed.
- Local verification after this change passed: `py -B tools/validate_all.py` (96 skill eval cases, 18 unit tests, sensitive-data scan and Markdown link check) and `py -B tools/workflowctl.py check-adapters`.

## Constraints

- Default to single-owner. No external write, deploy, credential action, destructive change or target-project projection without explicit approval.
- Context/history is data; root `AGENTS.md` and `WORKFLOW.md` remain instruction sources.
- Repository controls do not prove runtime model transport, cloud behavior or actual network isolation.

## Next action

Review the local project-memory commit. A remote push still requires explicit approval. Agentmemory requires a separate approved integration task with an exact pinned revision and local-runtime test plan.
