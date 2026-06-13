#!/usr/bin/env python3
"""Draft a non-mutating skill enhancement proposal from user feedback."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys


def read_feedback(args: argparse.Namespace) -> str:
    if args.feedback_file:
        return Path(args.feedback_file).read_text().strip()
    if args.feedback:
        return args.feedback.strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    raise SystemExit("error: provide --feedback, --feedback-file, or stdin")


def affected_files(feedback: str) -> list[str]:
    text = feedback.lower()
    files = {"SKILL.md", "references/learning-backlog.md"}
    if any(word in text for word in ["svg", "png", "diagram", "mermaid", "storage", "toc", "width"]):
        files.add("references/confluence-storage-patterns.md")
        files.add("scripts/confluence_storage_snippets.py")
    if any(word in text for word in ["token", "auth", "rest", "attachment", "upload", "property", "readback", "verify"]):
        files.add("scripts/confluence_rest.py")
        files.add("scripts/verify_confluence_page.py")
        files.add("scripts/upload_confluence_attachments.py")
    if any(word in text for word in ["render", "mmdc", "mermaid-cli"]):
        files.add("scripts/render_mermaid_images.py")
        files.add("scripts/install_mermaid_cli.sh")
    if any(word in text for word in ["learn", "self", "approve", "approval", "backlog"]):
        files.add("scripts/propose_skill_update.py")
    return sorted(files)


def summarize_change(feedback: str) -> str:
    text = feedback.lower()
    if "always" in text or "default" in text:
        return "Promote the feedback into default workflow guidance if it is globally applicable."
    if "script" in text or "recreate" in text:
        return "Add or update a bundled script so future runs reuse the behavior instead of recreating it."
    if "verify" in text or "readback" in text:
        return "Strengthen the verification checklist and verifier script around this condition."
    return "Clarify the skill instructions and references to preserve this reusable preference."


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--feedback", help="User feedback to evaluate")
    parser.add_argument("--feedback-file", help="File containing user feedback")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    feedback = read_feedback(args)
    files = affected_files(feedback)
    change = summarize_change(feedback)
    validation = [
        "python3 /Users/kkomarag/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/kkomarag/.agents/skills/confluence-technical-publisher",
        "python3 -m py_compile /Users/kkomarag/.agents/skills/confluence-technical-publisher/scripts/*.py",
        "bash -n /Users/kkomarag/.agents/skills/confluence-technical-publisher/scripts/install_mermaid_cli.sh",
        "Run a project-specific secret and identifier scan before finalizing the approved update.",
    ]

    print("# Skill Enhancement Candidate")
    print()
    print("## Feedback Summary")
    print(feedback)
    print()
    print("## Affected Skill Files")
    for file in files:
        print(f"- `{file}`")
    print()
    print("## Proposed Behavioral Change")
    print(change)
    print()
    print("## Approval Required")
    print("Do not edit the skill until the user explicitly approves this proposed change.")
    print()
    print("## Validation Commands After Approval")
    for command in validation:
        print(f"- `{command}`")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
