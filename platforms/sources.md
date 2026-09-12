# 外部 skill 源码

只读取所选条目。原生插件能保持相同成员、版本与必要适配时优先使用它；本页提供精选源码及兼容性不足时的明确路径。源码安装只复制完整 skill，不执行上游安装器，也不在准备 ResearchStudio/PPT Master 时安装业务依赖。

## 获取与部署

下表是当前仓库采用的源码 revision，安装无需查询本仓库的历史分支。按 revision 获取并记录来源；Matt 的 v1.1.0 是当前明确的版本约束。维护者要求升级时，按 [MAINTAIN.md](../MAINTAIN.md) 核实新 revision、成员与适配并修改本表；已安装内容按 INSTALL 的选择与来源规则更新。

| 来源 | Repository | Revision |
| --- | --- | --- |
| Matt | https://github.com/mattpocock/skills | d574778f94cf620fcc8ce741584093bc650a61d3 |
| Anthropic | https://github.com/anthropics/skills | 34040c9c568585f6929bedeaad110ad08f079624 |
| Karpathy | https://github.com/forrestchang/andrej-karpathy-skills | 2c606141936f1eeef17fa3043a72095b4765b9c2 |
| ResearchStudio | https://github.com/microsoft/ResearchStudio | 0597891df1a153b8e4cbdc8c1c685f43a0a6abcf |
| PPT Master | https://github.com/hugohe3/ppt-master | aee33e5a0f6e6b5582831ef3825a739f334325cb |
| frontend-slides | https://github.com/zarazhangrui/frontend-slides | 9906a34d640d2111f724544cbc50f7f130569ae1 |
| AI Research | https://github.com/Orchestra-Research/AI-research-SKILLs | 773a52944ba4747a18bd4ae9ade53fff041adcbc |
| DeepXiv | https://github.com/DeepXiv/deepxiv_sdk | 80be0b195789bf50299ab8d221abb5d17500ded8 |
| lieflat-charts | https://github.com/larashero3-dotcom/lieflat-charts | eace082a317b696c5570c25826a53a7fa113e984 |
| OpenAI plugins | https://github.com/openai/plugins | d416fd5a43426019986b1e489506db3db66dee3d |
| Humanizer | https://github.com/blader/humanizer | 9862685f575c65a8247f90369951df1b3416e3d6 |
| Humanizer-zh | https://github.com/op7418/Humanizer-zh | 91f3d394db8419c20d67ebe22a96cf8fee0a404b |
| neat-freak | https://github.com/KKKKhazix/khazix-skills | 2b4a645cfdc894156ae347d897723562f719ce95 |

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

`matt-workflow` 安装以下 20 个目录，目标名为最后一级目录名：

- `skills/engineering/` 下：ask-matt、diagnosing-bugs、grill-with-docs、triage、implement、improve-codebase-architecture、setup-matt-pocock-skills、tdd、to-spec、to-tickets、wayfinder、prototype、domain-modeling、codebase-design、research。
- `skills/productivity/` 下：grill-me、grilling、teach、writing-great-skills、handoff。

`matt-code-review` 独立选项：`skills/engineering/code-review` → `skills/code-review`。

`handoff` 使用上述 Matt 上游目录，归属 `matt-workflow`，不再单独选择或维护本地版本。旧独立 handoff 的迁移见 [迁移说明](../docs/migration.md#handoff)。安装范围由上面的成员列表定义，不复制整个上游 repo。Claude 的 Matt 原生包成员见 [目录](../catalog.md#members)。

<a id="writing"></a>
## Humanizer、Humanizer-zh 与 neat-freak

这三项是第三方原版，本仓库仅维护上游入口与部署配方。安装到用户的 agent home 后，源码仍以各自上游为准；本仓库中没有原版副本。

| ID | 上游提供的安装方式 | 所选源码的完整部署范围 |
| --- | --- | --- |
| humanizer | [blader/humanizer 安装说明](https://github.com/blader/humanizer#installation)：Claude 原生插件优先；也支持 Skills CLI 或手动复制 | 根目录 SKILL.md、LICENSE、agents/ → skills/humanizer；只复制 skill 内容，不复制仓库 AGENTS.md、CI 或验证工具 |
| humanizer-zh | [op7418/Humanizer-zh 安装说明](https://github.com/op7418/Humanizer-zh)：Skills CLI、Git 或手动安装 | 根目录 SKILL.md、LICENSE → skills/humanizer-zh |
| neat-freak | [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)：让 agent 从上游获取所选 skill | neat-freak/ 的完整运行内容（SKILL.md、references/、scripts/）及根 LICENSE → skills/neat-freak；evals 是上游评估数据，不需部署 |

上游 Skills CLI 入口分别为 `npx skills add blader/humanizer` 和 `npx skills add https://github.com/op7418/Humanizer-zh.git`。执行前核实其本机帮助、agent 参数、目标目录、所选范围与 revision；仅在能满足这些条件时直接使用。它可能默认写入共享目录，不能因此把 Codex 的权威副本改到 `.agents/skills`，也不能扩大到所有 agents。

需要固定 revision、自定义 home，或 CLI 无法满足目标路径时，使用上游同样支持的手动方案：按本页获取步骤下载表中 revision，在临时 stage 准备上述完整范围（保留执行位及许可），再通过文件工具部署。这仍从第三方原仓库安装，没有本仓库 vendored 副本。逐一验证所有资源的来源及目标路径。

Humanizer 当前上游为 3.0.0，旧内置版本为 2.2.0；原生包只含 humanizer 这一项。Claude 使用插件；Codex 0.153.4 会忽略其根目录 skill 入口，按上面的源码配方安装，详见[兼容性说明](codex/plugins.md)。已有副本迁移先说明版本与调用名变化（Claude 插件调用名为 `/humanizer:humanizer`），保留本地修改并由用户选择迁移。neat-freak 的运行源码继续保持上述已核对的固定 revision。

<a id="anthropic"></a>
## Anthropic

| 选项 | 完整源码目录 |
| --- | --- |
| documents | skills/pdf、skills/docx、skills/pptx、skills/xlsx |
| examples（Codex） | skills/canvas-design、skills/algorithmic-art、skills/mcp-builder |
| frontend-design | skills/frontend-design |

目标名保持目录名。文档能力已由当前 client 的内置插件完整提供时复用。Codex 0.153.4 已验证同范围的 document-skills 原生兼容包实际加载四项并保留完整资源，优先按[插件说明](codex/plugins.md)安装；client 不支持时使用上述源码。examples 的三个成员不能被整个十二项包替代。Claude examples 使用原生整包。

<a id="karpathy"></a>
## Karpathy

`skills/karpathy-guidelines` → `skills/karpathy-guidelines`。两平台优先原生包；只有 client 不支持插件或兼容性核实失败、且用户接受源码渠道时采用此路径。

<a id="superpowers"></a>
## Superpowers

Codex 首选当前账号可见的 OpenAI curated Superpowers，确切 selector 由[插件说明](codex/plugins.md)中的查询确定。目录不可用或 client 不支持插件时，可从上表 OpenAI plugins 的 `plugins/superpowers/skills/` 复制 [目录](../catalog.md#members) 中十四个完整成员，逐一记录。核对 `using-superpowers` 的加载要求；在拟部署的全局指令中加入其实际路径入口，保留用户其余指令。其他插件目录不复制。

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

用文件工具逐一发布 stage 内目录。检查 paper_search 的绝对脚本路径、scoop_check 的 fetch 入口，并确认源文件之外仅有预期适配。Reel 的 `paper2poster` 内含 html2pptx 等嵌套资源，必须完整保留。Reel 同样先将五个目录复制到新的 stage，然后运行下面的适配，再逐一发布：

```sh
python3 scripts/adapt_researchstudio.py --stage "$stage" --agent codex --bundle reel --root "$target_dir"
```

Reel 适配覆盖各 SKILL.md、引用的 Markdown runbook 和运行诊断中的旧 Claude/仓库相对脚本路径，替换成已验证的 Codex 绝对路径；保留资源与业务逻辑。上游路径或锚点变化时停止发布并检查。

本条验收是完整源码与适配，不运行上游 install.sh/npx setup，不创建 Python 环境、不装包或浏览器。缺少 API key、Chromium、LaTeX 等业务前提留到首次调用，由 skill 自带说明引导；交接简短注明“源码已安装，运行准备在首次使用完成”。

<a id="slides"></a>
## 演示文稿

| 选项 | 源码目录 → 目标 |
| --- | --- |
| ppt-master | skills/ppt-master → skills/ppt-master |
| frontend-slides | plugins/frontend-slides/skills/frontend-slides → skills/frontend-slides |

Claude 优先使用对应原生插件。Codex 的 frontend-slides 已验证原生兼容包实际加载完整 skill，按[插件说明](codex/plugins.md)优先采用；不支持插件的 client 使用上述源码。PPT Master 当前插件的根目录入口被 Codex 忽略，且嵌套 Git 来源没有固定 revision，保持上述固定源码路径。它的 Python/浏览器环境留到首次调用，验收不执行安装业务依赖的命令。

<a id="ai-research"></a>
## AI Research 整包（两端统一 31 项）

选择 `ai-research` 一次安装以下六组、共 31 个完整 skills，所有成员归属同一个 catalog ID。两平台优先使用这些上游分类插件；Codex 0.153.4 已验证六个兼容包实际加载全部 31 项。这里只打包这六组，其他上游研究分类不随本选项安装。

| 原生 selector（Claude / Codex） | 源码路径 → 目标名 |
| --- | --- |
| tokenization@ai-research-skills | 02-tokenization/huggingface-tokenizers；02-tokenization/sentencepiece |
| fine-tuning@ai-research-skills | 03-fine-tuning/axolotl；03-fine-tuning/llama-factory；03-fine-tuning/peft → peft-fine-tuning；03-fine-tuning/unsloth |
| post-training@ai-research-skills | 06-post-training/grpo-rl-training；06-post-training/miles → miles-rl-training；06-post-training/openrlhf → openrlhf-training；06-post-training/simpo → simpo-training；06-post-training/slime → slime-rl-training；06-post-training/torchforge → torchforge-rl-training；06-post-training/trl-fine-tuning → fine-tuning-with-trl；06-post-training/verl → verl-rl-training |
| inference-serving@ai-research-skills | 12-inference-serving/llama-cpp；12-inference-serving/sglang；12-inference-serving/tensorrt-llm；12-inference-serving/vllm → serving-llms-vllm |
| distributed-training@ai-research-skills | 08-distributed-training/accelerate → huggingface-accelerate；08-distributed-training/deepspeed；08-distributed-training/megatron-core → training-llms-megatron；08-distributed-training/pytorch-fsdp2；08-distributed-training/pytorch-lightning；08-distributed-training/ray-train |
| optimization@ai-research-skills | 10-optimization/awq → awq-quantization；10-optimization/bitsandbytes → quantizing-models-bitsandbytes；10-optimization/flash-attention → optimizing-attention-flash；10-optimization/gguf → gguf-quantization；10-optimization/gptq；10-optimization/hqq → hqq-quantization；10-optimization/ml-training-recipes |

Marketplace 为 `Orchestra-Research/AI-research-SKILLs`，revision 见本页来源表；按 [Claude](claude/README.md#ai-research) / [Codex](codex/plugins.md) 的原生命令只安装表中六个 selector。核对 manifest 的显式 skill 路径、资源及实际加载成员，不能把 cache 中其余目录计作已启用。原生调用名可能带分类插件前缀。

Client 不支持插件或固定版本条件不满足时，解释后按右列路径安装同一 31 项；省略目标名时使用最后一级目录名。源码部署使用文件工具的 `--item ai-research`，保留许可，逐一记录来源与结果。只有全部所选组件验证完成才标记整包成功，部分失败时保留已成功成员并续装。

旧六组 ID、Codex 24 项或其他部分选择按[迁移规则](../docs/migration.md#ai-research)保留原范围；新目录中的 31 项不自动扩充已有用户的安装。

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

stage 只含根文件及四个目录，保留 LICENSE；排除 `.git` 和 `docs/` 预览媒体。预览索引中的缩略图/文档链接可能缺失，图表和报告的文本选择资源完整。旧 marker 只作为识别线索，不据此覆盖用户已修改的目录。
