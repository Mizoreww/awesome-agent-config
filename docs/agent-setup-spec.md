# Agent 引导的配置安装方案

2026-09-12。设计决策已通过 grilling 问答确认：用户与已有的 Claude/Codex 对话完成选型和安装。此前的 Go 二进制、终端菜单和通用安装核心提案已撤回。本文件是当前实现的验收依据；Codex 配置由本仓库显式管理。

本仓库是 Claude/Codex 统一的主要开发线。安装、更新与维护只依赖当前仓库内容及所选外部上游。2026-09-17 作者已授权将当前开发成果提升至 main，仓库改名 awesome-agent-config，暂存其他分支并发布 changelog、tag 与 release。

2026-09-13 追加要求：移除 Lark / Feishu MCP、Claude-Mem、PUA 三语言包；删除 Claude 原八个 Common rules，将完整八条写作要求及全部示例译成英文，作为独立 rules/writing-style.md。语言规则仍可单独选择，并清理失效依赖。两端配置查询与增删改统一调用共享 edit-config，明确关联 agent-config-for-agents；查询只读。全面核对目录、模板、来源、安装及更新说明的一致性。

2026-09-17 交互纠正：安装时直接在当前对话展示目标 agent 的完整支持项、用途、作者推荐和安装状态，并优先使用实际可用的多选问答。单选/文本工具接收多个编号；没有问答工具时直接在聊天中提问。不以生成 Markdown、报告或文件链接替代选型；仅用户要求导出时生成文档。推荐名单及安装范围不因交互方式变化而改变。

2026-09-17 预设精简：按作者要求移除 Codex 的 explorer、reviewer、docs-researcher 三个自定义角色预设，包括模板、注册 patch、Core 安装项与推荐。保留原生子 agent 能力及已选审查/文档 skills，现有用户安装按迁移说明处理。

2026-09-17 集成精简：按作者要求从 Claude / Codex 移除 GitHub MCP 安装入口，退役 `github` 条目及其插件替代渠道。保留普通 Git/gh 工作流、审查 skills 和上游源码地址，不改动用户现有凭据或外部连接。活动目录为 39 个 ID，推荐草案为 Claude 20 项、Codex 18 项。

2026-09-17 正式发布：v4.0.0 采用当前 39 个活动 ID 和 Claude 20 / Codex 18 项作者推荐。正式仓库为 Mizoreww/awesome-agent-config，main 作为统一主线；旧 main 保存到 archive/legacy-claude，其他分支统一改为 archive/legacy-<原名称>（原名称中的 / 改为 -），历史 tags/releases 保留。edit-config 及模板更新来源同步至新仓库 main；旧名称按明确别名识别，已有分支、固定或本地策略仍按用户选择迁移。本条取代此前仅在开发分支工作、不执行主线发布的限制。

## 用户入口

README 提供一段可以直接交给 agent 的请求：

> 请阅读这个仓库的 INSTALL.md，默认配置当前对话使用的 agent。检查系统和已有配置后，直接在对话中按分类完整列出这个 agent 支持的安装项，连续编号，标注作者推荐及已安装状态，并解释用途。优先用可用的原生多选问答；否则让我在对话里选择多个编号，不生成单独的选型文档。根据我的选择完成安装、验证和记录；已有明确偏好请直接沿用。

已有 agent 就能开始，无需先安装一个用于安装其他内容的 skill。以后也可以说“给 Codex 增加论文工具”“更新我上次选择的内容”。

README 保留原 main 的双语分类、使用说明、表格、展示示例、目录结构、关键机制、设置、自定义、致谢及许可，合并 Codex 能力并更新已过时的安装说明。分类顺序为 Core、Language Rules、Review、Workflow、Integrations、Design & Content、Slides、Memory & Lifestyle、Storage、Academic Research、MCP Servers；catalog 沿用同一顺序。Codex Core 保留全局指令、基础设置、权限、状态栏与 lessons；训练与推理条目留在 Academic Research。

入口让用户打开 checkout 或分享当前 README 页面 URL；安装沿用该页面的 ref，不写死开发/历史分支，也不丢掉 ref 后静默落回旧默认分支。

## 仓库只维护这些内容

```text
README.md / README.zh-CN.md 给用户的完整分类表格、使用说明与上述入口
AGENTS.md / CLAUDE.md       本仓库的工作说明，按需指向 INSTALL.md
INSTALL.md                 两个 agent 共用的对话安装流程
MAINTAIN.md                Agent 增删改仓库内容时的维护流程
catalog.md                 完整分类目录、两平台作者推荐、来源与安装渠道
platforms/claude/           Claude 操作说明与待部署的配置模板
platforms/codex/            Codex 操作说明与待部署的配置模板
skills/                    自有或定制的完整 skill 源码
scripts/                   确有需要的备份、受控复制、配置合并与校验
```

先用 Markdown 维护目录即可。每项写清用途、适用场景、Claude/Codex 渠道、重要限制、来源和固定版本要求；Claude 与 Codex 的作者推荐标记分别维护。具体命令集中在平台说明里。特殊能力的安装细节按需链接，不让 agent 每次读取所有插件文档。

作者未提供推荐依据的新条目标记留空。推荐依据作者指定的历史 main/codex 安装默认项：核对两个来源快照的 Bash / PowerShell 交互菜单，按现有目录映射及之后明确的退役决定调整。v4.0.0 采用双语 README 中当前 Claude 20 项、Codex 18 项的名单，具体来源 SHA 与映射在 catalog 中；不能用 settings 中的启用值代替菜单默认。查询和安装读取当前目录，无需获取旧分支。

根目录 AGENTS.md/CLAUDE.md 管本仓库的开发与安装工作；要部署到用户 home 的全局指令放在 platforms 下。配置查询与修改由 edit-config 区分目标和操作，普通代码工作不会触发安装；模板在缺少 skill 时提供同一分支工作流的读取入口。查询不写记录、不改配置，也不隐式安装。内容共用的 skills 保留一份源码，平台差异只在确有需要处适配。

源码归属按用户最新选择区分：第三方原版提供第三方上游安装方式，仓库只保存自有 skill 和明确维护的定制衍生版，并保留上游署名。Humanizer、Humanizer-zh、neat-freak 原样副本移出仓库，条目改为从上游安装。paper-reading、storage-analyzer 定制版及 adversarial-review 定制版继续在这里维护。

handoff 不再独立设置，删除独立目录项和本地定制副本，只作为 Matt 包成员提供。Codex 的 Matt 精选范围加入上游 handoff，合计 20 项；其他版本与成员约束保持有效。旧 handoff ID 记录迁移关系，不自动扩大或覆盖已有用户安装。

AI Research 合并为一个 `ai-research` 选项，两端统一使用上游 tokenization、fine-tuning、post-training、inference-serving、distributed-training、optimization 六组完整 31 项。成员按分类列全，优先通过六个原生插件组成一个安装选择；逐组件记录来源、版本、归属和结果。Codex 原 24 项的七项增补已由作者确认进入新目录，但已有用户的旧六组 ID 或部分选择不因此自动扩充；迁移先展示成员差异。

Agent 维护 skills 时同步当前源码、catalog、双语 README 及对应平台/上游安装配方；作者推荐仍由作者决定。历史来源映射用于追溯首次合并，不能限制今后正常的 skills 增删改。稳定 ID 不复用于无关能力；删除或改名在迁移说明中记录，保留已安装用户的选择与归属直到明确迁移或卸载。

## INSTALL.md 的六步流程

1. **检查环境。** 读取本仓库安装说明，核实源码 revision，检测 OS、shell、agent CLI 和目标配置目录，查询已安装能力。默认目标是当前对话的 agent；用户明确要求配置两者时才分别处理。单纯存在目录不代表安装完整。完成条件：目标位置、可用命令与现有能力可明确列出。
2. **了解用途。** 沿用对话中已有偏好，只问会改变解释或选型的问题；能检测的环境信息不用问用户。当前 agent 无法可靠识别时，才补问目标。完成条件：知道给谁装、主要做什么、哪些内容已被用户选定。
3. **在对话中完整展示并确定选择。** 仅展示该目标支持的安装项，保留分类并跨分类连续编号，标注“作者推荐”和实际安装状态，每项附简短用途说明。按 INSTALL 的选型交互使用可用的原生多选问答或接收多个编号，遵守当前模式与工具 schema。Agent 可结合用途解释依赖、重叠与取舍，不用自己的精简推荐或生成文档替代对话中的完整目录。完成条件：已收到可映射到目标和稳定 ID 的实际选择。缺少选择时等待回复，预选、空回复或超时不算授权；用户已授权具体选择时直接继续。
4. **选择平台渠道。** 只读取所选平台和能力的安装说明，核对当前 CLI 支持的命令及来源。完成条件：每项都有已核实的安装办法和目标路径；缺少支持的项说明原因，不猜命令。
5. **执行安装。** 先记录选择、原状态和备份位置，再运行原生命令或受控文件操作。已满足的能力复用；来源和版本约束保持不变。完成条件：每项都有实际操作结果，失败不会被写成成功。
6. **验证与交接。** 查询原生安装状态，检查 skill 的完整资源与适用的 MCP/入口，区分已安装、待授权和失败。保存简短安装记录并告知结果；更新只处理已选内容。完成条件：记录与实际状态一致，未完成项清楚可操作。

普通选择通常用一两轮问答即可；用户想了解某项时展开解释。真正多选工具按容量分批，编号保持稳定，累计选择直到所需批次完成；用户给出完整选择时直接结束剩余提问。仅有单选/文本工具时用一个问题接收多个编号，不逐项追问。交互细节集中在 INSTALL，问答结束不额外增加一次确认。

编号对应目录定义的安装单位：整包插件占一个编号，并列出其成员；AI Research 这样的组合包也占一个编号，映射多个原生插件或完整源码成员；独立 skill 单独编号。用户只想要包内少数成员时，说明原生整包与精选源码的差异，再按其选择执行。显示编号仅用于当前目录，安装记录保存稳定的条目标识和来源，避免下次目录变化后编号错位。

两个 agent 都被明确选中时，分别显示各自的完整目录和作者推荐，选择中注明目标。再次展示目录时，用户报出的编号默认表示新增或更新；此前已装但未提到的项继续保留。明确请求移除时才执行卸载。

## 平台与渠道规则

- 新安装优先采用该 agent 上游支持的原生插件，再考虑经验证兼容插件和自有/精选 skills。这里的“原生”指安装机制，第三方作者身份如实说明。
- 仅支持 Claude 的插件不列入 Codex 的可选清单；已维护 Codex skill 实现的同类能力可单独介绍。插件 manifest 可被发现，不代表 hooks、工具和资源完整可用。
- 已有内置或外部能力满足需求时优先复用。整包会带来哪些成员应在选型时解释；避免同时装整包和其中相同的独立 skills。
- Codex App/CLI 共用 home 时只安装一次；仅 App 提供的能力不能推断 CLI/IDE 已具备。目标 client 按用户实际用途确定。WSL 和 Windows 配置分开管理。
- 自有 skills 源码共享，安装到各 agent 的目录。Codex 自管内容继续放在其 Codex home，默认 `~/.codex/skills`；不以 `~/.agents/skills` 为权威副本。
- `npx` 只在选定能力的上游安装方式或运行方式需要时使用；用户不必先学习不同渠道，再决定自己该运行哪条命令。
- 上游支持或命令变化时，agent 查询官方说明并核对本地 CLI。固定版本、精选成员和本仓库的必要适配保持有效，不能顺手升级到 latest。

Codex 尽量采用官方目录与可用插件：明确区分 OpenAI 发布、OpenAI curated 中的第三方作者、上游 Codex 专用包、Claude 格式兼容插件。从实际目录读取 selector，兼容性结论包括实际加载和完整资源，不能只凭 installed/enabled。可复用 OpenAI 文档能力时优先复用；其余文档四件套、frontend-slides、AI Research 使用已验证的上游兼容包。

无法满足范围、版本或入口约束的条目保留明确后备路径：Matt 固定精选、Codex examples、Humanizer、PPT Master 及没有插件入口的研究/写作 skills 使用上游源码，Playwright 保持固定 MCP，OpenAI 文档 MCP 不被更大的 Developers 插件替换。维护理由与具体配方集中在 platforms/codex/plugins.md，账号不可见的官方插件不宣称已验证可用。

## 保留的可靠性措施

Agent 负责理解需求、选型解释、查阅平台说明和处理异常。插件安装/更新/卸载交给原生 CLI；文件操作中反复出现且容易出错的部分，才从现有安装脚本提取小工具。每个工具承担一个明确动作，不新增菜单、推荐系统、通用 resolver 或自更新框架。

保留现有有用的保护：配置局部合并、备份、文件归属和修改检查、完整资源校验。真实 lessons、凭据、未受管 hooks/skills 及记忆数据库保持原样；只在缺少全局 lessons 时创建目标 agent 的空白模板。Claude 的 CLAUDE.md / lessons 与 Codex 的 AGENTS.md / lessons 独立维护。Claude 项目纠错写入其项目 memory/MEMORY.md；Codex 项目纠错写入项目根目录 lessons.md。Codex lessons 由 AGENTS 明确读取，不借 `model_instructions_file` 替换内置指令。

每个 agent home 下留一份简短安装记录，保存选择、来源/revision、受管文件及部署 hash、备份位置、待完成项。原生插件版本以原生查询为准；这份记录用于后续对话和文件保护，不实现另一套插件数据库。操作中断后先核对原生状态，归属不明的内容保留；卸载也只针对归属明确且用户要求移除的内容。

仓库来源记录包含 URL、解析后的 revision 和 branch / default-branch / pinned / local 更新策略；具体字段定义在 INSTALL。共享 edit-config 明确使用 Mizoreww/awesome-agent-config 的 main 分支，替代旧 update-config / update_config。仓库改名别名及策略处理遵循 docs/migration.md 的主线迁移；匹配 main 的 branch / default-branch 策略可续用，default-branch 仍保留该策略。缺失来源时使用 skill 的明确目标；其他 fork、分支（含旧开发分支）、固定或本地策略按明确迁移选择处理，不能静默覆盖。已有选择、文件归属和来源历史保持可追溯。新版本中已消失的 ID 需提示退役或迁移，不能被当作更新成功或自动删除。

Codex 的 Matt 包继续固定现有 commit，包含其上游 handoff，原生迁移经过入口、资源和所选成员验证后再采用。Playwright 保留固定版本、旧 Node 的兼容路径和 MCP initialize 检查。ResearchStudio Idea/Reel 与 PPT Master 按已有约定仅安装必要源码，依赖由首次调用准备。

## 实施验收

- 将已审查的统一开发成果快进到 main，并以其提交发布 v4.0.0 tag 和正式 GitHub release。仓库改名 awesome-agent-config；旧 main 的 d65cbda0058be09e4771f4603ccf45b3a589583b 保存到 archive/legacy-claude，其他分支改为 archive/legacy-<原名称>（原名称中的 / 改为 -），保留历史 tags/releases，不改写已有历史。
- 当前仓库独立保存自有和保留的定制 skill payload；未退役的第三方原版与外部 skill 组均有上游安装说明，不从历史 Claude/Codex 分支安装或更新。
- handoff 仅在 Matt 包中；AI Research 六组归为一个 31 项安装选择，活动目录共 39 个 ID；退役集成（含两端 GitHub MCP）、Common rules、旧更新入口、Codex 角色预设及 24 项范围在迁移说明中有明确处理。
- Codex 不再提供三个自定义角色的模板或注册 patch；基础配置保留原生多 agent 功能，不安装替代角色或改动已有用户的 agents 目录。
- Claude 写作 rule 包含八条完整英文要求、全部替换示例、统一中性状态标签、条目可独立陈述事实、未知原因及已验证结论的处理；CLAUDE 模板不重复保存缩略版。原 Common 文件全部移除，语言规则无悬空引用。
- edit-config 在两端模板中可自动触发配置查询与增删改，安装到各自 skills/edit-config；本仓库仅保留一份源码。查询和修改、仓库和已安装内容分别处理，版本与来源校验遵循明确分支。
- Codex 原生优先渠道通过当前 CLI、实际 skill 加载和完整资源核实；官方目录受账号/client 限制，失败、待授权和待首次使用准备分别记录。组合包部分失败时保留成功组件，只续装未完成项。
- 双语 README 保留原有 11 类和完整说明/表格；catalog 的稳定 ID、支持范围、来源和推荐与之相符。
- README、根指令、catalog 和 edit-config 均指向对话内选型；当前 agent 的完整选项、用途、推荐与状态实际出现在聊天中。支持多选的工具按 schema 使用并覆盖全部选项；单选/无工具模式接受多个编号。未收到选择不安装，未要求导出不生成选型或安装报告文件。
- 根指令能将仓库增删改路由到 MAINTAIN，将用户安装变更路由到 INSTALL；历史 provenance 不充当当前不可修改的清单。
- Claude/Codex 分别使用独立指令和 lessons 模板，现有真实记录保持不变。
- 作者推荐按指定的默认菜单来源核对，发布采用当前 Claude 20 / Codex 18 项；权限拆分、Common 替换、handoff 合包及旧更新入口改名的映射明确，推荐不扩大用户已选范围。
- 本地文件保护、原生插件与最小源码安装在隔离配置目录验证；当前文件导出到没有 .git / 旧 refs 的目录后，相关模板和共享 skill 安装仍可完成。
- 保留相关既有测试；临时新验收脚本不加入发布分支。
