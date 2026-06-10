---
name: clarify
description: Use when a vague, messy, voice-dictated, multi-part, or stress-test request
  should become a clean self-contained prompt before execution.
---

# Clarify

## Overview

Use this to turn an unclear ask into a prompt artifact that a fresh agent could execute without more context. The deliverable is the prompt, not the implementation, unless the user explicitly says to execute it.

## When to Use

- The request is voice-dictated, filler-heavy, or references "the thing" without clear anchors.
- The user brings a half-formed plan and wants it stress-tested.
- A multi-part ask has hidden decisions about inputs, outputs, scope, or success criteria.
- The output should be reusable in a later session, spec, issue, or prompt file.

Skip for trivial one-line requests where producing a prompt would be ceremony, unless the user explicitly invokes this skill.

## Workflow

1. Read the request and any local project context first: `AGENTS.md`, `README.md`, file structure, and named files.
2. If helpful, restate the ask as `Cleaned ask:` while preserving intent.
3. Ask one question at a time only when the answer changes the final prompt and cannot be discovered locally.
4. Recommend an answer with each question so the user can accept or correct it quickly.
5. Continue until the prompt can stand alone.
6. Emit a `Final prompt:` block as the deliverable.
7. Ask whether to execute it now, save it, or stop.

If the user says "just do it", "just run it", or "skip the prompt", state the assumptions and proceed with execution.

## Final Prompt Must Include

- what to build or do in one sentence.
- exact path or location when known.
- inputs and outputs.
- dependencies, conventions, and existing patterns.
- failure behavior.
- success criteria.
- likely out-of-scope items.

The prompt must read cold. Do not depend on "as discussed above".

## Question Rules

- Ask one question at a time.
- Ask only about decisions that change the deliverable.
- Do not ask for facts the repo or workspace can answer.
- Avoid questions about cosmetic choices unless they affect acceptance.

Recommended format:

```text
Q: <the unresolved decision>
My recommendation: <answer> - <short reason>
```

## Common Mistakes

- Do not batch several questions just because it feels efficient.
- Do not skip the final prompt after invoking this skill.
- Do not execute by default; this skill creates the executable prompt first.
- Do not write a prompt that relies on prior chat context.

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Prompt Enhancer
- Expand vague requests with who, what, when, where, why, how, and how-much constraints.
- Convert messy input into a self-contained task contract with inputs, outputs, scope, and acceptance criteria.
- Preserve user intent while removing ambiguity, hidden assumptions, and conflicting instructions.
- Offer concise alternatives when the best framing depends on a real tradeoff.

### Q
- Ask focused questions only after inspecting discoverable context.
- Prioritize questions that change the plan, reveal constraints, or expose risk.
- Identify the user's real objective, audience, success criteria, and out-of-scope boundaries.
- Stop questioning once the task is executable with defensible assumptions.

