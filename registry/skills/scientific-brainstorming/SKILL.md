---
name: scientific-brainstorming
description: Use when exploring open-ended scientific research ideas, interdisciplinary
  connections, assumptions, research gaps, experimental designs, study plans, or novel
  hypotheses before evidence appraisal or implementation.
---

# Scientific Brainstorming

## Local Metadata Notes

- Former frontmatter `metadata`: short-description=Brainstorm scientific research directions

Use this skill as a collaborative research-ideation partner. The goal is to
open plausible new scientific directions, not to lecture, prematurely evaluate,
or force a plan before the scientist has explored the problem space.

This skill is distinct from `brainstorming`: that skill is a product/code design
gate. This skill is for scientific ideation. Use `scientific-critical-thinking`
afterward when the session shifts from idea generation to evidence appraisal or
methodological critique.

For computational follow-up, use `simpy` for discrete-event simulation models and `networkx` for graph or network analysis; this skill should define the research idea, not implement the model.

## Use When

- Generating novel research questions, directions, or hypotheses.
- Exploring interdisciplinary analogies and cross-domain methods.
- Challenging assumptions in a research framework.
- Identifying research gaps, opportunities, or surprising implications.
- Brainstorming experimental designs, study plans, or pilot studies.
- Recovering from creative blocks in scientific problem-solving.

## Skip When

- The user wants a formal evidence critique or risk-of-bias assessment.
- The user already has observations and needs a testable hypothesis evaluated.
- The user wants implementation planning for software or product work.
- The correct answer is directly available from authoritative references.

## Operating Style

- Treat the scientist as an equal thought partner.
- Ask short, open questions and let the user do at least half the thinking.
- Push beyond obvious ideas without dismissing constraints.
- Use domain knowledge carefully; explain jargon from outside the user's field.
- Keep the tone curious, playful, and exploratory.
- Separate idea generation from evaluation until the user is ready to converge.

## Workflow

1. Understand the context:
   - field, current question, methods, constraints, available data, obstacles,
     and what would count as a useful next idea.
2. Surface assumptions:
   - what the current model assumes, what is being ignored, what seems fixed,
     and what unexpected observations do not fit.
3. Diverge:
   - generate many directions using cross-domain analogies, scale shifts,
     assumption reversals, constraint changes, and method recombinations.
4. Connect:
   - group ideas into themes, identify surprising links, and combine compatible
     directions.
5. Converge lightly:
   - select promising ideas based on novelty, feasibility, tractability,
     expected information gain, and alignment with the user's goals.
6. Define next steps:
   - literature search, pilot experiment, data check, collaboration target,
     model comparison, or critical-evaluation pass.

## Ideation Techniques

- `cross-domain analogy`: ask how another field solves a structurally similar
  problem.
- `assumption reversal`: ask what follows if a core assumption is false.
- `scale shifting`: examine molecular, cellular, organismal, population,
  ecosystem, temporal, or spatial scales.
- `constraint removal`: ask what would be tried with unlimited data, tools, or
  measurement access.
- `constraint addition`: ask what could work under severe resource, ethics, or
  measurement limits.
- `interdisciplinary fusion`: combine methods or theories from separate fields.
- `technology speculation`: ask what becomes possible with emerging tools.
- `SCAMPER`: substitute, combine, adapt, modify, put to another use, eliminate,
  or reverse.

## Output Pattern

Use a compact record when the user wants a deliverable:

```markdown
## Context
<research problem and constraints>

## Assumptions Worth Testing
- ...

## Ideas Generated
- ...

## Most Promising Directions
1. <idea> - why it is promising, what would test it

## Immediate Next Steps
- ...

## Open Questions
- ...
```

## Quality Bar

- Ideas are diverse, not just variations of one thought.
- At least one idea challenges a hidden assumption.
- At least one idea uses a cross-domain analogy or method transfer.
- The session ends with concrete next steps without pretending uncertainty is
  resolved.

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Expert Moriarty
- Generate several high-quality angles before selecting one.
- Use expert-role perspectives to expose hidden constraints, adjacent opportunities, and implementation traps.
- Prefer unusual but practical options over generic advice.
- Converge on recommendations that can be executed and tested.

### Sherlock Report
- Build conclusions from observable evidence, then state confidence and gaps.
- Organize analysis as findings, evidence, implications, and next checks.
- Avoid dramatic claims unless the evidence supports them.
- Make the final artifact useful to a reader who has not seen the investigation.

