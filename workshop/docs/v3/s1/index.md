# S1：Foundry Builder Orientation（90min，不动手）

> 时长：90 min ｜ 形式：讲师讲 + portal 走读 ｜ 凭证要求：无（S1 不连 endpoint）
> 状态：⚠️ 基于 Microsoft Foundry 2026/04-05 官方文档 + portal 实测截图；rebrand 进行中，讲师 Day-7 重抓核对

## 这一段的目标

学员对 **AI / agent 熟，对 Microsoft Foundry 0 知识**——S1 不做项目设计工作坊，也不让你填自己的项目决策卡。

90min 用来做一件事：**让 builder 看清 Foundry-native agentic solution 的能力地图**。这样 S2 动手时你知道每行代码对应平台的哪个能力，课后也知道这个 pattern 可以迁移到哪里。

学完 S1 你应该能：

- 一句话说清"Microsoft Foundry = 什么"
- 在 Foundry portal 5 个顶级 section（Home / Discover / Build / Operate / Docs）里指出每个干什么
- 讲清一个 Foundry-native workflow 为什么需要 agent、tool / knowledge、eval、guardrail、trace、governance 这几层

## 90min 节奏

| 时长 | 段 | 内容 |
|---|---|---|
| 5min | 一、开场 | 这门课会给你什么 / 不教什么 |
| 2min | 二、Foundry 是什么 | 一句话定位 + portal 入口 |
| 18min | 三、Discover + Build（portal 走读） | 在 portal 上指 S2 会用到的位置 |
| 15min | 四、Operate（Control Plane，Preview） | 跨 project 治理 5 panes |
| 30min | 五、Foundry-native solution pattern | Foundry 独有 3 件 + 三类 builder 怎么迁移 + 12 类 readiness 边界 |
| 15min | 六、Q&A + 环境自检 + scenario 自读 | — |
| 5min | 缓冲 | 讲师机动 |

## 一、开场（5 min）

### 1.1 这门课会给你什么（2 min）

- 看清 Microsoft Foundry 2026 当前的能力地图
- 跑通一个 prompt agent（Responses API + agent_reference）
- 用 built-in evaluator 跑一次评测
- 看一次 Control Plane 怎么管 guardrail policy
- 带走一个可迁移的 Customer Operations Agent pattern
- 知道课程分两层：课内跑通 agent → eval → guardrail → trace 这个 pattern；enterprise readiness 只做标记，不逐项实操，完整清单见 [Enterprise Readiness](../enterprise-readiness.md)

### 1.2 这门课不教（1.5 min）

- ❌ 逐个团队的项目设计 / architecture review
- ❌ Bicep / azd / IaC 部署
- ❌ Hosted / Workflow agents 实操（preview）
- ❌ Multi-agent 编排实操
- ❌ 5 维度评分流程

### 1.3 学员侧约定（1.5 min）

- S1 不动手、不连 endpoint
- S2 才用环境变量；S1 末尾环境自检
- 有问题随时打断，不憋到 Q&A

## 二、Foundry 是什么（2 min）

> 来源：[What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)（2026/04/29）

Microsoft Foundry = Azure 上一个**统一 AI 平台**——一个地方建 model + agent + knowledge base + 治理。

portal 入口：`https://ai.azure.com`（顶部要打开 **New Foundry** toggle）。

这就是 S2 你会用的那个平台。S2 动手 0 会教你装包 + 写第一行代码，S1 不预热。

## 三、Discover + Build：能用什么 + 在 project 里造什么（18 min，portal 走读）

> 来源：[Navigate the Foundry portal](https://learn.microsoft.com/en-us/azure/foundry/how-to/navigate-from-classic#navigate-the-portal)（2026/03）+ 讲师 portal 实测截图
>
> 节奏定位：**只在 portal 上指位置，不讲概念细节**。三种 agent 类型、evaluator 分类、两层 guardrail 关系——S2 动手时会重讲，S1 不预讲。

### 3.0 portal 5 顶级 section 定位（1 min）

讲师投屏 `https://ai.azure.com`，指右上角 5 个 section：

| Section | Scope | 干什么 |
|---|---|---|
| **Home** | 当前 project | 项目概览 + quick actions |
| **Discover** | 当前 project | 浏览 / 选型（看能用什么） |
| **Build** | 当前 project | 实际造（agent / model deployment / eval / guardrail） |
| **Operate** | **跨 projects** | 治理（详见§四） |
| **Docs** | — | 文档链接 |

§三看 **Discover + Build**，§四看 **Operate**。Home / Docs 自己摸索。

### 3.1 Discover：能用什么（5 min）

左栏 5 项（截图 portal 实拍）：

| 子节点 | 是什么 | builder 关心点 |
|---|---|---|
| **Overview** | featured 模型一眼看（GPT-5.4 / claude-opus-4-7 / model-router / Kimi-K2.5 …）| 进 Foundry 第一眼 |
| **Models** | 1,900+ 模型完整目录 | model 不锁 vendor；自动 Tier 升级 |
| **Agents** | agent 模板库（看别人怎么建）| S2 动手 0 之前可以来这里抄一个起手 |
| **Tools** | tool 目录浏览（**1,400+ tools** via 公共 + 私有 catalog；旧 agent docs 口径"12 built-in + 4 custom + Toolbox preview"是 agent 内置子集）| 决定接什么 tool 前看 |
| **Solution templates** | 场景化解决方案模板 | 客户运营 / 企业知识 / 数据分析等开箱场景 |

**顺带提**（builder 该知道存在）：Model Router（preview，自动选模型）/ Priority processing（preview，保留吞吐）/ Fireworks 模型导入（preview，第三方推理 provider）。

### 3.2 Build：在当前 project 里造（12 min）

左栏 8 项（截图 portal 实拍）。**目标：让学员 S2 打开 portal 知道每个子节点在哪、做什么用**——不讲概念。

| 子节点 | portal 上指什么 | v3 哪段会再讲 |
|---|---|---|
| **Agents** | "S2 动手 0 在这里 create agent；trace 在顶部 Traces tab；Workflows 标 Preview" | S2 动手 0 讲三种 agent 类型 |
| **Models** | "deployment 管理 + playground 在这里点开看" | — |
| **Fine-tune** | "v3 不涉及，知道在哪即可" | — |
| **Tools** | "project 内 tool 配置入口" | 课后扩展 |
| **Knowledge** | "**Foundry IQ 的 portal 入口在这里**" | §五 5.1.1 深讲 |
| **Data** | "S2 动手 1 上传 eval dataset 进这里" | S2 动手 1 |
| **Evaluations** | "S2 动手 1 在这里看 report_url + per-evaluator reasoning" | S2 动手 1 讲 evaluator 三类 |
| **Guardrails** | "S2 动手 2 业务层在这里配；和 Operate → Compliance 不是一个东西，§四再讲" | S2 动手 2 + §四 |

**讲师 portal 走读流程**：
- 每个子节点点开看 ~1.5min，按上表"portal 上指什么"那列念一句
- ⚠️ Day-7 portal UI 如有变化以当天为准

## 四、Operate：跨 project 治理（15 min）

> 来源：[Foundry Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview)（2026/05/06）+ portal 实测截图

### 4.0 定位 30s

- 从 Build（造）切到 Operate（管）
- ⚠️ Operate 整体当前 **Preview** 状态（portal Overview 旁明确标 Preview）
- 关键区别：Operate **跨 project + 跨订阅**——Discover / Build 锁定当前 project

### 4.1 5 个左栏子节点（8 min）

| Pane | 干什么 | builder 视角 |
|---|---|---|
| **Overview** | 跨 project + 跨 subscription：Running agents / Estimated cost / Agent success rate / 7D / 1M 视图 | 部 5 个 agent 后这是首页 |
| **Assets** | 所有 agents / models / tools 跨 project 清单 | "谁成本最高、谁版本最旧"——一眼看；**Continuous evaluation 在这里配** |
| **Compliance** | **4 个 tab**：Policies / Guardrails / Security posture / Data security and governance | **S2 动手 2 平台层**走 Policies tab |
| **Quota** | 模型部署配额视图；Show all toggle 看未部署模型可用配额 | 选 region / 模型前看 |
| **Admin** | 项目 / 用户 / 连接资源跨订阅治理 | IT admin 用，不日常 |

### 4.2 现场 portal 演示 Compliance（5 min）

讲师点开 Operate → Compliance（**学员不每人创建**——RBAC 不够），逐 tab 看：

| Compliance tab | 干什么 |
|---|---|
| **Policies** | **Create policy** 按钮在这里 → 选 controls（content safety / prompt injection / protected materials）+ scope（subscription / RG）+ exceptions；Azure Policy 后台跑 |
| **Guardrails** | 跨 project guardrail 状态视图——看 fleet 里 guardrail 配得齐不齐 |
| **Security posture** | 安全态势评估（v3 不展开） |
| **Data security and governance** | Purview / DLP 集成视图（v3 不展开） |

### 4.3 讨论（1.5 min）

你的产品 / 客户方案 / 平台工具里，Operate 这层等价物是什么？
通常要自己建 dashboard、权限治理、成本脚本和 policy 流程；这就是 Foundry Control Plane 要解决的问题。

## 五、Foundry-native solution pattern（30 min）

> 从 builder 视角讲"一个可交付的 agentic solution 为什么不只是 prompt demo"。不做每个团队的项目设计，只给你课后迁移这个 pattern 的判断框架。

### 5.1 Foundry 独有 3 件（10 min）

**5.1.1 Foundry IQ**（3.5 min）
- 是什么：企业知识层 = knowledge base + agentic retrieval + ACL/Purview
- portal 入口：**Build → Knowledge**
- 如果不用平台：需要自己维护 retrieval、引用、权限过滤和数据治理
- 拼出来的差距：ACL/Purview 集成要周；agentic retrieval（多步 query rewrite）要自己调
- builder 关心点：客服 FAQ 知识库的"正经"做法

**5.1.2 Foundry Control Plane（Operate）**（3.5 min）
- 是什么：跨订阅 fleet 治理 + Compliance policy + Quota + Cost
- 如果不用平台：需要自己维护 dashboard、cost script、policy 配置和资产清单
- 拼出来的差距：要月；跨订阅 / 跨 platform 那层基本拼不出来
- builder 关心点：你部 5 个 agent 后这是首页

**5.1.3 Built-in evaluators + Continuous evaluation**（3 min）
- 是什么：开箱 evaluator（task_adherence / coherence / violence / 十几个）+ Operate → Assets 配 continuous evaluation
- 如果不用平台：需要自己维护 eval harness、报告、CI gate 和线上采样评测
- 拼出来的差距：评测能拼，但接不进 Azure 治理体系；continuous evaluation 要自己造
- builder 关心点：S2 动手 1 就用这个

### 5.2 三类 builder 怎么迁移这个 pattern（15 min）

**5.2.1 Product startup**（5 min）
- 把课堂的"订单查询"换成产品内的 support / research / workflow assistant
- 保留：agent version、eval gate、business guardrail、trace
- 课后第一步：选 1 个高频 workflow，写 3 条 happy / edge / adversarial eval

**5.2.2 Solution partner**（5 min）
- 把课堂样例换成客户运营、现场服务、销售运营、合规审核等可交付方案
- 保留：mock-first、工具边界、转人工规则、runbook
- 课后第一步：把客户业务动作分成 query / recommend / mutate 三类，mutate 默认要人工确认

**5.2.3 Platform / infra builder**（5 min）
- 把课堂样例换成 eval gate、tool gateway、agent registry、observability workflow
- 保留：Foundry project endpoint、Control Plane、asset visibility、continuous evaluation
- 课后第一步：选一个平台能力做最小 adapter，而不是直接重建整套 agent runtime

### 5.3 开放 Q（5 min）

- builder 说自己的产品 / 客户 / 平台方向，讲师只帮映射到三类迁移路径
- 重点接住"我的场景是不是一定适合 Foundry"——答案可能是否定的；这节课只给判断依据，不替你完成设计

## 六、Q&A + 环境自检 + scenario 自读（15 min）

### 6.1 环境自检（5 min，所有学员当场跑）

```bash
az account show
python -c "import azure.ai.projects; print(azure.ai.projects.__version__)"
echo $PROJECT_ENDPOINT
codex --version
```
- 讲师在群里收"卡住的"
- 5 min 内解决不掉的让结对完成 S2

### 6.2 scenario 自读（5 min）

- 学员自己读 [scenario.md](../scenario.md)
- Customer Operations Agent 业务背景 + 5 个 user story
- 讲师不念

### 6.3 Q&A（5 min）

- 剩下时间收 S1 整体疑问
- 接不住的挪到 S2 间隙或课后

## 课后扩展（S1 没讲透的）

S1 没展开，但 builder 课后该读的：

- [Enterprise Readiness](../enterprise-readiness.md)——12 类上线边界：身份、网络、数据、部署、quota、安全、tool、eval、日志、DR、成本、运营责任
- [What is Foundry Agent Service?](https://learn.microsoft.com/en-us/azure/foundry/agents/overview)——三种 agent 类型详细对比
- [Tool catalog](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog)——1,400+ tools（公共 + 私有 catalog）+ agent 内置 12+4 子集 + Toolbox
- [What is Foundry IQ?](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq)——企业知识层的"正经"做法
- [Agent tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept)——OTel 语义约定 + 多 agent 追踪
- [Agent evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators)——task_adherence / intent_resolution / tool_call_success 等
- [Navigate the Foundry portal](https://learn.microsoft.com/en-us/azure/foundry/how-to/navigate-from-classic)——portal 完整导航地图
- [What's new in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/whats-new-foundry)——想跟踪月度更新看这里
- v2 三天班完整 11 模块：`docs/00-training-plan-v2.md`——⚠️ v2 内容仍基于 Foundry classic 旧口径，2026 上半年 partially outdated，等讲师升级
