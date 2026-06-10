# Continuity

## [PLANS]

- 2026-06-10: Added local `teach` skill plan surface for persistent Obsidian-backed learning workspaces.
- 2026-06-10: Prepared repository publication pass: generic README refresh, full worktree validation, commit, and push to `origin/main`.
- 2026-06-10: Remove `technical-poster-design` from the shared skill registry, refresh generated state, validate, commit, and push.

## [DECISIONS]

- `teach` is a separate skill, not merged into `personal-teacher-mentor` or `mentor-teacher`; those remain task-retrospective note skills.
- Teaching workspaces use `/Users/kkomarag/Documents/ObsidianNotes/40 Knowledge/AI/Study/<topic-slug>/` as the base pattern, with one learning topic per directory.
- The skill keeps local registry frontmatter minimal: only `name` and `description`.

## [PROGRESS]

- Created `registry/skills/teach/SKILL.md`.
- Added bundled references for mission, resources, and learning-record formats.
- Ran `scripts/sync.sh`; it refreshed adapters/manifest and validated, but did not rewrite `catalog.yaml` when `import_native` had `updates=0`.
- Refreshed `catalog.yaml` and `state/manifest.json` through `scripts.manage.write_catalog()` and `scripts.manage.write_manifest()`.
- Replaced README with a generic registry overview, workflow, install pointers, and a catalog-derived list of skills and purposes.
- Removed `registry/skills/technical-poster-design/` and refreshed `catalog.yaml`, `state/manifest.json`, and `README.md` so the skill is no longer discoverable from repo metadata.

## [DISCOVERIES]

- `scripts/sync.sh` currently prints `VALIDATE_OK` without necessarily refreshing `catalog.yaml`; use the manage functions or add a command path when catalog membership must be updated after adding a new skill.
- `git diff --cached --check` reports existing whitespace issues across imported registry/reference files; `README.md` was not the source. Leave broad whitespace normalization for a separate cleanup to avoid obscuring the registry publication diff.

## [OUTCOMES]

- `teach` is discoverable in `catalog.yaml`, `state/manifest.json`, and `/Users/kkomarag/.agents/skills/teach/SKILL.md`.
- Final validation command: `PYTHONPYCACHEPREFIX=/private/tmp/my-skills-and-agents-pycache scripts/validate.sh` -> `VALIDATE_OK`.
- README skill catalog matches `catalog.yaml`: 81 catalog skills, 81 README entries, no missing or extra skill names.
- `technical-poster-design` removal verification: exact-name grep found no repo references, README/catalog both list 80 skills, and validation returned `VALIDATE_OK`.
