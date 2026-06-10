---
name: scientific-slides
description: Use when planning, writing, reviewing, or building scientific presentations,
  conference talks, seminars, thesis defenses, journal clubs, research decks, PowerPoint
  slides, or LaTeX Beamer talks.
---

# Scientific Slides

## Local Metadata Notes

- Former frontmatter `metadata`: short-description=Design scientific research presentations

Use this skill for scientific talks that need a clear research story, strong
visual evidence, disciplined timing, citations, and audience-aware slide design.
Scientific slides should be visually engaging and rigorous, not dense paper
pages pasted into a deck.

This skill is distinct from `Presentations`: that skill owns the mechanics of
creating, editing, rendering, verifying, and exporting presentation artifacts.
Use `scientific-slides` for scientific talk structure and design judgment; use
`Presentations` when actually building a PowerPoint/PPTX deck in Codex.

Use `markdown-mermaid-writing` when the deliverable is a scientific Markdown note, report, README, or speaker document that needs Mermaid diagrams rather than a slide deck.

## Use When

- Preparing conference talks, seminars, lab meetings, thesis defenses, grant
  pitches, journal clubs, tutorials, or scientific briefings.
- Turning a paper, project, dataset, or research plan into slides.
- Reviewing scientific slides for narrative, visual hierarchy, timing, and
  evidence quality.
- Creating a PowerPoint, PPTX, PDF, or LaTeX Beamer scientific presentation.
- Designing result, method, contribution, limitation, or future-work slides.

## Skip When

- The user wants a non-scientific marketing, sales, or playful deck.
- The user only needs generic PPTX mechanics; use `Presentations`.
- The user wants evidence appraisal of a claim before building slides; use
  `scientific-critical-thinking`.
- The task is a written paper, report, or grant text with no talk component.

## Talk Planning Workflow

1. Define the talk:
   - audience, venue, time limit, format, speaker role, target takeaway, and
     required output format.
2. Choose the talk type:
   - conference short talk, seminar, thesis defense, journal club, grant pitch,
     teaching/tutorial, or internal research update.
3. Build the story:
   - problem, gap, central question, approach, key result, interpretation,
     limitations, and next step.
4. Allocate time:
   - use roughly one major idea per slide; cut content before shrinking text.
5. Plan visual evidence:
   - figures, diagrams, methods schematics, result plots, tables, photos,
     citations, and any required institutional branding.
6. Draft slide briefs:
   - one job per slide, one headline claim, one dominant visual, minimal text.
7. Build or review:
   - if producing a PPTX, follow the `Presentations` skill and verify rendered
     slides; if producing Beamer, keep source readable and compile-check when
     a TeX toolchain is available.
8. Validate:
   - check scientific accuracy, citation placement, visual readability, timing,
     speaker flow, and audience fit.

## Scientific Slide Rules

- Put the key claim in the title or visible headline.
- Use visuals as evidence, not decoration.
- Prefer direct labels and annotations over legends the audience must decode.
- Keep citations short and visible enough to be credible but not dominant.
- Use bullet text as speaking prompts, not paragraphs.
- Never bury a result in a crowded figure without highlighting the takeaway.
- Separate observed result, interpretation, and speculation.
- Include limitations when they affect the main claim.
- For current claims, verify sources before putting them on a slide.
- If using user-provided figures, preserve data integrity and do not redraw in a
  misleading way.

## Common Structures

### Short Conference Talk

1. Title and one-sentence contribution.
2. Problem and gap.
3. Approach or method.
4. Key result 1.
5. Key result 2 or mechanism.
6. Why it matters.
7. Limitations and next step.
8. Final takeaway.

### Seminar Or Thesis Defense

1. Motivation and field context.
2. Research questions or aims.
3. Background needed to understand the work.
4. Methods and design.
5. Results by aim.
6. Synthesis across results.
7. Limitations.
8. Contributions and future work.

### Journal Club

1. Paper context and why it matters.
2. Main claim.
3. Methods at a glance.
4. Key result figures.
5. Critical appraisal.
6. Discussion questions.

## Review Checklist

- Audience can state the core contribution after the first few slides.
- Each slide has one dominant job.
- Every figure has a visible takeaway.
- Text is readable at presentation distance.
- Color, labels, and contrast are accessible.
- Results are not overstated.
- Citations support factual claims.
- The deck fits the time limit.
- The final slide gives a memorable scientific takeaway.

## Output Pattern

When planning or reviewing, use this shape:

```markdown
## Talk Brief
Audience:
Time:
Format:
Core takeaway:

## Slide Sequence
1. <slide title> - job, dominant visual, evidence/citation

## Risks
- <accuracy, timing, design, or evidence issue>

## Build Notes
- Use `Presentations` for PPTX artifact creation when needed.
- Use Beamer only if the user requests LaTeX or a TeX workflow.
```

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Sherlock Report
- Build conclusions from observable evidence, then state confidence and gaps.
- Organize analysis as findings, evidence, implications, and next checks.
- Avoid dramatic claims unless the evidence supports them.
- Make the final artifact useful to a reader who has not seen the investigation.

### Instant Presentation
- Shape material into a clear audience journey with a strong opening, evidence path, and memorable close.
- Prefer visual structure, concise labels, and one main idea per section.
- Use diagrams or tables when they reduce cognitive load.
- Check that the artifact can be presented, not just read.

