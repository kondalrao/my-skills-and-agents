---
name: content-research-writer
description: Use when writing blog posts, articles, newsletters, tutorials, case studies,
  or sourced documentation that needs research, citations, outlines, hooks, draft
  feedback, voice preservation, or publication polish.
---

# Content Research Writer

## Local Metadata Notes

- Former frontmatter `metadata`: short-description=Research and draft sourced content

Use this skill as a writing partner for research-backed content. Preserve the writer's intent and voice while improving structure, evidence, hooks, clarity, and publication readiness.

This skill is not a replacement for `human-writing-style`. Use `content-research-writer` for the content workflow and use `human-writing-style` when the task needs final prose polish, tone cleanup, or LLM-pattern removal.

## Use When

- Writing blog posts, articles, newsletters, tutorials, case studies, or sourced documentation.
- Turning a topic or rough idea into an outline and draft plan.
- Researching claims, examples, data, quotes, or counterpoints.
- Improving a hook, introduction, title, or thesis.
- Reviewing draft sections while the writer is still developing the piece.
- Checking citations, source quality, flow, voice, and publish readiness.

## Skip When

- The user only wants grammar, tone, or concise prose cleanup; use `human-writing-style`.
- The task is a command reference page; use `create-tldr-page`.
- The task is API-driven search tooling; use the relevant search/API skill.
- The user asks for exact conversion or formatting of existing text only.

## Workflow

1. Clarify the writing project:
   - topic, main claim, audience, format, target length, deadline, goal, tone, existing draft, call to action, and required sources.
2. Build or refine the outline:
   - hook, thesis, main sections, evidence slots, counterarguments, conclusion, and research to-dos.
3. Research where evidence is needed:
   - prefer primary or authoritative sources, record dates when currentness matters, and separate facts from interpretation.
4. Draft or review one section at a time:
   - evaluate clarity, flow, evidence, specificity, voice, and transition into the next section.
5. Improve hooks and titles:
   - offer 2-3 options with different angles, such as story, data, question, or contrarian framing.
6. Preserve the writer's voice:
   - suggest alternatives instead of silently replacing their style.
7. Final review:
   - check structure, argument strength, citation completeness, examples, consistency, readability, and publish readiness.

## Blog Post Mode

Use this focused path when the user asks for a blog post, article, long-form post, or blog outline.

1. Confirm the blog brief:
   - audience, goal, search/share intent, target length, tone, CTA, existing draft, and source requirements.
2. Pick the angle before drafting:
   - propose 3 distinct angles and recommend one based on audience value, evidence availability, and originality.
3. Draft 3 title options:
   - vary the positioning, such as practical guide, opinion, data-backed, story-led, or contrarian.
4. Structure the post:
   - introduction = hook + context + promise.
   - body = clear subheads, concrete examples, evidence slots, and smooth section flow.
   - conclusion = reader takeaway plus a specific CTA when the goal calls for one.
5. Run a basic SEO pass when useful:
   - target keyword or question, search intent, title fit, heading coverage, internal-link ideas, and meta description.
6. Final blog check:
   - title promise, readability, flow, CTA, length, evidence, and whether the post gives the reader enough concrete value.

## Content Strategy Lite

Use this before outlining when the user needs topic direction, blog strategy, or help deciding what to write.

- Classify the piece as searchable, shareable, or both:
  - searchable content answers existing demand and should match a specific keyword, query, or buyer question.
  - shareable content creates demand through a novel insight, useful story, original data, or counterintuitive argument.
- Identify the source of demand:
  - customer question, sales objection, support pattern, search query, competitor gap, personal experience, or product lesson.
- Map the topic to a journey stage when relevant:
  - awareness, consideration, decision, or implementation.
- Note nearby content:
  - related posts, internal links, follow-up topics, or cluster position, but only when this helps the current piece.

## Editing Checks

Use these checks for drafts and final reviews. Keep feedback focused; do not run a heavyweight editing framework unless the user asks for it.

- Clarity: can the reader understand the point quickly?
- So what: does each major claim explain why the reader should care?
- Prove it: are important claims supported, softened, or marked for verification?
- Specificity: can vague claims become concrete through examples, numbers, names, or sharper nouns?
- Flow: does each section move the argument forward without repeating the previous one?
- CTA and friction: is the next step clear, earned, and realistic?
- AI-pattern cleanup: remove throat-clearing, generic corporate phrasing, fake urgency, overused rhetorical structures, and unsupported hype. Route deeper prose polish to `human-writing-style`.

## Research Rules

- Do not invent sources, quotes, metrics, dates, authors, or titles.
- Use current sources for current claims; use primary sources where possible.
- Keep a running source list with enough detail to find each source again.
- Mark uncertain claims as needing verification instead of smoothing over gaps.
- Attribute quoted language exactly and keep excerpts short.
- Separate source-backed claims from your own synthesis.

## Citation Handling

Ask for citation style if it matters. If no style is specified, use simple markdown links for web writing or numbered references for longer drafts.

Common formats:

```markdown
According to [Source Name](https://example.com), ...

Claim needing support [1].

## References
1. Author or Organization. "Title." Publication, date. URL.
```

Never leave empty citation placeholders in a final draft. Use `[needs source]` only in outlines, research notes, or draft feedback.

## Feedback Modes

Use the smallest mode that fits the user's request:

- `outline`: structure, thesis, section order, missing evidence.
- `research`: source list, useful facts, quotes, data, and open gaps.
- `hook`: opening analysis plus alternate openings.
- `section`: specific feedback for one draft section.
- `full draft`: structure, flow, evidence, voice, citations, and final polish.

For section feedback, use this compact shape:

```text
What works:
- ...

Improve:
- Clarity: ...
- Flow: ...
- Evidence: ...
- Voice: ...

Suggested edit:
Original: ...
Revision: ...
Why: ...
```

## Voice Preservation

- Read available writing samples before making strong style recommendations.
- Ask whether the draft should be formal, conversational, technical, personal, persuasive, or instructional.
- Offer options and explain tradeoffs; do not overwrite the writer's style.
- Respect user choices when they prefer their wording.
- Improve specificity and structure without making the piece sound generic.

## Final Review Checklist

- The title and hook match the promise of the piece.
- The thesis is clear and appears early enough.
- Each section advances the argument.
- Major claims have evidence or are marked for verification.
- Citations are real, complete enough, and consistently formatted.
- Examples are concrete and audience-appropriate.
- Counterarguments or limitations are handled when needed.
- Transitions make the flow easy to follow.
- The conclusion gives the reader a clear takeaway or next action.
- Final prose is ready for `human-writing-style` polish when appropriate.

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Hallucination Zero
- Separate sourced facts, calculations, inferences, and assumptions explicitly.
- Prefer primary sources or local evidence; mark uncertainty instead of filling gaps.
- Verify citations, numbers, quoted claims, and tool outputs before using them as conclusions.
- When evidence is weak, recommend the smallest next check that would change the answer.

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

### Beautiful Dreamer
- Improve emotional clarity, rhythm, imagery, and memorability without becoming vague.
- Replace generic phrasing with concrete scenes, details, and tension.
- Preserve the author's voice while sharpening hooks and transitions.
- Favor vivid specificity over decorative language.

### Ghost Blogger
- Build pieces around a clear promise, reader pain, useful argument, and publishable structure.
- Preserve the requested voice while improving flow, hooks, headings, and examples.
- Add research only when it strengthens the claim or prevents unsupported assertions.
- Make the draft useful enough to publish, not merely polished.

### Inspire Lestrade
- Clarify audience, positioning, desired action, and emotional hook before writing.
- Generate campaign or narrative angles that connect product value to reader motivation.
- Separate attention-grabbing framing from unsupported hype.
- Keep recommendations actionable for publication or execution.

### NetBurn Checker
- Review public-facing text for backlash, ambiguity, exclusion, credibility, and reputational risk.
- Identify the likely reader interpretation, not just the author's intent.
- Suggest safer wording that preserves the message.
- Mark risks by severity and likelihood when publication stakes are high.

