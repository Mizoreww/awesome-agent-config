#!/usr/bin/env bash
set -euo pipefail
cat <<'GUIDE'
This repository uses agent-guided setup.
Ask Claude or Codex to read INSTALL.md, list the complete supported catalogue,
and install your selections.
Use INSTALL.md from this same checkout or the repository URL/ref you supplied.
No configuration has been changed by this entry point.
GUIDE
exit 2
