# Evaluation

## 1. Static gates

```powershell
py tools/validate_all.py
```

Gate kiểm tra skill/profile/registry, trigger coverage, JSON Schema, positive/negative contract fixtures, orchestration semantics, state restrictions, adapter drift, context budget và Markdown link.

Static pass chỉ chứng minh cấu trúc, không chứng minh model behavior hoặc runtime compatibility.

## 2. Agent trial

Mỗi case định nghĩa task, fixture, hard guardrails, outcome checks, acceptable variations và budget. Với output biến thiên, chạy nhiều trial. Ghi runtime/model/version, turns, tool calls, token nếu có, elapsed time, conflict, retry và permission violation.

Ưu tiên grader theo thứ tự:

1. Schema/compiler/test/static analysis.
2. Runtime or rendered-state observation.
3. Human rubric cho judgment quan trọng.
4. LLM judge đã hiệu chuẩn cho phần khó tự động hóa.

Self-reflection hoặc exit code đơn lẻ không đủ làm evidence.

## 3. Paired A/B

Giữ cùng runtime, model, fixture, task và budget:

- A: single-agent hoặc không skill.
- B: delegated/multi-agent hoặc có skill.

Graduation yêu cầu hard guardrail đạt 100%, outcome không thấp hơn baseline và overhead token/time có lý do. Không so hai model khác nhau như một A/B pair.

## 4. Orchestration regressions

Bắt buộc có case cho invalid packet, overlapping write-set, out-of-scope write, stale base, timeout/crash, retry idempotency, wrong final owner, partial failure, prompt injection và secret leakage.

Global `stable` cần evidence riêng trên mỗi runtime. Case bị skip phải ghi `skipped/inconclusive`, không tính là pass.
