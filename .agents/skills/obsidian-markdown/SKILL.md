---
name: obsidian-markdown
description: Create or edit Obsidian-compatible Markdown using properties, wikilinks, embeds, callouts, tags, and vault-relative organization. Use when working inside an Obsidian vault or when the user explicitly asks for Obsidian syntax, notes, maps of content, or templates.
---

# Obsidian Markdown

Preserve the vault's existing conventions before introducing new syntax or structure.

## Workflow

1. Inspect nearby notes, templates, property names, link style, attachment settings, and folder conventions.
2. Use YAML properties only for structured fields that support retrieval or automation.
3. Use `[[Wikilinks]]` for internal notes and standard Markdown links for external URLs.
4. Prefer stable note titles and vault-relative paths. Add aliases when terminology varies.
5. Use embeds and callouts only when they improve retrieval or comprehension.
6. Check that every new internal link and embed resolves or is intentionally a future note.
7. Preserve user content, frontmatter, and block identifiers when editing.

Read [references/syntax.md](references/syntax.md) when using advanced Obsidian syntax.

## Cautions

- Do not assume renaming a file will update all links; behavior depends on Obsidian settings and plugins.
- Do not convert every phrase into a link or every field into metadata.
- Do not rewrite an entire note to normalize style when a surgical change is enough.
- Ask before reorganizing, renaming, or bulk-linking notes.
