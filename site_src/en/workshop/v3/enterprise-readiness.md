# Enterprise Readiness: 12 go-live boundaries

> This page is a v3 go-live boundary cheat sheet, not a hands-on procedure. The 4h class only covers the judgment framework; real projects must re-verify against the actual subscription, region, model, network, and compliance requirements at Day-7 or during customer discovery.

## Why this gets its own section

Getting the Customer Operations Agent to run only proves the pattern holds. When startups / partners actually deliver, customers don't only ask "does it run"; they audit against 12 categories of questions:

| Category | What customers will ask | Deliverable |
|---|---|---|
| 1. Tenant / subscription / project governance | How are resource ownership, naming, environments, and permission boundaries managed? | Subscription / RG / project topology |
| 2. Identity / RBAC / secrets | What identity do humans, apps, agents, and tools each use? | RBAC matrix + Key Vault policy |
| 3. Network security | Can calls and tool access go over private networking? | Private endpoint / outbound design |
| 4. Data governance / privacy / encryption | What data sits in prompts, files, traces, logs? | Data classification + retention + CMK policy |
| 5. Deployment topology / capacity | How to choose Global, Data Zone, Regional, PTU? | Deployment type + region + capacity plan |
| 6. Model access / quota / lifecycle | Which models are usable, is quota sufficient, how are model upgrades controlled? | Model access + TPM/RPM + fallback plan |
| 7. Safety controls | Can content filter, Prompt Shields, abuse monitoring be modified? | Filter / abuse monitoring decision record |
| 8. Tool / action security | Will the agent overstep or misoperate when calling business systems? | Tool allowlist + human approval rules |
| 9. Evaluation / red team / release gate | How do we prove a change did not regress? | Eval dataset + thresholds + CI gate |
| 10. Observability / logging / SIEM | Where do logs go? Can prompts enter logs? | App Insights / Log Analytics / SIEM routing |
| 11. Reliability / DR / graceful degradation | What happens when the platform or region has issues? | RTO/RPO + fallback runbook |
| 12. FinOps / operations ownership | Who owns cost, alerts, oncall, rollback? | Budget + alerts + runbook + owner |

Not all 12 need hands-on within 4h, but a builder must know they exist, otherwise the in-class demo cannot migrate into an enterprise environment.

## 1. Tenant / Subscription / Project Governance

Set resource boundaries first, then write code.

| Decision | Questions to ask |
|---|---|
| Tenant | Customer tenant or partner tenant? Who owns cross-tenant invitations? |
| Subscription | Are POC, staging, prod separate subscriptions? Is quota on the target subscription? |
| Resource group | Are network, Foundry project, App Insights, Key Vault in the same RG? |
| Project | Are dev / staging / prod three projects, or one project with multiple deployments? |
| Naming / tagging | How are cost, environment, owner, data class tagged? |

Recommendation: prod should not share dev agent versions; a partner demo subscription cannot directly become a customer production subscription.

Official entry: [RBAC for Foundry hubs and projects](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/hub-rbac-azure-ai-foundry).

## 2. Identity / RBAC / Secrets

Using `DefaultAzureCredential` in v3 is correct, but go-live also requires splitting identities cleanly:

| Principal | Minimum requirement |
|---|---|
| Human builder | Azure AI Developer / User minimum role, not Owner as daily permission |
| CI/CD | Federated credential or managed identity, no long-lived secrets |
| App runtime | Managed identity to call Foundry, Key Vault, tool backend |
| Tool backend | Its own scope; do not reuse the Foundry project identity for everything |
| Secrets | Managed in Key Vault, never in repo, prompt, trace, or tool output |

Judgment rules:

- If Entra ID / managed identity works, do not issue an API key.
- `DefaultAzureCredential` is only the client-side way to get a token; it does not equal a finished permission design.
- When a tool calls a business system, use that business system's own authorization boundary; do not treat the agent as a superuser.

Official entry: [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview), [Managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview).

## 3. Network Security

The in-class v3 defaults to public endpoint for the sake of running through in 4h. Enterprise projects must split inbound / outbound:

| Layer | Questions to ask | Foundry / Azure path |
|---|---|---|
| Inbound | Where do users, apps, CI access the project endpoint from? | Private Endpoint / Private Link, disable public network access, enterprise DNS, VPN / ExpressRoute |
| Outbound | Where does the agent go when calling tool / storage / search / database? | Managed virtual network / approved outbound, private endpoints, allowlists |

Judgment rules:

- For customer data, PII, regulated data: prefer designing private endpoints + disabling public access.
- If the agent must reach internal enterprise APIs: confirm outbound rules and private-network path first; do not bolt it on after code is written.
- The in-class environment only validates the public path; do not treat it as a production network template.

Official entry: [Configure a private link](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/configure-private-link), [Configure managed networks](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/configure-managed-network).

## 4. Data Governance / Privacy / Encryption

In an agent project, data does not only live in prompts. List at least 6 categories:

| Data | Where it may appear | Boundaries to define |
|---|---|---|
| User input | Prompt, trace, eval dataset | Whether it contains PII; whether sampling is allowed |
| Model output | Response, trace, logs | Whether it can enter logs; whether to redact |
| Files / knowledge | Upload, knowledge store, search index | Retention, ACL, Purview / DLP |
| Tool input/output | Function args, tool response | Minimal fields, no secrets, redaction |
| Evaluation data | JSONL, report, judge reasoning | Whether offline export is allowed; who can view |
| Operational logs | App Insights, Log Analytics, SIEM | Retention, region, RBAC |

For encryption, ask:

- Are customer-managed keys (CMK) required?
- Does the Key Vault firewall / private endpoint affect service access?
- System-assigned or user-assigned managed identity?

Official entry: [CMK for Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/encryption-keys-portal), [Data, privacy, and security](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy).

## 5. Deployment Topology / Capacity

Deployment type decides three things: where requests are processed, how throughput and latency are guaranteed, and how cost and quota are computed.

| Mode | Good for | Key boundaries |
|---|---|---|
| **Global Standard** | General online traffic, wanting more elasticity | Requests may be processed by global infrastructure; confirm the customer's data-processing requirements |
| **Data Zone Standard** | Constrained to EU / US or similar data zones | Stronger regional boundary than Global, but not a single region |
| **Regional Standard** | Explicit single-region processing requirement, low-risk POC | Capacity and model availability are more visibly affected by region |
| **Batch** | Offline evaluation, batch processing, low-cost non-realtime tasks | Not an online agent path; must accept async completion windows |
| **Provisioned / PTU** | Stable high throughput, predictable latency, enterprise production traffic | Requires PTU quota / reservation; region and model capacity may be sold out |

Do not present the in-class sample as a "deployment recommendation". It is only the minimum public + shared capacity path. A real customer must first answer:

- Are there data residency requirements?
- What is the peak QPS / TPM?
- Is there a latency SLO?
- Are they willing to pay PTU cost for reserved throughput?

Official entry: [Deployment types](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/deployment-types), [Provisioned throughput](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/provisioned-throughput).

## 6. Model Access / Quota / Lifecycle

Do not equate "can see the model" with "can use the model in production". Verify at least four layers:

| Layer | What to verify |
|---|---|
| Model availability | Whether the target model supports the target region / deployment type |
| Subscription and tier | Enterprise / MCA-E / default / student subscriptions have different default quotas |
| Quota dimension | Usually TPM / RPM managed by subscription + region + model / deployment type |
| PTU capacity | PTU quota and actual capacity are two different things; large customers must lock capacity ahead of time |
| Model lifecycle | How model upgrade, retirement, fallback model, eval regression are handled |

Instructor Day-7 must give learners explicit values: `MODEL_DEPLOYMENT_NAME`, deployment type, region/data zone, TPM/RPM, whether PTU.

Official entry: [Quotas and limits](https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits), [Model availability](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models).

## 7. Safety Controls: Content Filter / Prompt Shields / Abuse Monitoring

State the defaults clearly: these are not ordinary toggles.

| Item | Default / boundary |
|---|---|
| Content filtering | Enabled by default; categories and thresholds are configurable. Turning filtering off or moving to annotate-only typically requires applying for modified content filtering. |
| Prompt Shields | Generic prompt injection / document attack risk can be handled at the platform layer; business-scope overreach still relies on instructions, eval, output filter, tool approval. |
| Protected material | Copyright-material risk should be enabled / evaluated based on customer scenario. |
| Abuse monitoring | Automatic abuse detection by default; for some customers this may involve content sampling / human review. |
| Modified abuse monitoring | Not a casual portal toggle; typically only available to eligible managed customers / partners, approved through a Microsoft process. |

Classroom phrasing:

- "Content filter blocks generic safety categories; it does not block 'no refunds allowed' business rules."
- "Turning off / downgrading safety monitoring is not an engineering optimization, it is a compliance approval."
- "If the customer requires no prompt storage / no human review, run the eligibility and approval first, then design the logging policy."

Official entry: [Content filtering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter), [Prompt Shields](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields), [Limited access features](https://learn.microsoft.com/en-us/azure/ai-services/cognitive-services-limited-access).

## 8. Tool / Action Security

In 2026, agent risk is usually not "will it chat" but "will it call the wrong tool".

| Action type | Examples | Default policy |
|---|---|---|
| Query | Look up an order, ticket, inventory | Can be automated, but require argument validation and minimum return fields |
| Recommend | Suggest a refund, escalation, next step | Can be automated, but mark explicitly that it is not the final action |
| Mutate | Refund, change address, issue coupon, close alert, modify permissions | Default human approval / second confirmation / idempotency key |

Must do:

- Treat tool arguments and tool output as untrusted input.
- Do not return secrets, tokens, or connection strings in tool output.
- Every tool must have a scope, rate limit, audit log.
- Evaluation must cover tool misuse: wrong order, out-of-scope refund, prompt injection triggering a tool.

Official entry: [Function calling security considerations](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/function-calling?azure-portal=true).

## 9. Evaluation / Red Team / Release Gate

The 4 starter evaluations in class only prove the minimum closed loop. Go-live requires at least 5 categories:

| Category | Examples |
|---|---|
| Functional | Happy path, edge case, tool call success |
| Grounding | Whether the correct data is referenced, whether hallucinations occur |
| Safety | Harmful content, protected material, jailbreak |
| Business policy | No refund promises, no PII leakage, no out-of-scope action |
| Regression | Whether changes to prompt, model, tool, filter cause regression |

Production recommendations:

- Run an eval gate on every prompt / instructions / model deployment / tool schema change.
- After go-live, use continuous evaluation to monitor a sampled portion of traffic.
- Red team scan is not a one-time sign-off; rerun before significant releases.

Official entry: [Agent Monitoring Dashboard](https://learn.microsoft.com/en-us/azure/ai-foundry/observability/how-to/how-to-monitor-agents-dashboard?view=foundry), [Risk and safety evaluators](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/risk-safety-evaluators).

## 10. Observability / Logging / SIEM

In v3 hands-on 0 you look at portal trace. Real delivery must integrate with the customer's logging system:

| Target | Minimum approach | Productionization add-on |
|---|---|---|
| Agent trace | Connect Application Insights, view span / token / latency in the Foundry portal | Use Azure Monitor / Log Analytics to manage retention, RBAC, queries |
| Application logs | Structured logs on the SDK call side: request id, agent version, case id, latency, error type | Do not log full prompts, or redact / sample |
| External observability | OpenTelemetry / OTLP exporter | Wire into Datadog, Grafana, Jaeger, Honeycomb, and other existing systems |
| Security audit | Azure Monitor diagnostic settings / Event Hub routing | Into SIEM, retain access, quota, anomaly, policy events |

Suggested classroom phrasing:

- "Trace proves you can debug; Log Analytics / SIEM integration proves you can operate."
- "Whether prompts and outputs can enter logs is a customer compliance question, not an engineering default."

Official entry: [Agent tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept), [Set up tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup), [OpenTelemetry tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agents-sdk).

## 11. Reliability / DR / Graceful Degradation

Agent Service is a stateful system; you cannot recover by "redeploy the code once".

Ask:

- What is RTO / RPO?
- Who backs up agent definitions, threads, files, knowledge, tool connections?
- On a region outage, do you switch region, degrade to humans, or return read-only?
- Do the dependent Cosmos DB, Azure AI Search, Storage, App Insights also have recovery strategies?

Minimum:

- IaC retains project-dependent resources and app config.
- Agent instructions / eval dataset / tool schema live in git.
- Runbook clearly describes how to degrade when: model unavailable, quota burst, trace broken, tool backend down, region outage.

Official entry: [Foundry Agent Service disaster recovery](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/disaster-recovery), [Azure reliability guidance](https://learn.microsoft.com/en-us/azure/reliability/overview).

## 12. FinOps / Operations Ownership

The last item is not technical, it is who operates it.

| Item | What to define |
|---|---|
| Cost | Token, PTU, Application Insights ingest, storage, tool backend cost |
| Budget | Daily budget, monthly budget, anomalous-growth alert |
| Owner | Product owner, engineering owner, security owner, oncall |
| Runbook | 429, 5xx, wrong reply, out-of-scope promise, data leak, cost anomaly |
| Versioning | Agent version, model deployment, tool schema, eval dataset recorded together |
| Rollback | Roll back to which agent version / model / filter policy |

Recommendation: tag even during the demo phase, otherwise the partner soon loses track of which customer, which POC, which environment is spending money.

## How to cover it in class

- S1 Operate: touch on governance, network, quota, policy, cost; do not go into hands-on.
- S2 wrap: use this page as an extension of the go-live checklist; do not add hands-on time.
- Day-7: the instructor must use a real subscription to fill in deployment type, region, quota, filter, logging, network, RBAC, DR with screenshots or configuration evidence.

## Day-7 must-fill checklist

- [ ] Tenant / subscription / RG / project topology defined
- [ ] RBAC matrix: human, CI, runtime, tool identity defined
- [ ] Project endpoint: public or private endpoint?
- [ ] Outbound: does the agent/tool need to access private APIs? What is the path?
- [ ] Data: do prompt, trace, eval, tool output contain PII? Retention how long?
- [ ] Encryption: is CMK required? Key Vault / managed identity configured?
- [ ] Logging: Application Insights / Log Analytics / SIEM wired up? Prompts redacted?
- [ ] Deployment: Global / Data Zone / Regional / PTU which one? Why?
- [ ] Quota: target model, region, TPM/RPM, PTU quota sufficient?
- [ ] Content filter: default, custom, or modified content filtering?
- [ ] Abuse monitoring: default, or modified abuse monitoring approved?
- [ ] Tool action: query / recommend / mutate classification and human approval rules defined
- [ ] Eval: functional / safety / business-policy gates defined
- [ ] Reliability: RTO/RPO, fallback, DR runbook defined
- [ ] FinOps: budget, tags, owner, cost alert defined
