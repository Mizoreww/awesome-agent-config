# Changelog

## [4.0.0-dev.1] - 2026-09-12

### Features
- Introduce one agent-guided setup flow for Claude and Codex: detect the environment, show the complete classified catalogue with numbers and author recommendations, then install the user's choices.
- Preserve main v3.2.0 and codex v2.11.0 skills in one repository. Share five identical payloads, retain five platform variants, and document the external plugin/skill sources and pinned selections.
- Prefer native plugin/MCP management. Add small helpers for protected copies, partial JSON/TOML merges, backups, source adaptation and MCP initialization checks.
- Separate base settings, permissions, status lines, lessons hooks and subagents. Disable Codex external-agent import independently of optional base settings.

### Design Rationale
- Let the existing agent explain platform differences and resolve user choices. A second menu, binary distribution or package resolver would duplicate its role.
- Keep one Markdown catalogue with separate Claude/Codex recommendation columns. Recommendations remain empty until the author provides them.
- Preserve selected membership and revisions during native migration, especially Codex's Matt v1.1.0 snapshot and custom handoff.

### Notes & Caveats
- This development branch starts from main; neither release branch is merged or replaced. See [migration notes](docs/migration.md) and [source mappings](docs/source-provenance.json).
- install.sh/install.ps1 now show the agent entry point and exit with code 2. Previous menu flags no longer mutate configuration.
- Existing custom files, credentials, lessons and memory databases are preserved. Updating a selection never removes omitted items; uninstall requires an explicit request and ownership checks.
- ResearchStudio Idea/Reel and PPT Master install complete source with necessary adaptations only. Runtime dependencies remain a first-use step.
- Replace only the exact legacy model_instructions_file = "lessons.md" setting after deploying explicit lessons-reading instructions.
- Native Windows/WSL execution, credentialed integrations and the complete Claude-Mem lifecycle need platform-specific validation. New development checks remain outside the published tree; relevant existing skill tests remain.

Earlier releases: [Claude history](platforms/claude/CHANGELOG.previous.md) · [Codex history](platforms/codex/CHANGELOG.previous.md).
