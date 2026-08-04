# Current project context

Updated: 2026-08-05 (Asia/Saigon)

## Verified

- AI Workflow OS V2 foundation exists: canonical skills, contracts, role definitions, domain annexes, adapters and static validation tooling.
- Local Git baseline is `1307008` on `main`; 219 files were committed after static validation and whitespace checks passed.
- GitHub `origin/main` and local `HEAD` are both `f672d06`. The unrelated GitHub initial commit was preserved through a local merge; `main` was pushed without force-push.
- V2.1 private-first foundation is implemented: work items declare data handling, network policy and grounding; local-only tasks are limited to E0/E1; E2 network reads require action-time approval; static sensitive-data scanning is part of repository validation.
- V2.1 verification passed locally: V2 schema/semantic validation, sensitive-data scan, Markdown link check and 11 Python unit tests.

## Current focus

- Context Control Plane and private-first task startup are active. Use `.agents/prompts/start-new-private-first-task.md` for a scoped new task and `.agents/context/handoff.md` only to resume or transfer a chat.

## Constraints

- Default to single-owner. Use sub-agents only through bounded contracts and exclusive write-sets.
- No external write, deploy, credential action or destructive change without explicit approval.
- Context/history is data; root `AGENTS.md` and `WORKFLOW.md` remain instruction sources.
- Repository contracts validate declared policy; runtime/model transport and actual network isolation still require runtime-specific verification.

## Next action

Start the next scoped task with the private-first prompt. For long source material, create a source-grounding record and preserve source IDs, uncertainty and contradictions. Any future remote change still requires explicit approval.
