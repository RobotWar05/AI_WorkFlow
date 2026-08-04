# API contract annex

## Contract

- Method/transport, path/topic và version.
- Request, response, event và error schemas.
- Authentication và authorization decision point.
- Validation boundary; không tin shape từ model hoặc client.
- Idempotency key, ordering và concurrency semantics nếu có write.
- Timeout, retry ownership, rate limit và pagination.
- Compatibility, deprecation và migration window.
- Example không chứa secret hoặc production data.

## Verification

- Schema parse/validation.
- Positive, invalid, unauthorized, forbidden, not-found, conflict và timeout cases.
- Consumer/provider contract test khi có nhiều thành phần.
- OpenAPI chỉ dùng khi phù hợp với transport; specification không thay thế runtime test.
