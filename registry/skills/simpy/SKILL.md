---
name: simpy
description: Use when building, reviewing, or debugging Python SimPy discrete-event
  simulations involving processes, queues, resources, event timing, monitoring, capacity
  planning, logistics, service operations, manufacturing, or network traffic.
---

# SimPy

## Local Metadata Notes

- Former frontmatter `metadata`: short-description=Build SimPy discrete-event simulations

Use this skill for process-based discrete-event simulation in Python. Preserve
the upstream intent: SimPy models systems where entities move through processes,
wait for events, and contend for shared resources over simulation time.

Follow the project's dependency policy first. If SimPy is missing, verify the
active package manager before installing anything.

## Use When

- Modeling queues, wait times, service times, throughput, utilization, or
  bottlenecks.
- Simulating manufacturing, logistics, healthcare flow, call centers, retail
  checkout, packet/network traffic, scheduling, or resource capacity.
- Designing processes where entities compete for limited resources.
- Debugging a SimPy process that stalls, leaks a resource, misorders events, or
  reports impossible timing.
- Adding monitoring, statistics, reproducibility, or validation to a simulation.

## Skip When

- The system is continuous with fixed time steps or differential equations; use
  numerical modeling tools instead.
- The problem is pure graph analysis; use `networkx`.
- The task is only scientific claim appraisal; use `scientific-critical-thinking`.
- The user needs a real-time browser/UI workflow, not a simulation model.

## Modeling Workflow

1. Define the system boundary.
   - Entities: customers, jobs, vehicles, packets, parts, patients, requests.
   - Resources: servers, staff, machines, bandwidth, storage, inventory.
   - Processes: arrival, queue, service, transfer, failure, repair, departure.
   - Metrics: wait time, queue length, utilization, throughput, loss, latency.
2. Choose time units and random distributions.
   - Keep units explicit and consistent.
   - Seed randomness for reproducible runs.
3. Implement process generators.
   - A SimPy process is a Python generator that yields events.
   - Use `env.timeout(...)`, `env.process(...)`, resource requests, and custom
     events to model delays and synchronization.
4. Model shared resources.
   - Use `Resource`, `PriorityResource`, `PreemptiveResource`, `Container`,
     `Store`, `FilterStore`, or `PriorityStore` based on the constraint.
5. Add monitoring before tuning.
   - Collect event-level observations during the run, not only final totals.
   - Use `scripts/resource_monitor.py` as a reusable starting point when useful.
6. Validate and analyze.
   - Check simple cases against hand calculations or known queueing formulas.
   - Run multiple seeds when stochastic behavior matters.
   - Report confidence intervals or distribution summaries, not just one run.

## Core Pattern

```python
import random
import simpy


def customer(env, name, server, stats):
    arrival = env.now
    with server.request() as req:
        yield req
        wait = env.now - arrival
        service_time = random.uniform(2, 4)
        yield env.timeout(service_time)
    stats.append({"name": name, "arrival": arrival, "wait": wait})


def arrivals(env, server, stats):
    i = 0
    while True:
        yield env.timeout(random.expovariate(1 / 3))
        i += 1
        env.process(customer(env, f"customer-{i}", server, stats))


random.seed(42)
env = simpy.Environment()
server = simpy.Resource(env, capacity=2)
stats = []
env.process(arrivals(env, server, stats))
env.run(until=100)
```

## Resource Selection

| Need | SimPy type | Reference |
| --- | --- | --- |
| Limited identical capacity | `Resource` | `references/resources.md` |
| Priority queueing | `PriorityResource` | `references/resources.md` |
| Interrupt lower-priority users | `PreemptiveResource` | `references/resources.md` |
| Bulk material or continuous quantity | `Container` | `references/resources.md` |
| FIFO object queue | `Store` | `references/resources.md` |
| Selective object retrieval | `FilterStore` | `references/resources.md` |
| Priority-ordered objects | `PriorityStore` | `references/resources.md` |
| Custom synchronization | `env.event()`, `AllOf`, `AnyOf` | `references/events.md` |
| Hardware-in-loop or wall-clock sync | `simpy.rt.RealtimeEnvironment` | `references/real-time.md` |

## Bundled Resources

- `references/resources.md`: SimPy resource types and usage patterns.
- `references/events.md`: event creation, callbacks, combining events, and
  synchronization.
- `references/process-interaction.md`: waiting on processes, interrupts, and
  process coordination.
- `references/monitoring.md`: metrics, event tracing, resource monitoring, and
  data export.
- `references/real-time.md`: real-time simulation behavior.
- `scripts/basic_simulation_template.py`: queue simulation template.
- `scripts/resource_monitor.py`: reusable resource and container monitors.

## Validation Checklist

- Simulation time units are documented.
- Random seeds are set or stochastic variation is intentionally explored.
- Resource requests use context managers or explicit release paths.
- No Python blocking calls are used inside SimPy processes.
- Metrics are collected at the event level needed for the question.
- Results are checked against a simple baseline, hand calculation, or sanity
  expectation.
- Sensitivity to key assumptions is reported when conclusions depend on them.

## Common Pitfalls

- Forgetting `yield`; the process runs immediately instead of scheduling work.
- Reusing an event after it has already fired.
- Letting a resource request escape without release.
- Mixing time units across arrivals, service times, and reporting.
- Treating one stochastic run as a stable conclusion.
- Creating a deadlock where no scheduled process can make progress.

## Related Skills

- Use `networkx` when the simulated system depends on graph topology or routing.
- Use `scientific-critical-thinking` to assess whether a simulation design can
  support a scientific or operational conclusion.
- Use `markdown-mermaid-writing` to document process flows, resource contention,
  or simulation architecture in Markdown.

## Attribution

Adapted for Codex from the K-Dense `scientific-agent-skills` SimPy skill under
its MIT license.
