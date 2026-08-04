# Delegated task

1. Chứng minh subtask độc lập và delegation có lợi.
2. Tạo packet hợp lệ; cấp context chọn lọc, budget và return contract.
3. Mặc định worker read-only. Nếu ghi, cấp exclusive write-set.
4. Parent theo dõi state; không micromanage trajectory.
5. Worker dừng khi gặp escalation condition và trả partial artifact.
6. Parent validate schema, base revision, paths và evidence.
7. Integrator rerun integration checks trước khi nhận kết quả.

Không gửi toàn bộ chat cho worker nếu packet + artifact reference đã đủ.
