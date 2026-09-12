#!/usr/bin/env bash
# Check the shared entry points and structure without a GNU grep dependency.
set -euo pipefail
repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python3 - "$repo_dir" <<'PY'
from pathlib import Path
import re
import sys
root = Path(sys.argv[1])
en, zh = ((root / name).read_text(encoding="utf-8") for name in ("README.md", "README.zh-CN.md"))
for label, pattern in (("headings", r"^#+ "), ("code fences", r"^```"), ("table rows", r"^\|")):
    counts = [len(re.findall(pattern, text, re.M)) for text in (en, zh)]
    if counts[0] != counts[1]:
        sys.exit(f"{label} differ: {counts}")
links = [re.findall(r"\]\(([^)]+)\)", text) for text in (en, zh)]
normalize = lambda targets: [p.replace(".zh-CN.md", ".md") for p in targets]
if normalize(links[0]) != normalize(links[1]):
    sys.exit("README link targets differ")
print("README structure and entry points match.")
PY
