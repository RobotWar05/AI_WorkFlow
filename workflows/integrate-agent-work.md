# Integrate agent work

1. Validate integration plan và mọi handoff.
2. Reject out-of-scope writes, stale base, missing evidence hoặc invalid artifact.
3. Tích hợp theo dependency/merge order, không theo thời điểm worker trả về.
4. Resolve conflict công khai; không tự chọn một bên mà thiếu criterion.
5. Chạy checks sau từng boundary rủi ro và toàn hệ thống cuối cùng.
6. Ghi quality gate; failed/inconclusive chuyển `REWORK`.
7. Integrator là final-answer owner và là role duy nhất đóng parent task.
