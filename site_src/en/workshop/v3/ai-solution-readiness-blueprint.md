# AI Solution Builder Compass

> A top-of-mind checklist for builders turning real workflows into AI solutions, with Microsoft Foundry mapping only when it fits.

## What this page solves

This is not a formal architecture review, and it is not a prompt that asks AI to hand you a go / no-go verdict.

The goal is to make sure that after the session, a startup or partner builder facing any AI scenario keeps a fixed set of questions in mind: is the workflow real, what actions can AI take, what is the failure cost, can it be evaluated, where are the data and system boundaries, and where should platform capabilities plug in.

Foundry is an important implementation path, but not the default answer. First reason about the AI solution, then decide which parts fit Foundry's agent, model deployment, eval, guardrail, trace, tool calling, quota, network, RBAC, and monitoring.

## What you bring

- A real or near-real business scenario.
- Target users, inputs, outputs, business metrics, and the existing process.
- Whether it will touch business systems, handle sensitive data, or perform high-risk actions.
- An AI tool that can reach the public internet to read official docs.

## What you get

You should not just get a "can do / cannot do" answer. You should get a risk and validation map:

- **Top-of-mind answers**: current judgement, gaps, and next step for 10 key questions.
- **Solution shape**: assistant, copilot, agentic workflow, automation, decision support, tool orchestration, or non-AI.
- **Action boundary**: which actions are pure queries, which are recommendations, which mutate business systems, and which must require human confirmation.
- **Eval / safety seeds**: a first batch of executable eval cases, failure modes, and pass/fail signals.
- **Foundry fit map**: which Foundry capabilities to wire in now, which to verify after class, and which to leave out for now.
- **Evidence / tenant verification list**: which items must be checked against Microsoft Learn, and which must be confirmed inside the customer tenant.
- **Next prototype loop**: what the next minimal validation should do, what to mock, and how to judge whether it worked.

## Builder Top-of-Mind: 10 questions to keep asking

### 1. Is this really a workflow

Do not start from "I want to add AI". First describe how the user does it today, where they get stuck, and which step AI improves.

### 2. What is the business metric

Saving time, raising accuracy, lowering handling cost, reducing escalations, increasing conversion, shortening response time — each must land on an observable metric.

### 3. Is there any ground truth

If there is no reference answer, business rule, historical case, expert judgement, or human acceptance criterion, your eval will be weak.

### 4. What kind of action will AI actually perform

Split actions into `query`, `recommend`, and `mutate`. Modifying orders, sending email, opening tickets, triggering payments, or changing permissions should default to requiring human confirmation.

### 5. What is the failure cost

A wrong sentence, leaking customer data, mis-editing a system record, bypassing approval, or triggering a compliance incident are not the same level of risk.

### 6. Where are the data and permission boundaries

Be explicit about whether PII, customer data, log retention, encryption, RBAC, managed identity, Key Vault, private networking, and SIEM are relevant.

### 7. Is the system integration actually usable

Business APIs, permissions, test environments, mock data, rollback paths, and audit logs decide whether a prototype can progress to real validation.

### 8. How will you evaluate and keep improving it

Do not judge by whether the demo answer looks pleasant. At minimum prepare happy path, edge case, prompt injection, policy violation, tool misuse, and privacy leakage.

### 9. Which platform facts may drift

In 2026, models, SDKs, portal UI, deployment type, quota, PTU, content filter, abuse monitoring, and regional availability can all change. Foundry-specific conclusions must be checked against Microsoft Learn / Azure official docs.

### 10. Which biggest uncertainty does the next step validate

Do not build the whole system up front. Pick the single largest risk first: answer quality, tool calling, safety boundary, data access, latency, cost, or operational visibility.

## When to use it

- **Before a customer meeting**: turn vague requests into a concrete list of questions, instead of only debating "should we add AI".
- **Before a prototype**: lock down the first mock-first loop, so platform, data, tools, and go-live concerns do not collapse into one blob.
- **Before tech selection**: decide the solution shape first, then decide where Foundry plugs in.
- **Before a go-live discussion**: list the gaps in quota, deployment, network, RBAC, content filter, logging, DR, and FinOps.

## How to use it

1. Copy the prompt below into an AI tool that can reach the internet.
2. Fill in the project facts you know; leave the rest blank.
3. Ask the AI to produce top-of-mind answers first, and only then do the Foundry mapping.
4. Foundry-specific content must cite Microsoft Learn / Azure official docs.
5. For high-drift items such as portal UI, SDK, quota, PTU, filter, network, RBAC, CMK, monitoring, and DR, mark them `must verify in tenant / Day-7`.
6. When reading the output, do not treat it as a final plan; treat it as a risk map and a checklist for the next validation loop.

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

## How to read the AI output

Do not read it by "is the report polished". Read it against these 6 questions:

- Does it clearly state the workflow, user actions, and business metric?
- Does it separate `query` / `recommend` / `mutate`?
- Are there eval cases with observable pass/fail signals?
- Do Foundry-specific conclusions cite Microsoft Learn / Azure official evidence?
- Are high-drift items marked `must verify in tenant / Day-7`?
- Does the next prototype loop explicitly validate one biggest uncertainty?

## How it is used in class

The v3 classroom does not fill in this compass item by item. The class only requires you to understand:

- Customer Operations Agent is a transferable pattern, not the only scenario.
- Foundry capabilities should plug into a real workflow and a validation loop, not be used for the sake of using the platform.
- Enterprise readiness is a boundary you must keep in mind before any go-live commitment, not a graded item inside the 4-hour class.
- Back on a real project, use this compass to ask the right questions first, and only then decide the Foundry-specific path.
