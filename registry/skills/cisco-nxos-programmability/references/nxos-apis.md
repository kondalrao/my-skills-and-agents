# NX-OS APIs, YANG, and Telemetry

Use this reference when selecting or implementing a Nexus programmability interface. Verify release-specific behavior against Cisco docs before using exact payloads or feature commands.

Primary sources:
- Cisco Nexus 9000 NX-OS Programmability Guide: https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/105x/programmability/cisco-nexus-9000-series-nx-os-programmability-guide-105x/chapter-1.html
- Cisco Open NX-OS API documentation: https://developer.cisco.com/docs/nx-os/application-programming-interface-api/

## Interface Selection

| Interface | Use When | Notes |
| --- | --- | --- |
| NX-API CLI | You need HTTP access to CLI-style commands or legacy scripts already use NX-API | Check `feature nxapi`, management VRF, HTTP/HTTPS settings, and AAA behavior. |
| RESTCONF | You want REST-style model-driven operations through YANG models | Validate supported models and release behavior. |
| NETCONF | You need standards-based config/state operations with YANG and transactions | Good for controller-style automation and structured config. |
| gNMI/gRPC | You need model-driven telemetry or modern get/set/subscription behavior | Confirm gRPC/gNMI feature support and encoding. |
| On-box Python / guestshell | You need device-local scripts, event handling, or proximity to local files/commands | Release and platform support vary; validate feature availability. |

## Feature Gate Checklist

- Is the feature supported on the exact Nexus family and NX-OS release?
- Is the feature enabled: `feature nxapi`, `feature netconf`, RESTCONF, gRPC, guestshell, or related command?
- Which VRF carries management/API traffic?
- Are certificates, AAA, and RBAC configured for the automation account?
- Are payloads based on Cisco native YANG, OpenConfig, or CLI JSON?
- Is the operation read-only, candidate/transactional, or immediate configuration?

## Implementation Shape

For API code:

1. Keep transport/session setup separate from business logic.
2. Make payload construction data-driven and testable.
3. Log method, endpoint/model path, target device, and request id; do not log credentials.
4. Validate response status and returned device state, not just HTTP success.
5. Make retries conservative. Do not retry non-idempotent writes blindly.

## Telemetry Notes

- Prefer subscription-based telemetry for continuous state over periodic CLI polling when supported.
- Keep paths, sample intervals, encoding, and receiver behavior version-controlled.
- Validate that telemetry data maps back to operational questions; do not collect broad paths without a consumer.
