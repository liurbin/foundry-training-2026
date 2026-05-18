# D9: Production Checklist

> Module type: discussion + exercise + review | Duration: 90 min | Credentials: Reading and templates; no real deployment required

## Goals
- Apply a production checklist for incident response, rollback, monitoring, cost sampling, and CI/CD.
- Mark each item as present, partial, or missing.
- Draft at least one concrete runbook scenario.
- Know where a red-team gate belongs in the pipeline.

## Prerequisites
- D3 and D8 outputs are available.

## Subtasks
1. [GH Actions Workflow Walkthrough](01.md) - Read the workflow and mark critical steps.
2. [Red-Team Gate Integration](02.md) - Place D8 red-team checks in PR, pre-deploy, or post-deploy flow.
3. [Incident Review Case Reading](03.md) - Read a sanitized timeline and find where a runbook would help.
4. [Fill the Runbook Template](04.md) - Fill trigger, responder, diagnosis, and rollback steps.
5. [Azure DevOps vs GitHub Actions Differences](05.md) - Choose which pipeline family fits your team.
6. [Apply the Production Checklist](06.md) - Classify all checklist rows and write minimum fixes.

## Acceptance Criteria
- Every checklist row is classified.
- Missing or partial rows have concrete fixes no larger than one week of work.
- At least one incident runbook scenario is filled.
- Learner can answer who responds if an alert fires tonight.

## Credential Notes
Reading and templates; no real deployment required.

## Common Mistakes
- Writing strengthen monitoring as a fix.
- Sending alerts to an unattended mailbox.
- Assuming startups do not need production discipline.

## References
- Training plan v2: ../../handbook/00-training-plan-v2.md
- Instructor handbook v2: ../../handbook/01-instructor-handbook-v2.md
- Prompt spec library: ../../specs/
