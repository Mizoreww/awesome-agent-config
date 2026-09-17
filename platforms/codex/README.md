# Codex 操作说明

先完成 [INSTALL.md](../../INSTALL.md) 的目录展示和选择。目标使用已核实的 Codex home，默认 `~/.codex`；App/CLI 共用 home 时只安装一次。所有自管 skills 以这个目录为权威副本。

使用本仓库管理 Codex 的前提是关闭外部 agent 自动导入，以免绕过用户的选择。在选型时说明这一点；开始安装所选内容前，局部合并 templates/import-sync.toml 并显式 `--replace /desktop/external-agent-import-sync-enabled`，验证值为 false。即使未选基础 settings 也执行这个前提操作；它不删除已导入内容，也不改变其他设置。

<a id="configuration"></a>
## 配置

使用 [受控文件工具](../../scripts/README.md)，只处理对应所选 patch：

| Catalog ID | 来源 → 目标 / 操作 |
| --- | --- |
| instructions | templates/AGENTS.md → AGENTS.md；已有不同内容先具体合并 |
| settings | 仅合并 templates/config.toml → config.toml |
| permissions | 选择高自主权限后，合并 templates/permissions.toml；明确替换 /approval_policy 和 /sandbox_mode，不影响其它配置 |
| lessons | seed-lessons --agent codex 从 templates/lessons.md 创建空白记录；将 templates/AGENTS.md 的 Memory System 段合并到全局 AGENTS（若未随 instructions 部署），显式读取 global/project lessons，保留其余用户指令 |
| statusline | 合并 templates/statusline.toml；用户选择采用此 footer 时显式替换 /tui/status_line |

本仓库使用 Codex 的原生子 agent 能力，按任务和已选 skills 分工；不再部署固定模型的角色预设或设置它们的并发/嵌套限制。旧预设的处理见[迁移说明](../../docs/migration.md#codex-agent-presets)。已有 AGENTS.md 引用的工作流应与用户所选内容对齐，缺少前提时解释，不暗中补装。

Codex 的跨项目纠错写入本 home 的 lessons.md，项目纠错写入项目根目录 lessons.md。模板和真实记录均与 Claude 独立；已有 lessons 不替换为新的空白模板。

旧模板把 `model_instructions_file = "lessons.md"` 用作记忆入口。这会替换内置指令。先部署显式读取 lessons 的 AGENTS，再仅对这个确切旧值执行文件工具的 `--remove model_instructions_file`；其他自定义路径保持不变。

<a id="plugins"></a>
## 原生插件优先

为所选条目确定渠道时读取[插件选择与安装](plugins.md)：它集中维护 OpenAI 官方/curated、上游 Codex 包及兼容插件的来源、selector、验证办法和源码后备原因。先查询当前 client / 账号实际可见的目录，复用已有能力；App / CLI 与 IDE 的插件支持分别核实。

AI Research 是[一个 31 项整包](../sources.md#ai-research)，通过六个上游分类插件提供。选择、版本、归属和失败状态逐组件记录，旧选择按[迁移说明](../../docs/migration.md#ai-research)处理。

更新只升级相关 marketplace，再用原生 add/update 能力更新所选包，最后查询实际版本；不无参数升级所有 marketplace。卸载使用 `codex plugin remove <selector>`，先核实创建归属和依赖关系。原生插件 cache 与内部数据库不由文件工具修改。

<a id="local-skills"></a>
## Skills

共享 ../../skills 下的 paper-reading、edit-config 是自有 skills，storage-analyzer 是保留上游署名的本仓库定制版，完整部署到 skills 同名目录。edit-config 处理配置查询与增删改，跟踪本仓库 main 分支；具体来源冲突与更新流程由该 skill 定义。安装全局指令不会暗中补装它；模板也提供同一工作流的读取入口。旧更新 skill 见[迁移说明](../../docs/migration.md#edit-config)。Humanizer、Humanizer-zh、neat-freak 从 [上游安装](../sources.md#writing)。handoff 仅随 Matt 包从其上游获取，不再使用独立的本地副本。

本目录仍保存 Codex 历史 adversarial-review 源码以防遗失；它不是当前可选安装项。Codex 审查使用 Matt code-review，不运行 Claude 对审工具。

文档处理按[插件选择](plugins.md)优先复用 OpenAI 四种文档能力；缺少覆盖时安装 Anthropic 四件套兼容插件，client 不支持时采用完整源码。examples 只取三个成员，不能改成整包十二项。

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

旧 GitHub MCP / 对应插件选择按[退役说明](../../docs/migration.md#github-mcp)处理，不再作为安装或更新项。

templates/mcp 保存既有无凭据服务的参考配置，供核对来源；不整份复制来启用全部 MCP。
