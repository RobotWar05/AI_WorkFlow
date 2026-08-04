# AI Workflow OS

Workflow private-first, cross-runtime để xây skill, chạy agent đơn, giao việc cho sub-agent và kiểm soát multi-agent bằng contract có thể kiểm tra.

## 1. Trạng thái

V2 Foundation cung cấp kiến trúc, schema, form bàn giao, domain gate, role, adapter và static eval. Đây chưa phải tuyên bố “production-ready” hoặc “tốt nhất thế giới”. Mỗi runtime chỉ được graduate sau runtime A/B riêng.

## 2. Cấu trúc

```text
AI_Workflow/
├── AGENTS.md                 # Bản đồ bắt buộc cho AI
├── WORKFLOW.md               # Route vận hành ngắn
├── aiwf.json                 # Project manifest
├── .agents/skills/           # Skill chuẩn, nhỏ và tái sử dụng
├── agents/                   # Role, topology và capability matrix
├── contracts/                # JSON Schema, form và fixtures
├── domains/                  # Frontend, backend, full-stack, embedded
├── orchestration/            # Mode, policy và state machine
├── workflows/                # Runbook single/sub/multi-agent
├── adapters/                 # Runtime manifests
├── .codex/agents/            # Generated Codex projections
├── .claude/agents/           # Generated Claude projections
├── .agents/agents/           # Generated Antigravity projections
├── profiles/                 # Bundle skill nhỏ
├── evals/                    # Trigger, contract và orchestration eval
├── tools/                    # Validate, generate, install
├── knowledge/                # Obsidian second brain có approval gate
├── personalization/          # Preference giao tiếp
└── docs/                     # Kiến trúc, evidence và governance
```

## 3. Chọn chế độ

| Trường hợp | Mode |
|---|---|
| Task tuần tự, shared context hoặc cùng file | `single-owner` |
| Nghiên cứu/review/subtask bounded | `manager-workers` |
| Nhiều write-set độc lập, có Git baseline | `isolated-parallel` |
| Agent cần trao đổi ngang hàng | `peer-team-experimental` |

Single-agent là mặc định. Multi-agent chỉ được giữ khi chất lượng hoặc latency cải thiện sau khi tính coordination/token cost.

## 4. Lệnh thường dùng

```powershell
py tools/workflowctl.py status
py tools/workflowctl.py validate
py tools/workflowctl.py check-adapters
py tools/validate_all.py
```

Sau khi sửa `agents/definitions/`:

```powershell
py tools/workflowctl.py generate-adapters
```

## 5. Đọc gì khi cần

| Nhu cầu | Tài liệu |
|---|---|
| Bắt đầu task | [Getting started](docs/getting-started.md) |
| Hiểu source of truth | [Architecture](docs/architecture.md) |
| Agent/sub-agent/multi-agent | [Execution modes](orchestration/modes/README.md) |
| Form bàn giao | [Contracts](contracts/README.md) |
| Frontend/backend/full-stack/embedded | [`domains/`](domains/) |
| API | [API contract annex](domains/backend/api-contract.md) |
| Xây ứng dụng bằng API/SDK | [API and SDK workflow](docs/api-and-sdk.md) |
| Chọn route nhanh | [Workflow map](WORKFLOW.md) |
| Tiếp tục ở phiên sau | [V2 handoff](docs/v2-handoff.md) |
| Xây hoặc nhận skill | [Skill governance](docs/skill-governance.md) |
| Đánh giá chất lượng | [Evaluation](docs/evaluation.md) |
| Nguồn nghiên cứu | [Research sources](docs/research-sources.md) |

## 6. Giới hạn đã biết

- Repository chưa có initial Git commit; worktree mode chưa sẵn sàng.
- Claude adapter chưa runtime-test vì local Claude CLI không có.
- Codex và Antigravity adapter mới static-validated; chưa có behavioral A/B.
- Peer-team của vendor không phải portable baseline.
- `jsonschema` là dev dependency; xem `requirements-dev.txt`.

Reference planes và raw eval trace không phải active instructions. Không auto-install hoặc auto-update skill bên ngoài.
