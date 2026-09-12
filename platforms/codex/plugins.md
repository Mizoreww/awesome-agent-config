# Codex 插件选择与安装

为所选条目确定渠道时读取本页。2026-09-12 依据 [OpenAI 插件说明](https://developers.openai.com/codex/plugins)、[官方更新记录](https://learn.chatgpt.com/docs/changelog)及 Codex CLI 0.153.4 核实。App / CLI 支持插件；IDE extension 当前不支持。账号、登录方式和 client 会影响可见目录，API key 登录可能缺少需要 OAuth 的插件。

区分来源身份：**OpenAI 官方**由 OpenAI 发布；**OpenAI curated**可收录第三方作者；**上游 Codex 包**由原作者提供 Codex manifest；**兼容插件**由 Codex 读取上游 Claude 格式。原生命令安装成功不代表实际 skill、MCP 或 hooks 已加载。

## 1. 查询当前能力

```sh
codex plugin --help
codex plugin list --json
codex plugin list --available --json
codex plugin marketplace list --json
```

按实际目标 home 执行。先复用满足范围的已安装/内置能力；待授权与已可用分开记录。安装后从新会话的 skill 列表或工具状态验证实际加载、完整资源和调用名，不能仅检查 enabled。原生 skill 可能使用 `插件名:skill名`，记录实际名称。

## 2. OpenAI 目录中的能力

| Catalog ID | 优先渠道 | 选择与验证 |
| --- | --- | --- |
| documents | OpenAI 的 documents、pdf、presentations、spreadsheets | 核实四种能力在目标 client 可用后复用；本次可见的 runtime 来源为 openai-primary-runtime，它是客户端提供的目录，不是要用户复制的 cache 路径。缺少覆盖时用下表 Anthropic 四件套 |
| superpowers | OpenAI curated 的 Superpowers（作者 Jesse Vincent / obra） | 从当前列表选择 superpowers@openai-curated 或 superpowers@openai-api-curated；核对[十四个成员](../../catalog.md#members)与版本约束，不重复装 obra 源码 |
| github | OpenAI 发布的 GitHub 插件 | 当前目录存在 github@openai-curated 时优先选择；检查 connector 在目标 client 的可用性并完成原生授权。API key 目录未必提供它；已有可用 GitHub 集成先复用，否则走[官方 GitHub MCP](README.md#mcp) |

官方目录由客户端/账号提供，使用列表返回的确切 selector：

```sh
codex plugin add <exact-selector-from-the-list> --json
codex plugin list --json
```

App 可通过 Plugins 页面、CLI 可通过 `/plugins` 查看官方目录。CLI 0.153.4 会拒绝 `plugin marketplace add openai/plugins`，提示 `openai-curated` 是保留名称；不把这条命令作为官方目录安装步骤，也不重命名官方目录来绕过。没有匹配条目时说明可用范围，使用本仓库已有后备渠道。

GitHub 官方插件使用 connector，和直接配置 GitHub MCP 的授权入口不同；选型时说明所用入口，不重复创建连接。`openai-docs` 继续使用官方文档 MCP；OpenAI Developers 插件额外包含 API key、Agents SDK、Apps 开发等能力，不用它自动替换只选文档的用户范围。

## 3. 第三方原生与兼容插件

| Catalog ID | 原生 selector | Marketplace 来源 | 范围与验收 |
| --- | --- | --- | --- |
| documents | document-skills@anthropic-agent-skills | anthropics/skills | Anthropic 兼容包；实际加载 pdf、docx、pptx、xlsx 四项，资源完整 |
| frontend-slides | frontend-slides@frontend-slides | zarazhangrui/frontend-slides | 上游兼容包；实际加载一项，包含完整模板、脚本与引用 |
| ai-research | [六个 selector](../sources.md#ai-research) | Orchestra-Research/AI-research-SKILLs | 上游兼容包组合；一个选择，六个组件，实际加载 31 项 |
| karpathy | andrej-karpathy-skills@karpathy-skills | forrestchang/andrej-karpathy-skills | 上游兼容包；核对 karpathy-guidelines 及资源 |
| frontend-design | frontend-design@claude-plugins-official | anthropics/claude-plugins-official | Anthropic 兼容包；实际加载 frontend-design，已有提供方则复用 |
| context7 | context7@claude-plugins-official | anthropics/claude-plugins-official | Upstash 兼容包；包含 HTTP MCP，另验证实际连接及环境变量展开；连接未通过不能标记可用 |

只添加所选 marketplace。存在 [sources.md](../sources.md) 的 revision 约束时使用它；已存在的 marketplace 先核对来源、ref 与其他选择，不能为新条目悄悄改变既有版本策略。

```sh
codex plugin marketplace add <repository> --ref <recorded-revision> --json
codex plugin list --available --json
codex plugin add <exact-selector-from-the-list> --json
codex plugin list --json
```

没有固定 revision 的 marketplace 省略 `--ref`，安装前核对当前 manifest 并记录实际 revision。有固定约束时验证 marketplace 和最终插件源码都匹配；入口中的嵌套 Git 来源可能另取版本。AI Research 逐个执行六个 selector，仅安装这六组；组合记录与失败续装遵循 [INSTALL](../../INSTALL.md)。

## 4. 继续使用源码或 MCP 的条目

| 条目 | 当前原因与渠道 |
| --- | --- |
| Humanizer | 3.0.0 上游 manifest 指定 `skills: ["./"]`；CLI 0.153.4 显示 installed，但实际加载忽略根目录入口。使用[上游源码](../sources.md#writing)；以后确实加载成功才能改为插件优先 |
| PPT Master | 同样使用根目录 skill 入口；此外 marketplace 的嵌套 git-subdir 未固定 revision，实装资源与记录版本不同。保持[固定源码](../sources.md#slides)，业务依赖留到首次调用 |
| Matt | Codex 固定 v1.1.0 快照没有可用 marketplace，工作流二十项与 code-review 的选择边界也需保留；使用[精选源码](../sources.md#matt) |
| examples | 原生 Claude 整包包含十二项，Codex 精选三个成员；按[明确范围](../sources.md#anthropic)获取源码 |
| Playwright | 可见的 Claude 兼容插件使用 @playwright/mcp@latest，不能满足本仓库 0.0.78 和旧 Node launcher 约束；保留[原生 MCP](README.md#mcp) |
| Humanizer-zh / neat-freak / DeepXiv / ResearchStudio | 已核对的上游 revision 没有对应可用插件入口；保留[上游安装配方](../sources.md)，ResearchStudio 仅准备源码和适配 |
| OpenAI docs | 使用[原生 MCP](README.md#mcp)，保持文档专用范围 |

自有与定制 skills 继续由本仓库提供完整源码。上述结论是当前兼容性约束；维护者要求升级时重新核对对应上游。网络失败不静默切换渠道，不制造本仓库 wrapper 冒充上游插件。
