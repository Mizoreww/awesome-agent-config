# 来源与本地定制

源自 [poteto/noodle](https://github.com/poteto/noodle) 的 `.agents/skills/adversarial-review`，作者 Lauren Tan（poteto），MIT 许可见同目录 LICENSE。

原导入未记录准确的上游 commit；仓库 Git 历史保留导入与修改过程。本次核对的上游 revision 为 `82d2921c52370f23f29086de81ccfb600939c037`，它是核对点，不宣称是原始 fork 点。

本仓库将原则入口改为随 skill 分发的 `references/reviewer-lenses.md`，使 `brain/principles.md` 成为可选补充，并保留显式 reviewer prompt、输出核实和 lead judgment 规则。因此这是有意维护的定制版，不是上游原样副本。

Claude 版本供选装；Codex 版本只保留历史定制，当前 Codex 审查选择 Matt 的 code-review。更新本地定制时同步本说明和完整引用资源。
