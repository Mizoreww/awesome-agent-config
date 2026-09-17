Write-Output @"
This repository uses agent-guided setup.
Ask your agent to read INSTALL.md and show its supported options, uses and
recommendations directly in chat. Prefer native multi-select questions when
available; otherwise choose multiple numbers in chat. Then install your choices.
Generate a separate selection document only if you request an export.
Use INSTALL.md from this same checkout or the repository URL/ref you supplied.
No configuration has been changed by this entry point.
"@
exit 2
