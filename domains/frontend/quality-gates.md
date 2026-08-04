# Frontend quality gates

- G0: brief có user journey, states, viewport và acceptance IDs.
- G1: component/data ownership không mơ hồ; API dependency có source.
- G2: build/type/lint và focused tests có evidence.
- G3: loading/empty/error/disabled được kiểm tra.
- G4: keyboard, focus, semantics và representative viewports được quan sát.
- G5: performance và browser claims chỉ ghi “passed” khi đã đo.

Mọi mục chưa kiểm tra là `inconclusive`, không phải `passed`.
