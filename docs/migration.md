# 历史合并与迁移说明

首次合并从 main `d65cbda0058be09e4771f4603ccf45b3a589583b`（3.2.0）建立开发分支，纳入 codex `fdd3e50aca09d1b80ac416f320f42bc0ecef5faa`（2.11.0）的能力。以下来源名称和 SHA 记录这次历史合并，不是安装依赖。

当前仓库是统一维护的依据；旧分支今后归档也不影响安装和维护。本次不执行分支归档或默认分支切换。实际源码、平台配方和 catalog 可按 [MAINTAIN.md](../MAINTAIN.md) 演进，无需再与历史分支同步。

## 本地 skill 覆盖

首次合并时，main 的 7 个与 codex 的 8 个本地 skill 目录映射为 10 个目录；两端相同的五份共用副本。下表记录初始落点，之后的第三方源码调整与 handoff 合并见下方“当前源码归属”和“条目退役与改名”。

| 来源 | 初始位置 | 首次合并时的处理 |
| --- | --- | --- |
| 两端 humanizer、humanizer-zh、neat-freak、paper-reading、storage-analyzer | skills/同名目录 | 两端原始文件完全相同，保留共同副本 |
| main adversarial-review | platforms/claude/skills/adversarial-review | 保留 main 专属全文与 references |
| codex adversarial-review | platforms/codex/skills/adversarial-review | 保留历史全文与 references；Codex 当前审查策略采用 Matt code-review，因此不列为可安装项 |
| codex handoff | platforms/codex/skills/handoff | 首次保留定制版本；现按用户选择改为 Matt 上游成员 |
| main update-config | platforms/claude/skills/update-config | 保留调用名，入口改为对话维护 |
| codex update | platforms/codex/skills/update | 保留 update_config 调用名，入口改为对话维护 |

[source-provenance.json](source-provenance.json) 记录首次合并时 125 项原始文件映射及 Git blob ID，覆盖 skill、配置、规则、字体、hooks 和两端历史 changelog。当时未标 adaptation 的文件经过逐字节核对；记录中的路径与适配说明描述首次合并状态。它是历史快照，不要求后续版本仍与旧 blob 相等，也不参与安装校验。

root lessons.md 保留本仓库纠错历史，安装使用各自 platforms/claude/templates/lessons.md 和 platforms/codex/templates/lessons.md 的空白模板。历史映射中的 shared global-lessons 路径已由这两个模板替代；真实全局日志不会随模板变化被替换。

## 当前源码归属

| 内容 | 当前维护方式 |
| --- | --- |
| paper-reading、两端更新 skill | 自有源码保存在本仓库 |
| storage-analyzer、adversarial-review | 保留定制源码及上游署名；Codex 历史 adversarial-review 仍不作为安装项 |
| humanizer、humanizer-zh、neat-freak | 移除原样副本，稳定 ID 与能力保留；从 [第三方上游](../platforms/sources.md#writing) 安装 |
| handoff | 移除独立副本与选择，统一使用 Matt 包中的上游成员 |

已有第三方本地副本不会因仓库移除 vendored 目录而自动卸载。按当前上游配方更新或切换原生插件前，核对原版本、归属和本地修改；原有 Humanizer 2.2.0 升到当前 3.0.0 需说明差异。原样保存 neat-freak 的快照测试随 vendored 目录退役，源码下载与完整资源验证在隔离目录进行。

## 外部获取的能力

本地目录不是安装能力的全集。[catalog.md](../catalog.md) 和 [sources.md](../platforms/sources.md) 还覆盖：

- main settings 中的 20 个原生插件 selector（15 个启用、5 个关闭）加上安装菜单的 Matt 插件，共 21 个可选插件，以及 DeepXiv、ResearchStudio Idea 和 lieflat-charts 源码入口。
- Codex 的 Matt v1.1.0 工作流目前包含上游 handoff 共二十项，另有独立 code-review；Superpowers 十四项；Karpathy；PUA 三项。
- Anthropic 文档四项、Codex examples 精选三项、独立 frontend-design；frontend-slides、PPT Master。
- AI Research 原六组精选（24 项）已全部纳入新的两端统一 31 项整包；另外保留 DeepXiv 三项、ResearchStudio Idea 三项与 Reel 五项，以及既有 MCP 配置能力。

旧脚本的 `LEGACY_CLEANUP_SKILLS`、`MATTPOCOCK_LEGACY_SKILLS` 和已禁用/移除的插件名单属于历史清理规则，不是当时活跃安装项。它们不重新加入可选清单；迁移也不会自动删除用户仍保留的历史内容。

原生包内容会随上游演变。Agent 在展示整包和执行安装时核实 manifest，保留用户所选范围；新增成员需要明确说明。精选源码路径与固定 revision 是可检查的安装依据。

## 配置变化

根目录 AGENTS.md/CLAUDE.md 仅指导本仓库工作；原全局模板移入 platforms。settings、权限、状态栏、记忆 hooks、子 agent 注册和 MCP 分开选择，防止装一项时顺带启用其他能力。

Claude 全局模板按可用 Python 环境和已选审查工作流执行；原指令中的强制 Conda 和固定 review 依赖改为条件规则。Claude 规则、字体与状态栏仍可选择，路径支持实际配置目录。

Codex 关闭 `desktop.external-agent-import-sync-enabled`。旧 `model_instructions_file = "lessons.md"` 会替换模型内置指令，改为 AGENTS 显式读取 global/project lessons；部署新指令后才移除这个确切旧值。其他自定义 model_instructions_file 保留。

外部集成优先原生插件/MCP；旧 npx skill 拉取改为完整源码的明确路径。Playwright 固定 0.0.78 并保留旧 Node 兼容 launcher。ResearchStudio/PPT Master 只准备源码和必要适配，业务依赖留到首次调用。

## 已有用户如何迁移

让当前 agent 读取 [INSTALL.md](../INSTALL.md)，核实原生安装状态与文件后展示完整目录。选择表示新增/更新，未提到的内容继续保留；新推荐不扩大已选范围。

现有同内容文件可以复用；不同内容的 AGENTS/CLAUDE、skills、hooks 或配置先备份并准备具体合并。旧版 marker、npx lock 和导入 cache 仅作为识别线索，不自动证明新工具拥有删除权。数据库和真实 lessons 不搬移、不清空。

旧 install.sh/install.ps1 现在只显示对话安装入口，返回退出码 2 表示需要迁移；原 `--all`、`--force` 等参数不会安装、覆盖或卸载。使用同一份当前仓库的 INSTALL.md 继续，无需安装一个安装 skill 或返回旧分支。

文件归属、hash 和备份由 `agent-config/files.json` 保存；agent 的选择/原生操作记录由 `agent-config/selection.json` 保存。失败或中断后先恢复/核实真实状态，避免把计划当成成功。卸载只处理明确选择且归属可靠的内容。

安装记录增加仓库 URL、revision 与更新策略，具体见 [INSTALL.md](../INSTALL.md#repository-source)。旧记录缺少来源时，从可靠的原记录或用户给出的仓库页面 / checkout 补齐。不会因为当前 agent 是 Claude 或 Codex 就选择同名分支；指定 ref 也不会被默认分支取代。

## 条目退役与改名

活动目录现为 46 个 ID。更新遇到目录中消失的已选 ID 时，保留其现状与记录并提示处理方式，用户明确要求后才迁移或卸载。以后每次改名、替换或退役在此追加映射。

<a id="handoff"></a>
### handoff → matt-workflow 成员

handoff 已取消独立设置，两平台均由 Matt 包提供。新装 Matt 包时展示其 handoff 成员；旧 Matt 选择的成员记录若尚无 handoff，先说明新增范围，再按用户选择更新。

检测到旧独立 handoff 时，说明迁移将改为 Matt 上游版本，并展示包的完整范围；不能仅因旧 ID 存在就自动安装整个 Matt 包。用户选择迁移后，在隔离目录验证上游 handoff，核对旧 skills/handoff 的归属与修改；未修改的自管副本可受控替换并把归属改为 matt-workflow，外部或已修改副本先保留并准备具体合并。Claude 插件渠道切换时也先验证新包，再按明确移除选择处理旧副本。

验证成功后，将旧 ID 标记已迁移并保留对应记录，活动选择指向 matt-workflow。未选择迁移时记录“旧独立安装保留”，不报告更新成功。新入口只有 Matt 包，不再提供独立 handoff 配方。

<a id="ai-research"></a>
### 六个 AI Research ID → ai-research 整包

旧 `tokenization`、`fine-tuning`、`post-training`、`inference-serving`、`distributed-training`、`optimization` 合并为一个新选择 `ai-research`；原组名继续用于解释整包组件。新用户只选择一个编号，两端均安装上游这六组完整的 31 项，安装记录按整包及其组件保存。

已有单组或部分组选择保持原范围：根据记录核实、更新对应的原生 selector 或源码成员，不因目录合并而补装其他组。用户明确选择新整包后，展示实际差异、复用已有组件，再补装缺项。只有原六组已选择且实际范围等于完整 31 项时，才可以仅关联新的整包选择，保留原组件的文件归属和安装历史，无需重装。

Codex 旧六组共 24 项，仍属于待迁移的部分范围。新整包增加 miles-rl-training、slime-rl-training、torchforge-rl-training、huggingface-accelerate、pytorch-lightning、hqq-quantization、ml-training-recipes 七项；作者更新目录不等于已有用户同意补装。没有逐成员记录时先核对真实目录/manifest，不能只看旧六个 ID 齐全就标记 31 项完成。用户保持旧范围时沿用对应固定源码成员；原生组件会增加成员时先说明并等待选择。

源码切换原生插件时，先在隔离目录验证新包；核对旧副本的归属、本地修改及调用名变化，再按明确迁移选择处理重复副本。外部或已修改目录先保留，切换完成前不把两个提供方都记作活动成功。

原记录中的本地修改、外部安装和部分失败状态一并保留；只有全部所选成员验证完成才标记整包完成。明确请求卸载时逐组件检查创建归属，不因为合并 ID 获得外部内容的删除权。

## 支持边界

macOS、Linux、Windows 与 WSL 共用相同的 agent 流程，分别检测本地 CLI、shell、配置目录和运行前提。Windows 与 WSL 不混用 home；Codex App、CLI、IDE 的内置能力也应分别核对。

本开发环境是 macOS。Windows/WSL 的实际原生命令与 hooks 执行仍需对应环境验收；凭据类 MCP 和 Claude-Mem 的完整记忆生命周期需要用户授权及原生初始化。纯源码安装成功不代表可选业务依赖已经就绪。相关既有 skill 测试保留；只服务已退役终端安装器的断言随旧代码移除，新的开发验收脚本留在仓库之外。
