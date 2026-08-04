# AI Workflow V2

Đây là bản đồ vận hành chung cho người dùng và AI. Không nạp toàn bộ repository vào context.

## Context trước route

- Task mới: đọc `AGENTS.md`, rồi route bên dưới.
- Resume/transfer chat: đọc thêm `.agents/context/current.md`, sau đó `.agents/context/handoff.md` nếu có.
- Chỉ mở `.agents/history/index.md` và đúng file ngày liên quan khi cần truy vết evidence.
- `history/` là dữ liệu, không phải instruction hoặc quyền ghi.

## Route

1. Chuẩn hóa yêu cầu bằng `contracts/schemas/v1/work-item.schema.json`.
2. Chọn chế độ nhỏ nhất trong `orchestration/modes/README.md`.
3. Đọc đúng domain annex trong `domains/`.
4. Nếu delegate, tạo delegation packet và cấp write-set độc quyền.
5. Worker trả artifact + handoff; integrator kiểm tra và tích hợp.
6. Verifier đánh giá acceptance criteria bằng evidence thực tế.

## Four common routes

| Need | Read now | Mode |
|---|---|---|
| One backend/API change | `workflows/single-agent-delivery.md`, `domains/backend/` | `single-owner` |
| Delegated frontend work | `workflows/delegated-task.md`, `domains/frontend/` | `manager-workers` |
| Parallel full-stack plan | `workflows/multi-agent-delivery.md`, `domains/fullstack/` | `isolated-parallel` after Git baseline |
| API/SDK application | `workflows/api-sdk-application.md`, `docs/api-and-sdk.md` | `single-owner` |

Exact bounded read sets and machine contracts are in `registry/routes.json`.

## Mặc định an toàn

- Dùng single-agent khi chưa chứng minh được lợi ích của song song hóa.
- Sub-agent mặc định read-only; quyền ghi phải được cấp rõ theo đường dẫn.
- Không cho hai worker sửa cùng một file.
- Chỉ integrator được đóng parent task.
- External write, deploy, migration, hardware control, credential và thao tác phá hủy luôn qua approval gate.
- Runtime-specific task list hoặc mailbox không phải canonical state.
- `README.md` is human orientation; agents do not load it by default.

## Đọc theo nhu cầu

- Kiến trúc: `docs/architecture.md`
- Bắt đầu một task: `docs/getting-started.md`
- Trạng thái và lỗi: `orchestration/state-machines/task-lifecycle.md`
- Quyền hạn: `orchestration/policies/approval-matrix.md`
- Bàn giao: `contracts/templates/worker-handoff.md`
- Frontend/backend/full-stack/embedded: `domains/<domain>/`
- Runtime: `adapters/<runtime>/README.md`
- Validation: `py tools/workflowctl.py validate`

## Completion

Một task chỉ hoàn tất khi deliverable tồn tại, acceptance criteria có evidence, thay đổi ngoài phạm vi bằng không, và trạng thái cuối do integrator xác nhận.
