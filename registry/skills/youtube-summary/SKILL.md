---
name: youtube-summary
description: Use when the user provides a YouTube video or asks to transcribe, summarize,
  study, critique, or turn a YouTube source into an Obsidian knowledge note.
---

# YouTube Obsidian Summary

## Overview

Use this skill to turn a YouTube video into a durable Obsidian learning note. Prefer transcript evidence when available, fall back to audio transcription when captions are missing, and keep the final note as a summary and analysis artifact rather than a verbatim transcript dump.

## Default Outcome

Create or update one Markdown note under:

`/Users/kkomarag/Documents/ObsidianNotes/40 Knowledge`

Choose the most specific existing subdirectory by topic:

- AI or agent content: `40 Knowledge/AI`
- Programming or software engineering: `40 Knowledge/Programming`
- Networking: `40 Knowledge/Networking`
- Cisco networking: `40 Knowledge/Networking/Cisco`
- Linux kernel: `40 Knowledge/Linux Kernel`

If no existing subdirectory fits, suggest `40 Knowledge/Media Notes` and state that it is the fallback category. If the user asked for execution, create it; if they asked only for a recommendation, do not create it.

Every note must include the Obsidian tag `#YouTube`.

## Source Acquisition

1. Capture metadata first:

```bash
yt-dlp --dump-json --skip-download --no-playlist '<youtube-url>'
```

2. Try captions before audio transcription:

```bash
yt-dlp --write-subs --write-auto-subs --sub-langs 'en.*' --skip-download --convert-subs vtt -o '/tmp/youtube-%(id)s.%(ext)s' '<youtube-url>'
```

3. If captions and auto-captions are absent or unusable, extract audio:

```bash
yt-dlp -x --audio-format mp3 --audio-quality 5 -o '/tmp/youtube-%(id)s.%(ext)s' '<youtube-url>'
```

4. Transcribe the audio with the best available local or API path. On this machine, a prior proven fallback was OpenAI `whisper-1` with `response_format=verbose_json` and segment timestamps. Recheck current tool availability before relying on that path.

Do not claim transcript coverage unless the transcript or transcription was actually obtained. If only title, description, comments, or chapters are available, label the note as source-limited.

## Note Contract

Use this structure unless the user asks for a different format:

```markdown
---
tags:
  - YouTube
source_type: YouTube
source_url: <url>
channel: <channel or UNCONFIRMED>
published: <date or UNCONFIRMED>
captions: <manual | auto | audio-transcribed | unavailable | UNCONFIRMED>
created: <ISO date>
updated: <ISO date>
---

# <Video Title>

## Source Snapshot
- URL:
- Channel:
- Published:
- Duration:
- Transcript Basis:
- Confidence:

## Executive Summary
<5-10 bullets or short paragraphs covering the core message.>

## Teacher Notes
<Explain the concepts in a mentor/teacher voice. Define unfamiliar terms, show the mental model, and connect claims to examples.>

## Key Ideas
- <Idea> - <why it matters>

## Evidence From The Video
- <Timestamp or segment if available> - <paraphrased evidence>

## Practical Takeaways
- <Actionable takeaway>

## Research Opinion
### Position
<State the informed opinion clearly.>

### For / Advantages
- <Pros, advantages, or reasons the claim/workflow is strong.>

### Against / Disadvantages
- <Cons, limitations, missing evidence, or failure modes.>

### Correct / Well-Supported
- <Claims that are correct or well-supported, with reasoning.>

### Incorrect / Weakly-Supported
- <Claims that are incorrect, overstated, or unsupported, with reasoning.>

### Final Judgment
<Balanced judgment with confidence level and reasoning.>

## Open Questions
- <Question for future research or user follow-up>

## Discussion Log
### <ISO date> - Initial Summary
- <What was created and what evidence it used.>
```

## Research Opinion Rules

- Treat the opinion as a reasoned research judgment, not a reaction.
- Separate what the video says from what external or prior knowledge suggests.
- Include pros/cons and advantages/disadvantages even when the final judgment is favorable.
- Use `UNCONFIRMED` for missing dates, claims, author credentials, or source details.
- If web research is needed to judge correctness, use primary or official sources where possible and record source dates when relevant.
- If no external research was performed, say the opinion is based only on the transcript and general technical judgment.

## Follow-Up Discussions

When the user asks follow-up questions about the same video or note:

1. Reopen the existing Obsidian note.
2. Add or update the relevant content section.
3. Append a dated entry under `## Discussion Log` with the new question, answer summary, and any changed judgment.
4. Update the frontmatter `updated` date.

Do not create a second note for the same video unless the user explicitly asks for a separate artifact.

## Quality Bar

- Prefer a teacher/mentor explanation style for learning value.
- Keep summaries paraphrased; do not store a full copyrighted transcript unless the user explicitly asks and the use is appropriate.
- Preserve the source URL and transcript basis so future readers can judge evidence quality.
- If transcription fails, keep the note honest: source-limited is better than pretending the video was reviewed.
- Quote YouTube URLs in shell commands to avoid `zsh` globbing issues.
