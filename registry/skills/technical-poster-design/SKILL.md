---
name: technical-poster-design
description: Use when creating dense technical posters, infographics, one-page architecture
  maps, reference sheets, or use-case posters that need high information density,
  concrete sections, readable labels, diagrams, and PNG/PDF output rather than sparse
  art-poster styling.
---

# Technical Poster Design

Create dense, readable technical posters and one-page infographics. This skill is for practical engineering communication: use cases, architecture overviews, operational maps, security/network/performance summaries, incident explainers, and reference sheets.

Do not produce sparse museum-poster output. Whitespace is for readability only, not the main aesthetic.

## Output Contract

Produce:

1. A rendered `.png` or `.pdf` poster.
2. The source used to render it, unless the user explicitly asks for only the image.
3. Any local assets copied into the artifact folder, such as fonts or icons.

Prefer PNG for quick review. Use PDF when the user asks for print, deck import, or vector-friendly output.

## Workflow

1. Restate the poster goal, target audience, output format, and success criteria.
2. Extract 4-7 major sections from the topic. If the topic is broad, choose the most operationally useful sections.
3. For each section, include concrete examples, not just categories.
4. Select a layout pattern from `references/layout-patterns.md` when useful.
5. Render the poster with stable dimensions and bundled fonts from `assets/fonts`.
6. Verify the output: file type, dimensions, nonblank pixel extrema, script/typecheck if applicable, and a visual pass for text overflow or low contrast.

## Density Rules

- Fill roughly 70-85% of the canvas with useful information.
- Use 4-7 sections; 5 is a strong default.
- Give each section 3-5 concrete bullets, short callouts, or mini-diagram labels.
- Include compact metadata where useful: attach points, protocols, APIs, failure modes, "good when", tradeoffs, or examples.
- Keep labels short and scannable. Prefer precise phrases over paragraphs.
- Avoid decorative-only graphics. Visuals should classify, connect, compare, or explain.

## Layout Rules

- Use cards, bands, grids, radial hubs, matrices, timelines, or architecture maps.
- Keep cards at modest radii and avoid cards inside cards unless the inner element is a chip, badge, or code tag.
- Reserve large type for the title. Section titles should be compact.
- Put diagrams close to the text they explain.
- Keep all text inside its container. If it does not fit, reduce copy first, then adjust layout.
- Use whitespace as gutters and breathing room, not empty canvas.

## Typography

Use bundled fonts from `assets/fonts` when available:

- Display: `BigShoulders-Bold.ttf`, `Gloock-Regular.ttf`, `Tektur-Medium.ttf`
- Section headings: `InstrumentSans-Bold.ttf`, `Tektur-Medium.ttf`
- Body: `WorkSans-Regular.ttf`, `InstrumentSans-Regular.ttf`
- Code/chips/labels: `JetBrainsMono-Regular.ttf`, `JetBrainsMono-Bold.ttf`, `RedHatMono-Regular.ttf`
- Editorial accent: `InstrumentSerif-Italic.ttf`

If a font is missing, use local system fonts but say so in the final answer.

## Visual Style

Default to an engineering reference aesthetic:

- light technical grid or quiet background structure,
- restrained color per section,
- dark readable text,
- compact badges for APIs, hooks, protocols, tools, and states,
- small sparklines, arrows, flow lines, matrices, or topology fragments where they add meaning.

Avoid:

- sparse abstract art,
- long prose blocks,
- marketing hero layouts,
- decorative gradient blobs,
- illegible microtext,
- one-hue palettes,
- unlabeled diagrams that require guessing.

## Verification Checklist

Before calling the poster done:

- Confirm output path and file type.
- Confirm dimensions.
- Confirm image is nonblank with pixel extrema or equivalent.
- Compile or lint the render script if one was created.
- Visually inspect the poster for text overflow, low contrast, excessive blank space, and section balance.
- Mention any unresolved limitation in the final response.

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Instant Presentation
- Shape material into a clear audience journey with a strong opening, evidence path, and memorable close.
- Prefer visual structure, concise labels, and one main idea per section.
- Use diagrams or tables when they reduce cognitive load.
- Check that the artifact can be presented, not just read.

