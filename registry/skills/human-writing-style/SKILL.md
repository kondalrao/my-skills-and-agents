---
name: human-writing-style
description: Use when editing prose-heavy notes, docs, summaries, specs, or user-facing
  text for direct, concrete, human writing.
---

# Human Writing Style

Use this skill to make prose sound direct, concrete, and human. Apply it as judgment, not as a mechanical lint rule. Preserve exact source language in quotes, logs, code, API names, file paths, filenames, and command output.

## Core Voice

- Write like a person talking to another person, not like a corporate announcement.
- Be confident and direct. Remove softeners like "I think," "maybe," and "could" unless uncertainty is real.
- Prefer active voice.
- Say what something is before explaining what it is not.
- Address the reader as "you" when the piece speaks to an external audience.
- Use contractions when they make the sentence warmer and clearer.

## Specificity

- Replace vague praise with facts, examples, constraints, or measurable outcomes.
- Back claims with concrete examples or metrics when available.
- Emphasize customers, users, and community members over company achievements.
- Use realistic, product-based examples instead of `foo`, `bar`, or `baz` when prose includes examples.
- Make claims concrete enough that a reader could verify or disagree with them.

## Titles

- Make a clear promise so readers know what they will get.
- Prefer useful, specific titles over vague ones like "My thoughts on X."
- Use sharp opinions only when the content supports them with evidence.
- Draft a placeholder title first, finish the piece, then revise the title at the end.
- Avoid clickbait. The title should earn the reader's trust after they read the piece.

## Replace Or Remove

Use these replacements when they improve the sentence. Do not change preserved source text.

- `a bit`, `a little`, `pretty`, `quite`, `rather`, `really`, `very` -> remove or be specific
- `actually`, `arguably`, `it seems`, `sort of`, `kind of`, `pretty much` -> remove unless the uncertainty matters
- `assistance` -> `help`
- `best practices` -> `proven approaches`
- `blazing fast`, `lightning fast` -> a measured speed claim
- `commence` -> `start`
- `delve` -> `go into`
- `facilitate` -> `help` or `ease`
- `game-changing`, `innovative`, `modern`, `robust`, `great` -> name the specific benefit
- `implement` -> `do`, `build`, `add`, or the exact action when prose does not need the technical verb
- `individual` -> `person`, `man`, or `woman`, depending on context
- `initial` -> `first`
- `leverage`, `utilize` -> `use`
- `mission-critical` -> `important`
- `numerous` -> `many`
- `performant` -> `fast and reliable`, or a measured performance claim
- `referred to as` -> `called`
- `remainder` -> `rest`
- `seamless`, `seamlessly` -> `automatic`, or describe what the user no longer has to do
- `sufficient` -> `enough`
- `thing` -> the specific noun
- `webinar` -> `online event`

## Avoid Stock Phrases

- Remove self-congratulation like "We're excited," "Today, we're excited to," and "We can't wait to see what you'll build."
- Remove clichés like "The future of X," "By developers, for developers," and "We obsess over X."
- Do not start with "Great question," "You're right," "Let me help," or "Let's dive in."
- Skip broad openers like "In today's fast-paced digital world" and "In the ever-evolving landscape of."
- Avoid the pattern "It's not just X, it's Y."
- Do not use self-referential disclaimers like "As an AI" unless the user specifically asks about model behavior.
- Do not close with "In conclusion," "Overall," "To summarize," or "Hope this helps."

## LLM Pattern Cleanup

- Prefer commas, semicolons, or separate sentences over em dashes.
- Avoid perfectly symmetrical paragraphs and list items that feel generated.
- Do not overuse transitions like "Furthermore," "Additionally," and "Moreover."
- Use numbered lists only when order matters. Use bullets when order does not matter.
- Remove hedge stacks such as "may potentially" and "it is important to note that."
- Remove empty citation placeholders like `[1]` when no source exists.
- Remove copy-paste artifacts such as smart quotes, non-breaking spaces, and stray Unicode punctuation unless the target document intentionally uses them.

## Punctuation And Form

- Use Oxford commas consistently.
- Use exclamation points sparingly.
- Start sentences with "But" or "And" when it improves flow, but do not overuse the move.
- Use periods instead of long comma chains when clarity suffers.
- Keep headings short. Prefer sentence casing unless the surrounding document uses title case.

## Safe Exceptions

Do not rewrite text where exactness matters more than style:

- code, commands, logs, stack traces, and terminal output
- file paths, filenames, API names, identifiers, database fields, and config keys
- quoted source text, legal text, or user-provided language that must be preserved
- technical terms of art where the replacement would be less precise
- intentionally branded language unless the task is to rewrite that brand voice

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Beautiful Dreamer
- Improve emotional clarity, rhythm, imagery, and memorability without becoming vague.
- Replace generic phrasing with concrete scenes, details, and tension.
- Preserve the author's voice while sharpening hooks and transitions.
- Favor vivid specificity over decorative language.

### Contextual Translator
- Preserve meaning, register, domain terms, and implied audience across rewrites.
- Prefer natural target-language phrasing over literal translation.
- Flag terms where multiple translations materially change meaning.
- Keep formatting and structure stable unless the user asks for adaptation.

