# Safe Rollback

Use manually when recovering from wrong changes.

1. Identify the exact repository, files, and desired recovery point.
2. Inspect status, diff, history, and available recovery sources.
3. Separate user work from changes being rolled back.
4. Present the exact destructive command and affected paths before execution.
5. Require explicit approval for restore, reset, clean, deletion, or overwrite.
6. Prefer targeted and recoverable operations.
7. Verify restored content and report what can or cannot be recovered.
