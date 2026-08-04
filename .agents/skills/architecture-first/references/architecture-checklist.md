# Architecture checklist

## Boundaries

- Are responsibilities owned once rather than duplicated?
- Are dependency directions explicit?
- Are runtime-specific adapters separated from canonical logic?
- Are trust boundaries and external side effects visible?

## State and flow

- What creates, validates, transforms, persists, and consumes each datum?
- Which states and transitions are legal?
- What can run concurrently or out of order?
- What happens after restart, retry, timeout, or partial completion?

## Operations

- How is failure detected and diagnosed?
- Is rollback possible without data loss?
- Which resources are bounded?
- What proves the design meets acceptance criteria?
