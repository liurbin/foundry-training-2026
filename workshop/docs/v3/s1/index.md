# S1：Microsoft Foundry 平台扫盲（90min，不动手）

> 时长：90 min ｜ 形式：讲师讲 + portal 走读 ｜ 凭证要求：无（S1 不连 endpoint）
> 状态：⚠️ 基于 Microsoft Foundry 2026/04-05 官方文档；rebrand 进行中，讲师 Day-7 重抓核对

## 这一段的目标

学员对 **AI / agent 熟，对 Microsoft Foundry 0 知识**——S1 不教 agent 概念，也不让你填决策卡。

90min 用来做一件事：**让你看清 Microsoft Foundry 现在长什么样**。这样 S2 动手时你知道每行代码对应平台的哪个能力。

学完 S1 你应该能：

- 一句话说清"Microsoft Foundry = 什么"（不再以为是 Azure OpenAI 的换名）
- 在 Foundry portal 里指出 Build / Operate / Foundry IQ / Foundry Tools 各自的入口
- 跟讲师对照"你现有的栈"（Responses API / OpenAI Agents SDK / LangGraph / CrewAI / 等），讲出 Foundry 多了/少了什么

## 90min 节奏

| 时长 | 段 | 内容 |
|---|---|---|
| 5min | 一、开场 + 这门课你会得到什么 | — |
| 15min | 二、Foundry 来龙去脉（rebrand + Responses API + 资源模型） | 不绕过历史，但只挑影响代码的事讲 |
| 25min | 三、Foundry 7 能力域全景（portal 走读） | Models / Agent Service / Control Plane / IQ / Tools / AML / Local |
| 15min | 四、Control Plane 5 panes（builder 关心的"治理"层） | Overview / Assets / Compliance / Quota / Admin |
| 10min | 五、What's new April 2026 + builder 视角差异化 | Hosted-agent tracing preview / Model Router / Priority processing / Fireworks 等 |
| 10min | 六、Foundry vs 你的现有栈 | 讲师按入场调研对照 |
| 10min | 七、Q&A + 环境自检 + scenario 自读 | 所有学员 `az account show` + `python -c "import azure.ai.projects"` |

## 一、开场（5 min）

**这门课会给你什么**：

- 看清 Microsoft Foundry 2026 当前的能力地图（不是 2024 末的 Azure AI Foundry）
- 跑通一个 prompt agent（Responses API + agent_reference 形态）
- 用 built-in evaluator 跑一次评测（不是从零写 pytest）
- 看一次 Foundry Control Plane 怎么管 guardrail policy

**这门课不教**：

- ❌ Bicep / azd 部署 IaC—— v3 不走 IaC
- ❌ Hosted agents / Workflow agents 实操（都是 preview）
- ❌ Multi-agent 编排实操——只在能力地图里讲
- ❌ 5 维度评分流程——3 维 pass/fail

## 二、Foundry 来龙去脉（15 min）

> 来源：[What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry)（2026/04/29）

**1 个事实先讲在前面**：**Microsoft Foundry**（注意不是 "Azure AI Foundry"，rebrand 已完成）= 把之前散在 Azure AI Studio / Azure AI Foundry classic / 多个 SDK / Hub-based projects 全部统一到**一个 Azure resource provider namespace** 的产品。

### 旧 → 当前 对照表（影响代码的部分）

| 维度 | 旧 | 当前（2026） |
|---|---|---|
| 品牌 | Azure AI Studio / Azure AI Foundry | **Microsoft Foundry** |
| 周边服务 | Azure AI Services | **Foundry Tools** |
| Portal | Foundry (classic) | **Foundry**（new portal，`https://ai.azure.com` 顶部 New Foundry toggle） |
| Agent API | Assistants API（Agents v0.5/v1）| **Responses API**（Agents v2） |
| API 版本 | 月度 `api-version` | **v1 稳定路由** `/openai/v1/` |
| 资源模型 | Hub + Azure OpenAI + AI Services | **单一 Foundry resource**（含 projects） |
| Python SDK | `azure-ai-inference` / `-generative` / `-ml` / `AzureOpenAI()` 多包 | **`azure-ai-projects` 2.x** + `project.get_openai_client()` |
| 对话术语 | Threads / Messages / Runs / Assistants | **Conversations / Items / Responses / Agent Versions** |
| RBAC 角色 | Azure AI User / Owner / … | **Foundry User / Owner / Account Owner / Project Manager**（rename，权限 ID 不变） |

**核心代码形态**（这就是 S2 动手 0 你会做的事）：

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project = AIProjectClient(
    endpoint="https://<resource>.services.ai.azure.com/api/projects/<project>",
    credential=DefaultAzureCredential(),
)
openai = project.get_openai_client()

# 直接调 model
openai.responses.create(model="gpt-5-mini", input="...")

# 调 prompt agent + 多轮 conversation
openai.responses.create(
    conversation=conv.id,
    extra_body={"agent_reference": {"name": AGENT_NAME, "type": "agent_reference"}},
    input="...",
)
```

讲师会现场跑这段，让你看 codex CLI 怎么干。

## 三、Foundry 7 能力域全景（25 min，portal 走读）

> 来源：[Foundry documentation hub](https://learn.microsoft.com/en-us/azure/foundry/)（2026/04/13）

讲师投屏 `https://ai.azure.com`，对照每个能力域**点开看**。学员不操作，看一遍即可。

| 能力域 | 是什么 | builder 关心点 |
|---|---|---|
| **Foundry Models** | 1,900+ 模型目录：GPT-5 / GPT-4.1 / Claude / Grok / Mistral / DeepSeek-R1 / Phi-4 / Llama …；自动 Tier 升级 | model 切换不改代码（不锁 vendor）；fine-tune 入口 |
| **Foundry Agent Service** | 三种 agent 类型：**Prompt (GA) / Workflow (preview) / Hosted (preview)**；Tool catalog 12 built-in + 4 custom；Toolbox preview | Prompt agent 是 v3 主路径；Hosted agents = container（Micro VM）跑你自己的 LangGraph / Agent Framework 代码 |
| **Foundry Control Plane** | 跨订阅治理：Operate 工具栏下 5 panes | **新 pillar**；管 fleet / compliance / quota / cost；Defender + Purview + Entra + Azure Policy 集成 |
| **Foundry IQ** | 企业知识层 = knowledge base + agentic retrieval + ACL/Purview | 客服 agent 接 FAQ 知识库的真实路径；跟 Fabric IQ / Work IQ 并列三件套 |
| **Foundry Tools**（rebrand） | Speech / Translator / Language / Document Intelligence / Content Understanding / Face（之前叫 Azure AI Services） | 不是 agent 的事，是平台级 AI 服务库 |
| **Azure Machine Learning** | train / pipelines / AutoML | 不是 v3 焦点；ML eng / data scientist 用 |
| **Foundry Local** | 端侧跑 LLM / HuggingFace 模型集成 | offline / edge 场景；v3 不涉及 |

**SDK 4 语言**：Python（GA）/ C#（GA）/ JavaScript（preview）/ Java（preview）。v3 用 Python。

> ⏱️ Day-7：portal 走读时如果某能力域 UI 已变，以当天 portal 为准，不要硬讲文档表述。

## 四、Control Plane 5 panes（15 min，builder 关心的"治理"层）

> 来源：[What is Microsoft Foundry Control Plane?](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview)（2026/05/06）

入口：Foundry portal 右上角 **Operate** 工具栏。

| Pane | 干什么 | builder 视角 |
|---|---|---|
| **Overview** | fleet health / 成本趋势 / run 完成率 / 阻止行为 | 你部了 5 个 agent 后，这是首页 |
| **Assets** | 跨 project 所有 agents / models / tools 清单（version / tag / health / cost / token usage 过滤） | "我们公司有多少 agent 在跑 / 谁的成本最高"——一眼看 |
| **Compliance** | 创建 guardrail policy（**content safety / prompt injection / protected materials**）；scope = subscription / RG；Azure Policy + Defender + Purview 集成 | S2 动手 2 你会用到 |
| **Quota** | 模型部署配额视图；Show all toggle 看未部署模型的可用配额 | 选 region / 模型前先看这里 |
| **Admin** | 项目 / 用户 / 连接资源跨订阅治理 | 不是 builder 日常事，但 IT admin 角色会用 |

**讨论**：你现有的栈（OpenAI / LangGraph / 自管）里 Control Plane 这层等价物是什么？通常是没有——你要自己建 dashboard / 接 Datadog / 写 cost script。

## 五、What's new April 2026（10 min，builder 视角差异化）

> 来源：[What's new in Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/whats-new-foundry)（2026/05/12）

**产品更新（last 30 days）**：

- **Foundry Control Plane** 新 pillar（上节讲过）
- **Agent Monitoring Dashboard**：运营指标 + 评测结果
- **Hosted-agent tracing (Preview)**：debug session details / run steps / tool calls
- **Built-in evaluators**（S2 动手 1 你会用）
- **AI gateway 集成（preview）**
- **Model Router**：自动选模型
- **Priority processing**：保留吞吐
- **Fireworks 模型导入（preview）**：第三方推理 provider
- **GPT Realtime 2.0 (preview)**

**集成层**：

- **LangChain + LangGraph 集成**：tracing 已经接通
- **Microsoft Agent Framework**：微软自家的 multi-agent SDK，AutoGen + Semantic Kernel 合并产物
- **A2A protocol (preview)**：agent 间通信协议
- **MCP**：tool / 工具协议，Foundry 全量支持（remote / local / Azure Functions custom）

**builder 视角差异化卖点**（v3 这门课不能全讲，但你应该知道存在）：

- **Foundry IQ**：把企业知识库做成 ACL 感知的 agentic retrieval——你自己用 LangChain 搭一套要花周
- **Control Plane**：跨订阅 / 跨 platform fleet 管理——你自己写 dashboard 要花月
- **Built-in evaluators + Continuous evaluation**：开箱即用的 eval 体系——你自己用 promptfoo / DeepEval 搭也行，但 Foundry 这套接进 Application Insights + Azure Policy

## 六、Foundry vs 你的现有栈（10 min）

**讲师按入场调研对照**。常见栈：

| 你现有 | Foundry 怎么接 |
|---|---|
| **OpenAI Responses API + 自己 orchestrator** | Foundry SDK 走的是同一个 Responses API；多了 agent_reference / Tracing / Eval / Control Plane |
| **OpenAI Agents SDK** | Foundry **OTel 集成已经接通**（trace 直接在 Foundry portal 看）；可以跑在 Hosted agents 上 |
| **LangGraph / LangChain** | 官方 [LangChain + LangGraph 集成](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/langchain)；可以跑在 Hosted agents 上；tracing 自动接 OTel 语义约定 |
| **CrewAI / AutoGen / Pydantic AI** | 走 Hosted agents（任何 Python 框架都能跑）；tracing 看是否实现了 OTel 语义约定 |
| **自己的 vector DB + LangChain RAG** | 对照 Foundry IQ（knowledge base + agentic retrieval + ACL/Purview）——决定迁不迁 |
| **自己的 MCP server** | Foundry 直接接 remote MCP server / Toolbox preview |

**留 5min** 给学员说自己的栈，讲师回应。

## 七、Q&A + 环境自检 + scenario 自读（10 min）

- **环境自检**：所有学员当场跑：
  ```bash
  az account show
  python -c "import azure.ai.projects; print(azure.ai.projects.__version__)"
  echo $PROJECT_ENDPOINT
  codex --version
  ```
- **scenario 自读**：5min 自己读 [scenario.md](../scenario.md)，了解客服 agent 业务背景 + 5 个 user story。讲师不念。
- 剩下时间 Q&A。

## 课后扩展（S1 没讲透的）

S1 没展开，但 builder 课后该读的：

- [What is Foundry Agent Service?](https://learn.microsoft.com/en-us/azure/foundry/agents/overview)——三种 agent 类型详细对比
- [Tool catalog](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog)——12 built-in + 4 custom tools + Toolbox
- [What is Foundry IQ?](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq)——客服 FAQ 知识库的"正经"做法
- [Agent tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept)——OTel 语义约定 + 多 agent 追踪
- [Agent evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators)——task_adherence / intent_resolution / tool_call_success 等
- v2 三天班完整 11 模块（如果想系统学）：`docs/00-training-plan-v2.md`——⚠️ v2 内容仍基于 Foundry classic 旧口径，2026 上半年已 partially outdated，等讲师升级
