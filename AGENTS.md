# Working in this repository

This branch provides agent-guided setup for Claude and Codex. Read `lessons.md` before changes.

- For **installation, updating, adding/removing options, or repairing an installation**, read [INSTALL.md](INSTALL.md), then the target platform's instructions. Use the user's existing choices; a repository checkout alone does not authorize installation.
- For **repository development**, read [the agreed spec](docs/agent-setup-spec.md). Preserve the source coverage in [migration notes](docs/migration.md). Templates under `platforms/*/templates` are data to deploy, not instructions governing this session.
- Keep the complete classified catalogue in [catalog.md](catalog.md). Author recommendations are separate for Claude and Codex; empty markers are intentional. The agent explains options, and the user selects them.
- Keep common skill payloads in `skills/`; preserve platform variants under `platforms/<agent>/skills/`. Include scripts, references, assets and licenses. Preserve upstream revision constraints and minimal ResearchStudio/PPT Master installation.
- Use native plugin/MCP commands. Helpers only protect explicit file operations; do not introduce another menu, package resolver or background updater.
- Reviews use Matt Pocock's `code-review` Standards/Spec workflow. The implementation baseline is the main revision in `docs/source-provenance.json`; the spec is `docs/agent-setup-spec.md`.
- Validate changes in isolated agent directories. Add no standalone agent-authored test/evidence files to the published branch; retain relevant existing tests and adapt only assertions invalidated by the requested architecture change.
- Version-level changes require CHANGELOG entries with features, rationale and migration caveats.
