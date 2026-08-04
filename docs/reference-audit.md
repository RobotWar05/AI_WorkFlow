# Kiểm toán nguồn tham chiếu lịch sử

Ngày kiểm toán: 2026-08-03. Ngày loại local snapshot: 2026-08-04. Đây là record quyết định và provenance; payload nguồn không còn trong working tree.

## `skills_reference` (đã loại local snapshot)

- Tại thời điểm kiểm toán: 70 file, khoảng 350 KB; có nested Git và ba báo cáo audit chưa track.
- Có giá trị ở governance, progressive disclosure, debugging và handoff.
- Nhãn `Stable` cũ không có đủ eval để coi là bằng chứng.
- Một số rule embedded dùng thông số tuyệt đối hoặc khẳng định sai; không nhập nguyên trạng.
- `structured-response` là personalization, không phải capability skill.

## `projects_reference_vinqa` (đã loại local snapshot)

- 78 `SKILL.md`: API 41, client 37.
- 25 common skill bị sao chép giữa hai repo; 90 file trùng byte-for-byte, tạo khoảng 193,148 byte dư thừa.
- Không có `evals/` hoặc `scripts/` dù skill creator nội bộ yêu cầu eval-driven workflow.
- 24 Markdown link target bị thiếu.
- Router theo đuôi file làm một số common skill không thể được phát hiện; cả hai router còn nói có `.skillsrc` dù file đó không tồn tại.
- Nội dung drift so với stack thực tế: dự án đã dùng Spring Boot 4.0.5, Java 21, React 19.2.5, TypeScript 6.0.2 và Vite 8.0.10, trong khi nhiều skill vẫn hướng dẫn phiên bản cũ.
- Quarantine các skill tự ghi learning log, tự sửa skill, auto-fix feedback, telemetry rộng, hoặc DAST không có authorization gate.

## Quyết định

Chỉ adapt các cấu trúc có thể kiểm chứng: scientific debugging, boundary/data-flow checklist, progressive disclosure, trigger eval và design direction có phạm vi. Không sao chép router, telemetry, các lệnh tool riêng runtime, rule bảo mật tuyệt đối, hoặc nội dung framework chưa kiểm tra phiên bản. Các derivative đang active được kiểm soát bởi source-of-truth hiện tại, không phụ thuộc local snapshot.
