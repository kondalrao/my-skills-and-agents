# Cisco Network as Code for NX-OS

Use Cisco Network as Code when the desired outcome is model-driven NX-OS configuration from version-controlled YAML and Terraform-backed workflows rather than imperative scripts.

Primary source:
- Cisco Network as Code NX-OS introduction: https://netascode.cisco.com/docs/start/nxos/introduction/

## Use When

- A team wants version-controlled desired state for Nexus configuration.
- The same model should apply consistently across multiple devices.
- Code review, drift review, and pipeline execution are more important than ad hoc CLI speed.
- Operators prefer data-model-shaped YAML that maps to familiar NX-OS concepts.

## Avoid When

- The task is a one-off diagnostic or short read-only query.
- Existing production automation is already standardized on Ansible, pyATS, or a controller and adding Terraform would fragment ownership.
- The required NX-OS feature is not covered by the data model.

## Workflow

1. Confirm the NX-OS module/provider supports the target release and feature.
2. Model intent in YAML or the repository's established data format.
3. Run format/schema validation.
4. Run `terraform plan` or the project wrapper to inspect the diff.
5. Apply through the established pipeline.
6. Validate device state with pyATS/Genie or equivalent post-checks.

## Guardrails

- Treat generated Terraform plans as review artifacts, not just command output.
- Keep credentials, device inventory, and environment-specific values separated from reusable intent.
- Preserve a clear ownership boundary between as-code desired state and emergency/manual remediation.
- Record manual changes and reconcile them back into source control quickly.
