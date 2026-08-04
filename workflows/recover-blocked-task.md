# Recover a blocked task

1. Xác định state cuối và attempt ID; không chạy lại mù quáng.
2. Phân loại: input, approval, permission, tool, timeout, conflict, stale base, verification fail.
3. Giữ artifact/evidence hợp lệ từ attempt trước.
4. Chỉ retry khi thao tác idempotent hoặc có deduplication/recovery plan.
5. Tạo attempt mới với budget bounded và context đã cập nhật.
6. Escalate nếu cùng blocker lặp lại hoặc cần mở rộng authority.
