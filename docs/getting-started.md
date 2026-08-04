# Bắt đầu một công việc

## Lối ngắn nhất

1. Viết objective, deliverable, non-goal và acceptance criteria.
2. Chọn một mode:
   - `single-owner`: mặc định.
   - `manager-workers`: subtask độc lập, parent tích hợp.
   - `isolated-parallel`: write-set tách biệt và có Git baseline.
   - `peer-team-experimental`: chỉ thử nghiệm có đo lường.
3. Chọn đúng domain annex.
4. Chạy công việc và lưu evidence trong handoff.
5. Chạy `py tools/workflowctl.py validate` và check riêng của dự án.

## Lệnh

```powershell
py tools/workflowctl.py validate
py tools/workflowctl.py check-adapters
py tools/validate_all.py
```

Kiểm tra một contract cụ thể:

```powershell
py tools/workflowctl.py validate-file contracts/examples/valid/work-item.json --schema work-item.schema.json
```

Sinh lại runtime adapters sau khi sửa canonical agent definition:

```powershell
py tools/workflowctl.py generate-adapters
```

## Chọn tài liệu

| Nếu cần | Đọc |
|---|---|
| Giao một subtask | `workflows/delegated-task.md` |
| Chạy agent đơn | `workflows/single-agent-delivery.md` |
| Chạy song song | `workflows/multi-agent-delivery.md` |
| Tích hợp kết quả | `workflows/integrate-agent-work.md` |
| Task bị lỗi/chặn | `workflows/recover-blocked-task.md` |
| Đánh giá workflow | `workflows/evaluate-agent-system.md` |
| Xây ứng dụng API/SDK | `workflows/api-sdk-application.md` |

Không đọc mọi file “để chắc chắn”. Progressive disclosure là một phần của kiến trúc, không phải tối ưu phụ.
