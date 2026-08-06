# Project memory bootstrap

Use this workflow only when initializing the AI Workflow control plane in a target project. The target project owns its own memory; AI Workflow OS only provides a reviewed projection.

1. Confirm the target root, runtime, owner, current task, preservation requirements and data classification.
2. Ask for one memory profile: `none`, `balanced` or `deep`. Do not infer it from repository size.
3. For `balanced` or `deep`, run the skill-install and memory-profile commands in dry-run mode. The memory dry run may run before `.agents/` exists, but `--apply` must fail closed until the control plane exists. Show every destination before writing.
4. Wait for explicit approval for the target project. Copy only the selected skill projection and template package; never copy AI Workflow history, raw chat, credentials or unrelated knowledge.
5. Create `knowledge/` only for `balanced` or `deep`. It is a project-local Obsidian vault; source files remain in their approved original paths by default.
6. Record the selected profile in `.agents/memory-profile.json`. Future upgrades compare versions and present a diff; they never auto-update a project.
7. Use `source-grounding.md` before turning long documents into notes. Show note diffs and wait for approval before every durable knowledge write.

## Profile boundary

| Profile | Memory behavior |
| --- | --- |
| `none` | Context and append-only history only. |
| `balanced` | Approval-gated Markdown knowledge, source records, decisions and maps of content. |
| `deep` | Balanced plus claim/health templates and a manually requested local semantic index. No hooks, scheduled agents, automatic capture or automatic repair. |

The semantic index is derived data. It must be Git ignored, local-only unless separately approved, and may return only source notes with confidence. It is not an authority and must abstain if the source evidence is insufficient.
