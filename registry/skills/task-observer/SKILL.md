---
name: task-observer
description: Use when observing repeated task patterns, skill gaps, reusable workflow
  candidates, or improvements that should become durable skills.
---

# Task Observer

Observe task work for repeated patterns, skill gaps, and durable improvements without interrupting the main task.

## Routing

Use this skill when:
- Repeated behavior suggests a new or improved skill.
- A task exposes a reusable script, validation check, template, or reference.
- A completed workflow should be reviewed for skill-catalog improvements.

Do not use it to implement skill edits directly. Route concrete skill edits through `local-skill-lifecycle-manager` and skill creation guidance.

## Core Workflow

1. Watch for repeated manual work, recurring corrections, missing verification, or duplicated skill behavior.
2. Record only high-signal observations; do not store transcripts, secrets, or raw logs.
3. Classify observations as new-skill candidates, existing-skill improvements, reusable tools/scripts, or cross-cutting principles.
4. Surface observations only when they materially affect future work or the user asks for a review.
5. Preserve confidentiality and strip project-specific sensitive details before proposing reusable skills.

## Detailed Protocol

Read `references/full-task-observer-protocol-2026-05-20.md` for the full observation taxonomy, logging formats, review cadence, confidentiality safeguards, and delivery workflow.

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Work Force
- Break complex work into roles, dependencies, checkpoints, and handoff-ready tasks.
- Identify what can run in parallel, what must be sequenced, and what needs a primary owner.
- Define completion evidence for each workstream.
- Keep coordination overhead proportional to the task size.

