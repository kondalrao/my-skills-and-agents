# Install

## Prerequisites

- Python 3.11 or newer.
- Git access to `git@github.com:kondalrao/my-skills-and-agents.git`.
- Installed tools are optional. Missing tools are skipped and reported.

## Local Machine

```bash
cd /Users/kkomarag/Workspace/my-skills-and-agents
scripts/validate.sh
scripts/install-local.sh --dry-run
scripts/install-local.sh --check-symlinks
scripts/install-local.sh apply
```

The installer creates timestamped backups before replacing any managed path.

## Project Adapters

```bash
scripts/install-project-adapters.sh /path/to/project
```

This installs Cursor and VS Code instruction adapters into the target project.

## Rollback

Use the timestamped backup printed by `install-local.sh`, or restore from the
initial pre-migration backup:

```text
/Users/kkomarag/backups/my-skills-and-agents/pre-migration-20260521-223435
```

