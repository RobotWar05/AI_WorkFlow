# Full-stack integration annex

Full-stack là composition, không phải mega-skill.

Integrator đọc annex này. Frontend/backend worker chỉ đọc annex của domain mình; không nạp cả hai stack trừ khi task thực sự sở hữu integration.

## Contract trước implementation

- End-to-end user journey và acceptance owner.
- Frontend/backend write ownership.
- API/event schema owner và version.
- State owner, validation boundary và auth/session propagation.
- Backend error -> UI state mapping.
- Optimistic update, rollback và reconciliation nếu có.
- Migration/deploy order và backward compatibility window.
- Cross-layer fixture và rollback path.

## Recommended split

```text
architect: contract + dependency order
backend: provider implementation
frontend: consumer implementation
integrator: schema/version conflict + E2E
verifier: deterministic checks + rendered/runtime evidence
```

Chỉ chạy frontend/backend song song sau khi contract đã được chấp nhận và write-set tách biệt.
