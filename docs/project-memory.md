# Project memory profiles

AI Workflow OS is a portable control plane, not a shared memory vault. A project receives a small independent projection only after a user selects a profile and approves target writes.

## Roles

| Data | Purpose | Must not become |
| --- | --- | --- |
| `.agents/context/current.md` | Concise task snapshot | A long-term knowledge base |
| `.agents/history/` | Append-only verified events | Raw chat storage |
| `knowledge/` | Durable, sourced project knowledge | A copy of all source documents |
| Local semantic index | Manual recall aid | The source of truth |

## Bootstrap

Start from `.agents/prompts/bootstrap-project.md`. The AI must ask for `none`, `balanced` or `deep`, show dry-run output, and wait for approval before creating a target projection.

For `balanced` or `deep`, install the matching skill bundle into the target runtime and project the matching template:

```powershell
py E:\AI_Workflow\tools\manage_skills.py install --runtime codex --scope workspace --profile knowledge-balanced --target E:\TargetProject --dry-run
py E:\AI_Workflow\tools\bootstrap_memory_profile.py --target E:\TargetProject --profile balanced
```

Replace `codex` and `balanced` with the approved target runtime and profile. Both commands are dry runs unless the installer is invoked without `--dry-run` and the memory command includes `--apply`. The memory dry run also works before `.agents/` exists; it reports that the control plane is a prerequisite for apply.

After the user approves the exact target paths, rerun the first command without `--dry-run`, then rerun the second with `--apply`. The projection refuses to overwrite an existing `knowledge/` directory or memory manifest.

## External sources

`kepano/obsidian-skills` remains the pinned source of the Obsidian syntax derivative. `obsidian-second-brain` and `agentmemory` are candidates for selective future adaptation only. No upstream installer, hook, scheduler, network feature or automatic update is part of a profile.

Agentmemory is deferred until a project has an approved Deep vault and a separate local-only integration review. If enabled later, it may index only approved notes, must run manually, and must return the source Markdown note with every recall result.
