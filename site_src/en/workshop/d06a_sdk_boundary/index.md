# D6a: Agent Framework SDK Boundary

> Module type: decision + hands-on | Duration: 60 min | Credentials: Mock provider is enough

## Goals
- Name conditions that force or justify an SDK path.
- Rewrite the D3 agent path with the SDK baseline.
- Compare code size, dependencies, startup mode, operations burden, and state ownership.
- Decide whether the project should stay on Agent Service, move to SDK, or keep a hybrid path.

## Prerequisites
- D2 and D3 are complete.

## Subtasks
1. [Rewrite the D3 Agent with the SDK Path](01.md) - Create a minimal SDK version that runs locally.
2. [Compare Code Size, Dependencies, and Startup Mode](02.md) - Fill a concrete comparison table.
3. [Decision Card and Net Cost Delta](03.md) - Record trigger conditions and operational cost differences.

## Acceptance Criteria
- SDK path runs with a mock provider.
- Comparison table has at least four real rows.
- Cost delta includes runtime, observability, on-call, and state-store costs.

## Credential Notes
Mock provider is enough.

## Common Mistakes
- Switching to SDK because the code looks cleaner.
- Running SDK self-hosted without observability.
- Keeping both paths without a business reason.

## References
- Training plan v2: ../../handbook/00-training-plan-v2.md
- Instructor handbook v2: ../../handbook/01-instructor-handbook-v2.md
- Prompt spec library: ../../specs/
