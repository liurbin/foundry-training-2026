# D5: Deployment, Capacity, Scaling, and Cost

> Module type: hands-on + instructor demo | Duration: 90 min | Credentials: Learners use stubs and replay responses; instructor owns real load tests

## Goals
- Choose one deployment target and one capacity mode.
- Implement 429 and 5xx retry with bounded exponential backoff and jitter.
- Design a safe prompt and model cache key.
- Estimate monthly cost for 1k, 10k, and 100k DAU bands.
- Observe the instructor load-test recording or demo.

## Prerequisites
- D2 cost inputs exist.
- D3 call path or mock provider is available.

## Subtasks
1. [Deployment and Capacity Mode Comparison](00.md) - Pick Hosted Agents, Container Apps self-hosting, or SDK self-hosting; pick PAYG, quota increase, PTU, or reservation.
2. [429 Retry with Jitter](01.md) - Use a stub to prove retry and jitter behavior.
3. [Cache Strategy and Pitfalls](02.md) - Define a cache key, TTL, and privacy exclusions.
4. [Three-Tier Cost Estimation and Capacity Planning](03.md) - Estimate best and worst monthly costs for three scale bands.
5. [Load-Test Walkthrough](04.md) - Watch 100 RPS by 5 min evidence and record retry and cache observations.

## Acceptance Criteria
- Deployment and capacity decision note is complete, including why alternatives were rejected.
- Retry is implemented at provider/client level, not business level.
- Cache key excludes user IDs and personal data.
- Cost estimate includes assumptions and capacity mode per scale band.

## Credential Notes
Learners use stubs and replay responses; instructor owns real load tests.

## Common Mistakes
- Choosing PTU without current stable high-throughput SLA.
- Using user_id in a cache key.
- Running learner-side real load tests against shared quota.

## References
- Training plan v2: ../../handbook/00-training-plan-v2.md
- Instructor handbook v2: ../../handbook/01-instructor-handbook-v2.md
- Prompt spec library: ../../specs/
