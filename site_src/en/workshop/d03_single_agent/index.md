# D3: Single-Agent Platform Path

> Module type: hands-on + review | Duration: 120 min | Credentials: Azure subscription and Foundry project for real deployment; mock or instructor endpoint for fallback

## Goals
- Deploy or understand a minimal Foundry agent resource path.
- Invoke the agent externally through an agent reference.
- Observe or review a trace for one successful invocation.
- Know which region and model deployment settings must be parameterized.

## Prerequisites
- D1 and D2 are complete.
- Python or the learner-selected SDK runtime is available.
- Instructor confirms the tracing setup or provides fallback evidence.

## Subtasks
1. [Bicep Resource Deployment](01.md) - Generate, review, and optionally run modular Bicep for agent resources.
2. [Run a Single Agent](02.md) - Call the deployed or mocked agent once and capture logs.
3. [Enable and Verify Tracing](03.md) - Check trace evidence and record what was observed.

## Acceptance Criteria
- Bicep is modular and parameterized.
- No secret, endpoint, or deployment name is hardcoded.
- A successful invocation returns non-empty text or a fallback mock proves the call path.
- Trace observation is recorded when tracing is enabled.

## Credential Notes
Azure subscription and Foundry project for real deployment; mock or instructor endpoint for fallback.

## Common Mistakes
- Deploying AI-generated Bicep without reading the diff.
- Hardcoding model deployment names or secrets.
- Writing retry logic in this step instead of leaving retry strategy for D5.

## References
- Training plan v2: ../../handbook/00-training-plan-v2.md
- Instructor handbook v2: ../../handbook/01-instructor-handbook-v2.md
- Prompt spec library: ../../specs/
