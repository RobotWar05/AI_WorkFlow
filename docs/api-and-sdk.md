# API và SDK workflow

## Boundary

Repository contracts là provider-neutral. SDK adapter chỉ chuyển contract thành cấu hình typed cho runtime; không đặt business state trong prompt hoặc vendor transcript.

```text
application request
  -> deterministic policy/router
  -> work item + approval state
  -> agent runner / handoff
  -> typed tool boundary
  -> artifact + trace + quality gate
  -> application response
```

## Provider routes

- OpenAI application: ưu tiên [Agents SDK](https://openai.github.io/openai-agents-python/) khi cần agent-as-tool, handoff, guardrail, session và tracing. Responses API là model/tool boundary; application vẫn sở hữu authorization và business state.
- Anthropic application: dùng [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) cho loop/tools/permissions/hooks; không phụ thuộc Claude Code Agent Teams experimental.
- Google application: dùng [Google ADK](https://adk.dev/) cho sequential/parallel/loop workflows, session và eval; Antigravity definitions chỉ là IDE adapter.
- Remote agent system: dùng [A2A](https://a2a-protocol.org/latest/specification/) ở network boundary, với authentication và capability discovery riêng.

## API requirements

- Parse input/output tại boundary bằng schema.
- Tool có side-effect class, timeout, error model, idempotency và approval rule.
- Không truyền secret qua prompt, handoff hoặc artifact.
- Retry external write chỉ khi có idempotency key hoặc recovery contract.
- Trace phải redaction-aware; raw transcript không tự trở thành durable knowledge.
- Completion dựa trên application state/evidence, không dựa trên final text của model.

Provider-specific adapter code chỉ nên được thêm khi có application fixture và credential/test boundary rõ.

## Execution route

Start with [`workflows/api-sdk-application.md`](../workflows/api-sdk-application.md) and the bounded fixture at [`evals/fixtures/api-sdk/application-work-item.json`](../evals/fixtures/api-sdk/application-work-item.json). `adapters/` only generates runtime agent definitions; it is not application integration code.
