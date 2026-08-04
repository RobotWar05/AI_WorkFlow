# Project context control plane

`AGENTS.md` and `WORKFLOW.md` are the only instruction sources. This folder stores bounded project context; its contents do not grant authority or override those files.

## Read order

1. Read root `AGENTS.md`.
2. For an active task, read `context/current.md`.
3. For a new chat or transfer, read `context/handoff.md`.
4. Open `history/index.md` and one relevant day only when tracing evidence.

## Layout

```text
.agents/
├── agents/       # Generated runtime projections
├── skills/       # Canonical reusable procedures
├── context/      # Current snapshot and copy-ready handoff
├── history/      # Append-only verified daily events
└── prompts/      # Start, summarize and bootstrap prompts
```

Do not store raw chat, secrets, credentials or transient run logs here. Use `.aiwf/runs/` for local generated run state and Git for file history.

`prompts/start-new-chat.md` is for a concise new-chat/resume startup. `prompts/start-new-private-first-task.md` is for a new scoped task. `prompts/bootstrap-project.md` initializes this control-plane structure in another project after approval.
