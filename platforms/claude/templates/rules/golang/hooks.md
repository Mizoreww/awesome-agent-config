# Go Hooks

## PostToolUse Hooks

This rule describes optional hooks. Configure them only when requested in the actual Claude home's `settings.json` (respect `CLAUDE_CONFIG_DIR`):

- **gofmt/goimports**: Auto-format `.go` files after edit
- **go vet**: Run static analysis after editing `.go` files
- **staticcheck**: Run extended static checks on modified packages
