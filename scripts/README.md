# Explicit file operations

These helpers have no catalogue, menu or plugin installer. The agent decides the selected item and final directory according to [INSTALL.md](../INSTALL.md).

Use an available Python 3.10+ interpreter (including a verified app-provided runtime). TOML merge alone also needs `tomlkit==0.13.3`; with uv available, prefix that operation with `uv run --with tomlkit==0.13.3 python`. Reuse an existing environment or prepare a temporary one; do not install Python packages globally. If no suitable runtime exists, explain this prerequisite before preparing one.

## Protected copy

Use an explicit absolute target directory. Examples assume Bash; on PowerShell use the same argument list with the verified Python command and quoted Windows paths.

```sh
python3 scripts/managed_files.py --root "$target_dir" --dry-run install skills/paper-reading skills/paper-reading --item paper-reading --origin "$source_revision"
python3 scripts/managed_files.py --root "$target_dir" install skills/paper-reading skills/paper-reading --item paper-reading --origin "$source_revision"
```

The complete directory is copied and verified, including assets/references/scripts. Existing identical external content is reused without claiming ownership. Different unowned or locally modified content is preserved with an error; inspect and discuss a concrete migration before any replacement. Symbolic links require explicit manual inspection.

```sh
python3 scripts/managed_files.py --root "$target_dir" status
python3 scripts/managed_files.py --root "$target_dir" seed-lessons --agent codex
python3 scripts/managed_files.py --root "$target_dir" remove skills/paper-reading
```

Use `--agent claude` for a Claude home. Each agent has its own blank template under `platforms/<agent>/templates/lessons.md`; the helper never infers the agent from a directory name. Existing lessons are always preserved, including when upgrading from the previous shared blank template. Never deploy the repository's project lessons as global memory.

The last command is only for an explicit removal request. Only helper-created, unchanged copies are removable. JSON/TOML merge targets cannot be removed with this operation.

## Partial configuration merge

```sh
python3 scripts/managed_files.py --root "$target_dir" --dry-run merge platforms/claude/templates/settings.json settings.json --item settings
uv run --with tomlkit==0.13.3 python scripts/managed_files.py --root "$target_dir" merge platforms/codex/templates/config.toml config.toml --item settings
```

Codex setup first applies only the import prerequisite:

```sh
uv run --with tomlkit==0.13.3 python scripts/managed_files.py --root "$target_dir" merge platforms/codex/templates/import-sync.toml config.toml --item import-sync --replace /desktop/external-agent-import-sync-enabled
```

Missing keys are added; unchanged previously managed values can update. Existing differing user values are preserved and reported by JSON pointer. `--replace /model`, for example, requires a user-selected change to that setting. Only hook and permission lists are additive; argument arrays and status lines are not concatenated. TOML comments and unrelated keys are preserved.

After deploying the corrected AGENTS instructions, remove the old lessons override only when its value is exactly `lessons.md`:

```sh
uv run --with tomlkit==0.13.3 python scripts/managed_files.py --root "$target_dir" merge platforms/codex/templates/import-sync.toml config.toml --item lessons --replace /desktop/external-agent-import-sync-enabled --remove model_instructions_file
```

Do not supply `--remove` if that value is absent or points elsewhere. Permissions, hooks, status lines and agents have separate template patches and catalogue IDs; merge only what was selected.

## Recovery and records

File metadata lives in `<target>/agent-config/files.json`; backups are below its `backups/` directory. Operations lock their metadata, record intent before replacing files, then verify content. The next operation can recover a completed or safely reversible interrupted write; unexpected user changes require inspection. Retain backups until the user has checked the result.

The agent maintains the selection/native-plugin record described in INSTALL.md separately. Never infer native-plugin ownership from a same-name skill or an import cache.

## Specific source preparation and verification

- `adapt_researchstudio.py --stage <temporary-Idea-skills> --agent <claude|codex> --root <final-root>`: changes only staged source and validates expected upstream anchors. The default Idea bundle prepares global paths/tool instructions; add `--bundle reel` for the five Codex Reel skills and their referenced runbooks. Use a fresh stage each time; publish only after success. This does not install business dependencies.
- `stage_lieflat.py <checkout> <fresh-stage>`: keeps root files and templates/examples/scripts/agents, including the license; excludes preview media. Review the upstream noncommercial license before selection.
- `check_mcp.py --timeout 60 -- <command> <args...>`: tests a stdio initialize handshake without adding a server. It stops the test process afterwards. HTTP integrations use their native client's connection/authentication check.
