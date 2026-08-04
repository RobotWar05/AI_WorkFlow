---
name: second-brain
description: Capture, retrieve, connect, and maintain durable knowledge in an Obsidian-style second brain with provenance, confidence, and approval-gated writes. Use when the user asks to save knowledge, organize notes, recall prior decisions, create a project or area note, reconcile duplicates, or maintain maps of content.
---

# Second Brain

Retrieve only within authorized scope and disclose the minimum relevant content; write deliberately. Never create, edit, move, rename, or delete knowledge notes without the user's approval for that operation.

## Choose the Mode

- **Recall:** search the smallest relevant scope, rank authoritative and recent notes, and answer with note paths.
- **Capture:** distill durable knowledge, propose destination and diff, then wait for approval before writing.
- **Maintenance:** detect stale, duplicate, orphaned, or conflicting notes; propose changes without applying them.

Read [references/recall.md](references/recall.md) for retrieval, [references/capture.md](references/capture.md) before any proposed write, and [references/schema.md](references/schema.md) when choosing properties or folders.

## Knowledge Quality

- Separate source facts, user decisions, assistant inference, and unresolved questions.
- Attach provenance and an observed or reviewed date to claims that may drift.
- Prefer one durable concept per atomic note, but keep project context together when splitting would harm comprehension.
- Link only meaningful relationships and explain conflicts instead of silently merging them.
- Never store credentials, API keys, recovery codes, or authentication secrets in knowledge notes; direct them to an appropriate secret manager. Store other sensitive or personal material only with explicit scope and destination approval.

## Write Gate

Before a write, show the target path, purpose, proposed content or concise diff, links affected, and conflicts found. Apply only the approved scope, then verify the resulting note and links.
