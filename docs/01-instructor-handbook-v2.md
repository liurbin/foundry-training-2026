# 讲师手册 v2：决策模块交付物

> 本手册是 `docs/00-training-plan-v2.md` 第五·六节"每模块交付物清单"的**实现**。
> plan 定义接口（每模块必有 spec / negative examples / 验收 三项），手册填实现。
> 改 plan 模块结构 → 必须同步改本手册对应章节。
> 改本手册的 spec 模板 → 不需要改 plan。

## 使用方式

- 每模块一节，固定四块：**目标速查 / prompt spec / negative examples / 验收 checklist**
- spec 模板是给学员的，讲师 Day 现场可直接投屏 / 复制到共享文档
- negative examples 既是上课的"决策点讲解"素材，也是学员自验证的反例库
- 验收 checklist 用于讲师抽检 + 学员自评 + 综合作业评分维度交叉引用
- Day-7 讲师现成物统一跟踪在 `docs/02-instructor-prep-checklist.md`，不要只依赖各模块"讲师准备"段临场翻找

## 填充进度

| 模块 | 状态 |
|------|------|
| D1 | ✅ 第 1 轮 |
| D2 | ✅ 第 1 轮 |
| D3 | ✅ 第 1 轮 |
| D4 | ✅ 第 1 轮 |
| D5 | ✅ 第 1 轮 |
| D6a | ✅ 第 1 轮 |
| D6b | ✅ 第 1 轮 |
| D7 | ✅ 第 1 轮 |
| D8 | ✅ 第 1 轮 |
| D9 | ✅ 第 1 轮 |
| D10 | ✅ 第 1 轮 |
| D11 | ✅ 第 1 轮 |

---

## D1 — 何时用 Foundry / 何时不用

### 目标速查

| 项 | 内容 |
|----|------|
| 时长 | 45 min（30 讲 / 0 实操 / 15 评审） |
| Day | 1 |
| 关键产出 | "我的项目何时用 Foundry"决策卡 + Foundry 能力地图（plan 五·五节） |
| 对应原则 | 1（只讲决策点）、2（AI 不知道的事） |

### prompt spec

**特殊说明**：D1 无 AI-pair 实操，spec 形态 = 讲师提供模板，学员当场填。

文件：`spec-d1-foundry-fit.md`

````markdown
# 我的项目：是否用 Foundry 决策卡

## 项目一句话描述
（业务目标 + 当前阶段，1 行）

## 决策维度勾选
- [ ] 我需要托管 agent 运行时 + 状态管理 → 倾向 Foundry
- [ ] 我需要 Azure 生态（AAD / Key Vault / App Insights）原生集成 → 倾向 Foundry
- [ ] 我有合规/数据驻留要求（金融、医疗、政企）→ 倾向 Foundry
- [ ] 我需要 portal 上让非工程师配 agent / 看 trace → 倾向 Foundry
- [ ] 我只需要单次 LLM call，无 agent 概念 → 不用 Foundry
- [ ] 我的核心模型在 Azure 目录外（Claude / Gemini / 自托管）且不打算切 → 不用 Foundry
- [ ] 我做的是研究 demo / hackathon，下周扔 → 不用 Foundry
- [ ] 我已经有成熟 LangGraph / CrewAI 生产栈，无迁移动机 → 不用 Foundry

## 结论
[用 / 不用 / 部分用]

## 部分用的话，哪一部分？
（对照五·五能力地图：只用 Evaluations？只用 Models？只用 Agent Service 但 SDK 路径？）

## 我不确定的地方
（这一栏讲师评审段必看）
````

### negative examples（≥3）

| # | 学员常犯的错 | 反例点 |
|---|--------------|--------|
| 1 | "公司是 Azure 客户所以一定用 Foundry" | 维度错位：客户合同 ≠ 技术选型。可能正解是用 Azure OpenAI 直调，不引入 Agent Service |
| 2 | "Foundry 比 LangGraph 高级所以选 Foundry" | 比较错位：托管平台 vs 编排库，不在一个轴上。问的是"我要不要托管运行时"，不是"哪个更高级" |
| 3 | "我现在不用，等以后再迁" | 假设错位：迁移成本不在"以后"产生，在写第一行代码时就决定。Day3 D10 会回到这条 |
| 4 | "用了 Foundry 就锁死 Azure" | 事实错位：D4 会演示 provider 抽象 + 第三方模型目录，锁定程度取决于你怎么写代码 |

### 验收 checklist

学员产出"算过"的标准（讲师抽 2-3 人评审段对照）：

- [ ] 决策卡至少勾 1 个"倾向 Foundry" + 1 个"倾向不用 Foundry"维度；若单边成立必须写一句为什么对侧维度全不适用
- [ ] 结论一栏不是"再想想"——给出明确"用 / 不用 / 部分用"
- [ ] 如果结论是"部分用"，能在五·五能力地图上指出至少 2 格
- [ ] "我不确定的地方"非空（讲师宁可学员承认不确定，也不要假装全懂）
- [ ] 能口头讲清"为什么不选 LangGraph / 直接 Azure OpenAI"中至少一条对照

---

## D2 — Agent Service vs SDK 选型

### 目标速查

| 项 | 内容 |
|----|------|
| 时长 | 90 min（40 讲 / 30 实操 / 20 评审） |
| Day | 1 |
| 关键产出 | "Agent Service vs SDK 选型"决策卡（写自己项目的） |
| 对应原则 | 1、5（可移植/成本/scaling 必修） |

### prompt spec

文件：`spec-d2-service-vs-sdk.md`

````markdown
# Agent Service vs Agent Framework SDK 选型决策卡

## 上下文
- 项目：[一句话]
- 团队规模：[人数 + AI 熟手占比]
- 是否需要非工程师在 portal 配 agent：[是/否]

## 四个维度打分（1-5，5 = 强需求）
| 维度 | 分 | 说明 |
|------|----|----|
| 托管运行时（不想自己跑 worker） | _ | |
| portal 可视化（PM/SA 直接配） | _ | |
| 代码完全控制（自定义编排 / 自定义状态） | _ | |
| 跨 provider 移植性 | _ | |

## 决策规则（讲师给的启发式）
- 前两项 ≥ 后两项 → Agent Service
- 后两项 ≥ 前两项 → SDK
- 接近 → 混合（Service 跑入口 agent，SDK 跑专家 agent）

## 我的选择 + 理由（≥3 句）
[…]

## 成本影响
- Agent Service：托管费 + 平台调用费
- SDK：自托管运行时（Container Apps / 自己 VM）+ 模型调用费

### 估算输入（必填，不接受"差不多"）
| 项 | 值 |
|----|----|
| 日请求量（DAU × 人均次数） | _ |
| 平均输入 token / 输出 token | _ / _ |
| 并发峰值（QPS） | _ |
| 是否需要 7×24 on-call | 是 / 否 |
| 运行时规格（SDK 路径才填，如 Container App 2vCPU/4GB×N 实例） | _ |

[我这个项目，哪一边总成本低？给出数量级（$/月）和主导成本项]

## 我没想清楚的地方
[…]
````

### negative examples（≥3）

| # | 学员常犯的错 | 反例点 |
|---|--------------|--------|
| 1 | "SDK 更灵活所以默认选 SDK" | 灵活 ≠ 合适。SDK 路径意味着你自己负责运行时、状态、failover——团队没人值班就别选 |
| 2 | "Agent Service 是托管的所以一定贵" | 没算自托管的人力 + 运维 + on-call。3 人团队跑自托管 SDK 路径，第一个 incident 就把价差吃回来 |
| 3 | "选了 Service 就不能用 SDK" | Foundry 允许混合：portal 配入口 agent + SDK 写专家 agent + 两边互通。D6a/b 会讲 |
| 4 | "决策卡是 PM 填的，工程师不用关心" | 这张卡决定了未来 6 个月 80% 的工程实现路径，工程师不参与等于把锅交给 PM |

### 验收 checklist

- [ ] 四维度全部打分（不允许空）
- [ ] 决策结论与四维度分数一致（不一致必须解释，比如"分数倾向 SDK 但团队没人值班所以选 Service"）
- [ ] 成本影响一栏有具体数字方向（不接受"差不多"）
- [ ] 评审段能回答："如果团队 6 个月后翻倍，这个决策要不要重做？"

---

## D3 — 单 agent 平台路径（Bicep + agent_reference）

### 目标速查

| 项 | 内容 |
|----|------|
| 时长 | 120 min（上午 60：30 讲 / 30 实操；下午 60：45 实操 / 15 评审，跨午饭） |
| Day | 1 |
| 关键产出 | 跑通的 Foundry 单 agent + AI 生成的 Bicep + agent_reference 代码 |
| 对应原则 | 1、3（每模块交付 prompt spec） |

### prompt spec

文件：`spec-d3-single-agent.md`

````markdown
# 让 AI 帮我跑通 Foundry 单 agent（Bicep + agent_reference）

## 目标
在我的 Foundry project 里部署一个最小 agent，从外部代码用 agent_reference 调起来，能返回。

## 输入（学员现场填）
- Foundry project 名：[…]
- Region：[…]
- 模型部署名：[…]
- 我要让 agent 做什么（一句话）：[…]
- 我用的语言 / SDK：[Python / .NET / TS …]

## 让 AI 生成的产物清单
1. Bicep 模板（创建 agent + connection）
2. 部署脚本（az deployment …）
3. 用 agent_reference 调 agent 的最小代码
4. 一次成功调用的 trace 链接（学员自己跑后贴）

## 约束（告诉 AI 必须遵守）
- 不要 hardcode 任何 secret，必须用 Key Vault 引用或 env
- 不要用 deprecated API（讲师当天给出 rebrand 期已知漂移清单）
- Bicep 必须用 module 化，不写成单文件 200 行
- 调用代码必须捕获 429 + 5xx 并打日志（具体重试策略放 D5）

## 观测前置（影响验收第 3 条）
- 确认 project 已接 Application Insights / tracing 开关（讲师 Day1 上午统一确认 1 次）
- 如果 project 未启用 tracing：本模块"trace 链接"验收转为可选，留到 D5/D9 补；学员不应被卡在观测配置问题上

## 自验证
- [ ] az deployment 成功无 error
- [ ] 调用返回 200 且文本非空
- [ ] portal 能看到本次调用 trace
````

### negative examples（≥3）

| # | 学员常犯的错 | 反例点 |
|---|--------------|--------|
| 1 | 把 model deployment name 写死在 Bicep 里 | 不同环境（dev/staging/prod）必走 parameter；rebrand 期模型名经常改 |
| 2 | 让 AI 生成 Bicep 后直接 az deploy 不审 diff | AI 经常多创资源（多余的 storage / log workspace）。审 diff 是工程师的活，不是 AI 的活 |
| 3 | agent_reference 调用代码没加重试 | 第一次跑 demo 没事，到 D5 压测 / D9 生产场景就炸 |
| 4 | 把 connection string 直接放 .env 提交 git | Key Vault + Managed Identity 是 Foundry 默认路径，没理由绕开 |

### 验收 checklist

- [ ] Bicep 在学员自己的 Foundry project 跑通（不接受"讲师那边能跑"）
- [ ] agent_reference 代码在学员本机能成功调用一次
- [ ] portal Monitoring → Traces 能看到这次调用（**前置条件未满足时此项转可选**，见 spec 观测前置段）
- [ ] 学员能口头讲清"如果换 region 要改哪几行 Bicep"
- [ ] secret 100% 不在源码里（讲师 grep 抽查）

---

## D4 — Provider 抽象（含非 Azure provider 切换演示）

### 目标速查

| 项 | 内容 |
|----|------|
| 时长 | 90 min（30 讲 / 40 实操 / 20 评审） |
| Day | 1 |
| 关键产出 | 一段 provider 抽象代码 + 能在 Foundry / 第三方 provider 间切的最小 demo（学员侧用 mock provider） |
| 对应原则 | 1、5（可移植必修） |

### prompt spec

文件：`spec-d4-provider-abstraction.md`

````markdown
# 让 AI 帮我写一层 provider 抽象

## 目标
我的业务代码不直接依赖 Foundry SDK 或 OpenAI SDK，而是依赖一个 ChatProvider 接口。
今天能在 Foundry / mock 之间切，未来能加第三方 provider（Anthropic / 自托管）。

## 接口定义（学员必须先想清楚）
```python
class ChatProvider(Protocol):
    async def chat(self, messages: list[Message], **opts) -> ChatResponse: ...
```

## 让 AI 生成的产物清单
1. ChatProvider 接口（含 Message / ChatResponse 的最小字段）
2. FoundryProvider 实现（包 Foundry SDK 调用）
3. MockProvider 实现（学员侧，返回写死文本，用于不依赖真 key 跑 abstraction）
4. 一个 switch 配置（env 变量决定加载哪个 provider）
5. 单元测试：MockProvider 通 + FoundryProvider 用 contract test 框（不强求真调）

## 约束
- 接口里不准出现任何 provider 专有概念（不准有 Foundry 的 thread_id、不准有 OpenAI 的 tool_choice）
- 共性参数（temperature / max_tokens / stop）走结构化字段；provider 专有参数走 **opts 透传
- 不写"抽象工厂的工厂"——一个 if/elif 就够

## 自验证
- [ ] MockProvider 在没有任何 Azure 凭证的机器上能跑
- [ ] 业务代码 grep 不到 "azure" 或 "openai" 字符串（除 provider 实现文件外）
- [ ] 加第三个 provider 不需要改业务代码，只加一个文件
````

### negative examples（≥3）

| # | 学员常犯的错 | 反例点 |
|---|--------------|--------|
| 1 | 接口里塞 Foundry 专有字段（thread_id、tool_resources）"以备将来" | 接口被污染，第二个 provider 来就得加 if 分支。专有字段走 opts |
| 2 | 让 AI 写 4 层抽象（Factory + Builder + Strategy + Registry） | 你只有 2 个 provider，单 if/elif 就够。复杂度欠债比 vendor 锁定更可怕 |
| 3 | "Foundry 已经支持多 provider 目录所以不用自己抽象" | 模型目录解决的是 model_id 切换，不解决 SDK 锁定。Foundry SDK 调用代码本身就是耦合 |
| 4 | MockProvider 写得太聪明（带状态、模拟错误） | mock 就是返回写死文本，能让 abstraction 跑起来即可。复杂 mock 应该是单测 fixture，不是 provider |

### 验收 checklist

- [ ] 学员代码里业务层 import 的是 `ChatProvider`，不是任何具体 provider
- [ ] MockProvider 在断网 / 无 key 环境能跑通
- [ ] 讲师 live 演示切换：Foundry → 非 Azure provider（仅讲师持 key），学员看着切换瞬间
- [ ] 学员能口头讲清"我这个项目，1 年内会不会真的换 provider？不会的话这层抽象值不值得？"
- [ ] 没有 4 层以上抽象（讲师抽查代码结构）

---

## D5 — Scaling + Cost 决策（Hosted Agents 主路径 + Container Apps legacy 对照）

### 部署路径分层（讲师必须开篇讲清）

| 路径 | 状态 | 本课定位 | scaling 模型 |
|------|------|---------|-------------|
| **Foundry Hosted Agents** | 当前主路径（new backend） | **学员目标路径** | 托管容器，scale-to-zero，15 min idle 后释放 |
| Container Apps（ACA）自托管 | legacy / 自托管对照（走旧 `azd ai agent` 模板） | 仅作"自托管时你要操心什么"对照讲，不作为学员部署目标 | 自管 min/max replicas + scale rules |

- 学员的 D5 部署目标 = **Hosted Agents**；scale-to-zero 是产品给的能力，不需要自己写 Bicep。
- ACA 段落（min replicas / Bicep / 冷启动取舍）保留意义在于："如果哪天你必须自托管，要知道代价"——这是对照视角，不是必跑路径。
- 因此 **"min replicas ≥ 1"是 ACA 段的硬约束，不适用 Hosted Agents**——Hosted Agents 的 scale-to-zero 是产品默认行为，不踩这条规则。

### 目标速查

| 项 | 内容 |
|----|------|
| 时长 | 90 min（30 讲 / 40 实操 / 20 评审） |
| Day | 1 |
| 关键产出 | 带 429 重试 + 缓存策略 + 成本估算的部署方案（部署目标 = Hosted Agents；ACA 仅对照讲） |
| 对应原则 | 1、5（成本/scaling 必修） |

### prompt spec

文件：`spec-d5-scaling-cost.md`

````markdown
# 让 AI 帮我把 D3 的单 agent 部署到 Hosted Agents（主路径），并补 429 重试 + 缓存 + 成本估算；ACA 仅作对照

## 输入
- 来自 D2 成本估算表：日请求量 / 平均 token / QPS（直接搬过来）
- 来自 D3：可调用的 Foundry agent + agent_reference 代码
- 目标 SLO：[p95 延迟 / 月度可用率，至少给一个数]

## 让 AI 生成的产物清单
1. Hosted Agents 部署配置（主路径；scale-to-zero 默认，15 min idle 释放）
2. （对照视角，可选）ACA 自托管 Bicep 骨架：含 min/max replicas + scale rules——讲清楚为什么自托管要踩 min replicas ≥ 1 这条线
3. 429 + 5xx 重试策略（带 jitter 的指数退避，不允许无脑 retry-once；Retry-After 视为硬下界）
4. 一层缓存（按 prompt+model hash，TTL 学员定，写清楚为什么这个 TTL）
5. 成本估算脚本：输入 DAU/QPS → 输出月度 $ 上下限（模型费 + 运行时费 + 缓存命中率影响）
6. TPM/RPM 配额对照：估算的 token/min 是否超 D1 prep 时确认的配额

## 约束
- **主路径（Hosted Agents）**：使用产品默认 scale-to-zero；冷启动取舍由 SLO 决定要不要做保活探针，不要自己写 min replicas 限制
- **对照路径（ACA 自托管）**：如果选自托管，min replicas 不准为 0（冷启动 + 第一次 429 会同时炸）
- 重试上限明确写死（默认 3 次），不准无限重试
- 缓存键不准包含 user_id / 个人数据（合规雷区）
- 成本估算必须给区间（best/worst），不准给单点数字

## 自验证
- [ ] 用 stub / 讲师提供的 replay response 注入 429，观测到重试 + jitter 行为正确（不抛业务层）
- [ ] 真实 100 RPS × 5min 压测为**可选**（讲师统一演示或录屏；真跑由讲师侧执行，避免学员触发共享配额）
- [ ] 缓存命中率 > 0（说明缓存真的接进去了）
- [ ] 成本估算的 best/worst 差 ≤ 3x（否则假设太松）
````

### negative examples（≥3）

| # | 学员常犯的错 | 反例点 |
|---|--------------|--------|
| 1 | 把 Hosted Agents 当成 ACA 写一份 min-replicas-≥1 的 Bicep | 路径选错：Hosted Agents 是托管容器，scale-to-zero 是产品默认行为；学员要做的是接受 + 在 SLO 层面决定要不要保活，不是自己拉起 min replicas |
| 2 | ACA 路径走 scale-to-zero "省钱" | 自托管路径下，冷启动 5-15s 第一波用户跑光；省的容器费不够赔的延迟预算（这是 ACA 段的反例，不是 Hosted Agents 的反例） |
| 3 | 重试逻辑写在业务层（catch 429 → sleep → retry） | 多处重复 + 没 jitter → thundering herd。重试必须在 provider/HTTP 客户端层统一 |
| 4 | 缓存键直接用整个 prompt 字符串 | 一个空格差异就 miss；同时如果 prompt 含 PII 等于把 PII 写进缓存 store |
| 5 | 成本估算只算模型费 | 漏算运行时（Hosted Agents 计费 / ACA 容器费）、出口流量、Application Insights 摄入费——这三项中型项目能占 30%+ |

### 验收 checklist

- [ ] 主路径部署目标明确写"Hosted Agents"；若学员选了 ACA 对照路径，需在产出里说明为什么（如"未来必须自托管 / 合规要求 VNet 隔离"）
- [ ] ACA 对照路径产出（如果有）：Bicep min replicas ≥ 1（讲师 grep 抽查；仅适用 ACA 段）
- [ ] 重试策略代码集中在一处（grep "retry" 不应散落 5+ 文件）
- [ ] 缓存命中率有真实数字（不接受"应该会命中"）
- [ ] 成本估算 best/worst 都给，且差距合理（≤3x）
- [ ] 学员能口头讲清"如果 DAU 翻 10 倍，哪一项成本先爆"，以及"如果今天必须从 Hosted Agents 切到 ACA，要补哪几件事"

### 讲师准备

- **429 注入 stub / replay response**（学员侧验证 retry 行为用，不依赖真实配额）
- 100 RPS × 5min 真实压测脚本 + 录屏（讲师侧演示用）
- 一份"中型项目成本三档参考"（小：1k DAU / 中：10k DAU / 大：100k DAU），D2 成本表填不出时学员可对照

---

## D6a — Agent Framework SDK 的边界

### 目标速查

| 项 | 内容 |
|----|------|
| 时长 | 60 min（20 讲 / 30 实操 / 10 评审） |
| Day | 2 |
| 关键产出 | 跑通的 SDK 路径 agent + "何时从 Agent Service 切到 SDK"决策卡（含成本影响栏） |
| 对应原则 | 1、5 |

### prompt spec

文件：`spec-d6a-sdk-boundary.md`

````markdown
# 让 AI 帮我用 Agent Framework SDK 重写 D3 的 agent

## 目标
同样的业务逻辑，用 SDK 路径再实现一遍，对比 Agent Service 路径，得出"何时切 SDK"的判断。

## 输入
- D3 的 Agent Service 实现（作为对照）
- 我的业务里有没有 Agent Service 不支持的需求（自定义状态？自定义编排？特殊 provider？）

## 让 AI 生成的产物清单
1. SDK 路径 agent 实现（最小可跑）
2. 与 Agent Service 路径的代码量 / 依赖 / 启动方式对比表
3. "何时切 SDK"决策卡（4 触发条件 + 我项目目前命中几条）

## 决策卡模板
- [ ] Agent Service 不支持我要的编排模式（如自定义状态机）
- [ ] 我需要把 agent 嵌入已有服务进程（不想多一个托管运行时）
- [ ] 我对延迟敏感，托管层多一跳无法接受
- [ ] 我要 provider 不在 Foundry 模型目录里
→ 命中 ≥1 条：考虑 SDK；命中 0 条：留在 Agent Service

## 成本影响（决策卡必填）
SDK 路径相比 Agent Service 新增的成本项：
- 运行时：Container Apps / VM 实例费（参考 D5 估算表）
- 观测：自接 Application Insights 摄入费 + dashboard 维护
- 维护：on-call 轮值（24/7 还是工作时间）
- 状态：自建状态存储（Redis / Cosmos）
[我这个项目，省下的托管费 vs 上述新增项，净差额方向？]

## 约束
- 不准把 Agent Service 的代码直接复制改名——必须重写、对照
- 必须留下 README 说明"为什么我项目里两条路径都保留 / 只保留一条"

## 自验证
- [ ] SDK 路径 agent 能跑通（输入 → 输出）
- [ ] 对比表填实，不接受"差不多一样"
- [ ] 决策卡命中条数 + 结论一致
- [ ] 成本影响栏给出净差额方向（不接受空）
````

### negative examples（≥3）

| # | 学员常犯的错 | 反例点 |
|---|--------------|--------|
| 1 | "SDK 路径代码更少 / 更优雅所以切 SDK" | 代码量不是切换理由。切 SDK = 自己接管运行时责任，省的那点代码以后用人力运维补回来 |
| 2 | 把 SDK agent 跑在 Container Apps 上但不接 Application Insights | 失去 Foundry portal 的 trace 视角，又没自建观测——黑盒 |
| 3 | SDK 路径直接 import OpenAI SDK | 跳过 D4 的 provider 抽象，把第二次 vendor 锁定埋进去 |
| 4 | "我两条路径都跑通了所以两条都保留" | 重复实现 = 2 倍维护成本，没业务理由就砍一条 |

### 验收 checklist

- [ ] SDK 路径与 Agent Service 路径的对比表填实（≥4 行）
- [ ] 决策卡命中条数与最终选择一致
- [ ] 如果两条路径都保留，README 写清理由（不接受"以防万一"）
- [ ] 学员能口头讲清"我项目 6 个月内会不会从 Service 切 SDK"

---

## D6b — A2A + MCP 的边界

### 目标速查

| 项 | 内容 |
|----|------|
| 时长 | 60 min 主段 + 衔接 45 min 叠加段（在 D6b 的 A2A demo 上加 MCP tool；产物归属 D6b） |
| Day | 2 |
| 关键产出 | A2A 最小 demo + MCP 最小 demo + 叠加 demo（A2A demo 上加 MCP tool） + "A2A vs MCP 选型"决策卡（含成本影响） |
| 对应原则 | 1、2（A2A/MCP 是 rebrand 期 AI 知识薄弱区） |

### prompt spec

文件：`spec-d6b-a2a-mcp.md`

````markdown
# 让 AI 帮我跑通 A2A 和 MCP 两个最小 demo，再叠加

## 目标
分别理解 A2A（agent ↔ agent）和 MCP（agent → 工具）的边界；叠加场景能复现真实多 agent + 工具集成。

## 让 AI 生成的产物清单
1. A2A 最小 demo：两个 agent 互相调用（不准用同进程函数调用伪装）
2. MCP 最小 demo：一个 agent 调一个 MCP server 提供的 tool
3. 叠加 demo：在 #1 基础上，给其中一个 agent 加一个 MCP tool
4. "A2A vs MCP 选型"决策卡

## 决策卡四问
- 我要让两个独立 agent 协作（各自有 LLM）？ → A2A
- 我要让一个 agent 调结构化工具/资源？ → MCP
- 既要又要？ → 叠加（但要算成本，见下）
- 都不要（单 agent 直接 function call 够）？ → 不引入，写明拒绝理由

## 成本影响（决策卡必填）
- A2A：多一次 agent 调用 = 多一倍 token + 一跳延迟
- MCP：多一个 server 进程 / 网络跳；tool schema 进 prompt 也占 token
[我这个 demo 引入 A2A/MCP 后，每次请求 token 增加估算：_]

## 约束
- A2A 两个 agent 不准同进程函数调用伪装——必须走 A2A 协议
- MCP tool 不准只 echo 输入——至少有一次真实外部副作用（HTTP / 文件 / 计算）
- 叠加 demo 必须能 trace 到"agent A → agent B → MCP tool"完整链路

## Fallback（rebrand 期漂移高发，留兜底）
- A2A 和 MCP 至少**学员本机跑通 1 个**；另 1 个可用讲师 prepared repo + trace 对照
- 叠加 demo 跑不通**不阻塞**"A2A vs MCP 边界判断"的验收——决策卡填实即可
- 真实跑通两条 + 叠加 = 课堂目标；只跑通 1 条 + 决策卡 = 验收过线

## 自验证
- [ ] 三个 demo 各自能跑（不互相依赖才算）
- [ ] 叠加 demo 链路 trace 看得到三段
- [ ] 决策卡四问全答 + token 增量估算非空
````

### negative examples（≥3）

| # | 学员常犯的错 | 反例点 |
|---|--------------|--------|
| 1 | "A2A 更高级所以两个 agent 必须 A2A" | A2A 是协议，不是必经路径。同进程 + 共享内存的 multi-agent 在很多场景更便宜更快 |
| 2 | MCP 用来包装本地纯函数 | 纯函数直接做 tool 就行，包成 MCP server 是给自己加运维负担 |
| 3 | 叠加 demo 跑通了就觉得"以后所有项目都 A2A+MCP" | 叠加 = 双倍成本 + 双倍故障面。综合作业里必须有人选"我不引入"才正常 |
| 4 | A2A demo 用同进程函数调用伪装 | 没学到 A2A 的真实代价（序列化、网络、版本协商），决策卡就拍脑袋 |

### 验收 checklist

- [ ] A2A 或 MCP 至少 1 个学员本机跑通；另 1 个学员能用 prepared repo 跑或读懂 trace
- [ ] trace 能看到 A2A 调用跨进程（不是同进程函数）
- [ ] 决策卡 token 增量栏有具体数字（叠加 demo 跑不通不阻塞此项）
- [ ] 学员能口头讲清"我综合作业场景会不会用 A2A / MCP"——不用也算过

### 讲师准备

- A2A / MCP 各自的"已知 rebrand 期坑"清单（Day-7 跑通 fork 后整理）
- **A2A + MCP prepared repo**（学员 fallback 用：本机跑不起来时切到这个 repo 看 trace + 读代码）
- 一个反例 demo：同进程函数调用伪装的 multi-agent（讲负例时打开对比）

---

## D7 — 多 agent 编排三选一

### 目标速查

| 项 | 内容 |
|----|------|
| 时长 | 120 min（50 讲 / 50 实操 / 20 评审） |
| Day | 2 |
| 关键产出 | "多 agent 三选一"决策卡 + 主路径（Agent Service 原生）跑通 + 另两种用 prepared diff / 录屏对照 |
| 对应原则 | 1、4（HandoffService 作为显式反例并入） |

### prompt spec

文件：`spec-d7-multi-agent.md`

````markdown
# 让 AI 帮我用 Agent Service 原生模式跑通多 agent 编排（主路径）+ 看懂另两种

## 目标
主路径学员自己 AI-pair 跑通；as_tool 看讲师 prepared diff；Workflows 看讲师录屏。
最终输出"三选一"决策卡。

## 让 AI 生成的产物清单（仅主路径）
1. 两个专家 agent + 一个 orchestrator agent（Agent Service 原生编排）
2. 三段 trace 链路截图
3. "三选一"决策卡

## 决策卡三问
- 编排逻辑稳定 + 不需要自定义控制流？ → Agent Service 原生
- 编排逻辑要自定义 + 但每个子 agent 独立可测？ → as_tool 模式
- 复杂分支 / 长时间运行 / 需要 visual designer？ → Workflows
- 选 Workflows 必须额外写：为什么不能 Service 原生或 as_tool 解决

## 反例栏（口头讲，不要求跑）
HandoffService 手写模式：plan v1 旧路径，多 agent 状态机自己写——已废，因为 Agent Service 原生覆盖了 80% 场景

## 约束
- 主路径必须真跑通（不准只看讲师演示）
- as_tool / Workflows 不要求跑通，但学员必须能口头讲清"这两种相比主路径多/少什么"

## 自验证
- [ ] 主路径 trace 看到三段（orchestrator → 专家 1 → 专家 2）
- [ ] 决策卡三问全答
- [ ] 能讲出为什么不选另外两种
````

### negative examples（≥3）

| # | 学员常犯的错 | 反例点 |
|---|--------------|--------|
| 1 | "Workflows 看起来最强大所以选 Workflows" | Workflows 学习曲线 + 运维复杂度高；80% 场景 Agent Service 原生够 |
| 2 | 主路径跑不通就想跳到 as_tool 试 | 跳来跳去 = 一种都没学透；先在主路径上 debug 到通 |
| 3 | 重写 HandoffService 手写状态机 | plan v1 旧路径，已废。AI 可能还会建议这条——必须显式拒绝 |
| 4 | 三种都跑通 = 学得好 | 不是。理解边界 > 全部跑通。两小时只够把主路径跑透 + 另两种看懂 |

### 验收 checklist

- [ ] 主路径 trace 三段完整（讲师当场看 trace）
- [ ] 决策卡选择与三问答案一致
- [ ] 学员能口头讲清 as_tool 与主路径的本质差异
- [ ] 如果选 Workflows，必须答出"为什么不用主路径"

### 讲师准备（**这条 plan 已经依赖，必须 Day-7 完成**）

- as_tool 模式的 prepared diff（patch 文件，可在主路径代码上一键 apply 看变化）
- Workflows 模式的录屏（10-15 min，含 visual designer 操作 + 一次完整运行 trace）
- 主路径自己跑通至少 1 次的 trace 截图（兜底：学员跑不通时讲师演示）

---

## D8 — 红队作为上线门槛

### 目标速查

| 项 | 内容 |
|----|------|
| 时长 | 105 min（30 讲 / 50 实操 / 25 评审） |
| Day | 2 |
| 关键产出 | 红队 baseline 报告（ASR）+ "如何把红队接进 CI/CD"思维 spec |
| 对应原则 | 5（红队前移） |

### prompt spec

文件：`spec-d8-redteam-gate.md`

````markdown
# 让 AI 帮我跑红队 baseline + 设计上线门槛

## 输入
- 一个被测 agent（D3 或 D6a/b 任选一个）
- 业务可接受的 ASR 上限（Attack Success Rate；学员自己定，必须 < 100%）

## 产品口径（2026 当前，讲师必须先和学员讲清）
- 微软现在有两个 Red Teaming Agent：
  1. **云端 Red Teaming Agent**（Foundry 内置）—— 唯一支持把 **Foundry Agents 当 target** 的路径；本课走这条
  2. 本地 PyRIT-based Red Teaming Agent —— **不兼容** Foundry new portal/SDK；本课不用，只在边界澄清时提一下
- 学员真跑走 SDK（指向云端 Red Teaming Agent，target = D3/D6a/b 的 Foundry agent）
- Portal 路径作为讲师演示视图，让学员看一次端到端结果如何呈现；**学员不要求每人当场在 portal 里跑**

## 让 AI 生成的产物清单
1. 看一次讲师 portal 演示（num_objectives=3 起步），理解结果界面 + ASR 数字读法
2. SDK 跑一次云端红队（同 agent 同 attack set），拿到自己的结果 JSON
3. baseline 报告：ASR、按攻击类型分类、Top 3 失败 case
4. CI/CD 接入设计稿（不要求实接，画一张图 + 写 3 条 gate 规则）

## CI/CD gate 设计模板
- gate A：ASR > X% 阻塞 merge
- gate B：新增攻击类型失败率 > Y% 报警
- gate C：[学员自定义]

## 约束
- SDK 必须学员自己跑（target = 自己的 Foundry agent）；portal 是讲师演示，不要求每人当场跑
- baseline 报告必须有数字，不接受"看起来还行"
- Top 3 失败 case 必须人工 review（红队工具能找 case，判定要不要修是人的活）

## Fallback（SDK 跑超时时）
- 若 50min 内 SDK 跑不通：至少完成 SDK 命令 + 配置文件 + 用讲师 sample JSON 完成 baseline 报告结构
- 真实跑通 SDK 转课后 / 综合作业加分项
- portal 由讲师演示完成，不存在"portal 跑不通"的学员场景

## 自验证
- [ ] SDK 跑出的 ASR 是具体数字，且与讲师 portal 演示的量级一致（差 ≤ 2x 算合理）
- [ ] baseline 报告含至少 2-3 个攻击类型分类（取决于 attack set；不足 3 类需在报告说明覆盖缺口及下一步补法）
- [ ] CI/CD gate 3 条规则全填，能给具体阈值
- [ ] Top 3 失败 case 学员能口头判定"修 / 不修 / 加 system prompt 兜底"
````

### negative examples（≥3）

| # | 学员常犯的错 | 反例点 |
|---|--------------|--------|
| 1 | "ASR=0% 才能上线" | 不现实；红队工具会持续找新攻击。设业务可接受阈值 + 持续监控比追零更可行 |
| 2 | 红队结果直接 dump 给 PM 不做人工 review | 红队工具会标"成功"但实际是无害 case；人工 review 不可省 |
| 3 | 把红队当一次性活动跑完就归档 | 红队是 gate，不是 checkbox。模型/prompt/工具变了都要重跑 |
| 4 | 用 portal 跑一次就行不用 SDK | portal 用于探索 / 演示结果界面；SDK 才能接 CI/CD，是学员必跑路径 |
| 5 | 选了本地 PyRIT Red Teaming Agent 当工具 | 本地版**不兼容** Foundry new portal/SDK；要把 Foundry Agent 当 target 必须走云端 Red Teaming Agent |

### 验收 checklist

- [ ] SDK 输出 JSON 真跑或用讲师 sample JSON 完成报告（fallback 见 spec）；portal 由讲师演示，学员无须自交截图
- [ ] baseline ASR 是具体数字（如 23.4%）
- [ ] CI/CD gate 阈值与业务可接受 ASR 上限一致
- [ ] Top 3 失败 case 处置决策有理由（不接受"以后再说"）

### 讲师准备

- 至少 1 个跑通的 baseline portal 演示（讲师本人 Day-7 跑过；课上现场演示给学员看一次）
- **SDK 红队 sample JSON**（学员 fallback 用：跑不通时拿这个做 baseline 报告结构）
- 一份"红队工具当前已知坑"清单（如某类攻击 false positive 高 / 本地 vs 云端 Red Teaming Agent 边界）
- 综合作业评分时 D8 占 20%——评分细则提前给学员看

---

## D9 — 生产化 checklist

### 目标速查

| 项 | 内容 |
|----|------|
| 时长 | 90 min（40 讲 / 30 实操 / 20 评审） |
| Day | 3 |
| 关键产出 | 生产化 checklist 应用清单（学员在自己项目上勾几项） |
| 对应原则 | 5（生产化必修） |

### prompt spec

文件：`spec-d9-prod-checklist.md`

````markdown
# 让 AI 帮我把生产化 checklist 应用到我项目

## 输入
- 我项目当前状态（来自 D3/D5/D6a/b 的产物）
- 业务可接受的事故级别 SLO（例：单次事故 ≤ 30min 恢复 / 月度可用率 ≥ 99.5%）

## checklist（讲师 Day3 上午统一发，学员逐项打勾 + 写差距）

### 事故 / 回滚
- [ ] 有 runbook（事故触发 → 谁响应 → 怎么定位 → 怎么回滚）
- [ ] 回滚单元明确（agent 版本？Bicep stack？模型版本？）
- [ ] 上一次 deploy 的回滚命令现在能否一行跑通

### 监控
- [ ] 三个核心指标接 alert：错误率 / p95 延迟 / 月度成本预算（**阈值从 SLO 反推**，不接受拍脑袋数字）
- [ ] alert 接到真人（不是只发邮件到 noreply）
- [ ] trace 采样率合理（100% 烧钱，10% 找不到长尾）

### 成本采样
- [ ] 每天有自动报表（cost-per-call / cost-per-DAU）
- [ ] 预算超阈值触发硬动作（不是只发邮件）

### CI/CD
- [ ] D8 红队 gate 已接（或明确计划接的时间）
- [ ] Bicep diff 必须人审才能 apply
- [ ] Azure DevOps / GH Actions 对照表（学员选用哪条 + 为什么）

## 让 AI 帮我做的事
1. 把 checklist 每项转成"我项目当前状态：已有 / 部分 / 没有"
2. 没有的项给出最小补法（不超过 1 周工作量）
3. 输出"我项目离生产化还差几项"清单

## 约束
- 不准让 AI 帮你"以后补"——每项必须有明确"已有 / 部分 / 没有"判定
- 部分 / 没有的项必须给具体补法，不接受"加强监控"这种空话

## 自验证
- [ ] checklist 所有项都判定（不留空）
- [ ] 没有 / 部分的项都有最小补法
- [ ] 能口头讲清"我项目离上线还差几项 + 哪项最关键"
````

### negative examples（≥3）

| # | 学员常犯的错 | 反例点 |
|---|--------------|--------|
| 1 | "我们是 startup，生产化 checklist 不适用" | 反了。startup 一个事故就死，反而比大厂更需要薄但全的 checklist |
| 2 | alert 接到 noreply / Teams 频道没人盯 | 没人响应的 alert = 没 alert，更糟（产生"已监控"幻觉） |
| 3 | trace 采样 100% 觉得"安全" | 烧 Application Insights 摄入费；中型项目一个月几千刀就这么没了 |
| 4 | "回滚命令以后写" | 事故发生时再翻 wiki 太晚。runbook 必须在 deploy 前就有 |

### 验收 checklist

- [ ] 学员产出的 checklist 应用清单所有项都判定
- [ ] "没有"的项必须有最小补法（不接受跳过）；若全部"没有"是合理状态（项目尚早），评审段标记"生产化预备"即可，不阻塞验收
- [ ] runbook 至少有 1 条具体事故场景的处置流程
- [ ] 评审段能回答："如果今晚 alert 触发，谁接？怎么响应？"

### 讲师准备

- 一份"事故复盘真实案例"（脱敏的；学员讲解段用）
- runbook 模板（Markdown，学员可裁剪填）
- Azure DevOps 对照 GH Actions 的差异表（讲解段用）

---

## D10 — Foundry 能力边界表

### 目标速查

| 项 | 内容 |
|----|------|
| 时长 | 60 min（35 讲 / 15 实操 / 10 评审） |
| Day | 3 |
| 关键产出 | Foundry 能力边界表（与 plan 第五·五能力地图镜像） + 我项目命中的边界 + 迁移方案 |
| 对应原则 | 1、2（Foundry 不能做什么，AI 知道得最少） |

### prompt spec

文件：`spec-d10-foundry-limits.md`

````markdown
# 让 AI 帮我对照 Foundry 能力边界表，找出我项目命中的边界

## 输入
- plan 第五·五能力地图 + 本节边界表（讲师 Day3 发）
- 我项目 D2 / D6a 决策卡产物

## 边界表（讲师当天发实物，学员对照勾选）
> 13 个能力域与 plan 五·五能力地图一一对应（镜像）；plan 改 → 本表同步改。
> "验证来源"列由讲师 Day-7 填实（官方文档 URL / portal 截图 / fork 实测 三选一）；未验证假设只能列脚注、不进主表、不作为课堂边界结论。

| 能力域 | Foundry 的边界（不能做 / 有限制） | 验证来源 | 命中？ | 迁移方案 |
|--------|--------------------------------|---------|--------|----------|
| Agent Service | 自定义控制流 / 复杂状态机受限 | TODO（Day-7） | [ ] | 切 SDK 路径（D6a） |
| Workflows | visual designer 的版本管理 / code review 不友好 | TODO（Day-7） | [ ] | 用 Agent Service 原生编排或 SDK 自写状态机 |
| Projects | 跨 project 资源共享 / 迁移粒度 | TODO（Day-7） | [ ] | … |
| Connections | 第三方凭证类型覆盖 / 轮换支持 | TODO（Day-7） | [ ] | … |
| Identity | RBAC 粒度 / 跨租户访问 | TODO（Day-7） | [ ] | … |
| Models | 模型目录外的模型支持有限 / 滞后 | TODO（Day-7） | [ ] | … |
| Evaluations / Red Team | 内置 attack set 覆盖范围 / 自定义攻击集成 | TODO（Day-7） | [ ] | … |
| Tracing / Monitoring | 采样率 / 自定义维度 / 摄入成本 | TODO（Day-7） | [ ] | … |
| Deployment | Hosted Agents 外的部署目标支持 / 自托管（ACA）迁移代价 | TODO（Day-7） | [ ] | … |
| Quotas / Cost | TPM / RPM 配额上限 + 增配审批流程 | TODO（Day-7） | [ ] | … |
| SDK / Agent Framework | 与 Agent Service 的能力差 / 版本节奏 | TODO（Day-7） | [ ] | … |
| A2A | 协议成熟度 / 跨 vendor 互通验证 | TODO（Day-7） | [ ] | … |
| MCP | MCP server 集成限制（rebrand 期） | TODO（Day-7） | [ ] | … |

（如需补充：合规 / 数据驻留 / 多租户隔离粒度作为跨能力域的"非功能"边界，由讲师 Day-7 评估是否单列。）

## 让 AI 帮我做的事
1. 我项目命中的边界项打勾
2. 每命中一项，让 AI 给 2 个迁移方案备选
3. 我从备选里选 1 个 + 写出选择理由

## 约束
- 不准把"边界"当"缺点"——边界是中性的，关键是我项目是否命中
- 命中的项必须给迁移方案；没命中的项不要硬找

## 自验证
- [ ] 边界表 13 行全部判定（命中 / 未命中）
- [ ] 命中项都有迁移方案 + 理由
- [ ] 边界表"验证来源"列已由讲师填实（学员看到"TODO"应当反馈）
- [ ] 与 D1 决策卡一致（如果 D1 说"用 Foundry"但 D10 命中 ≥3 项关键边界，需要回去 review D1）
````

### negative examples（≥3）

| # | 学员常犯的错 | 反例点 |
|---|--------------|--------|
| 1 | "Foundry 这些都不能做所以不用 Foundry" | 边界 ≠ 否决。命中 0 项 + 命中 1 项 + 命中 5 项的迁移成本完全不同 |
| 2 | 给"切走"作为唯一迁移方案 | 大多数边界有"绕过"或"混合"方案，不需要全切。AI 容易给极端方案 |
| 3 | 命中边界 = 立刻迁移 | 命中 + 业务暂未触发 = 记录在 risk register，不一定要立刻动 |
| 4 | "我项目没命中任何边界" | 通常是没认真对照。AI 帮你逐项过，至少应该有 1-2 项命中或部分命中 |

### 验收 checklist

- [ ] 边界表 13 行全判定
- [ ] 命中项的迁移方案具体（不接受"考虑切到其他平台"）
- [ ] 与 D1 决策卡一致性检查通过（不一致需写明）
- [ ] 评审段能回答："命中的边界里，哪一项 6 个月内最可能成为阻塞"

### 讲师准备

- **边界表实物（含具体边界描述 + 验证来源）**——13 行覆盖 plan 五·五能力地图全部能力域；Day-7 必须定稿
- 每条边界标注验证来源：官方文档 URL / portal 截图 / fork 实测（三选一硬要求）；"未验证假设"只能作为风险备注列在边界表脚注，不进入主表
- 与 plan 第五·五能力地图的镜像校对（同步更新）
- 至少 3 个迁移方案样本（命中常见边界时给学员参考）

---

## D11 — AI-pair 工作流如何成为团队资产

### 目标速查

| 项 | 内容 |
|----|------|
| 时长 | 35 min（25 讲 / 0 实操 / 10 评审）—— 午饭后轻量开场 |
| Day | 3 |
| 关键产出 | 团队 spec 模板库目录 + 2 个示例 spec 大纲（讲师演示，学员誊抄/裁剪） |
| 对应原则 | 3（每模块交付 prompt spec）、2（MCP 接 Foundry 是 AI 不知道的事） |

### prompt spec

**特殊说明**：D11 无 AI-pair 实操（35min 体量塞不下）。spec 形态 = 讲师演示团队 spec 库的搭建路径，学员誊抄目录结构 + 裁剪 2 个示例 spec 回去用。

文件：`spec-d11-ai-pair-team.md`

````markdown
# 团队 spec 模板库搭建指南（讲师演示用）

## 目录结构（推荐起步）
```
team-specs/
├── README.md              # 本库怎么用、怎么贡献、怎么 review
├── decision-cards/        # 决策卡模板（来自 D1/D2/D6a/D7/D10）
│   ├── foundry-fit.md
│   ├── service-vs-sdk.md
│   └── ...
├── implementation/        # 实现 spec（来自 D3/D4/D5/D6b/D8/D9）
│   ├── single-agent.md
│   ├── provider-abstraction.md
│   └── ...
├── negative-examples/     # 反例库（持续更新）
└── runbooks/              # D9 runbook 模板
```

## 2 个示例 spec 大纲（学员誊抄/裁剪）

### 示例 1：新 agent 上线 spec（基于 D3 + D5 + D9）
- 业务输入：场景 / SLO / 成本预算
- 必填决策：Service vs SDK / provider / 编排模式
- 必交产物：Bicep / 重试策略 / 监控接入 / runbook
- 验收 gate：红队 ASR 阈值 / 成本估算 / checklist 完成度

### 示例 2：新 provider 接入 spec（基于 D4）
- 接口契约（ChatProvider Protocol）
- 必填字段 vs opts 透传规则
- 单测要求（mock provider 必有）
- review checklist（不准污染接口 / 不准超 1 个 if 分支）

## MCP 接 Foundry 的工作流（plan 已说明的两条路径）
- **若 Foundry MCP server 可用**：现场连接演示，学员看 Claude/Cursor 直接读 Foundry 文档
- **若不可用**：讲 Learn URL / SDK docs / portal evidence 喂给 AI 的替代工作流（手动 prompt 模板）

## 团队 spec 库治理
- 谁可以提 spec：所有人
- 谁审 spec：1 个核心维护者 + 1 个使用方
- 反例库怎么更新：每次出事故 → review 是否漏在 spec → 加反例；或新模块/新 provider 上线时主动梳理一轮
- 多久 review 一次全库：季度 + 大模型升级时
````

### negative examples（≥3）

| # | 学员常犯的错 | 反例点 |
|---|--------------|--------|
| 1 | "建个 wiki 就是 spec 库" | wiki 通常没版本、没 review 流程，半年后腐烂。spec 库需要 PR + review |
| 2 | spec 写太死（"必须用 X 模型 + Y temperature"） | spec 不是 SOP；过死的 spec 让 AI 失去判断空间，反而降质量 |
| 3 | 反例库只加不减 | 老反例随平台演化可能失效；半年 review 一次必须有"已废除"标签 |
| 4 | "团队人少不需要 spec 库" | 反了。1-2 人团队 = 知识全在脑子里 = 离职即灭绝。spec 库是知识资产化的最低门槛 |

### 验收 checklist

- [ ] 学员把 spec 库目录结构截图/抄到自己团队文档（不要求脱稿复述）
- [ ] 学员选定带回去用的 2 个示例 spec 之一，能口头讲清"我团队下周怎么开始"
- [ ] 能回答："spec 库谁审？多久 review？"
- [ ] 若 MCP 现场连不上，学员理解替代工作流（不阻塞验收）

### 讲师准备

- **决定 Day3 当天用哪条 MCP 路径**（Foundry MCP server 是否可用，Day-7 验证）
- 团队 spec 库目录结构示例（直接投屏 demo 仓库）
- 2 个示例 spec 的完整文件（学员要拷走的实物）
