# Agent control-plane template

Copy this skeleton into a project only after the user approves the target. Replace every `<...>` placeholder with verified project facts; do not copy AI Workflow OS history or credentials.

```text
project/
├── AGENTS.md
└── .agents/
    ├── context/
    ├── history/
    └── prompts/
```

Root `AGENTS.md` is the instruction source. Context/history are bounded project data. Reusable skills and role definitions remain in AI Workflow OS unless deliberately installed for the target runtime.

The bootstrap asks for a memory profile. `none` keeps only context/history. `balanced` creates approval-gated Obsidian Markdown knowledge. `deep` adds source/claim health templates and an optional manually invoked local index. The template packages live in `memory-profiles/`; do not copy them until the user selects a profile and approves the target write.
