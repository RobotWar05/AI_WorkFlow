# Kiến trúc V2

## 1. Mục tiêu

Một portable control plane cho single-agent, sub-agent và multi-agent, không phụ thuộc task list riêng của vendor. Kiến trúc tối ưu cho progressive disclosure và mechanical validation.

## 2. Các plane

| Plane | Owner | Trách nhiệm |
|---|---|---|
| Instruction | `AGENTS.md`, skill | Invariant và procedure chuyên biệt |
| Contract | `contracts/` | Shape trao đổi máy đọc được |
| Orchestration | `orchestration/`, `workflows/` | Mode, state, authority, failure |
| Domain | `domains/` | Delta chuyên môn và acceptance |
| Agent | `agents/definitions/` | Role/capability canonical |
| Adapter | `adapters/`, generated folders | Mapping tới runtime |
| Evidence | `evals/` | Static, behavioral và regression proof |
| Knowledge | `knowledge/` | Tri thức dài hạn có provenance/approval |

## 3. Data flow

```text
request -> work item -> route/mode -> domain + minimal skills
        -> single execution OR delegation packets
        -> artifacts + worker handoffs
        -> integration plan -> quality gate -> final owner
```

Runtime task state, transcript và mailbox là execution detail. Canonical task state và artifact contract nằm trong repository/run manifest.

## 4. Authority flow

User approval là giới hạn trên. Parent chỉ cấp một phần authority cho worker; worker không thể mở rộng hoặc chuyển quyền cho agent khác. Integrator kiểm tra scope và evidence trước khi nhận artifact.

## 5. Failure/recovery

Mỗi retry là attempt mới. Artifact hợp lệ được giữ; state không bị ghi đè. Timeout, permission, stale base, write conflict và failed verification có nhánh riêng. Worktree mode fail-closed khi thiếu Git baseline.

## 6. Token flow

Startup chỉ nạp root map và metadata. Routing nạp một workflow/role. Execution nạp một domain annex/contract. Deep references chỉ truy xuất khi nhánh hiện tại cần. Xem [token efficiency](token-efficiency.md).

## 7. Compatibility

Canonical JSON không mô phỏng mọi field vendor. Adapter phải khai báo unsupported field và fail-closed khi một security capability bắt buộc không thể ánh xạ. MCP kết nối tool/data; A2A là remote agent adapter; SDK là application orchestration; chúng không thay thế contract nội bộ.
