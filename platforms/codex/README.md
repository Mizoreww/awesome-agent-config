# Codex 操作说明

先完成 [INSTALL.md](../../INSTALL.md) 的目录展示和选择。目标使用已核实的 Codex home，默认 `~/.codex`；App/CLI 共用 home 时只安装一次。所有自管 skills 以这个目录为权威副本。

使用本仓库管理 Codex 的前提是关闭外部 agent 自动导入，以免绕过用户的选择。在选型时说明这一点；开始安装所选内容前，局部合并 templates/import-sync.toml 并显式 `--replace /desktop/external-agent-import-sync-enabled`，验证值为 false。即使未选基础 settings 也执行这个前提操作；它不删除已导入内容，也不改变其他设置。

<a id="configuration"></a>
## 配置与子 agents

使用 [受控文件工具](../../scripts/README.md)，只处理对应所选 patch：

| Catalog ID | 来源 → 目标 / 操作 |
| --- | --- |
| instructions | templates/AGENTS.md → AGENTS.md；已有不同内容先具体合并 |
| settings | 仅合并 templates/config.toml → config.toml |
| permissions | 选择高自主权限后，合并 templates/permissions.toml；明确替换 /approval_policy 和 /sandbox_mode，不影响其它配置 |
| lessons | seed-lessons --agent codex 从 templates/lessons.md 创建空白记录；将 templates/AGENTS.md 的 Memory System 段合并到全局 AGENTS（若未随 instructions 部署），显式读取 global/project lessons，保留其余用户指令 |
| statusline | 合并 templates/statusline.toml；用户选择采用此 footer 时显式替换 /tui/status_line |
| agent-explorer | templates/agents/explorer.toml → agents/explorer.toml；合并 templates/agent-patches/explorer.toml |
| agent-reviewer | templates/agents/reviewer.toml → agents/reviewer.toml；合并 templates/agent-patches/reviewer.toml |
| agent-docs-researcher | templates/agents/docs-researcher.toml → agents/docs-researcher.toml；合并 templates/agent-patches/docs_researcher.toml |

子 agent 配置先复制验证，再注册其 config_file；失败不留下悬空配置。已有 AGENTS.md 引用的工作流应与用户所选内容对齐，缺少前提时解释，不暗中补装。

Codex 的跨项目纠错写入本 home 的 lessons.md，项目纠错写入项目根目录 lessons.md。模板和真实记录均与 Claude 独立；已有 lessons 不替换为新的空白模板。

旧模板把 `model_instructions_file = "lessons.md"` 用作记忆入口。这会替换内置指令。先部署显式读取 lessons 的 AGENTS，再仅对这个确切旧值执行文件工具的 `--remove model_instructions_file`；其他自定义路径保持不变。

<a id="plugins"></a>
## 原生插件优先

本机能力检查顺序：`codex plugin --help`、`codex plugin list --json`、`codex plugin list --available --json`。先核实当前 client 已提供的插件和实际能力；配置文件列出 enabled 不代表资源完整。

```sh
codex plugin marketplace add <repository-or-url> --json
codex plugin list --available --json
codex plugin add <exact-selector-from-the-list> --json
codex plugin list --json
```

| Catalog ID | 首选来源与范围 |
| --- | --- |
| superpowers | OpenAI 官方 openai/plugins，当前 selector 为 superpowers@openai-curated；只添加该包，避免重复安装 obra 源码副本 |
| karpathy | forrestchang/andrej-karpathy-skills；核实兼容包 selector、skill 路径及加载情况 |
| context7 | anthropics/claude-plugins-official 的兼容包，核实 HTTP MCP；不能完整适配时使用下面的原生 HTTP MCP |
| frontend-design | anthropics/claude-plugins-official 的纯 skill 兼容包；保持单一提供方 |

原生命令不支持 plugins 的 client，或包不能保持用户选定范围时，使用 [源码说明](../sources.md) 中已有的相应路径，并说明渠道。网络/安装失败不静默切换成源码。

Matt 固定 v1.1.0 commit 与精选范围，具体来源由本仓库 sources.md 定义。此上游快照没有 marketplace，使用源码方式，包含上游 handoff。只有实际验证了固定 source、入口与完整成员的兼容插件，才进行明确迁移；不因为最新上游已有 marketplace 就升级版本。

更新只升级相关 marketplace，再用原生 add/update 能力更新所选包，最后查询实际版本；不无参数升级所有 marketplace。卸载使用 `codex plugin remove <selector>`，先核实创建归属和依赖关系。原生插件 cache 与内部数据库不由文件工具修改。

<a id="local-skills"></a>
## Skills

共享 ../../skills 下的 paper-reading 是自有 skill，storage-analyzer 是保留上游署名的本仓库定制版，完整部署到 skills 同名目录。本目录 skills/update 部署到 skills/update，保留 update_config 调用名。Humanizer、Humanizer-zh、neat-freak 从 [上游安装](../sources.md#writing)。handoff 仅随 Matt 包从其上游获取，不再使用独立的本地副本。

本目录仍保存 Codex 历史 adversarial-review 源码以防遗失；它不是当前可选安装项。Codex 审查使用 Matt code-review，不运行 Claude 对审工具。

文档处理先核实本 client 的 OpenAI documents/pdf/spreadsheets/presentations 是否实际可用，满足需求时复用。否则使用原有 Anthropic 四件套的完整源码；如果对应兼容原生包已验证且满足同一范围，可优先采用原生渠道。examples 只取三个成员，不能改成整包十二项。

所有固定来源、成员与必要适配见 [sources.md](../sources.md)。

<a id="mcp"></a>
## MCP

先用 `codex mcp list` 核对现有服务，重名不同来源时保留并解释。下面的公开地址无需写入凭据：

```sh
codex mcp add context7 --url https://mcp.context7.com/mcp
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
```

仅在选择了相应服务且没有插件已提供它时执行。HTTP 服务通过原生连接/授权状态验证。

Playwright 固定为 0.0.78。Node >= 20 时先检查再注册：

```sh
python3 scripts/check_mcp.py --timeout 60 -- npx -y @playwright/mcp@0.0.78
codex mcp add playwright -- npx -y @playwright/mcp@0.0.78
```

Node 18 等旧环境使用私有 Node 24，不替换系统 Node：

```sh
python3 scripts/check_mcp.py --timeout 60 -- npx -y --loglevel=error --package=node@24 --package=@playwright/mcp@0.0.78 -- playwright-mcp
codex mcp add playwright -- npx -y --loglevel=error --package=node@24 --package=@playwright/mcp@0.0.78 -- playwright-mcp
```

Windows 若可执行入口是 npx.cmd，按本机 shell 核实调用方式；必要时通过原生 cmd 入口启动相同参数。没有可用 Node/npm 时说明并准备所选服务的前提，不影响不依赖它的 skills 安装。一次 initialize 成功只证明 MCP 启动；业务浏览器就绪按所需工作流另外验证。

GitHub：核实 [官方 MCP server](https://github.com/github/github-mcp-server) 支持后，使用 https://api.githubcopilot.com/mcp 和 `--bearer-token-env-var GITHUB_PERSONAL_ACCESS_TOKEN`，或复用既有受支持配置。用户在环境中设置 token；不要把值传入聊天或记录。旧版 @modelcontextprotocol/server-github 仅作为已有安装的来源识别，不自动删掉。

Lark：核实 [lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp)，用户补齐 app ID/secret 后按 `codex mcp add --help` 注册并验证。缺凭据记为待配置，不写占位服务器或打印真实 secret。templates/mcp 保存旧版可用的无凭据服务配置，供核对来源；不整份复制来启用全部 MCP。

<a id="claude-mem"></a>
## Claude-Mem 的 Codex 版本

上游 13.24.23（ed57a511f5dbf84e75c9a785df818c43b66b5849）的 marketplace `thedotmack` 指向 `./plugin`，其中已包含 `plugin/.codex-plugin/plugin.json`，引用 `hooks/codex-hooks.json`、`.mcp.json` 和完整 skills。优先核实并安装该 Codex 包：

```sh
codex plugin marketplace add thedotmack/claude-mem --json
codex plugin list --available --json
codex plugin add claude-mem@thedotmack --json
codex plugin list --json
```

用户选择后仍需读取 [上游](https://github.com/thedotmack/claude-mem) 当前 Codex 安装说明，定位 Codex 专用包，并核对 .codex-plugin/plugin.json、hooks、MCP 和 worker。通过原生插件发现/安装流程配置，按需完成原生 trust/初始化；保留数据库。没有可核实的 Codex 包时记录待支持，不安装 Claude hooks 来冒充兼容，也不复用其他机器的本地 cache 路径。
