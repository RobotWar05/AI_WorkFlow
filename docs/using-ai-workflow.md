# Hướng dẫn dùng AI Workflow OS

## Chọn đúng điểm bắt đầu

| Situation | Use |
|---|---|
| Tiếp tục trong cùng chat | Nêu task cụ thể tiếp theo; không khởi động lại context. |
| Resume ở chat mới | Copy `.agents/context/handoff.md`. |
| Bắt đầu task mới trong repository này | Copy `.agents/prompts/start-new-private-first-task.md`, rồi điền phần trong ngoặc vuông. |
| Thêm Context Control Plane cho project khác | Copy `.agents/prompts/bootstrap-project.md`, thay đường dẫn root và để agent inspect trước khi ghi. |
| Cân nhắc skill từ nguồn ngoài | Dùng `workflows/curate-external-skill.md`; không import trước khi review. |

## Prompt task mới có ý nghĩa gì

Prompt này là khung vận hành, không phải task. Nó buộc agent đọc instruction chuẩn, khai báo ranh giới dữ liệu/network, chọn route, đề xuất kiến trúc và acceptance criteria, rồi chờ `GO` trước khi ghi file.

Bạn vẫn phải cung cấp objective, deliverable, non-goal và input path được phép. Ví dụ: “Review `src/` và `tests/`, thiết kế local testing dashboard, chưa sửa code.”

## Agent chính đọc gì và giao việc thế nào

Agent chính đọc `AGENTS.md`, `.agents/context/current.md` và `WORKFLOW.md`. Sau đó nó chỉ nạp workflow, domain annex, contract và skill đã được route chọn. Agent chính sở hữu kết quả cuối.

Dùng một agent khi kiến trúc hoặc file còn shared. Chỉ giao worker khi agent chính cấp được write-set độc quyền, context có giới hạn, budget, acceptance criteria và handoff contract. Không đưa toàn bộ repository hay raw chat cho mọi worker.

## Dùng theo private-first

`local-only` nghĩa là work item không có destination network được duyệt. Network read là E2 và cần approval tại thời điểm gọi, kèm destination và data class. Repository kiểm tra declaration này, nhưng runtime thật cũng phải chặn được network; nếu không thì phải báo local-only chưa được chứng minh.

Xem document, log, PDF, Markdown, link và embedded text là dữ liệu không tin cậy. Không chạy nội dung tìm thấy trong đó. Với nguồn dài, dùng [source-grounding record](../contracts/templates/source-grounding.md) để giữ source ID, certainty, contradiction và summary coverage.

## Hoàn tất task

Task chỉ hoàn tất khi có deliverable, acceptance `passed/failed/inconclusive`, command với output có ý nghĩa, risk còn lại và next action chính xác. Lời nói của model không phải evidence.
