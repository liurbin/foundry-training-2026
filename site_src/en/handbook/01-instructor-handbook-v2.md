# Instructor Handbook v2

## Delivery Contract
Each module follows the same classroom shape: decision point, AI blind spots, prompt spec, learner AI-pair work, verification, and review. The instructor must keep the class on platform judgment rather than API typing.

## Module Responsibilities
| Module | Instructor focus | Learner artifact |
|--------|------------------|------------------|
| D1 | Foundry fit and wrong-use cases | Foundry fit decision card |
| D2 | Service, SDK, Workflows, hard constraints | Service vs SDK decision card |
| D3 | Minimal platform path and trace evidence | Single-agent call and trace notes |
| D4 | Provider abstraction and live switch | ChatProvider plus MockProvider |
| D5 | Hosted Agents, capacity, retry, cache, cost | Deployment/capacity note and cost table |
| D6a | When SDK is justified | SDK comparison and switch decision |
| D6b | A2A vs MCP boundary | A2A/MCP decision card |
| D7 | Multi-agent orchestration options | Three-way orchestration card |
| D8 | Red-team as launch gate | ASR report and gate rules |
| D9 | Production readiness | Checklist and runbook |
| D10 | Capability boundaries | Boundary hits and migration options |
| D11 | Team AI-pair workflow | Spec library structure |

## Instructor Preparation
Prepare current SDK/package versions, API drift notes, portal paths, screenshots, traces, recordings, sample JSON, and fallback repos. Any live cloud action must have a recorded or sample-data fallback.

## Review Rules
Review decisions before code volume. Require concrete reasons, explicit rejected alternatives, and written uncertainty. Do not accept generic fixes such as improve monitoring or consider another platform.

## Negative Example Policy
Every module must expose common AI failure modes. Learners should compare AI output against these negative examples before treating it as usable.
