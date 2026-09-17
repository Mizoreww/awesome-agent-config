# Claude 操作说明

先完成 [INSTALL.md](../../INSTALL.md) 的目录展示与用户选择。目标默认是已核实的 Claude config directory；全局默认 `~/.claude`，支持用户指定的 `CLAUDE_CONFIG_DIR`。命令先以本机 `claude ... --help` 核实。

<a id="configuration"></a>
## 配置与规则

使用 [managed_files.py](../../scripts/README.md) 的预览、受控复制与局部合并；模板在本目录的 templates 下。

| Catalog ID | 来源 → 目标 / 操作 |
| --- | --- |
| instructions | templates/CLAUDE.md → CLAUDE.md，包含 edit-config 调用入口；现有不同文件需要具体合并，不直接覆盖 |
| settings | 仅合并 templates/settings.json → settings.json |
| permissions | 用户选择权限配置后，合并 templates/permissions.json；有差异的权限键需要明确 `--replace`，不要顺带改模型或插件 |
| lessons | seed-lessons --agent claude 从 templates/lessons.md 创建空白记录；将 templates/CLAUDE.md 的 Memory System 段合并到全局 CLAUDE（若未随 instructions 部署），再合并 templates/lessons-hooks.json。保留用户指令与 hooks；Windows 先核实这些 command hooks 使用的 Bash 可用 |
| statusline | templates/hooks/statusline.sh → hooks/statusline.sh；合并 templates/statusline.json；检查 Bash/jq。字体位于 templates/fonts（含 LICENSE），按 OS 用户字体目录安装，缺字体可使用文本显示 |
| rules-writing-style | templates/rules/writing-style.md → rules/writing-style.md；完整八条写作规则与英文示例 |
| rules-python | templates/rules/python → rules/python |
| rules-typescript | templates/rules/typescript → rules/typescript |
| rules-golang | templates/rules/golang → rules/golang |

写作规则按单文件部署，语言规则按所选目录复制；不把说明用的 rules/README.md 放入会自动加载的规则目录。语言规则独立于写作规则，按项目需要选择。旧 Common rules 的处理见[迁移说明](../../docs/migration.md#common-rules)。hooks/statusline 默认通过 CLAUDE_CONFIG_DIR 定位；若安装到未设置该环境变量的自定义目录，先在临时 patch 中生成正确引用并验证，再合并。

全局模板中提到的工作流必须与所选能力一致：解释依赖、让用户选择对应工作流，或对拟部署模板做明确适配；不能暗中安装未选插件。

Claude 的跨项目纠错写入本 home 的 lessons.md，项目纠错写入当前 Claude 项目的 memory/MEMORY.md。模板和真实记录均与 Codex 独立；已有 lessons 不替换为新的空白模板。

<a id="plugins"></a>
## 原生插件

先查询 `claude plugin list --json` 与 marketplace 状态。仅为用户所选插件添加必要 marketplace：

```sh
claude plugin marketplace add <repository-or-url> --scope user
claude plugin install <plugin@marketplace> --scope user
claude plugin list --json
```

下面是本仓库支持的插件 selector。只执行所选行，不遍历全表安装。

| Catalog ID | 原生 selector | Marketplace 来源 |
| --- | --- | --- |
| karpathy | andrej-karpathy-skills@karpathy-skills | forrestchang/andrej-karpathy-skills |
| matt-workflow | mattpocock-skills@mattpocock | mattpocock/skills |
| superpowers | superpowers@claude-plugins-official | anthropics/claude-plugins-official |
| claude-pr-review | code-review@claude-plugins-official | anthropics/claude-plugins-official |
| codex-in-claude | codex@openai-codex | openai/codex-plugin-cc |
| code-simplifier | code-simplifier@claude-plugins-official | anthropics/claude-plugins-official |
| context7 | context7@claude-plugins-official | anthropics/claude-plugins-official |
| playwright | playwright@claude-plugins-official | anthropics/claude-plugins-official |
| documents | document-skills@anthropic-agent-skills | anthropics/skills |
| examples | example-skills@anthropic-agent-skills | anthropics/skills |
| frontend-design | frontend-design@claude-plugins-official | anthropics/claude-plugins-official |
| humanizer | humanizer@humanizer（上游要求 Claude Code >= 2.1.142） | blader/humanizer |
| frontend-slides | frontend-slides@frontend-slides | zarazhangrui/frontend-slides |
| ppt-master | ppt-master@ppt-master | hugohe3/ppt-master |
| claude-health | health@claude-health | tw93/claude-health |
| ai-research | [六个分类插件组成一个安装项](#ai-research) | Orchestra-Research/AI-research-SKILLs |

读取所用 manifest 核实完整成员和插件要求。example-skills 已含 frontend-design，选择整包后复用；同一服务的 MCP 不再另外注册。

更新用本机帮助核实 `claude plugin update <selector>`，显式卸载用 `claude plugin uninstall <selector> --scope user`；只操作用户选择且归属明确的项。原来由用户安装的插件复用时不接管所有权。

<a id="ai-research"></a>
## AI Research 整包

用户选择 `ai-research` 后，添加一次 `Orchestra-Research/AI-research-SKILLs` marketplace，核对其 checkout revision 与[共享来源表](../sources.md#ai-research)，再按上面的原生命令依次安装该表六个 selector。对话目录只显示一个编号；两端统一为这六组完整的 31 项，成员见 [catalog](../../catalog.md#ai-research-members)。若当前上游已改变范围或版本，先解释差异；原生渠道无法满足固定约束时使用共享表中的完整源码配方。

选择记录使用 `ai-research`，每个插件分别保存 selector、版本、创建归属与结果。复用已有安装；部分插件失败时保留已成功组件，整包标记部分完成，只重试未完成项。更新/移除也核对每个组件的归属与修改。旧单组选择按[迁移规则](../../docs/migration.md#ai-research)保留原范围。

<a id="local-skills"></a>
## 本地 skills

共享目录 ../../skills 下的 paper-reading 是自有 skill，storage-analyzer 是保留上游署名的本仓库定制版，分别完整复制到目标 skills 同名目录。Humanizer、Humanizer-zh、neat-freak 从 [上游安装](../sources.md#writing)，不再从本仓库复制。

本目录 skills/adversarial-review 是 Claude 专属版本，安装到 skills/adversarial-review。共享 ../../skills/edit-config 完整部署到 skills/edit-config，处理配置查询与增删改，跟踪本仓库 main 分支；具体来源冲突与更新流程由该 skill 定义。安装全局指令不会暗中补装它；模板也提供同一工作流的读取入口。旧更新 skill 见[迁移说明](../../docs/migration.md#edit-config)。上游获取的 DeepXiv、ResearchStudio、lieflat-charts 见 [共享源码说明](../sources.md)。

adversarial-review 是基于 poteto/noodle 的定制版，来源与修改见其 UPSTREAM.md。handoff 已包含在 Matt 原生包内，不提供独立安装项。

<a id="mcp"></a>
## MCP

Context7 和 Playwright 通过上述原生插件提供，选择它们时复用插件的 MCP，无需另行注册。其他未选服务不因配置合并而启用。

旧 GitHub MCP 记录按[退役说明](../../docs/migration.md#github-mcp)处理，不再作为安装或更新项。
