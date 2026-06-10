#!/usr/bin/env python3
"""Manage the shared skills and agents registry.

The script intentionally uses only the Python standard library so it can run on
the laptop and on a minimal Linux server.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import tomllib
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
REGISTRY = REPO / "registry"
SKILLS = REGISTRY / "skills"
AGENTS = REGISTRY / "agents"
ADAPTERS = REPO / "adapters"
REPORTS = REPO / "reports"
STATE = REPO / "state"

LOCAL_SKILLS = Path.home() / ".agents" / "skills"
CODEX_AGENTS = Path.home() / ".codex" / "agents"
CLAUDE_AGENTS = Path.home() / ".claude" / "agents"
CLAUDE_SKILLS = Path.home() / ".claude" / "skills"
OPENCODE_SKILLS = Path.home() / ".config" / "opencode" / "skills"
OPENCODE_AGENTS = Path.home() / ".config" / "opencode" / "agents"

SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
FORBIDDEN_PARTS = {
    ".env",
    "node_modules",
    "sessions",
    "telemetry",
    "plugin-cache",
    "plugins/cache",
    ".codex/sessions",
    ".claude/projects",
    ".cursor/projects",
}


def now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def rel(path: Path) -> str:
    return str(path.relative_to(REPO))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def split_frontmatter(text: str) -> tuple[dict[str, str], str, str]:
    if not text.startswith("---\n"):
        return {}, "", text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, "", text
    raw = text[4:end]
    body = text[text.find("\n", end + 1) + 1 :]
    return parse_simple_yaml(raw), raw, body


def parse_simple_yaml(raw: str) -> dict[str, str]:
    data: dict[str, str] = {}
    current: str | None = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[0].isspace() and current:
            data[current] = f"{data[current]} {line.strip()}".strip()
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        current = key.strip()
        data[current] = strip_scalar(value.strip())
    return data


def strip_scalar(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def yaml_scalar(value: str) -> str:
    return json.dumps(str(value), ensure_ascii=False)


def dump_frontmatter(fields: dict[str, str]) -> str:
    lines = ["---"]
    for key, value in fields.items():
        lines.append(f"{key}: {yaml_scalar(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def skill_files(root: Path = SKILLS) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.rglob("SKILL.md") if path.is_file())


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists() or dst.is_symlink():
        shutil.rmtree(dst)
    ignore = shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc")
    shutil.copytree(src, dst, symlinks=True, ignore=ignore)


def slug(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return cleaned or "unnamed"


def ensure_dirs() -> None:
    for path in [
        SKILLS,
        AGENTS,
        ADAPTERS / "codex" / "agents",
        ADAPTERS / "claude" / "agents",
        ADAPTERS / "opencode" / "agents",
        ADAPTERS / "cursor" / "rules",
        ADAPTERS / "vscode" / "instructions",
        REPORTS / "audits",
        REPORTS / "conflicts",
        STATE,
    ]:
        path.mkdir(parents=True, exist_ok=True)


def migrate_local() -> None:
    ensure_dirs()
    audits: list[str] = []

    if not LOCAL_SKILLS.exists():
        raise SystemExit(f"missing local skills root: {LOCAL_SKILLS}")

    for skill_md in sorted(LOCAL_SKILLS.glob("*/SKILL.md")):
        text = read_text(skill_md)
        meta, _, _ = split_frontmatter(text)
        source_dir = skill_md.parent
        name = meta.get("name") or source_dir.name
        target_name = slug(name)
        if name != target_name:
            audits.append(f"- normalized `{source_dir.name}` / `{name}` -> `{target_name}`")
        target_dir = SKILLS / target_name
        copy_tree(source_dir, target_dir)

    opencode_report = compare_opencode_skills()
    if opencode_report:
        audits.append(opencode_report)

    migrate_codex_agents(audits)
    render_adapters()
    write_catalog()
    write_manifest()

    audit_text = "# Migration Audit\n\n" + "\n".join(audits or ["- no migration notes"])
    write_text(REPORTS / "audits" / f"migration-{now_stamp()}.md", audit_text + "\n")
    print("MIGRATE_OK")


def compare_opencode_skills() -> str:
    if not OPENCODE_SKILLS.exists():
        return ""
    lines: list[str] = ["\n## OpenCode Skill Comparison"]
    found = False
    for skill_md in sorted(OPENCODE_SKILLS.glob("*/SKILL.md")):
        text = read_text(skill_md)
        meta, _, _ = split_frontmatter(text)
        name = slug(meta.get("name") or skill_md.parent.name)
        registry_skill = SKILLS / name / "SKILL.md"
        if registry_skill.exists():
            if read_text(registry_skill) != text:
                found = True
                diff = "\n".join(
                    difflib.unified_diff(
                        read_text(registry_skill).splitlines(),
                        text.splitlines(),
                        fromfile=f"registry/skills/{name}/SKILL.md",
                        tofile=str(skill_md),
                        lineterm="",
                    )
                )
                lines.append(f"\n### duplicate `{name}` differs\n\n```diff\n{diff}\n```")
            continue
        found = True
        target = SKILLS / name
        copy_tree(skill_md.parent, target)
        lines.append(f"- imported OpenCode-only skill `{name}` from `{skill_md.parent}`")
    if not found:
        return ""
    text = "\n".join(lines)
    write_text(REPORTS / "audits" / f"opencode-skills-{now_stamp()}.md", text + "\n")
    return text


def migrate_codex_agents(audits: list[str]) -> None:
    if not CODEX_AGENTS.exists():
        raise SystemExit(f"missing Codex agents root: {CODEX_AGENTS}")
    claude_bodies = read_claude_agent_bodies()
    overlaps = 0
    for toml_path in sorted(CODEX_AGENTS.glob("*.toml")):
        data = tomllib.loads(read_text(toml_path))
        name = data.get("name") or toml_path.stem
        description = data.get("description", "")
        body = data.get("developer_instructions", "").strip() + "\n"
        if name in claude_bodies:
            overlaps += 1
            claude_body = claude_bodies[name].strip()
            if claude_body and normalize_text(claude_body) not in normalize_text(body):
                body = (
                    body.rstrip()
                    + "\n\n## Legacy Claude Source Notes\n\n"
                    + claude_body
                    + "\n"
                )
        fields = {
            "name": name,
            "description": description,
            "type": "agent",
            "source": "local",
            "status": "active",
            "codex_model": str(data.get("model", "")),
            "codex_model_reasoning_effort": str(data.get("model_reasoning_effort", "")),
            "codex_sandbox_mode": str(data.get("sandbox_mode", "")),
        }
        write_text(AGENTS / f"{name}.agent.md", dump_frontmatter(fields) + "\n" + body)
    audits.append(f"- migrated `{len(list(CODEX_AGENTS.glob('*.toml')))}` Codex agents")
    audits.append(f"- merged/preserved Claude body notes for `{overlaps}` overlapping agents")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def read_claude_agent_bodies() -> dict[str, str]:
    bodies: dict[str, str] = {}
    if not CLAUDE_AGENTS.exists():
        return bodies
    for path in sorted(CLAUDE_AGENTS.glob("*.md")):
        text = read_text(path)
        meta, _, body = split_frontmatter(text)
        name = meta.get("name") or path.stem
        bodies[name] = body
    return bodies


def agent_sources() -> list[tuple[Path, dict[str, str], str]]:
    agents: list[tuple[Path, dict[str, str], str]] = []
    for path in sorted(AGENTS.glob("*.agent.md")):
        meta, _, body = split_frontmatter(read_text(path))
        if not meta.get("name"):
            raise SystemExit(f"agent missing name: {path}")
        agents.append((path, meta, body.strip() + "\n"))
    return agents


def render_adapters() -> None:
    ensure_dirs()
    for subdir in [
        ADAPTERS / "codex" / "agents",
        ADAPTERS / "claude" / "agents",
        ADAPTERS / "opencode" / "agents",
        ADAPTERS / "cursor" / "rules",
        ADAPTERS / "vscode" / "instructions",
    ]:
        if subdir.exists():
            shutil.rmtree(subdir)
        subdir.mkdir(parents=True, exist_ok=True)

    agents = agent_sources()
    for _, meta, body in agents:
        name = meta["name"]
        description = meta.get("description", "")
        write_text(
            ADAPTERS / "codex" / "agents" / f"{name}.toml",
            render_codex_agent(meta, body),
        )
        write_text(
            ADAPTERS / "claude" / "agents" / f"{name}.md",
            dump_frontmatter({"name": name, "description": description}) + "\n" + body,
        )
        write_text(
            ADAPTERS / "opencode" / "agents" / f"{name}.md",
            dump_frontmatter(
                {"name": name, "description": description, "mode": "subagent"}
            )
            + "\n"
            + body,
        )

    render_ide_adapters(agents)
    write_manifest()
    print("RENDER_OK")


def render_codex_agent(meta: dict[str, str], body: str) -> str:
    lines = [
        f"name = {json.dumps(meta['name'])}",
        f"description = {json.dumps(meta.get('description', ''))}",
    ]
    if meta.get("codex_model"):
        lines.append(f"model = {json.dumps(meta['codex_model'])}")
    if meta.get("codex_model_reasoning_effort"):
        lines.append(
            f"model_reasoning_effort = {json.dumps(meta['codex_model_reasoning_effort'])}"
        )
    if meta.get("codex_sandbox_mode"):
        lines.append(f"sandbox_mode = {json.dumps(meta['codex_sandbox_mode'])}")
    lines.append(f"developer_instructions = {json.dumps(body)}")
    return "\n".join(lines) + "\n"


def render_ide_adapters(agents: list[tuple[Path, dict[str, str], str]]) -> None:
    summary_lines = [
        "# Shared Skills and Agents",
        "",
        "Use this repository as the source of truth for personal AI skills and agents.",
        "Native skill and agent invocation belongs to Codex, Claude Code, and OpenCode.",
        "Cursor and VS Code receive this instruction-level projection only.",
        "",
        "## Available Agent Roles",
        "",
    ]
    for _, meta, _ in agents:
        summary_lines.append(f"- `{meta['name']}`: {meta.get('description', '')}")
    summary = "\n".join(summary_lines).strip() + "\n"

    cursor = (
        "---\n"
        'description: "Shared personal AI skills and agents index"\n'
        'globs: "**/*"\n'
        "alwaysApply: false\n"
        "---\n\n"
        + summary
    )
    write_text(ADAPTERS / "cursor" / "rules" / "shared-skills-and-agents.mdc", cursor)

    write_text(ADAPTERS / "vscode" / "copilot-instructions.md", summary)
    write_text(
        ADAPTERS / "vscode" / "instructions" / "shared-skills-and-agents.instructions.md",
        "---\n"
        'applyTo: "**"\n'
        "---\n\n"
        + summary,
    )


def write_catalog() -> None:
    lines = ["version: 1", "items:"]
    for path in skill_files():
        meta, _, _ = split_frontmatter(read_text(path))
        name = meta.get("name") or path.parent.name
        lines.extend(
            [
                f"  - name: {yaml_scalar(name)}",
                '    type: "skill"',
                f"    path: {yaml_scalar(rel(path.parent))}",
                '    source: "local"',
                '    status: "active"',
                f"    why: {yaml_scalar(meta.get('description', ''))}",
                '    last_reviewed: ""',
            ]
        )
    for path, meta, _ in agent_sources():
        lines.extend(
            [
                f"  - name: {yaml_scalar(meta['name'])}",
                '    type: "agent"',
                f"    path: {yaml_scalar(rel(path))}",
                '    source: "local"',
                f"    status: {yaml_scalar(meta.get('status', 'active'))}",
                f"    why: {yaml_scalar(meta.get('description', ''))}",
                '    last_reviewed: ""',
            ]
        )
    write_text(REPO / "catalog.yaml", "\n".join(lines) + "\n")


def repo_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for root in [REGISTRY, ADAPTERS]:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*")):
            if path.is_file():
                hashes[rel(path)] = sha256_file(path)
    for name in ["catalog.yaml", "trust.yaml", "lock.json"]:
        path = REPO / name
        if path.exists():
            hashes[name] = sha256_file(path)
    return hashes


def write_manifest() -> None:
    manifest = {
        "version": 1,
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "pre_migration_backup": "/Users/kkomarag/backups/my-skills-and-agents/pre-migration-20260521-223435",
        "managed_paths": {
            "skills_shared": str(LOCAL_SKILLS),
            "skills_claude": str(CLAUDE_SKILLS),
            "skills_opencode": str(OPENCODE_SKILLS),
            "agents_codex": str(CODEX_AGENTS),
            "agents_claude": str(CLAUDE_AGENTS),
            "agents_opencode": str(OPENCODE_AGENTS),
        },
        "repo_hashes": repo_hashes(),
    }
    write_text(STATE / "manifest.json", json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def validate() -> None:
    errors: list[str] = []
    warnings: list[str] = []
    validate_forbidden(errors)
    validate_skills(errors, warnings)
    validate_agents(errors)
    validate_adapters(errors)
    validate_manifest(errors)
    if warnings:
        for warning in warnings:
            print(f"WARN: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)
    print("VALIDATE_OK")


def validate_forbidden(errors: list[str]) -> None:
    for path in REPO.rglob("*"):
        if ".git" in path.parts:
            continue
        relpath = rel(path)
        for part in FORBIDDEN_PARTS:
            if part in relpath:
                errors.append(f"forbidden path in repo: {relpath}")


def validate_skills(errors: list[str], warnings: list[str]) -> None:
    seen: dict[str, str] = {}
    for path in skill_files():
        meta, _, _ = split_frontmatter(read_text(path))
        name = meta.get("name")
        description = meta.get("description", "")
        if not name:
            errors.append(f"skill missing name: {rel(path)}")
            continue
        if not SKILL_NAME_RE.match(name):
            errors.append(f"skill name is not lowercase hyphenated: {name} at {rel(path)}")
        if len(name) > 64:
            errors.append(f"skill name too long: {name}")
        if not description or len(description) > 1024:
            errors.append(f"skill description invalid length: {name}")
        if path.parent.name != name:
            errors.append(f"skill folder/name mismatch: {rel(path.parent)} has name {name}")
        if name in seen:
            errors.append(f"duplicate skill name: {name} at {seen[name]} and {rel(path)}")
        seen[name] = rel(path)
    if not seen:
        errors.append("no skills found")
    for path in SKILLS.rglob("*"):
        if path.is_file() and path.stat().st_size > 5 * 1024 * 1024:
            warnings.append(f"large skill asset: {rel(path)}")


def validate_agents(errors: list[str]) -> None:
    seen: dict[str, str] = {}
    for path, meta, body in agent_sources():
        name = meta.get("name", "")
        if not SKILL_NAME_RE.match(name):
            errors.append(f"agent name is not lowercase hyphenated: {name}")
        if name in seen:
            errors.append(f"duplicate agent name: {name} at {seen[name]} and {rel(path)}")
        seen[name] = rel(path)
        if not meta.get("description"):
            errors.append(f"agent missing description: {name}")
        if not body.strip():
            errors.append(f"agent missing body: {name}")
    if not seen:
        errors.append("no agents found")


def validate_adapters(errors: list[str]) -> None:
    for path in sorted((ADAPTERS / "codex" / "agents").glob("*.toml")):
        try:
            tomllib.loads(read_text(path))
        except Exception as exc:
            errors.append(f"invalid Codex TOML {rel(path)}: {exc}")
    for root in [ADAPTERS / "claude" / "agents", ADAPTERS / "opencode" / "agents"]:
        for path in sorted(root.glob("*.md")):
            meta, _, _ = split_frontmatter(read_text(path))
            if not meta.get("name"):
                errors.append(f"adapter missing name: {rel(path)}")
    cursor = ADAPTERS / "cursor" / "rules" / "shared-skills-and-agents.mdc"
    if not cursor.exists():
        errors.append("missing Cursor rules adapter")
    vscode = ADAPTERS / "vscode" / "copilot-instructions.md"
    if not vscode.exists():
        errors.append("missing VS Code copilot instructions adapter")


def validate_manifest(errors: list[str]) -> None:
    try:
        manifest = json.loads(read_text(STATE / "manifest.json"))
    except Exception as exc:
        errors.append(f"invalid manifest: {exc}")
        return
    hashes = manifest.get("repo_hashes", {})
    for path, expected in hashes.items():
        full = REPO / path
        if not full.exists():
            errors.append(f"manifest path missing: {path}")
        elif sha256_file(full) != expected:
            errors.append(f"manifest hash stale: {path}")


def doctor() -> None:
    print("Doctor: validating repository")
    validate()
    for path in [LOCAL_SKILLS, CLAUDE_SKILLS, OPENCODE_SKILLS, CODEX_AGENTS, CLAUDE_AGENTS, OPENCODE_AGENTS]:
        state = "exists" if path.exists() or path.is_symlink() else "missing"
        target = f" -> {os.readlink(path)}" if path.is_symlink() else ""
        print(f"{path}: {state}{target}")
    print("DOCTOR_OK")


def sync() -> None:
    import_native()
    render_adapters()
    validate()
    subprocess.run(["git", "status", "--short"], cwd=REPO, check=False)


def import_native() -> None:
    # Skills are symlinked in the install model, so native skill edits already
    # land in registry/skills. Agents are managed copies, so import only when
    # exactly one native adapter changed for a given canonical agent. If multiple
    # tools diverged, stop and write a conflict report.
    conflicts: list[str] = []
    updates = 0
    for path, meta, canonical_body in agent_sources():
        name = meta["name"]
        candidates: list[tuple[str, str, dict[str, str]]] = []
        codex_path = CODEX_AGENTS / f"{name}.toml"
        if codex_path.exists():
            try:
                data = tomllib.loads(read_text(codex_path))
                body = str(data.get("developer_instructions", "")).strip()
                meta_updates = {
                    "codex_model": str(data.get("model", meta.get("codex_model", ""))),
                    "codex_model_reasoning_effort": str(
                        data.get(
                            "model_reasoning_effort",
                            meta.get("codex_model_reasoning_effort", ""),
                        )
                    ),
                    "codex_sandbox_mode": str(
                        data.get("sandbox_mode", meta.get("codex_sandbox_mode", ""))
                    ),
                }
                if body and body != canonical_body.strip():
                    candidates.append(("codex", body, meta_updates))
            except Exception as exc:
                conflicts.append(f"## {name}\n\nCodex adapter parse failed: `{exc}`\n")

        for label, root in [("claude", CLAUDE_AGENTS), ("opencode", OPENCODE_AGENTS)]:
            native_path = root / f"{name}.md"
            if not native_path.exists():
                continue
            native_meta, _, body = split_frontmatter(read_text(native_path))
            if native_meta.get("name") and native_meta["name"] != name:
                conflicts.append(
                    f"## {name}\n\n{label} adapter name mismatch: `{native_meta['name']}`\n"
                )
                continue
            body = body.strip()
            if body and body != canonical_body.strip():
                candidates.append((label, body, {}))

        if not candidates:
            continue
        unique_bodies = {body for _, body, _ in candidates}
        if len(unique_bodies) > 1:
            labels = ", ".join(label for label, _, _ in candidates)
            conflicts.append(
                f"## {name}\n\nMultiple native adapters diverged: {labels}. "
                "Resolve manually in `registry/agents`.\n"
            )
            continue
        label, body, meta_updates = candidates[0]
        merged_meta = dict(meta)
        merged_meta.update({k: v for k, v in meta_updates.items() if v})
        write_text(path, dump_frontmatter(merged_meta) + "\n" + body.strip() + "\n")
        updates += 1
        print(f"IMPORTED {name} from {label}")

    if conflicts:
        report = REPORTS / "conflicts" / f"native-import-{now_stamp()}.md"
        write_text(report, "# Native Import Conflicts\n\n" + "\n".join(conflicts))
        raise SystemExit(f"native import conflicts written to {report}")
    if updates:
        write_catalog()
    print(f"IMPORT_NATIVE_OK updates={updates}")


def install_local(args: argparse.Namespace) -> None:
    mappings = [
        ("skill symlink", SKILLS, LOCAL_SKILLS, True),
        ("Claude skill symlink", SKILLS, CLAUDE_SKILLS, True),
        ("OpenCode skill symlink", SKILLS, OPENCODE_SKILLS, True),
        ("Codex agents", ADAPTERS / "codex" / "agents", CODEX_AGENTS, False),
        ("Claude agents", ADAPTERS / "claude" / "agents", CLAUDE_AGENTS, False),
        ("OpenCode agents", ADAPTERS / "opencode" / "agents", OPENCODE_AGENTS, False),
    ]
    if args.check_symlinks:
        for label, src, dst, symlink in mappings:
            if symlink:
                print(f"{label}: source={src} target={dst} source_exists={src.exists()}")
        return
    if args.mode == "dry-run":
        for label, src, dst, symlink in mappings:
            method = "symlink" if symlink else "managed copy"
            print(f"{label}: {method} {src} -> {dst}")
        return
    backup_root = Path.home() / "backups" / "my-skills-and-agents" / f"install-{now_stamp()}"
    backup_root.mkdir(parents=True, exist_ok=True)
    for _, src, dst, symlink in mappings:
        if not src.exists():
            print(f"SKIP missing source {src}")
            continue
        if dst.exists() or dst.is_symlink():
            backup_dst = backup_root / str(dst).lstrip("/")
            backup_dst.parent.mkdir(parents=True, exist_ok=True)
            if dst.is_symlink():
                backup_dst.write_text(os.readlink(dst), encoding="utf-8")
                dst.unlink()
            elif dst.is_dir():
                shutil.copytree(dst, backup_dst, symlinks=True)
                shutil.rmtree(dst)
            else:
                shutil.copy2(dst, backup_dst)
                dst.unlink()
        dst.parent.mkdir(parents=True, exist_ok=True)
        if symlink:
            dst.symlink_to(src, target_is_directory=True)
        else:
            shutil.copytree(src, dst, symlinks=True)
    print(f"INSTALL_OK backup={backup_root}")


def install_project(project: Path) -> None:
    if not project.exists() or not project.is_dir():
        raise SystemExit(f"project directory does not exist: {project}")
    backup_root = project / ".ai-adapter-backup" / now_stamp()
    mappings = [
        (ADAPTERS / "cursor" / "rules", project / ".cursor" / "rules"),
        (ADAPTERS / "vscode" / "copilot-instructions.md", project / ".github" / "copilot-instructions.md"),
        (ADAPTERS / "vscode" / "instructions", project / ".github" / "instructions"),
    ]
    for src, dst in mappings:
        if dst.exists() or dst.is_symlink():
            backup_dst = backup_root / str(dst.relative_to(project))
            backup_dst.parent.mkdir(parents=True, exist_ok=True)
            if dst.is_dir():
                shutil.copytree(dst, backup_dst, symlinks=True)
                shutil.rmtree(dst)
            else:
                shutil.copy2(dst, backup_dst)
                dst.unlink()
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            shutil.copytree(src, dst, symlinks=True)
        else:
            shutil.copy2(src, dst)
    ag = project / "AGENTS.md"
    if not ag.exists():
        write_text(
            ag,
            "# Agent Instructions\n\n"
            "This project can use shared personal AI instructions from:\n\n"
            f"`{REPO}`\n",
        )
    print(f"PROJECT_INSTALL_OK backup={backup_root}")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("migrate-local")
    sub.add_parser("render-adapters")
    sub.add_parser("validate")
    sub.add_parser("doctor")
    sub.add_parser("sync")
    sub.add_parser("import-native")
    install = sub.add_parser("install-local")
    install.add_argument("mode", nargs="?", choices=["apply", "dry-run"], default="dry-run")
    install.add_argument("--check-symlinks", action="store_true")
    project = sub.add_parser("install-project-adapters")
    project.add_argument("project")
    args = parser.parse_args()

    if args.cmd == "migrate-local":
        migrate_local()
    elif args.cmd == "render-adapters":
        render_adapters()
    elif args.cmd == "validate":
        validate()
    elif args.cmd == "doctor":
        doctor()
    elif args.cmd == "sync":
        sync()
    elif args.cmd == "import-native":
        import_native()
    elif args.cmd == "install-local":
        install_local(args)
    elif args.cmd == "install-project-adapters":
        install_project(Path(args.project).resolve())


if __name__ == "__main__":
    main()
