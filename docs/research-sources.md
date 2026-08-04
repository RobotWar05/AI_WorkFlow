# Research sources

Danh sách này chỉ giữ nguồn tác động trực tiếp tới kiến trúc. Pin/license của community skill nằm trong `registry/sources.json`.

## Runtime và harness

- [OpenAI: Harness engineering](https://openai.com/index/harness-engineering/): repo knowledge là system of record, AGENTS là bản đồ, invariant được kiểm tra cơ học.
- [OpenAI Symphony specification](https://github.com/openai/symphony/blob/main/SPEC.md): workflow trong repo, single authoritative orchestrator state, bounded concurrency/retry và isolated workspace.
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/): agent, handoff, guardrail, session và tracing cho ứng dụng.
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents): agent definition, tools, permission và worktree isolation.
- [Claude Code agent teams](https://code.claude.com/docs/en/agent-teams): experimental; không dùng làm portable baseline.
- [Antigravity subagents](https://antigravity.google/docs/subagents): custom agent, tool allowlist, lifecycle và workspace mode.
- [Google ADK](https://adk.dev/): deterministic workflow/agent runtime cho ứng dụng Google-oriented.
- [A2A specification](https://a2a-protocol.org/latest/specification/): remote agent card, task, message và artifact; dùng ở adapter boundary.

## Khoa học và evaluation

- [Least-to-Most Prompting](https://arxiv.org/abs/2205.10625): decomposition theo dependency có thể cải thiện compositional tasks; không phải lý do chia mọi task.
- [SWE-agent](https://papers.nips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html): tool/agent-computer interface ảnh hưởng kết quả.
- [Intrinsic self-correction limits](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html): reflection không thay thế external verification.
- [Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/): context dài không đảm bảo sử dụng thông tin đồng đều.
- [Anthropic: Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): just-in-time retrieval, compaction và artifact references.
- [Anthropic: Multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system): multi-agent phù hợp breadth-first independent work, có coordination/token cost lớn.
- [Anthropic: Agent evals](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents): outcome + transcript metrics, nhiều grader và nhiều trial.
- [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf): governance, provenance, TEVV và human oversight.

## Standards

- [JSON Schema 2020-12](https://json-schema.org/draft/2020-12/json-schema-core)
- [OpenAPI 3.1.1](https://spec.openapis.org/oas/v3.1.1.html)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)

## Community discovery

- [Goon Nguyen](https://goonnguyen.substack.com/p/toi-a-sai-ve-agent-skills-va-cach), [skills.sh](https://www.skills.sh/), [Ponytail](https://github.com/DietrichGebert/ponytail), [Kepano Obsidian Skills](https://github.com/kepano/obsidian-skills).

Popularity chỉ dùng để discovery. Mọi adoption phải đọc toàn bộ source, external call, license, revision, write behavior, token footprint và local eval.
