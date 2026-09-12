#!/usr/bin/env python3
"""Adapt a staged ResearchStudio Idea snapshot for the selected agent skill directory."""
import argparse
from pathlib import Path
import re
import sys


def adapt(stage: Path, agent_root: Path, agent: str):
    files = {
        "paper": stage / "paper_search/SKILL.md",
        "scoop": stage / "scoop_check/SKILL.md",
        "fetch": stage / "scoop_check/scripts/fetch_paper.sh",
    }
    required = [stage / "idea_spark/SKILL.md", stage / "paper_search/scripts/search_papers.py", *files.values()]
    for path in required:
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"Missing regular source file: {path}")
    if any(p.is_symlink() for p in stage.rglob("*")):
        raise ValueError("Staged source contains links")
    source = {name: path.read_text(encoding="utf-8") for name, path in files.items()}
    root = (agent_root.expanduser().resolve() / "skills").as_posix()
    if any(c in root for c in "\n\r"):
        raise ValueError("Target directory cannot contain line breaks")
    # The upstream runbook embeds these paths inside Bash double quotes.
    root = re.sub(r'([\\"$`])', r'\\\1', root)
    search = root + "/paper_search/scripts/search_papers.py"
    fetch = root + "/scoop_check/scripts/fetch_paper.sh"
    replacements = {
        "paper": [
            ("${CLAUDE_PROJECT_DIR}/skills/paper_search/scripts/search_papers.py", search),
            ("${CLAUDE_PROJECT_DIR}/allinone.md", "${PWD}/allinone.md"),
        ],
        "scoop": [
            (".claude/skills/", f"the installed {agent.title()} skills directory"),
            ("${CLAUDE_PROJECT_DIR}", "${PWD}"),
            ("Do **not** use `AskUserQuestion` or pause for confirmation at any point", "Do **not** ask a blocking clarification question or pause for confirmation at any point"),
            ("use `TaskCreate` to register all seven steps as tasks up front", "record all seven steps using the available planning tool or a concise written plan"),
            ("handing the PDF URL to `WebFetch` directly", "asking web browsing to summarize the PDF directly"),
            ("Use `WebFetch` first only to locate the PDF URL", "Use web browsing only to locate the PDF URL"),
            ("Use the `Read` tool on the printed `.txt` path.", "Read the printed `.txt` path with the available local filesystem tools."),
            ("try `WebFetch` on the abstract / HTML version", "use web browsing on the abstract / HTML version"),
            ('scripts/fetch_paper.sh "<PDF_URL>" "<pdf_name>"', f'bash "{fetch}" "<PDF_URL>" "<pdf_name>"'),
        ],
        "fetch": [
            (': "${CLAUDE_PROJECT_DIR:?CLAUDE_PROJECT_DIR must be set}"', 'PROJECT_DIR="${CODEX_PROJECT_DIR:-${CLAUDE_PROJECT_DIR:-$PWD}}"'),
            ("${CLAUDE_PROJECT_DIR}", "${PROJECT_DIR}"),
        ],
    }
    if agent == "claude":
        replacements["scoop"] = [
            pair for pair in replacements["scoop"]
            if pair[0] in ("${CLAUDE_PROJECT_DIR}", 'scripts/fetch_paper.sh "<PDF_URL>" "<pdf_name>"')
        ]
    # Check all anchors before writing any file; an upstream change needs inspection.
    for name, pairs in replacements.items():
        for old, new in pairs:
            if old not in source[name]:
                raise ValueError(f"Upstream adapter anchor changed in {files[name]}: {old}")
            source[name] = source[name].replace(old, new)
    if agent == "codex" and re.search(r"TaskCreate|AskUserQuestion|WebFetch|`Read` tool", source["scoop"]):
        raise ValueError("Unadapted Claude tool references remain")
    for name, content in source.items():
        files[name].write_text(content, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", type=Path, required=True, help="Temporary directory containing only the three Idea skills")
    parser.add_argument("--agent", choices=("claude", "codex"), required=True)
    parser.add_argument("--root", type=Path, required=True, help="Final agent home; only embedded in staged instructions")
    args = parser.parse_args()
    try:
        adapt(args.stage, args.root, args.agent)
        print("Staged Idea instructions adapted; no runtime dependencies installed.")
    except (ValueError, OSError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
