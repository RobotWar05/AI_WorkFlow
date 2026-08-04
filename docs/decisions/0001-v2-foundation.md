# ADR-0001: V2 Foundation

- Trạng thái: accepted
- Ngày: 2026-08-03
- Phạm vi: workflow repository

## Quyết định

- Giữ skill nhỏ; đưa coordination vào contract và workflow.
- Dùng JSON + JSON Schema làm canonical machine contract; Markdown làm form cho người.
- Dùng single-owner làm mặc định và một integrator làm final owner.
- Sinh runtime adapter từ canonical agent definition, không duy trì ba bản bằng tay.
- Giữ peer-team ở trạng thái experimental.
- Không bật parallel-write bằng worktree trước khi repository có initial commit.

## Lý do

Kiến trúc này giảm instruction trùng lặp, cho phép validation cơ học và giữ khác biệt runtime ở boundary. Nó cũng ngăn worker tự mở rộng quyền hoặc tuyên bố parent task hoàn tất.

## Không chọn

- Một mega-skill cho mọi domain: context lớn, trigger mơ hồ và khó eval.
- Một workflow riêng cho từng runtime: nhanh drift và khó so sánh.
- Multi-agent mặc định: tăng coordination cost khi task không độc lập.

## Tiêu chí chấp nhận V2 Foundation

- Contract/schema hợp lệ và có positive/negative fixtures.
- Role, mode, domain, handoff và integration ownership có tài liệu rõ.
- Adapter sinh lặp lại được và drift check pass.
- Skill orchestration có trigger suite.
- Toàn bộ static validation pass.
- Claim runtime chỉ giới hạn ở runtime đã thực sự smoke-test.
