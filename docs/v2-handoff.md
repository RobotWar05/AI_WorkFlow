# V2 handoff

## Đã hoàn thành

- V2 control plane: work item, delegation, artifact, handoff, integration, quality gate, lifecycle và approval policy.
- 9 canonical role cards; Codex, Claude và Antigravity projections sinh từ cùng nguồn.
- Domain annex cho frontend, backend/API, full-stack và embedded.
- API/SDK application route, typed tool contract và bounded fixture.
- Route registry: bốn entry path cho backend, frontend delegation, full-stack parallel và API/SDK.
- Static gates: schema, negative fixture, ownership/state semantics, adapter drift, skill triggers, unit tests và Markdown links.

## Bắt đầu phiên sau

1. Chạy `py tools/workflowctl.py status`.
2. Chọn route trong [`registry/routes.json`](../registry/routes.json); chỉ đọc `must_load` của route đó.
3. Tạo task bằng [`contracts/templates/task-brief.md`](../contracts/templates/task-brief.md).
4. Chạy `single-owner` trước. Chỉ delegate khi task có return contract và write-set độc quyền.
5. Trước bàn giao, chạy `py tools/validate_all.py` cùng check riêng của dự án.

## Prompt copy-ready

```text
Làm việc trong E:\AI_Workflow. Đọc AGENTS.md và WORKFLOW.md trước.
Chọn route phù hợp trong registry/routes.json; chỉ nạp must_load của route.
Tạo/kiểm tra work item theo contracts/schemas/v1/work-item.schema.json.
Giữ single-owner nếu chưa chứng minh được lợi ích của delegation.
Nếu delegate: dùng delegation packet, exclusive write-set, budget và handoff evidence.
Không tuyên bố hoàn tất nếu acceptance criteria chưa có evidence thực tế.
Cuối phiên: báo deliverable, validation đã chạy, risk/unknown và next action.
```

## Trạng thái xác minh

Verified on 2026-08-04: static validation pass; 11 skill/88 trigger cases; 9 Python unit tests; adapter drift check pass. Xem `tools/validate_all.py` và `tools/workflowctl.py`.

## Chưa được tuyên bố

- Chưa có initial Git commit nên `isolated-parallel`/worktree chưa sẵn sàng.
- Adapter Codex/Claude/Antigravity mới static-validated, chưa có paired behavioral A/B.
- Claude adapter chưa local runtime-test vì Claude CLI chưa có.
- Không có production deployment, credential, hardware hoặc external-write test nào đã chạy.
