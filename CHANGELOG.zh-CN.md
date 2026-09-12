# 变更记录

## [4.0.0-dev.1] - 2026-09-12

### Features
- Claude 与 Codex 共用对话安装流程：检测环境，按分类完整列出带编号、作者推荐标记的目录，再执行用户选择。
- 合并 main v3.2.0 和 codex v2.11.0 的 skills。五份相同 payload 共用源码，五份平台差异独立保留；外部来源、固定版本和精选成员有明确路径。
- 优先使用原生插件/MCP 管理；小工具负责受控复制、JSON/TOML 局部合并、备份、源码适配和 MCP 初始化检查。
- 基础设置、权限、状态栏、记忆 hooks 和子 agents 分开选择；Codex 自动导入独立于基础设置关闭。

### Design Rationale
- 由已有 agent 解释平台差异、理解用户选择，避免再维护终端菜单、二进制发布或包解析框架。
- 一份 Markdown 目录维护两端独立的作者推荐。作者尚未指定的标记留空。
- 原生渠道迁移保留已选范围和 revision，尤其是 Codex 的 Matt v1.1.0 与定制 handoff。

### Notes & Caveats
- 开发分支基于 main，两个发布分支均未合并或替换。详见[迁移说明](docs/migration.md)与[来源映射](docs/source-provenance.json)。
- install.sh/install.ps1 只显示对话入口并返回退出码 2，旧菜单参数不再修改配置。
- 保留用户定制、凭据、真实 lessons 与记忆数据库。更新不会卸载未提到的项；卸载需要明确请求与归属核对。
- ResearchStudio Idea/Reel、PPT Master 只安装完整源码及必要适配，运行依赖留到首次调用。
- 部署显式读取 lessons 的指令后，才移除确切的旧 model_instructions_file = "lessons.md" 设置。
- Windows/WSL 原生命令、凭据类集成与 Claude-Mem 完整生命周期仍需对应环境验证。新开发验收脚本保留在仓库之外，相关既有 skill 测试继续保留。

历史版本：[Claude](platforms/claude/CHANGELOG.previous.zh-CN.md) · [Codex](platforms/codex/CHANGELOG.previous.zh-CN.md)。
