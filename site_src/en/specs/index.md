# Prompt Spec Library

> Reusable specs and decision cards for AI-pair development.

The prompt spec library is the main reusable output of the course. Learners use
these files to ask AI assistants for implementation, analysis, or review, while
still preserving human ownership of platform decisions.

## Spec Principles

Every spec should include:

- A clear task and project context
- Current SDK, portal, and platform assumptions
- Inputs and expected outputs
- Constraints the AI must obey
- Negative examples the AI is likely to get wrong
- Concrete self-verification steps

## Library Index

| Spec | Use it when | Output |
|------|-------------|--------|
| [D1 Foundry Fit](spec-d1-foundry-fit.md) | Deciding whether to use Foundry for a project | Foundry fit decision card. |
| [D2 Service vs SDK](spec-d2-service-vs-sdk.md) | Choosing Agent Service, SDK, or hybrid | Scored platform decision with hard constraints and cost inputs. |
| [D3 Single Agent](spec-d3-single-agent.md) | Deploying and invoking one Foundry agent | Bicep, deployment script, `agent_reference` code, and trace link. |
| [D4 Provider Abstraction](spec-d4-provider-abstraction.md) | Decoupling business code from provider SDKs | `ChatProvider`, provider implementations, switch config, and tests. |
| [D5 Scaling and Cost](spec-d5-scaling-cost.md) | Adding retry, cache, cost estimation, and capacity reasoning | Deployment and capacity note plus runtime safeguards. |
| [D6a SDK Boundary](spec-d6a-sdk-boundary.md) | Testing whether the project should switch to SDK | SDK rewrite, comparison table, and switch decision card. |
| [D6b A2A + MCP](spec-d6b-a2a-mcp.md) | Separating agent-to-agent and tool protocol choices | A2A/MCP demos, decision card, token and latency estimate. |
| [D7 Multi-Agent](spec-d7-multi-agent.md) | Choosing a multi-agent orchestration path | Native orchestration output, trace evidence, and three-way decision card. |
| [D8 Red-Team Gate](spec-d8-redteam-gate.md) | Creating a launch gate from red-team results | ASR report, attack categories, failed-case review, and gate rules. |
| [D9 Production Checklist](spec-d9-prod-checklist.md) | Applying production readiness checks | Checklist status, minimum fixes, and launch gap list. |
| [D10 Foundry Limits](spec-d10-foundry-limits.md) | Mapping project needs to Foundry boundaries | Boundary hits and migration options. |
| [D11 AI-Pair Team](spec-d11-ai-pair-team.md) | Turning specs into a team workflow | Team spec repository structure and two starter spec outlines. |

## English Decision Card Templates

### D1: Foundry Fit

Use Foundry when the project needs managed agent runtime, state, Azure identity,
Key Vault, App Insights, compliance alignment, or a portal-based operations
surface.

Do not use Foundry when the project only needs one-off LLM calls, depends on a
model outside the Azure catalog with no plan to switch, is a disposable demo, or
already has a mature LangGraph or CrewAI production stack with no migration
reason.

Required conclusion: `use`, `do not use`, or `partially use`.

### D2: Agent Service vs SDK

Score four dimensions from 1 to 5:

| Dimension | Direction |
|-----------|-----------|
| Managed runtime | Favors Agent Service. |
| Portal visibility | Favors Agent Service. |
| Full code control | Favors SDK. |
| Cross-provider portability | Favors SDK. |

Hard constraints override the score when they apply: private deployment,
network isolation, minimum operations staffing, stable high-throughput SLA, or
strict budget requirements.

### D5: Deployment and Capacity

Deployment target:

- Foundry Hosted Agents: default path.
- Container Apps self-hosting: only when self-hosting, VNet, or customer-private
  Azure requirements dominate.
- SDK self-hosting: for cross-cloud, customer-owned Kubernetes, or truly private
  deployments.

Capacity mode:

- PAYG + default quota: default for unpredictable traffic and most early stages.
- Quota increase: growing traffic without commitment.
- PTU / provisioned throughput: stable high-throughput SLA.
- Reservation: long-term stable usage and price locking.

### D8: Red-Team Gate

A valid red-team baseline must include:

- ASR as a concrete number
- Attack categories
- Top failed cases reviewed manually
- False-positive analysis
- Three CI/CD gate rules with thresholds

## Team Spec Repository Starter

```text
team-specs/
|-- README.md
|-- decision-cards/
|-- implementation/
|-- negative-examples/
`-- runbooks/
```

Review rule: every incident, failed AI output, or platform drift should either
update a spec, add a negative example, or create a runbook entry.
