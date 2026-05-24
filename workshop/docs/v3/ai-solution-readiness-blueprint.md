# AI Solution Builder Compass

> A top-of-mind checklist for builders turning real workflows into AI solutions, with Microsoft Foundry mapping only when it fits.

## 这页解决什么问题

这不是一份正式架构评审，也不是让 AI 给你拍一个 go / no-go 结论。

它的目标是让 startup / partner builder 离开 session 后，面对任何 AI 场景时，脑子里始终挂着一组关键问题：workflow 是否真实、AI 能做什么动作、失败代价是什么、能不能评测、数据和系统边界在哪里、平台能力该接到哪里。

Foundry 是重要实现路径，但不是默认答案。先想清楚 AI solution，再判断哪些部分适合用 Foundry 的 agent、model deployment、eval、guardrail、trace、tool calling、quota、network、RBAC 和 monitoring。

## 你投入什么

- 一个真实或准真实的业务场景。
- 目标用户、输入、输出、业务指标和现有流程。
- 会不会接业务系统、处理敏感数据、执行高风险动作。
- 一个能联网查官方文档的 AI 工具。

## 你得到什么

你不应该只得到“能做 / 不能做”。你应该得到一张风险和验证地图：

- **Top-of-mind answers**：10 个关键问题的当前判断、缺口和下一步。
- **Solution shape**：assistant、copilot、agentic workflow、automation、decision support、tool orchestration，或 non-AI。
- **Action boundary**：哪些只是查询，哪些是建议，哪些会修改业务系统，哪些必须人工确认。
- **Eval / safety seeds**：第一批可执行 eval cases、失败模式和 pass/fail 信号。
- **Foundry fit map**：哪些 Foundry 能力现在该接，哪些课后验证，哪些暂时不接。
- **Evidence / tenant verification list**：哪些必须查 Microsoft Learn，哪些必须在客户 tenant 里确认。
- **Next prototype loop**：下一轮最小验证要做什么、mock 什么、怎么判断是否有效。

## Builder Top-of-Mind：10 个一直要问的问题

### 1. 这是不是一个真实 workflow

不要从“我要加 AI”开始。先说清楚用户今天怎么做、卡在哪里、AI 改善哪个动作。

### 2. 业务指标是什么

节省时间、提高准确率、降低处理成本、减少升级、提升转化率、缩短响应时间，都要落到可观察指标。

### 3. 有没有 ground truth

如果没有标准答案、业务规则、历史案例、专家判断或人工验收标准，eval 会很弱。

### 4. AI 到底执行哪类动作

把动作拆成 `query`、`recommend`、`mutate`。修改订单、发邮件、建工单、触发付款、改权限这类动作默认需要人工确认。

### 5. 失败代价是什么

答错一句话、泄露客户数据、误改系统记录、绕过审批、触发合规事件，不是同一级风险。

### 6. 数据和权限边界在哪里

明确 PII、客户数据、日志留存、加密、RBAC、managed identity、Key Vault、private networking、SIEM 这些是否相关。

### 7. 系统集成是否真实可用

业务 API、权限、测试环境、mock 数据、回滚机制、审计日志，决定 prototype 能不能走向真实验证。

### 8. 怎么评测和持续改进

不要只看 demo 回答是否顺眼。至少准备 happy path、edge case、prompt injection、policy violation、tool misuse、privacy leakage。

### 9. 平台事实是否会漂移

2026 年模型、SDK、portal UI、deployment type、quota、PTU、content filter、abuse monitoring、regional availability 都可能变化。Foundry-specific 结论必须查 Microsoft Learn / Azure 官方文档。

### 10. 下一步验证哪个最大不确定性

不要一上来做完整系统。先选一个最大风险：答案质量、工具调用、安全边界、数据接入、latency、成本或运维可见性。

## 什么时候用

- **客户会前**：把模糊需求变成一组具体问题，避免只聊“能不能加 AI”。
- **prototype 前**：确定第一轮 mock-first loop，不把平台、数据、工具、上线问题混成一团。
- **技术选型前**：先判断 solution shape，再判断 Foundry 接在哪里。
- **上线讨论前**：把 quota、deployment、network、RBAC、content filter、logging、DR、FinOps 等缺口列出来。

## 怎么使用

1. 复制下面 prompt 到能联网的 AI 工具。
2. 填入你知道的项目事实；不知道的留空。
3. 要求 AI 先输出 top-of-mind answers，再做 Foundry mapping。
4. Foundry-specific 内容必须引用 Microsoft Learn / Azure 官方文档。
5. 对 portal UI、SDK、quota、PTU、filter、network、RBAC、CMK、monitoring、DR 等高漂移项，必须标 `must verify in tenant / Day-7`。
6. 读输出时不要把它当最终方案；把它当风险地图和下一轮验证清单。

## Copy/Paste Prompt

```text
You are helping me think like an AI solution builder.

Your job is not to sell me a platform and not to produce a heavy architecture review. Your job is to keep the most important AI solution questions top of mind, turn my scenario into a risk and validation map, and only then map relevant parts to Microsoft Foundry.

Use two layers:

A. General AI Solution Builder Compass
- Do not assume Microsoft Foundry is required.
- First reason about the workflow, users, value, risks, data, actions, evaluation, operating model, and next validation loop.
- Decide whether the solution shape is assistant/copilot, agentic workflow, knowledge/research assistant, automation, decision support, content generation, tool orchestration, platform capability, or non-AI software.

B. Microsoft Foundry Fit Map
- Only do this after the general builder compass.
- For every Foundry-specific claim, first build an evidence pack from current Microsoft Learn / Azure official documentation.
- Do not rely on memory for Foundry facts.

My project facts:
- Industry / customer type:
- Target workflow:
- Users:
- Current process:
- Main pain point:
- Input:
- Expected output:
- Business metric:
- Ground truth / source of truth:
- Will it call business systems? Which ones?
- Will it perform irreversible or high-risk actions?
- Data types / PII / compliance requirements:
- Expected traffic / latency requirement:
- Current cloud / Azure / Foundry status:
- Timeline:
- Known constraints:

Important rules:
- Ask me at most 8 clarification questions if required. If enough information is present, proceed.
- Separate assumptions from confirmed facts.
- For Foundry-specific recommendations, cite evidence item IDs from the evidence pack.
- If a Foundry-specific claim cannot be verified from Microsoft Learn / Azure official docs, mark it "unverified".
- If docs conflict, show both sources and mark the decision "needs human verification".
- For portal UI, SDK methods, project endpoint, agent type, model access, deployment type, quota, PTU, content filtering, abuse monitoring, private networking, RBAC, CMK, monitoring, and DR, mark "must verify in tenant / Day-7".

Output format:

1. Builder Top-of-Mind Answers

Answer these 10 questions:
- Is this a real workflow?
- What business metric should move?
- What ground truth or evaluation signal exists?
- What actions will AI take: query, recommend, or mutate?
- What is the failure cost?
- What data, privacy, permission, and network boundaries matter?
- Are required systems and APIs actually available?
- How will we evaluate and improve it?
- Which platform facts are high-drift and must be verified from docs or tenant?
- What is the next smallest validation loop?

For each answer, include:
- current judgement: green / yellow / red
- why it matters
- missing information
- next question or action

2. Solution Shape

Classify the best current shape:
- assistant / copilot
- agentic workflow
- knowledge / research assistant
- automation
- decision support
- content generation
- tool orchestration
- platform capability
- non-AI software

Explain why, and name one shape that should be avoided for now.

3. Action Boundary

Split actions into:
- query
- recommend
- mutate

For mutate actions, default to human approval or two-step confirmation. Identify actions the AI must never perform directly.

4. Eval and Safety Seeds

Create at least 10 initial eval cases:
- happy path
- edge case
- adversarial / prompt injection
- business policy violation
- tool misuse
- privacy / data leakage

For each case, provide:
- user input
- expected behavior
- failure mode
- pass/fail signal
- evaluator type: deterministic, LLM-judge, custom evaluator, or human review

5. Operating Questions

List the open operating questions for:
- owner
- release gate
- monitoring
- feedback loop
- rollback
- cost signal
- incident handling
- runbook topics

6. Microsoft Learn Evidence Pack

Before giving Foundry-specific recommendations, search current Microsoft Learn / Azure official documentation and produce an evidence pack.

Cover only the areas relevant to this scenario:
- What is Microsoft Foundry / project endpoint / SDK
- Agent Service / agent versions / Responses API
- Foundry IQ / knowledge
- Function calling / tools / MCP
- Evaluation / continuous evaluation / built-in evaluators
- Guardrails / content filter / Prompt Shields / protected material
- Abuse monitoring / modified content filtering / limited access
- Deployment types: Global / Data Zone / Regional / Batch / PTU
- Quota / model availability / model lifecycle
- Private endpoint / managed network
- Application Insights / tracing / monitoring / SIEM export
- RBAC / managed identity / Key Vault / CMK
- Disaster recovery / reliability

For each source, output:
- evidence id
- title
- URL
- last updated date if available
- claims supported
- confidence: confirmed / unclear / conflicting / not found

Use only Microsoft Learn / Azure official docs for Foundry-specific facts. If you must use another source, mark it non-authoritative.

7. Foundry Fit Map

Using only the evidence pack plus my project facts, map Foundry capabilities into three buckets:

Use now:
- Foundry capabilities that directly support the next validation loop.

Verify later:
- Foundry capabilities that may matter for production but require tenant, quota, security, networking, or customer confirmation.

Do not use yet:
- Foundry capabilities that are unnecessary, premature, or not supported by the evidence.

Consider:
- project / environment structure
- model deployment and deployment type
- agent type and versioning
- knowledge approach
- tool / function calling / MCP approach
- eval strategy
- guardrail strategy
- tracing / monitoring approach
- governance approach

For every item, include:
- evidence ids
- assumption
- must verify in tenant / Day-7: yes/no

8. Enterprise Readiness Watchlist

Do not write a heavy audit report. Create a watchlist for:
- governance
- identity / RBAC / secrets
- network
- data / privacy / encryption
- deployment topology / capacity
- model access / quota / lifecycle
- safety controls / content filter / abuse monitoring
- tool action security
- eval / red team / release gate
- observability / logging / SIEM
- reliability / DR / graceful degradation
- FinOps / operations ownership

For each category output:
- why it might matter
- current unknowns
- who must answer
- artifact or evidence needed
- must verify in tenant / Day-7: yes/no

9. Next Prototype Loop

Define one next loop, not a full project plan:
- goal
- largest uncertainty being tested
- what to mock
- what to connect for real
- files / scripts / assets to create if implementation starts
- eval cases to run
- safety guardrail to include
- verification signal
- stop condition

10. What To Keep Top of Mind

End with a concise list of the 5 most important things the builder should not forget for this scenario.
```

## AI 输出后怎么读

不要按“报告是否漂亮”来读。按这 6 个问题读：

- 有没有把 workflow、用户动作、业务指标讲清楚？
- 有没有把 `query` / `recommend` / `mutate` 分开？
- 有没有 eval cases 和可观察 pass/fail signal？
- Foundry-specific 结论有没有 Microsoft Learn / Azure 官方证据？
- 高漂移项有没有标 `must verify in tenant / Day-7`？
- 下一轮 prototype loop 有没有明确验证一个最大不确定性？

## 课内怎么用

v3 课堂不逐项填写这个 compass。课堂只要求你理解：

- Customer Operations Agent 是一个可迁移 pattern，不是唯一场景。
- Foundry 能力要接在真实 workflow 和验证闭环上，不是为了用平台而用平台。
- Enterprise readiness 是上线承诺前必须挂在脑子里的边界，不是 4h 课内评分项。
- 回到真实项目后，用这个 compass 先把问题问对，再决定 Foundry-specific path。
