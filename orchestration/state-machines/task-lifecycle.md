# Task lifecycle

```text
DRAFT -> READY -> ASSIGNED -> WORKING -> READY_FOR_REVIEW
      -> READY_FOR_INTEGRATION -> INTEGRATING -> VERIFIED -> COMPLETED
```

## Interrupt states

`INPUT_REQUIRED`, `APPROVAL_REQUIRED`, `BLOCKED`, `FAILED`, `REJECTED`, `CANCELED`, `REWORK`.

## Invariants

- `READY` yêu cầu brief hợp lệ và acceptance criteria có ID.
- `ASSIGNED` yêu cầu owner; delegation yêu cầu write-set và return contract.
- `READY_FOR_INTEGRATION` yêu cầu handoff hợp lệ.
- `VERIFIED` yêu cầu quality gate không còn blocker.
- Chỉ integrator chuyển parent task sang `INTEGRATING`, `VERIFIED`, `COMPLETED`.
- Retry tạo attempt mới; không ghi đè evidence của attempt cũ.
- Resume phải đọc trạng thái bền vững trước khi chạy lại để tránh duplicate execution.
