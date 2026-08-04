# Verification matrix

| Change | Minimum relevant evidence |
|---|---|
| Source code | diff review, formatter/linter where configured, focused tests, build or type check |
| Firmware | compile, memory report, simulator or approved read-only target observation, timing/failure-path evidence when affected; flashing needs explicit authority |
| Configuration | parser/schema check, resolved values, dry-run or isolated smoke test |
| Documentation | link/path check, examples checked, rendered layout when layout matters |
| UI | build/type check, representative viewport render, keyboard/focus check, error and empty states |
| Skill | metadata validation, link validation, positive/negative/overlap trigger evals, forward test |
| Migration | confirmed non-mutating dry run; backup/rollback evidence, execution, and post-migration validation only when explicitly authorized |
