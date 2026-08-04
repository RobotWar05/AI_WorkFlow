# API/SDK application

Use this runbook to build an application that calls an agent SDK or exposes typed tools. It is separate from `adapters/`, which only generates IDE/CLI agent definitions.

1. Create a work item with provider, runtime, model policy, user-visible outcome, tool boundaries, data classification and external-effect limits.
2. Keep deterministic policy outside the model: routing, authorization, approval, retries, task state and completion criteria belong to application code.
3. Define each tool with `tool-contract/v1`: schema, timeout, idempotency, effect class, approval and error codes.
4. Implement one provider adapter behind a narrow application interface. Do not leak vendor transcript into canonical task state.
5. Add a fixture, deterministic tool tests, failure/timeout tests and redaction-aware trace policy.
6. Run a single-agent baseline before adding handoff or multiple agents. Use SDK-specific orchestration only behind the same canonical contracts.
7. Keep deployment, credentials and external writes action-time approved.

Fixture: `evals/fixtures/api-sdk/application-work-item.json`.
