---
name: graphify
description: Use when turning code, docs, papers, media, or notes into a knowledge
  graph with Graphify outputs, queries, exports, or vault artifacts.
---

# Graphify

Turn source material into a knowledge graph with clustered communities, audit trail, and optional HTML, JSON, Obsidian, Neo4j, SVG, GraphML, MCP, or watch-mode outputs.

## Routing

Use this skill for:
- `/graphify` full extraction and graph generation.
- `/graphify --update`, `--cluster-only`, `query`, `path`, `explain`, `add`, `--watch`, hook, and export workflows.
- Repairing or explaining existing `graphify-out` artifacts.

For Obsidian-vault-specific repairs, hook compatibility, or missing artifact diagnosis, prefer `graphify-vault-operator`.

## Core Workflow

1. Confirm Graphify is installed and inspect the local CLI surface before promising commands.
2. Detect the input corpus and warn when inputs are too small, too broad, binary-heavy, or source-limited.
3. If the corpus includes PDF, Office, HTML, CSV/JSON/XML, ZIP, EPUB, or other
   document formats, route through `convert-plaintext-to-md` first and use its
   bundled `scripts/markitdown_to_md.py` helper to create Markdown source files.
4. Run the requested Graphify mode, preserving cache/update behavior when available.
5. Verify expected artifacts exist before reporting completion.
6. Keep uncertainty visible: separate extracted relationships from inferred or semantic relationships.

## Detailed Workflows

Read `references/full-graphify-workflow-2026-05-20.md` for the full legacy command flows, export modes, query/path/explain/add procedures, and honesty rules.

## Local Metadata Notes

- Invocation trigger formerly stored in frontmatter: `/graphify`.
