# Evaluate an agent system

1. Định nghĩa outcome và hard guardrails trước trial.
2. Giữ runtime, model, fixture và budget tương đương giữa A/B.
3. Chạy nhiều trial khi output có biến thiên.
4. Ưu tiên deterministic grader; LLM judge chỉ dùng cho phần định tính và phải hiệu chuẩn.
5. Đo routing error, duplicate work, permission violation, conflict, retry, turns, tool calls, tokens và latency.
6. Không ép một trajectory duy nhất nếu nhiều cách đều hợp lệ.
7. Graduate chỉ khi hard guardrail đạt, outcome không kém baseline và overhead có lý do.
