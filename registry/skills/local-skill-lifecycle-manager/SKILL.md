---
name: local-skill-lifecycle-manager
description: Use when adding, updating, merging, repairing, or validating local Codex
  skills under ~/.agents/skills or ~/.codex/skills, especially when checking uniqueness,
  overlap, frontmatter, or duplicate skill names.
---

# Local Skill Lifecycle Manager

## Overview

Use this for local skill catalog work where correctness depends on the real installed roster, not on the requested skill name alone. Treat exact-name uniqueness and functional overlap as separate gates.

## When to Use

- A user asks whether a skill is unique and can be added.
- A user asks to install, update, merge, or convert an upstream skill.
- A user points at a `SKILL.md` and asks to fix it.
- Codex reports skill metadata, YAML, duplicate-name, or context-budget warnings.
- The task touches `~/.agents/skills`, `~/.codex/skills`, or plugin-cache skill roots.

Skip for one-off prompt writing, repo-local `AGENTS.md` guidance, or project documentation that is not meant to become an installed skill.

## Workflow

1. Read the target skill or upstream source.
2. Inventory active local skill names and nearby functional overlaps across `~/.agents/skills`, `~/.codex/skills`, and relevant plugin skill roots.
3. Decide:
   - same name and same purpose: update in place.
   - new name but overlapping purpose: merge useful material into the existing best-fit skill.
   - genuinely new capability: install as a new skill.
4. Keep frontmatter small:
   - only `name` and `description`.
   - description starts with `Use when...`.
   - description is trigger-only, not a workflow summary.
5. Preserve source intent while adapting commands, paths, and wording to the local Codex environment.
6. Put routing notes in the body, not frontmatter.

## Validation

Always verify before reporting completion:

- YAML frontmatter parses.
- `name` matches the folder name unless there is a strong reason.
- exact active-name count is `1` for each changed skill.
- no unintended duplicate install was created.
- any referenced bundled files, scripts, or paths exist.

Useful completion signals:

```text
PARSE_OK
<skill_name>_count=1
```

## Common Mistakes

- Do not copy broad upstream skills verbatim when they shadow local skills.
- Do not install a second same-purpose skill just because the upstream folder name differs.
- Do not rewrite the whole skill when only YAML frontmatter is broken.
- Do not claim CLI behavior was smoke-tested if the underlying command is missing from `PATH`.
- Do not grow `description` fields to explain the whole workflow; that contributes to skill discovery budget pressure.

## Local Writing-Skills Delta

The disabled local `writing-skills` copy carried one useful local convention: in this Codex setup, local skill frontmatter should contain only `name` and `description`. Preserve that rule here when repairing or converting local skills.

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Mechanical Robot
- Execute deterministic checklists exactly when the task is mechanical.
- Preserve formatting, names, paths, and ordering unless the requirement says otherwise.
- Avoid creative rewrites for validation, migration, formatting, or inventory tasks.
- Report exact pass/fail outputs and any skipped item.

