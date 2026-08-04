---
name: embedded-system-design
description: Design or review embedded firmware and automation under real hardware, timing, memory, concurrency, communication, and recovery constraints. Use for MCU architecture, RTOS tasks, state machines, peripherals, protocols, control loops, watchdogs, or safety-relevant device behavior; layer with debugging for observed faults and architecture-first for cross-component structural decisions.
---

# Embedded System Design

Start from measured or documented hardware constraints. Do not invent MCU resources, peripheral behavior, timing limits, or library APIs.

## Architecture Workflow

1. Identify the board, MCU, clocks, memory, peripherals, electrical interfaces, toolchain, and operational environment.
2. Define inputs, outputs, safety states, timing deadlines, update rates, and acceptance tolerances.
3. Separate hardware access, drivers, services, domain logic, communication, and application orchestration.
4. Model behavior with explicit state and events when more than one mode or recovery path exists.
5. Build a timing and concurrency model: execution budgets, priorities, shared resources, ISR boundaries, and worst credible blocking.
6. For operations that can exceed a deadline or stall liveness, define bounded behavior: timeout, cancellation, supervised blocking, or documented proof that indefinite waiting is safe. Bound retries and define recovery.
7. Budget static memory, stack, heap, buffers, queues, and persistent storage.
8. Define startup, calibration, degraded mode, watchdog behavior, safe shutdown, and reset recovery.
9. Add observability that can distinguish timing, communication, power, and logic faults.
10. Plan host tests, simulation, hardware-in-loop tests, and fault injection appropriate to the risk.

Read [references/reliability-checklist.md](references/reliability-checklist.md) before implementation or review.

## Default Biases

Prefer non-blocking state progression, short ISRs, explicit ownership, bounded queues, monotonic timing, and deterministic memory use where constraints justify them. These are design biases, not absolute rules: justify exceptions with measured constraints.
