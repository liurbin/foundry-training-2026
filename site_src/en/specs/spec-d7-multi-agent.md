# D7 Multi-Agent

## Goal
Run native multi-agent orchestration and compare as_tool and Workflows.

## Inputs
- Project context and current stage.
- Relevant outputs from earlier modules.
- Current platform assumptions, SDK versions, portal evidence, or instructor-provided fallback artifacts.

## Ask AI to Produce
- Trace and three-way orchestration card.
- A short explanation of decisions and rejected alternatives.
- Verification steps that can be run or reviewed during class.

## Constraints
- Do not hardcode secrets, endpoints, regions, model deployment names, or private keys.
- Do not invent platform capabilities that were not verified by documentation, portal screenshots, or fork tests.
- Keep abstractions minimal and aligned with the module goal.
- Explicitly name uncertainty instead of hiding it.

## Self-Verification
- [ ] The output is concrete enough for instructor review.
- [ ] Rejected alternatives are documented.
- [ ] Operational, cost, security, and boundary assumptions are visible.
- [ ] The artifact can be reused in the capstone or team spec library.
