---
name: create-agentsmd
description: Use when creating, replacing, or substantially refreshing a repository
  AGENTS.md from project evidence, commands, docs, CI, and local conventions.
---

# Create AGENTS.md

## Purpose

Create a root or nested `AGENTS.md` that gives coding agents concrete, verified project instructions. Treat it as agent-facing operational documentation, not a human README replacement.

Source basis: adapted from GitHub's `awesome-copilot` `create-agentsmd.prompt.md` and the public `agents.md` format guidance.

## Use When

- A repository needs a new `AGENTS.md`.
- Existing instructions are missing, generic, or stale enough to rewrite.
- A monorepo or multi-package workspace needs root plus nested agent instructions.
- The user asks for an agent instruction file that works across coding tools.

Use `agent-md-refactor` instead when the main task is splitting a bloated existing `AGENTS.md`, `CLAUDE.md`, or equivalent into progressive-disclosure files.

## Workflow

1. Establish scope:
   - Identify the repository root and any package or subproject roots.
   - Read existing `AGENTS.md`, `README.md`, contributing docs, package manifests, build files, test configs, and CI workflows.
   - Check whether a closer nested `AGENTS.md` should exist for a subproject.
2. Extract evidence:
   - Project purpose and architecture in one short paragraph.
   - Exact install, build, lint, typecheck, test, and dev-server commands.
   - Required environment setup, generated files, data directories, services, and non-obvious local prerequisites.
   - Code style, test placement, PR, security, and deployment conventions that are real in the repo.
3. Write the file:
   - Use standard Markdown.
   - Prefer concise sections with actionable bullets and exact commands.
   - Include only instructions that help agents work correctly in this repo.
   - Keep human-facing product description brief; point to README or docs for long background.
4. Verify:
   - Run or inspect commands before presenting them as verified.
   - If a command is too expensive, destructive, or unavailable, label it as documented but not run.
   - Check Markdown links and nested-file precedence assumptions.
5. Rehydrate:
   - Update related docs only when the new `AGENTS.md` changes canonical project workflow knowledge.

## Recommended Sections

Use only the sections that fit the project:

- `Project Overview`: purpose, architecture, key technologies.
- `Setup Commands`: dependency installation and required local services.
- `Development Workflow`: dev server, watch mode, generated artifacts, environment files.
- `Testing Instructions`: exact commands for full and targeted tests.
- `Code Style`: repo-specific patterns, formatting, imports, naming, comments.
- `Build and Deployment`: build outputs, packaging, deploy commands, CI expectations.
- `Security and Data`: secrets, credentials, test data, permission-sensitive operations.
- `Monorepo Notes`: package discovery, filtering, workspace-specific commands, nested `AGENTS.md` precedence.
- `PR and Review`: required checks, commit or title conventions, review constraints.
- `Troubleshooting`: common local failures with concrete fixes.

## Quality Bar

- Prefer exact commands over vague process notes.
- Keep root `AGENTS.md` focused; link to existing docs for detailed background.
- Do not invent architecture, commands, or policies.
- Remove generic advice such as "write clean code" unless it maps to a repo-specific rule.
- Preserve existing local conventions and naming.
- If instructions conflict, surface the conflict before rewriting.

## Output Contract

When reporting completion, include:

- Path of each `AGENTS.md` created or changed.
- Evidence used to derive commands and conventions.
- Verification attempted, with pass/fail/not-run status.
- Any unresolved assumptions or intentionally omitted sections.
