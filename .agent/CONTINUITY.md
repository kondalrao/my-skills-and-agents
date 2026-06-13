# Continuity

## [PLANS]

- 2026-06-10: Added local `teach` skill plan surface for persistent Obsidian-backed learning workspaces.
- 2026-06-10: Prepared repository publication pass: generic README refresh, full worktree validation, commit, and push to `origin/main`.
- 2026-06-10: Remove `technical-poster-design` from the shared skill registry, refresh generated state, validate, commit, and push.
- 2026-06-10: Incorporate Microsoft MarkItDown as a reusable Markdown extraction helper for relevant local skills.
- 2026-06-10: Use the ACTOR self-education video to tighten `teach` around mission, compression, challenge, teach-back, and action.

## [DECISIONS]

- `teach` is a separate skill, not merged into `personal-teacher-mentor` or `mentor-teacher`; those remain task-retrospective note skills.
- Teaching workspaces use `/Users/kkomarag/Documents/ObsidianNotes/40 Knowledge/AI/Study/<topic-slug>/` as the base pattern, with one learning topic per directory.
- The skill keeps local registry frontmatter minimal: only `name` and `description`.
- MarkItDown integration lives under `convert-plaintext-to-md`; consuming skills route there instead of duplicating raw MarkItDown usage.
- The MarkItDown helper is intentionally local-file-only and uses `convert_local()`; publishing/visual conversion skills such as `publish-to-pages` stay on their existing fidelity-preserving paths.
- `teach` should use AI as framer/interpreter/opponent/coach/action companion, but not as a replacement for the learner's retrieval, judgment, or practice.
- ACTOR in `teach` is a required lesson-design contract for saved lessons and follow-up teaching turns, not just a model to mention.

## [PROGRESS]

- Created `registry/skills/teach/SKILL.md`.
- Added bundled references for mission, resources, and learning-record formats.
- Ran `scripts/sync.sh`; it refreshed adapters/manifest and validated, but did not rewrite `catalog.yaml` when `import_native` had `updates=0`.
- Refreshed `catalog.yaml` and `state/manifest.json` through `scripts.manage.write_catalog()` and `scripts.manage.write_manifest()`.
- Replaced README with a generic registry overview, workflow, install pointers, and a catalog-derived list of skills and purposes.
- Removed `registry/skills/technical-poster-design/` and refreshed `catalog.yaml`, `state/manifest.json`, and `README.md` so the skill is no longer discoverable from repo metadata.
- Added `registry/skills/convert-plaintext-to-md/scripts/markitdown_to_md.py`.
- Updated `convert-plaintext-to-md`, `graphify`, `explain-visually`, `vault-setup`, and the vault import workflow to route document extraction through the helper.
- Ran `scripts/sync.sh`; it refreshed `state/manifest.json` and returned `VALIDATE_OK`.
- Added an Obsidian YouTube note for "How To Become Dangerously Self-Educated (with AI)" based on audio transcription.
- Updated `registry/skills/teach/SKILL.md` with a compact ACTOR-style lesson learning loop.
- Strengthened `registry/skills/teach/SKILL.md` so ACTOR is mandatory for saved lessons, practice activities, and follow-up teaching turns unless the user asks for a one-off explanation.

## [DISCOVERIES]

- `scripts/sync.sh` currently prints `VALIDATE_OK` without necessarily refreshing `catalog.yaml`; use the manage functions or add a command path when catalog membership must be updated after adding a new skill.
- `git diff --cached --check` reports existing whitespace issues across imported registry/reference files; `README.md` was not the source. Leave broad whitespace normalization for a separate cleanup to avoid obscuring the registry publication diff.
- MarkItDown is not installed in the current environment; the wrapper's missing-dependency path reports `python3 -m pip install 'markitdown[all]'`.
- Python compile checks in this repo still need `PYTHONPYCACHEPREFIX=/private/tmp/my-skills-and-agents-pycache` to avoid home-directory pycache permission failures.
- `yt-dlp` reported no manual or automatic captions for `VeU6gScy92s`; the usable source basis was Whisper transcription from downloaded audio.

## [OUTCOMES]

- `teach` is discoverable in `catalog.yaml`, `state/manifest.json`, and `/Users/kkomarag/.agents/skills/teach/SKILL.md`.
- Final validation command: `PYTHONPYCACHEPREFIX=/private/tmp/my-skills-and-agents-pycache scripts/validate.sh` -> `VALIDATE_OK`.
- README skill catalog matches `catalog.yaml`: 81 catalog skills, 81 README entries, no missing or extra skill names.
- `technical-poster-design` removal verification: exact-name grep found no repo references, README/catalog both list 80 skills, and validation returned `VALIDATE_OK`.
- MarkItDown helper verification: `--help` works; remote URLs are rejected; existing outputs require `--force`; missing MarkItDown prints install guidance; fake-module positive-path tests verified file output and clean stdout/stderr separation.
- Final MarkItDown integration validation: `PYTHONPYCACHEPREFIX=/private/tmp/my-skills-and-agents-pycache scripts/validate.sh` -> `VALIDATE_OK`.
- ACTOR teaching-loop update verification: `PYTHONPYCACHEPREFIX=/private/tmp/my-skills-and-agents-pycache scripts/sync.sh` and `scripts/validate.sh` both returned `VALIDATE_OK`.
- Mandatory ACTOR contract verification: active local skill count is one at `/Users/kkomarag/.agents/skills/teach/SKILL.md`; `/Users/kkomarag/.codex/skills` has no duplicate `teach`.
