# Backend quality gates

- G0: boundary, invariant, data owner và risk đã rõ.
- G1: API/data contract được version và có error model.
- G2: auth, validation, timeout, retry, idempotency và concurrency được xử lý theo scope.
- G3: unit/integration/contract checks có command, exit code và evidence.
- G4: migration/rollout/rollback được xác định; chưa chạy nếu thiếu approval.
- G5: observability đủ để phát hiện và chẩn đoán failure path chính.
