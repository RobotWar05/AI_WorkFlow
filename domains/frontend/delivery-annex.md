# Frontend delivery annex

Đọc file này khi task thay đổi route, component, interaction hoặc rendered UI.

## Brief bắt buộc

- User journey và route/component scope.
- Design source, token hoặc visual direction; nêu rõ phần được phép suy luận.
- Data/API dependency và state owner.
- Trạng thái: loading, empty, error, success, disabled và offline nếu liên quan.
- Viewport/browser matrix.
- Keyboard, focus, semantics và accessible name.
- Performance budget và test scope.

## Delivery flow

```text
brief -> information architecture -> component/state/data boundary
      -> implementation -> interaction/accessibility tests
      -> rendered review -> verification handoff
```

Không tuyên bố responsive hoặc accessible chỉ từ source review. Phải quan sát giao diện đại diện khi runtime cho phép.
