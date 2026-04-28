# Awesome Agent Skills

> 精选与 AI Agent、Skills 相关的 GitHub 热门项目日报

---

## 📅 2026-04-27 GitHub Agent热门仓库日报

| 排名 | 仓库 | ⭐ Stars | 📈 今日新增 | 语言 | 核心亮点 |
|------|------|---------|-----------|------|----------|
| 🥇 1 | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 53,312 | +183 | Python | 多Agent协作的LLM金融交易框架 |
| 🥈 2 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | 30,723 | +700 | TypeScript | 零服务端代码智能引擎 + Graph RAG Agent |
| 🥉 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | 26,788 | +2,519 | Shell | 真实工程师的Agent技能集，20+技能 |
| 4 | [gastownhall/beads](https://github.com/gastownhall/beads) | 21,932 | +152 | Go | 编码Agent的持久化记忆与图问题追踪器 |
| 5 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | 2,364 | +517 | Python | 40+实用Codex技能精选列表 |

---

## 🔥 热门仓库详细介绍

### 1. TauricResearch/TradingAgents

**🔗 链接**: https://github.com/TauricResearch/TradingAgents
**⭐ Star数**: 53,312 | **🍴 Fork**: 9.7k | **语言**: Python | **许可证**: Apache-2.0

#### 📋 简介
TradingAgents 是一个模仿真实交易公司运作的多Agent交易框架。通过部署专业化的LLM驱动的Agent——从基本面分析师、情绪专家、技术分析师到交易员和风险管理团队——平台协同评估市场状况并做出交易决策。这些Agent通过动态讨论来寻找最优策略。

#### 🚀 核心架构

| 团队 | Agent角色 | 职责 |
|------|----------|------|
| **分析师团队** | 基本面分析师 | 评估公司财务和业绩指标，识别内在价值 |
| | 情绪分析师 | 分析社交媒体和公众情绪，衡量短期市场情绪 |
| | 新闻分析师 | 监控全球新闻和宏观经济指标 |
| | 技术分析师 | 使用MACD、RSI等技术指标检测交易模式 |
| **研究团队** | 看多/看空研究员 | 通过结构化辩论平衡潜在收益与风险 |
| **交易员** | 交易Agent | 综合分析师和研究员报告做出交易决策 |
| **风控** | 风险管理 + 投资组合经理 | 评估投资组合风险，审批/否决交易提案 |

#### 💎 核心特性
- **多LLM提供商**：支持 OpenAI、Google、Anthropic、xAI、DeepSeek、Qwen、GLM、Ollama、Azure
- **持久化决策日志**：每次运行自动记录决策，下次分析时注入历史反思
- **检查点恢复**：基于 LangGraph 的断点续跑，崩溃后从上次成功步骤恢复
- **结构化输出**：Research Manager、Trader、Portfolio Manager 均采用结构化输出
- **CLI + Python API**：交互式命令行和编程接口双模式
- **Docker 支持**：一键容器化部署，含 Ollama 本地模型配置

#### 📖 快速上手
```python
from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

ta = TradingAgentsGraph(debug=True, config=DEFAULT_CONFIG.copy())
_, decision = ta.propagate("NVDA", "2026-01-15")
print(decision)
```

---

### 2. abhigyanpatwari/GitNexus

**🔗 链接**: https://github.com/abhigyanpatwari/GitNexus
**⭐ Star数**: 30,723 | **🍴 Fork**: 3.5k | **语言**: TypeScript (98%) | **许可证**: PolyForm Noncommercial

#### 📋 简介
GitNexus 是零服务端代码智能引擎，为AI Agent构建代码库的"神经系统"。它将代码库索引为知识图谱——追踪每一个依赖、调用链、集群和执行流程——然后通过智能工具将上下文暴露给AI Agent，使其不再遗漏代码。

> *类似 DeepWiki，但更深入。DeepWiki 帮你理解代码，GitNexus 让你分析代码——因为知识图谱追踪每一条关系，而不仅仅是描述。*

#### 🚀 核心创新：预计算关系智能

| 对比维度 | 传统 Graph RAG | GitNexus |
|----------|---------------|----------|
| **查询方式** | LLM 多轮探索图边 | 工具一次调用返回完整上下文 |
| **可靠性** | LLM 可能遗漏上下文 | 预计算结构，上下文已内置 |
| **Token效率** | 10+查询链才理解一个函数 | 1次查询即可 |
| **模型要求** | 需要大模型 | 小模型也能获得架构级理解 |

#### 💎 核心特性
- **16个MCP工具**：query、context、impact、detect_changes、rename、cypher 等
- **影响分析**：追踪上游/下游依赖，按深度分层，标注置信度
- **360°上下文视图**：任意符号的入站/出站调用、导入、所属进程
- **多仓库MCP架构**：全局注册表，一个MCP服务器服务多个索引仓库
- **14种语言支持**：TypeScript、Python、Java、Go、Rust、C#、Kotlin 等
- **双模式**：CLI + MCP（本地开发） / Web UI（浏览器快速探索）
- **4个Agent Skills**：自动安装探索、调试、影响分析、重构技能
- **Wiki生成**：从知识图谱自动生成 LLM 驱动的文档

#### 📖 快速上手
```bash
# 一键索引（安装Agent Skills + 注册Hooks + 生成AGENTS.md）
npx gitnexus analyze

# 配置MCP
npx gitnexus setup
```

---

### 3. mattpocock/skills

**🔗 链接**: https://github.com/mattpocock/skills
**⭐ Star数**: 26,788 | **🍴 Fork**: 2.1k | **语言**: Shell | **许可证**: MIT

#### 📋 简介
Matt Pocock 的个人Agent技能集合，直接来源于他的 `.claude` 目录。这些技能用于日常真实工程工作——不是vibe coding，而是真正的工程实践。包含 **20个技能**，覆盖从规划到交付的完整开发流程。

#### 🚀 技能分类

| 类别 | 技能 | 一句话描述 |
|------|------|-----------|
| **规划与设计** | `to-prd` | 对话上下文→PRD→GitHub Issue |
| | `to-issues` | 将计划拆分为可独立认领的垂直切片Issues |
| | `grill-me` | 对设计方案进行无死角追问，遍历决策树的每个分支 |
| | `design-an-interface` | 并行子Agent生成多个截然不同的接口设计 |
| | `request-refactor-plan` | 通过用户访谈创建详细重构计划 |
| **开发** | `tdd` | 红-绿-重构循环的测试驱动开发 |
| | `triage-issue` | 探索代码库定位Bug根因，生成含TDD修复计划的Issue |
| | `improve-codebase-architecture` | 基于领域语言和ADR发现代码库深度优化机会 |
| **工具与配置** | `setup-pre-commit` | 配置 Husky + lint-staged + Prettier + 类型检查 + 测试 |
| | `git-guardrails-claude-code` | Claude Code Hooks拦截危险git命令 |
| **写作与知识** | `write-a-skill` | 创建新技能（带结构和渐进披露） |
| | `edit-article` | 文章编辑：重构段落、提升清晰度、精简文字 |
| | `ubiquitous-language` | 提取DDD风格的通用语言词汇表 |
| | `obsidian-vault` | 搜索、创建和管理Obsidian知识库笔记 |

#### 📖 使用方法
```bash
npx skills@latest add mattpocock/skills/<技能名>
```

#### 💎 核心优势
- **实战驱动**：来自日常工程实践，不是玩具Demo
- **开箱即用**：一条 `npx` 命令安装
- **全流程覆盖**：规划→设计→开发→测试→部署→知识管理
- **安全防护**：内置Git危险操作防护机制

---

### 4. gastownhall/beads

**🔗 链接**: https://github.com/gastownhall/beads
**⭐ Star数**: 21,932 | **🍴 Fork**: 1.4k | **语言**: Go (94.2%) | **许可证**: MIT

#### 📋 简介
Beads 是面向AI编码代理的分布式图问题追踪器，由 Dolt（版本控制的SQL数据库）驱动。核心使命是为编码代理提供持久化、结构化的记忆系统——用依赖感知的图结构替代混乱的markdown计划，让Agent在长周期任务中不丢失上下文。

#### 🚀 核心特性

| 特性 | 说明 |
|------|------|
| **Dolt驱动** | 版本控制SQL数据库，支持单元格级合并、原生分支、内置远程同步 |
| **零冲突** | 哈希ID（`bd-a1b2`），多Agent/多分支工作流无合并冲突 |
| **记忆压缩** | 语义"记忆衰减"——自动摘要已关闭的旧任务，节省上下文窗口 |
| **消息系统** | 线程消息（`--thread`）、临时生命周期、邮件委托 |
| **图链接** | `relates_to`、`duplicates`、`supersedes`、`replies_to` 知识图谱关系 |
| **层级ID** | Epic（`bd-a3f8`）→ Task（`bd-a3f8.1`）→ Sub-task（`bd-a3f8.1.1`） |
| **多模式** | 嵌入式（默认）/ 服务器 / 隐蔽 / 贡献者模式 |

#### 💎 核心优势
- **解决Agent记忆问题**：持久化结构化记忆替代易丢失的markdown
- **依赖感知**：`bd ready` 自动识别无阻塞可执行任务
- **多Agent协作零冲突**：哈希ID机制确保并发安全
- **上下文窗口优化**：记忆压缩机制自动管理上下文空间
- **Git可选**：支持非Git VCS（Sapling、Jujutsu）和CI/CD场景
- **89个版本发布**：活跃迭代，最新版 v1.0.3

#### 📖 快速上手
```bash
brew install beads
cd your-project && bd init
bd ready                     # 列出可执行任务
bd create "Fix auth bug" -p 0  # 创建P0任务
bd update <id> --claim       # 原子认领任务
```

---

### 5. ComposioHQ/awesome-codex-skills

**🔗 链接**: https://github.com/ComposioHQ/awesome-codex-skills
**⭐ Star数**: 2,364 | **🍴 Fork**: 171 | **语言**: Python

#### 📋 简介
实用Codex技能的精选列表，用于在 Codex CLI 和 API 之间自动化工作流。Codex Skills 是模块化的指令包，告诉 Codex 如何按照你的期望执行任务——每个技能拥有独立的 `SKILL.md` 元数据和步骤指引。

#### 🚀 技能分类

| 类别 | 代表技能 | 功能 |
|------|---------|------|
| **开发与代码工具** | `codebase-migrate` | 大型代码库迁移，可审查批次+CI验证 |
| | `gh-fix-ci` | 检查失败的GitHub Actions，提出修复 |
| | `mcp-builder` | 构建和评估MCP服务器 |
| | `sentry-triage` | 将Sentry堆栈帧映射到本地源码诊断问题 |
| **生产力与协作** | `connect` | 连接1000+应用（Slack、GitHub、Notion等） |
| | `notion-*`系列 | Notion知识捕获/会议智能/研究文档/规格转实现 |
| | `meeting-notes-and-actions` | 会议转录→摘要+决策+行动项 |
| **沟通与写作** | `email-draft-polish` | 邮件起草、改写、精简 |
| | `changelog-generator` | 从提交或摘要生成变更日志 |
| | `content-research-writer` | 带来源引用的研究和内容起草 |
| **数据与分析** | `spreadsheet-formula-helper` | 电子表格公式编写和调试 |
| | `helium-mcp` | 实时新闻搜索+偏见评分+市场数据 |
| **元工具** | `skill-creator` | 技能构建指南 |
| | `template-skill` | 新技能起始模板 |

#### 💎 核心优势
- **模块化设计**：渐进式披露——元数据决定触发时机，主体内容按需加载
- **1000+应用集成**：通过 Composio CLI 实现真实操作（邮件、Issue、Slack等）
- **标准化结构**：`SKILL.md` + `scripts/` + `references/` + `assets/`
- **一键安装**：Skill Installer 从GitHub路径直接安装

#### 📖 快速上手
```bash
python skill-installer/scripts/install-skill-from-github.py \
  --repo ComposioHQ/awesome-codex-skills \
  --path meeting-notes-and-actions
```

---

## 📊 今日趋势洞察

| 趋势 | 详情 |
|------|------|
| **Agent多角色协作成为主流** | TradingAgents 用6+专业Agent模拟真实交易团队，标志着单Agent→多Agent协作的范式转变 |
| **Skills生态爆发** | `mattpocock/skills`日增2,519星领跑，`awesome-codex-skills`日增517星，Skills正成为Agent标准交互方式 |
| **Agent记忆与上下文是核心痛点** | `beads`（持久化记忆）和`GitNexus`（代码知识图谱）都在解决Agent上下文丢失问题 |
| **预计算优于实时推理** | GitNexus的"预计算关系智能"思路——索引时预计算结构而非运行时多轮查询——代表了Agent工具设计的新方向 |
| **Claude/Codex生态主导** | 5个仓库中4个与Claude Code或Codex直接集成，OpenAI Agent生态仍在追赶 |

---

*本日报由自动化任务生成，每日更新 | 数据来源：GitHub Trending*

---

## 📅 2026-04-28 GitHub Trending - Agent/Skills 精选

> 自动筛选自 GitHub Trending，聚焦 AI Agent 和 Skills 相关的热门仓库

---

### 1. DeepSeek-V3

| 项目 | 详情 |
|------|------|
| **仓库** | [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) |
| **⭐ Stars** | 103,117 |
| **简介** | DeepSeek-V3 是由深度求索(DeepSeek)开发的第三代大语言模型，采用创新的MoE架构，拥有671B总参数和37B激活参数。支持128K长上下文，在代码生成、数学推理和多语言处理方面表现卓越，训练成本仅557万美元，性价比极高。 |

**核心特性：**
- MoE架构(671B参数)
- 128K长上下文支持
- 高效推理与训练
- 多语言与代码能力
- 开源可商用

---

### 2. TradingAgents

| 项目 | 详情 |
|------|------|
| **仓库** | [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) |
| **⭐ Stars** | 53,840 |
| **简介** | TradingAgents 是一个基于多智能体LLM的金融交易框架。通过模拟真实交易公司的团队协作机制，让多个AI智能体分别扮演不同角色(分析师、策略师、交易员等)进行协作决策，实现更智能的量化交易策略生成。 |

**核心特性：**
- 多智能体协作架构
- 模拟真实交易团队
- 角色分工明确
- 自主交易决策
- 支持回测验证

---

### 3. skills

| 项目 | 详情 |
|------|------|
| **仓库** | [mattpocock/skills](https://github.com/mattpocock/skills) |
| **⭐ Stars** | 30,638 |
| **简介** | Matt Pocock 的 Claude Skills 集合，专为 Claude Code 设计的实用技能库。包含大量经过实战验证的提示词模板和最佳实践，帮助开发者更高效地使用 Claude 进行代码审查、重构、测试编写等开发任务。 |

**核心特性：**
- Claude Code优化技能
- 实战验证模板
- 代码审查技能
- 重构与测试技能
- 持续更新维护

---

### 4. claude-code-templates

| 项目 | 详情 |
|------|------|
| **仓库** | [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) |
| **⭐ Stars** | 25,804 |
| **简介** | Claude Code Templates 是一个CLI工具，用于配置和监控 Claude Code 项目。提供标准化的项目模板、配置管理和监控功能，帮助团队快速搭建基于Claude的开发环境，提升AI辅助编程效率。 |

**核心特性：**
- CLI配置工具
- 标准化项目模板
- 实时监控功能
- 团队协作支持
- 易用的命令行接口

---

### 5. free-claude-code

| 项目 | 详情 |
|------|------|
| **仓库** | [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code) |
| **⭐ Stars** | 16,198 |
| **简介** | Free Claude Code 项目让用户可以在终端、VSCode等环境中免费使用 Claude Code 功能。通过巧妙的API封装和本地代理，实现了无需付费订阅即可体验Claude强大的代码辅助能力。 |

**核心特性：**
- 免费使用Claude Code
- 终端与IDE集成
- 本地代理服务
- VSCode插件支持
- 开源替代方案

---

📊 *本报告由自动化任务生成于 2026-04-28*

🔍 *筛选关键词: agent, agents, skill, skills, ai, claude, llm, mcp, copilot, automation, bot*
