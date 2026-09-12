---
name: update_config
description: Maintain this repository's installed configuration when the user asks to update, add, remove or repair selected content.
---

# Maintain the selected configuration

Target **codex** unless the user explicitly names another agent. Resolve its actual config home from the environment or the user's chosen path. Read `agent-config/selection.json` and `agent-config/files.json` there when present; query native installation state before changing anything.

Resolve the repository from the receipt's `repository` object: `url`, `revision`, and `update`. For `update.kind = branch`, fetch `update.ref`; for `default-branch`, query the remote HEAD with `git ls-remote --symref <url> HEAD`; for `pinned`, retain the recorded commit; for `local`, read `update.path`. Work in a temporary checkout when fetching. Preserve the user's existing checkout and local changes.

If an older receipt lacks repository metadata, use a reliably recorded repository origin or the URL/ref/checkout explicitly supplied in this request. If neither identifies the source, ask for it. A missing branch or local path requires a source decision; never guess a branch from the agent's name or fall back to a legacy installer.

Read `INSTALL.md`, `catalog.md` and `platforms/codex/README.md` from that same resolved source. If it lacks this agent-guided layout, report the incompatible source and request the intended one. Follow INSTALL for receipt fields, installation, updates, additions, explicit removals and retired IDs.

Default to recorded selections. When changing choices, show the complete supported catalogue by category with continuous numbers, author recommendations and installed status. Omitted items stay installed. Preserve pinned upstream sources, user edits, credentials and this agent's real lessons. Verify each operation and update its receipt; a repository version alone is not proof of success.
