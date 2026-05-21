# S1：Foundry 介绍 + 决策对齐（90min，不动手）

> 时长：90 min ｜ 形式：讲师讲 + 集体口头表态 ｜ 凭证要求：无（S1 不连 endpoint）

## 这一段的目标

S1 不写代码，也不让学员**填决策卡**——填卡是 v2 三天班的产物形态（学员带自己项目），4h 短课塞不下"填卡 + 评审"流程。

S1 90min 用来做两件事：

1. **30min 把 Foundry 是什么、当前能做什么、不能做什么讲清**——蒸馏自 v2 D10 能力边界表（14 行）+ D5 部署 / 容量对照
2. **40min 用 D1/D2 决策维度做集体口头表态**——拿客服 agent 当例子，每个维度集体回答 yes/no + 一条理由

学完 S1 你应该能：

- 在能力边界表里指出"客服 agent 用得到的 5-6 行" + "可能命中边界的 1-2 行"
- 当场口头给出"客服 agent 用 / 不用 / 部分用 Foundry"的明确结论
- 选 Agent Service 还是 SDK 时，能用 D2 四维度说一句话理由

## 90min 节奏

| 时长 | 段落 | 集体产出 |
|---|---|---|
| 30min | 一、Foundry 介绍：能力边界 + 部署 / 容量分层 | 学员能口头指出客服 agent 命中 / 不命中的边界行 |
| 10min | 二、客服场景介入 + 用得到哪几行 | 在边界表上集体圈出 5-6 行 |
| 40min | 三、决策对齐：D1 用不用 + D2 Service vs SDK + D7 单 vs 多 agent | 三组维度集体口头表态，每组给一条理由 |
| 10min | 四、Q&A + S2 预告（环境自检） | 所有学员 `codex --version` 有输出 |

## 一、Foundry 介绍：能力边界 + 部署 / 容量分层（30 min）

> 来源：v2 `prep-artifacts/day-7/specs/spec-d10-foundry-limits.md`（14 行边界表）+ `docs/01-instructor-handbook-v2.md` D5 段（部署 / 容量分层）。
> v3 不重写最新能力——v2 已基于 2026/05 官方文档锚点整理过；这里只挑客服 agent 用得到的子集讲。

### 1a. 能力边界表（v2 D10 镜像，挑 6 行讲，15 min）

完整 14 行见 v2 `spec-d10-foundry-limits.md`。v3 短课聚焦客服 agent 高频用到的：

| # | 能力域 | 客服 agent 视角的边界 | 命中阀值 |
|---|---|---|---|
| 1 | Agent Service | 三种 agent 类型分层：prompt / workflow / **hosted**；自定义控制流 = Hosted | 客服只用 prompt agent 即可 |
| 6 | Models | 模型目录（Azure OpenAI 直供 + 第三方）；Tier 1-6 自动 quota 升级 | **具体 model 名以讲师 Day-7 私信为准**——rebrand 期目录会漂 |
| 7 | Red Team | 本地 PyRIT **不兼容** Foundry new portal/SDK；要把 Foundry agent 当 target 必须走云端 Red Teaming Agent；区域受限 5 个 region | S2 动手 2 不真接红队工具，只讲框架；命中边界仅供讨论 |
| 8 | Tracing | OTel + App Insights；**仅 prompt agents GA**，hosted/workflow/custom 仍 preview | 客服走 prompt agent，落在 GA 范围 |
| 9 | Deployment | **Hosted Agents** 是当前主路径：托管容器、scale-to-zero、~15min idle 释放、session 文件 30 天；ACA 是 legacy | 客服默认走主路径 |
| 14 | MCP | remote MCP / Azure Functions custom MCP；rebrand 期 Toolbox preview | 客服可接也可不接，看真接口形态 |

讲师 demo：现场打开 v2 D10 spec，对照官方 learn.microsoft.com 锚点演示**怎么查最新能力**——而不是背 model 名。

### 1b. 部署 / 容量分层（v2 D5 镜像，15 min）

| 部署目标 | 何时选 | 客服 agent 默认 |
|---|---|---|
| **Hosted Agents**（主路径） | 默认 | ✅ |
| Container Apps 自托管 | 必须自托管 / VNet 强约束 / 私有 Azure | 仅有合规要求时 |
| SDK self-host（AKS / VM） | 跨云 / 自带 K8s | 客服基本不会 |

| 容量模式 | 何时选 | 客服 agent 默认 |
|---|---|---|
| **PAYG + 默认配额** | 默认 / POC / 中小规模 | ✅ |
| Quota increase | 流量上涨但不想买 commitment | 上线后视情况 |
| PTU / Reservation | 高吞吐 + 稳定 SLA / 锁价 | 客服规模化后再考虑 |

讨论：客服 agent 上线 6 个月内会不会触发 PTU 阀值？通常不会——这就是为什么 v3 短课不做 PTU 实操。

## 二、客服场景介入 + 用得到哪几行（10 min）

读 [scenario.md](../scenario.md) §业务背景 + §Agent 能力范围。

集体在边界表上**圈**——讲师投屏，学员口头答：

- 客服 agent 用得到 1a 表的哪几行？（预期答：1 / 6 / 8 / 9，可能加 14）
- 可能**命中边界**的是哪几行？（预期答：7 红队区域受限——但 v3 不真跑；其他基本不命中）
- 不需要的能力域有哪些？（A2A / Workflows / Capacity dedicated / Identity 跨租户 …）

10min 走完即过——不强求每个学员都答对，目的是让学员**知道边界表是查询入口**，需要时翻 v2 D10。

## 三、决策对齐：三组维度口头表态（40 min）

蒸馏自 v2 D1（用不用 Foundry）+ D2（Service vs SDK）+ D7（单 vs 多 agent）。**学员不填卡**，每个维度集体口头答 yes/no + 一条理由，讲师板书。

### 3a. D1：客服 agent 用 / 不用 / 部分用 Foundry（15 min）

8 条决策维度（蒸馏自 v2 D1 决策卡）：

- [ ] 需要托管 agent 运行时 + 状态管理 → 倾向 Foundry
- [ ] 需要 Azure 生态（AAD / Key Vault / App Insights）原生集成 → 倾向 Foundry
- [ ] 有合规 / 数据驻留要求 → 倾向 Foundry
- [ ] 需要 portal 上让非工程师配 agent / 看 trace → 倾向 Foundry
- [ ] 只需要单次 LLM call，无 agent 概念 → **不用** Foundry
- [ ] 核心模型在 Azure 目录外（Claude / Gemini / 自托管）且不打算切 → **不用** Foundry
- [ ] 研究 demo / hackathon，下周扔 → **不用** Foundry
- [ ] 已有成熟 LangGraph / CrewAI 生产栈，无迁移动机 → **不用** Foundry

集体过：客服 agent 命中哪几条"倾向"？哪几条"不用"？预期结论 = **用 Foundry**（命中前 2 条 + 不命中后 4 条）。

不强求一致——学员可以反驳"我们公司客服已有 LangGraph"，讲师追问"迁移成本 vs 收益"。

### 3b. D2：Agent Service vs SDK（15 min）

四维度（v2 D2，1-5 打分），客服 agent 口头估值：

| 维度 | 客服 agent 估值 | 倾向 |
|---|---|---|
| 托管运行时（不想自己跑 worker） | 强（4-5） | Service |
| Portal 可视化（PM/SA 直接配） | 弱-中（2-3） | — |
| 代码完全控制（自定义编排 / 状态） | 弱（1-2） | — |
| 跨 provider 移植性 | 中（3） | — |

口径：前两项 ≥ 后两项 → **Agent Service**。客服 agent 是 Service 的典型场景。

硬约束扫一遍：客服 agent 通常**不命中**私有部署 / VNet 隔离——除非业务有特殊要求。

### 3c. D7：单 agent vs 多 agent（10 min）

三问（v2 D7）：

1. 职责能不能在一个 system prompt 讲清？→ 客服核心能力（订单 / 物流 / 退款工单）能讲清 → 单 agent 起步
2. 需不需要显式编排？→ "先查订单 → 判退款资格 → 创建工单"这条链可以放 function calling 里，不需要 multi-agent
3. 要稳定 tool 调用图 / trace replay？→ 上线后要，但 v3 课中不做

预期结论：**v3 课中走单 agent + function calling**；多 agent（客诉升级 agent）作为生产化扩展，留课后。

## 四、Q&A + S2 预告（10 min）

- 所有学员当场跑：`codex --version` + `echo $OPENAI_BASE_URL`，确认环境就绪
- S2 第一段动手 0：用 codex CLI 把刚才讨论的"客服 agent 用 Agent Service + 单 agent"这个决策落到代码

## 课后扩展

S1 没讲透的内容（4h 课只能这样）：

- v2 D1 完整决策卡：`workshop/docs/d01_concepts/`
- v2 D2 完整决策卡 + 成本估算：`workshop/docs/d02_agent_vs_sdk/`
- v2 D7 多 agent 三选一实操：`workshop/docs/d07_multi_agent/`
- v2 D10 14 行边界表完整版（含官方 URL 锚点）：`prep-artifacts/day-7/specs/spec-d10-foundry-limits.md`
- v2 D5 部署 / 容量分层完整讨论：`docs/01-instructor-handbook-v2.md` D5 段
