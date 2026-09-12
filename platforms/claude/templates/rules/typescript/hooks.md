# TypeScript/JavaScript Hooks

## PostToolUse Hooks

This rule describes optional hooks. Configure them only when requested in the actual Claude home's `settings.json` (respect `CLAUDE_CONFIG_DIR`):

- **Prettier**: Auto-format JS/TS files after edit
- **TypeScript check**: Run `tsc` after editing `.ts`/`.tsx` files
- **console.log warning**: Warn about `console.log` in edited files

## Stop Hooks

- **console.log audit**: Check all modified files for `console.log` before session ends
