# Python Hooks

## PostToolUse Hooks

This rule describes optional hooks. Configure them only when requested in the actual Claude home's `settings.json` (respect `CLAUDE_CONFIG_DIR`):

- **black/ruff**: Auto-format `.py` files after edit
- **mypy/pyright**: Run type checking after editing `.py` files

## Warnings

- Warn about `print()` statements in edited files (use `logging` module instead)
