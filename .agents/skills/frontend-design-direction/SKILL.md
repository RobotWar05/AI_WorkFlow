---
name: frontend-design-direction
description: Establish and implement a distinctive visual direction for landing pages, portfolios, marketing sites, and redesigns that would otherwise look generic. Use when visual taste, brand expression, layout, typography, color, motion, or a source-grounded redesign is central; do not use as a universal product-dashboard style mandate.
---

# Frontend Design Direction

Design from the brief and content, not from a fixed aesthetic checklist.

## Preflight

1. Inspect the existing product, content, assets, brand constraints, and technical stack.
2. Identify audience, page purpose, primary action, information hierarchy, and reference sites.
3. Decide the design dials: quiet or expressive, dense or spacious, editorial or utilitarian, geometric or organic, static or motion-led.
4. Choose a coherent type, color, spacing, surface, imagery, and motion system.
5. Explain why this direction fits the audience and content, including where it should not be used.

Use [references/brief-and-dials.md](references/brief-and-dials.md) when the brief is incomplete or several directions are plausible.

## Implementation

- Build hierarchy with content and layout before decoration.
- Reuse a small token system and intentional component variants.
- Preserve semantic HTML, responsive behavior, keyboard access, readable contrast, and reduced-motion behavior.
- Adapt existing components rather than replacing working product patterns without reason.
- Render representative viewports and inspect the result. Correct overflow, awkward wrapping, weak hierarchy, and generic placeholder imagery.

Do not ban system fonts, white backgrounds, common layouts, or familiar components categorically. A design choice is valid when it serves the brief and works in the rendered interface.
