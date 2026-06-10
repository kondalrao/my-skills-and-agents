# pyATS and Genie for NX-OS

Use pyATS/Genie when the task needs structured device state, repeatable checks, or before/after comparison across Nexus switches. pyATS is especially useful when show-command parsing and normalized feature learning reduce brittle text parsing.

Primary source:
- Cisco pyATS documentation: https://developer.cisco.com/docs/pyats/

## Typical Flow

1. Load the testbed from the project-defined YAML file.
2. Connect with `learn_hostname=True` when hostname normalization matters.
3. Use `device.parse("show ...")` when a parser exists and the task is command-specific.
4. Use `device.learn("feature")` when a normalized feature model is better than command output.
5. Use `genie.utils.diff.Diff` for before/after comparisons.
6. Disconnect cleanly and preserve evidence in JSON or text artifacts.

## Minimal Pattern

```python
from genie.testbed import load

testbed = load("testbed.yaml")
dev = testbed.devices["leaf1"]
dev.connect(learn_hostname=True, log_stdout=False)

interfaces = dev.parse("show interface status")
platform = dev.learn("platform")

dev.disconnect()
```

## Before and After Diff

```python
from genie.testbed import load
from genie.utils.diff import Diff

testbed = load("testbed.yaml")
dev = testbed.devices["leaf1"]
dev.connect(learn_hostname=True, log_stdout=False)

before = dev.learn("interface")
# apply or observe change outside this snippet
after = dev.learn("interface")

diff = Diff(before.info, after.info)
diff.findDiff()
print(diff)

dev.disconnect()
```

## NX-OS Feature Checks

Good candidates for `learn()` or parser-driven checks:

- interface state, counters, MTU, speed, admin state,
- VLAN and VXLAN state,
- VRF and routing table state,
- BGP/OSPF/ISIS neighbors,
- LLDP/CDP neighbors,
- platform, inventory, image, modules,
- ACL or route-policy state where parsers exist.

## Guardrails

- Do not parse `show running-config` with regular expressions unless there is no structured alternative and the scope is narrow.
- Treat missing Genie parser support as an implementation detail to handle explicitly; fall back to raw output plus small targeted parsing.
- Keep secrets out of testbed files committed to source control.
- For production changes, pyATS is usually a validation layer, not the only change mechanism.
