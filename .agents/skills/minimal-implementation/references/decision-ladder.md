# Minimal design review

Prefer:

- one proven path before a configurable framework;
- direct code before an abstraction with one caller;
- existing dependencies before a new package;
- explicit local state before distributed state;
- measured optimization before speculative caching;
- reversible decisions before premature generality.

Do not confuse fewer lines with lower complexity. A shorter implementation with hidden coupling, unsafe defaults, or ambiguous ownership is not minimal; it transfers complexity to operations and debugging.

This workflow is conceptually inspired by YAGNI and community “Ponytail” discussions. It is an original, safety-bounded implementation; external candidates remain subject to provenance and license review in the registry.
