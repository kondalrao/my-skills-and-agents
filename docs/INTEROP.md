# Tool Interop Model

## Skills

Skills are stored once in `registry/skills/<name>/SKILL.md`. The same folder is
symlinked into each native skill root that supports Agent Skills:

- Codex and OpenCode shared path: `~/.agents/skills`
- Claude Code: `~/.claude/skills`
- OpenCode native path: `~/.config/opencode/skills`

## Agents

Agents are stored in canonical Markdown under `registry/agents/*.agent.md`.
Adapters are generated for:

- Codex: `adapters/codex/agents/*.toml`
- Claude Code: `adapters/claude/agents/*.md`
- OpenCode: `adapters/opencode/agents/*.md`

Codex model settings are preserved for Codex only. Claude Code and OpenCode use
their configured defaults unless canonical metadata explicitly sets a
tool-specific value.

## Cursor and VS Code

Cursor and VS Code do not receive native skills or subagents from this repo.
They receive instruction adapters:

- Cursor: `.cursor/rules/*.mdc`
- VS Code: `.github/copilot-instructions.md` and
  `.github/instructions/*.instructions.md`

These files point back to the shared guidance instead of duplicating the whole
catalog into every project.

