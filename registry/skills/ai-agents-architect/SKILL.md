---
name: ai-agents-architect
description: Use when designing or reviewing autonomous AI agent systems, especially
  agent loops, tool use, memory, planning, multi-agent orchestration, guardrails,
  or agent observability.
---

# AI Agents Architect

## Overview

Use this skill to design agent systems that can act autonomously while remaining controllable. Focus on bounded loops, tool contracts, state and memory, recovery behavior, human handoff, and observability before adding autonomy or multiple agents.

## When to Use

Use for tasks involving:

- Autonomous AI agent application design or review
- ReAct, plan-and-execute, supervisor, or multi-agent flows
- Tool/function calling architecture, tool registries, or dynamic tool selection
- Agent memory design: working, episodic, semantic, or retrieval-backed memory
- Agent planning, replanning, checkpointing, or recovery
- Agent guardrails, human approval gates, safety limits, or failure boundaries
- Agent evaluation, tracing, cost controls, and debugging visibility

Do not use this for generic "tool use" unless the tool calls are part of an agent loop or autonomous workflow.

## Use Existing Local Skills Instead

- Use `mcp-builder` when the work is specifically designing or implementing MCP servers, MCP clients, tool schemas, or protocol integrations.
- Use `agentic-eval` when the main problem is evaluator-optimizer loops, self-critique, rubrics, or LLM-as-judge quality gates.
- Use `prompt-engineer` when the main change is prompt/instruction contract design rather than runtime architecture.
- Use the `ai-engineer` runtime agent when implementation or debugging of model-backed application code is needed.
- Use Superpowers subagent workflow skills when orchestrating Codex workers; that is execution workflow design, not product agent architecture.

## Architecture Checklist

Before implementation, pin down:

- Goal: what the agent is allowed to accomplish without human intervention.
- Loop: ReAct, plan-and-execute, supervisor, or single-step tool call.
- Stop conditions: max iterations, max tokens, timeout, cost cap, and "ask human" rule.
- Tool surface: allowed tools, schemas, examples, error contracts, and permission boundaries.
- State: what lives in current context, durable memory, task checkpoints, and external stores.
- Planning: when plans are created, updated, invalidated, and exposed for review.
- Failure behavior: retry policy, fallback path, degraded mode, and surfaced errors.
- Safety: authorization checks, destructive-action approval, data-access boundaries, and audit trail.
- Observability: structured traces for decisions, tool calls, latency, token use, and failures.
- Evaluation: test scenarios for success paths, ambiguous input, tool failure, memory drift, and runaway loops.

## Core Patterns

### ReAct Loop

Use for simple tool use with clear reason-act-observe flow.

- Thought: decide the next useful action.
- Action: invoke one allowed tool with validated inputs.
- Observation: parse and incorporate the result.
- Repeat until the task is complete, blocked, or a stop limit is reached.
- Always include iteration, timeout, token, and cost limits.

### Plan and Execute

Use for complex multi-step tasks that need an explicit plan.

- Planner decomposes the objective into ordered steps.
- Executor performs steps against the real environment.
- Replanner updates the plan when observations invalidate assumptions.
- Planner and executor may be separate models only when that separation reduces risk or complexity.

### Tool Registry

Use when many tools exist or tools change at runtime.

- Register each tool with schema, trigger guidance, examples, and failure modes.
- Select a small relevant tool set per task instead of exposing everything.
- Lazy-load expensive or rarely used tools.
- Track tool usage, errors, latency, and agent selection quality.

### Hierarchical Memory

Use for long-running agents that need context beyond one turn.

- Working memory: current task context and scratch state.
- Episodic memory: past interactions, outcomes, and checkpoints.
- Semantic memory: durable facts and reusable patterns.
- Retrieval memory: long-term storage queried through RAG or structured lookup.
- Filter and summarize memory before injection; do not append everything verbatim.

### Supervisor Pattern

Use only when one agent with good tools is not enough.

- Supervisor owns decomposition, delegation, aggregation, and failure handling.
- Specialist agents have narrow capabilities and explicit output contracts.
- Handoffs include task, context, constraints, expected output, and stop criteria.
- Supervisor validates returned work before using it downstream.

### Checkpoint Recovery

Use for long-running tasks that may fail or be interrupted.

- Checkpoint after each successful step or transaction boundary.
- Store task state, inputs, outputs, decisions, and progress.
- Resume from the last known-good checkpoint.
- Clean up checkpoints after completion or mark them as retained evidence.

## Sharp Edges

### Unbounded Agent Loops

Severity: critical

Symptoms:

- Agent runs forever
- API costs spike
- Application hangs
- Tool calls repeat with little variation

Fix:

- Set max iterations, max tokens, timeouts, and cost caps.
- Add circuit breakers for repeated tool failures.
- Force a human-handoff state when the agent is stuck or confidence drops.

### Vague Tool Descriptions

Severity: high

Symptoms:

- Agent picks the wrong tool
- Parameter errors increase
- Agent claims it cannot do tasks covered by available tools

Fix:

- Give every tool a clear one-sentence purpose.
- Document when to use it and when not to.
- Include typed parameters, examples, expected outputs, and expected errors.

### Silent Tool Errors

Severity: high

Symptoms:

- Agent continues with missing or stale data
- Final answer is wrong
- Debugging requires reconstructing hidden failures

Fix:

- Return explicit tool errors to the agent.
- Include error type, recovery hints, and retry eligibility.
- Log tool inputs, outputs, failures, and correlation IDs.

### Memory Bloat

Severity: medium

Symptoms:

- Context windows fill quickly
- Agent references outdated facts
- Token cost rises without quality improvement

Fix:

- Summarize before storing.
- Filter by relevance and recency.
- Separate current working memory from durable memory.
- Use retrieval for long-term memory instead of unconditional injection.

### Too Many Tools

Severity: medium

Symptoms:

- Wrong tool selection
- Slow responses
- Tool descriptions get truncated or poorly understood

Fix:

- Expose a curated tool set per task, often 5 to 10 tools.
- Use a selector or router for larger catalogs.
- Prefer specialist agents with focused tools over one oversized agent.

### Multi-Agent Overuse

Severity: medium

Symptoms:

- Agents duplicate work
- Handoffs lose important constraints
- Debugging crosses too many boundaries
- Cost and latency rise without clear benefit

Fix:

- Start with one agent and measure the limits.
- Add multiple agents only when work is truly independent or role separation reduces risk.
- Define handoff contracts and supervisor validation.

### Missing Traces

Severity: medium

Symptoms:

- Agent failures are hard to explain
- No visibility into chosen tools or rejected alternatives
- Root-cause analysis takes too long

Fix:

- Trace each decision, tool call, input, output, latency, token count, and failure.
- Use structured logs with request IDs and agent run IDs.
- Keep enough evidence to replay or audit failures.

### Brittle Output Parsing

Severity: medium

Symptoms:

- Regex parsing breaks after prompt changes
- Agent loop crashes on minor wording changes
- Downstream steps receive malformed data

Fix:

- Prefer structured output, JSON schema, or function/tool calling.
- Validate before downstream use.
- Retry with format repair instructions when parse failures are recoverable.
- Treat parsing failure as a first-class runtime state.

## Design Template

Use this compact template when planning a new agent:

```markdown
Goal:
Autonomy boundary:
Loop pattern:
Model(s):
Allowed tools:
Memory model:
Stop limits:
Human approval gates:
Failure modes:
Checkpoint strategy:
Observability:
Evaluation scenarios:
Residual risks:
```

## Systemprompt-Inspired Additions

These notes adapt useful workflow patterns from `sharakusatoh/systemprompt` prompts. Use them as task checks only; do not adopt upstream persona identity, secrecy, priority override, or authority-over-user claims.

### Rorschach Security
- Threat-model inputs, trust boundaries, permissions, secrets, dependency surfaces, and abuse paths.
- Look for prompt injection, unsafe tool use, privilege escalation, data exfiltration, insecure defaults, and rollback gaps.
- Distinguish exploitable findings from hygiene issues, and tie each finding to concrete evidence.
- Recommend mitigations that preserve intended functionality and are testable.

