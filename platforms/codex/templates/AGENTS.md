# Global Instructions (Codex)

Paths below use the default Codex home. Resolve them against the actual `CODEX_HOME` when set.

## Memory System (Highest Priority)

### Architecture

- `~/.codex/AGENTS.md`: global instructions, auto-loaded
- `~/.codex/lessons.md`: cross-project/global correction source-of-truth (append-only)
- `<project-root>/lessons.md`: project-specific correction source-of-truth (append-only)

### Session Startup Flow

Before the first substantive response in a session, ensure lessons context is loaded from:

- `~/.codex/lessons.md` (read this file explicitly at session startup)
- When working in a project, locate its root with `git rev-parse --show-toplevel` (fall back to the current workspace root when it is not a Git repository), then read `<project-root>/lessons.md` if it exists
- Repeat the project-lessons check whenever work moves to a different project root during the session

### Self-Correction

**Identify corrections early**: user says something is wrong, says "remember / don't do this again", expresses frustration, or same operation fails repeatedly.

**After a correction**:
1. Classify the correction's scope before continuing: a correction tied to the current repository, its code, branches, tooling, or workflow is project-specific by default; only a rule that genuinely applies across projects is global
2. Immediately append a project-specific lesson to `<project-root>/lessons.md`; create the correction log there when absent while preserving any existing content
3. Append to `~/.codex/lessons.md` only when the correction is genuinely global; when uncertain, prefer the project log
4. Record date, context, mistake, and a concrete actionable rule
5. Continue task execution only after recording

## Core Settings

- Language: respond in user's preferred language; keep technical terms in English when appropriate
- Shell: use the shell available in the current environment (zsh/Bash or PowerShell)

## Communication Preferences

- If user says a hypothesis is wrong, stop that direction immediately
- Prefer implementation over repetitive questioning

## Workflow

- Configuration: invoke `edit-config` for inspecting, adding, changing, removing, repairing, or updating this repository's Claude/Codex configuration, templates, or catalogue. If unavailable, read and follow [its branch-specific instructions](https://github.com/Mizoreww/awesome-claude-code-config/blob/agent-config-for-agents/skills/edit-config/SKILL.md) without installing extra content. Queries remain read-only; changes follow the user's selected scope.

- Web search: before searching, determine the current real date — prefer system command (`date '+%Y-%m-%d'`), fall back to web time API if system clock may be inaccurate. Include the year (and month if relevant) in search queries. Never rely solely on model knowledge or system prompt for the date.
- Use explicit planning for non-trivial tasks
- Verify before marking done (tests/logs where applicable)
- Fix bugs directly and report what changed

## Version Changelog

When making version-level changes to a project (new features, major refactors, architectural changes, breaking changes), maintain a `CHANGELOG.md` in the project root:

```markdown
## [version] - YYYY-MM-DD
### Features
- What was changed
### Design Rationale
- Why it was done this way, what trade-offs were considered
### Notes & Caveats
- Edge cases, compatibility, migration concerns, etc.
```

- Not every commit needs an entry — only update on **version-level changes**
- Does not conflict with AGENTS.md: AGENTS.md manages instructions, CHANGELOG.md tracks evolution
- Create the file proactively if it doesn't exist

## Rule Set

- Use the project's documented standards and language-specific skills that are actually installed. This repository does not install additional language skills implicitly.

## Code Review

Whenever a code review is needed — whether explicitly requested by the user or triggered by a workflow — use the selected `code-review` skill from `mattpocock/skills` when available. If it is absent, explain the prerequisite and review using available tools; install it only when selected. In Codex sessions, do not invoke `adversarial-review` and do not spawn reviewers through `claude -p`; use the Matt Pocock two-axis Standards/Spec review workflow directly.

## Paper Reading

- Use the `paper-reading` skill for research paper tasks when selected and installed
