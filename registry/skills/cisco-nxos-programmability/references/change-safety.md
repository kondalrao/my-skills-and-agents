# Nexus Change Safety

Use this reference before any task that may change NX-OS device configuration or management access.

## Minimum Change Record

Capture:

- device(s), platform, NX-OS release, management VRF, and access method,
- requested change and business/technical reason,
- exact commands, playbook, API payload, or model diff,
- expected state after the change,
- rollback procedure,
- verification commands or tests,
- known blast radius and maintenance-window assumptions.

## Pre-Change Baseline

Always collect:

- running config or relevant config sections,
- logs around current time,
- relevant feature state,
- relevant protocol neighbors,
- interface status/counters for affected ports,
- route/VRF/VLAN/VXLAN state when impacted,
- management reachability and device-originated connectivity tests when relevant.

## Post-Change Verification

Use the same checks as the baseline, then add feature-specific checks:

- config contains only expected changes,
- affected interfaces/protocols are in expected state,
- no new critical logs appeared,
- route and neighbor counts did not drift unexpectedly,
- traffic or ping checks still pass,
- telemetry/API subscriptions still report expected state.

## Rollback Rules

- Define rollback before applying the change.
- Prefer exact inverse commands for small additions.
- Prefer restoring known-good config sections for complex edits.
- For as-code workflows, rollback through source control and the same pipeline when time allows.
- For management-plane changes, preserve an out-of-band recovery path.

## Silent Failure Points

- NX-API/RESTCONF/NETCONF feature disabled or bound to the wrong VRF.
- AAA/RBAC permits login but blocks config or model operations.
- HTTP success but device rejected part of the payload.
- Parser returns raw text because no Genie parser exists.
- Ansible reports changed but post-state does not match intent.
- Model-driven telemetry path exists but does not update for the feature being monitored.
- Manual emergency changes create drift from source-controlled desired state.
