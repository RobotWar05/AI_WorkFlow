# Profiles

Profiles are distribution bundles for installation, not a runtime router and not a command to preload every skill. Route by task and trigger first; install only the smallest bundle needed by a target workspace.

`engineering-core` is the general bundle. `context` contains only approval-gated project continuity. `orchestration` contains only the coordination skill. Domain profiles remain opt-in.

`knowledge-balanced` and `knowledge-deep` install the same small Obsidian skill base. Their different project templates are projected separately by `tools/bootstrap_memory_profile.py`; profile installation alone never creates a vault.
