#!/usr/bin/env python3
"""Adapt a staged ResearchStudio snapshot for the selected agent skill directory."""
import argparse
import json
from pathlib import Path
import re
import shlex
import sys

from managed_files import digest


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
        replacements["fetch"][0] = (
            ': "${CLAUDE_PROJECT_DIR:?CLAUDE_PROJECT_DIR must be set}"',
            'PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$PWD}"',
        )
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


def adapt_reel(stage: Path, agent_root: Path):
    names = ("paper2assets", "paper2poster", "paper2video", "paper2blog", "paper2reel")
    root = agent_root.expanduser().resolve() / "skills"
    if any(c in root.as_posix() for c in "\n\r"):
        raise ValueError("Target directory cannot contain line breaks")
    digest(stage)
    for name in names:
        if not (stage / name / "SKILL.md").is_file():
            raise ValueError(f"Missing complete Reel member: {name}")
    pattern = re.compile(
        r"(?<![\w./])(?:~/\.claude/|\.claude/|<config>/)?skills/"
        r"(?P<name>paper2assets|paper2poster|paper2video|paper2blog|paper2reel)"
        r"(?P<suffix>(?:/[\w.*-]+)*/?)"
    )

    def absolute_path(match):
        relative = match["name"] + match["suffix"]
        # Template globs in prose name a directory, not a required individual file.
        reference = relative.rsplit("/", 1)[0] if "*" in relative else relative
        if not (stage / reference).exists():
            raise ValueError(f"Upstream Reel reference is missing: {relative}")
        return shlex.quote((root / relative).as_posix())

    updates = {}
    for path in sorted(stage.rglob("*.md")):
        original = path.read_text(encoding="utf-8")
        content, count = pattern.subn(absolute_path, original)
        if path.parent == stage / "paper2video" and path.name == "SKILL.md":
            anchor = "Run Paper2Video workflow commands from `ResearchStudio-Reel/` unless noted."
            if anchor not in content:
                raise ValueError("Upstream Reel working-directory instruction changed")
            content = content.replace(anchor, "Use the absolute skill paths below. Keep outputs in the user's project directory.")
        if path.name == "SKILL.md" and path.parent.name in names:
            if count == 0:
                raise ValueError(f"Upstream Reel path anchors changed: {path}")
            boundary = content.find("\n---", 4)
            if not content.startswith("---\n") or boundary < 0:
                raise ValueError(f"Missing skill frontmatter: {path}")
            boundary += len("\n---")
            note = (
                "\n\n## Codex runtime paths\n\n"
                "Use the available Codex tools for Claude tool names below. "
                "Resolve remaining relative script paths against the directory containing this SKILL.md, "
                "and use absolute project output paths. Reuse existing selected skill providers; "
                "additional skill dependencies belong in the actual Codex home. "
                "Runtime dependency setup remains a first-use step.\n"
            )
            content = content[:boundary] + note + content[boundary:]
        if content != original:
            updates[path] = content
    # This executable only embeds a repair command; keep that diagnostic consistent too.
    diagnostics = stage / "paper2poster/scripts/utils/deliverables.py"
    source = diagnostics.read_text(encoding="utf-8")
    anchor = ('"Run Step 10:  python ~/.claude/skills/paper2poster/scripts/"\n'
              '        "render_poster.py <outdir>/poster.html"')
    if source.count(anchor) != 2:
        raise ValueError("Upstream Reel diagnostic anchors changed")
    command = "Run Step 10: python " + shlex.quote((root / "paper2poster/scripts/render_poster.py").as_posix()) + " <outdir>/poster.html"
    updates[diagnostics] = source.replace(anchor, json.dumps(command))
    for path, content in updates.items():
        path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", type=Path, required=True, help="Temporary directory containing the selected bundle's skills")
    parser.add_argument("--agent", choices=("claude", "codex"), required=True)
    parser.add_argument("--bundle", choices=("idea", "reel"), default="idea")
    parser.add_argument("--root", type=Path, required=True, help="Final agent home; only embedded in staged instructions")
    args = parser.parse_args()
    try:
        if args.bundle == "reel":
            if args.agent != "codex":
                raise ValueError("Reel is currently offered only for Codex")
            adapt_reel(args.stage, args.root)
        else:
            adapt(args.stage, args.root, args.agent)
        print("Staged instructions adapted; no runtime dependencies installed.")
    except (ValueError, OSError) as error:
        print(error, file=sys.stderr)
        sys.exit(1)
