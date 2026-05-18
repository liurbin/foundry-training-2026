# D6b: A2A + MCP Boundary

> Module type: hands-on | Duration: 60 min + 45 min overlay | Credentials: Local demos and prepared traces; no remote MCP server required

## Goals
- Separate agent-to-agent collaboration from tool/resource protocol design.
- Run or inspect at least one A2A or MCP demo.
- Understand the cost and failure-surface increase when stacking A2A and MCP.
- Recognize a trace that spans agent A, agent B, and an MCP tool.

## Prerequisites
- D6a SDK baseline exists.
- A prepared repo or trace is available for fallback.

## Subtasks
1. [What MCP Is and How It Differs from Tool Calling](01.md) - Distinguish protocol boundary from in-process tool schemas.
2. [Add an MCP Tool to the A2A Chain](02.md) - Attach a real local file, HTTP, or calculation tool.
3. [Trace Review: A to B to MCP Tool](03.md) - Identify the three hops in trace evidence.
4. [A2A vs MCP Decision Card and Cost Estimate](04.md) - Decide whether the capstone should use A2A, MCP, both, or neither.

## Acceptance Criteria
- At least one of A2A or MCP runs locally, or a prepared trace is reviewed.
- Decision card includes token and latency impact.
- In-process function calls are not presented as A2A.

## Credential Notes
Local demos and prepared traces; no remote MCP server required.

## Common Mistakes
- Wrapping a local function as MCP only to add operational burden.
- Using echo-only MCP tools.
- Ignoring doubled token cost and doubled failure surface.

## References
- Training plan v2: ../../handbook/00-training-plan-v2.md
- Instructor handbook v2: ../../handbook/01-instructor-handbook-v2.md
- Prompt spec library: ../../specs/
