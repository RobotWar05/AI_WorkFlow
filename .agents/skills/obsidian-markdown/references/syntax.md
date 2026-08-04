# Obsidian syntax reference

## Internal links

```markdown
[[Note name]]
[[Note name|Display text]]
[[Note name#Heading]]
![[Attachment.png]]
```

## Properties

```yaml
---
type: note
status: draft
tags:
  - topic/example
source:
  - https://example.com
---
```

Keep dates in an unambiguous ISO form when machine processing matters.

## Callouts

```markdown
> [!warning]
> State a concrete risk and the action it requires.
```

## Blocks

```markdown
Reusable paragraph. ^stable-block-id
```

Use block identifiers sparingly because they create maintenance coupling.
