# Ansible cisco.nxos

Use Ansible `cisco.nxos` when the task benefits from idempotent modules, inventory-driven configuration, facts collection, or repeatable playbook execution.

Primary source:
- Ansible Cisco NX-OS collection: https://docs.ansible.com/projects/ansible/latest/collections/cisco/nxos/

## Common Use Cases

- Gather facts with `cisco.nxos.nxos_facts`.
- Run operational commands with `cisco.nxos.nxos_command`.
- Apply scoped CLI configuration with `cisco.nxos.nxos_config`.
- Use resource modules for structured config where available.
- Use inventory/group vars for management VRF, transport, credentials, and fabric role.

## Inventory Pattern

```yaml
all:
  children:
    nxos:
      hosts:
        leaf1:
          ansible_host: 192.0.2.10
      vars:
        ansible_network_os: cisco.nxos.nxos
        ansible_connection: ansible.netcommon.network_cli
```

For NX-API-based workflows, verify the current `cisco.nxos` collection docs for the required connection plugin and variables before writing examples.

## Playbook Pattern

```yaml
- name: Validate Nexus state
  hosts: nxos
  gather_facts: false
  tasks:
    - name: Gather NX-OS facts
      cisco.nxos.nxos_facts:

    - name: Check interface status
      cisco.nxos.nxos_command:
        commands:
          - show interface status
      register: interface_status
```

## Change Pattern

1. Run facts and command checks first.
2. Apply the narrowest module or `nxos_config` block that represents the change.
3. Register output.
4. Re-run validation commands.
5. Fail the play if post-checks do not match expected state.

## Guardrails

- Prefer resource modules over raw config when they cover the feature cleanly.
- Use `check_mode` where supported, but do not treat it as proof of device behavior.
- Avoid giant generated config blobs unless the deployment strategy is explicitly replace-style and rollback is clear.
- Pin or record the `cisco.nxos` collection version for repeatable behavior.
- Keep secrets in vaults or external secret managers, not inventory files.
