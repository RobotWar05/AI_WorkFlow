# Execution modes

| Mode | Dùng khi | Không dùng khi |
|---|---|---|
| `single-owner` | Task tuần tự, shared context, cùng file | Có nhiều nhánh độc lập đáng kể |
| `manager-workers` | Bounded research/review/implementation trả về parent | Worker cần trao đổi ngang hàng liên tục |
| `isolated-parallel` | Tối thiểu hai write-set độc lập, có integrator và Git baseline | Chưa có commit nền hoặc ownership chồng lấn |
| `peer-team-experimental` | Peer communication tạo giá trị đo được | Task nhỏ, tuần tự, budget thấp hoặc runtime chưa ổn định |

## Decision gate

Chỉ dùng nhiều agent khi tất cả điều kiện sau đúng:

1. Có ít nhất hai workstream thực sự độc lập.
2. Mỗi workstream có return contract và acceptance riêng.
3. Write-set không chồng lấn hoặc có isolation thật.
4. Có integrator và merge order.
5. Cost/latency budget được chấp nhận.
6. Failure của một worker không làm mất toàn bộ run.

Nếu bất kỳ điều kiện nào thiếu, dùng `single-owner` hoặc `manager-workers` read-only.
