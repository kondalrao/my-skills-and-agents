# Troubleshooting

## Validation Fails

Run:

```bash
scripts/doctor.sh
```

Fix the first reported error before continuing. The validator intentionally
stops on duplicate names, invalid frontmatter, stale adapters, and unsafe files.

## Native Edits Conflict

If `scripts/sync.sh` reports a conflict, inspect the generated report under:

```text
reports/conflicts/
```

Resolve the canonical `registry/` file manually, then rerun `scripts/sync.sh`.

## Tool Does Not See a Skill

Check symlinks:

```bash
scripts/install-local.sh --check-symlinks
```

Restart the tool if it caches skill discovery.

