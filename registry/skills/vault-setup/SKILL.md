---
name: vault-setup
description: Use when setting up, verifying, importing into, or configuring an Obsidian
  vault with bundled vault setup tools.
---

# vault-setup-skill

Interactive vault configurator — asks one free-text question, infers your role and folders, builds a personalized Obsidian vault with CLAUDE.md and companion skill links.

## Directory Structure

```
vault-setup-skill/
├── SKILL.md                          # This file (routing + quick ref)
├── RoleTemplates.md                  # Keyword-to-folder mapping table
├── PluginRecommendations.md          # Obsidian plugins by role type
├── Workflows/
│   ├── Setup.md                      # Main 6-step setup flow
│   ├── ImportFiles.md                # File import guidance
│   └── Verify.md                     # Post-setup verification
├── Tools/
│   ├── VaultBuilder.py               # CLI: create, verify, inject-global
│   └── VaultBuilder.help.md          # Tool documentation
└── scripts/
    └── process_docs_to_obsidian.py   # Bulk file import to inbox/
```

## Workflow Routing

| Intent | Workflow | Tool |
|--------|----------|------|
| Set up a new vault | `Workflows/Setup.md` | `Tools/VaultBuilder.py create` |
| Import existing files | `Workflows/ImportFiles.md` | `scripts/process_docs_to_obsidian.py` |
| Verify vault setup | `Workflows/Verify.md` | `Tools/VaultBuilder.py verify` |
| Add vault to global context | `Workflows/Setup.md` Step 5 | `Tools/VaultBuilder.py inject-global` |
| Choose Obsidian plugins | `PluginRecommendations.md` | — |
| Understand folder mapping | `RoleTemplates.md` | — |

## Examples

```
"Set up my Obsidian vault"              → Workflows/Setup.md
"I want to create a second brain"       → Workflows/Setup.md
"Import my documents into the vault"    → Workflows/ImportFiles.md
"Verify my vault is set up correctly"   → Workflows/Verify.md
"What plugins should I install?"        → PluginRecommendations.md
"Add this vault to my global config"    → Workflows/Setup.md Step 5
```

## Quick Reference

**Base folders** (always created): `inbox/`, `daily/`, `projects/`, `archive/`

**Additional folders** detected from keywords — see `RoleTemplates.md` for full mapping.

**Companion skills** (linked, not created): `daily-skill`, `tldr-skill`, `obsidian-master-skill`

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| `click` not found when running VaultBuilder.py | Missing dependency | `pip install click` |
| Vault folders created but Obsidian doesn't see them | Obsidian not pointed at vault root | Open Obsidian → "Open folder as vault" → select the vault directory |
| `inject-global` says "Already configured" but Claude doesn't see context | Vault path in CLAUDE.md doesn't match exactly | Check `~/.claude/CLAUDE.md` for the vault path — it must be the resolved absolute path |
| Symlink shows `[BROKEN]` in verify | Target skill directory was moved or deleted | Re-create the symlink: `ln -sf /path/to/skill ~/.claude/skills/skill-name` |
| `process_docs_to_obsidian.py` shows encoding warnings | Source files contain non-UTF-8 characters | Review warned files manually; convert source encoding with `iconv` if needed |

### Edge Cases

- **Empty keywords**: If `--role-keywords` is empty, only base folders are created (inbox, daily, projects, archive)
- **Vault path doesn't exist**: VaultBuilder creates it automatically via `mkdir -p`
- **Running create twice**: Safe — folders use `exist_ok=True`, CLAUDE.md is overwritten (back up first if customized)
