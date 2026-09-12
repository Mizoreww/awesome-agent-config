# 让 Agent 维护仓库

用户要求在本仓库新增、更新、修改、删除 skills / 插件 / 配置，或调整作者推荐时，按本文件执行。给用户机器安装或更新已选内容走 [INSTALL.md](INSTALL.md)。仓库改动与用户已安装内容分别处理；修改目录不会直接修改任何 agent home。

## 1. 确定修改范围

读取相关 [catalog.md](catalog.md) 条目、完整 skill 及其引用资源、对应平台说明；涉及外部来源时读取 [sources.md](platforms/sources.md) 的相应部分。沿用用户已明确的目标和授权。

当前 checkout 的文件是维护依据。旧分支和 [历史映射](docs/migration.md) 只用于追溯，安装和维护均无需获取它们。外部上游 revision 是当前仓库的版本约束；可以在用户要求升级时核实并更新，不能只因为有 latest 就解锁。

先确认源码归属：第三方原版只维护上游安装方式，不复制进本仓库；作者自有 skill 留在这里。作者明确维护的定制衍生版也可保留完整源码，附上游署名和本地修改说明。handoff 仅属于 Matt 工作流包，使用该包的上游版本。

完成条件：明确涉及的稳定 ID、支持的 agent、成员范围、来源与变更原因。

## 2. 修改内容与安装办法

| 请求 | Agent 要完成的修改 |
| --- | --- |
| 新增自有 skill | 共用源码放 `skills/<name>/`，真正的平台差异放 `platforms/<agent>/skills/<name>/`；包含 SKILL.md、脚本、引用资源和许可 |
| 新增上游能力 | 优先核实对应 agent 的官方安装机制与上游支持；只在平台说明或 sources 中记录上游安装入口、selector / revision、完整成员、验证方式和限制，不内置原版 payload |
| 修改 skill | 编辑本仓库的完整源码及受影响资源；同步必要的平台适配，保留用户要求的定制 |
| 更新上游 | 比较当前记录与拟升级 revision 的成员、入口、资源、许可及兼容性；更新来源记录和必要适配，在隔离目录验证后提交 |
| 删除或改名 | 清理活动目录、当前文档链接及安装配方；稳定 ID 不复用于别的能力，改名保留旧 ID 的迁移说明 |
| 修改推荐 | 仅按作者明确指定的名单更新 catalog 对应 agent 的推荐列；同步 README 标记 |
| 修改配置或记忆规则 | 分别修改 Claude / Codex 模板与平台说明；保持各自的全局指令、lessons 模板及项目记忆位置一致 |

上游原生包扩展成员时，说明新增范围，保留已有用户的选择边界。ResearchStudio Idea/Reel、PPT Master 继续只部署完整源码和必要适配，业务依赖由首次调用准备。通用脚本只承担明确文件操作，复杂选择由 agent 完成。

完成条件：每项能力在支持的平台有可执行、可验证的安装办法；变更不会依赖旧分支或另一 agent 的配置。

## 3. 同步用户与 Agent 的入口

- `catalog.md` 是稳定 ID、分类、支持范围、作者推荐和安装渠道的权威目录。
- `README.md` 与 `README.zh-CN.md` 是面向用户的同一份完整介绍：保留 Core、Language Rules、Review、Workflow、Integrations、Design & Content、Slides、Memory & Lifestyle、Storage、Academic Research、MCP Servers 的分类顺序，更新用途、来源、平台支持及推荐标记。
- 平台说明 / `sources.md` 集中保存具体安装配方；README 与 catalog 链接到它们，避免再复制命令。涉及通用安装行为时同步 INSTALL；版本级变化同步 VERSION 与双语 CHANGELOG。
- 移除或替换活动 ID 时，在 [迁移说明](docs/migration.md) 新增旧 ID → 新 ID / 退役原因与处理方式。安装记录中的旧 ID 需被识别、解释并保留；只有用户要求移除才卸载已有副本。

历史 changelog、项目 lessons 和首次合并的 provenance 保留原始事实；它们不要求当前 skill 永远与旧 blob 相同。

完成条件：两份 README、catalog、源码与配方描述同一套能力，没有失效链接或隐式新增安装范围。

## 4. 验证并交接

运行 `bash scripts/check-readme-sync.sh`，检查所改条目的链接、完整资源和必要适配。涉及文件操作或安装行为时在临时 agent home 验证，包括保留已有修改；只运行受影响的既有测试。新的临时测试与验收记录放仓库之外。

验证当前 checkout 或其导出目录可独立使用；需要网络时只访问所选来源，不取旧 Claude/Codex 分支。按本仓库约定完成代码审查。

完成条件：报告修改的条目、验证结果及剩余限制；用户的安装选择、真实 lessons 和定制内容保持可追溯。
