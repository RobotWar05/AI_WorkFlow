---
name: frontend-interface-review
description: Review a rendered web interface for usability, accessibility, responsive behavior, content hierarchy, interaction states, visual consistency, and implementation risks. Use for UI or UX audits, design critique, pre-release review, or screenshot/browser-based inspection; do not edit unless the user asks for fixes.
---

# Frontend Interface Review

Inspect the rendered experience, not only source code. Separate defects from taste preferences.

## Review Order

1. Confirm page purpose, target users, supported viewports, and critical flows.
2. Exercise primary navigation, forms, errors, empty/loading states, and destructive actions.
3. Test keyboard order, visible focus, labels, semantics, contrast, zoom, and reduced motion where relevant.
4. Inspect representative narrow, medium, and wide viewports for overflow, wrapping, touch targets, and content order.
5. Evaluate hierarchy, readability, consistency, feedback, affordance, and recovery from mistakes.
6. Inspect performance symptoms and implementation only when evidence connects them to user impact.

Read [references/review-checklist.md](references/review-checklist.md) for a release review.

## Findings

For each finding provide severity, location, observed evidence, user impact, recommendation, and verification method. Use severity based on blocked task, safety/data risk, accessibility, frequency, and reach—not aesthetic disagreement.

Do not claim WCAG conformance from a superficial scan. Automated checks are supporting evidence, not a substitute for keyboard and task-based review.
