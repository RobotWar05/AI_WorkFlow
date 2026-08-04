# Embedded delivery annex

## Inputs bắt buộc

- Board/MCU, pin map, clock, memory và toolchain version đã xác minh.
- Sensor/actuator/communication contract và datasheet source.
- Timing budget, sample/control rate và worst-case path.
- State machine, safe state, timeout và watchdog behavior.
- ISR/task ownership, shared resources và initialization order.
- Noise, disconnect, brownout, reset và communication failure behavior.
- Bench/HIL/simulator/test evidence có thể thu thập an toàn.

## Defaults

- Non-blocking; polling có timeout.
- ISR ngắn; không cấp phát động bừa bãi.
- Hardware control/flash là E6 và cần approval.
- Chưa xác minh phần cứng thì ghi assumption/unknown, không bịa thông số.
