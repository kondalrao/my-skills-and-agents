# Learning Record Format

Learning records live in:

```text
learning-records/NNNN-<slug>.md
```

They are not session logs. They capture non-obvious learning state that should change future teaching.

## Template

```markdown
# <Short Title>

<One to three sentences explaining what was learned or established, why it matters, and how it changes future lessons.>
```

## Optional Sections

Use these only when they add value:

```markdown
Status: active
```

```markdown
## Evidence

<How the user demonstrated the understanding or revealed prior knowledge.>
```

```markdown
## Implications

<What this unlocks, rules out, or changes for future lessons.>
```

## When To Write One

Write a learning record when:

- The user demonstrates genuine understanding, not just exposure.
- The user discloses prior knowledge and its depth matters.
- A misconception is corrected.
- The mission shifts because learning changed what the user wants.

Do not write a learning record for material that was merely covered, routine progress notes, or definitions better captured in a glossary.

## Numbering

Scan `learning-records/` for the highest existing number and increment by one. When a later record contradicts an earlier record, mark the earlier record as superseded instead of deleting it.
