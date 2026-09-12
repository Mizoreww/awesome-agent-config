# 由 Agent 引导的 Claude / Codex 配置

[English](README.md)

一个仓库维护 Claude 和 Codex 配置、共享 skills 及平台集成。让已有的 agent 检测环境、解释完整目录，再安装你选择的内容。

把下面这段话交给 Claude 或 Codex：

> 请阅读 https://github.com/Mizoreww/awesome-claude-code-config/tree/agent-config-for-agents 中的 INSTALL.md，默认配置当前对话使用的 agent。按分类完整列出支持的安装项，连续编号，标注作者推荐和已安装状态，并解释用途。根据我的选择完成安装与验证，保留已有定制。

Agent 使用原生插件/MCP 命令，只有受控文件操作使用小工具。选择前无需先学习安装渠道和命令。

- [完整目录](catalog.md)：Claude/Codex 分别标注支持范围和作者推荐；作者尚未指定的推荐标记留空。
- [安装流程](INSTALL.md)：首次安装、新增、更新与明确卸载。
- [Claude 操作说明](platforms/claude/README.md) · [Codex 操作说明](platforms/codex/README.md)。
- [迁移与来源覆盖](docs/migration.md)：保留两条发布分支的能力，包括安装时获取的外部 skill 组。
- [变更记录](CHANGELOG.zh-CN.md)。

共享 skills 放在 `skills/`；平台差异与待部署配置放在 `platforms/`。根目录 AGENTS.md/CLAUDE.md 用于本仓库工作，不会被复制为用户全局指令。

当前开发分支以 Claude v3.2.0 为基础，纳入 Codex v2.11.0 的能力；原发布分支保持不变。macOS/Linux/Windows/WSL 共用安装说明，每个集成按实际运行环境核实支持。验证范围见迁移说明。

本仓库采用 MIT 许可。内置 skills 保留各自许可说明；外部 lieflat-charts 采用 PolyForm Noncommercial 1.0.0，选择时请核对来源许可。
