<!-- 用户表格与 catalog.md、README.md 同步维护。 -->

[English](README.md) | **中文** | [更新日志](CHANGELOG.zh-CN.md)

# Awesome Claude Code & Codex Configuration

![Claude 状态栏](assets/statusline.png)

一个仓库维护 [Claude Code](https://claude.com/claude-code) 和 [Codex](https://developers.openai.com/codex/) 的全局指令、编码规则、插件、共享 skills、状态栏与纠错记忆。已有 agent 负责识别平台、解释选项并安装你选择的内容。macOS、Linux、Windows、WSL 共用这套对话流程，具体命令按本机 client 核实。

## 示例

![Claude Code Demo](images/claude-code-demo.png)

- [paper-reading skill 实战 — *Attention Is All You Need*](docs/Attention_Is_All_You_Need.zh-CN.md)
- [adversarial-review skill 实战](docs/adversarial-review-showcase.md)

## 快速开始

在 Claude 或 Codex 中打开这份 checkout，或把**当前正在阅读的仓库页面 URL**与下面这段请求一起发给 agent。分享分支页面时保留 URL 中的 branch/ref。

> 请读取我提供的 checkout 或仓库页面中的 INSTALL.md，使用与这份 README 相同的分支/revision。默认配置当前对话使用的 agent。检查系统、client 和已有配置，直接在当前对话中按分类完整列出这个 agent 支持的安装项，连续编号，附上具体用途、作者推荐与已安装状态。优先使用可用的原生多选问答；没有时让我在对话里选择多个编号或名称。选项直接显示在对话中，不生成单独的 Markdown 文档或报告。根据我的选择安装和验证，保留已有定制。

Agent 会在当前对话中只展示目标 agent 支持的完整选项，附上用途与推荐。客户端有真正的多选问答工具时，按分类勾选；没有时，直接回复多个编号、名称或自然语言选择。Agent 会遵守工具的实际限制，并沿用你已经明确的选择。插件整包占一个编号并列出成员，包内已有能力不会再重复安装。推荐草案按当前 main/Codex 安装菜单默认项整理，[映射关系](catalog.md#recommendations)已注明，待作者最终确认；推荐标记不代表你已同意安装。

之后直接说“添加 paper-reading”“更新我上次选择的内容”或“移除 storage-analyzer”。已有选择会沿用，没有提到的已安装项不会被卸载。两端统一使用 `edit-config` 查询、增删改、修复和更新配置，跟踪本仓库的 `agent-config-for-agents` 分支。查询只读；未安装 skill 时，全局指令提供同一工作流的读取入口。

优先使用原生插件/MCP 命令；所选范围或 client 需要时，agent 再按仓库说明采用源码安装。你无需自己判断 npx、插件和 skill 复制渠道。Codex 安装会关闭外部 agent 自动导入，使安装内容遵循你的选择。Windows 与 WSL 分别检测配置，共用 home 的 App/CLI 会复用已有安装。

Codex 会先检查可用的 OpenAI 官方/curated 目录，再核实上游 Codex 包与兼容插件。[插件说明](platforms/codex/plugins.md)集中记录具体渠道和限制；官方目录的可用范围取决于账号与 client，已有同等能力会优先复用。

[安装流程](INSTALL.md) · [Claude 操作说明](platforms/claude/README.md) · [Codex 操作说明](platforms/codex/README.md) · [完整目录与整包成员](catalog.md)

## 分类目录

保留原有分类，合并 Claude 与 Codex 的能力。第三方原版从上游安装，本仓库保存自有 skill 与保留署名的定制版。handoff 仅作为 Matt 包成员提供。`—` 表示本仓库未为该 agent 提供该项，agent 展示选择时会过滤它。平台列中的 **★** 表示该 agent 的候选推荐，待作者最终确认。准确渠道、稳定 ID 与推荐标记以 [catalog.md](catalog.md) 为准。

### Core · 基础配置

| 项目 | 来源 | 功能 | Claude | Codex |
| --- | --- | --- | --- | --- |
| **CLAUDE.md / AGENTS.md** | [本仓库](platforms/claude/README.md#configuration) | 各 agent 独立的全局指令 | 模板 ★ | 模板 ★ |
| **Base settings** | [本仓库](platforms/codex/README.md#configuration) | 局部合并模型、推理与运行设置 | 模板 ★ | 模板 ★ |
| **Permissions** | [本仓库](platforms/codex/README.md#configuration) | 用户选择可信环境后，单独配置高自主权限 | 模板 ★ | 模板 ★ |
| **Writing style rule** | [本仓库](platforms/claude/README.md#configuration) | 完整英文写作要求与示例，替代原 Common rules | 规则 ★ | — |
| **StatusLine** | [本仓库](platforms/claude/README.md#configuration) | Claude 渐变上下文/用量栏与字体；Codex 原生状态栏 | 模板 ★ | 模板 ★ |
| **Lessons** | [本仓库](platforms/codex/README.md#configuration) | 独立空白全局记录及记忆规则，保留真实纠错历史 | 模板 ★ | 模板 ★ |

### Language Rules · 语言规则

| 项目 | 来源 | 功能 | Claude | Codex |
| --- | --- | --- | --- | --- |
| **Python rules** | [本仓库](platforms/claude/README.md#configuration) | PEP 8、pytest、类型注解与 bandit | 模板 | — |
| **TypeScript rules** | [本仓库](platforms/claude/README.md#configuration) | Zod、Playwright 与不可变性 | 模板 | — |
| **Go rules** | [本仓库](platforms/claude/README.md#configuration) | gofmt、表驱动测试与 gosec | 模板 | — |

### Review · 审查

| 项目 | 来源 | 功能 | Claude | Codex |
| --- | --- | --- | --- | --- |
| **Claude code-review** | [Anthropic](https://github.com/anthropics/claude-plugins-official) | 基于置信度的 PR 代码审查 | 原生插件 ★ | — |
| **Matt code-review** | [Matt Pocock](https://github.com/mattpocock/skills) | Standards / Spec 双轴审查；Codex 可单独选择 | Matt 包内 | 精选源码 ★ |
| **adversarial-review** | [poteto/noodle](https://github.com/poteto/noodle/blob/main/.agents/skills/adversarial-review/SKILL.md) | Skeptic、Architect、Minimalist 视角的跨模型审查 | 内置 skill ★ | — |
| **codex-in-claude** | [OpenAI](https://github.com/openai/codex-plugin-cc) | 在 Claude 内调用 Codex CLI，按需选择审查方式 | 原生插件 | — |

### Workflow · 工作流

| 项目 | 来源 | 功能 | Claude | Codex |
| --- | --- | --- | --- | --- |
| **andrej-karpathy-skills** | [Karpathy skills](https://github.com/forrestchang/andrej-karpathy-skills) | 先思考、保持简单与改动集中、明确可验证结果 | 原生插件 ★ | 插件 / 源码 ★ |
| **superpowers** | [obra / OpenAI curated](https://github.com/obra/superpowers) | 头脑风暴、调试、TDD、worktree 与规划，14 项整包 | 原生插件 | 插件 / 源码 |
| **mattpocock-skills** | [Matt Pocock](https://github.com/mattpocock/skills) | 规划、TDD、研究、grilling 与交付；Claude 整包，Codex v1.1.0 精选 20 项，含 handoff | 原生插件 ★ | 精选源码 ★ |
| **neat-freak** | [khazix-skills](https://github.com/KKKKhazix/khazix-skills/tree/2b4a645cfdc894156ae347d897723562f719ce95/neat-freak) | 对齐项目文档、agent 规则、获准维护的记忆及工作区残留 | 上游安装 ★ | 上游安装 ★ |
| **code-simplifier** | [Anthropic](https://github.com/anthropics/claude-plugins-official) | 代码简化与重构 agent | 原生插件 ★ | — |
| **edit-config** | [本仓库](skills/edit-config/SKILL.md) | 查询和管理 agent-config-for-agents 的配置，两端共用 | 内置 skill ★ | 内置 skill ★ |

### Integrations · 开发集成

| 项目 | 来源 | 功能 | Claude | Codex |
| --- | --- | --- | --- | --- |
| **context7** | [Upstash](https://github.com/upstash/context7) | 查询最新库文档 | 原生插件 ★ | 插件 / MCP ★ |
| **playwright** | [Microsoft](https://github.com/microsoft/playwright-mcp) | 浏览器自动化、E2E 与截图；Codex MCP 固定 0.0.78 | 原生插件 ★ | MCP ★ |

### Design & Content · 设计与内容

| 项目 | 来源 | 功能 | Claude | Codex |
| --- | --- | --- | --- | --- |
| **document-skills** | [Anthropic](https://github.com/anthropics/skills) | 创建和编辑 PDF、DOCX、PPTX、XLSX；优先复用 Codex 已有同等内置能力 | 原生插件 ★ | 内置能力 / 兼容插件 / 源码 ★ |
| **example-skills** | [Anthropic](https://github.com/anthropics/skills) | Claude：12 项示例；Codex：canvas-design、algorithmic-art、mcp-builder 三项 | 原生插件 ★ | 精选源码 ★ |
| **frontend-design** | [Anthropic](https://github.com/anthropics/claude-plugins-official) | 前端视觉与界面设计，examples 整包已提供时复用 | 原生插件 ★ | 插件 / 源码 ★ |
| **humanizer** | [blader](https://github.com/blader/humanizer) | 去除英文写作中的机械化 AI 表达 | 插件 / 源码 ★ | 上游安装 ★ |
| **humanizer-zh** | [op7418](https://github.com/op7418/Humanizer-zh) | 去除中文写作中的机械化 AI 表达 | 上游安装 | 上游安装 |
| **lieflat-charts** | [lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) | Lupi / Basics / Glance / Maps HTML 图表与 12 个双语报告模板；源码不含预览媒体，仅限非商业用途 | 精选源码 | — |

### Slides · 演示文稿

| 项目 | 来源 | 功能 | Claude | Codex |
| --- | --- | --- | --- | --- |
| **frontend-slides** | [zarazhangrui](https://github.com/zarazhangrui/frontend-slides) | 零依赖 HTML 演示文稿，支持 PPT 转换与多种风格 | 原生插件 | 兼容插件 / 源码 |
| **ppt-master** | [hugohe3](https://github.com/hugohe3/ppt-master) | 从 PDF / DOCX / URL / Markdown 生成可编辑 PPTX、形状与动画；首次使用准备运行环境 | 原生插件 | 精选源码 |

### Memory & Lifestyle · 记忆与生活

| 项目 | 来源 | 功能 | Claude | Codex |
| --- | --- | --- | --- | --- |
| **claude-health** | [tw93](https://github.com/tw93/claude-health) | Claude 会话的健康与状态面板 | 原生插件 | — |

### Storage · 存储分析

| 项目 | 来源 | 功能 | Claude | Codex |
| --- | --- | --- | --- | --- |
| **storage-analyzer** | [khazix-skills（定制）](https://github.com/KKKKhazix/khazix-skills/tree/fcba3adcf5def1ccd4bb688de93060227471b129/storage-analyzer) | 只读磁盘分析、交互 HTML 报告与受保护的清理入口；包含 Linux 支持和安全修复 | 内置 skill | 内置 skill |

### Academic Research · 学术研究

| 项目 | 来源 | 功能 | Claude | Codex |
| --- | --- | --- | --- | --- |
| **paper-reading** | [本仓库](skills/paper-reading/) | 论文阅读、图表提取、证据检查与 HTML 报告 | 内置 skill ★ | 内置 skill ★ |
| **AI Research skills** | [AI Research](https://github.com/Orchestra-Research/AI-research-SKILLs) | 一个整包：分词、微调、后训练、推理服务、分布式训练与优化；[两端共用 31 项成员](catalog.md#ai-research-members) | 6 个原生插件 | 6 个兼容插件 / 源码 |
| **deepxiv-cli** | [DeepXiv](https://github.com/DeepXiv/deepxiv_sdk) | arXiv / PMC 论文混合检索与阅读 CLI | 精选源码 | 精选源码 |
| **deepxiv-trending-digest** | [DeepXiv](https://github.com/DeepXiv/deepxiv_sdk) | 近期热门论文的 Markdown 摘要 | 精选源码 | 精选源码 |
| **deepxiv-baseline-table** | [DeepXiv](https://github.com/DeepXiv/deepxiv_sdk) | 基于研究论文生成基线对比表 | 精选源码 | 精选源码 |
| **ResearchStudio Idea** | [Microsoft](https://github.com/microsoft/ResearchStudio) | idea_spark、paper_search、scoop_check；完整源码，首次使用准备依赖 | 精选源码 | 精选源码 |
| **ResearchStudio Reel** | [Microsoft](https://github.com/microsoft/ResearchStudio) | paper2assets、paper2poster、paper2video、paper2blog、paper2reel，独立选择 | — | 精选源码 |

### MCP Servers · MCP 服务

| 项目 | 来源 | 功能 | Claude | Codex |
| --- | --- | --- | --- | --- |
| **OpenAI docs** | [OpenAI](https://developers.openai.com/mcp) | OpenAI 官方开发文档 | — | MCP ★ |


完整包成员见 [catalog.md](catalog.md#members)，源码 revision 与适配见 [sources.md](platforms/sources.md)。存储分析的定制记录在 [UPSTREAM.md](skills/storage-analyzer/UPSTREAM.md)，已通过 [khazix-skills#50](https://github.com/KKKKhazix/khazix-skills/pull/50) 提交上游。Context7、Playwright 统一放在开发集成，不重复列为独立 MCP 选项。

## 目录结构

```text
.
├── README.md / README.zh-CN.md   # 用户指南与分类表格
├── AGENTS.md / CLAUDE.md         # 本仓库的工作指令
├── INSTALL.md                   # Agent 引导的安装与更新
├── MAINTAIN.md                  # Agent 修改本仓库的流程
├── catalog.md                   # ID、支持范围、推荐与渠道
├── skills/                      # 自有及定制 skill 的完整源码
├── platforms/
│   ├── claude/                  # Claude 指令、lessons、规则、hooks、skills
│   ├── codex/                   # Codex 指令、lessons、设置、skills
│   └── sources.md               # 外部 revision、成员与适配
├── scripts/                     # 受控文件操作与专用小工具
├── lessons.md                   # 本仓库的项目纠错历史
├── docs/                        # 示例、方案与历史迁移记录
└── install.sh / install.ps1     # 指向 INSTALL.md 的兼容提示
```

## 关键机制

- **对话选型**：完整编号列表、用途解释与用户选择记录。插件、MCP 使用目标 agent 的原生工具管理；自管文件通过受控复制和局部合并部署。
- **独立记忆**：Claude 使用自己的全局 `lessons.md` 与项目 `memory/MEMORY.md`；Codex 使用自己的全局 `lessons.md` 与项目根目录 `lessons.md`。模板和真实历史各自保留，仅在缺少全局记录时创建空白文件。
- **规则与状态栏**：Claude 提供一份写作规则，以及独立的 Python / TypeScript / Go 规则；渐变状态栏展示模型、目录、venv、Git、上下文与用量。Codex 使用原生状态栏与子 agent 能力，本仓库不再安装自定义角色预设。
- **分支配置管理**：edit-config 跟踪 agent-config-for-agents 并记录实际 revision；来源策略冲突时明确选择是否迁移，保留已有选择与定制。安装与维护不需要旧 Claude/Codex 分支。
- **限定修改范围**：保留用户定制、凭据、hooks 和记忆数据库，通过备份与文件归属支持更新和明确移除。ResearchStudio Idea/Reel、PPT Master 只准备完整源码，运行依赖留到首次使用。

## 默认设置

下表来自当前模板，仅在选择对应项时应用。已有覆盖值会保留并报告差异。基础设置、权限、状态栏、lessons 分开选择；关闭 Codex 自动导入是安装前提。Agent 会先核实本机版本是否支持相关设置。

| Agent | 配置键 | 模板值 | 作用 |
| --- | --- | --- | --- |
| Claude | `model` / `effortLevel` | `opus` / `xhigh` | 模型与推理强度 |
| Claude | `tui` | `fullscreen` | 全屏终端界面 |
| Claude | `env.CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | `1` | 开启 agent teams 实验功能 |
| Claude | `env.CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` | `1` | 在支持的模型上请求固定思考预算 |
| Claude | `permissions.defaultMode` | `auto` | 独立权限模板还包含宽泛的工具放行规则 |
| Codex | `model` / `model_reasoning_effort` | `gpt-5.6-sol` / `max` | 模型与推理强度 |
| Codex | `web_search` | `live` | 实时网络搜索 |
| Codex | `features.multi_agent` / `concurrent_reasoning_summaries` | `true` / `false` | Agent 协作与摘要行为 |
| Codex | `shell_environment_policy.inherit` | `all` | 继承 shell 环境 |
| Codex | `approval_policy` / `sandbox_mode` | `never` / `danger-full-access` | 单独选择的高自主权限 |
| Codex | `desktop.external-agent-import-sync-enabled` | `false` | 安装内容由明确选择控制 |

实际配置及逐项操作见 [Claude](platforms/claude/README.md#configuration) · [Codex](platforms/codex/README.md#configuration)，当前平台验证范围见 [迁移说明](docs/migration.md)。

## 自定义

你可以直接让 agent 维护仓库本身。它会遵循 [MAINTAIN.md](MAINTAIN.md)，修改完整内容和安装办法，并同步目录与两份 README。

| 请求示例 | Agent 负责修改的内容 |
| --- | --- |
| “加上这个 skill，说明什么时候用” | 自有 skill 保存源码，第三方原版记录上游安装配方，并维护平台支持、分类与用途 |
| “更新 ResearchStudio” | 记录的上游 revision、成员和必要适配，在隔离环境验证 |
| “修改这个 skill / 删除这个选项” | 当前源码与引用；删除记录说明旧 ID 的处理，不静默卸载用户副本 |
| “Claude / Codex 推荐这些 skills” | 仅修改对应 agent 的作者推荐标记 |
| “添加一种语言规则” | `platforms/claude/templates/rules/<lang>/` 及目录条目 |
| “调整 Claude / Codex 指令或 lessons 策略” | 对应 agent 的模板与配套记忆规则 |

查询和修改已安装的配置时使用 [edit-config](skills/edit-config/SKILL.md)，修改操作遵循 [INSTALL.md](INSTALL.md)。根目录 AGENTS.md、CLAUDE.md、lessons.md 属于本仓库；待部署的全局文件在各平台的 templates 中。

## 致谢

- [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) — Anthropic Academy 官方课程
- [为 10 个 Claude Code 打工](https://mp.weixin.qq.com/s/9qPD3gXj3HLmrKC64Q6fbQ) by 胡渊鸣 — 多实例并行实践
- [Harness Engineering](https://openai.com/index/harness-engineering/) by OpenAI
- [Anthropic Engineering](https://www.anthropic.com/engineering) / [OpenAI Engineering](https://openai.com/news/engineering/)
- [Claude Code Best Practice](https://github.com/shanraisshan/claude-code-best-practice) by shanraisshan
- [Claude How To](https://github.com/luongnv89/claude-howto) by luongnv89

## License

本仓库采用 MIT 许可，内置和获取的第三方组件保留各自许可。**lieflat-charts** 使用 [PolyForm Noncommercial 1.0.0](https://github.com/larashero3-dotcom/lieflat-charts/blob/main/LICENSE)，仅限非商业用途；只有选择后才从上游获取，本仓库不做再分发。
