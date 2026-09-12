# Changelog

## [4.0.0-dev.2] - 2026-09-12

### Features
- Restore the full bilingual README, including the original 11 categories, usage guidance, tables, showcases, settings and customization. Align all 51 active catalogue entries with the same category order.
- Make installation and updates independent of legacy branches. Record the repository source and its branch, default-branch, pinned or local update policy; both update skills follow that record.
- Add MAINTAIN.md so agents maintain skill payloads, upstream recipes, recommendations and both READMEs together, including explicit handling of retired IDs.
- Split Claude and Codex blank lessons templates and require an explicit agent when seeding a log. Keep their global instructions and project memory conventions independent.
- Replace vendored Humanizer, Humanizer-zh and neat-freak originals with upstream installation recipes. Keep author-owned and intentionally customized skills here with attribution.
- Fold handoff into the Matt bundle, using its upstream version; remove the independent option and local copy. Codex's selected Matt bundle now has 20 members.

### Design Rationale
- The current repository is the authority for ongoing development. Historical mappings prove the initial consolidation and remain available for provenance without freezing future skill changes.
- Preserve the detailed user-facing guide while letting the agent own platform detection, explanations and installation commands.

### Notes & Caveats
- Existing lessons remain untouched. Direct helper callers must use `seed-lessons --agent claude` or `--agent codex`.
- Older selection receipts need a verified repository source before updates; a missing or incompatible source is not replaced with a guessed legacy branch.
- Existing standalone handoff and third-party copies remain until the user chooses a migration. Humanizer's current upstream is 3.0.0; explain the change from the previously bundled 2.2.0 before migrating.
- No branch archival or remote default-branch change is performed. During the transition, share the current README page URL with its ref or open its checkout.

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
