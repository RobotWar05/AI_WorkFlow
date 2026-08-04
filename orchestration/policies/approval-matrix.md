# Approval matrix

| Effect class | Ví dụ | Mặc định |
|---|---|---|
| E0 Read local | Đọc file, status, log | Cho phép trong scope |
| E1 Reversible workspace write | Sửa source/docs được yêu cầu | Cho phép khi user đã yêu cầu triển khai |
| E2 Network read | Tài liệu, API GET không nhạy cảm | Cho phép khi research được yêu cầu |
| E3 External write/communication | Issue, email, PR comment, upload | Cần approval cụ thể |
| E4 Deploy/migration/production | Deploy, DB migration, production API | Cần approval tại thời điểm chạy |
| E5 Identity/credential/payment | Login, OTP, KYC, ngân hàng | User kiểm soát; agent không tự đại diện |
| E6 Hardware control | Flash, actuator, đổi controller | Cần approval và recovery plan |
| E7 Destructive | Delete, force reset, irreversible rewrite | Cần target chính xác và approval riêng |

## Delegation rules

- Worker không thừa hưởng quyền chỉ vì parent có quyền.
- Delegation packet phải ghi effect class tối đa.
- Agent không được né approval bằng cách giao hành động cho agent khác.
- Secret chỉ truyền qua runtime secret mechanism, không ghi vào contract, log hoặc artifact.
