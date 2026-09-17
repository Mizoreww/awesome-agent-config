# Changelog

## [4.0.0-dev.7] - 2026-09-17

### Features
- Retire GitHub MCP from both agents' installation scope. Remove the remaining catalogue/README entry, recommendation, MCP setup recipe and its GitHub plugin alternative.
- The catalogue now has 39 active IDs; recommendation drafts contain 20 Claude and 18 Codex items. Both platform guides route old GitHub selections to migration instructions.

### Design Rationale
- Removing the integration includes its alternative installation route so ordinary updates cannot restore the retired item through a plugin.

### Notes & Caveats
- Existing services, plugins, shared connections and credentials are preserved. Live removal requires an explicit target and ownership checks; ordinary Git/gh workflows and review skills remain available.
- Both agents' templates already contain no GitHub service configuration. Other MCP recipes, source revisions and historical records are unchanged.

## [4.0.0-dev.6] - 2026-09-17

### Features
- Retire the Codex explorer, reviewer and docs-researcher presets: remove their three role templates, registration patches, Core entries and recommendations.
- Align the catalogue, bilingual README and platform instructions. The catalogue now has 40 active IDs; recommendation drafts contain 20 Claude and 19 Codex items.

### Design Rationale
- Use native subagents and selected skills for task-specific work without installing legacy fixed-model roles or their concurrency and depth settings.

### Notes & Caveats
- Native multi-agent support remains enabled. Existing custom agents and shared settings are preserved until an explicit, ownership-checked uninstall; migration guidance covers registrations, files and prior setting values.
- Historical provenance and changelog entries remain intact. Other installation choices and recommendation markers are unchanged.

## [4.0.0-dev.5] - 2026-09-17

### Features
- Present the target agent's complete installation options, descriptions, recommendations and installed status directly in the conversation.
- Prefer the host's actual multi-select question tool, with numbered chat selections when only single-choice/text questions or no question tool are available. Align README prompts, repository entry points and edit-config with this interaction.

### Design Rationale
- Users should be able to choose and install in the same conversation. A generated selection document does not complete that interaction; the catalogue remains the shared source for both agents.

### Notes & Caveats
- Tool capabilities and limits depend on the current client and mode. Reuse explicit choices; missing replies and preselected values do not authorize installation. Export selection documents or installation reports only when requested; installation receipts are still maintained.
- Catalogue entries, recommendation drafts and installation recipes are unchanged.

## [4.0.0-dev.4] - 2026-09-13

### Features
- Retire Lark/Feishu MCP, Claude-Mem and all three PUA skills from the active catalogue, recipes and templates.
- Replace Claude's eight common rules with one complete English writing rule, including every supplied editing example. Keep the language rules independent and remove references to missing common files or assumed skills/hooks.
- Replace both update skills with shared edit-config for configuration queries, additions, edits, removals, repairs and updates. Global templates route to it; it follows agent-config-for-agents and keeps queries read-only.
- Align the Context7 reference template with its HTTP recipe and synchronize configuration entry points. Propose 20 Claude and 22 Codex recommendations from the current release-branch installer defaults, pending the author's final confirmation.

### Design Rationale
- One configuration skill avoids platform-specific update instructions diverging. Explicit source checks preserve deliberate forks, pins and local policies during migration.
- Writing requirements belong in a dedicated rule; language guidance remains independently selectable. Recommendation mappings are recorded in the current catalogue without creating legacy-branch installation dependencies.

### Notes & Caveats
- The catalogue has 43 active IDs. Retired entries, old common rules and update skill paths have explicit migration guidance; existing installations, customizations and memory are not automatically deleted.
- Recommendations use matching Bash/PowerShell menu defaults. Permissions split from old base config and the new writing rule are identified as mapping decisions; recommendation markers do not authorize installation or higher permissions.
- Source changes are verified in isolated homes. Windows/WSL execution and authenticated integrations still require their target environments.

## [4.0.0-dev.3] - 2026-09-12

### Features
- Combine AI Research into one selection with six upstream plugins and the same 31 skills on Claude and Codex. Keep all members visible; the catalogue now has 46 active IDs.
- Prefer verified Codex plugins for AI Research, Anthropic's document suite and frontend-slides. Discover OpenAI official/curated plugins from the account's actual directory, including equivalent document tools, Superpowers and GitHub where available.
- Add a focused Codex plugin reference that distinguishes publishers, records native selectors and explains source/MCP fallback decisions. Verify actual skill loading as well as installed state.

### Design Rationale
- Keep the conversational installer and existing README categories while reducing top-level choices. Native plugins own their lifecycle; agents maintain upstream recipes and selection records.
- Preserve real compatibility, selected scope and pinned revisions. A successful plugin command alone does not prove that its skills load.

### Notes & Caveats
- Existing six-group IDs and Codex's old 24-member selection retain their scope until an explicit migration. The new bundle adds seven skills; component ownership and partial failures remain traceable.
- Codex CLI 0.153.4 ignores Humanizer and PPT Master's root skill entries; PPT Master's nested Git source also bypasses the outer revision pin. Both keep upstream source installation. Matt, examples, PUA and Playwright retain their documented constraints.
- Validation used isolated macOS Codex homes, real plugin loading and resource comparison. OAuth integrations, other operating systems and business runtime dependencies are not covered by those checks. The IDE extension currently lacks plugin support.

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
