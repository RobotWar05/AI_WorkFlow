# Failure and recovery

| Failure | Hành động |
|---|---|
| Invalid packet | Không dispatch; trả về lỗi schema |
| Worker timeout | Giữ artifact, đánh dấu attempt failed, retry nếu idempotent |
| Tool/permission denied | Chuyển `APPROVAL_REQUIRED` hoặc `BLOCKED`; không bypass |
| Worker crash | Giữ log/evidence; tạo attempt mới từ checkpoint sạch |
| Write conflict | Dừng integration; ownership review hoặc re-delegate |
| Stale base | Revalidate/rebase có kiểm soát hoặc reject |
| Verification fail | Chuyển `REWORK`, gắn failed criterion IDs |
| Partial multi-agent failure | Tích hợp chỉ artifact độc lập đã pass; phần còn lại giữ unresolved |

Retry phải bounded, có attempt ID và backoff. Không retry thao tác không idempotent nếu chưa có deduplication key hoặc approval mới.
