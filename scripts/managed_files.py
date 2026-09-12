#!/usr/bin/env python3
"""Protect explicitly selected files. Selection and plugin management belong to the agent."""

from __future__ import annotations

import argparse
from collections.abc import MutableMapping
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import sys
import tempfile
import uuid


def is_link(path: Path) -> bool:
    # Windows junctions/reparse points also redirect paths outside the selected tree.
    return path.is_symlink() or bool(
        os.name == "nt" and path.exists() and path.lstat().st_file_attributes & 0x400
    )


def digest(path: Path) -> str | None:
    if is_link(path):
        raise ValueError(f"Symbolic link requires manual handling: {path}")
    if not path.exists():
        return None
    entries = [path] if path.is_file() else [path, *sorted(path.rglob("*"))]
    result = hashlib.sha256()
    for entry in entries:
        if is_link(entry) or not (entry.is_file() or entry.is_dir()):
            raise ValueError(f"Only regular files/directories are supported: {entry}")
        name = "." if entry == path else entry.relative_to(path).as_posix()
        result.update(name.encode() + b"\0")
        if entry.is_file():
            result.update(b"file\0" + entry.read_bytes())
            result.update(b"executable" if entry.stat().st_mode & 0o111 else b"regular")
        else:
            result.update(b"directory")
    return result.hexdigest()


def atomic_write(path: Path, data: bytes, mode: int = 0o600) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".agent-config-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, mode)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def value_hash(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, default=str).encode()).hexdigest()


def pointer(parts) -> str:
    return "/" + "/".join(p.replace("~", "~0").replace("/", "~1") for p in parts)


def merge_values(current, patch, owned, replace, parts=()):
    """Fill missing values; update unchanged managed values; preserve user overrides."""
    kept, fields = [], dict(owned)
    for key, value in patch.items():
        position = pointer((*parts, key))
        if key in current and isinstance(current[key], MutableMapping) and isinstance(value, MutableMapping):
            nested_kept, fields = merge_values(
                current[key], value, fields, replace, (*parts, key)
            )
            kept.extend(nested_kept)
        elif key not in current and isinstance(value, MutableMapping):
            current[key] = {}
            nested_kept, fields = merge_values(current[key], value, fields, replace, (*parts, key))
            kept.extend(nested_kept)
        elif key not in current:
            current[key] = value
            fields[position] = value_hash(value)
        elif position in replace:
            current[key] = value
            fields[position] = value_hash(value)
        elif (position.startswith("/hooks/") or position in ("/permissions/allow", "/permissions/deny", "/permissions/ask")) and isinstance(current[key], list) and isinstance(value, list):
            # Settings hooks/allow lists are additive; external entries retain their order.
            combined = list(current[key])
            for entry in value:
                if entry not in combined:
                    combined.append(entry)
            current[key] = combined
            fields[position] = value_hash(combined)
        elif owned.get(position) == value_hash(current[key]):
            current[key] = value
            fields[position] = value_hash(value)
        elif current[key] != value:
            kept.append(position)
    return kept, fields


class ManagedFiles:
    def __init__(self, root: Path, dry_run=False):
        self.root = root.expanduser().resolve()
        self.dry_run = dry_run
        self.metadata = self.path("agent-config")
        self.receipt = self.path("agent-config/files.json")
        self.state = {"schema": 1, "files": {}}

    def path(self, relative: str) -> Path:
        name = PurePosixPath(relative)
        if name.is_absolute() or not name.parts or name.as_posix() != relative or any(p in (".", "..") for p in name.parts):
            raise ValueError(f"Expected a relative path inside the agent home: {relative}")
        if "\\" in relative or ":" in relative:
            raise ValueError(f"Use a portable relative path: {relative}")
        target = self.root
        for part in name.parts:
            target = target / part
            if is_link(target):
                raise ValueError(f"Symbolic link requires manual handling: {target}")
        return target

    def load(self):
        if self.receipt.exists():
            self.state = json.loads(self.receipt.read_text(encoding="utf-8"))
            if self.state.get("schema") != 1 or not isinstance(self.state.get("files"), dict):
                raise ValueError("Unsupported installation record; preserve it and use a compatible helper")

    def save(self):
        atomic_write(self.receipt, (json.dumps(self.state, indent=2) + "\n").encode())

    @contextmanager
    def locked(self):
        if self.dry_run:
            self.load()
            if self.state.get("pending"):
                raise ValueError("Unfinished file operation: inspect files.json before previewing")
            yield
            return
        self.metadata.mkdir(parents=True, exist_ok=True, mode=0o700)
        lock = self.path("agent-config/files.lock")
        with lock.open("a+b") as stream:
            if os.name == "nt":
                import msvcrt
                if stream.tell() == 0:
                    stream.write(b"0")
                    stream.flush()
                stream.seek(0)
                msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            self.load()
            self.recover()
            yield

    def recover(self):
        pending = self.state.get("pending")
        if not pending:
            return
        target = self.path(pending["target"])
        actual = digest(target)
        if actual == pending["after"]:
            record = pending["record"]
            if record is None:
                self.state["files"].pop(pending["target"], None)
            else:
                record["backup"] = pending["backup"]
                self.state["files"][pending["target"]] = record
        elif actual == pending["before"]:
            pass
        elif actual is None and pending["backup"]:
            backup = self.path(pending["backup"])
            if digest(backup) != pending["before"]:
                raise ValueError("Interrupted operation has an unexpected backup; inspect files.json")
            os.replace(backup, target)
        else:
            raise ValueError("Interrupted operation conflicts with current files; inspect files.json")
        self.state.pop("pending")
        self.save()

    def commit(self, relative, incoming, record, before):
        target = self.path(relative)
        after = digest(incoming) if incoming else None
        if self.dry_run:
            return {"status": "preview", "target": relative, "before": before, "after": after}
        if digest(target) != before:
            raise ValueError(f"Concurrent edit detected: {target}")
        backup = None
        if before is not None:
            backup = f"agent-config/backups/{uuid.uuid4().hex}/{target.name}"
        self.state["pending"] = {
            "target": relative, "before": before, "after": after,
            "backup": backup, "record": record,
        }
        self.save()
        target.parent.mkdir(parents=True, exist_ok=True)
        if backup:
            destination = self.path(backup)
            destination.parent.mkdir(parents=True, mode=0o700)
            if target.is_dir() or incoming is None:
                os.replace(target, destination)
            else:
                shutil.copy2(target, destination)
        try:
            if incoming:
                if incoming.is_dir():
                    os.replace(incoming, target)
                else:
                    mode = incoming.stat().st_mode & 0o777
                    atomic_write(target, incoming.read_bytes(), mode)
        except BaseException:
            if backup and not target.exists():
                os.replace(self.path(backup), target)
            raise
        if digest(target) != after:
            raise ValueError(f"Post-write verification failed; backup retained: {target}")
        if record is None:
            self.state["files"].pop(relative, None)
        else:
            record["backup"] = backup
            self.state["files"][relative] = record
        self.state.pop("pending")
        self.save()
        return {"status": "removed" if incoming is None else "installed", "target": relative, "backup": backup}

    def install(self, source, relative, item, origin):
        target = self.path(relative)
        if relative == "lessons.md":
            raise ValueError("Use seed-lessons to create a blank log; existing lessons are never replaced")
        if relative == "agent-config" or relative.startswith("agent-config/"):
            raise ValueError("Installation metadata is not an installation target")
        if relative in ("config.toml", "settings.json"):
            raise ValueError("Use merge for configuration files")
        if relative == "skills" or (relative.startswith("skills/") and len(PurePosixPath(relative).parts) != 2):
            raise ValueError("Install each complete skill at skills/<name>")
        for existing in self.state["files"]:
            if relative.startswith(existing + "/") or existing.startswith(relative + "/"):
                raise ValueError(f"Target overlaps an existing managed copy: {existing}")
        source = source.absolute()
        incoming_hash = digest(source)
        if incoming_hash is None:
            raise ValueError(f"Missing source: {source}")
        if relative.startswith("skills/") and not (source / "SKILL.md").is_file():
            raise ValueError("Install a complete skill directory containing SKILL.md")
        before = digest(target)
        previous = self.state["files"].get(relative)
        if before == incoming_hash:
            managed = previous and previous["hash"] == before
            return {"status": "already-managed" if managed else "provided-externally", "target": relative}
        if before is not None and (not previous or previous["hash"] != before):
            raise ValueError(f"Existing or locally modified content preserved: {target}")
        record = {"items": [item], "kind": "copy", "hash": incoming_hash,
                  "origin": origin, "created": previous.get("created", True) if previous else True}
        if self.dry_run:
            return self.commit(relative, source, record, before)
        target.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="stage-", dir=self.metadata) as temporary:
            stage = Path(temporary) / source.name
            if source.is_dir():
                shutil.copytree(source, stage)
            else:
                shutil.copy2(source, stage)
            if digest(stage) != incoming_hash:
                raise ValueError("Source changed while staging")
            return self.commit(relative, stage, record, before)

    def merge(self, patch_file, relative, item, replace, remove, origin):
        if relative not in ("config.toml", "settings.json"):
            raise ValueError("Merge only config.toml or settings.json; other files use protected copy")
        target = self.path(relative)
        before = digest(target)
        original = target.read_text(encoding="utf-8") if target.exists() else ""
        patch_text = patch_file.read_text(encoding="utf-8")
        if relative.endswith(".toml"):
            try:
                import tomlkit
            except ImportError:
                raise ValueError("TOML editing needs tomlkit==0.13.3; see scripts/README.md") from None
            document = tomlkit.parse(original)
            patch = tomlkit.parse(patch_text)
            serialize = tomlkit.dumps
        else:
            document = json.loads(original or "{}")
            patch = json.loads(patch_text)
            serialize = lambda data: json.dumps(data, indent=2) + "\n"
        if not isinstance(document, MutableMapping) or not isinstance(patch, MutableMapping):
            raise ValueError("Config and patch must be objects")
        previous = self.state["files"].get(relative, {})
        kept, fields = merge_values(document, patch, previous.get("fields", {}), set(replace))
        for key in remove:
            if key != "model_instructions_file" or document.get(key) != "lessons.md":
                raise ValueError("Automatic removal is limited to model_instructions_file = 'lessons.md'")
            del document[key]
            fields.pop("/" + key, None)
        output = serialize(document)
        if output == original:
            return {"status": "unchanged", "target": relative, "preserved": kept}
        record = {"items": sorted(set(previous.get("items", []) + [item])), "kind": "merge",
                  "fields": fields, "created": previous.get("created", before is None), "origin": origin}
        # Staging is outside the target in dry-run mode.
        with tempfile.TemporaryDirectory(prefix="agent-config-merge-") as temporary:
            staged = Path(temporary) / target.name
            staged.write_text(output, encoding="utf-8")
            staged.chmod(target.stat().st_mode & 0o777 if target.exists() else 0o600)
            record["hash"] = digest(staged)
            result = self.commit(relative, staged, record, before)
        return {**result, "preserved": kept}

    def remove(self, relative):
        target = self.path(relative)
        previous = self.state["files"].get(relative)
        if not previous or previous["kind"] != "copy" or not previous["created"]:
            raise ValueError("Only an explicitly selected, helper-created copy can be removed; merge configs manually")
        before = digest(target)
        if before != previous["hash"]:
            raise ValueError("Local modification or missing target: preserve and inspect before removal")
        return self.commit(relative, None, None, before)

    def seed_lessons(self):
        target = self.path("lessons.md")
        if target.exists():
            return {"status": "preserved", "target": "lessons.md"}
        if not self.dry_run:
            template = Path(__file__).resolve().parents[1] / "platforms/global-lessons.md"
            data = template.read_bytes()
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            except FileExistsError:
                return {"status": "preserved", "target": "lessons.md"}
            with os.fdopen(fd, "wb") as stream:
                stream.write(data)
                stream.flush()
                os.fsync(stream.fileno())
        return {"status": "preview" if self.dry_run else "seeded", "target": "lessons.md"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="Explicit Claude or Codex config directory")
    parser.add_argument("--dry-run", action="store_true")
    commands = parser.add_subparsers(dest="action", required=True)
    for command in ("install", "merge"):
        sub = commands.add_parser(command)
        sub.add_argument("source", type=Path)
        sub.add_argument("target", help="Relative path inside the config directory")
        sub.add_argument("--item", required=True, help="Stable catalogue ID, never the displayed number")
        sub.add_argument("--origin", default="local-checkout", help="Repository and resolved source revision")
        if command == "merge":
            sub.add_argument("--replace", action="append", default=[], help="Explicitly replace this JSON pointer")
            sub.add_argument("--remove", action="append", default=[], help="Remove the obsolete lessons override")
    commands.add_parser("remove").add_argument("target")
    commands.add_parser("seed-lessons")
    commands.add_parser("status")
    args = parser.parse_args()
    manager = ManagedFiles(args.root, args.dry_run)
    if args.action == "status":
        manager.load()
        print(json.dumps({"pending": manager.state.get("pending"), "files": [
            {"target": name, "items": record["items"], "matches": digest(manager.path(name)) == record["hash"]}
            for name, record in manager.state["files"].items()
        ]}, indent=2))
        return
    with manager.locked():
        if args.action == "install":
            result = manager.install(args.source, args.target, args.item, args.origin)
        elif args.action == "merge":
            result = manager.merge(args.source, args.target, args.item, args.replace, args.remove, args.origin)
        elif args.action == "remove":
            result = manager.remove(args.target)
        else:
            result = manager.seed_lessons()
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError, KeyError) as error:
        print(f"Preserved existing files: {error}", file=sys.stderr)
        sys.exit(1)
