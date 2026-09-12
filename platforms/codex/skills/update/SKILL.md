---
name: update_config
description: Update this agent's selected configuration from the agent-config-for-agents branch. Use when the user asks to update, add, or remove this repository's installed configuration.
---

# Maintain the selected configuration

Target **codex** unless the user explicitly names another agent. Read the target's `agent-config/selection.json` and `agent-config/files.json` when present. Query actual native installation state; without a receipt, preserve existing external content.

Read `INSTALL.md` from the same resolved revision of:
https://github.com/Mizoreww/awesome-claude-code-config/tree/agent-config-for-agents

Follow its update/add/remove flow and the codex platform instructions. Default to the recorded selections. For changed selections, show the complete supported catalogue by category with continuous numbers, author recommendations and installed status. An omitted item remains installed; removal requires an explicit request.

Preserve pinned sources, user edits, credentials and real lessons. Verify each selected operation and update its receipt. A matching repository version alone does not establish that all items are installed or up to date.
