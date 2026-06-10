---
name: explain-visually
description: Use when source material should become a responsive HTML visual explainer
  that teaches a repo, spec, PR, architecture, or concept.
---

# Explain Visually

## Overview

Create a human-facing HTML artifact that explains an idea visually. The reader should understand the idea well enough to retell it.

## When to Use

- The user asks to explain a repo, spec, PR, architecture, workflow, or concept visually.
- A normal Markdown summary would hide the mental model, flow, or transformation.
- The output should be a standalone HTML explainer with diagrams and responsive layout.

Skip when the requested deliverable is specifically Markdown with Mermaid, Draw.io, Excalidraw, slides, or a text-only answer.

## Workflow

1. Understand the source material:
   - audience
   - core idea
   - moving parts
   - decisions and tradeoffs
   - concrete facts, paths, commands, interfaces, and examples
2. Outline the teaching path before building:
   - what the reader should understand
   - explanation order
   - which ideas need diagrams
   - what can be omitted
   - which facts support the explanation
3. Build a responsive HTML explainer:
   - use Tailwind CSS via CDN when a simple static artifact is enough.
   - use custom CSS only for fonts, theme tokens, diagrams, and small refinements.
   - use slide-like sections on desktop and readable stacked sections on mobile.
   - do not preserve a fixed 16:9 frame on mobile.
4. Verify in a browser or browser automation before finishing.

## Teaching Shape

Default order:

1. core lesson
2. why the old way fails
3. new mental model
4. how it works
5. concrete example
6. what to do next

The first screen must state the core lesson in plain language. Include at least one transformation: before/after, problem/solution, vague/clear, or hidden/visible.

## Style

- Use simple concrete titles.
- Prefer short explanatory copy over slogans.
- Ground factual claims in the source.
- Use SVG diagrams only when they teach.
- Keep one clear idea per section.
- Use strong spacing, type scale, and visual hierarchy.
- Ensure diagram labels are centered, aligned, and contained inside shapes.

## Verification

Check desktop and mobile viewports. Fix:

- overflow
- overlapping text
- clipped labels
- unreadable scale
- cramped spacing
- broken responsive layout

Do not use `overflow: hidden` to hide layout problems.

## Common Mistakes

- Do not decorate instead of explaining.
- Do not make unsupported claims.
- Do not use abstract titles when simple words work.
- Do not cram multiple lessons into one section.
- Do not finish if the reader could not retell the idea from the artifact.

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Instant Presentation
- Shape material into a clear audience journey with a strong opening, evidence path, and memorable close.
- Prefer visual structure, concise labels, and one main idea per section.
- Use diagrams or tables when they reduce cognitive load.
- Check that the artifact can be presented, not just read.

