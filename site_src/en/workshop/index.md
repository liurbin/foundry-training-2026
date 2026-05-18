# Learner Workshop

> 3 days, 11 decision modules, 45 learner subtasks, and one capstone.

The learner path is designed for AI-native developers. The instructor explains
platform decisions and hidden constraints; learners write specs, ask AI to
implement, and verify the result.

## Credential Model

Learners are not required to bring an Azure subscription.

| Path | How it works |
|------|--------------|
| Learner default | Mock provider, local stubs, sample JSON, prepared repos, and decision cards. |
| Instructor demo | Real Foundry portal, model deployments, tracing, red-team runs, and live provider switch. |
| Learner optional | Learners with their own Azure subscription may run selected deployment steps after class. |

## Module Map

| Module | Duration | Type | Learner outcome |
|--------|----------|------|-----------------|
| [D1: Concepts and Decision Framework](../../workshop/d01_concepts/) | 45 min | Decision | A Foundry fit card for the learner's own project. |
| [D2: Agent Service vs SDK](../../workshop/d02_agent_vs_sdk/) | 90 min | Decision | A scored platform choice with hard constraints and cost inputs. |
| [D3: Single-Agent Platform Path](../../workshop/d03_single_agent/) | 120 min | Hands-on | A minimal Foundry agent, external invocation path, and trace observation checklist. |
| [D4: Provider Abstraction](../../workshop/d04_provider_abstraction/) | 90 min | Hands-on | A `ChatProvider` interface plus a mock provider that works without cloud credentials. |
| [D5: Deployment, Capacity, Scaling, and Cost](../../workshop/d05_scaling_cost/) | 90 min | Hands-on | Retry with jitter, cache policy, cost estimate, deployment choice, and capacity choice. |
| [D6a: Agent Framework SDK Boundary](../../workshop/d06a_sdk_boundary/) | 60 min | Decision + hands-on | A clear decision on whether and when to switch from Agent Service to SDK. |
| [D6b: A2A + MCP Boundary](../../workshop/d06b_a2a_mcp/) | 60 + 45 min | Hands-on | A2A vs MCP decision card and at least one runnable local demo or prepared trace. |
| [D7: Multi-Agent Orchestration](../../workshop/d07_multi_agent/) | 120 min | Hands-on | A three-way decision across Agent Service native orchestration, `as_tool`, and Workflows. |
| [D8: Red-Team Baseline](../../workshop/d08_red_team/) | 105 min | Hands-on | A baseline report with ASR, attack categories, false-positive review, and gate rules. |
| [D9: Production Checklist](../../workshop/d09_production/) | 90 min | Decision | A production-readiness checklist with concrete gaps and minimum fixes. |
| [D10: Foundry Capability Boundary Table](../../workshop/d10_boundary/) | 60 min | Decision | A 14-row boundary table mapped to the learner's own project. |
| [D11: AI-Pair Workflow](../../workshop/d11_ai_pair/) | 35 min | Decision + workflow | A team spec-library starting structure and two reusable example spec outlines. |

## Day 1

Day 1 builds the platform decision foundation.

| Time | Module | What gets produced |
|------|--------|--------------------|
| 09:00-09:45 | D1 | Foundry fit decision card and capability-map placement. |
| 10:00-11:30 | D2 | Agent Service vs SDK decision card with hard constraints. |
| 11:30-14:30 | D3 | Single-agent path, `agent_reference` invocation, and trace checklist. |
| 14:45-16:15 | D4 | Provider abstraction and live switch observation notes. |
| 16:30-18:00 | D5 | Deployment and capacity note, retry, cache, and cost estimate. |

## Day 2

Day 2 expands the path from one agent to SDK, A2A, MCP, multi-agent
orchestration, and red-team gating.

| Time | Module | What gets produced |
|------|--------|--------------------|
| 09:30-10:30 | D6a | SDK boundary decision card and code comparison table. |
| 10:45-12:30 | D6b | A2A/MCP decision card, trace observation, and fallback demo evidence. |
| 13:30-15:30 | D7 | Multi-agent orchestration decision card and trace review. |
| 15:45-17:30 | D8 | Red-team baseline report and CI/CD gate design. |

## Day 3

Day 3 turns the course into production and team workflow assets.

| Time | Module | What gets produced |
|------|--------|--------------------|
| 09:00-10:30 | D9 | Production checklist application and runbook draft. |
| 10:45-11:45 | D10 | Foundry boundary table mapped to each learner project. |
| 11:45-12:30 | Capstone kickoff | Scenario choice, required outputs, and scoring expectations. |
| 13:30-14:05 | D11 | Team spec-library structure and two example spec outlines. |
| 14:05-18:45 | Capstone | Implementation, demo, review, cost recap, and closing. |

## Acceptance Pattern

Every module follows the same course contract:

1. Decision point and platform boundary are explained first.
2. Learners write or adapt a prompt spec.
3. AI generates implementation or analysis artifacts.
4. Learners verify outputs against explicit acceptance criteria.
5. The class reviews negative examples and adjusts decisions.

## Capstone Rubric

| Dimension | What reviewers look for |
|-----------|--------------------------|
| Working implementation | The agent path runs or the fallback evidence is complete and reproducible. |
| Architecture decision quality | The selected path is justified against alternatives, constraints, and cost. |
| Red-team baseline | ASR is reported, false positives are reviewed, and gate rules are concrete. |
| Production readiness | Monitoring, rollback, cost sampling, and runbook gaps are explicit. |
| AI-pair workflow | Specs, negative examples, and reusable prompts are preserved as team assets. |

