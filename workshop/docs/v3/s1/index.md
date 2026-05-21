# S1：Microsoft Foundry 平台扫盲（90min，不动手）

> 时长：90 min ｜ 形式：讲师讲 + portal 走读 ｜ 凭证要求：无（S1 不连 endpoint）
> 状态：⚠️ 基于 Microsoft Foundry 2026/04-05 官方文档 + portal 实测截图；rebrand 进行中，讲师 Day-7 重抓核对

## 这一段的目标

学员对 **AI / agent 熟，对 Microsoft Foundry 0 知识**——S1 不教 agent 概念，也不让你填决策卡。

90min 用来做一件事：**让你看清 Microsoft Foundry 现在长什么样**。这样 S2 动手时你知道每行代码对应平台的哪个能力。

学完 S1 你应该能：

- 一句话说清"Microsoft Foundry = 什么"
- 在 Foundry portal 5 个顶级 section（Home / Discover / Build / Operate / Docs）里指出每个干什么
- 跟讲师对照"你现有的栈"（Responses API / OpenAI Agents SDK / LangGraph / CrewAI 等），讲出 Foundry 多了/少了什么

## 90min 节奏

| 时长 | 段 | 内容 |
|---|---|---|
| 5min | 一、开场 | 这门课会给你什么 / 不教什么 |
| 3min | 二、Foundry 是什么 | 一句话定位 + S2 你会写到的两个名字 |
| 23min | 三、Discover + Build（portal 走读） | "能用什么"+"在 project 里造什么" |
| 15min | 四、Operate（Control Plane，Preview） | 跨 project 治理 5 panes |
| 26min | 五、为什么不自己拼 + 你的栈怎么接 | Foundry 独有 3 件 + 你现栈对照 |
| 15min | 六、Q&A + 环境自检 + scenario 自读 | — |
| 3min | 缓冲 | 讲师机动 |

## 一、开场（5 min）

### 1.1 这门课会给你什么（2 min）

- 看清 Microsoft Foundry 2026 当前的能力地图
- 跑通一个 prompt agent（Responses API + agent_reference）
- 用 built-in evaluator 跑一次评测
- 看一次 Control Plane 怎么管 guardrail policy

### 1.2 这门课不教（1.5 min）

- ❌ Bicep / azd / IaC 部署
- ❌ Hosted / Workflow agents 实操（preview）
- ❌ Multi-agent 编排实操
- ❌ 5 维度评分流程

### 1.3 学员侧约定（1.5 min）

- S1 不动手、不连 endpoint
- S2 才用环境变量；S1 末尾环境自检
- 有问题随时打断，不憋到 Q&A

## 二、Foundry 是什么（3 min）

> 来源：[What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)（2026/04/29）

### 2.1 一句话定位（1 min）

Microsoft Foundry = Azure 上一个**统一 AI 平台**——一个地方建 model + agent + knowledge base + 治理。

portal 入口：`https://ai.azure.com`（顶部要打开 **New Foundry** toggle）。

这就是 S2 你会用的那个平台。

### 2.2 S2 你会写到的两个名字（2 min）

- **Python 包**：`azure-ai-projects` 2.x
- **核心调用形态**（讲师投屏代码，不让学员跟）：
  ```python
  project = AIProjectClient(endpoint=..., credential=DefaultAzureCredential())
  openai = project.get_openai_client()
  openai.responses.create(input="...", extra_body={"agent_reference": {...}})
  ```
- 关键词记 3 个：`AIProjectClient` / `responses.create` / `agent_reference`——S2 动手 0 就这仨

## 三、Discover + Build：能用什么 + 在 project 里造什么（23 min，portal 走读）

> 来源：[Navigate the Foundry portal](https://learn.microsoft.com/en-us/azure/foundry/how-to/navigate-from-classic#navigate-the-portal)（2026/03）+ 讲师 portal 实测截图

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

### 3.1 Discover：能用什么（6 min）

左栏 5 项（截图 portal 实拍）：

| 子节点 | 是什么 | builder 关心点 |
|---|---|---|
| **Overview** | featured 模型一眼看（GPT-5.4 / claude-opus-4-7 / model-router / Kimi-K2.5 …）| 进 Foundry 第一眼 |
| **Models** | 1,900+ 模型完整目录 | model 不锁 vendor；自动 Tier 升级 |
| **Agents** | agent 模板库（看别人怎么建）| S2 动手 0 之前可以来这里抄一个起手 |
| **Tools** | tool 目录浏览（12 built-in + 4 custom + Toolbox preview）| 决定接什么 tool 前看 |
| **Solution templates** | 场景化解决方案模板 | 客服 / RAG / 数据分析等开箱场景 |

**顺带提**（builder 该知道存在）：

- **Model Router**（preview）：自动选模型，省成本
- **Priority processing**（preview）：保留吞吐，应对高峰
- **Fireworks 模型导入**（preview）：第三方推理 provider

### 3.2 Build：在当前 project 里造（16 min）

左栏 8 项（截图 portal 实拍）：

| 子节点 | 是什么 | v3 哪段会再讲 |
|---|---|---|
| **Agents** | create / version / deploy agent | **S2 动手 0** 在这里 create；**trace 也在这里看**（顶部 Traces tab）|
| **Models** | deployment 管理 + playground | — |
| **Fine-tune** | 模型微调 | v3 不涉及 |
| **Tools** | project 内 tool 配置（function call / MCP / OpenAPI）| 课后扩展 |
| **Knowledge** | **这就是 Foundry IQ 的 portal 入口** | §五 5.1.1 深讲 |
| **Data** | 数据集 / dataset 管理 | S2 动手 1 上传 eval dataset 在这里 |
| **Evaluations** | built-in evaluator + report 视图 | **S2 动手 1** 在这里看 report_url |
| **Guardrails** | project 内 guardrail 配置（content safety 类）| **S2 动手 2 业务层**用这里 |

**深讲 3 个（每个 ~4min）**：

**3.2.1 Build → Agents**（4 min）
- 三种 agent 类型：**Prompt (GA) / Workflow (preview) / Hosted (preview)**
- Workflows tab 当前在 Agents 页面顶部，标 **Preview**
- builder 关心点：
  - Prompt agent 是 v3 主路径
  - Hosted agents = container（Micro VM）跑你自己的 LangGraph / Agent Framework / CrewAI 代码
  - Workflows = 微软自家可视化编排（你 LangGraph 在的位置）

**3.2.2 Build → Evaluations**（4 min）
- built-in evaluator 三类：**Agent**（task_adherence / intent_resolution / tool_call_success）/ **Quality**（coherence / groundedness）/ **Safety**（violence / hate / sexual / self-harm / jailbreak）
- Custom evaluator 入口
- builder 关心点：S2 动手 1 直接用这套，不从零写 pytest

**3.2.3 Build → Guardrails**（4 min）
- project 级 guardrail 配置——content safety + 业务规则
- ⚠️ **和 Operate → Compliance → Guardrails 是两个东西**：
  - **Build → Guardrails**：project 内、agent 级，**学员实际能配**（动手 2 走这条）
  - **Operate → Compliance**：跨 project / 跨订阅，要 Owner / Resource Policy Contributor 权限（动手 2 讲师演示）
- ⚠️ Day-7 讲师 portal 实测补：Build → Guardrails 子页具体能配哪些 control（content filter / prompt shield / jailbreak / protected materials / custom）——官方文档当前在重组（多个 URL 404）

**剩余 5 个子节点点名即可（4 min）**：Models / Fine-tune / Tools / Knowledge（§五会深讲）/ Data

> ⏱️ Day-7：portal 走读时如果某子节点 UI 已变，以当天 portal 为准

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

你现有的栈（OpenAI / LangGraph / 自管）里 Operate 这层等价物是什么？
通常是没有——你要自己建 dashboard / 接 Datadog / 写 cost script。

## 五、为什么不自己拼 + 你的栈怎么接（26 min）

> 把"What's new"和"vs 你的栈"合并。从 builder 视角讲"Foundry 帮你省了什么、你现栈怎么接"。

### 5.1 Foundry 独有 3 件（10 min）

**5.1.1 Foundry IQ**（3.5 min）
- 是什么：企业知识层 = knowledge base + agentic retrieval + ACL/Purview
- portal 入口：**Build → Knowledge**
- 自己拼怎么做：LangChain + 向量 DB + 自写 ACL 过滤
- 拼出来的差距：ACL/Purview 集成要周；agentic retrieval（多步 query rewrite）要自己调
- builder 关心点：客服 FAQ 知识库的"正经"做法

**5.1.2 Foundry Control Plane（Operate）**（3.5 min）
- 是什么：跨订阅 fleet 治理 + Compliance policy + Quota + Cost
- 自己拼怎么做：Datadog dashboard + 自写 cost script + Azure Policy 手配
- 拼出来的差距：要月；跨订阅 / 跨 platform 那层基本拼不出来
- builder 关心点：你部 5 个 agent 后这是首页

**5.1.3 Built-in evaluators + Continuous evaluation**（3 min）
- 是什么：开箱 evaluator（task_adherence / coherence / violence / 十几个）+ Operate → Assets 配 continuous evaluation
- 自己拼怎么做：promptfoo / DeepEval / 自写 pytest harness
- 拼出来的差距：评测能拼，但接不进 Azure 治理体系；continuous evaluation 要自己造
- builder 关心点：S2 动手 1 就用这个

### 5.2 你的现有栈怎么接（12 min，讲师按入场调研对照）

**5.2.1 已经在 OpenAI 生态的**（4 min）
- **OpenAI Responses API + 自己 orchestrator** → 同一个 Responses API，多了 agent_reference / Tracing / Eval / Control Plane
- **OpenAI Agents SDK** → Foundry OTel 集成已接通，trace 直接在 Build → Agents → Traces 看；可跑 Hosted agents

**5.2.2 用 Python 多 agent 框架的**（4 min）
- **LangGraph / LangChain** → 官方集成；可跑 Hosted agents；tracing 自动接 OTel
- **CrewAI / AutoGen / Pydantic AI** → 走 Hosted agents（任何 Python 框架都能跑）；tracing 看是否实现 OTel 语义约定
- **Microsoft Agent Framework** → 微软自家（AutoGen + Semantic Kernel 合并产物），Foundry 一等公民
- **A2A protocol** (preview) → agent 间通信，Foundry 支持

**5.2.3 自管基础设施的**（4 min）
- **自己的 vector DB + LangChain RAG** → 对照 Foundry IQ（Build → Knowledge），决定迁不迁
- **自己的 MCP server** → Foundry 直接接 remote MCP server / Build → Tools / Toolbox preview
- **自己的 evaluation pipeline** → 对照 5.1.3，决定迁不迁

### 5.3 开放 Q（4 min）

- builder 说自己的栈，讲师对照回应
- 重点接住"我现在 X 已经跑得好好的，为什么换"——这是 builder 真正的顾虑

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
- 客服 agent 业务背景 + 5 个 user story
- 讲师不念

### 6.3 Q&A（5 min）

- 剩下时间收 S1 整体疑问
- 接不住的挪到 S2 间隙或课后

## 课后扩展（S1 没讲透的）

S1 没展开，但 builder 课后该读的：

- [What is Foundry Agent Service?](https://learn.microsoft.com/en-us/azure/foundry/agents/overview)——三种 agent 类型详细对比
- [Tool catalog](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog)——12 built-in + 4 custom tools + Toolbox
- [What is Foundry IQ?](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq)——客服 FAQ 知识库的"正经"做法
- [Agent tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept)——OTel 语义约定 + 多 agent 追踪
- [Agent evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators)——task_adherence / intent_resolution / tool_call_success 等
- [Navigate the Foundry portal](https://learn.microsoft.com/en-us/azure/foundry/how-to/navigate-from-classic)——portal 完整导航地图
- [What's new in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/whats-new-foundry)——想跟踪月度更新看这里
- v2 三天班完整 11 模块：`docs/00-training-plan-v2.md`——⚠️ v2 内容仍基于 Foundry classic 旧口径，2026 上半年 partially outdated，等讲师升级
