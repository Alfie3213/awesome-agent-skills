# Awesome Agent Skills

> 精选与 AI Agent、Skills 相关的 GitHub 热门项目日报

---

## 📅 2026-04-27 GitHub Agent热门仓库日报

| 排名 | 仓库 | ⭐ Stars | 语言 | 核心亮点 |
|------|------|---------|------|----------|
| 🥇 1 | [mattpocock/skills](https://github.com/mattpocock/skills) | 25,163 | Shell | 真实工程师的Agent技能集，覆盖全流程 |
| 🥈 2 | [trycua/cua](https://github.com/trycua/cua) | 14,535 | Python | Computer-Use Agent完整基础设施 |
| 🥉 3 | [gastownhall/beads](https://github.com/gastownhall/beads) | 21,817 | Go | 编码Agent的分布式图问题追踪器 |
| 4 | [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | 30,431 | TypeScript | 零服务端代码智能引擎+Graph RAG Agent |
| 5 | [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | 2,198 | Python | 40+实用Codex技能精选列表 |

---

## 🔥 热门仓库详细介绍

### 1. mattpocock/skills

**🔗 链接**: https://github.com/mattpocock/skills  
**⭐ Star数**: 25,163 | **🍴 Fork**: 2k | **语言**: Shell

#### 📋 简介
Matt Pocock 的个人代理技能集合，直接来源于他的 `.claude` 目录。这些技能用于日常真实工程工作，强调"real engineering"而非花哨的演示代码。

#### 🚀 主要特性
包含 **18个技能**，分为四大类：

| 类别 | 技能示例 |
|------|----------|
| **规划与设计** | `to-prd` - 对话转PRD；`to-issues` - 拆分为Issues；`grill-me` - 设计面试追问 |
| **开发** | `tdd` - 测试驱动开发；`triage-issue` - Bug根因调查；`improve-codebase-architecture` - 架构优化 |
| **工具与配置** | `setup-pre-commit` - 配置Git钩子；`git-guardrails-claude-code` - Git安全保护 |
| **写作与知识** | `write-a-skill` - 创建新技能；`edit-article` - 文章编辑；`obsidian-vault` - Obsidian知识库管理 |

#### 📖 使用方法
```bash
npx skills@latest add mattpocock/skills/<技能名>
```

#### 💎 核心优势
- 实战驱动：直接来自日常工程实践
- 开箱即用：一条命令安装，无需复杂配置
- 全流程覆盖：从规划设计→编码开发→工具配置→知识管理
- 安全防护：内置Git危险操作防护

---

### 2. trycua/cua

**🔗 链接**: https://github.com/trycua/cua  
**⭐ Star数**: 14,535 | **🍴 Fork**: 910 | **语言**: Python/HTML/Swift

#### 📋 简介
Computer-Use Agents的开源基础设施，提供沙箱、SDK和基准测试，用于训练和评估能够控制完整桌面环境（macOS/Linux/Windows/Android）的AI Agent。

#### 🚀 主要特性

| 组件 | 功能描述 |
|------|----------|
| **Cua Driver** | 后台驱动原生macOS应用，不抢占光标和焦点；支持Chromium和Canvas工具 |
| **Cua Sandbox** | 跨OS统一API，支持云和本地(QEMU)部署 |
| **CuaBot** | 多代理协作计算机使用，支持H.265、共享剪贴板和音频 |
| **Cua-Bench** | 在OSWorld/ScreenSpot/Windows Arena等数据集上评估代理 |
| **Lume** | 基于Apple Virtualization.Framework的macOS/Linux虚拟化 |

#### 📖 使用方法
```bash
# 安装Driver
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/cua-driver/scripts/install.sh)"

# Python SDK
pip install cua

# 使用Sandbox
from cua import Sandbox, Image
async with Sandbox.ephemeral(Image.linux()) as sb:
    result = await sb.shell.run("echo hello")
    screenshot = await sb.screenshot()
```

#### 💎 核心优势
- 跨平台统一API：一套代码控制多OS沙箱
- 后台无侵入：不抢占用户光标和焦点
- MCP集成：与Claude Code、Cursor等工具直接集成
- Apple Silicon原生优化：接近原生性能

---

### 3. gastownhall/beads

**🔗 链接**: https://github.com/gastownhall/beads  
**⭐ Star数**: 21,817 | **🍴 Fork**: 1.4k | **语言**: Go (94.1%)

#### 📋 简介
面向AI编码代理的分布式图问题追踪器，由Dolt（版本控制的SQL数据库）驱动。核心定位是为编码代理提供持久化、结构化的记忆系统，用依赖感知的图结构替代混乱的markdown计划。

#### 🚀 主要特性

| 特性 | 说明 |
|------|------|
| **Dolt驱动** | 版本控制SQL数据库，支持单元格级合并和原生分支 |
| **零冲突** | 基于哈希的ID（`bd-a1b2`），防止多代理/多分支合并冲突 |
| **记忆压缩** | 语义"记忆衰减"，自动摘要旧任务，节省上下文窗口 |
| **图链接** | 支持relates_to、duplicates、supersedes、replies_to关系 |
| **层级ID** | Epic→Task→Sub-task层级结构 |
| **灵活模式** | 嵌入式/服务器/隐蔽/贡献者多种模式 |

#### 📖 使用方法
```bash
# 安装
brew install beads

# 初始化
cd your-project
bd init

# 核心命令
bd ready          # 列出可执行任务
bd create "Title" -p 0   # 创建P0任务
bd update <id> --claim   # 原子认领任务
bd dep add <child> <parent>  # 链接任务依赖
```

#### 💎 核心优势
- 解决代理记忆问题：持久化结构化记忆替代易丢失的markdown
- 依赖感知：自动识别无阻塞可执行任务
- 多代理协作零冲突：哈希ID机制
- 上下文窗口优化：记忆压缩机制
- Git可选：支持非Git VCS和CI/CD场景

---

### 4. abhigyanpatwari/GitNexus

**🔗 链接**: https://github.com/abhigyanpatwari/GitNexus  
**⭐ Star数**: 30,431 | **🍴 Fork**: 3.5k | **语言**: TypeScript (98%)

#### 📋 简介
零服务端代码智能引擎，完全在浏览器中运行的客户端知识图谱创建器。为AI Agent构建上下文的神经系统——将代码库索引为知识图谱，追踪每一个依赖、调用链、集群和执行流程。

#### 🚀 主要特性

| 功能 | 描述 |
|------|------|
| **知识图谱构建** | 多阶段索引：结构分析→解析→跨文件解析→聚类→流程追踪→搜索 |
| **16个MCP工具** | list_repos、query、context、impact、detect_changes、rename、cypher等 |
| **影响分析** | 追踪上游/下游依赖，按深度分层，标注置信度 |
| **360°上下文视图** | 对任意符号展示：入站调用、出站调用、导入、所属进程 |
| **多文件重命名** | 图谱高置信度编辑 + 文本搜索补充 |
| **Wiki生成** | 从知识图谱自动生成LLM驱动的文档 |

#### 📖 使用方法
```bash
# 全局安装
npm install -g gitnexus

# 一键索引
npx gitnexus analyze

# 配置MCP
npx gitnexus setup

# 常用命令
gitnexus analyze [path]      # 索引仓库
gitnexus serve               # 启动本地HTTP服务器
gitnexus wiki [path]         # 生成Wiki
```

#### 💎 核心优势
- 预计算关系智能：索引时预计算结构，一次调用返回完整上下文
- 完全本地/浏览器端：零隐私风险，代码不上传服务器
- 深度编辑器集成：Claude Code获得MCP+技能+Hooks完整支持
- 小模型大能力：预计算工具让小模型具备架构级理解力
- 支持14种编程语言：TypeScript、Python、Java、Go、Rust等

---

### 5. ComposioHQ/awesome-codex-skills

**🔗 链接**: https://github.com/ComposioHQ/awesome-codex-skills  
**⭐ Star数**: 2,198 | **🍴 Fork**: 165 | **语言**: Python

#### 📋 简介
实用Codex技能的精选列表，用于在Codex CLI和API之间自动化工作流。包含40+实用技能，由ComposioHQ维护。

#### 🚀 主要特性

| 类别 | 技能示例 |
|------|----------|
| **开发与代码工具** | `codebase-migrate` - 大型代码库迁移；`gh-fix-ci` - 修复GitHub Actions；`mcp-builder` - 构建MCP服务器 |
| **生产力与协作** | `connect` - 连接1000+应用；`notion-*`系列 - Notion集成；`meeting-notes-and-actions` - 会议智能 |
| **沟通与写作** | `email-draft-polish` - 邮件润色；`changelog-generator` - 变更日志生成 |
| **数据与分析** | `spreadsheet-formula-helper` - 公式助手；`helium-mcp` - 实时新闻搜索 |
| **元工具** | `template-skill` - 技能模板；`skill-creator` - 技能构建指南 |

#### 📖 使用方法
```bash
# 克隆并安装
python skill-installer/scripts/install-skill-from-github.py \
  --repo ComposioHQ/awesome-codex-skills \
  --path meeting-notes-and-actions

# 验证安装
ls ~/.codex/skills
```

#### 💎 核心优势
- 模块化设计：渐进式披露，仅在需要时加载主体内容
- 1000+应用集成：通过connect技能实现真实操作（邮件、议题、Slack等）
- 标准化结构：易于创建和共享的标准格式
- 一键安装：Skill Installer让安装只需一条命令

---

## 📊 今日趋势洞察

| 趋势 | 详情 |
|------|------|
| **AI Agent生态爆发** | 5个热门仓库中有5个与Agent/Skills直接相关 |
| **Skills成为热门概念** | `mattpocock/skills`和`awesome-codex-skills`直接以skills为核心 |
| **Agent基础设施完善** | `trycua/cua`提供沙箱和SDK，`beads`提供内存增强，`GitNexus`提供代码理解 |
| **Claude生态关联** | 多个仓库（skills、openclaw）与Claude AI生态相关 |
| **今日增长冠军** | `mattpocock/skills`以日增2,519 stars领跑 |

---

*本日报由自动化任务生成，每日更新 | 数据来源：GitHub Trending*
