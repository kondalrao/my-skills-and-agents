---
name: cisco-nxos-programmability
description: Use when automating, validating, testing, or programming Cisco Nexus
  NX-OS switches with pyATS/Genie, NX-API, RESTCONF, NETCONF, gNMI, Ansible cisco.nxos,
  Network as Code, or safe switch configuration workflows.
---

# Cisco NX-OS Programmability

## Purpose

Guide Nexus switch automation work across validation, data collection, API programming, desired-state automation, and change execution. Prefer official Cisco, Ansible, and project documentation over remembered syntax when the exact command, module, YANG path, or release behavior matters.

## Use This For

- Building or reviewing automation for Cisco Nexus NX-OS switches.
- Choosing between CLI automation, pyATS/Genie, NX-API, RESTCONF, NETCONF, gNMI, Ansible, Terraform, or Network as Code.
- Writing safe change plans, rollback plans, and pre/post validation for switch configuration.
- Parsing show commands, comparing device state, or creating testbed-driven network checks.
- Working with NX-OS programmability features, feature gates, management VRFs, or model-driven telemetry.

## Do Not Use This For

- Generic Python infrastructure automation with no Nexus or NX-OS device surface; use `python-devops-infrastructure-automation`.
- Kernel, eBPF, XDP, or host datapath work; use `ebpf`.
- Network graph modeling without device automation; use `networkx`.
- Diagrams only; use the diagramming skills.

## First Pass

1. Identify the target platform, NX-OS release, device family, lab vs production status, and access method.
2. Separate read-only validation from configuration changes.
3. Confirm required features and transport: SSH, NX-API, RESTCONF, NETCONF, gRPC/gNMI, guestshell, or container runtime.
4. For any write operation, require a baseline, expected state, rollback plan, and post-change verification.
5. Use primary docs for release-sensitive details before committing to exact module names, feature commands, YANG paths, or payload shape.

## Tool Selection

| Need | Default Path |
| --- | --- |
| Parse CLI output, learn device state, run before/after checks | pyATS/Genie |
| Small operational command collection over SSH | pyATS or Netmiko, depending on existing project stack |
| Declarative config tasks with idempotent modules | Ansible `cisco.nxos` |
| Desired-state NX-OS fabric config from YAML/Terraform | Cisco Network as Code |
| Program against NX-OS APIs | NX-API, RESTCONF, NETCONF, or gNMI |
| Streaming telemetry or model-driven state subscription | gNMI/gRPC telemetry |
| On-box automation or device-local scripting | NX-OS Python, guestshell, or application hosting after release check |

## Safety Workflow For Changes

Before applying config:

- Capture running config and the relevant operational state.
- Capture connectivity from the switch when reachability is part of the success criteria.
- State the exact config or payload to apply, the intended effect, and the blast radius.
- Define the rollback as concrete inverse commands, restored config sections, or source-control revert plus redeploy.
- Avoid batching unrelated changes.

After applying config:

- Re-run the same pre-change checks.
- Check logs for new errors around the change timestamp.
- Compare intended vs actual config/state.
- Report verification as passed, failed, or inconclusive with evidence.
- If failed, rollback first unless the user explicitly asks to preserve the failed state for debugging.

## Reference Routing

- Read `references/pyats-genie.md` for testbeds, parsing, `learn()`, Diff, and AEtest validation.
- Read `references/nxos-apis.md` for NX-API, RESTCONF, NETCONF, YANG, gNMI, and telemetry transport choices.
- Read `references/ansible-nxos.md` for `cisco.nxos` module patterns, inventory variables, idempotency, and verification.
- Read `references/network-as-code-nxos.md` for Cisco Network as Code, Terraform-backed YAML models, and when to avoid imperative scripts.
- Read `references/change-safety.md` before production-impacting changes or rollback planning.

## Output Contract

For design or review tasks, provide:

- recommended automation path and why,
- prerequisites and feature gates,
- commands, modules, or payloads to verify from primary docs,
- pre-change and post-change checks,
- rollback plan,
- residual risk and unknowns.

For implementation tasks, keep changes scoped to the requested repo or artifact, add tests or validation where practical, and document exact commands that could affect devices.
