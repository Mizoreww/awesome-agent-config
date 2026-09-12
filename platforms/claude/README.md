# Claude 操作说明

先完成 [INSTALL.md](../../INSTALL.md) 的目录展示与用户选择。目标默认是已核实的 Claude config directory；全局默认 `~/.claude`，支持用户指定的 `CLAUDE_CONFIG_DIR`。命令先以本机 `claude ... --help` 核实。

<a id="configuration"></a>
## 配置与规则

使用 [managed_files.py](../../scripts/README.md) 的预览、受控复制与局部合并；模板在本目录的 templates 下。

| Catalog ID | 来源 → 目标 / 操作 |
| --- | --- |
| instructions | templates/CLAUDE.md → CLAUDE.md；现有不同文件需要具体合并，不直接覆盖 |
| settings | 仅合并 templates/settings.json → settings.json |
| permissions | 用户选择权限配置后，合并 templates/permissions.json；有差异的权限键需要明确 `--replace`，不要顺带改模型或插件 |
| lessons | seed-lessons；合并 templates/lessons-hooks.json。保留用户的 hooks；Windows 先核实这些 command hooks 使用的 Bash 可用 |
| statusline | templates/hooks/statusline.sh → hooks/statusline.sh；合并 templates/statusline.json；检查 Bash/jq。字体位于 templates/fonts（含 LICENSE），按 OS 用户字体目录安装，缺字体可使用文本显示 |
| rules-common | templates/rules/common → rules/common |
| rules-python | templates/rules/python → rules/python |
| rules-typescript | templates/rules/typescript → rules/typescript |
| rules-golang | templates/rules/golang → rules/golang |

规则按所选目录复制，不把说明用的 rules/README.md 放入会自动加载的规则目录。hooks/statusline 默认通过 CLAUDE_CONFIG_DIR 定位；若安装到未设置该环境变量的自定义目录，先在临时 patch 中生成正确引用并验证，再合并。

全局模板中提到的工作流必须与所选能力一致：解释依赖、让用户选择对应工作流，或对拟部署模板做明确适配；不能暗中安装未选插件。

<a id="plugins"></a>
## 原生插件

先查询 `claude plugin list --json` 与 marketplace 状态。仅为用户所选插件添加必要 marketplace：

```sh
claude plugin marketplace add <repository-or-url> --scope user
claude plugin install <plugin@marketplace> --scope user
claude plugin list --json
```

下面是保留 main 所有可选插件的 selector。只执行所选行，不遍历全表安装。

| Catalog ID | 原生 selector | Marketplace 来源 |
| --- | --- | --- |
| karpathy | andrej-karpathy-skills@karpathy-skills | forrestchang/andrej-karpathy-skills |
| matt-workflow | mattpocock-skills@mattpocock | mattpocock/skills |
| superpowers | superpowers@claude-plugins-official | anthropics/claude-plugins-official |
| claude-pr-review | code-review@claude-plugins-official | anthropics/claude-plugins-official |
| codex-in-claude | codex@openai-codex | openai/codex-plugin-cc |
| code-simplifier | code-simplifier@claude-plugins-official | anthropics/claude-plugins-official |
| context7 | context7@claude-plugins-official | anthropics/claude-plugins-official |
| playwright | playwright@claude-plugins-official | anthropics/claude-plugins-official |
| documents | document-skills@anthropic-agent-skills | anthropics/skills |
| examples | example-skills@anthropic-agent-skills | anthropics/skills |
| frontend-design | frontend-design@claude-plugins-official | anthropics/claude-plugins-official |
| frontend-slides | frontend-slides@frontend-slides | zarazhangrui/frontend-slides |
| ppt-master | ppt-master@ppt-master | hugohe3/ppt-master |
| claude-mem | claude-mem@thedotmack | thedotmack/claude-mem |
| claude-health | health@claude-health | tw93/claude-health |
| tokenization | tokenization@ai-research-skills | Orchestra-Research/AI-research-SKILLs |
| fine-tuning | fine-tuning@ai-research-skills | Orchestra-Research/AI-research-SKILLs |
| post-training | post-training@ai-research-skills | Orchestra-Research/AI-research-SKILLs |
| inference-serving | inference-serving@ai-research-skills | Orchestra-Research/AI-research-SKILLs |
| distributed-training | distributed-training@ai-research-skills | Orchestra-Research/AI-research-SKILLs |
| optimization | optimization@ai-research-skills | Orchestra-Research/AI-research-SKILLs |

读取所用 manifest 核实完整成员和插件要求。example-skills 已含 frontend-design，选择整包后复用；同一服务的 MCP 不再另外注册。Claude-Mem 的 worker、hooks、数据库与普通 skill 不同，保留已有数据；使用原生安装/初始化流程。

更新用本机帮助核实 `claude plugin update <selector>`，显式卸载用 `claude plugin uninstall <selector> --scope user`；只操作用户选择且归属明确的项。原来由用户安装的插件复用时不接管所有权。

<a id="local-skills"></a>
## 本地 skills

共享目录 ../../skills 下的 humanizer、humanizer-zh、neat-freak、paper-reading、storage-analyzer，分别完整复制到目标 skills 同名目录。

本目录 skills 下的 adversarial-review、update-config 是 Claude 专属版本，分别安装到 skills/adversarial-review、skills/update-config。更新入口已经改为本分支的对话流程。上游获取的 DeepXiv、ResearchStudio、lieflat-charts 见 [共享源码说明](../sources.md)。

<a id="mcp"></a>
## Lark MCP

主分支保留的可选服务是 Lark；参考 templates/mcp/mcp-servers.json，核实上游 [lark-openapi-mcp](https://github.com/larksuite/lark-openapi-mcp) 的当前参数。用户补齐凭据后，用 `claude mcp add --help` 确定用户 scope 与参数形式并注册，再检查连接。占位凭据不构成可用服务，也不写入成功记录。

Context7 和 Playwright 已通过上述原生插件提供，选择它们时不要再从参考 JSON 重复注册。其他未选服务不因配置合并而启用。
