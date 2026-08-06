# Bootstrap a project control plane

```text
Use $manage-project-context to initialize a new project's context control plane.

Before writing, confirm the target project root, project purpose, active runtime/stack, owner, current task, whether existing notes must be preserved, and memory profile: `none`, `balanced`, or `deep`. Show the dry-run output for any selected skill install and memory profile projection. Copy only the skeleton in project-templates/agent-control-plane and the selected memory profile; replace placeholders with verified project facts. Do not copy AI_Workflow history, credentials, raw chat or runtime-specific adapters.

Create root AGENTS.md only if the project has none or the user explicitly approves replacing it. Create .agents/context/current.md, context/handoff.md, history/index.md and prompts. For `balanced` or `deep`, create only the project-local `knowledge/` projection after explicit approval. Keep current/handoff concise, make history append-only, and leave implementation work single-owner by default.
```
