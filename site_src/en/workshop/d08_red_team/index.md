# D8: Red-Team Baseline

> Module type: hands-on + review | Duration: 105 min | Credentials: Instructor portal demo; learner SDK run or sample JSON fallback

## Goals
- Run or inspect one red-team baseline.
- Read ASR as a launch-gate metric.
- Identify at least one false-positive pattern.
- Create CI/CD gate rules based on red-team evidence.

## Prerequisites
- A target agent exists from D3, D6a, or D6b.
- The learner defines a business-acceptable ASR threshold below 100 percent.

## Subtasks
1. [Watch the Portal Red-Team Baseline](01.md) - Observe the instructor run and result UI.
2. [Run One SDK Red-Team Scan](02.md) - Run the cloud red-team path or prepare the command and config.
3. [Fallback When the SDK Run Times Out](03.md) - Use sample JSON to complete the report structure.
4. [Result Analysis and False-Positive Review](04.md) - Classify attacks, inspect top failures, and decide fix / do not fix / prompt mitigation.

## Acceptance Criteria
- Baseline report contains a numeric ASR.
- At least two or three attack categories are covered, or gaps are documented.
- Top failed cases receive manual review.
- Three gate rules have thresholds.

## Credential Notes
Instructor portal demo; learner SDK run or sample JSON fallback.

## Common Mistakes
- Treating red-team as a checkbox.
- Accepting tool judgments without manual review.
- Blocking class progress when a long SDK run times out.

## References
- Training plan v2: ../../handbook/00-training-plan-v2.md
- Instructor handbook v2: ../../handbook/01-instructor-handbook-v2.md
- Prompt spec library: ../../specs/
