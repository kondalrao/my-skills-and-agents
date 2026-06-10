---
name: idea-refine
description: Use when shaping a raw product, feature, process, or project idea before
  formal specs or implementation. Refines the idea through divergent options, convergent
  evaluation, assumption checks, MVP scope, and a concise idea one-pager.
---

# Idea Refine

Use this skill to turn an early idea into a focused concept worth validating.
It sits before `brainstorming`, `create-specification`, `product-spec-writer`,
or `writing-plans`: use those once the user wants a formal design/spec or an
implementation path.

Source adapted from Addy Osmani's `agent-skills` `idea-refine` skill:
https://github.com/addyosmani/agent-skills/tree/main/skills/idea-refine

## Use When

- The user has a raw idea and wants to refine, ideate, stress-test, or sharpen it.
- The desired output is a lightweight idea brief, not a full implementation plan.
- The idea may be product, feature, workflow, startup, writing, tooling, or process oriented.
- The user asks for MVP scope, assumptions, non-goals, or "what should this really be?"

## Skip When

- The user already has an approved direction and needs a formal spec or PRD.
- The work is scientific research ideation; use `scientific-brainstorming`.
- The user wants a deep project design gate before coding; use `brainstorming`.
- The user wants implementation steps; use planning or implementation skills after refinement.

## Workflow

Work as an interactive thinking partner. Be direct, specific, and willing to
reject weak directions. Keep the process lightweight.

1. Understand the idea:
   - Restate it as a "How might we..." problem statement.
   - Ask up to 3-5 sharpening questions, one at a time when needed.
   - Do not proceed until the target user and success criteria are clear enough.
   - If inside a codebase, inspect relevant files and constraints before guessing.

2. Diverge:
   - Generate 5-8 meaningfully different variations.
   - Use only the lenses that fit: inversion, simplification, constraint changes,
     audience shift, combination, first principles, or expert lens.
   - Read `references/frameworks.md` if the idea needs more ideation lenses.

3. Converge:
   - Cluster the strongest variations into 2-3 directions.
   - Stress-test each direction for user value, feasibility, and differentiation.
   - Surface hidden assumptions, failure modes, and tradeoffs.
   - Read `references/refinement-criteria.md` for the evaluation rubric.

4. Sharpen:
   - Recommend one direction or explain why none is ready.
   - Define the smallest MVP that tests the riskiest assumption.
   - Name what is intentionally out of scope.

5. Ship a one-pager:
   - Ask whether the user wants the final brief saved.
   - If yes, save to the user's chosen path, or default to
     `docs/ideas/<idea-name>.md` when that fits the repo.
   - Do not create files without confirmation.

## Output Template

```markdown
# <Idea Name>

## Problem Statement
How might we <outcome> for <specific user> without <key constraint>?

## Recommended Direction
<Chosen direction and why it is sharper than the alternatives.>

## Key Assumptions to Validate
- [ ] <Assumption> - <fast validation method>
- [ ] <Assumption> - <fast validation method>
- [ ] <Assumption> - <fast validation method>

## MVP Scope
<Smallest version that tests the core assumption.>

## Not Doing
- <Excluded idea> - <reason>
- <Excluded idea> - <reason>

## Open Questions
- <Question that must be answered before building>
```

## Quality Bar

- Target user and success criteria are explicit.
- Multiple directions were explored before convergence.
- Assumptions include concrete validation methods.
- The MVP is smaller than the user's first instinct.
- The "Not Doing" list makes tradeoffs visible.
- Codebase constraints are referenced when the idea lives inside a repo.

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Q
- Ask focused questions only after inspecting discoverable context.
- Prioritize questions that change the plan, reveal constraints, or expose risk.
- Identify the user's real objective, audience, success criteria, and out-of-scope boundaries.
- Stop questioning once the task is executable with defensible assumptions.

### Expert Moriarty
- Generate several high-quality angles before selecting one.
- Use expert-role perspectives to expose hidden constraints, adjacent opportunities, and implementation traps.
- Prefer unusual but practical options over generic advice.
- Converge on recommendations that can be executed and tested.

### President Sonic
- Frame decisions in terms of goals, constraints, tradeoffs, stakeholders, and reversibility.
- Convert strategy into executable priorities with explicit non-goals.
- Record why the chosen path beats alternatives.
- Keep leadership framing concise and operational.

