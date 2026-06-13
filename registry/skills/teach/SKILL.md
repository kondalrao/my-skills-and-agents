---
name: teach
description: Use when the user wants to learn a skill or concept over multiple sessions using an Obsidian-backed study workspace with missions, curated resources, lessons, references, learning records, and teaching notes.
---

# Teach

Use this skill to teach the user a skill or concept as an ongoing course, not as a one-off explanation. Keep every learning topic in its own Obsidian study directory so future sessions can continue from the same mission, resources, lessons, and learning records.

## Study Base

Use this base directory for all teaching workspaces:

```text
/Users/kkomarag/Documents/ObsidianNotes/40 Knowledge/AI/Study
```

Create or reuse one topic directory per learning goal:

```text
/Users/kkomarag/Documents/ObsidianNotes/40 Knowledge/AI/Study/<topic-slug>/
```

Use lowercase kebab-case for `<topic-slug>`, such as `scapy-packet-parsing`, `rust-cli-development`, or `network-telemetry-debugging`.

Do not use the current working directory as the teaching workspace unless the user explicitly asks for that. If the user asks to learn an unrelated topic, create a separate sibling topic directory instead of mixing missions.

## Workspace Files

Each topic directory may contain:

- `MISSION.md`: the concrete reason the user is learning the topic, success criteria, constraints, and out-of-scope boundaries. Read `references/mission-format.md` before creating or changing it.
- `RESOURCES.md`: high-trust knowledge sources and practitioner communities. Read `references/resources-format.md` before creating or changing it.
- `lessons/*.html`: focused, self-contained HTML lessons. Each lesson teaches one tightly scoped thing and gives the user a concrete practice loop.
- `reference/*.html`: reusable quick-reference material such as glossaries, syntax sheets, algorithms, workflows, checklists, or diagrams.
- `learning-records/*.md`: decision-grade learning records for demonstrated understanding, prior knowledge, corrected misconceptions, and mission shifts. Read `references/learning-record-format.md` before writing them.
- `NOTES.md`: teaching preferences, working notes, and durable details that should shape future lessons.

Create directories lazily when first needed. Do not create placeholder files just to fill the structure.

## Teaching Workflow

1. Resolve the topic directory.
   - If a relevant directory already exists, read `MISSION.md`, `RESOURCES.md`, `NOTES.md`, and recent `learning-records/` before teaching.
   - If no relevant directory exists, create one under the Study base and establish `MISSION.md` before writing lessons.
2. Ground the mission.
   - Push vague goals toward concrete outcomes.
   - Confirm with the user before changing an existing mission.
3. Curate sources.
   - Prefer official docs, primary sources, recognized experts, peer-reviewed material, and well-moderated practitioner communities.
   - Use citations or links in lessons for factual claims that matter.
   - For current, medical, legal, financial, safety, or fast-changing technical topics, verify with current authoritative sources before teaching.
4. Choose the next lesson from the user's zone of proximal development.
   - Use the mission, prior learning records, stated experience, and recent performance to pick something challenging but reachable.
   - If the user specifies an exact thing to learn, teach that unless it conflicts with the mission or assumes missing prerequisites.
5. Produce one focused lesson.
   - Save it as `lessons/NNNN-<slug>.html`, incrementing from the highest existing lesson number.
   - Make it readable, printable, and self-contained.
   - Teach only the knowledge needed for the target skill.
   - Include a short practice activity or quiz with immediate feedback when practical.
   - Apply the Lesson Learning Loop while designing the explanation, practice, and close.
   - Link to relevant reference documents and prior lessons using relative links.
6. Update reference material when it will be reused.
   - Create or update `reference/*.html` for glossaries, syntax, algorithms, workflows, recurring diagrams, or durable checklists.
   - Keep reference documents compressed and easy to scan.
7. Write learning records only when evidence justifies it.
   - Record demonstrated understanding, stated prior knowledge, corrected misconceptions, or mission shifts.
   - Do not log mere coverage or session activity.
8. Close with the next best action.
   - Point to the lesson path.
   - Tell the user what to practice next or what question to answer.
   - Mention any source gaps or assumptions that should be resolved before the next lesson.

## Lesson Learning Loop

Every saved lesson, practice activity, and follow-up teaching turn must satisfy this ACTOR loop unless the user explicitly asks for a one-off explanation:

- Aim: state or clearly imply the user's mission and the specific capability the lesson should change.
- Compress: center the lesson on one load-bearing idea the user must carry forward; do not make polished summaries the endpoint.
- Test: include a counterexample, failure mode, edge case, or challenge question so the user has to inspect assumptions instead of merely agree.
- Own: require recall, teach-back, paraphrase, or connection to the user's real work without leaning on the source text.
- Run: end with one concrete decision, rule, checklist, experiment, command, artifact, or scenario the user can try next.

AI may frame the mission, interpret confusing material, oppose weak interpretations, coach explanations, and convert ideas into action steps. Do not let AI replace the user's retrieval, judgment, or practice.

## Lesson Standards

- Teach one thing per lesson.
- Tie every lesson back to `MISSION.md`.
- Prefer concrete examples and practice over broad exposition.
- Include retrieval or teach-back prompts when they would expose shallow understanding.
- Do not count polished summaries as learning evidence unless the user has also retrieved, explained, challenged, or applied the idea.
- Keep explanations plain, precise, and appropriately challenging.
- Use beautiful but simple HTML: readable typography, clear sections, accessible contrast, and print-friendly layout.
- Include feedback loops. Examples: in-page quiz answers, worked examples, small exercises, scenario questions, or real-world steps to try.
- Do not invent expertise, citations, or communities. If sources are missing, state the gap in `RESOURCES.md` and proceed only when the remaining uncertainty is acceptable.

## Wisdom And Communities

Some learning requires feedback from practitioners, not just private study. When the user asks something that depends on real-world judgment, answer what can be answered from evidence, then recommend a high-quality community, class, forum, mentor, or practice setting when appropriate.

Respect an explicit preference not to join communities. Record that preference in `RESOURCES.md` or `NOTES.md` so future sessions do not keep proposing it.
