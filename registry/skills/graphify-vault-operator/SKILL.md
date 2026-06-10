---
name: graphify-vault-operator
description: Use when operating, repairing, validating, or explaining Graphify in
  the Obsidian vault, including scoped indexes, hook failures, graphify-out artifacts,
  or Graphify-backed subagent smoke tests.
---

# Graphify Vault Operator

## Overview

Use this for Graphify work in the Obsidian vault where the live artifact tree, hook payload, and installed package may disagree with older assumptions. Verify the current state before explaining or changing anything.

## When to Use

- The user asks to use or fix Graphify in the Obsidian vault.
- A hook error mentions Graphify, `PreToolUse`, `permissionDecision`, `additionalContext`, or `systemMessage`.
- The user asks why `graphify-out/wiki/index.md` or another artifact is missing.
- The user asks for one global index, scoped graph refresh, or Graphify-backed subagent testing.
- `AGENTS.md`, `.codex/hooks.json`, `.graphifyignore`, or `graphify-out` needs to be checked after Graphify changes.

Skip for general graph theory or Python graph analysis; use `networkx` for that.

## Local Defaults

- Vault root: `/Users/kkomarag/Documents/ObsidianNotes`.
- Canonical scoped index: `50 Machine/Graphify/global-index`.
- Preferred source scope: `20 Areas/Personal`, `30 Projects`, `40 Knowledge`, and `50 Machine/LLM Wiki/Sources`.
- `graphify-out` may be a symlink; follow it when inspecting artifacts.
- `GRAPH_REPORT.md` is the current practical entry point when no generated wiki exists.

Treat these as defaults, not facts that never drift. Re-check before editing.

## Workflow

1. Inspect the live vault state:
   - `.codex/hooks.json`
   - `AGENTS.md`
   - `.graphifyignore`
   - `graphify-out` and its symlink target
   - `graphify --help` and installed `graphifyy` path/version when relevant
2. For hook failures, compare the generated hook payload with the Codex event contract before patching.
3. Prefer durable package/template fixes plus `graphify codex install` over one-off edits to generated hook files.
4. Preserve the vault-specific scoped Graphify section in `AGENTS.md`; remove duplicate generic Graphify blocks if regeneration appends one.
5. For artifact questions, inspect the current tree before concluding something is broken.
6. For behavior confirmation, use a focused smoke test that answers from `GRAPH_REPORT.md` or graph artifacts before raw note search.

## Validation

Use checks that match the change:

- Artifact check: list `graphify-out`, following symlinks with `find -L` when needed.
- CLI surface check: confirm whether commands such as `graphify wiki` actually exist before referencing their outputs.
- Hook check: run the approved read-only Codex smoke command when verifying generated hook compatibility.
- Syntax check: if package bytecode compilation wants to write under restricted home paths, use AST parsing instead.

## Common Mistakes

- Do not assume `graphify-out/wiki/index.md` should exist; current builds may use `GRAPH_REPORT.md` instead.
- Do not inspect a symlink with plain `find` and conclude the output is empty.
- Do not disable Graphify just to silence a hook unless the user asks for removal.
- Do not trust older memory about the hook payload shape; inspect the live generated hook and installed generator.
- Do not leave duplicate Graphify instruction blocks in `AGENTS.md` after reinstalling the integration.
