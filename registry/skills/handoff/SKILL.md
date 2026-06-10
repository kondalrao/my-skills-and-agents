---
name: handoff
description: Use when the user asks to prepare a handoff, resume brief, context transfer, or next-session summary for another agent or future session.
---

# Handoff

Use this skill only when the user explicitly asks for a handoff, resume brief, context transfer, next-session summary, or similar artifact.

The goal is to give the next agent enough context to resume without replaying the whole conversation.

## Workflow

1. Gather the current state from the conversation, relevant files, plans, diffs, commands, and existing artifacts.
2. If `.agent/CONTINUITY.md` exists in the current workspace, read it and reference it where useful. Do not update it as part of this skill.
3. Create a Markdown handoff in the OS temp directory.
   - On macOS, prefer `/private/tmp/handoff-<task-slug>-YYYYMMDD-HHMMSS.md`.
   - Derive `<task-slug>` from the handoff focus using lowercase words separated by hyphens.
4. Paste the full handoff in chat after writing the file.
5. If the file cannot be written, paste the full handoff in chat and state the attempted path or failure reason.

## Required Handoff Template

```markdown
# Handoff: <short task title>

## Reason For Handoff
<Why this session is being handed off, why the next agent is needed, and what it should prioritize first.>

## Goal
<The user-visible objective and success criteria.>

## Current State
<What is already done, what is in progress, and what has not started.>

## Key Decisions
<Decisions made so far, including tradeoffs or rejected options when they matter.>

## Important Files And Artifacts
<Paths, URLs, commits, PRs, issues, plans, ADRs, diffs, or temp files the next agent should inspect. Reference existing artifacts instead of copying them.>

## Suggested Skills
<- skill-name: one-line reason this skill is relevant. Include 1-5 skills when applicable.>

## Risks Or Open Questions
<Known blockers, assumptions, sensitive areas, or questions the next agent should resolve.>

## Next Steps
<Ordered, concrete actions for the next agent.>
```

## Content Rules

- `Reason For Handoff` is mandatory. It must explain why the handoff exists and what the next agent needs to do with the context.
- Tailor the handoff to any focus the user gives, such as review, implementation, debugging, validation, or documentation.
- Reference existing PRDs, plans, ADRs, issue threads, commits, diffs, logs, and workspace files by path or URL instead of duplicating them.
- Suggested skills should be names plus one-line reasons, not absolute paths by default.
- Redact obvious secrets such as API keys, passwords, tokens, cookies, private credentials, and credential-bearing URLs.
- If a detail may be sensitive but is important for resuming work, ask before including it.
- Keep the handoff concise, but include enough concrete file paths, commands, decisions, and next actions for another agent to continue safely.
