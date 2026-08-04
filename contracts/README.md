# Contracts

JSON Schema là nguồn máy đọc được; Markdown template là form ngắn cho người.

| Trao đổi | Schema | Form |
|---|---|---|
| Parent task | `schemas/v1/work-item.schema.json` | `templates/task-brief.md` |
| Parent -> worker | `schemas/v1/delegation-packet.schema.json` | `templates/delegation-packet.md` |
| Worker -> parent | `schemas/v1/handoff.schema.json` | `templates/worker-handoff.md` |
| Multi-result integration | `schemas/v1/integration-plan.schema.json` | `templates/integration-plan.md` |
| Completion evidence | `schemas/v1/quality-gate.schema.json` | `templates/quality-gate.md` |

Máy dùng JSON; không parse Markdown form để ra quyết định an toàn. Version mới không được âm thầm thay đổi semantics của `v1`.
