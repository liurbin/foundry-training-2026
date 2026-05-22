# AI Solution Readiness Blueprint

> A doc-grounded workflow for assessing real AI opportunities and mapping them to Microsoft Foundry when it fits.

## 这是什么

这是 v3 短课的带走物。它不是让 AI 直接替你拍脑袋写方案，而是让 AI 先做 **general AI solution assessment**，再在需要 Foundry 时做 **Microsoft Learn evidence pack** 和 Foundry-specific implementation path。

适合三类人：

- Product startup：评估一个 AI capability 是否值得做进产品。
- Solution partner：评估一个客户 workflow 是否适合交付为 AI solution。
- Platform / infra builder：评估是否要做 eval、tool gateway、agent registry、observability 等平台能力。

## 使用规则

复制下面 prompt 到你常用的 AI 工具里。要求 AI 严格遵守：

1. 不默认 Microsoft Foundry 是唯一答案。
2. 先做 general assessment，再做 Foundry-specific mapping。
3. Foundry-specific 结论必须先查 Microsoft Learn / Azure 官方文档。
4. 每个高漂移结论必须标注 `must verify in tenant / Day-7`。
5. 没有证据的地方标 `unverified`，不能编。

高漂移项包括：portal UI、SDK 方法、project endpoint、agent type、deployment type、model availability、quota、PTU、content filter、abuse monitoring、private networking、RBAC、CMK、monitoring、DR。

## Copy/Paste Prompt

```text
You are helping me assess a real AI solution opportunity.

Your job is not to sell me a platform. Your job is to help me decide whether this workflow should use AI at all, what solution pattern fits, and whether Microsoft Foundry is an appropriate implementation path.

Use two layers:

A. General AI Solution Readiness
- Do not assume Microsoft Foundry is required.
- Decide whether this is better as assistant/copilot, agentic workflow, knowledge/research assistant, automation, decision support, tool orchestration, or non-AI software.

B. Microsoft Foundry Implementation Readiness
- Only do this after the general assessment.
- For every Foundry-specific claim, first build an evidence pack from current Microsoft Learn / Azure official documentation.
- Do not rely on memory for Foundry facts.

My project facts:
- Industry / customer type:
- Target workflow:
- Users:
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
- If a claim cannot be verified from Microsoft Learn / Azure official docs, mark it "unverified".
- If docs conflict, show both sources and mark the decision "needs human verification".
- For portal UI, SDK methods, model access, deployment type, quota, PTU, content filtering, abuse monitoring, private networking, RBAC, CMK, monitoring, and DR, mark "must verify in tenant / Day-7".

Output format:

1. General AI Solution Assessment

Assess the workflow using:
- workflow volume
- business metric
- ground truth / evaluability
- user journey
- action boundary
- integration availability
- risk level
- change management

For each dimension, mark green / yellow / red and explain briefly.

Then classify the solution pattern:
- assistant / copilot
- agentic workflow
- knowledge / research assistant
- automation
- decision support
- content generation
- tool orchestration
- should not use AI

2. Action Boundary

Split all actions into:
- query
- recommend
- mutate

For mutate actions, default to human approval or two-step confirmation. Identify actions the AI must never perform directly.

3. General Evaluation and Safety Plan

Create at least 10 eval cases:
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
- whether it can be deterministic, LLM-judge, or custom evaluator

4. General Operating Model

Define:
- owner
- release gate
- monitoring
- feedback loop
- rollback
- cost signal
- runbook topics

5. Microsoft Learn Evidence Pack

Before giving Foundry-specific recommendations, search current Microsoft Learn / Azure official documentation and produce an evidence pack.

Cover, if relevant:
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

6. Foundry-Specific Implementation Path

Using only the evidence pack plus my project facts, recommend:
- project / environment structure
- model deployment and deployment type
- agent type and versioning
- knowledge approach
- tool / function calling / MCP approach
- eval strategy
- guardrail strategy
- tracing / monitoring approach
- Control Plane / governance approach

For every recommendation, include:
- evidence ids
- assumption
- must verify in tenant / Day-7: yes/no

7. Enterprise Readiness Checklist

Assess 12 categories:
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
- current assumption
- missing information
- recommended decision
- owner
- artifact to produce
- must verify in tenant / Day-7: yes/no

8. Prototype Loops

Use model-execution loops, not human project-management phases.

Loop 1: mock-first agent
- goal
- files / scripts to create
- verification

Loop 2: eval + guardrail
- goal
- eval cases
- verification

Loop 3: tool / knowledge / observability
- goal
- integration boundary
- verification

9. Stop / Proceed Decision

Choose one:
- proceed now
- proceed after prerequisites
- do not proceed yet

Explain the reason in terms of:
- business value
- evaluability
- action risk
- integration readiness
- Foundry readiness
- missing tenant verification
```

## 人工检查清单

AI 输出后，先检查这 6 件事，再拿去和客户或团队讨论：

- [ ] General assessment 没有默认“必须用 Foundry”。
- [ ] Foundry-specific 部分有 Microsoft Learn evidence pack。
- [ ] 每个 deployment / quota / filter / networking / RBAC 结论都标了证据或 `unverified`。
- [ ] 所有不可逆动作都被归到 `mutate`，并要求 human approval。
- [ ] Eval cases 覆盖 happy / edge / adversarial / policy / tool misuse / privacy。
- [ ] Day-7 / tenant verification checklist 清楚列出谁负责补证据。

## 课内怎么用

v3 课堂不逐项填写这个 blueprint。课堂只要求你理解：

- Customer Operations Agent 是一个可迁移 pattern，不是唯一场景。
- Enterprise readiness 是生产承诺前的边界，不是 4h 课内评分项。
- 回到真实项目后，用这个 blueprint 先判断该不该做，再决定是否走 Foundry-specific path。
