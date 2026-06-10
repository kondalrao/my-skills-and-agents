# AI Skills and Agent Registry

This repository is a portable source of truth for reusable AI skills, agent
instructions, and tool-specific adapters. It keeps the author-owned definitions
in `registry/`, renders projections for supported tools, and commits generated
state so changes can be reviewed before installation.

## Repository Layout

- `registry/skills/`: canonical skill folders, each centered on `SKILL.md`.
- `registry/agents/`: canonical agent instruction files when present.
- `adapters/`: generated projections for tools such as Codex, Claude Code,
  OpenCode, Cursor, and VS Code.
- `catalog.yaml`: human-readable inventory of registered skills and agents.
- `state/manifest.json`: generated file manifest and hashes used by validation.
- `docs/`: setup, interoperability, and troubleshooting notes.
- `scripts/`: sync, validation, import, render, migration, and install helpers.

## Common Workflow

```bash
git pull --rebase
scripts/sync.sh
PYTHONPYCACHEPREFIX=/private/tmp/my-skills-and-agents-pycache scripts/validate.sh
git status
```

Edit `registry/` as the canonical source. Use `scripts/sync.sh` to import native
edits, render adapters, refresh generated state, and run validation. Commit the
registry, generated adapters, catalog, manifest, docs, and scripts together when
they are part of the same change.

Do not commit local auth files, runtime sessions, telemetry, plugin caches,
secrets, logs, or generated backups.

## Installation

Use the install helpers after validation:

```bash
scripts/install-local.sh
scripts/install-project-adapters.sh
```

See `docs/INSTALL.md`, `docs/INTEROP.md`, and `docs/TROUBLESHOOTING.md` for
details on local installation, adapter behavior, and common failure modes.

## Skill Catalog

- `agent-md-refactor`: refactoring bloated AGENTS.md, CLAUDE.md, or similar agent instruction files into scoped, progressive guidance.
- `agent-rules-books-router`: coding work should be guided by book-derived software-engineering rule sets, especially for refactoring, review, architecture, legacy code, reliability, data systems, domain modeling, or implementation discipline.
- `agentic-eval`: evaluating or improving AI agent outputs with clear rubrics, datasets, traces, scoring, or iteration loops.
- `ai-agents-architect`: designing or reviewing autonomous AI agent systems, especially agent loops, tool use, memory, planning, multi-agent orchestration, guardrails, or agent observability.
- `api-design-agent`: designing or reviewing scalable, consistent, developer-friendly APIs, contracts, resources, authentication, or versioning.
- `architecture-blueprint-generator`: generating architecture blueprints from a codebase, including patterns, components, interactions, and extension points.
- `architecture-decision-records`: documenting significant architectural decisions, reviewing past technical choices, recording trade-offs, or establishing ADR decision processes.
- `browser-use`: automating browser navigation, forms, screenshots, state inspection, web testing, or webpage data extraction with browser-use.
- `capacity`: checking Azure OpenAI model capacity, quota, regional availability, or deployment feasibility before creating a model deployment.
- `cc-godmode`: coordinating a broad multi-agent development workflow that needs research, architecture, implementation, validation, testing, and release handoffs.
- `cisco-nxos-programmability`: automating, validating, testing, or programming Cisco Nexus NX-OS switches with pyATS/Genie, NX-API, RESTCONF, NETCONF, gNMI, Ansible cisco.nxos, Network as Code, or safe switch configuration workflows.
- `clarify`: a vague, messy, voice-dictated, multi-part, or stress-test request should become a clean self-contained prompt before execution.
- `code-review-agent`: reviewing code for correctness, maintainability, security, regressions, test gaps, or merge readiness.
- `content-research-writer`: writing blog posts, articles, newsletters, tutorials, case studies, or sourced documentation that needs research, citations, outlines, hooks, draft feedback, voice preservation, or publication polish.
- `context-map`: mapping files, entry points, dependencies, and ownership relevant to a task before changing code.
- `convert-plaintext-to-md`: converting plain text or lightly structured documentation into Markdown using explicit formatting instructions or examples.
- `copilot-cli-quickstart`: teaching GitHub Copilot CLI from scratch, answering CLI questions, or running a beginner tutorial flow.
- `create-agentsmd`: creating, replacing, or substantially refreshing a repository AGENTS.md from project evidence, commands, docs, CI, and local conventions.
- `create-architectural-decision-record`: creating a focused Architecture Decision Record document for a specific technical decision.
- `create-implementation-plan`: creating a structured implementation plan for a feature, refactor, upgrade, design, architecture, or infrastructure change.
- `create-specification`: creating an AI-ready specification that defines requirements, constraints, interfaces, acceptance criteria, and examples.
- `create-technical-spike`: creating a time-boxed technical spike document for researching a critical implementation decision.
- `create-tldr-page`: creating a tldr command page from official docs, help output, command examples, and strict tldr formatting.
- `creative-writing`: writing, revising, or critiquing fiction, literary prose, stories, scenes, dialogue, plot concepts, characters, titles, or creative narrative voice.
- `customize`: customizing Azure OpenAI model deployment choices, including region, capacity, quota, SKU, and project constraints.
- `debugging-agent`: reproducing, isolating, and fixing software defects through systematic root-cause debugging.
- `deploy-model`: deploying Azure OpenAI models in Microsoft Foundry, including preset, capacity, region, quota, or customization decisions.
- `developer-growth-analysis`: the user asks to analyze recent coding sessions, chat history, commits, or task work to identify developer strengths, recurring gaps, improvement areas, learning resources, and actionable growth plans.
- `docker-containerization-expert`: designing, reviewing, or troubleshooting Docker images, containers, runtime behavior, or container security.
- `draw-io-diagram-generator`: creating, editing, validating, or exporting draw.io diagrams such as architecture, flow, sequence, ER, UML, or network diagrams.
- `ebpf`: writing, reviewing, debugging, or explaining eBPF programs for Linux observability, networking, tracing, XDP, tc, or BPF maps.
- `excalidraw-diagram`: creating Excalidraw .excalidraw diagrams from natural language, workflows, architectures, systems, flowcharts, mind maps, data flows, or visual explanations.
- `explain-visually`: source material should become a responsive HTML visual explainer that teaches a repo, spec, PR, architecture, or concept.
- `graphify`: turning code, docs, papers, media, or notes into a knowledge graph with Graphify outputs, queries, exports, or vault artifacts.
- `graphify-vault-operator`: operating, repairing, validating, or explaining Graphify in the Obsidian vault, including scoped indexes, hook failures, graphify-out artifacts, or Graphify-backed subagent smoke tests.
- `grill-me`: stress-testing a plan or design through focused questioning until assumptions, tradeoffs, and gaps are explicit.
- `grill-with-docs`: challenging a plan against existing docs, domain language, ADRs, and known model constraints.
- `handoff`: the user asks to prepare a handoff, resume brief, context transfer, or next-session summary for another agent or future session.
- `human-writing-style`: editing prose-heavy notes, docs, summaries, specs, or user-facing text for direct, concrete, human writing.
- `idea-refine`: shaping a raw product, feature, process, or project idea before formal specs or implementation. Refines the idea through divergent options, convergent evaluation, assumption checks, MVP scope, and a concise idea one-pager.
- `kubernetes-container-orchestration`: designing, reviewing, or troubleshooting Kubernetes workloads, configuration, networking, storage, or operations.
- `linux-perf`: collecting, reading, or explaining Linux perf profiles, call graphs, flamegraphs, counters, or CPU performance evidence.
- `local-skill-lifecycle-manager`: adding, updating, merging, repairing, or validating local Codex skills under ~/.agents/skills or ~/.codex/skills, especially when checking uniqueness, overlap, frontmatter, or duplicate skill names.
- `make-skill-template`: creating a reusable GitHub Copilot skill template or scaffolding a new Agent Skill from a prompt.
- `markdown-mermaid-writing`: creating Markdown documents, reports, READMEs, ADRs, scientific notes, or version-controlled docs that should include Mermaid diagrams as the canonical text source for workflows, architectures, timelines, schemas, relationships, or visual explanations.
- `mcp-builder`: designing, building, or evaluating MCP servers and tools for external APIs or services.
- `mcp-cli`: interacting with MCP servers, tools, APIs, or resources through a CLI workflow.
- `mentor-teacher`: writing a detailed learning synthesis note to the user's Obsidian vault after completing a task.
- `microsoft-foundry`: deploying, evaluating, optimizing, or troubleshooting Microsoft Foundry agents, model deployments, quota, capacity, RBAC, or project setup.
- `monitoring-observability`: designing or reviewing monitoring, observability, logs, traces, metrics, alerts, Prometheus, or Grafana workflows.
- `networkx`: creating, analyzing, importing, exporting, or visualizing Python NetworkX graphs for relationship data, graph algorithms, shortest paths, centrality, clustering, communities, synthetic networks, topology, or knowledge graphs.
- `obsidian-vault`: searching, creating, organizing, or updating Obsidian vault notes, wikilinks, indexes, and local note conventions.
- `personal-teacher-mentor`: the user wants teacher or mentor behavior during task work, or when completed work should be turned into a plain-language Obsidian note that explains the task, reasoning, rejected approaches, tradeoffs, mistakes, lessons learned, and any durable workflow or documentation updates.
- `practice-cognition`: a plan, hypothesis, design, or judgment needs validation through direct practice, trial runs, feedback, or iteration before treating it as true.
- `premium-frontend-ui`: crafting immersive, polished frontend UI with advanced motion, typography, responsive layout, and visual hierarchy.
- `preset`: selecting a recommended Azure OpenAI model deployment preset based on capacity, region, quota, and project constraints.
- `project-workflow-analysis-blueprint-generator`: documenting end-to-end application workflows by tracing entry points, data flow, services, persistence, errors, and tests.
- `prompt-builder`: helping create high-quality GitHub Copilot prompts with structure, tool context, constraints, and examples.
- `publish-to-pages`: publishing HTML, PDF, PPTX, Google Slides, presentations, or web content to GitHub Pages.
- `python-async-programming-export`: working on Python asyncio, concurrency patterns, event loops, cancellation, tasks, or async safety.
- `python-devops-infrastructure-automation`: building Python DevOps, infrastructure automation, IaC, CI/CD, or operational tooling workflows.
- `python-fastapi-development`: designing, implementing, reviewing, or deploying Python FastAPI backends, validation, and API behavior.
- `python-mcp-server-generator`: generating a Python MCP server project with tools, resources, configuration, and runnable structure.
- `reasoner-planner-agent`: structuring dependency-aware, risk-aware reasoning and execution plans before implementation.
- `refactor`: safely refactoring code to improve maintainability without changing behavior.
- `refactor-plan`: planning a multi-file refactor with sequencing, rollback points, and verification steps.
- `reflect-on-changes`: summarizing recent code changes, review findings, touched docs, or lessons into durable follow-up guidance.
- `refractoring-agent`: improving code quality through behavior-preserving refactoring and conservative design cleanup.
- `ruff-recursive-fix`: running Ruff checks, applying autofixes, reviewing lint changes, and iterating until Python lint passes.
- `scientific-brainstorming`: exploring open-ended scientific research ideas, interdisciplinary connections, assumptions, research gaps, experimental designs, study plans, or novel hypotheses before evidence appraisal or implementation.
- `scientific-critical-thinking`: evaluating scientific claims, study design, evidence quality, statistical validity, bias, confounding, causal inference, GRADE/Cochrane-style appraisal, or research conclusions.
- `scientific-slides`: planning, writing, reviewing, or building scientific presentations, conference talks, seminars, thesis defenses, journal clubs, research decks, PowerPoint slides, or LaTeX Beamer talks.
- `simpy`: building, reviewing, or debugging Python SimPy discrete-event simulations involving processes, queues, resources, event timing, monitoring, capacity planning, logistics, service operations, manufacturing, or network traffic.
- `sora`: generating, editing, extending, polling, downloading, deleting, or queueing Sora video jobs with the bundled CLI.
- `task-observer`: observing repeated task patterns, skill gaps, reusable workflow candidates, or improvements that should become durable skills.
- `teach`: the user wants to learn a skill or concept over multiple sessions using an Obsidian-backed study workspace with missions, curated resources, lessons, references, learning records, and teaching notes.
- `technical-poster-design`: creating dense technical posters, infographics, one-page architecture maps, reference sheets, or use-case posters that need high information density, concrete sections, readable labels, diagrams, and PNG/PDF output rather than sparse art-poster styling.
- `valyu-best-practices`: using Valyu for real-time search, URL content extraction, cited answers, datasource selection, or deep research.
- `vault-setup`: setting up, verifying, importing into, or configuring an Obsidian vault with bundled vault setup tools.
- `workflow-orchestration`: coordinating multi-step agent work, selecting skills, decomposing tasks, planning subagent usage, or choosing sequential, parallel, or primary-support workflows.
- `youtube-summary`: the user provides a YouTube video or asks to transcribe, summarize, study, critique, or turn a YouTube source into an Obsidian knowledge note.
