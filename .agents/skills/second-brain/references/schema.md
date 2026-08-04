# Vault schema

## Folders

- `00-inbox`: unprocessed captures.
- `10-projects`: active outcomes with an end state.
- `20-areas`: ongoing responsibilities.
- `30-resources`: external subject material.
- `40-notes`: durable atomic or conceptual notes.
- `50-mocs`: maps of content and curated navigation.
- `90-system`: templates and vault operations.
- `attachments`: non-Markdown assets.

## Suggested properties

Use only what retrieval needs:

```yaml
type: note
status: draft
created: "<current YYYY-MM-DD>"
reviewed: "<current YYYY-MM-DD>"
confidence: unverified
source: []
aliases: []
tags: []
```

Replace the date placeholders at capture time. Treat `created` as historical and `reviewed` as evidence freshness. Use `verified`, `inferred`, or `unverified` for confidence; it describes the claim, not the importance of the note.
