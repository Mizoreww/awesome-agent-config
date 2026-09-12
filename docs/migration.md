# 两条发布分支的合并说明

开发分支 `agent-config-for-agents` 从 main `d65cbda0058be09e4771f4603ccf45b3a589583b`（3.2.0）建立，额外读取 codex `fdd3e50aca09d1b80ac416f320f42bc0ecef5faa`（2.11.0）。只向该开发分支提交，不合并或重写原发布分支。

## 本地 skill 覆盖

main 的 7 个与 codex 的 8 个本地 skill 目录，映射为 10 个实际目录。两端相同的五份只维护一次；包含脚本、资源、许可的完整 payload 均保留。

| 来源 | 新位置 | 处理 |
| --- | --- | --- |
| 两端 humanizer、humanizer-zh、neat-freak、paper-reading、storage-analyzer | skills/同名目录 | 两端原始文件完全相同，保留共同副本 |
| main adversarial-review | platforms/claude/skills/adversarial-review | 保留 main 专属全文与 references |
| codex adversarial-review | platforms/codex/skills/adversarial-review | 保留历史全文与 references；Codex 当前审查策略采用 Matt code-review，因此不列为可安装项 |
| codex handoff | platforms/codex/skills/handoff | 保留定制版本，不被 Matt 上游副本替代 |
| main update-config | platforms/claude/skills/update-config | 保留调用名，入口改为对话维护 |
| codex update | platforms/codex/skills/update | 保留 update_config 调用名，入口改为对话维护 |

[source-provenance.json](source-provenance.json) 记录 125 项原始文件映射及 Git blob ID，覆盖 skill、配置、规则、字体、hooks 和两端历史 changelog。未标 adaptation 的目标与来源逐字节一致；被拆分/适配的文件在记录中说明原因。root lessons.md 保留项目纠错历史，安装只使用 platforms/global-lessons.md 的空白模板。

## 外部获取的能力

本地目录不是安装能力的全集。[catalog.md](../catalog.md) 和 [sources.md](../platforms/sources.md) 还覆盖：

- main settings 中的 20 个原生插件 selector（15 个启用、5 个关闭）加上安装菜单的 Matt 插件，共 21 个可选插件，以及 DeepXiv、ResearchStudio Idea 和 lieflat-charts 源码入口。
- Codex 的 Matt v1.1.0 十九项工作流、独立 code-review、定制 handoff；Superpowers 十四项；Karpathy；PUA 三项。
- Anthropic 文档四项、Codex examples 精选三项、独立 frontend-design；frontend-slides、PPT Master。
- AI Research 六组精选（24 项）、DeepXiv 三项、ResearchStudio Idea 三项与 Reel 五项，以及既有 MCP 配置能力。

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

旧 install.sh/install.ps1 现在只显示对话安装入口，返回退出码 2 表示需要迁移；原 `--all`、`--force` 等参数不会安装、覆盖或卸载。原发布分支仍可提供旧流程。此开发版不要求用户先安装一个安装 skill。

文件归属、hash 和备份由 `agent-config/files.json` 保存；agent 的选择/原生操作记录由 `agent-config/selection.json` 保存。失败或中断后先恢复/核实真实状态，避免把计划当成成功。卸载只处理明确选择且归属可靠的内容。

## 支持边界

macOS、Linux、Windows 与 WSL 共用相同的 agent 流程，分别检测本地 CLI、shell、配置目录和运行前提。Windows 与 WSL 不混用 home；Codex App、CLI、IDE 的内置能力也应分别核对。

本开发环境是 macOS。Windows/WSL 的实际原生命令与 hooks 执行仍需对应环境验收；凭据类 MCP 和 Claude-Mem 的完整记忆生命周期需要用户授权及原生初始化。纯源码安装成功不代表可选业务依赖已经就绪。相关既有 skill 测试保留；只服务已退役终端安装器的断言随旧代码移除，新的开发验收脚本留在仓库之外。
