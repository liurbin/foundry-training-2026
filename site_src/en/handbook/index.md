# Instructor Pack

> The instructor pack turns the course plan into a delivery checklist.

This section summarizes the English instructor-facing output. The detailed
Chinese source pages remain available under the original Instructor Pack
navigation.

## Course Design Contract

The course is derived from five design principles:

| Principle | Instructor implication |
|-----------|------------------------|
| Teach decisions, not APIs | API syntax belongs to AI assistants and docs. Class time is for platform choices and boundaries. |
| Prioritize what AI does not know | Rebrand-period API drift, workshop bugs, portal behavior, cost limits, and business constraints are the instructor's value. |
| Every module delivers a prompt spec | Learners should leave with reusable specs, not just throwaway code. |
| Negative examples must be explicit | The class must name the mistakes AI is likely to generate and show how to detect them. |
| Red-team, portability, scaling, and cost are required | These topics are scored, not treated as optional production polish. |

## Instructor Responsibilities

| Area | Must be ready before class |
|------|----------------------------|
| Platform path | Real or recorded Foundry project setup, model deployment, agent invocation, and trace evidence. |
| API drift | Current package versions, renamed fields, broken examples, and current portal paths. |
| Provider abstraction | One non-Azure provider key for instructor-only live switch or a fallback recording. |
| Scaling and cost | 429 stub, replay response, cost tiers, and capacity-mode explanation. |
| Red-team | Portal demonstration, SDK sample JSON, ASR interpretation, and false-positive examples. |
| Production | Runbook template, incident review sample, CI/CD gate placement, and rollback discussion. |
| Boundary table | 14 capability rows with official documentation, portal screenshot, or fork-tested evidence. |

## Day-7 Readiness Gates

Day-7 means seven calendar days before training delivery. The instructor must
finish these checks or explicitly prepare a fallback.

| Gate | Required evidence |
|------|-------------------|
| Fork run-through | Terminal logs, failed item notes, and any required local patches. |
| API drift validation | Current status of known drift points, including response format and token provider patterns. |
| Portal path validation | Screenshots for Models, Agents, Monitoring, Evaluations, and relevant settings. |
| Workflow samples | At least two runnable samples or recordings with trace evidence. |
| Rubric | A one-page 5-dimension scoring rubric used by instructor, assistants, and learners. |
| Spec library | 12 prompt spec files available in `prep-artifacts/day-7/specs/`. |

## Upstream Workshop Mapping

The course adapts `microsoft/TechWorkshop-L300-AI-Apps-and-agents`, but the
v2 course is not a linear translation of that workshop.

| v2 module group | Relationship to upstream |
|-----------------|--------------------------|
| D3 and D8 | Mostly reused: Bicep, single-agent path, tracing, UI/SDK red-team concepts. |
| D6a, D6b, D7, D9 | Partly reused: SDK, A2A, multi-agent, and GitHub Actions ideas need new decision framing. |
| D1, D2, D4, D5, D10, D11 | New: decision framework, provider abstraction, scaling/cost, boundary table, and team spec workflow. |

## Human Prerequisites

These items cannot be completed by the agent or by static course material alone.

| Timing | Human prerequisite |
|--------|--------------------|
| 2 weeks before class | Confirm external subscription availability, instructor non-Azure provider key, model access, and TPM capacity. |
| 1 week before class | Send learner precheck and run environment self-check. |
| Day-7 | Run the fork, capture evidence, decide fallback recordings, and validate platform drift. |
| Delivery day | Keep keys private, use instructor-side demos for real cloud actions, and provide sanitized artifacts to assistants. |

## Maintenance Rules

- If a design principle changes, update the course plan first, then instructor
  handbook, module pages, prompt specs, and acceptance criteria.
- If upstream changes, update the mapping table and only then adjust affected
  modules.
- If Foundry portal or SDK behavior drifts after Day-7, update the prepared
  evidence and explain the drift during class; do not silently change the
  course contract.
