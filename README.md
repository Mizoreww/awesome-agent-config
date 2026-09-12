# Agent-guided Claude & Codex configuration

[中文](README.zh-CN.md)

One repository for Claude and Codex settings, shared skills and platform-specific integrations. Your existing agent detects the environment, explains the complete catalogue, and installs what you choose.

Give Claude or Codex this request:

> Read INSTALL.md in https://github.com/Mizoreww/awesome-claude-code-config/tree/agent-config-for-agents. Configure the agent I am talking to. List all supported installation options by category with continuous numbers, mark author recommendations and existing installations, and explain their purpose. Install and verify my choices, preserving existing customizations.

The agent uses native plugin/MCP commands and small helpers for protected file operations. You do not need to understand the installation channels before choosing.

- [Complete catalogue](catalog.md): separate Claude/Codex support and author recommendation columns. Recommendations remain empty until the author supplies them.
- [Installation workflow](INSTALL.md): first setup, additions, updates and explicit removals.
- [Claude instructions](platforms/claude/README.md) · [Codex instructions](platforms/codex/README.md).
- [Migration and source coverage](docs/migration.md): preserves both published branches, including externally fetched skill groups.
- [Changelog](CHANGELOG.md).

Common skills remain under `skills/`; platform variants and deployable settings live under `platforms/`. The root AGENTS.md/CLAUDE.md govern repository work, and are not copied into your global configuration.

This is the development branch based on Claude v3.2.0, with Codex v2.11.0 capabilities incorporated. Existing release branches are unchanged. macOS/Linux/Windows/WSL use the same agent instructions; actual runtime support is checked for each selected integration. See the migration notes for verification limits.

This repository is MIT licensed. Bundled skills retain their own notices; external lieflat-charts uses PolyForm Noncommercial 1.0.0. Review the selected source license.
