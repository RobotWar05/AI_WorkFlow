# Token efficiency

## Ngân sách context

- Root map: mục tiêu dưới 120 dòng mỗi file.
- Skill body: mục tiêu dưới 150 dòng; chi tiết đưa vào `references/`.
- Một task chỉ nạp: root map, một workflow, một domain annex và contract liên quan.
- Một delegation packet chỉ chứa context cần cho worker; dùng path và artifact thay vì chép transcript.
- Continuation không lặp lại brief nếu thread vẫn giữ context.

## Chống phình

- Một quy tắc chỉ có một canonical owner.
- Adapter và bảng tổng hợp phải sinh từ canonical data khi có thể.
- Không tạo skill chỉ để chứa checklist tĩnh; đặt checklist trong domain/policy.
- Không thêm framework skill nếu chưa xác nhận stack và version.
- Không lưu raw transcript vào Git; chỉ lưu summary, decision và evidence có giá trị.

## Dấu hiệu cần dọn

- Cùng một rule xuất hiện ở ba file.
- AI phải đọc hơn bốn tài liệu trước khi bắt đầu task thường.
- Description của skill không nói rõ khi nào không dùng.
- Handoff chép toàn bộ hội thoại thay vì trỏ tới artifact.
- Runtime adapter được sửa tay.
