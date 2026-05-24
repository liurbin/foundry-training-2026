# v3 Short Course: Foundry Builder Onboarding (4 hours)

> Course type: 4h short course | Pacing: S1 90min decisions + S2 150min hands-on | Credentials: instructor distributes Foundry project endpoint + Azure account invitation (Entra ID / RBAC, **not an API key**) + model deployment name

## Course positioning

This is a **Foundry platform onboarding for builders**, not a project design workshop.

- In-class goal: understand the minimum closed loop of a Foundry-native agentic solution, and hand-run a transferable pattern
- Not in class: walking each startup / partner through their own project design
- After-class extension: swap the in-class pattern for your product, customer solution, or platform-tool scenario

## What you will do in this course

Around a single **Customer Operations Agent (e-commerce support sample)**, experience the full closed loop of a Foundry-native agentic solution:

1. **Understand Foundry**: what project endpoint / model / agent / tool / knowledge / eval / guardrail / trace each solve
2. **Start the agent**: drive it in natural language with the codex CLI, connecting the agent to the Foundry project endpoint the instructor distributes
3. **Evaluation**: have the codex CLI help you write 4 cases (happy / edge / two adversarial), produce explicit pass/fail
4. **Add a guard**: pick 1 attack, add a business guardrail, then re-run the evaluation to verify
5. **Go-live checklist**: 12 categories of enterprise-readiness boundaries (identity, network, data, deployment, quota, safety, tooling, eval, logging, DR, cost, operations)

## 4h pacing

| Segment | Length | Format | Link |
|---|---|---|---|
| Pre-class | 10min | Self-serve setup | [codex CLI setup guide](prerequisites/codex-cli-setup.md) |
| S1 | 90min | Foundry builder orientation, no hands-on | [S1 Foundry platform tour](s1/index.md) |
| S2 opening | 10min | Evaluation-first argument + endpoint walkthrough | beginning of [s2/00-bootstrap.md](s2/00-bootstrap.md) |
| S2-0 | 20min | Hands-on: start the agent (hardcode simplification) | [s2/00-bootstrap.md](s2/00-bootstrap.md) |
| S2-1 | 55min | Hands-on: write evaluations | [s2/01-eval.md](s2/01-eval.md) |
| S2 Red Team framing | 15min | Instructor talk + demo 1 attack | beginning of [s2/02-guard.md](s2/02-guard.md) |
| S2-2 | 35min | Hands-on: add a guardrail | [s2/02-guard.md](s2/02-guard.md) |
| S2 wrap | 15min | Observability + go-live | [s2/wrap.md](s2/wrap.md) |

Total: S1 90min + S2 (10+20+55+15+35+15)=150min = **240min / 4h**

**Pacing convention**: 4h is a guideline, not a deadline. Whatever segment does not finish, continue after class — see each page's "after-class extension" section.

Go-live boundaries are kept separately in [Enterprise Readiness: 12 go-live boundaries](enterprise-readiness.md). For migrating to a real project, use the [AI Solution Builder Compass](ai-solution-readiness-blueprint.md): first nail down the workflow, action boundaries, eval, safety, and platform-drift questions that a builder must keep top-of-mind, then do the Foundry-specific document research and implementation path.

## Unified sample scenario

The entire course uses the same fictional sample: **Customer Operations Agent (mid-size e-commerce support)**.

We chose customer support not because startups / partners can only build support agents, but because within 4h it can simultaneously cover: business boundaries, mock data, evaluation, prompt injection, out-of-scope promises, trace, and go-live runbook. See [`scenario.md`](scenario.md). S2 hands-on code and evaluation cases all map to this sample — you do not need to bring your own project.

## After finishing the course you should be able to

- Verbally articulate the responsibilities and boundaries of project / agent / model / eval / guardrail / trace inside Foundry
- Use the codex CLI to make an agent produce explicit pass/fail on at least 1 evaluation case
- Explain which attack class the guardrail you added defends against, and why it matters for this workflow
- Explain how your scenario **uses Foundry fully**: when migrating this pattern to your product / customer solution / platform tool, which capabilities to wire up on Day-1, which to fill in after class, which not to wire up at all

All 4 items pass = course pass. **"Cannot block it" also counts as pass** (as long as you can explain why; see [s2/02-guard.md](s2/02-guard.md)).

## What this course does not teach

- ❌ Per-team project design workshop — class gives a pattern, it does not pick a project for you
- ❌ Bicep / azd deployment IaC — v3 uses the codex CLI + SDK to start agents, no IaC path
- ❌ Hands-on multi-agent orchestration — only S1 decision segment covers the framing, no handoff / Workflows hands-on
- ❌ Real business-system integration — all business data is mocked (instructor provides mock JSON under `code/`)
- ❌ 5-dimension scoring process — simplified to 4-item pass/fail

To go through all 11 modules systematically → take the v2 3-day class (site entry: [`handbook/00-training-plan-v2.md`](../../handbook/00-training-plan-v2.md)).

## After class

Each segment has an "after-class extension" section, listing what to do next:

- Product startup: swap the Customer Operations Agent for your product's support / research / workflow assistant
- Solution partner: swap the sample for a customer's service operations, field service, sales operations, or compliance review scenario
- Platform / infra builder: swap the sample for an eval gate, tool gateway, agent registry, or observability workflow
- Use the [AI Solution Builder Compass](ai-solution-readiness-blueprint.md) to assess your real scenario — first nail down workflow / action / eval / risk, then do Foundry-specific mapping
- Replace mock business data with real interfaces
- Fill in [enterprise readiness](enterprise-readiness.md): identity, private networking, data governance, deployment mode, quota, safety controls, tool actions, eval, logging, DR, cost, and operational ownership
- Add more guardrails / multi-agent collaboration / CI/CD integration

The instructor maintains this v3 content on an ongoing basis; raise issues in the after-class group.
