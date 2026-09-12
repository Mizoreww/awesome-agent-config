# Claude Rules

| Selection | Source | Installed path |
| --- | --- | --- |
| rules-writing-style | writing-style.md | rules/writing-style.md |
| rules-python | python/ | rules/python/ |
| rules-typescript | typescript/ | rules/typescript/ |
| rules-golang | golang/ | rules/golang/ |

The writing rule contains the complete eight writing requirements and English editing examples. Language directories are independent selections containing coding, testing, patterns, security, and optional hook guidance. They do not require a common rule layer or install the external skills mentioned in their references.

Follow [Claude configuration operations](../../README.md#configuration) and the [protected file workflow](../../../../scripts/README.md). Copy the selected file or full language directory without flattening it. Keep this README out of the deployed rules directory.

The previous common rule files are retired. Handle existing installations using the [migration instructions](../../../../docs/migration.md#common-rules); repository removal alone does not authorize deleting users' rules.

For new or changed rules, follow [MAINTAIN.md](../../../../MAINTAIN.md), keep references valid, and update the catalogue and both READMEs. Configuration requests use [edit-config](../../../../skills/edit-config/SKILL.md).
