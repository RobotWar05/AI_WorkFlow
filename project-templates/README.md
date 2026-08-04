# Project bootstrap

Không nhân bản bốn bộ workflow. Mọi project dùng một scaffold và chọn domain annex bằng manifest.

```text
project/
├── AGENTS.md             # Project-specific map
├── aiwf.json             # Runtime/profile/domain selection
├── .agents/              # Context, history and reusable prompts
├── docs/
│   ├── architecture.md
│   └── decisions/
├── contracts/            # Project API/data contracts
├── evals/                # Project fixtures and acceptance
└── .aiwf/runs/           # Local generated state, ignored
```

## Domain mapping

- Frontend: `domains/frontend/`
- Backend/API: `domains/backend/`
- Full-stack: `domains/fullstack/`
- Embedded: `domains/embedded/`

Chỉ copy project-specific facts. Link hoặc retrieve reusable workflow từ repository này để tránh drift.

Sao chép [`agent-control-plane/`](agent-control-plane/) khi project cần continuity qua ngày hoặc chuyển chat. Không copy raw history giữa các project.
