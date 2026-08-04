# Runtime adapters

`agents/definitions/` là canonical. `.codex/agents/`, `.claude/agents/` và `.agents/agents/` là generated projections; không sửa tay.

```powershell
py tools/workflowctl.py generate-adapters
py tools/workflowctl.py check-adapters
```

Adapter manifest phải khai báo version range, maturity, mapping, unsupported fields và fallback. “File sinh được” không đồng nghĩa “behavior đã được runtime chứng minh”. SDK/API adapter sau này nên sinh typed configuration trực tiếp, không parse ngược Markdown/TOML.
