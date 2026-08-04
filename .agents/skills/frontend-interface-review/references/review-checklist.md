# Interface review checklist

## Critical paths

- Primary action is findable and completes with clear feedback.
- Validation explains the problem and how to recover.
- Destructive actions expose scope and prevent accidental activation.
- Loading, empty, partial, offline, and error states are intentional.

## Accessibility and resilience

- Semantic controls work with keyboard and retain visible focus.
- Labels, names, instructions, and error associations are meaningful.
- Text and controls remain usable under zoom and reflow.
- Motion respects user preference and does not carry essential meaning alone.
- Responsive layout preserves reading and interaction order.

## Visual system

- Hierarchy reflects content priority.
- Spacing, typography, color, and component states are internally consistent.
- Repetition aids learning; variation communicates meaning.
