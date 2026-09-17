---
name: edit-config
description: Inspect, add, change, remove, repair, or update Claude and Codex configuration from Mizoreww/awesome-claude-code-config on agent-config-for-agents. Use for configuration queries and edits, installed skills/plugins/rules/MCP, and changes to this repository's configuration templates or catalogue.
---

# Edit agent configuration

This skill serves both Claude and Codex and tracks one repository branch:

- Repository: `https://github.com/Mizoreww/awesome-claude-code-config.git`
- Branch: `agent-config-for-agents`

## 1. Identify the request and target

Distinguish inspection from modification, and repository edits from changes to an installed agent. Default to the current conversation's agent; target both only when requested. Resolve the actual `CLAUDE_CONFIG_DIR`, `CODEX_HOME`, or user-selected home. Read relevant configuration, `agent-config/selection.json`, and `agent-config/files.json` when present; use native lists to verify installed state. Redact credentials.

For inspection, report current values, selected content, sources, differences, and pending items directly in the conversation as relevant. Export a document only when requested. Reading configuration does not authorize writing receipts, changing settings, installing dependencies, or disabling imports. Stop when the query is answered unless the user also requested a change.

Completion: the operation, target, existing state, and authorization are clear.

## 2. Resolve the branch for changes

Fetch the branch above into a fresh temporary checkout and resolve its full commit SHA. Use files from that same SHA throughout an installation/update operation. Preserve existing user checkouts and local edits. A missing branch or incompatible layout is an error; do not fall back to `main`, `codex`, or the remote default branch.

For installed configuration, compare the receipt's repository URL and update policy with this target. Equivalent HTTPS/SSH URLs for this GitHub repository identify the same source. Matching branch records can proceed. Missing source metadata uses this skill's explicit target without inventing installation ownership. A conflicting fork, branch, pinned commit, or local source remains unchanged until the user chooses migration; reuse an already explicit migration request instead of asking again. Record the previous source when migrating, and keep all selections, hashes, and backups.

For repository edits, use the user's designated checkout, verify its repository and branch, and read its current `MAINTAIN.md`. A checkout already on the target branch may contain authorized uncommitted changes; preserve and work with them rather than substituting the remote snapshot. Installation changes still use a single resolved source as described above.

Completion: the source, revision, and any source migration are established.

## 3. Apply the requested operation

- **Installed configuration:** read `INSTALL.md`, `catalog.md`, and the target platform's README from the resolved source. Follow their native plugin/MCP, protected file, and verification procedures. Default to recorded selections. For additions or changed selections, follow `INSTALL.md`'s `choose-options` procedure: show the target agent's complete supported catalogue directly in the conversation, with category grouping, continuous item numbers, useful descriptions, author recommendations and installed status. Prefer a real multi-select question tool when available; otherwise accept multiple numbers or names in chat. Export a selection document only when requested. Reuse explicit choices; wait for an actual response when choices are missing. Recommendations do not authorize installation.
- **Repository configuration:** follow `MAINTAIN.md` for templates, skills, catalogue entries, recommendations, and documentation. Editing repository files does not modify an agent home.

Handle retired or renamed IDs using `docs/migration.md`. Omitted selections remain installed. Removal requires an explicit request and ownership checks. Preserve upstream revision constraints, local customizations, credentials, hooks, memory databases, and each agent's real lessons. Continue within the user's existing authorization.

Completion: each requested change has an actual result, including failures and pending steps.

## 4. Verify and record

Verify the changed files or native resources. For installed changes, record `repository.url`, the actual `repository.revision`, and `repository.update = {"kind":"branch","ref":"agent-config-for-agents"}` after source resolution; preserve per-item revisions and provenance. Repository edits follow their own commit and validation workflow. A repository version alone does not establish installation success.

Report what changed and what remains pending. Keep the two agent homes and their records independent. The old `update-config` / `update_config` names migrate to this skill through the repository's migration instructions.
