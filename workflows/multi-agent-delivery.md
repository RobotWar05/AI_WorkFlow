# Multi-agent delivery

1. So sánh với baseline single-agent.
2. Lập DAG, ownership matrix, merge order và failure policy.
3. Yêu cầu Git baseline cho isolated parallel writes.
4. Dispatch bounded workers; không cho nested delegation nếu chưa được cấp.
5. Giao tiếp qua artifact/handoff; peer messaging chỉ khi topology yêu cầu.
6. Giữ một authoritative task state và một integrator.
7. Xử lý partial failure; không hủy artifact độc lập đã pass.
8. Đo quality, elapsed time, token/tool calls và conflict.
9. Giữ multi-agent chỉ khi evidence tốt hơn baseline hoặc latency gain đáng giá.
