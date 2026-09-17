# Project Lessons

> Project-specific corrections for `awesome-claude-code-config`.
> Format: date, context, mistake, rule. Cross-project rules belong in `~/.codex/lessons.md`.

---

<!-- Keep repository-specific corrections here so they travel with this project. -->

<!--
Example lessons (invisible to `cat`, visible in editors):

## 2025-01-15
**Context**: Editing Python files
**Mistake**: Used `print()` for debugging in production code
**Rule**: Always use `logging` module instead of `print()`. Remove all `print()` before committing.

## 2025-02-03
**Context**: Running shell commands on user's machine
**Mistake**: Modified ~/.zshrc without being asked
**Rule**: Never modify shell config files (~/.bashrc, ~/.profile, ~/.zshrc) unless explicitly requested. Prefer project-local or user-space alternatives.
-->

## 2026-07-15 - Codex branch skills must be installed under `~/.codex`
**Context**: Fixing the split where updated Codex-branch skills appeared under `~/.agents/skills` while stale copies remained under `~/.codex/skills`.
**Mistake**: Treated the shared `~/.agents/skills` location used by `npx skills` as an acceptable Codex installation target.
**Rule**: The Codex branch owns `~/.codex`; every branch-managed skill, including skills fetched through `npx skills`, must be copied or installed there. Do not rely on `.agents/skills` discovery or leave it as the authoritative copy.

## 2026-07-13 - Keep this task's changes on codex-dev
**Context**: ResearchStudio evaluation and correction-memory routing in `awesome-claude-code-config`.
**Mistake**: Updated only the live `~/.codex/AGENTS.md` and treated the memory-routing request as machine-local, even though the user intended both it and the ResearchStudio work to be versioned Codex-branch changes.
**Rule**: Implement the project/global lessons routing in the repository's Codex AGENTS template and installers, keep the ResearchStudio integration on `codex-dev`, and do not modify Claude `main` or promote formal `codex` before user testing and confirmation.

## 2026-07-13 - Install only a blank global lessons log
**Context**: Separating installed global memory from per-project correction history.
**Mistake**: The old installer treated the repository-root `lessons.md` as the file to copy into every user's global Codex directory, conflating project history with global memory.
**Rule**: Seed `~/.codex/lessons.md` only from a blank global template. A project's root `lessons.md` is created by the agent on the first project-specific correction and then maintained as a project artifact, analogous to an on-demand `CHANGELOG.md`; never install or copy one project's lessons into global state.

## 2026-07-13 - ResearchStudio must be opt-in
**Context**: Adding ResearchStudio to the Codex Academic Research category.
**Mistake**: Although the interactive menu default was off, the first implementation still installed ResearchStudio through generic non-interactive `all` fallback paths, which could make a default no-TTY install opt in implicitly.
**Rule**: ResearchStudio is default-off everywhere. Install it only after an explicit menu selection, explicit `--all` / `-All`, or explicit AI-research skill-group request; ordinary default/fallback installs and dry-run-only mode must not install it.

## 2026-07-13 - Keep the ResearchStudio guide out of the repository
**Context**: Teaching the user how to use the optional ResearchStudio integration.
**Mistake**: Added a multi-file teaching guide under `docs/researchstudio-guide/`, even though the guide is personal reference material rather than a project artifact to upload.
**Rule**: Keep the user-facing ResearchStudio guide outside the repository and explain usage directly to the user. Version only the installer behavior and concise maintainer-facing documentation needed by this project.

## 2026-07-13 - Disclose ResearchStudio's Python dependency step
**Context**: A user explicitly selects the optional ResearchStudio item in the Codex installer.
**Mistake**: The installer requested upstream Python dependency installation with `RS_PIP=1` but did not clearly tell the user that four packages would be installed or that an upstream pip failure could require manual repair.
**Rule**: When ResearchStudio installation starts, display one concise notice naming the automatically requested Python packages and tell the user to run the connector check afterward because upstream pip failure is non-fatal.

## 2026-07-13 - Prefer a post-install ResearchStudio self-check
**Context**: Making ResearchStudio dependency failures actionable after an opt-in install.
**Mistake**: Added only a pre-install dependency notice, leaving the user to run and interpret the connector check manually even though the installer can perform that validation itself.
**Rule**: After the upstream ResearchStudio installer finishes, automatically run its `check_connectors` command. Print the check output and, when dependencies, credentials, or probes are degraded, tell the user exactly how to install the Python packages, where to add missing environment variables, and how to rerun the check.

## 2026-07-13 - Make self-check remediation instructional
**Context**: Reporting a degraded ResearchStudio post-install self-check.
**Mistake**: Summarized categories of corrective action without teaching the user the actual sequence or showing platform-appropriate commands and configuration examples.
**Rule**: Self-check remediation must be a numbered, copyable procedure: install packages with the active interpreter, show concrete Bash or PowerShell venv activation for PEP 668, show the `.env` key/value format without real secrets, protect the file where applicable, and finish with the exact rerun command. Missing Python or skill scripts must likewise include concrete install or reinstall commands.

## 2026-07-13 - Separate ResearchStudio Idea and Reel availability
**Context**: Mapping the official ResearchStudio project into the Codex Academic Research menu.
**Mistake**: Treated Reel's absence from the GitHub npx package as if Reel itself were unreleased, even though the official repository publishes five Reel skills and its full-checkout installer can install them.
**Rule**: Present two independent, default-off Academic Research entries: ResearchStudio Idea through the packaged official npx path, and ResearchStudio Reel through a full official checkout. Keep their ownership, dependencies, self-checks, removal, and quickstarts separate; state clearly that Reel needs native tools and Chromium beyond its Python packages.

## 2026-07-13 - Use one ResearchStudio installation model
**Context**: Installing the independent ResearchStudio Idea and Reel entries in the Codex Academic Research category.
**Mistake**: Mixed the packaged npx path for Idea with a source-checkout path for Reel, creating two installation, update, security-validation, and troubleshooting models for one upstream project.
**Rule**: Install both ResearchStudio entries from the official source repository. For each selected bundle, copy only an explicit skill allowlist after validating required `SKILL.md` files and rejecting links; install known dependencies explicitly, run bundle-specific self-checks, and never execute the upstream installer or use `sudo`.

## 2026-07-13 - Offer ppt-master as a full opt-in setup
**Context**: Restoring `hugohe3/ppt-master` to the Codex Slides category.
**Mistake**: Treated ppt-master's heavy environment as a reason to omit it completely, even though the user wants the complete capability when they explicitly select it.
**Rule**: Add ppt-master as an independent, default-off Slides item on `codex-dev`. A normal/default install must not touch it; an explicit selection must install the Codex skill together with its required runtime dependencies, run an actionable self-check, and explain any remaining platform or credential repair without silently claiming success.

## 2026-07-13 - Keep agent-authored tests out of uploaded branches
**Context**: Preparing the current `codex-dev` installer changes for the user to test and later upload.
**Mistake**: Added agent-authored regression scripts and TDD evidence files to the branch that the user intends to publish.
**Rule**: Use temporary/local tests to validate this repository's installer changes, but do not include agent-authored standalone test files or test-evidence documents in the uploaded branch unless the user explicitly asks for them. Existing tests may receive only the minimum compatibility edits required to remove assertions contradicted by the requested production change or initialize newly managed names; do not add new agent-authored test scenarios. Give the user a direct manual test command instead.

## 2026-07-13 - Prove the real installer works before handoff
**Context**: The user ran the Codex installer on a Node.js 18 / PEP 668 host after the ResearchStudio and PPT Master changes.
**Mistake**: Relied on mocked and structural checks without completing a clean end-to-end installer run on the actual host toolchain. `npx skills` failed under Node.js 18, Python `--user` installs failed under PEP 668, selected skills remained incomplete, and source copies were still reported as installed.
**Rule**: Before presenting or uploading installer changes, run the real installer in an isolated HOME using the host's actual Node/Python constraints and verify every selected component exists and passes its runtime self-check. Provide a runtime path that works on Node.js 18 and PEP 668 systems, and never print an installation-success message when required dependencies failed.

## 2026-07-13 - Reuse installer-managed runtimes before adding duplicates
**Context**: Adding browser-backed checks for optional ResearchStudio and ppt-master skills while the Codex installer already manages Playwright MCP and related browser tooling.
**Mistake**: Added a separate Python Playwright and Chromium installation to ppt-master before proving that its source required that exact runtime or attempting to reuse the installer-managed browser capability.
**Rule**: Inspect the selected skill's actual runtime calls and the installer-managed dependency first. Reuse a compatible existing runtime or browser cache when possible; install another Playwright package or browser only when the skill demonstrably needs a different API/runtime and no compatible shared installation is available.

## 2026-07-13 - Test each opt-in environment independently
**Context**: Verifying ppt-master after a combined full installer run.
**Mistake**: The combined run passed because ResearchStudio Reel had already installed Python Playwright and Chromium, masking that ppt-master's upstream `requirements.txt` omits its visual-review browser dependency.
**Rule**: Validate every default-off bundle in a fresh isolated HOME without sibling bundles. A bundle's installer and self-check must supply and prove its own required runtime while still reusing a compatible shared dependency when one genuinely exists.

## 2026-07-13 - Do not install dependencies for disabled connectors
**Context**: Running a clean ResearchStudio Idea install and observing its dependency closure.
**Mistake**: Included `scholarly` even though Google Scholar is disabled in the installed paper-search source list, causing unrelated Selenium and Sphinx packages to be installed.
**Rule**: Derive automatic dependencies from active execution paths, not every optional source file present upstream. Leave disabled connector dependencies uninstalled until that connector is explicitly enabled.

## 2026-07-13 - Distinguish agent-driven skill setup from script-level auto-install
**Context**: Explaining what happens when ResearchStudio Idea is invoked with missing dependencies.
**Mistake**: Claimed the skill would only degrade or fail because its Python scripts do not silently install packages, overlooking that Codex follows the skill's setup instructions and can proactively create a project-local venv and run `pip install` before continuing.
**Rule**: Inspect both executable scripts and `SKILL.md`/setup instructions before describing runtime dependency behavior. Call this an agent-driven setup when the agent performs it, and verify whether an installer-provisioned interpreter is actually reused before claiming that preinstallation prevents per-project environment creation.

## 2026-07-13 - Keep third-party research and slide skills minimally installed
**Context**: Finalizing the Codex installer entries for ResearchStudio Idea, ResearchStudio Reel, and PPT Master.
**Mistake**: Made the installer provision and probe each upstream skill's Python packages, Playwright browser, and native-tool environment even though the skills can handle or explain first-use setup themselves.
**Rule**: These three opt-in entries install only the skill source plus necessary Codex instruction/path adaptation. Do not create environments, install Python packages or browsers, or fail installation because runtime dependencies are absent; leave dependency setup to the invoked skill workflow.

## 2026-07-13 - Do not print redundant post-install skill guides
**Context**: Completing the minimal ResearchStudio Idea, ResearchStudio Reel, and PPT Master installation flow.
**Mistake**: Printed three long Quickstart blocks after installation even though Codex already exposes installed skills through its picker and each skill carries its own usage/setup instructions.
**Rule**: For these three opt-in entries, finish with the normal concise installer result only. Do not print separate post-install Quickstart, dependency, credential, browser-panel, or cross-skill guidance unless the user explicitly requests it.

## 2026-09-12
**Context**: Investigating the current Claude/Codex configuration and installation architecture.
**Mistake**: The initial assessment used stale local main/origin/codex snapshots and therefore described obsolete installer sizes and plugin defaults as the basis for recommendations.
**Rule**: Before assessing this repository's current installation design, compare local refs with remote heads and inspect the latest remote snapshots without replacing the working tree. Clearly distinguish local checkout, remote release, and actual installed state; do not present historical defaults as current ones.

## 2026-09-12
**Context**: Designing the next Claude/Codex installation architecture after platform research.
**Mistake**: The recommendations did not make the requested single-repository, single-installer experience concrete enough.
**Rule**: Design one shared catalogue and installer that detects OS and installed agents, filters unsupported capabilities per agent, and prefers that agent’s native plugin distribution when supported. Disable Codex automatic external-agent import as requested so the installer has explicit ownership; preserve platform-specific runtime configuration behind the shared entry point.

## 2026-09-12
**Context**: Choosing the unified Claude/Codex repository's installation experience.
**Mistake**: Proposed a Go executable, multi-platform releases, a resolver, and installer lifecycle machinery when the user wanted a simple agent-friendly repository.
**Rule**: Use agent-guided conversational installation as the primary interface: the agent reads concise repository instructions, detects the environment, explains supported options, reuses the user's stated preferences, and runs the appropriate native installation commands. Maintain shared skills and small platform-specific recipes; keep only deterministic helpers justified by risky or repetitive file operations. This supersedes the earlier standalone unified-installer recommendation; do not continue the binary/CLI/framework direction.

## 2026-09-12
**Context**: Clarifying the conversational installation catalogue during the grilling session.
**Mistake**: Proposed that the agent start with its own compact recommended selection instead of showing the full supported catalogue.
**Rule**: The repository author maintains separate Claude and Codex recommendations. The agent must list every eligible installation item for the target agent, grouped by category with numbers, mark author-recommended items, and let the user select. Agent explanations may clarify tradeoffs but must not replace the author's recommendations, hide unselected eligible items, or treat a recommendation marker as installation consent.

## 2026-09-12 - Unified development branch
**Context**: Implementing the confirmed agent-guided setup design.
**Rule**: Work from current main on `agent-config-for-agents`; use codex as a source of additional skills/configuration, preserve both source variants where they differ, and do not merge this work into either release branch.

## 2026-09-12 - Reuse the full macOS browser executable path in tests
**Context**: Running the preserved paper-reading browser tests through their Linux-style Chrome discovery path.
**Mistake**: Exposed only a symlink to the macOS Chrome binary; Chrome then looked for its Frameworks directory beside the symlink and failed to launch.
**Rule**: When adapting these tests to an installed macOS Chrome, use a temporary shell launcher that execs the real app executable path, with Playwright's isolated profile. Do not copy or relocate the browser binary or change the published skill payload to fix test environment discovery.

## 2026-09-12 - Distinguish menu coverage from enabled settings
**Context**: Counting preserved Claude plugin options while consolidating main and codex.
**Mistake**: Attributed all 21 offered plugins to settings.json and inferred their enabled/optional breakdown from a summary instead of the actual template.
**Rule**: Count settings keys, enabled values and installer menu entries separately. main has 20 settings selectors (15 true, 5 false), with Matt offered additionally by the menu; source coverage is their union, not the enabled-only subset.

## 2026-09-12 - Maintain one independent repository, with the original README experience
**Context**: Refining the unified repository before it becomes the primary development line and the old Claude/Codex branches become legacy archives.
**Mistake**: Framed the repository around preserving two release branches, hard-coded the development branch in update entrypoints, and replaced main's detailed README categories, usage guidance and tables with a short landing page.
**Rule**: Treat this repository's current contents as the installation and maintenance authority. Legacy branch names and snapshot mappings are historical provenance only, never required for installation, updates or skill edits. Preserve main's README category order, showcases, practical usage sections and tables while merging both agents' skills and showing support/recommendations separately. Keep each agent's global instructions and lesson templates/state independent. Document how the agent adds, updates and removes skills and keeps catalogue, README and recipes consistent. Do not rename/archive branches or change the remote default merely because that is the user's future plan.

## 2026-09-12 - Keep upstream skills at their upstream source
**Context**: Refining ownership in the unified skill repository.
**Mistake**: Treated existing bundled third-party skill copies as shared repository payloads without distinguishing upstream ownership from locally maintained work.
**Rule**: For third-party skills, publish the upstream installation method and source instead of maintaining a duplicate payload here. Keep the user's own skills in this repository. Inspect local adaptations before moving a derived skill upstream; preserve intentionally maintained custom versions unless the user chooses the upstream version, and keep catalogue, READMEs and recipes aligned.

## 2026-09-12 - Handoff belongs to the Matt bundle
**Context**: Deciding which derived skills remain local in the unified repository.
**Mistake**: Kept handoff as an independent Codex option and local customized payload when the user wants it only within Matt skills.
**Rule**: Offer handoff solely as a member of matt-workflow. Use the selected Matt source, remove the independent catalogue entry and local handoff copy, and document the old handoff ID as a migration to the bundle. Existing installations are migrated only when requested. This supersedes earlier requirements to preserve the customized handoff variant.

## 2026-09-12 - Offer AI Research as one bundle
**Context**: Simplifying the unified Academic Research catalogue.
**Mistake**: Offered the six AI Research groups as separate top-level installation choices.
**Rule**: Present one ai-research bundle containing tokenization, fine-tuning, post-training, inference-serving, distributed-training and optimization. Keep each group's members visible and retain the platform's upstream installation methods. Legacy partial selections do not authorize adding the rest of the bundle.
**Clarification**: The author explicitly selected the complete upstream 31-member AI Research bundle for both agents, replacing Codex's 24-member curation for new bundle installs. Existing partial installations still require an explicit migration choice before adding members.

## 2026-09-13 - Replace Claude common rules with the full writing rule
**Context**: Revising the Claude writing instructions and auditing configuration consistency.
**Mistake**: The initial change placed a condensed writing section in the CLAUDE.md template; the author subsequently requested the complete English version as a rule instead.
**Rule**: Remove the other Claude common rules and place the complete English translation, including examples, in one writing rule. Remove the duplicate condensed template section. Keep the language-specific rules unless separately requested, and reconcile their references with the new common rule layout.

## 2026-09-13 - Associate update skills with the active development branch
**Context**: Connecting update-config to the branch the author is developing.
**Mistake**: The generic recorded-source workflow did not explicitly associate the update skills with this development branch.
**Rule**: Both update skills must identify Mizoreww/awesome-claude-code-config and agent-config-for-agents as their update target. Keep installation choices, ownership and customizations; handle conflicting source records explicitly. This supersedes the earlier prohibition on naming the development branch in these update entrypoints, without making archived Claude/Codex branches installation dependencies.

## 2026-09-13 - Read exact text before document replacements
**Context**: Synchronizing bilingual README and configuration changes.
**Mistake**: Repeatedly prepared text replacements from remembered wording, causing patch failures and one partially updated bilingual pair.
**Rule**: Read the exact current lines before replacements; use verified anchors, check each file's resulting state after a failed batch, and complete bilingual synchronization before validation.


## 2026-09-17 - Present installation choices in the conversation
**Context**: A user asked an agent to install this repository, but received a generated Markdown document instead of usable choices in the conversation.
**Mistake**: The installation instructions required a catalogue but did not make its delivery surface and question interaction explicit enough.
**Rule**: Present the current target agent's complete supported catalogue directly in the conversation, grouped and numbered with useful descriptions, author recommendations and installed status. Prefer the host's real multi-select question UI when available; respect its actual limits, and otherwise accept multiple numbers/names in chat. Keep all eligible options visible, reuse explicit selections, and wait for an actual response where selection is still missing. Do not replace this interaction with a generated Markdown/report file or a link to one unless the user requests an export. Installation receipts are separate from the user-facing choices.


## 2026-09-17 - Retire redundant Codex role presets
**Context**: The author questioned the Core explorer, reviewer and docs-researcher entries and requested their removal after checking their origin.
**Mistake**: Kept legacy custom role presets as recommended Core installation items, adding fixed model and concurrency settings to ordinary Codex setup.
**Rule**: Retire agent-explorer, agent-reviewer and agent-docs-researcher from this branch's catalogue, recommendations, templates and registration patches. Keep Codex's native multi-agent capability and the selected review/documentation skills available. Historical provenance and existing user installations remain traceable; retiring repository presets does not authorize deleting live custom agents or disabling native subagents.


## 2026-09-17 - Retire GitHub MCP installation options
**Context**: The author requested removal of GitHub MCP from both Claude and Codex offerings.
**Mistake**: Continued offering the legacy GitHub integration through a recommended MCP/plugin entry after the repository had moved toward fewer explicit integrations.
**Rule**: Retire the github catalogue item, its MCP configuration and install recipes, and its plugin replacement route for both targets. Keep unrelated GitHub source links, Git/gh workflows and review skills intact. Preserve existing external integrations and credentials unless their live removal is explicitly requested; ordinary updates do not reinstall the retired item through another channel.
