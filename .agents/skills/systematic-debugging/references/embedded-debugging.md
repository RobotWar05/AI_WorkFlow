# Embedded debugging

Capture the board revision, firmware revision, clocking, reset reason, power conditions, peripheral configuration, and a timestamped event trace.

Check these failure classes explicitly when relevant:

- initialization and startup order;
- blocking waits and missing timeouts;
- interrupt latency, ISR workload, and interrupt safety;
- shared-state races, priority inversion, and deadlock;
- stack exhaustion, heap fragmentation, lifetime errors, and buffer bounds;
- integer overflow, counter wraparound, unit mismatch, and timing jitter;
- electrical noise, signal integrity, brownout, and peripheral recovery;
- watchdog resets that hide the blocked subsystem.

Prefer instrumentation that changes timing as little as practical. Treat a failure that disappears under logging as timing evidence, not proof of a fix.
