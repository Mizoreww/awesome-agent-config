#!/usr/bin/env python3
"""Stage lieflat-charts root files and the original directory allowlist."""
import argparse
from pathlib import Path
import shutil

from managed_files import digest


def stage(source, output):
    if output.exists():
        raise ValueError("Use a fresh staging directory")
    for name in ("SKILL.md", "LICENSE"):
        if not (source / name).is_file():
            raise ValueError(f"Missing {name}")
    selected = []
    for entry in source.iterdir():
        if entry.name == ".git":
            continue
        if entry.is_symlink():
            raise ValueError(f"Unexpected source link: {entry}")
        if entry.is_file() or entry.name in ("templates", "examples", "scripts", "agents"):
            digest(entry)
            selected.append(entry)
    output.mkdir(parents=True)
    for entry in selected:
        if entry.is_dir():
            shutil.copytree(entry, output / entry.name)
        else:
            shutil.copy2(entry, output / entry.name)
    print("Staged source and license; preview media under docs/ excluded.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    stage(args.source, args.output)
