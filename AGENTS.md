# Working in this repository

This repository provides agent-guided setup for Claude and Codex. Read `lessons.md` before changes.

- For **installing this repository**, follow [INSTALL.md](INSTALL.md). Present the current target agent's complete options, uses and recommendations directly in the conversation; prefer available native multi-select questions under [the selection procedure](INSTALL.md#choose-options). Generate a selection document only when the user requests an export.
- For **inspecting, adding, changing, removing, repairing or updating agent configuration**, invoke [edit-config](skills/edit-config/SKILL.md). It routes installed changes to INSTALL and repository changes to MAINTAIN. Queries remain read-only; a repository checkout alone does not authorize installation.
- For **adding, editing, updating or retiring repository skills, plugins, recommendations or templates**, follow [MAINTAIN.md](MAINTAIN.md). Read [the agreed spec](docs/agent-setup-spec.md) for architectural changes. Current files define behavior; historical branch mappings are provenance only.
- Templates under `platforms/*/templates` are data to deploy, not instructions governing this session. Keep each agent's global instructions and lessons independent.
- Keep the complete classified catalogue in [catalog.md](catalog.md). Author recommendations are separate for Claude and Codex and follow its recorded basis. The agent explains options, and the user selects them.
- Keep author-owned and intentionally customized skills in `skills/` or `platforms/<agent>/skills/`, with complete resources and upstream attribution where applicable. Third-party originals stay upstream; maintain their installation recipes instead of vendoring payloads. Preserve revision constraints and minimal ResearchStudio/PPT Master installation. Handoff belongs only to the Matt bundle.
- Use native plugin/MCP commands. Helpers only protect explicit file operations; use the host's question UI for choices, without adding a standalone menu, package resolver or background updater.
- Reviews use Matt Pocock's `code-review` Standards/Spec workflow. Pin the commit preceding the work being reviewed (or the user's specified base); the spec is `docs/agent-setup-spec.md`.
- Validate changes in isolated agent directories. Add no standalone agent-authored test/evidence files to the published branch; retain relevant existing tests and adapt only assertions invalidated by the requested architecture change.
- Version-level changes require CHANGELOG entries with features, rationale and migration caveats.
