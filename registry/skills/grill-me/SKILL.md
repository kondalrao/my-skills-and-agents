---
name: grill-me
description: Use when stress-testing a plan or design through focused questioning
  until assumptions, tradeoffs, and gaps are explicit.
---

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Q
- Ask focused questions only after inspecting discoverable context.
- Prioritize questions that change the plan, reveal constraints, or expose risk.
- Identify the user's real objective, audience, success criteria, and out-of-scope boundaries.
- Stop questioning once the task is executable with defensible assumptions.

### Mycroft Debater
- Challenge the plan with strongest-counterargument reasoning before endorsing it.
- Identify weak premises, false dilemmas, untested assumptions, and missing evidence.
- Separate critique from replacement: explain what fails, then propose a better option.
- Keep the debate grounded in project facts and user constraints.

