# Training Plan v2: AI-Native Developer Edition

## Positioning
This is a 3-day Microsoft Foundry course for AI-native developers. It is not an API walkthrough and it is not a generic AI-pair programming class. The instructor teaches Foundry capability boundaries, platform choices, composition paths, red-team gates, cost, scaling, and production tradeoffs.

## Learner Profile
Learners already use AI coding assistants in daily work. They care about shipping a demonstrable MVP quickly while still reasoning about production concerns from day one.

## Design Principles
- Teach decisions, not API field lists.
- Prioritize current platform facts that AI assistants may not know.
- Make every module produce a reusable prompt spec or decision card.
- Name negative examples explicitly.
- Treat portability, scaling, cost, and red-team as required course material.

## Agenda
| Day | Modules | Main outcome |
|-----|---------|--------------|
| Day 1 | D1-D5 | Foundry fit, Service vs SDK, single-agent path, provider abstraction, deployment and capacity decision. |
| Day 2 | D6a-D8 | SDK boundary, A2A/MCP boundary, multi-agent orchestration, red-team baseline. |
| Day 3 | D9-D11 plus capstone | Production checklist, capability boundary table, team AI-pair workflow, capstone demo. |

## Capability Map
The course uses 14 Foundry capability domains: Agent Service, Workflows, Projects, Connections, Identity, Models, Evaluations/Red Team, Tracing/Monitoring, Deployment, Quotas, Capacity, SDK/Agent Framework, A2A, and MCP.

## Capstone Rubric
| Dimension | Weight |
|-----------|--------|
| Working implementation | 25% |
| Architecture decision quality | 25% |
| Red-team baseline | 20% |
| Production readiness | 15% |
| AI-pair workflow reuse | 15% |

## Human Gating Items
Instructor-side Azure subscription, model access, TPM capacity, provider key for D4, portal screenshots, validated traces, sample JSON, and Day-7 evidence are human prerequisites and cannot be invented by the course material.
