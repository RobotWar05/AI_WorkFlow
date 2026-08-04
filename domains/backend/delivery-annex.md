# Backend delivery annex

Đọc file này khi task thay đổi service, API, event, job, persistence hoặc backend integration.

## Brief bắt buộc

- Service boundary, domain invariants và data owner.
- API/event/job contract và compatibility policy.
- Authentication, authorization và trust boundary.
- Persistence, migration, transaction, concurrency và idempotency.
- Error model, timeout, retry và degraded behavior.
- Logs, metrics, traces và correlation identifiers.
- Unit, integration, contract, performance và recovery checks phù hợp.
- Rollout và rollback; production effect luôn approval-gated.

## Delivery flow

```text
domain contract -> boundary schema -> persistence/reliability design
                -> implementation -> deterministic tests
                -> observability/recovery check -> handoff
```
