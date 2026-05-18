# Foundry Developer Training 2026

> A 3-day, 11-module Microsoft Foundry workshop for AI-native developers.
> The course is decision-driven, platform-aware, and production-oriented.

This English edition covers the published training output: the learner workshop,
the instructor pack, and the prompt spec library. It is adapted from the Chinese
source materials while keeping the same curriculum structure and acceptance
criteria.

## Positioning

This is not a Foundry API crash course, and it is not a generic AI-pair
programming class.

The course teaches how to reason about Microsoft Foundry as a platform:
capability map, platform boundaries, composition paths, operational tradeoffs,
red-team gates, cost, scaling, and team-level AI-pair workflows.

## Audience

- Python and cloud developers who already use Claude Code, Codex, GitHub
  Copilot, or a similar AI coding assistant in daily work
- Startup engineers, partner SAs, and implementation engineers who need a
  "3-day MVP, production-grade direction" style of training
- Teams that are already adopting, or about to adopt, Microsoft Foundry

Learners do not need their own Azure subscription for the main class path.
Real Azure and Foundry actions are demonstrated by the instructor; learners
complete most checks with mock providers, stubs, sample JSON, and decision cards.

## What Learners Can Do Afterward

1. Decide when to use Agent Service, Agent Framework SDK, or a hybrid path.
2. Run a single-agent and multi-agent path end to end, including tracing and
   a red-team baseline.
3. Explain what Foundry can and cannot do across 14 capability areas.
4. Add provider abstraction, retry, cache, cost estimation, and production
   checklist thinking before launch.
5. Turn AI-pair prompts, negative examples, and decision cards into team assets.

## Site Map

| Section | Purpose |
|---------|---------|
| [Learner Workshop](workshop/) | 3-day learner-facing course map with module goals, prerequisites, tasks, acceptance, and credential assumptions. |
| [Instructor Pack](handbook/) | Course design, instructor preparation, upstream workshop mapping, and Day-7 readiness gates. |
| [Prompt Spec Library](specs/) | Reusable prompt specs and decision cards that learners can feed into AI coding assistants. |

## Course Shape

| Day | Theme | Core outcome |
|-----|-------|--------------|
| Day 1 | Foundry capability map, platform path, provider abstraction, scaling, and cost | Each learner can place their project on the Foundry map and choose a deployment and capacity direction. |
| Day 2 | SDK boundary, A2A, MCP, multi-agent orchestration, and red-team baseline | Each learner understands when to switch paths and how to treat red-team results as a launch gate. |
| Day 3 | Production checklist, capability boundary table, AI-pair workflow, and capstone | Each learner turns course artifacts into a production-oriented project plan and team spec workflow. |

## Scoring Rubric

| Dimension | Weight |
|-----------|--------|
| Working implementation | 25% |
| Architecture decision quality | 25% |
| Red-team baseline and gate design | 20% |
| Production readiness | 15% |
| AI-pair workflow reuse | 15% |

## Human Gating Items

The agent-generated and learner-side materials are ready to use, but a real
instructor still has to validate time-sensitive platform details before delivery:

- 2 weeks before class: confirm MCAPS external subscription availability,
  instructor-side non-Azure provider API key, model access, and TPM capacity.
- 1 week before class: send the learner precheck and run the environment check.
- Day-7: run the fork, capture portal screenshots, validate API drift, prepare
  sample JSON, traces, fallback recordings, and a final capability-boundary table.

## Source Reference

The original Chinese site remains the canonical detailed source for the full
module subtask pages and implementation notes. This English edition keeps the
same structure and links back to those detailed Chinese pages where useful.

