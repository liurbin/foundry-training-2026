# Wrap-up: observability + go-live checklist (15 min)

> Duration: 15 min | Format: instructor talk + learners self-check against the Customer Operations Agent | No hands-on
> Status: ⚠️ Distilled from v2 D9/D10 + Foundry 2026/05 [Agent tracing concepts](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept) + [Monitor agents dashboard](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard)
>
> Pacing tip: this 15 min is a suggestion; allocate the five subsections as 4+4+3+2+2. The instructor can leave time on the "scoring self-check" and drop the "runbook template" details for learners to read after class.

## 1. Observability trio (4 min)

Your Customer Operations Agent is already visible in the portal trace. **The production minimum also needs**:

1. **Tracing**: every conversation can be traced to a span → seen in hands-on 0
   - v3 uses prompt agent server-side tracing; concrete GA / preview status, entry points and latency are subject to Day-7 tenant verification
   - Hosted / Workflow / Custom agent tracing, scheduled evaluation, red team scan, and similar capabilities may have preview boundaries—confirm support before going to production
   - Trace data lands in the **Application Insights** linked to your project—⚠️ this is **billed separately** (by ingest GB + retention days); estimate peak trace volume before go-live or the month-end bill will blow up
2. **Agent Monitoring Dashboard** (Foundry portal Observability → Monitor): operational metrics + evaluation results aggregated, faster than stitching together your own Datadog
3. **Continuous evaluation**: in Control Plane → **Assets** pane, enable continuous evaluation for a deployed agent—live requests are auto-sampled to run evals, with results flowing back into the dashboard. Preferred for production vs. relying only on CI pre-merge runs

**Customer Operations scenario specifics**:

- A single conversation accumulates tokens across **multiple turns**—one turn looks cheap, 10 turns might blow up
- 429 at peak—operational traffic has intraday peaks and troughs, size Quota for peak (Control Plane → **Quota** pane)

## 2. Go-live checklist (4 min)

**6-item minimum production checklist** (v3 keeps only the essentials in class; full 12 categories in [Enterprise Readiness](../enterprise-readiness.md)):

- [ ] **Environment separation**: dev / staging / prod each have their own Foundry project (or at least independent deployments); prod does not share dev's agent version
- [ ] **Eval gate wired into CI**: every PR runs the hands-on 1 evaluation; at minimum task_adherence happy path does not regress
- [ ] **Guardrail policy enabled**: content safety + prompt injection + protected materials; business rules go via instructions / output filter / tool approval
- [ ] **Observability / logging**: Application Insights + structured log paths defined; whether prompts go into logs is decided
- [ ] **Runbook / rollback**: 429 / 5xx / wrong replies / unauthorized commitments have handling flows; agent version can be rolled back
- [ ] **Cost / quota alert**: TPM/RPM, PTU, Application Insights ingest, daily/monthly budget and alerts set

In-class threading:

- **Touched today**: agent version, eval, guardrail, trace, quota 429, runbook.
- **Must add after class**: identity, private networking, data retention, deployment type, CMK, SIEM, DR, FinOps.
- **Requires customer / Microsoft prerequisites**: PTU capacity, modified abuse monitoring, private networking, enterprise RBAC.

Discussion: how many does your project hit today? Which are Day-1 must-haves?

## 3. Runbook template (3 min)

**Example: Customer Operations Agent 429 throttling handling**:

```markdown
## Customer Operations Agent 429 throttling

### Trigger
Foundry portal Metrics / Application Insights: `RateLimitExceeded` > 5 in a 1 min window

### First response (≤ 5 min)
1. Which deployment is being throttled (dev/staging/prod?)
2. Is the LLM call volume an unusual burst (yes → throttling is correct, no → quota issue)

### Handling
- Real burst: enable 503 throttling fallback (agent returns "system busy, please wait"), no impact to other users
- Quota issue: Control Plane → Quota request to expand quota; temporarily shift traffic to backup deployment or enable **Priority processing** (preview, reserved throughput)

### Notification
- > 10 min without recovery: page oncall + product owner
- Operations side falls back to humans

### Post-mortem
- File an RCA within 24h: burst source / whether it matches capacity plan / adjust Quota threshold
```

The base 4-category runbook is in `workshop/docs/v3/code/runbook.md`; the instructor uses the live environment on Day-7 to add screenshots, owners, and real alert entry points.

## 4. After-class self-study pack (3 min)

What the short course didn't get through, and what you want to continue:

Back in real projects, do not wire up the whole system first. First replicate the in-class loop: `workflow → baseline agent → baseline eval → guarded version → regression eval → trace / report evidence → readiness gaps`.

### Run v3 deeper

- **Real-project migration**: use [AI Solution Builder Compass](../ai-solution-readiness-blueprint.md) to first put workflow, action boundary, eval, security, and platform drift issues into your head, then build the Foundry-specific evidence pack
- **Product startup**: swap the in-class agent for an in-product support / research / workflow assistant; re-run hands-on 0/1/2
- **Solution partner**: swap the in-class agent for a customer ops, field service, sales ops, or compliance review solution; re-run eval + guardrail
- **Platform / infra builder**: swap the in-class agent for an eval gate, tool gateway, agent registry, or observability workflow
- **Wire real interfaces**: replace the hardcoded orders in instructions with **function calling / OpenAPI tool / MCP** calling the real backend
- **Wire Foundry IQ**: build FAQ / return policy as a knowledge base; the agent uses agentic retrieval (with ACL/Purview) instead of stuffing the system prompt
- **Fill in enterprise readiness**: check the 12 go-live boundaries against [Enterprise Readiness](../enterprise-readiness.md)
- **Multi-agent split**: split customer-complaint escalation into a standalone agent; the main agent calls it via connected agents / A2A protocol
- **CI integration**: eval + GitHub Actions as a merge gate
- **Continuous evaluation**: enable for the staging deployment; watch a week of real task_adherence drift

### Foundry platform further reading

| Want to go deeper on | Official entry |
|---|---|
| Detailed comparison of three agent types (Prompt/Workflow/Hosted) | [What is Foundry Agent Service?](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) |
| 1,400+ tools (public + private catalog) + agent built-in 12+4 subset + Toolbox preview | [Tool catalog](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog) |
| Enterprise knowledge + agentic retrieval + ACL | [What is Foundry IQ?](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq) |
| Cross-subscription fleet governance | [Foundry Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview) |
| Tracing + OTel semantic conventions | [Agent tracing concepts](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept) |
| Full evaluator list | [Agent evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators) |
| AI Red Teaming Agent (preview) | [AI red teaming agent](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent) |
| Go-live boundary cheat sheet | [Enterprise Readiness](../enterprise-readiness.md) |
| Real-project top-of-mind framework | [AI Solution Builder Compass](../ai-solution-readiness-blueprint.md) |

### v2 3-day class (systematic study)

The full v2 11 modules are in the repo at `docs/00-training-plan-v2.md`. **⚠️ Note**: v2 is still based on the Foundry classic line (Assistants API / multi-package SDK / monthly api-version), partially outdated in H1 2026—the conceptual structure is usable, but for specific API calls defer to the latest Foundry docs.

## 5. Your scoring self-check (2 min)

Go back to [v3 overview](../index.md) §"What you should be able to do after". All 4 items passing = course passed:

- [ ] **Cognition**: can verbally explain at least 4 of Foundry's 7 capability domains + what each of the 5 Control Plane panes does (S1)
- [ ] **Hands-on**: hands-on 0 ran 1 conversation + hands-on 1 has at least 2 evaluations with clear pass/fail
- [ ] **Transplant**: can explain, when applying this Customer Operations Agent pattern to your product / customer solution / platform tooling, which Foundry capabilities to wire in Day-1, which to add after class, and which not to wire
- [ ] **Security**: can explain which attack types your guardrail blocks, why this workflow matters, and what the platform layer vs. business layer can each solve (whether it actually blocks or not is not the criterion)

Failing any 1 item doesn't affect handing out course materials; the instructor will follow up after class.

## Feedback

In-class blockers / post-class improvement ideas—write **1 sentence** in the group chat. The instructor will fold it back into this v3 content—the next cohort benefits.
