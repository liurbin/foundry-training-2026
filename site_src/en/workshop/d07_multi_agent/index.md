# D7: Three-Way Multi-Agent Orchestration Choice

> Module type: hands-on + decision | Duration: 120 min | Credentials: Foundry endpoint or instructor/shared/mock fallback for the main path

## Goals
- Compare Agent Service native orchestration, as_tool, and Workflows.
- Run or inspect orchestrator to expert-agent traces.
- Understand where control flow, testability, and state ownership live.
- Reject the deprecated hand-written HandoffService pattern.

## Prerequisites
- D3 is complete.
- D6a and D6b boundaries are understood.

## Subtasks
1. [Main Path: Native Agent Service Orchestration](01.md) - Build or inspect orchestrator plus two specialist agents.
2. [Comparison Path A: as_tool](02.md) - Apply or inspect the prepared diff and compare control-flow ownership.
3. [Comparison Path B: Workflows Recording](03.md) - Watch the visual designer recording and note one fit and one non-fit case.
4. [Three-Path Orchestration Decision](04.md) - Choose the path and explain why the other two are not selected.

## Acceptance Criteria
- Main path trace or fallback evidence shows orchestrator to expert calls.
- as_tool and Workflows differences can be explained orally.
- Decision card answers all three path questions.

## Credential Notes
Foundry endpoint or instructor/shared/mock fallback for the main path.

## Common Mistakes
- Rebuilding a hand-written state machine when native orchestration is sufficient.
- Choosing Workflows for simple 80 percent orchestration.
- Treating multi-agent as automatically requiring A2A.

## References
- Training plan v2: ../../handbook/00-training-plan-v2.md
- Instructor handbook v2: ../../handbook/01-instructor-handbook-v2.md
- Prompt spec library: ../../specs/
