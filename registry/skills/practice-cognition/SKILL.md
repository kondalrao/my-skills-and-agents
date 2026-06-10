---
name: practice-cognition
description: Use when a plan, hypothesis, design, or judgment needs validation through
  direct practice, trial runs, feedback, or iteration before treating it as true.
---

# Practice Cognition

## Local Metadata Notes

- Former frontmatter `metadata`: short-description=Validate ideas through practice loops

Use this skill to keep reasoning tied to observable results. The loop is:
practice, understand, re-practice, refine. Do not treat a plan as correct
until it has survived an appropriate practical check.

For source excerpts behind the framing, read `original-texts.md` only when the
user asks for philosophical or historical grounding.

## Use When

- A proposal, design, implementation plan, or diagnosis has not been tested.
- A first attempt failed and the next step needs to learn from evidence.
- The work is stuck in abstract reasoning without a concrete trial.
- The work is pure activity without reflection on what the activity proves.
- A decision depends on whether observed behavior matches expectations.

## Skip When

- The task is a one-off output with no meaningful validation loop.
- The user already has verified results and only needs execution.
- The question can be answered directly from authoritative documentation.
- The work is still early investigation with no hypothesis to test.

## Operating Loop

1. State the current stage before acting:
   - `perception`: gathering first-hand facts from code, docs, output, or users.
   - `rationalization`: forming a hypothesis, model, or plan from those facts.
   - `verification`: testing the hypothesis against practice.
   - `synthesis`: turning the result into the next, better understanding.
2. Set the cycle termination condition:
   - `This cycle is complete when <specific observable condition>.`
3. Gather or create direct evidence:
   - inspect real files, run the smallest relevant command, build a prototype,
     execute a smoke test, compare outputs, or review primary sources.
4. Form the hypothesis explicitly:
   - `My hypothesis is: <claim>. I expect: <observable result>.`
5. Verify in practice:
   - run the check and compare actual results against expectations.
6. Evaluate honestly:
   - success means the understanding is provisionally usable.
   - failure means the understanding must be revised.
   - partial success means record what held and what broke.
7. Synthesize the next step:
   - `What this round taught: <lesson>. Next cycle should: <action>.`

## Stage Rules

| Stage | Required action | Avoid |
| --- | --- | --- |
| Perception | Record concrete facts before judging. | Premature conclusions. |
| Rationalization | Name the hypothesis and expected observation. | Implementing an unstated guess. |
| Verification | Run the smallest decisive practical check. | Treating confidence as evidence. |
| Synthesis | State what changed in understanding. | Starting another attempt without learning. |

## Common Mistakes

- Declaring a plan correct before any practical test.
- Explaining away failed evidence to protect a preferred theory.
- Copying another context's solution without checking local constraints.
- Running many actions without extracting the governing pattern.
- Reading only theory when a small direct experiment is possible.

## Output Pattern

When this skill shapes the response, keep the loop visible but compact:

```text
Stage: verification
Cycle complete when: <observable condition>
Hypothesis: <claim>
Check: <command/test/review/prototype>
Observed: <result>
Learning: <what changed>
Next: <smallest useful follow-up>
```

## Related Skills

- Use investigation-oriented skills before this one when no testable hypothesis
  exists yet.
- Use debugging skills when the practical check exposes an unexpected failure.
- Use review or critique skills during synthesis when the lesson affects future
  decisions or standards.

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Hallucination Zero
- Separate sourced facts, calculations, inferences, and assumptions explicitly.
- Prefer primary sources or local evidence; mark uncertainty instead of filling gaps.
- Verify citations, numbers, quoted claims, and tool outputs before using them as conclusions.
- When evidence is weak, recommend the smallest next check that would change the answer.

### Mycroft Debater
- Challenge the plan with strongest-counterargument reasoning before endorsing it.
- Identify weak premises, false dilemmas, untested assumptions, and missing evidence.
- Separate critique from replacement: explain what fails, then propose a better option.
- Keep the debate grounded in project facts and user constraints.

