# Embedded reliability checklist

## Timing and concurrency

- Are deadlines and worst-case execution assumptions stated with units?
- Can a counter wrap, scheduler delay, or retry storm break the design?
- Is shared state atomic, locked, message-passed, or otherwise owned explicitly?
- Are ISR-to-task handoffs bounded and safe?

## Resources

- Are stack high-water marks and buffer capacities measurable?
- Is dynamic allocation avoided only where fragmentation or determinism matters, rather than by superstition?
- Can queue overflow, log growth, or persistent-write wear occur?

## Failures

- Can an external interaction fail to return or exceed its deadline? If so, define timeout or cancellation and a meaningful failure state.
- Does the watchdog supervise liveness instead of being fed indiscriminately?
- Can the device return to a safe state after brownout, reset, corrupt input, or partial initialization?
- Are calibration data and hardware assumptions versioned and validated?
