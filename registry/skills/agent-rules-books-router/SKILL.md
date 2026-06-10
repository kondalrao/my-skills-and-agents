---
name: agent-rules-books-router
description: Use when coding work should be guided by book-derived software-engineering rule sets, especially for refactoring, review, architecture, legacy code, reliability, data systems, domain modeling, or implementation discipline.
---

# Agent Rules Books Router

## Purpose

Use this skill to apply one focused local rule set from `agent-rules-books` during coding work. The skill is offline-first: use bundled files under `references/upstream/` and do not fetch remote docs at runtime.

The core operating rule is: choose the smallest mechanism that still changes the coding decision.

## Routing Workflow

1. Classify the task before coding.
2. Select one primary local `*.mini.md` rule file from `references/source-index.md`.
3. Read that local `mini` file before planning or editing.
4. Use `*.nano.md` only when the user asks for a very small always-on baseline or cross-tool portable rule.
5. Use the full `*.md` file only for audits, deep design sessions, rule derivation, or explicit exhaustive guidance.
6. If two rule sets are relevant, name the primary and secondary pressure. Keep the primary tied to the user's requested outcome.

## Default Routes

- Everyday implementation, readability, naming, small functions, tests: `references/upstream/clean-code/clean-code.mini.md`
- Broad construction discipline, defensive programming, implementation quality: `references/upstream/code-complete/code-complete.mini.md`
- Reducing complexity, designing deeper modules, simplifying interfaces: `references/upstream/a-philosophy-of-software-design/a-philosophy-of-software-design.mini.md`
- Architecture boundaries, dependency direction, framework isolation: `references/upstream/clean-architecture/clean-architecture.mini.md`
- Behavior-preserving cleanup: `references/upstream/refactoring/refactoring.mini.md`
- Code smells and practical cleanup tactics: `references/upstream/refactoring-guru/refactoring-guru.mini.md`
- Risky legacy changes, characterization tests, dependency breaking: `references/upstream/working-effectively-with-legacy-code/working-effectively-with-legacy-code.mini.md`
- Production reliability, failure modes, timeouts, retries, observability: `references/upstream/release-it/release-it.mini.md`
- Data consistency, schema evolution, replication, streams, distributed systems: `references/upstream/designing-data-intensive-applications/designing-data-intensive-applications.mini.md`
- Domain modeling, ubiquitous language, bounded contexts: `references/upstream/domain-driven-design/domain-driven-design.mini.md`
- Lightweight DDD, subdomains, context mapping: `references/upstream/domain-driven-design-distilled/domain-driven-design-distilled.mini.md`
- Aggregates, domain events, application architecture: `references/upstream/implementing-domain-driven-design/implementing-domain-driven-design.mini.md`
- Enterprise application layering, service layer, repositories, unit of work: `references/upstream/patterns-of-enterprise-application-architecture/patterns-of-enterprise-application-architecture.mini.md`
- General engineering judgment, feedback loops, automation, DRY at knowledge level: `references/upstream/the-pragmatic-programmer/the-pragmatic-programmer.mini.md`

## Interaction With Other Local Skills

This skill chooses book-derived decision pressure. It does not replace local operational skills.

- For actual refactoring execution, combine with `refactor` or `refractoring-agent` when those skills trigger.
- For review output format and severity ordering, follow `code-review-agent`.
- For ADR artifacts, use `architecture-decision-records`.
- For language, framework, infrastructure, or domain-specific implementation, keep the relevant local skill primary and use this router only as supporting design pressure.

## Offline Contract

- Runtime guidance must come from bundled local files.
- Remote URLs in `references/source-index.md` are provenance only.
- If a bundled file is missing, stop and report the missing file instead of searching the web.
- When maintaining this skill, run `ruby scripts/validate_offline_bundle.rb` from the skill directory before claiming it is valid.
