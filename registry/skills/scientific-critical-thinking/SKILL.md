---
name: scientific-critical-thinking
description: Use when evaluating scientific claims, study design, evidence quality,
  statistical validity, bias, confounding, causal inference, GRADE/Cochrane-style
  appraisal, or research conclusions.
---

# Scientific Critical Thinking

## Local Metadata Notes

- Former frontmatter `metadata`: short-description=Evaluate scientific evidence quality

Use this skill to evaluate scientific rigor and determine what conclusions are
actually supported. Be constructive and proportionate: identify strengths,
limitations, uncertainty, and concrete improvements.

This skill is distinct from `practice-cognition`: that skill asks whether an
idea has been tested in practice. This skill evaluates scientific evidence,
methodology, statistical reasoning, bias, confounding, and claim strength.

## Use When

- Reviewing papers, protocols, study designs, abstracts, claims, or conclusions.
- Assessing internal, external, construct, or statistical validity.
- Identifying bias, confounding, p-hacking, selective reporting, or logical
  fallacies.
- Comparing evidence from multiple studies.
- Applying GRADE, Cochrane risk-of-bias, CONSORT, STROBE, PRISMA, or similar
  scientific appraisal frameworks.
- Improving a proposed study design before data collection.

## Skip When

- The user wants open-ended ideation; use `scientific-brainstorming`.
- The user wants formal peer-review prose rather than analysis scaffolding.
- The user only needs a source lookup or literature summary.
- The task is code review, debugging, or implementation quality review.

## Appraisal Workflow

1. Identify the claim:
   - causal, associational, descriptive, predictive, mechanistic, or normative.
   - quote the claim when possible.
2. Identify the evidence:
   - study type, population, intervention/exposure, comparator, outcomes,
     sample size, follow-up, and data source.
3. Assess design fit:
   - whether the design can answer the question and support the claim strength.
4. Evaluate validity:
   - internal validity, external validity, construct validity, and statistical
     conclusion validity.
5. Check bias and confounding:
   - selection, measurement, performance, detection, attrition, reporting,
     publication, researcher, and analysis biases.
6. Evaluate statistics:
   - power, assumptions, test choice, multiple comparisons, missing data,
     effect sizes, confidence intervals, model fit, and overinterpretation.
7. Grade evidence quality:
   - use the right framework for the domain and state confidence level.
8. Produce a balanced conclusion:
   - what is supported, what is uncertain, what is unsupported, and what would
     change the assessment.

## Core Checklists

### Study Design

- Is the design appropriate for the research question?
- Are comparison groups adequate?
- Can the design support causal language?
- Were hypotheses and analysis plans prespecified?
- Are practical or ethical constraints acknowledged?

### Bias And Confounding

- Could selection or attrition distort the sample?
- Are observers, participants, or assessors blinded where feasible?
- Were all planned outcomes reported?
- Could unmeasured confounding explain the result?
- Is contradictory evidence handled fairly?

### Statistics

- Was sample size justified before data collection?
- Are tests appropriate for data type, distribution, and design?
- Are multiple comparisons corrected or labeled exploratory?
- Are p-values interpreted correctly?
- Are effect sizes and confidence intervals reported?
- Is statistical significance separated from practical importance?

### Claim Strength

- Does the conclusion follow from the data?
- Is correlation treated as causation?
- Does the claim overgeneralize beyond sample, setting, or measurement?
- Are limitations stated clearly?
- Is uncertainty proportional to evidence quality?

## Output Pattern

```markdown
## Summary
<what was evaluated>

## Strengths
- ...

## Major Concerns
- <issue, why it matters, evidence needed>

## Minor Concerns
- ...

## Evidence Quality
<high/moderate/low/very low, with reason>

## Supported Conclusions
- ...

## Unsupported Or Overstated Claims
- ...

## Recommendations
- ...
```

## Quality Bar

- Name specific methodological issues rather than saying "weak study".
- Distinguish data from interpretation.
- Distinguish evidence against a claim from evidence for the null.
- Do not apply stricter standards to disliked findings.
- Acknowledge uncertainty and specify what information would resolve it.
- Suggest improvements, not only flaws.

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

### Sherlock Report
- Build conclusions from observable evidence, then state confidence and gaps.
- Organize analysis as findings, evidence, implications, and next checks.
- Avoid dramatic claims unless the evidence supports them.
- Make the final artifact useful to a reader who has not seen the investigation.

