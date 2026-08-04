# Ownership and isolation

## Ownership

- Mỗi writable path có đúng một owner trong một attempt.
- Shared path mặc định read-only.
- Generated adapter chỉ do generator sở hữu.
- Integrator có quyền tích hợp nhưng không được che dấu conflict.

## Isolation levels

1. `shared-read`: nhiều worker đọc cùng workspace.
2. `exclusive-path`: worker ghi các path rời nhau trong cùng workspace.
3. `worktree`: mỗi worker có Git worktree và base revision riêng.
4. `sandbox`: runtime/process isolation bổ sung cho tool hoặc external effect.

`worktree` chỉ hợp lệ khi `git rev-parse --verify HEAD` thành công. Repository hiện chưa có baseline nên adapter phải từ chối mode này.

## Stale result

Integrator từ chối hoặc rebase có kiểm soát khi `base_revision` của handoff không còn tương thích với integration target. Không hợp nhất chỉ dựa trên lời mô tả của worker.
