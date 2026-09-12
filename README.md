<!-- Keep the user-facing tables aligned with catalog.md and README.zh-CN.md. -->

**English** | [中文](README.zh-CN.md) | [Changelog](CHANGELOG.md)

# Awesome Claude Code & Codex Configuration

![Claude Statusline](assets/statusline.png)

One repository for [Claude Code](https://claude.com/claude-code) and [Codex](https://developers.openai.com/codex/): global instructions, coding rules, plugins, shared skills, status lines and correction memory. Your existing agent detects the platform, explains the options and installs your choices. The same conversation works on macOS, Linux, Windows and WSL, with commands checked against the local client.

## Showcase

![Claude Code Demo](images/claude-code-demo.png)

- [paper-reading skill — *Attention Is All You Need*](docs/Attention_Is_All_You_Need.md)
- [adversarial-review skill — worked example](docs/adversarial-review-showcase.md)

## Quick Start

Open this checkout in Claude or Codex, or share **the URL of the repository page you are reading** along with the request below. Keep its branch/ref when sharing a branch page.

> Read INSTALL.md from the checkout or repository page I shared, using the same branch/revision as its README. Configure the agent I am talking to. Detect my OS, client and existing configuration. List every supported installation option by category with continuous numbers, mark author recommendations and existing installations, and explain each option. Install and verify my choices, preserving my customizations.

The agent lists the complete catalogue for your agent. Reply with numbers, names or a description of what you want. A plugin bundle gets one number and lists its members; capabilities included in that bundle are not installed twice. Author recommendations are separate for Claude and Codex and remain empty until the author supplies them. Recommendations do not select items for you.

For later changes, say “add paper-reading”, “update my previous selections” or “remove storage-analyzer”. Existing choices are reused; omitting an installed item never uninstalls it. The optional update skills are `/update-config` on Claude and `update_config` on Codex; normal conversation works without them.

Native plugin/MCP commands are preferred; the agent chooses source installation when the documented scope or client requires it. You do not need to choose between npx, plugins and skill copies yourself. Codex setup disables external-agent auto-import so installations follow your selections. Windows and WSL are detected and configured separately; App/CLI installations sharing a home are reused.

[Installation workflow](INSTALL.md) · [Claude operations](platforms/claude/README.md) · [Codex operations](platforms/codex/README.md) · [Full catalogue and bundle members](catalog.md)

## Catalogue

The tables retain the original categories and merge the Claude and Codex capabilities. Third-party originals are installed from their upstream sources; this repository stores author-owned and intentionally customized skills with attribution. Handoff belongs to the Matt bundle only. `—` means this repository does not offer that item for the agent. The agent hides those entries when presenting your choices. A platform cell marked **★** means the author recommends it for that agent; no recommendations are set yet. Exact routes, stable IDs and recommendation markers live in [catalog.md](catalog.md).

### Core

| Item | Source | What It Does | Claude | Codex |
| --- | --- | --- | --- | --- |
| **CLAUDE.md / AGENTS.md** | [Repository](platforms/claude/README.md#configuration) | Separate global instructions for each agent | Template | Template |
| **Base settings** | [Repository](platforms/codex/README.md#configuration) | Partially merge model, reasoning and runtime settings | Template | Template |
| **Permissions** | [Repository](platforms/codex/README.md#configuration) | Optional high-autonomy permissions for a user-selected trusted environment | Template | Template |
| **Common rules** | [Repository](platforms/claude/README.md#configuration) | Coding style, Git, security and testing rules | Template | — |
| **StatusLine** | [Repository](platforms/claude/README.md#configuration) | Claude gradient context/usage bar and fonts; Codex native footer | Template | Template |
| **Lessons** | [Repository](platforms/codex/README.md#configuration) | Independent blank global logs and memory routing; preserve real corrections | Template | Template |
| **explorer** | [Repository](platforms/codex/README.md#configuration) | Subagent for tracing code paths and locating implementations | — | Template |
| **reviewer** | [Repository](platforms/codex/README.md#configuration) | Subagent for defects, regressions and missing coverage | — | Template |
| **docs-researcher** | [Repository](platforms/codex/README.md#configuration) | Subagent for checking documentation and API usage | — | Template |

### Language Rules

| Item | Source | What It Does | Claude | Codex |
| --- | --- | --- | --- | --- |
| **Python rules** | [Repository](platforms/claude/README.md#configuration) | PEP 8, pytest, type hints and bandit | Template | — |
| **TypeScript rules** | [Repository](platforms/claude/README.md#configuration) | Zod, Playwright and immutability | Template | — |
| **Go rules** | [Repository](platforms/claude/README.md#configuration) | gofmt, table-driven tests and gosec | Template | — |

### Review

| Item | Source | What It Does | Claude | Codex |
| --- | --- | --- | --- | --- |
| **Claude code-review** | [Anthropic](https://github.com/anthropics/claude-plugins-official) | Confidence-based pull request review | Native plugin | — |
| **Matt code-review** | [Matt Pocock](https://github.com/mattpocock/skills) | Separate Standards and Spec reviews; a standalone choice on Codex | In Matt bundle | Selected source |
| **adversarial-review** | [poteto/noodle](https://github.com/poteto/noodle/blob/main/.agents/skills/adversarial-review/SKILL.md) | Cross-model review through Skeptic, Architect and Minimalist lenses | Bundled skill | — |
| **codex-in-claude** | [OpenAI](https://github.com/openai/codex-plugin-cc) | Call Codex CLI from Claude; choose alongside review tools according to need | Native plugin | — |

### Workflow

| Item | Source | What It Does | Claude | Codex |
| --- | --- | --- | --- | --- |
| **andrej-karpathy-skills** | [Karpathy skills](https://github.com/forrestchang/andrej-karpathy-skills) | Think before coding, keep changes focused, define verifiable outcomes | Native plugin | Plugin / source |
| **superpowers** | [obra / OpenAI curated](https://github.com/obra/superpowers) | Brainstorming, debugging, TDD, worktrees and planning; 14-skill bundle | Native plugin | Plugin / source |
| **mattpocock-skills** | [Matt Pocock](https://github.com/mattpocock/skills) | Planning, TDD, research, grilling and delivery; Claude full package, Codex 20 selected v1.1.0 skills, including handoff | Native plugin | Selected source |
| **neat-freak** | [khazix-skills](https://github.com/KKKKhazix/khazix-skills/tree/2b4a645cfdc894156ae347d897723562f719ce95/neat-freak) | Reconcile project docs, agent rules, authorized memory and workspace residue | Upstream install | Upstream install |
| **code-simplifier** | [Anthropic](https://github.com/anthropics/claude-plugins-official) | Code simplification and refactoring agent | Native plugin | — |
| **update-config / update_config** | [Repository](INSTALL.md) | Maintain the selected installation from its recorded repository source | Bundled skill | Bundled skill |

### Integrations

| Item | Source | What It Does | Claude | Codex |
| --- | --- | --- | --- | --- |
| **context7** | [Upstash](https://github.com/upstash/context7) | Up-to-date library documentation lookup | Native plugin | Plugin / MCP |
| **playwright** | [Microsoft](https://github.com/microsoft/playwright-mcp) | Browser automation, E2E testing and screenshots; Codex MCP pinned to 0.0.78 | Native plugin | MCP |

### Design & Content

| Item | Source | What It Does | Claude | Codex |
| --- | --- | --- | --- | --- |
| **document-skills** | [Anthropic](https://github.com/anthropics/skills) | PDF, DOCX, PPTX and XLSX creation and editing; reuse equivalent built-in Codex tools | Native plugin | Built-in / source |
| **example-skills** | [Anthropic](https://github.com/anthropics/skills) | Claude: 12 examples; Codex: canvas-design, algorithmic-art and mcp-builder | Native plugin | Selected source |
| **frontend-design** | [Anthropic](https://github.com/anthropics/claude-plugins-official) | Distinctive frontend interfaces; reused when already supplied by the examples bundle | Native plugin | Plugin / source |
| **humanizer** | [blader](https://github.com/blader/humanizer) | Remove mechanical AI writing patterns in English | Plugin / source | Upstream install |
| **humanizer-zh** | [op7418](https://github.com/op7418/Humanizer-zh) | Remove mechanical AI writing patterns in Chinese | Upstream install | Upstream install |
| **lieflat-charts** | [lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) | Lupi / Basics / Glance / Maps HTML galleries and 12 bilingual report templates; source excludes preview media; noncommercial use only | Selected source | — |

### Slides

| Item | Source | What It Does | Claude | Codex |
| --- | --- | --- | --- | --- |
| **frontend-slides** | [zarazhangrui](https://github.com/zarazhangrui/frontend-slides) | Zero-dependency HTML slide generation with PPT conversion and varied styles | Native plugin | Selected source |
| **ppt-master** | [hugohe3](https://github.com/hugohe3/ppt-master) | Editable PPTX from PDF / DOCX / URL / Markdown, with shapes and animations; runtime setup on first use | Native plugin | Selected source |

### Memory & Lifestyle

| Item | Source | What It Does | Claude | Codex |
| --- | --- | --- | --- | --- |
| **claude-mem** | [thedotmack](https://github.com/thedotmack/claude-mem) | Persistent memory, search and timelines; includes skills, hooks, MCP and a worker | Native plugin | Codex plugin¹ |
| **claude-health** | [tw93](https://github.com/tw93/claude-health) | Health and wellness dashboard for Claude sessions | Native plugin | — |
| **pua / pua-en / pua-ja** | [tanweai](https://github.com/tanweai/pua) | Three Codex-specific productivity prompts with their references | — | Selected source |

### Storage

| Item | Source | What It Does | Claude | Codex |
| --- | --- | --- | --- | --- |
| **storage-analyzer** | [khazix-skills (modified)](https://github.com/KKKKhazix/khazix-skills/tree/fcba3adcf5def1ccd4bb688de93060227471b129/storage-analyzer) | Read-only disk analysis and an interactive HTML report with guarded cleanup; includes Linux support and security fixes | Bundled skill | Bundled skill |

### Academic Research

| Item | Source | What It Does | Claude | Codex |
| --- | --- | --- | --- | --- |
| **paper-reading** | [Repository](skills/paper-reading/) | Research paper reading, figure extraction, evidence checks and HTML reports | Bundled skill | Bundled skill |
| **tokenization** | [AI Research](https://github.com/Orchestra-Research/AI-research-SKILLs) | HuggingFace Tokenizers and SentencePiece | Native plugin | Selected source |
| **fine-tuning** | [AI Research](https://github.com/Orchestra-Research/AI-research-SKILLs) | Axolotl, LLaMA-Factory, PEFT and Unsloth | Native plugin | Selected source |
| **post-training** | [AI Research](https://github.com/Orchestra-Research/AI-research-SKILLs) | GRPO, OpenRLHF, SimPO, TRL and verl | Native plugin | Selected source |
| **inference-serving** | [AI Research](https://github.com/Orchestra-Research/AI-research-SKILLs) | vLLM, SGLang, TensorRT-LLM and llama.cpp | Native plugin | Selected source |
| **distributed-training** | [AI Research](https://github.com/Orchestra-Research/AI-research-SKILLs) | DeepSpeed, FSDP2, Megatron-Core and Ray Train | Native plugin | Selected source |
| **optimization** | [AI Research](https://github.com/Orchestra-Research/AI-research-SKILLs) | AWQ, GPTQ, GGUF, Flash Attention and bitsandbytes | Native plugin | Selected source |
| **deepxiv-cli** | [DeepXiv](https://github.com/DeepXiv/deepxiv_sdk) | arXiv / PMC hybrid paper search and reading CLI | Selected source | Selected source |
| **deepxiv-trending-digest** | [DeepXiv](https://github.com/DeepXiv/deepxiv_sdk) | Markdown digests of recently trending papers | Selected source | Selected source |
| **deepxiv-baseline-table** | [DeepXiv](https://github.com/DeepXiv/deepxiv_sdk) | Baseline comparison tables grounded in research papers | Selected source | Selected source |
| **ResearchStudio Idea** | [Microsoft](https://github.com/microsoft/ResearchStudio) | idea_spark, paper_search and scoop_check; complete source, first-use dependencies | Selected source | Selected source |
| **ResearchStudio Reel** | [Microsoft](https://github.com/microsoft/ResearchStudio) | paper2assets, paper2poster, paper2video, paper2blog and paper2reel; independently selected | — | Selected source |

### MCP Servers

| Item | Source | What It Does | Claude | Codex |
| --- | --- | --- | --- | --- |
| **Lark / Feishu** | [Lark](https://github.com/larksuite/lark-openapi-mcp) | Lark integration; supply credentials through the local environment / native setup | MCP | MCP |
| **GitHub** | [GitHub](https://github.com/github/github-mcp-server) | Repository and issue tools; requires authorization | — | MCP |
| **OpenAI docs** | [OpenAI](https://developers.openai.com/mcp) | Official OpenAI developer documentation | — | MCP |


¹ Claude-Mem has a Codex package with its own manifest, hooks, MCP and worker. The agent verifies the current package and native initialization; preserving a database or discovering a manifest alone does not prove the memory lifecycle works.

Complete bundle membership is listed in [catalog.md](catalog.md#members). Selected source revisions and adaptations are in [sources.md](platforms/sources.md). Storage analyzer modifications are documented in [UPSTREAM.md](skills/storage-analyzer/UPSTREAM.md) and submitted as [khazix-skills#50](https://github.com/KKKKhazix/khazix-skills/pull/50). Context7 and Playwright appear under Integrations and are not duplicated as separate MCP choices.

## Directory Structure

```text
.
├── README.md / README.zh-CN.md   # User guide and category tables
├── AGENTS.md / CLAUDE.md         # Instructions for working in this repository
├── INSTALL.md                   # Agent-guided installation and updates
├── MAINTAIN.md                  # Agent workflow for changing this repository
├── catalog.md                   # IDs, support, recommendations and routes
├── skills/                      # Author-owned and customized skill sources
├── platforms/
│   ├── claude/                  # Claude instructions, lessons, rules, hooks, skills
│   ├── codex/                   # Codex instructions, lessons, agents, skills
│   └── sources.md               # External revisions, members and adaptations
├── scripts/                     # Protected file operations and focused helpers
├── lessons.md                   # This repository's correction history
├── docs/                        # Showcases, spec and historical migration notes
└── install.sh / install.ps1     # Compatibility notices pointing to INSTALL.md
```

## Key Mechanisms

- **Agent-guided choices** — complete numbered lists, explanations and a record of the user's selections. Plugins and MCP servers are managed through the target agent's native tools; custom files use protected copies and partial merges.
- **Independent memory** — Claude uses its own global `lessons.md` plus project `memory/MEMORY.md`; Codex uses its own global `lessons.md` plus project-root `lessons.md`. Templates and real histories remain separate. Only missing global logs are seeded.
- **Layered rules and status lines** — Claude common rules extend into Python / TypeScript / Go; the gradient status line shows model, directory, venv, Git, context and usage. Codex has separate subagent templates and a native footer.
- **Repository-based updates** — record the repository URL, resolved revision and update policy. Follow the user-supplied branch, pinned commit, local checkout or explicitly chosen remote default. Installation and maintenance need no legacy Claude/Codex branches.
- **Scoped changes** — preserve user edits, credentials, hooks and memory databases. Backups and file ownership support safe updates and explicit removals. ResearchStudio Idea/Reel and PPT Master prepare complete source only; runtime dependencies are handled on first use.

## Settings Defaults

These are values from the current templates, applied only when the corresponding item is selected. Existing overrides are preserved and differences reported. Base settings, permissions, status lines and lessons are separate choices; Codex's auto-import setting is an installation prerequisite. The agent checks local version support before applying a setting.

| Agent | Key | Template value | Effect |
| --- | --- | --- | --- |
| Claude | `model` / `effortLevel` | `opus` / `xhigh` | Model and reasoning effort |
| Claude | `tui` | `fullscreen` | Fullscreen terminal interface |
| Claude | `env.CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | `1` | Enable the agent-teams experiment |
| Claude | `env.CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` | `1` | Request fixed thinking where the model supports it |
| Claude | `permissions.defaultMode` | `auto` | Separate permissions template also contains broad tool allowances |
| Codex | `model` / `model_reasoning_effort` | `gpt-5.6-sol` / `max` | Model and reasoning effort |
| Codex | `web_search` | `live` | Live web search |
| Codex | `features.multi_agent` / `concurrent_reasoning_summaries` | `true` / `false` | Agent collaboration and summary behavior |
| Codex | `shell_environment_policy.inherit` | `all` | Inherit the shell environment |
| Codex | `approval_policy` / `sandbox_mode` | `never` / `danger-full-access` | Separately selected high-autonomy permissions |
| Codex | `desktop.external-agent-import-sync-enabled` | `false` | Keep imports under explicit selection control |

Actual settings and per-item operations: [Claude](platforms/claude/README.md#configuration) · [Codex](platforms/codex/README.md#configuration). Current platform validation limits are recorded in [migration notes](docs/migration.md).

## Customization

You can ask the agent to maintain the repository itself. It follows [MAINTAIN.md](MAINTAIN.md), updates the complete payload and installation route, and keeps the catalogue and both READMEs consistent.

| Request | What the agent changes |
| --- | --- |
| “Add this skill and explain when to use it” | Local source for author-owned skills; upstream installation recipe for third-party originals, with support, category and usage description |
| “Update ResearchStudio” | Recorded upstream revision, members and necessary adaptations, verified in isolation |
| “Edit this skill / remove this option” | Current payload and references; removal records explain old IDs without silently uninstalling user copies |
| “Recommend these skills for Claude / Codex” | Only that agent's author recommendation markers |
| “Add language rules” | `platforms/claude/templates/rules/<lang>/` and its catalogue entry |
| “Change Claude / Codex instructions or lessons policy” | That agent's templates and matching memory rules |

To change your installed configuration instead, use [INSTALL.md](INSTALL.md). The root AGENTS.md, CLAUDE.md and lessons.md belong to this repository; deployable global files live under each platform's templates.

## Acknowledgements

- [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) — Anthropic Academy's official course
- [Working for 10 Claude Codes](https://mp.weixin.qq.com/s/9qPD3gXj3HLmrKC64Q6fbQ) by Hu Yuanming — multi-instance patterns
- [Harness Engineering](https://openai.com/index/harness-engineering/) by OpenAI
- [Anthropic Engineering](https://www.anthropic.com/engineering) / [OpenAI Engineering](https://openai.com/news/engineering/)
- [Claude Code Best Practice](https://github.com/shanraisshan/claude-code-best-practice) by shanraisshan
- [Claude How To](https://github.com/luongnv89/claude-howto) by luongnv89

## License

This repository is MIT. Bundled and fetched third-party components retain their own licenses. **lieflat-charts** uses [PolyForm Noncommercial 1.0.0](https://github.com/larashero3-dotcom/lieflat-charts/blob/main/LICENSE), for noncommercial use only; it is fetched only when selected and is not redistributed here.
