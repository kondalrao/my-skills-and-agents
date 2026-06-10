---
name: developer-growth-analysis
description: Use when the user asks to analyze recent coding sessions, chat history,
  commits, or task work to identify developer strengths, recurring gaps, improvement
  areas, learning resources, and actionable growth plans.
---

# Developer Growth Analysis

## Local Metadata Notes

- Former frontmatter `metadata`: short-description=Analyze developer growth from recent work

Use this skill to produce an evidence-based developer growth report from the user's recent work. The goal is not generic coaching. Ground every insight in observable work history, then turn patterns into prioritized learning actions.

This skill is distinct from `personal-teacher-mentor` and `mentor-teacher`. Those skills create a learning synthesis after a task. This skill analyzes a time window across one or more sessions or projects to find recurring patterns.

This skill is distinct from `reflect-on-changes`. That skill updates repository knowledge and proposes mechanical checks. This skill focuses on the developer's growth, study plan, strengths, and repeated skill gaps.

## Use When

- The user asks for developer growth, skill gaps, coaching, improvement areas, or a retrospective over recent coding work.
- The user asks to analyze recent chats, sessions, commits, PRs, or task logs.
- The user wants targeted learning resources based on actual work patterns.
- The user wants a weekly or daily report with strengths, gaps, action items, and a focused study plan.
- The user wants a report they can share with a mentor or revisit later.

## Skip When

- The user only wants a learning note for the just-completed task; use `personal-teacher-mentor`.
- The user wants repository docs or lint-rule candidates updated after a code change; use `reflect-on-changes`.
- There is no accessible work history and the user does not provide examples.
- The request is only a code review, debugging session, or implementation task.

## Inputs

Use the narrowest relevant evidence source available:

- current conversation and tool activity
- local Codex session history under `~/.codex/sessions` when relevant
- `~/.codex/history.jsonl` or equivalent local history if present
- recent commits, PRs, review comments, diffs, test failures, or issue notes
- user-provided summaries, logs, pasted code, or project notes

State which sources were inspected. If a source is missing, say so and continue
with the best available evidence.

## Analysis Workflow

1. Define the report window:
   - default to the last 24-48 hours for "recent" unless the user specifies a range.
2. Gather evidence:
   - identify projects, technologies, task types, repeated questions, failures, course corrections, review findings, and successful patterns.
3. Extract work patterns:
   - problem domains, tools used, debugging style, planning style, validation habits, code quality risks, and collaboration behavior.
4. Identify 3-5 improvement areas:
   - each must be specific, evidence-based, actionable, and prioritized.
5. Identify strengths:
   - name behaviors to continue, not generic compliments.
6. Curate learning resources:
   - prefer official docs, primary sources, respected essays, papers, or high signal discussions.
   - for Hacker News resources, search HN only when live web/search tools are available or provide search queries the user can run.
7. Produce the report:
   - make it scan-friendly, concrete, and usable for the next week.
8. Optional delivery:
   - send to Slack only if a Slack connector/tool is available and the user explicitly wants delivery there. Otherwise, return the report in chat or save it where the user requested.

## Evidence Rules

- Do not infer a growth gap from one isolated typo or one-off mistake.
- Do not overstate confidence when evidence is thin.
- Quote or cite enough concrete examples for each major finding.
- Separate observed behavior from interpretation.
- Treat sensitive content, secrets, private code, and customer data as confidential; summarize without exposing them.
- If using web resources, prefer current, authoritative sources and include links. Do not invent article titles, dates, engagement, or URLs.

## Report Template

```markdown
# Developer Growth Report

**Report Period**: <date range>
**Evidence Sources**: <sessions, commits, PRs, notes, chat history>
**Last Updated**: <timestamp>

## Work Summary
<2-3 short paragraphs covering projects, technologies, task types, and focus.>

## Improvement Areas

### 1. <Area name>
**Why this matters**: <impact on current work>
**What I observed**: <specific evidence>
**Recommendation**: <concrete next step>
**Time to skill up**: <small estimate or practice window>

## Strengths Observed
- <specific behavior to keep>

## Action Items
1. <highest impact action>
2. <next action>
3. <next action>

## Learning Resources
### For: <Improvement area>
1. [<Title>](<URL>) - <why this helps>

## Follow-up Check
<what to review in a week to see whether the pattern improved>
```

## Resource Curation

For each improvement area, include 1-3 resources. Good resources are:

- official docs for language, framework, or tool gaps
- vendor or project guides for production practices
- well-regarded technical essays or postmortems
- conference talks, papers, or tutorials with concrete examples
- Hacker News discussions only when they add useful practitioner perspective

If live search is unavailable, include precise search prompts instead:

```text
Search: site:news.ycombinator.com <technology> <pattern> best practices
Search: <official docs> <specific gap>
```

## Quality Bar

- Every improvement area has evidence and an action.
- Every recommendation is practical within the user's actual project context.
- Strengths are specific enough to repeat deliberately.
- Learning resources map directly to the observed gaps.
- The report is honest, not motivational filler.
- The next follow-up is clear enough to run another growth analysis later.

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Inspire Lestrade
- Clarify audience, positioning, desired action, and emotional hook before writing.
- Generate campaign or narrative angles that connect product value to reader motivation.
- Separate attention-grabbing framing from unsupported hype.
- Keep recommendations actionable for publication or execution.

