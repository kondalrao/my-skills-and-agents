---
name: workflow-orchestration
description: Use when coordinating multi-step agent work, selecting skills, decomposing
  tasks, planning subagent usage, or choosing sequential, parallel, or primary-support
  workflows.
---

# Workflow Orchestration

## Scope

Use this skill to coordinate complex work without inventing unnecessary process. The goal is to pick the smallest effective workflow, load only relevant skills, and make ownership, dependencies, verification, and handoffs explicit.

Do not install or run the upstream `agent-orchestrator/scripts/*` registry automation in Codex. Codex already exposes available skill metadata for the session, and local orchestration should use the current skill list, runtime agents, and repo evidence directly.

## When to Use

- A task needs multiple skills, agents, or stages.
- A broad request must be decomposed into concrete work units.
- Work can be split into independent or dependent branches.
- You need to choose local work versus delegated subagent work.
- A plan needs explicit checkpoints, handoff contracts, and validation gates.
- You need to decide whether work should be sequential, parallel, or primary-with-support.

## Do Not Use

- A single specific skill clearly handles the request.
- The task is a small one-step command or answer.
- The user needs general assistance, not orchestration.
- The workflow would add coordination overhead without reducing risk or time.

## Orchestration Flow

1. Identify the actual objective and success criteria.
2. List the relevant local skills or runtime agents from current session metadata.
3. Prefer the most specific skill or agent that can complete the task alone.
4. If multiple capabilities are needed, choose an orchestration pattern.
5. Define ownership, input, output, dependency, and verification for each stage.
6. Execute or hand off only after the workflow is concrete enough to validate.

## Skill Selection Rules

- Exact domain match wins over broad orchestration.
- Specific implementation skills beat general planning skills.
- Existing repo conventions beat generic workflow preferences.
- If two skills overlap, use the narrower skill first and keep this skill as coordination glue.
- If a skill requires scripts, references, or tools that are not installed locally, do not pretend they are available.

## Orchestration Patterns

### Sequential Pipeline

Use when one stage produces input needed by the next stage.

Example flow:

```text
research -> architecture plan -> implementation -> verification -> docs
```

Use this when later steps are blocked until earlier evidence or artifacts exist.

### Parallel Work

Use when branches can proceed independently without shared write scope or unresolved dependency.

Example flow:

```text
user request -> [frontend investigation, backend investigation, test audit] -> synthesis
```

Each branch needs a clear owner, bounded scope, and expected output. Avoid parallelism when workers would edit the same files or rediscover the same facts.

### Primary With Support

Use when one skill or agent owns the main task and others provide supporting evidence.

Example flow:

```text
debugger primary + docs researcher support -> fix plan
```

The primary owner integrates the supporting output and remains responsible for final correctness.

### Single Owner

Use when one skill, one runtime agent, or the parent agent can complete the work cleanly.

This is the default when coordination overhead is higher than task complexity.

## Subagent Use

Use subagents only for independent, bounded work that materially advances the current task.

Before delegating, define:

- Owner: the role or agent responsible.
- Scope: files, subsystem, or question owned by that agent.
- Inputs: exact context the agent needs.
- Output: expected summary, patch, evidence, or decision.
- Stop rule: when the agent should return blocked instead of guessing.
- Integration point: how the parent agent will verify and merge the result.

Keep urgent blocking work local when the next parent-agent step depends on it.

## Verification

Before calling an orchestrated task complete:

- Verify each stage output against its stated contract.
- Run the right checks for any changed code, docs, or configuration.
- Confirm delegated work in the filesystem or diff, not only from an agent report.
- Re-check dependency assumptions if the workflow changed mid-task.
- Record meaningful decisions or outcomes in the relevant continuity or project documentation.

## Common Pitfalls

- Adding a meta-orchestrator when one specific skill is enough.
- Running stale registry scripts instead of using current Codex skill metadata.
- Delegating overlapping work to multiple agents and then merging contradictions.
- Treating parallelism as inherently better than a short sequential path.
- Failing to define what each agent returns before dispatching it.
- Skipping final integration review because each individual branch looked reasonable.

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### President Sonic
- Frame decisions in terms of goals, constraints, tradeoffs, stakeholders, and reversibility.
- Convert strategy into executable priorities with explicit non-goals.
- Record why the chosen path beats alternatives.
- Keep leadership framing concise and operational.

### Work Force
- Break complex work into roles, dependencies, checkpoints, and handoff-ready tasks.
- Identify what can run in parallel, what must be sequenced, and what needs a primary owner.
- Define completion evidence for each workstream.
- Keep coordination overhead proportional to the task size.

