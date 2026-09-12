# 外部 skill 源码

只读取所选条目。原生插件能保持相同成员、版本与必要适配时优先使用它；本页提供精选源码及兼容性不足时的明确路径。源码安装只复制完整 skill，不执行上游安装器，也不在准备 ResearchStudio/PPT Master 时安装业务依赖。

## 获取与部署

下表是本开发版核对的源码 revision。按 revision 获取并记录来源；Matt 的 v1.1.0 是必须保留的版本约束。更新跟随本仓库的新来源记录；用户明确要求更新某个上游时，核实新 revision 的成员与适配后再更新该项。

| 来源 | Repository | Revision |
| --- | --- | --- |
| Matt | https://github.com/mattpocock/skills | d574778f94cf620fcc8ce741584093bc650a61d3 |
| Anthropic | https://github.com/anthropics/skills | 34040c9c568585f6929bedeaad110ad08f079624 |
| Karpathy | https://github.com/forrestchang/andrej-karpathy-skills | 2c606141936f1eeef17fa3043a72095b4765b9c2 |
| ResearchStudio | https://github.com/microsoft/ResearchStudio | 0597891df1a153b8e4cbdc8c1c685f43a0a6abcf |
| PPT Master | https://github.com/hugohe3/ppt-master | aee33e5a0f6e6b5582831ef3825a739f334325cb |
| frontend-slides | https://github.com/zarazhangrui/frontend-slides | 9906a34d640d2111f724544cbc50f7f130569ae1 |
| PUA | https://github.com/tanweai/pua | e6e6cd237ad17750d179674bff52f8184abea8fd |
| AI Research | https://github.com/Orchestra-Research/AI-research-SKILLs | 773a52944ba4747a18bd4ae9ade53fff041adcbc |
| DeepXiv | https://github.com/DeepXiv/deepxiv_sdk | 80be0b195789bf50299ab8d221abb5d17500ded8 |
| lieflat-charts | https://github.com/larashero3-dotcom/lieflat-charts | eace082a317b696c5570c25826a53a7fa113e984 |
| OpenAI plugins | https://github.com/openai/plugins | d416fd5a43426019986b1e489506db3db66dee3d |

在新的临时目录获取源码。例如下面是 Bash 参数形式；PowerShell 使用同样参数及其变量语法。`source_url`、`revision`、`checkout` 由当前所选项确定；不要修改用户现有 checkout。

```sh
git clone --depth=1 --filter=blob:none --no-checkout "$source_url" "$checkout"
git -C "$checkout" fetch --depth=1 origin "$revision"
git -C "$checkout" sparse-checkout init --cone
git -C "$checkout" sparse-checkout set <所选源码目录...>
git -C "$checkout" checkout --detach "$revision"
git -C "$checkout" rev-parse HEAD
```

核实 revision、目录内 SKILL.md、脚本/资源及许可，拒绝符号链接。Git 不支持 sparse/partial clone 时可使用同一 revision 的完整临时 checkout；实际复制范围仍按下文，不能扩大。完整目录经 [文件工具](../scripts/README.md) 预览后复制到 `<agent-home>/skills/<目标名>`；共享上游 LICENSE/NOTICE 不在 skill 目录内时一并保留在副本中，已有同名许可不得覆盖。

```sh
python3 scripts/managed_files.py --root "$target_dir" --dry-run install "$checkout/<skill-path>" "skills/<name>" --item "<catalog-id>" --origin "$source_url@$revision"
python3 scripts/managed_files.py --root "$target_dir" install "$checkout/<skill-path>" "skills/<name>" --item "<catalog-id>" --origin "$source_url@$revision"
```

安装验证包括资源树与来源的一致性，不能只检查 SKILL.md 的存在。准备阶段失败时不发布半个 skill；每个成员单独记录结果，失败后可以从已有结果继续。

<a id="matt"></a>
## Matt（Codex 固定精选）

`matt-workflow` 安装以下 19 个目录，目标名为最后一级目录名：

- `skills/engineering/` 下：ask-matt、diagnosing-bugs、grill-with-docs、triage、implement、improve-codebase-architecture、setup-matt-pocock-skills、tdd、to-spec、to-tickets、wayfinder、prototype、domain-modeling、codebase-design、research。
- `skills/productivity/` 下：grill-me、grilling、teach、writing-great-skills。

`matt-code-review` 独立选项：`skills/engineering/code-review` → `skills/code-review`。

`handoff` 使用本仓库 `platforms/codex/skills/handoff`；保留其定制内容。固定快照内的其他 skills 不在旧 Codex 活跃安装范围，不能把整个 repo 都装入。Claude 的 Matt 原生包保留 main 的完整范围，成员见 [目录](../catalog.md#members)。

<a id="anthropic"></a>
## Anthropic

| 选项 | 完整源码目录 |
| --- | --- |
| documents | skills/pdf、skills/docx、skills/pptx、skills/xlsx |
| examples（Codex） | skills/canvas-design、skills/algorithmic-art、skills/mcp-builder |
| frontend-design | skills/frontend-design |

目标名保持目录名。文档能力已由当前 client 的内置插件完整提供时复用。documents 对应的原生包若经过验证支持当前 Codex client，优先安装同范围的 document-skills；examples 的三个成员不能被整个十二项包替代。Claude examples 使用原生整包。

<a id="karpathy"></a>
## Karpathy

`skills/karpathy-guidelines` → `skills/karpathy-guidelines`。两平台优先原生包；只有 client 不支持插件或兼容性核实失败、且用户接受源码渠道时采用此路径。

<a id="superpowers"></a>
## Superpowers

Codex 首选 `superpowers@openai-curated`。不支持插件的 client 可从上表 OpenAI plugins 的 `plugins/superpowers/skills/` 复制 [目录](../catalog.md#members) 中十四个完整成员，逐一记录。核对 `using-superpowers` 的加载要求；在拟部署的全局指令中加入其实际路径入口，保留用户其余指令。其他插件目录不复制。

<a id="researchstudio"></a>
## ResearchStudio Idea / Reel

Idea 两平台均支持；Reel 保留 Codex 原有选项。二者独立选择。

| 选项 | 上游父目录 | 只安装这些完整成员 |
| --- | --- | --- |
| researchstudio-idea | ResearchStudio-Idea/skills | idea_spark、paper_search、scoop_check |
| researchstudio-reel | ResearchStudio-Reel/skills | paper2assets、paper2poster、paper2video、paper2blog、paper2reel |

Idea 先把三个目录复制到**全新的临时 stage**，再运行：

```sh
python3 scripts/adapt_researchstudio.py --stage "$stage" --agent codex --root "$target_dir"
```

Claude 改用 `--agent claude`。适配修正全局安装的脚本路径和项目输出路径；Codex 还替换 Claude 专用工具指令。脚本只改 stage，所有锚点匹配成功后才发布；锚点不符应检查新上游，不能用宽泛替换绕过。Windows 的 shell 脚本需可用 Bash；路径应为该 Bash 能访问的形式，必要时通过 Git Bash 的 `cygpath` 核实。

用文件工具逐一发布 stage 内目录。检查 paper_search 的绝对脚本路径、scoop_check 的 fetch 入口，并确认源文件之外仅有预期适配。Reel 的 `paper2poster` 内含 html2pptx 等嵌套资源，必须完整保留。

本条验收是完整源码与适配，不运行上游 install.sh/npx setup，不创建 Python 环境、不装包或浏览器。缺少 API key、Chromium、LaTeX 等业务前提留到首次调用，由 skill 自带说明引导；交接简短注明“源码已安装，运行准备在首次使用完成”。

<a id="slides"></a>
## 演示文稿

| 选项 | 源码目录 → 目标 |
| --- | --- |
| ppt-master | skills/ppt-master → skills/ppt-master |
| frontend-slides | plugins/frontend-slides/skills/frontend-slides → skills/frontend-slides |

Claude 优先使用对应原生插件。Codex 原生兼容包经验证能提供同一范围、同一 revision 时也优先采用；否则按上述路径部署完整源码。PPT Master 的 Python/浏览器环境留到首次调用，验收不执行安装业务依赖的命令。

<a id="pua"></a>
## PUA（Codex）

复制 `codex/pua`、`codex/pua-en`、`codex/pua-ja` 到同名 skills 目录。保留各自 `references/` 等资源；这些是上游 Codex 专用版本。新出现的其他 PUA skills 不随本选项自动安装。

<a id="ai-research"></a>
## AI Research（Codex 精选）

Claude 用六个分类原生插件；Codex 保持原分支成员。表中省略目标名时使用最后一级目录名；不要把上游目录前缀误当成 skill 名。

| Catalog ID | 源码路径 → 目标名 |
| --- | --- |
| tokenization | 02-tokenization/huggingface-tokenizers；02-tokenization/sentencepiece |
| fine-tuning | 03-fine-tuning/axolotl；03-fine-tuning/llama-factory；03-fine-tuning/peft → peft-fine-tuning；03-fine-tuning/unsloth |
| post-training | 06-post-training/grpo-rl-training；06-post-training/openrlhf → openrlhf-training；06-post-training/simpo → simpo-training；06-post-training/trl-fine-tuning → fine-tuning-with-trl；06-post-training/verl → verl-rl-training |
| distributed-training | 08-distributed-training/deepspeed；08-distributed-training/pytorch-fsdp2；08-distributed-training/megatron-core → training-llms-megatron；08-distributed-training/ray-train |
| inference-serving | 12-inference-serving/vllm → serving-llms-vllm；12-inference-serving/sglang；12-inference-serving/tensorrt-llm；12-inference-serving/llama-cpp |
| optimization | 10-optimization/awq → awq-quantization；10-optimization/gptq；10-optimization/gguf → gguf-quantization；10-optimization/flash-attention → optimizing-attention-flash；10-optimization/bitsandbytes → quantizing-models-bitsandbytes |

这些目标名沿用旧安装目录；核对 SKILL.md frontmatter 的实际调用名并记录。上游原生插件的分类成员可能更多，不能因此扩大用户选的精选范围。

<a id="deepxiv"></a>
## DeepXiv

三个独立条目：`skills/deepxiv-cli`、`skills/deepxiv-trending-digest`、`skills/deepxiv-baseline-table`，目标同名。解释后两项的 CLI 前提，复用已存在的 DeepXiv CLI；缺少运行依赖时按上游说明准备并单独报告状态。不会把整个 SDK clone 当成 skill。

<a id="lieflat"></a>
## lieflat-charts（Claude）

上游许可为 **PolyForm Noncommercial 1.0.0**。选型时说明仅许可非商业使用。仓库只保存来源与做法，不内置第三方 payload。

临时 checkout 使用上述完整 revision；sparse 范围为 `templates examples scripts agents`（cone 模式同时保留根文件）。然后：

```sh
python3 scripts/stage_lieflat.py "$checkout" "$stage"
python3 scripts/managed_files.py --root "$target_dir" --dry-run install "$stage" skills/lieflat-charts --item lieflat-charts --origin "$source_url@$revision"
python3 scripts/managed_files.py --root "$target_dir" install "$stage" skills/lieflat-charts --item lieflat-charts --origin "$source_url@$revision"
```

stage 只含根文件及四个目录，保留 LICENSE；排除 `.git` 和 `docs/` 预览媒体。与 main 一样，预览索引中的缩略图/文档链接可能缺失，图表和报告的文本选择资源完整。旧 marker 只作为识别线索，不据此覆盖用户已修改的目录。
