# 完整安装目录

本文件定义当前仓库的完整能力、稳定 ID、平台支持和作者推荐；安装与维护直接使用当前内容。最后两列分别维护 Claude / Codex 推荐。本轮按作者要求从最新远端安装菜单默认项整理，来源与映射见[推荐依据](#recommendations)；名单待作者最终确认，展示时注明这是推荐草案。

本文件供 agent 读取。面向用户时，按用户语言直接在当前对话展示目标 agent 的完整目录：保留分类，跨分类连续编号，只读当前目标的平台列，附用途、作者推荐和实际已安装状态。平台列“—”的项不进入该目标选择。写着“由某包提供”的行是成员提示，不占第二个可安装编号。依赖未准备时显示前提；不要隐藏受支持的选装项。按 [INSTALL 的选型交互](INSTALL.md#choose-options)优先使用真实多选问答，或在对话接收多个编号；未要求导出时不另建选型文档。其余安装行为由 [INSTALL.md](INSTALL.md) 定义；修改目录和来源按 [MAINTAIN.md](MAINTAIN.md) 同步两份 README 与操作说明。

“原生插件”使用该 agent 的原生命令；兼容包仍需核实当前 manifest、所需 hooks/MCP 与 client 支持。目录并不宣称每个外部包已在所有 OS 验收。共用名字也不意味着两平台必须选同一渠道。

第三方原版由上游分发，这里记录安装方式；本仓库只保存作者自有或明确维护的定制 skills。handoff 是 Matt 包成员，不单独编号或维护副本。

## Core · 基础配置

| ID | 安装项与用途 | Claude | Codex | Claude 推荐 | Codex 推荐 |
| --- | --- | --- | --- | --- | --- |
| instructions | 全局指令（Claude 的 CLAUDE.md / Codex 的 AGENTS.md） | [平台配置](platforms/claude/README.md#configuration) | [平台配置](platforms/codex/README.md#configuration) | 推荐 | 推荐 |
| settings | 基础模型、推理和运行设置；不附带启用插件/MCP | [平台配置](platforms/claude/README.md#configuration) | [平台配置](platforms/codex/README.md#configuration) | 推荐 | 推荐 |
| permissions | 旧版本的高自主权限配置；仅用于用户选择的可信环境 | [平台配置](platforms/claude/README.md#configuration) | [平台配置](platforms/codex/README.md#configuration) | 推荐 | 推荐 |
| rules-writing-style | 清晰、准确的写作规则；完整英文要求及示例 | [平台配置](platforms/claude/README.md#configuration) | — | 推荐 | — |
| statusline | 终端状态栏；Claude 渐变脚本与字体 / Codex 原生 footer | [平台配置](platforms/claude/README.md#configuration) | [平台配置](platforms/codex/README.md#configuration) | 推荐 | 推荐 |
| lessons | 空白全局纠错记录；保留现有真实记录 | [平台配置](platforms/claude/README.md#configuration) | [平台配置](platforms/codex/README.md#configuration) | 推荐 | 推荐 |

## Language Rules · 语言规则

| ID | 安装项与用途 | Claude | Codex | Claude 推荐 | Codex 推荐 |
| --- | --- | --- | --- | --- | --- |
| rules-python | Python 规则 | [平台配置](platforms/claude/README.md#configuration) | — | — | — |
| rules-typescript | TypeScript 规则 | [平台配置](platforms/claude/README.md#configuration) | — | — | — |
| rules-golang | Go 规则 | [平台配置](platforms/claude/README.md#configuration) | — | — | — |

## Review · 审查

| ID | 安装项与用途 | Claude | Codex | Claude 推荐 | Codex 推荐 |
| --- | --- | --- | --- | --- | --- |
| claude-pr-review | Claude 官方 code-review：PR 审查 | [原生插件](platforms/claude/README.md#plugins) | — | 推荐 | — |
| matt-code-review | Matt code-review：Standards / Spec 双轴审查；Claude 已包含在 Matt 包中 | [由 matt-workflow 提供](#members) | [固定源码](platforms/sources.md#matt) | — | 推荐 |
| adversarial-review | 跨模型审查；与 Claude 内调用 Codex 的方式择需使用 | [本地 skill](platforms/claude/README.md#local-skills) | — | 推荐 | — |
| codex-in-claude | OpenAI codex-plugin-cc：在 Claude 中调用 Codex | [原生插件](platforms/claude/README.md#plugins) | — | — | — |

## Workflow · 工作流

| ID | 安装项与用途 | Claude | Codex | Claude 推荐 | Codex 推荐 |
| --- | --- | --- | --- | --- | --- |
| karpathy | Karpathy 编码准则 | [原生插件](platforms/claude/README.md#plugins) | [原生插件](platforms/codex/README.md#plugins)；[固定源码](platforms/sources.md#karpathy) | 推荐 | 推荐 |
| superpowers | Superpowers 完整工作流包；成员见下方 | [原生插件](platforms/claude/README.md#plugins) | [原生插件](platforms/codex/README.md#plugins) | — | — |
| matt-workflow | Matt 工作流；两平台保留各自范围，成员见下方 | [原生插件](platforms/claude/README.md#plugins) | [固定源码](platforms/sources.md#matt) | 推荐 | 推荐 |
| neat-freak | 知识、文档与工作区收尾 | [上游安装](platforms/sources.md#writing) | [上游安装](platforms/sources.md#writing) | 推荐 | 推荐 |
| code-simplifier | 代码简化与重构 agent | [原生插件](platforms/claude/README.md#plugins) | — | 推荐 | — |
| edit-config | 查询、增删改、修复与更新配置；两端共用，跟踪 agent-config-for-agents | [共享 skill](platforms/claude/README.md#local-skills) | [共享 skill](platforms/codex/README.md#local-skills) | 推荐 | 推荐 |

## Integrations · 开发集成

| ID | 安装项与用途 | Claude | Codex | Claude 推荐 | Codex 推荐 |
| --- | --- | --- | --- | --- | --- |
| context7 | 查询最新库文档 | [原生插件](platforms/claude/README.md#plugins) | [原生插件](platforms/codex/README.md#plugins)；[HTTP MCP](platforms/codex/README.md#mcp) | 推荐 | 推荐 |
| playwright | 浏览器自动化与 E2E | [原生插件](platforms/claude/README.md#plugins) | [固定版本 MCP](platforms/codex/README.md#mcp) | 推荐 | 推荐 |

## Design & Content · 设计与内容

| ID | 安装项与用途 | Claude | Codex | Claude 推荐 | Codex 推荐 |
| --- | --- | --- | --- | --- | --- |
| documents | 文档四件套：pdf、docx、pptx、xlsx | [原生插件](platforms/claude/README.md#plugins) | 已有内置能力优先；[原生兼容插件](platforms/codex/plugins.md)；[源码后备](platforms/sources.md#anthropic) | 推荐 | 推荐 |
| examples | Claude 示例全包 / Codex 精选三个；成员见下方 | [原生插件](platforms/claude/README.md#plugins) | [固定源码](platforms/sources.md#anthropic) | 推荐 | 推荐 |
| frontend-design | 前端视觉设计；已装 examples 整包时不重复 | [原生插件](platforms/claude/README.md#plugins) | [原生插件](platforms/codex/README.md#plugins)；[固定源码](platforms/sources.md#anthropic) | 推荐 | 推荐 |
| humanizer | 英文写作去除机械表达 | [原生插件](platforms/claude/README.md#plugins)；[上游源码](platforms/sources.md#writing) | [上游安装](platforms/sources.md#writing) | 推荐 | 推荐 |
| humanizer-zh | 中文写作去除机械表达 | [上游安装](platforms/sources.md#writing) | [上游安装](platforms/sources.md#writing) | — | — |
| lieflat-charts | HTML 图表模板；PolyForm Noncommercial 1.0.0 | [固定源码](platforms/sources.md#lieflat) | — | — | — |

## Slides · 演示文稿

| ID | 安装项与用途 | Claude | Codex | Claude 推荐 | Codex 推荐 |
| --- | --- | --- | --- | --- | --- |
| frontend-slides | HTML slides 与 PPT 转换 | [原生插件](platforms/claude/README.md#plugins) | [原生兼容插件](platforms/codex/plugins.md)；[源码后备](platforms/sources.md#slides) | — | — |
| ppt-master | 可编辑 PPTX；Codex 仅安装必要 skill 源码 | [原生插件](platforms/claude/README.md#plugins) | [固定源码](platforms/sources.md#slides) | — | — |

## Memory & Lifestyle · 记忆与生活

| ID | 安装项与用途 | Claude | Codex | Claude 推荐 | Codex 推荐 |
| --- | --- | --- | --- | --- | --- |
| claude-health | Claude 健康与状态面板 | [原生插件](platforms/claude/README.md#plugins) | — | — | — |

## Storage · 存储分析

| ID | 安装项与用途 | Claude | Codex | Claude 推荐 | Codex 推荐 |
| --- | --- | --- | --- | --- | --- |
| storage-analyzer | 只读存储分析与交互报告 | [本地 skill](platforms/claude/README.md#local-skills) | [本地 skill](platforms/codex/README.md#local-skills) | — | — |

## Academic Research · 学术研究

| ID | 安装项与用途 | Claude | Codex | Claude 推荐 | Codex 推荐 |
| --- | --- | --- | --- | --- | --- |
| paper-reading | 论文阅读、证据检查与 HTML 报告 | [本地 skill](platforms/claude/README.md#local-skills) | [本地 skill](platforms/codex/README.md#local-skills) | 推荐 | 推荐 |
| ai-research | AI Research 整包：分词、微调、后训练、推理服务、分布式训练与优化；两端统一 31 项，成员见下方 | [原生插件组合](platforms/claude/README.md#ai-research) | [原生兼容插件组合](platforms/codex/plugins.md)；[源码后备](platforms/sources.md#ai-research) | — | — |
| deepxiv-cli | DeepXiv 论文检索与阅读 | [固定源码](platforms/sources.md#deepxiv) | [固定源码](platforms/sources.md#deepxiv) | — | — |
| deepxiv-trending-digest | DeepXiv 热门论文摘要 | [固定源码](platforms/sources.md#deepxiv) | [固定源码](platforms/sources.md#deepxiv) | — | — |
| deepxiv-baseline-table | DeepXiv 基线对比表 | [固定源码](platforms/sources.md#deepxiv) | [固定源码](platforms/sources.md#deepxiv) | — | — |
| researchstudio-idea | idea_spark、paper_search、scoop_check；最小源码 | [固定源码](platforms/sources.md#researchstudio) | [固定源码](platforms/sources.md#researchstudio) | — | — |
| researchstudio-reel | paper2assets、paper2poster、paper2video、paper2blog、paper2reel | — | [固定源码](platforms/sources.md#researchstudio) | — | — |

## MCP Servers · MCP 服务

| ID | 安装项与用途 | Claude | Codex | Claude 推荐 | Codex 推荐 |
| --- | --- | --- | --- | --- | --- |
| github | GitHub 仓库与 issue 工具；需用户授权 | — | 可用时优先 [OpenAI 官方插件](platforms/codex/plugins.md)；[GitHub MCP](platforms/codex/README.md#mcp) | — | 推荐 |
| openai-docs | OpenAI 官方文档 MCP | — | [MCP](platforms/codex/README.md#mcp) | — | 推荐 |

<a id="members"></a>
## 整包成员

原生插件安装前重新读取上游 manifest。如果成员与下面快照不同，完整告知用户后按其选择继续，不能在更新时静默扩大范围。

- **document-skills**：pdf、docx、pptx、xlsx。
- **Claude example-skills**：algorithmic-art、brand-guidelines、canvas-design、doc-coauthoring、frontend-design、internal-comms、mcp-builder、skill-creator、slack-gif-creator、theme-factory、web-artifacts-builder、webapp-testing。
- **Codex examples 精选**：canvas-design、algorithmic-art、mcp-builder；不装整个 Claude 示例包。
- **Superpowers**：brainstorming、dispatching-parallel-agents、executing-plans、finishing-a-development-branch、receiving-code-review、requesting-code-review、subagent-driven-development、systematic-debugging、test-driven-development、using-git-worktrees、using-superpowers、verification-before-completion、writing-plans、writing-skills。
- **Claude Matt 原生包（1.2.3 快照）**：ask-matt、diagnosing-bugs、grill-with-docs、triage、improve-codebase-architecture、setup-matt-pocock-skills、tdd、to-spec、to-tickets、wayfinder、implement、prototype、research、domain-modeling、codebase-design、code-review、resolving-merge-conflicts、wizard、grill-me、grilling、handoff、teach、to-questionnaire、wait-what、writing-for-agents。
- **Codex Matt v1.1.0 精选**：ask-matt、diagnosing-bugs、grill-with-docs、triage、implement、improve-codebase-architecture、setup-matt-pocock-skills、tdd、to-spec、to-tickets、wayfinder、prototype、domain-modeling、codebase-design、grill-me、grilling、research、teach、writing-great-skills、handoff，共 20 项。code-review 是独立可选项；handoff 仅作为本包成员安装。
- **code-simplifier** 和 **codex-in-claude**：分别包含 agent/commands 等插件能力，按照上游 manifest 说明实际安装范围。

<a id="ai-research-members"></a>
### AI Research 整包

`ai-research` 占一个编号，两端统一包含下面六组、共 31 项。Claude 使用六个上游分类插件，Codex 优先使用同一来源的兼容插件；获取渠道见对应平台说明。分类名只解释成员，不再成为独立安装选项。旧 24 项及部分选择的处理见[迁移说明](docs/migration.md#ai-research)。

| 分组与用途 | Claude / Codex 共用成员（共 31 项） |
| --- | --- |
| 分词（tokenization） | huggingface-tokenizers、sentencepiece |
| 微调（fine-tuning） | axolotl、llama-factory、peft-fine-tuning、unsloth |
| 后训练（post-training） | grpo-rl-training、miles-rl-training、openrlhf-training、simpo-training、slime-rl-training、torchforge-rl-training、fine-tuning-with-trl、verl-rl-training |
| 推理（inference-serving） | serving-llms-vllm、sglang、tensorrt-llm、llama-cpp |
| 分布式（distributed-training） | huggingface-accelerate、deepspeed、pytorch-fsdp2、training-llms-megatron、pytorch-lightning、ray-train |
| 优化（optimization） | awq-quantization、gptq、gguf-quantization、optimizing-attention-flash、quantizing-models-bitsandbytes、hqq-quantization、ml-training-recipes |

历史来源及条目迁移见 [迁移说明](docs/migration.md)，这些记录不限制当前能力的正常维护。Codex 历史 adversarial-review 的源码仍保留，但当前策略使用 Matt code-review，因此不列为 Codex 可安装项。

<a id="recommendations"></a>
## 推荐依据

2026-09-13 按作者要求核对远端快照的交互安装菜单，Bash 与 PowerShell 默认项一致。这里只记录推荐来源；安装、更新与查询不需要获取历史分支。

| Agent | 来源快照 | 当前推荐数 |
| --- | --- | --- |
| Claude | main · d65cbda0058be09e4771f4603ccf45b3a589583b | 20 |
| Codex | codex · fdd3e50aca09d1b80ac416f320f42bc0ecef5faa | 19 |

- 旧 settings/config 默认包含权限设置；拆分后的 `settings` 与 `permissions` 均列为候选推荐。高自主权限仍需用户明确选择可信环境，推荐标记不构成授权。
- Claude 原 `rules-common` 默认项对应新的 `rules-writing-style` 候选；完整内容已按本轮要求替换，旧通用编码规则不恢复。
- 两端的旧更新项对应 `edit-config`；Codex 独立 handoff 已并入原本推荐的 Matt 包，不另计一次。
- 2026-09-17 按作者要求移除 Codex 的 explorer、reviewer、docs-researcher 自定义预设，推荐草案由 22 项减为 19 项；原生子 agent 能力继续可用，旧安装按[迁移说明](docs/migration.md#codex-agent-presets)处理。
- Claude 的 frontend-design 仍按原菜单标记推荐，已选 examples 整包时复用其中成员，避免重复安装。
- AI Research 的六组在两端菜单中均默认关闭，合包后仍不标记推荐。main/settings.json 中启用插件的布尔值不替代交互菜单默认选择。
- Lark / Feishu、Claude-Mem、PUA 已退役，不出现在推荐名单。其他原本关闭的选项继续可选，不因目录改动加入推荐。
