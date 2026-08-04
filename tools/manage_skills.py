#!/usr/bin/env python3
"""Validate, list, and safely install AI Workflow skill profiles."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = (ROOT / ".agents" / "skills").resolve()
PROFILES = (ROOT / "profiles").resolve()
REGISTRY = (ROOT / "registry").resolve()
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
PROFILE_KEYS = {"name", "description", "extends", "skills"}
SKILL_STATUSES = {"candidate", "quarantined", "draft", "trial", "stable", "deprecated"}


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path.name}: root must be an object")
    return value


def contained_child(parent: Path, child: Path) -> bool:
    try:
        child.relative_to(parent)
        return child.parent == parent
    except ValueError:
        return False


def profile_data(name: str) -> dict:
    if not isinstance(name, str) or not NAME_RE.fullmatch(name):
        raise ValueError(f"Invalid profile name: {name!r}")
    path = (PROFILES / f"{name}.json").resolve()
    if not contained_child(PROFILES, path) or not path.is_file():
        raise ValueError(f"Unknown profile: {name}")
    data = load_json(path)
    extra = set(data) - PROFILE_KEYS
    if extra:
        raise ValueError(f"{path.name}: unsupported keys {sorted(extra)}")
    if data.get("name") != name:
        raise ValueError(f"{path.name}: name must match filename")
    if not isinstance(data.get("description"), str) or not data["description"].strip():
        raise ValueError(f"{path.name}: description must be a non-empty string")
    for field in ("extends", "skills"):
        value = data.get(field, [])
        if not isinstance(value, list) or any(not isinstance(item, str) or not NAME_RE.fullmatch(item) for item in value):
            raise ValueError(f"{path.name}: {field} must be a list of kebab-case names")
        if len(value) != len(set(value)):
            raise ValueError(f"{path.name}: {field} contains duplicates")
    return data


def resolve_profile(name: str, stack: tuple[str, ...] = ()) -> list[str]:
    if name in stack:
        raise ValueError(f"Profile cycle: {' -> '.join((*stack, name))}")
    data = profile_data(name)
    result: list[str] = []
    for parent in data.get("extends", []):
        for skill in resolve_profile(parent, (*stack, name)):
            if skill not in result:
                result.append(skill)
    for skill in data.get("skills", []):
        if skill not in result:
            result.append(skill)
    return result


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing opening frontmatter delimiter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("missing closing frontmatter delimiter") from exc
    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        if key in values:
            raise ValueError(f"duplicate frontmatter key: {key}")
        values[key] = value.strip()
    return values


def has_links(path: Path) -> bool:
    return path.is_symlink() or any(item.is_symlink() for item in path.rglob("*"))


def validate_openai_yaml(path: Path, skill: str) -> list[str]:
    if not path.is_file():
        return [f"{skill}: missing agents/openai.yaml"]
    text = path.read_text(encoding="utf-8")
    errors = []
    for field in ("display_name:", "short_description:", "default_prompt:"):
        if field not in text:
            errors.append(f"{skill}: openai.yaml missing {field[:-1]}")
    if f"${skill}" not in text:
        errors.append(f"{skill}: openai.yaml default_prompt must mention ${skill}")
    policy = re.search(r"allow_implicit_invocation:\s*(\S+)", text)
    if policy and policy.group(1) not in {"true", "false"}:
        errors.append(f"{skill}: allow_implicit_invocation must be true or false")
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    skill_names = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    for name in sorted(skill_names):
        folder = (SKILLS / name).resolve()
        skill_md = folder / "SKILL.md"
        if not NAME_RE.fullmatch(name) or not contained_child(SKILLS, folder):
            errors.append(f"{name}: invalid or uncontained skill folder")
        if has_links(folder):
            errors.append(f"{name}: symlinks/reparse-like links are not allowed")
        if not skill_md.is_file():
            errors.append(f"{name}: missing SKILL.md")
            continue
        text = skill_md.read_text(encoding="utf-8")
        if len(text.splitlines()) > 500:
            errors.append(f"{name}: SKILL.md exceeds 500 lines")
        if "TODO" in text:
            errors.append(f"{name}: unresolved TODO")
        try:
            meta = parse_frontmatter(skill_md)
            if set(meta) != {"name", "description"}:
                errors.append(f"{name}: frontmatter keys must be name and description only")
            if meta.get("name") != name:
                errors.append(f"{name}: frontmatter name does not match folder")
            description = meta.get("description", "").strip('"\'')
            if not description or len(description) > 1024:
                errors.append(f"{name}: description must contain 1-1024 characters")
        except ValueError as exc:
            errors.append(f"{name}: {exc}")
        errors.extend(validate_openai_yaml(folder / "agents" / "openai.yaml", name))
        for source in folder.rglob("*.md"):
            for raw in LINK_RE.findall(source.read_text(encoding="utf-8")):
                target = raw.split("#", 1)[0].strip().strip("<>")
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                resolved = (source.parent / target).resolve()
                try:
                    resolved.relative_to(folder)
                except ValueError:
                    errors.append(f"{source.relative_to(ROOT)}: link escapes skill folder: {raw}")
                    continue
                if not resolved.exists():
                    errors.append(f"{source.relative_to(ROOT)}: broken link {raw}")

    for path in sorted(PROFILES.glob("*.json")):
        try:
            skills = resolve_profile(path.stem)
            missing = [name for name in skills if name not in skill_names]
            if missing:
                errors.append(f"{path.name}: unknown skills {', '.join(missing)}")
            if len(skills) > 5:
                errors.append(f"{path.name}: resolves to {len(skills)} skills; maximum is 5")
        except (ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{path.name}: {exc}")

    registry_files: dict[str, dict] = {}
    for path in REGISTRY.glob("*.json"):
        try:
            registry_files[path.name] = load_json(path)
        except (ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
    skill_registry = registry_files.get("skills.json", {}).get("skills", [])
    if not isinstance(skill_registry, list) or any(not isinstance(item, dict) for item in skill_registry):
        errors.append("registry/skills.json: skills must be a list of objects")
    else:
        names = [item.get("name") for item in skill_registry]
        if len(names) != len(set(names)):
            errors.append("registry/skills.json: duplicate skill name")
        if set(names) != skill_names:
            errors.append(f"registry/skills.json mismatch; missing={sorted(skill_names - set(names))}, extra={sorted(set(names) - skill_names)}")
        profile_membership = {skill: [] for skill in skill_names}
        for profile_path in PROFILES.glob("*.json"):
            for skill in resolve_profile(profile_path.stem):
                profile_membership[skill].append(profile_path.stem)
        source_ids = {item.get("id") for item in registry_files.get("sources.json", {}).get("sources", [])}
        for item in skill_registry:
            status = item.get("status")
            if not isinstance(status, str) or not (status in SKILL_STATUSES or status.startswith("stable:")):
                errors.append(f"registry/skills.json: invalid status for {item.get('name')}")
            if sorted(item.get("profile", [])) != sorted(profile_membership.get(item.get("name"), [])):
                errors.append(f"registry/skills.json: profile drift for {item.get('name')}")
            if item.get("source") != "local" and item.get("source") not in source_ids:
                errors.append(f"registry/skills.json: unknown source for {item.get('name')}")
    for item in registry_files.get("sources.json", {}).get("sources", []):
        revision = item.get("revision")
        if revision is not None and not SHA_RE.fullmatch(str(revision)):
            errors.append(f"registry/sources.json: invalid revision for {item.get('id')}")
    return errors


def tree_digest(path: Path) -> str:
    digest = hashlib.sha256()
    for file in sorted(item for item in path.rglob("*") if item.is_file()):
        digest.update(file.relative_to(path).as_posix().encode())
        digest.update(file.read_bytes())
    return digest.hexdigest()


def destination(runtime: str, scope: str, target: Path) -> Path:
    if scope == "workspace":
        return target / (".claude/skills" if runtime == "claude" else ".agents/skills")
    home = Path.home()
    if runtime == "claude":
        return home / ".claude" / "skills"
    if runtime == "antigravity-ide":
        return home / ".gemini" / "config" / "skills"
    return home / ".agents" / "skills"


def registered_statuses() -> dict[str, str]:
    data = load_json(REGISTRY / "skills.json")
    return {item["name"]: item["status"] for item in data["skills"]}


def install(args: argparse.Namespace) -> int:
    errors = validate()
    if errors:
        raise ValueError("Repository validation failed; run 'manage_skills.py validate'")
    if args.scope == "user" and args.target:
        raise ValueError("--target is only valid with --scope workspace")
    selected = resolve_profile(args.profile)
    statuses = registered_statuses()
    if args.scope == "user" and not args.allow_draft:
        blocked = [name for name in selected if statuses.get(name) not in {"trial", "stable", f"stable:{args.runtime}"}]
        if blocked:
            raise ValueError(f"Global install blocked for non-graduated skills: {', '.join(blocked)}; review and pass --allow-draft to acknowledge")
    target = Path(args.target).resolve() if args.target else Path.cwd().resolve()
    dest_root = destination(args.runtime, args.scope, target)
    print(f"Profile: {args.profile} ({', '.join(selected)})")
    print(f"Destination: {dest_root}")

    plan: list[tuple[str, Path, Path, str]] = []
    conflicts: list[str] = []
    for name in selected:
        source = (SKILLS / name).resolve()
        if not contained_child(SKILLS, source) or not (source / "SKILL.md").is_file() or has_links(source):
            raise ValueError(f"Unsafe or invalid skill source: {name}")
        dest = dest_root / name
        if source == dest.resolve():
            state = "active"
        elif dest.exists():
            state = "identical" if dest.is_dir() and not has_links(dest) and tree_digest(source) == tree_digest(dest) else "conflict"
        else:
            state = "copy"
        plan.append((name, source, dest, state))
        if state == "conflict":
            conflicts.append(name)
    if conflicts:
        raise ValueError(f"Destination differs; refusing partial install or overwrite: {', '.join(conflicts)}")
    for name, _, _, state in plan:
        label = {"active": "ACTIVE", "identical": "SKIP", "copy": "WOULD COPY" if args.dry_run else "COPY"}[state]
        print(f"{label:<10} {name}")
    if args.dry_run or not any(state == "copy" for *_, state in plan):
        return 0

    stage_root = dest_root.parent / f".{dest_root.name}.aiwf-stage-{uuid.uuid4().hex}"
    created: list[Path] = []
    try:
        stage_root.mkdir(parents=True, exist_ok=False)
        for name, source, _, state in plan:
            if state != "copy":
                continue
            staged = stage_root / name
            shutil.copytree(source, staged)
            if tree_digest(source) != tree_digest(staged):
                raise RuntimeError(f"Staging digest mismatch: {name}")
        dest_root.mkdir(parents=True, exist_ok=True)
        for name, _, dest, state in plan:
            if state != "copy":
                continue
            if dest.exists():
                raise RuntimeError(f"Destination appeared during install: {dest}")
            (stage_root / name).replace(dest)
            created.append(dest)
    except Exception:
        for path in reversed(created):
            if path.exists():
                shutil.rmtree(path)
        raise
    finally:
        if stage_root.exists():
            shutil.rmtree(stage_root)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="List profiles and resolved skills")
    sub.add_parser("validate", help="Validate skills, profiles, links, metadata, and registries")
    installer = sub.add_parser("install", help="Install a profile using preflight, staging, and no overwrite")
    installer.add_argument("--runtime", choices=("codex", "claude", "antigravity-ide"), required=True)
    installer.add_argument("--scope", choices=("workspace", "user"), required=True)
    installer.add_argument("--profile", required=True)
    installer.add_argument("--target", help="Workspace root; defaults to the current directory")
    installer.add_argument("--dry-run", action="store_true")
    installer.add_argument("--allow-draft", action="store_true", help="Acknowledge non-graduated skills for user/global install")
    args = parser.parse_args()
    try:
        if args.command == "list":
            for path in sorted(PROFILES.glob("*.json")):
                print(f"{path.stem}: {', '.join(resolve_profile(path.stem))}")
            return 0
        if args.command == "validate":
            errors = validate()
            if errors:
                print("Validation failed:")
                for error in errors:
                    print(f"- {error}")
                return 1
            print("Validation passed.")
            return 0
        return install(args)
    except (ValueError, RuntimeError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
