---
name: cc-godmode
description: Use when coordinating a broad multi-agent development workflow that needs
  research, architecture, implementation, validation, testing, and release handoffs.
---

# CC Godmode

Coordinate broad multi-agent development workflows by choosing the right specialist path and enforcing quality gates.

## Routing

Use this only for large, multi-stage work that genuinely needs orchestration across research, architecture, implementation, validation, UX testing, and release notes.

Prefer narrower skills when the task has a single focus:
- `workflow-orchestration` for general step coordination.
- `ai-agents-architect` for agent-system architecture.
- `code-review-agent` for review stance.
- `debugging-agent` or `systematic-debugging` for root-cause work.
- `refactor` or `refactor-plan` for scoped refactors.

## Core Workflow

1. Classify the request: feature, bug, API change, refactor, release, process issue, or research.
2. Assign only the necessary specialist roles; avoid multi-agent overhead for narrow work.
3. Require implementation validation and user-facing quality checks before release-style handoff.
4. Keep API changes on the critical path with explicit consumer impact review.
5. Produce concise handoff reports with decisions, changed files, validation, risks, and next steps.

## Detailed Manual

Read `references/full-cc-godmode-manual-2026-05-20.md` for the legacy role matrix, workflow variants, quality gates, and report templates.
