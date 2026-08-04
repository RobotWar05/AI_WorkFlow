# AI Workflow Operating Rules

Repository này là nguồn chuẩn private-first cho skill, contract và workflow agent đa runtime.

## Start here

1. Đọc yêu cầu hiện tại và instruction gần nhất.
2. Dùng `WORKFLOW.md` để route; không nạp toàn bộ docs/skill.
3. Chọn một workflow, một domain annex và tập skill nhỏ nhất.
4. Dùng contract JSON khi giao việc hoặc tích hợp giữa agent.

## Invariants

- Không bịa file, API, command, measurement, hardware fact hoặc test result.
- Phân biệt verified fact, inference và unknown.
- Một writable path chỉ có một owner trong một attempt.
- Single-owner là mặc định; parallel write cần write-set tách biệt và Git baseline.
- Sub-agent không tự mở rộng quyền; external effect vẫn qua approval gate.
- Worker không được đóng parent task; integrator sở hữu integration và final answer.
- Self-reflection không phải verification; completion cần evidence thực tế.
- Giữ câu trả lời trọng tâm, đủ ý; không kể lại toàn bộ quá trình nếu không cần.

## Source of truth

| Concern | Canonical source |
|---|---|
| Skill procedure | `.agents/skills/` |
| Agent role | `agents/definitions/` |
| Contract | `contracts/schemas/v1/` |
| Mode/policy/state | `orchestration/` |
| Domain acceptance | `domains/` |
| Runtime projection | Generated from canonical definitions |
| Provenance/lifecycle | `registry/` |
| Evidence | `evals/` |

Nguồn tham chiếu đã loại khỏi working tree sau khi được kiểm toán. Provenance ngắn gọn và quyết định chọn lọc còn ở `registry/sources.json`, `docs/reference-audit.md` và `THIRD_PARTY_NOTICES.md`; chúng không phải active instructions.

## Approval and writes

- Workspace write phải nằm trong yêu cầu đã được phê duyệt.
- Knowledge write cần approved diff.
- External communication, deploy, migration, credential, hardware control và destructive action cần approval cụ thể.
- Không hand-edit `.codex/agents/`, `.claude/agents/` hoặc `.agents/agents/`; chạy generator.

## Definition of done

- Deliverable tồn tại và đúng scope.
- Acceptance criteria có passed/failed/inconclusive cùng evidence.
- Relevant validation đã chạy và meaningful output đã được đọc.
- Không có thay đổi ngoài phạm vi hoặc claim vượt quá bằng chứng.
