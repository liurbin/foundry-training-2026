# 动手 0：起 Customer Operations Agent + 跑通第一条对话（10min 开场 + 20min 动手 = 30min）

> 时长：30 min（含 S2 开场 10min）｜ 形式：codex CLI 动手 ｜ 凭证：环境变量已配好（见课前引导）
> 状态：⚠️ 具体话术待讲师 Day-7 实测后补；当前是骨架，但 SDK 调用结构已对齐 Microsoft Foundry 2026/05 官方 quickstart

## 开场：评测先行（10 min，讲师讲）

蒸馏自 v2 D7 + D9 + Foundry 官方 [Evaluate your AI agents](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-agent)：

- **写功能前先写评测**——agent 输出是概率性的，没评测就没"做完"的客观标准
- v3 的姿势：动手 0 起 agent → 动手 1 立刻用 **Foundry built-in evaluators** 跑评测 → 动手 2 用 **Control Plane guardrail policy** 加防护再跑回评测 → **评测贯穿 S2 全程**
- 今天用的 endpoint 是讲师统一发的 Foundry project endpoint，业务数据全 mock（见 [scenario.md](../scenario.md)）

## 这一段你要做什么（20 min 动手）

用 codex CLI 让 AI 帮你：

1. 在 Foundry project 里创建一个 **prompt agent**（type = prompt，Foundry 当前 GA 的 agent 类型）
2. 用 `azure-ai-projects` 2.x SDK + Responses API 调它
3. 让 agent 回答一次 `I need to check order ORD-T-12345`
4. 在 Foundry portal 看到这次调用的 trace span（入口和 GA / preview 状态以讲师 Day-7 实测为准）

### 你正在练的能力

把一个业务 workflow 压成**最小可运行 baseline agent**，并留下后续 eval / guardrail 能追溯的版本和 trace 证据。

### 本段产物

- 一个可调用的 `AGENT_NAME` + baseline version。
- 两轮真实 agent 回复：happy path + edge input。
- 一条 portal trace 证据。
- 一份 baseline evidence 记录，供动手 1 / 2 继续使用。

### 不是本段目标

- 不是做完整客服系统。
- 不是接真实订单接口。
- 不是把 system prompt 写到生产可用。

**简化约定**（重要）：

- 订单数据**hardcode 在 agent 的 instructions（system prompt）里**——不调 tool、不读 mock JSON
- 真实生产形态：用 **Function calling / OpenAPI tool** 调外部接口，或用 **Foundry IQ** 接知识库；这些是课后扩展
- scenario.md 里 P0 三个查询能力是**目标蓝图**；动手 0 只做最小集

## 准备

新开终端，激活 venv，检查环境变量：

```bash
source ~/foundry-v3-env/bin/activate
cd ~/foundry-v3-tmp     # 或你课前建的工作目录

# 确认凭证 + 环境变量
az account show | head -5
echo $PROJECT_ENDPOINT
echo $MODEL_DEPLOYMENT_NAME
echo $AGENT_NAME
```

## 步骤 1：让 codex 起 agent（10 min）

进入 codex 交互模式：

```bash
codex
```

进入后，给它这段需求（**这是 v3 推荐 prompt 模板，讲师 Day-7 会迭代**）：

```
帮我用 azure-ai-projects 2.x SDK 在 Microsoft Foundry 里创建一个 prompt agent，名字读环境变量 AGENT_NAME。要求：

1. 用 DefaultAzureCredential 鉴权，endpoint 读 PROJECT_ENDPOINT
2. model 读 MODEL_DEPLOYMENT_NAME
3. instructions（system prompt）：
   "你是一家中等规模电商的客服助手，可以查询订单状态、物流、退款进度。
    重要约束：不要承诺退款，不要主动外呼，遇到客诉升级类话术（要投诉/12315/全额退款威胁等）请转人工。
    你当前 hardcode 知道一条订单：ORD-T-12345 已发货，预计明日到达，物流单号 SF1234567890。
    遇到其他订单号请反问让用户提供有效订单或手机号。"
4. 调用 PromptAgentDefinition + project.agents.create_version
5. 把 agent.name / agent.version 打印出来

写完执行它。
```

**关键**：codex 给你方案时**先审再让它执行**——审 4 件事：

- 包名对不对（必须是 `azure-ai-projects` 不是别的）
- 凭证读法（必须 `DefaultAzureCredential`，不要让它读什么 `OPENAI_API_KEY`）
- 没把 endpoint / token 写进日志
- 没把 instructions hardcode 进代码（应该走变量，方便后面改）

### 期望产物

```
Agent created (name: customer-service-agent-v3-yourname, version: 1)
```

`TODO 讲师 Day-7`：贴一段真实跑出来的 console output + Foundry portal 截图（应该在 Build → Agents 里能看到这个 agent）。

## 步骤 2：跑一次对话（5 min）

继续在 codex 里：

```
现在再写一个脚本调刚才创建的 agent：

1. 用 project.get_openai_client() 拿 OpenAI-compatible client
2. openai.conversations.create() 起一个 conversation
3. openai.responses.create(
       conversation=conversation.id,
       extra_body={"agent_reference": {"name": AGENT_NAME, "type": "agent_reference"}},
       input="I need to check order ORD-T-12345",
   )
4. 打印 response.output_text
5. 接着同一个 conversation 再问一句"那我那个 abc123 的订单呢"，看 agent 怎么反问

执行它。
```

### 期望输出（讲师 Day-7 补真实示例）

```
[第一轮]
您的订单 ORD-T-12345 已发货，预计明日到达，物流单号 SF1234567890。

[第二轮]
您提供的"abc123"不是有效订单号格式，请提供形如 ORD-YYYYMMDD-XXXXX 的订单号，
或留下手机号，我帮您核对。
```

## 步骤 3：在 Foundry portal 看 trace（5 min）

打开讲师发的 Foundry portal 链接（`https://ai.azure.com`，顶部 **New Foundry** toggle 打开），找到你的 project：

1. 顶部 5 个 section 选 **Build**
2. 左栏选 **Agents** → 能看到你刚才创建的 agent，version = 1
3. **Agents 页面顶部** tab 切到 **Traces** → 能看到刚才两次 `responses.create` 调用

> ⚠️ Trace 入口在 **Build → Agents → Traces tab**（顶部，不是 Operate 左栏）。来源：[Set up tracing in Foundry](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup) "In the left navigation, select Agents. At the top, select Traces."

期望看到（来自 Foundry 官方 [Agent tracing 概念](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept)）：

- ✅ 顶层 span：agent 调用
- ✅ 子 span：LLM call（model = 你的 deployment）
- ✅ token 计数（prompt + completion）
- ✅ 时延（端到端 ms）
- ✅ 输入 / 输出 文本

> v3 走 prompt agent server-side tracing；Tracing 文档和部分 portal 体验可能仍标 preview。讲师 Day-7 必须用当天 tenant 确认入口、数据延迟和 GA / preview 状态。

看不到？常见原因：

- 你的 project 还没接 Application Insights（trace 数据存那里——讲师 Day-7 确认 project 已配好；如果 portal 提示 "Connect Application Insights"，说明 project 还没连）
- trace 异步未到（等 30s 刷新）
- agent 没真跑（步骤 1/2 输出是 codex 编的样例文字而不是真返回——回去审代码）

### Baseline evidence 记录

把下面 5 项记下来，后面 eval 和 guardrail 都要引用：

| 项 | 你的值 |
|---|---|
| Agent name |  |
| Baseline version |  |
| Model deployment |  |
| Trace visible? | yes / no |
| Trace entry time / screenshot |  |

## 步骤 4：自检（5 min）

- [ ] `project.agents.create_version` 真跑过一次（codex 执行了 + 你看到 agent name / version）
- [ ] `openai.responses.create` 跑了两次，输出含订单号 + ETA + 物流单号；第二次有反问行为
- [ ] portal trace 看到至少 1 个顶层 span + token 计数
- [ ] 你能用一句话讲清"刚才 codex 做了什么、我审了哪几个点"

### 你应该能复述

- 这个 baseline agent 解决了哪个最小 workflow？
- 你创建的是哪个 agent version？
- 这一步为什么先 hardcode 数据，而不是接真实系统？
- trace 证明了什么，没证明什么？

4 项打勾即动手 0 pass（对应§评分"实操"维度的第一条）。

## Enterprise Readiness checkpoint

这一步课内只验证讲师发的 project endpoint + 当前模型 deployment 能跑通。生产前补：

- **Identity**：runtime 用 managed identity，不用个人 `az login`。
- **Network**：确认 public endpoint 还是 private endpoint，以及 tool outbound 路径。
- **Deployment**：确认 Global / Data Zone / Regional / PTU，不把课堂 shared capacity 当生产建议。
- **Quota**：确认目标模型在目标 region / deployment type 下的 TPM/RPM 足够。

## 常见卡点（讲师 Day-7 补）

| 现象 | 处理 |
|---|---|
| `DefaultAzureCredential failed` | `az login` 重跑；检查 Foundry User 角色 |
| `ModuleNotFoundError: azure.ai.projects` | 没进 venv 或装到了 1.x；`pip install --upgrade "azure-ai-projects>=2.0.0"` |
| `404 Not Found` | `PROJECT_ENDPOINT` 拼接错；复制讲师私信或 portal overview 的完整 project endpoint，不要手工改域名 |
| `AttributeError: 'AgentsOperations' object has no attribute 'create_version'` | 装到了 1.x；同上重装 2.x |
| codex 反复改代码不收敛 | 明确告诉它"先停下，把当前完整 stacktrace 贴出来再改" |
| 真跑通但 portal 看不到 trace | project 还没接 Application Insights——这不是学员问题，告诉讲师 |

## 课后扩展

- **加 tool（function calling 或 MCP）**：把订单查询从 hardcode in instructions 改成调 tool，看 trace 里多一层 `execute_tool` span
- **接 Foundry IQ**：把"FAQ / 退货政策"做成 knowledge base，让 agent 用 agentic retrieval 检索而不是塞 system prompt
- **用 OpenAPI tool 接 mock 订单接口**：把 `mock_orders.json` 包成 FastAPI 服务，写 OpenAPI spec，agent 调它

→ 下一段 [动手 1：用 Foundry built-in evaluators 跑评测](01-eval.md)
