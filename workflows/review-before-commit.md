# Review Before Commit

Use manually before a commit.

1. Confirm the repository and intended scope.
2. Inspect `git status`, staged diff, and unstaged diff without modifying them.
3. Classify findings: correctness, regression, security/secret, generated junk, documentation, or out-of-scope change.
4. Cite the exact file and relevant symbol or line.
5. Recommend the smallest correction; do not stage, commit, restore, or delete without explicit approval.
6. Re-run the relevant verification after approved fixes.
