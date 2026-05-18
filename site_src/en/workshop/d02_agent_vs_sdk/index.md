# D2: Agent Service vs SDK Selection

> Module type: decision | Duration: 90 min | Credentials: None

## Goals
- Explain the boundary between Agent Service, Agent Framework SDK, and Workflows.
- Score managed runtime, portal visibility, code control, and provider portability.
- Use hard constraints such as private deployment, network isolation, operations staffing, throughput, and budget.
- Carry concrete traffic and cost inputs into D5 capacity planning.

## Prerequisites
- D1 decision card is complete.

## Subtasks
1. [Architecture Overview and Capability Boundaries](01.md) - Map runtime ownership, state ownership, portal visibility, and code control.
2. [Four-Dimension Scoring and Decision Rules](02.md) - Score the project and check hard constraints.
3. [Cost Estimation and Hybrid Path](03.md) - Estimate monthly order of magnitude and decide whether a hybrid path is justified.

## Acceptance Criteria
- All four dimensions are scored.
- All hard-constraint rows are marked hit or not hit.
- Cost inputs include request volume, token size, peak QPS, on-call expectation, and runtime shape if SDK is selected.
- Any decision that contradicts the heuristic includes a written reason.

## Credential Notes
None.

## Common Mistakes
- Defaulting to SDK just because it is more flexible.
- Assuming managed service is always more expensive without counting self-hosting and on-call.
- Treating capacity decisions as afterthoughts instead of architecture inputs.

## References
- Training plan v2: ../../handbook/00-training-plan-v2.md
- Instructor handbook v2: ../../handbook/01-instructor-handbook-v2.md
- Prompt spec library: ../../specs/
