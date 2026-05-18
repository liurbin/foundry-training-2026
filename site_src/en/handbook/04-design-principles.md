# Training Design Principles: AI-Native Developer Edition

> Bilingual mirror. Original source: `docs/04-design-principles.md`.

## English Guide

This is the instructor-facing bilingual mirror for the handbook page. Use the English heading for navigation and the Chinese source below as the complete canonical delivery material.

- Chinese canonical title: 培训设计原则：AI 原生开发者版
- English navigation title: Training Design Principles: AI-Native Developer Edition
- Scope: this page is part of the full bilingual Foundry training site.

## Chinese Source with Bilingual Headings

# Training Design Principles: AI-Native Developer Edition / 培训设计原则：AI 原生开发者版

> 本文档是后续所有培训材料（议程、讲师手册、评估题、综合作业、改造 fork）的**源头依据**。
> 画像或原则有变化时，先改本文档，再派生议程和手册。

## 定位声明

> **本培训不是 Foundry API 速成，也不是泛 AI-pair 编程课，而是面向 AI 原生开发者的 Foundry 能力掌握课。**
>
> AI 负责生成实现细节；讲师负责讲清 **Foundry 的平台能力、能力边界、组合路径和生产化取舍**。

这一句话决定了所有后续设计：

- 不是"教 Foundry API"——AI 比讲师讲得快、讲得全
- 不是"教 AI-pair"——学员已经熟手，不需要重学
- 是"教 Foundry 这个具体平台的能力地图与工程取舍"——这是 AI 不知道、讲师真正有价值的地方

---

## 一、Learner画像 / 一、学员画像

**AI 原生开发者熟手**：

| 维度 | 具象描述 |
|------|---------|
| 工具栈 | Claude Code / Codex / GitHub Copilot 飞起，vibe coding 是日常 |
| 节奏 | 3 天内出能演示的 MVP，不接受"30 天 POC"的传统培训节奏 |
| 关心 | 成本、scaling、可移植、红队、生产化——从第一天就要 |
| 角色 | 混合（startup 工程师 + partner SA/实施），但**不区分身份**，共同语言是"快速生产级" |
| 不关心 | 手把手敲 API、boilerplate、教学环境的简化场景 |

**反画像**（不是这群人）：
- 不是企业 IT 培训对象
- 不是从未写过 AI 应用的新手
- 不是只关心"先跑起来"不管生产的 demo 党
- 不是被强制来上课的开发者

---

## 二、5 条设计原则

### 原则 1：只讲决策点，不教 API

**为什么**：vibe coding 熟手能让 AI 在 5 分钟内写完任何 API 调用代码。讲师花 30 分钟讲 `AIProjectClient.agents.create_version()` 的字段含义是**双重浪费**——学员不需要，AI 也能解释。

**取舍**：
- ✅ 讲：为什么用 Foundry Agent Service 而不是直接调 OpenAI（这是 AI 不会替你判断的）
- ✅ 讲：`agent_reference` 的边界——什么场景会触发平台锁定（这是工程决策）
- ❌ 不讲：`PromptAgentDefinition` 每个字段是什么意思（让学员让 AI 解释）

**衡量**：每个模块讲解时间里，"决策与边界"占 >70%，"API 用法"占 <30%。

---

### 原则 2：AI 不知道的事优先

**为什么**：vibe coding 熟手依赖 AI 助手，但 AI 的训练数据有**滞后期**和**盲区**。培训的独特价值在于补 AI 的盲区。

**AI 知道得很好的事**（一笔带过）：
- agent-framework / OpenAI SDK 的标准用法
- Bicep / GitHub Actions 标准模板
- OTel 通用配置
- A2A 协议规范

**AI 知道得不好的事**（重点讲）：
- **Foundry rebrand 期的 API 真实状态**：`agent-framework-azure-ai==1.0.0rc6` 的字段名变动、文档与代码矛盾、新旧路径并存
- **原 workshop 的具体 bug**：3 处已知 bug、注释掉的 OTel 代码——AI 的训练数据可能包含原 workshop 但不会标注 bug
- **Foundry Agent Service vs Agent Framework SDK 的双轨制现状**：AI 倾向给"标准答案"，但当前生态没有标准答案
- **当前最新 API 漂移**：rc 期间的字段重命名（如 `OpenAIChatOptions` 是否还存在）
- **工程实践的"为什么"**：成本计算的真实数字、scaling 的真实瓶颈、红队的实际 ROI——AI 不知道你的预算和合规要求

**AI 完全不知道的事**（独家价值）：
- 你的业务场景的选型判断
- 你的客户的合规边界
- 你的团队的技术约束

---

### 原则 3：每个 Ex 交付 prompt spec，不是代码

**为什么**：vibe coding 工作流的产物不是"我写的代码"，而是"我能复用的 prompt spec"——一份能直接喂给 AI 助手让它生成生产级代码的规格说明。

**spec 模板**（每个 Ex 输出一份）：

```
## 任务
<一句话说清楚要实现什么>

## 上下文
- 框架/SDK: <agent-framework 1.0 / azure.ai.projects / a2a-sdk 0.3.25 等>
- 当前已知问题: <列出 AI 训练数据里可能没有的 bug 或漂移>
- 约束: <成本/延迟/可移植/合规要求>

## 输入/输出
- 输入: <数据形状>
- 输出: <数据形状>

## 实现要求
- <关键决策点 1>
- <关键决策点 2>

## Negative examples (AI 容易写错的地方)
- ❌ <反例 1>
- ❌ <反例 2>

## Acceptance Criteria / 验收
- <可执行的验证步骤>
```

**衡量**：综合作业评分中 "AI-pair workflow 复用度" 占 15%——评估学员的 spec 让 AI 生成了多少可用代码。

---

### 原则 4：Negative example 必须显式列出

**为什么**：AI 写错的地方往往是**最难发现**的地方（语法上对、语义上错）。培训不显式标出，学员让 AI 生成时就会复现。

**Negative example 来源**：
1. 原 workshop 已知 bug（3 处）
2. Foundry rebrand 期 API 漂移导致 AI 用旧名字
3. 生产工程实践中的常见反模式（如忘记 429 重试、忘记成本采样）
4. 讲师从真实项目中总结的"我们栽过的跟头"

**举例**：

```markdown
## Ex03 Negative Examples

❌ AI 会写：`tools=get_products`
✅ 正确写：`tools=[get_products]`
原因：tools 是 list 类型，单个工具也要包成 list。AI 看到单元素习惯性省略 list。

❌ AI 可能写：`from agent_framework import ai_function` + `@ai_function`
✅ 正确写：`from agent_framework import tool` + `@tool`
原因：原 workshop 文档说 @ai_function，但代码用 @tool。AI 训练数据可能学到错的命名。

❌ AI 会写：`OpenAIChatOptions(response_format=ResponseFormat)`
⚠️ 当前未验证：rc6 期间这个字段可能改名。讲师培训前 7 天必须验证。
```

**衡量**：每个模块必须有 ≥3 个 negative example，否则模块设计不通过。

---

### 原则 5：红队前移，可移植/成本/scaling 是必修

**为什么**：旧 plan 把红队放 Day3、成本放 Day3 最后——这是"生产化是 nice-to-have"的传统思维。AI 原生开发者从第一天就要算账、要可移植、要扛流量、要安全。

**前移**：
- **成本**：Day1 架构总览课就讲，每个 Ex 带成本说明（不是只在 Day3 最后讲一次）
- **可移植**：Day1 加可移植性专题（写 provider abstraction），不是只口头提一句
- **Scaling**：Day1 部署到 Foundry Hosted Agents 主路径时就接 429 重试 + 并发限流 + 缓存（不依赖具体部署目标——Hosted Agents 的 scale-to-zero 是产品默认；ACA 自托管是对照路径，min replicas ≥ 1 那条约束限定在 ACA 段）
- **红队**：从 Day3 提前到 Day2 下午，强调"红队是上线门槛不是 nice-to-have"

**必修不是 nice-to-have**：综合作业评分中，可移植/scaling/红队**全部纳入评分维度**，不是加分项。

---

## 三、AI-pair 工作流设计

### 三方分工

| 角色 | 做什么 | 不做什么 |
|------|--------|---------|
| **讲师** | 讲决策点、讲 AI 盲区、做 spec 设计示范、review 学员的 AI 输出 | 不教 API、不演示 boilerplate、不手把手敲代码 |
| **学员** | 听决策、写 spec、让 AI 实现、判断 AI 输出对不对 | 不从零敲代码、不背 API 文档 |
| **AI 助手** | 生成代码、解释 API、写 boilerplate | 不做架构决策、不判断成本/合规 |

### 时间结构倒置

| 时间分配 | 旧 plan | 新原则 |
|---------|---------|--------|
| 讲师讲解 | 30% | 50%（但讲的是决策点、AI 盲区、negative examples，**不是 API**） |
| 演示/动手 | 70%（讲师演示 + 学员敲代码） | 30%（学员 AI-pair 实操） |
| 评审/复盘 | 0% | 20%（全员 review AI 输出、决策卡点评） |

⚠️ **关键澄清**：50% 讲师讲解 ≠ 传统讲课中心化。

| 不是这个意思 | 是这个意思 |
|-------------|-----------|
| ❌ 讲师把 API 文档念一遍 | ✅ 讲 Foundry Agent Service vs SDK 的选型边界 |
| ❌ 讲师演示怎么调 `agents.create_version()` | ✅ 讲 `agent_reference` 这个机制在哪些场景会触发平台锁定 |
| ❌ 讲师手把手带学员敲代码 | ✅ 讲 AI 训练数据里没有的 rc 期 API 漂移、原 workshop bug |
| ❌ 讲师讲完学员只会复读 | ✅ 讲完学员能写出 spec 让 AI 生成正确实现 |

**判别标准**：如果讲师讲的内容能被 ChatGPT 一段回答替代，那就讲错了——必须讲 AI 答不出的部分。

### AI-pair 工作流专题（新增模块）

Day3 给 30 分钟专门讲：

1. **Foundry 文档怎么 prompt 给 AI**——把 Learn 文档 URL 给 Claude Code 时的最佳 prompt 模板
2. **如何用 MCP 让 AI 直接连 Foundry**——介绍 Foundry MCP server（如果存在）
3. **AI 写错时的诊断流程**——validate → diff with negative example → 反馈给 AI 修正
4. **可复用的 prompt spec 库**——本次培训产出的 spec 如何作为团队资产

---

## 四、议程结构原则

### 时间块设计

每个模块统一结构（约 60-90 分钟）：

```
┌─────────────────────────────────────────────────────┐
│  [15-30 min] 决策点讲解                              │
│  - 这个模块要做什么决策                              │
│  - AI 不知道的事                                     │
│  - Negative examples                                 │
├─────────────────────────────────────────────────────┤
│  [20-40 min] AI-pair 实操                            │
│  - 学员写 spec                                       │
│  - 让 AI 实现                                        │
│  - 验证输出                                          │
├─────────────────────────────────────────────────────┤
│  [10-20 min] 评审 + 复盘                             │
│  - 抽 2-3 人展示 AI 输出                            │
│  - 全员点评决策点                                    │
│  - 更新 negative example 库                          │
└─────────────────────────────────────────────────────┘
```

### Day 主题原则

- **Day 1**：决策 + 平台快速通关（让学员一天内能跑出 Foundry MVP，意识到成本/锁定风险）
- **Day 2**：SDK + Workflows + 红队前移（从"用平台"到"控制平台"）
- **Day 3**：生产化 + 综合作业（3 天内完成"能演示的生产级"作品）

### 必砍内容

旧 plan 中以下内容必须砍掉或大幅压缩：

- ❌ 手把手敲 boilerplate 的时间块（AI 5 分钟搞定）
- ❌ 单 agent 给 135 分钟（压到 60 分钟，AI-pair）
- ❌ 多 agent 用手写 HandoffService 90 分钟（砍掉，直接用 Workflows）
- ❌ OTel 的 KQL 深挖（学员能让 AI 写 KQL，讲必要观测点即可）
- ❌ Bicep 字段逐行讲解（AI 写 Bicep 比讲师讲得快）

### 必加内容

- ✅ Day1 成本/可移植/scaling 专题（旧 plan 缺失或太晚）
- ✅ Day2 红队前移（旧 plan 在 Day3 末尾）
- ✅ Day3 AI-pair 工作流专题（全新）
- ✅ Day3 生产化专题（事故复盘 + 上线 checklist）
- ✅ 每个 Ex 的 prompt spec 模板
- ✅ 每个 Ex 的 negative example 清单（≥3 条）

---

## 五、综合作业设计逻辑

### 场景"任选其一"而非"统一场景"

**为什么**：学员身份混合（startup + partner），统一场景必然有人觉得无关。给 3 个场景任选，覆盖主要工作场景：

| 场景 | 适合谁 | 强调维度 |
|------|--------|---------|
| B2C AI 助手 startup | startup 工程师 | 成本、scaling、缓存 |
| partner POC 给金融客户 | partner SA/实施 | 红队、可移植、合规 |
| 垂直行业 SaaS | 跨场景 | 多租户、扩展性、客户自助 onboard |

### 评分维度反映原则

| 维度 | 权重 | 对应原则 |
|------|------|---------|
| 能跑通 | 25% | 基础门槛，但不是核心 |
| 架构选型决策卡 | 25% | 原则 1（讲决策点） |
| 红队 baseline | 20% | 原则 5（红队必修） |
| 生产化 checklist | 15% | 原则 5（生产化必修） |
| AI-pair workflow 复用度 | 15% | 原则 3（交付 spec） |

**决策卡要求**：必须有可移植/成本/scaling 三选一的明确说明（不能全选，强迫学员做 tradeoff）。

---

## 六、本原则文档的使用方式

### 何时更新

- 学员画像有变化 → 改第一节
- 培训交付后收集反馈 → 改 5 条原则中相应项
- AI 工具栈/Foundry API 重大变化 → 改原则 2 的"AI 不知道的事"清单

### 派生关系

```
docs/04-design-principles.md (本文档)
    │
    ├──→ docs/00-training-plan-v2.md         (议程是原则的应用)
    ├──→ docs/01-instructor-handbook-v2.md   (手册是原则的展开)
    ├──→ docs/02-instructor-prep-checklist.md (Day-7 现成物对应原则的执行)
    ├──→ docs/03-workshop-fork-mapping.md    (上游借用对照)
    ├──→ workshop/                           (学员侧站点；代码 + 子任务反映原则的工程化)
    └──→ prep-artifacts/day-7/specs/         (11 spec 是原则 4 的载体)
```

### 不变量

无论议程怎么改，以下不变：

1. 决策点讲解时间占比 >70%
2. 每个模块 ≥3 个 negative example
3. 每个 Ex 交付一份 prompt spec
4. 综合作业 5 个评分维度的权重比例
5. 红队不晚于 Day2 下午出现

---

## 七、待验证假设

本原则文档基于的假设（培训前/培训中需要验证）：

| 假设 | 如何验证 | 如果不成立怎么办 |
|------|---------|----------------|
| 学员都是 vibe coding 熟手 | 报名表加一题"日常用什么 AI 编程工具" | 不熟手的人单独 onboarding，或拆双轨道 |
| 学员能在 60 分钟内让 AI 写完 Ex02 单 agent | Day1 第一节模块结束观察完成率 | Day1 实时延长，砍 Day3 buffer 时间 |
| 3 个场景能覆盖学员真实业务 | Day3 综合作业开题后看选场景分布 | 加场景 4 或允许学员自定义 |
| Negative example 真的有用 | Day2 末尾匿名反馈问"AI 错误清单有用吗" | 删/改对应模块 |

---

## 八、参考与启发

本原则的思想来源：

- 用户协作偏好："给判断 → 附依据；给方案 → 标出能力边界；给建议 → 落到具体下一步"
- 对原 workshop 的核查发现：双轨制混乱、bug、注释代码、缺 Workflows
- 学员画像迭代（3 轮）：通用开发者 → startup/partner → AI 原生熟手
- AI 原生开发的工程化趋势：spec-driven、AI-pair、生产化前移
