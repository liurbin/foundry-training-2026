# D4: Provider Abstraction

> Module type: hands-on + instructor demo | Duration: 90 min | Credentials: Learners use mock only; instructor uses one non-Azure provider key for the demo

## Goals
- Define a minimal ChatProvider interface.
- Run business logic through MockProvider without Azure credentials.
- Keep provider-specific concepts out of business code.
- Observe a Foundry to non-Azure provider switch and record behavioral differences.

## Prerequisites
- D3 single-agent path is available as the baseline to decouple.
- Basic Python Protocol or typed interface knowledge.

## Subtasks
1. [Provider Interface Design](01.md) - Design Message, ChatResponse, and ChatProvider with only shared fields.
2. [MockProvider Implementation and Business-Code Refactor](02.md) - Move business logic behind the provider interface and verify mock execution.
3. [Watch the Foundry to Non-Azure Provider Live Switch](03.md) - Observe the instructor switch and record differences in response, errors, quotas, or tool semantics.

## Acceptance Criteria
- Business code does not import Azure or OpenAI SDKs directly outside provider implementations.
- MockProvider runs offline.
- Adding a third provider only requires a new provider file and a simple config branch.

## Credential Notes
Learners use mock only; instructor uses one non-Azure provider key for the demo.

## Common Mistakes
- Leaking provider-specific thread IDs or tool-choice fields into the common interface.
- Building factory-of-factory abstractions for a two-provider exercise.
- Giving learners private provider keys.

## References
- Training plan v2: ../../handbook/00-training-plan-v2.md
- Instructor handbook v2: ../../handbook/01-instructor-handbook-v2.md
- Prompt spec library: ../../specs/
