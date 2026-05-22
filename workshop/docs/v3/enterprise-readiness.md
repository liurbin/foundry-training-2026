# Enterprise Readiness：12 个上线边界

> 这页是 v3 的上线边界速查，不是动手步骤。4h 课内只讲判断框架；真实项目要在 Day-7 或客户 discovery 里按订阅、区域、模型、网络和合规要求重验。

## 为什么必须单独讲

Customer Operations Agent 跑通只证明 pattern 成立。Startup / partner 真正交付时，客户不会只问“能不能跑”，而会按 12 类问题审：

| 类别 | 客户会问什么 | 交付物 |
|---|---|---|
| 1. Tenant / subscription / project governance | 资源归属、命名、环境、权限边界怎么管？ | 订阅 / RG / project 拓扑 |
| 2. Identity / RBAC / secrets | 人、应用、agent、tool 分别用什么身份？ | RBAC 矩阵 + Key Vault 策略 |
| 3. Network security | 调用和 tool 访问能不能走私网？ | Private endpoint / outbound 设计 |
| 4. Data governance / privacy / encryption | prompt、文件、trace、日志里有什么数据？ | 数据分类 + retention + CMK 策略 |
| 5. Deployment topology / capacity | Global、Data Zone、Regional、PTU 怎么选？ | deployment type + region + capacity 计划 |
| 6. Model access / quota / lifecycle | 哪些模型能用，quota 够不够，模型升级怎么控？ | model access + TPM/RPM + fallback 计划 |
| 7. Safety controls | content filter、Prompt Shields、abuse monitoring 能不能改？ | filter / abuse monitoring 决策记录 |
| 8. Tool / action security | agent 调业务系统会不会越权或误操作？ | tool allowlist + human approval 规则 |
| 9. Evaluation / red team / release gate | 怎么证明改动没退化？ | eval dataset + thresholds + CI gate |
| 10. Observability / logging / SIEM | 日志进哪里，prompt 能不能入日志？ | App Insights / Log Analytics / SIEM 路由 |
| 11. Reliability / DR / graceful degradation | 平台或 region 出问题怎么办？ | RTO/RPO + fallback runbook |
| 12. FinOps / operations ownership | 成本、告警、oncall、回滚谁负责？ | budget + alerts + runbook + owner |

这 12 类不是都要在 4h 内实操，但 builder 必须知道它们存在，否则课堂 demo 迁不进企业环境。

## 1. Tenant / Subscription / Project Governance

先定资源边界，再写代码。

| 决策 | 要问的问题 |
|---|---|
| Tenant | 客户 tenant 还是 partner tenant？跨 tenant 邀请谁负责？ |
| Subscription | POC、staging、prod 是否分订阅？quota 是否在目标订阅上？ |
| Resource group | 网络、Foundry project、App Insights、Key Vault 是否同 RG？ |
| Project | dev / staging / prod 是三个 project，还是一个 project 多 deployment？ |
| Naming / tagging | 成本、环境、owner、数据等级如何 tag？ |

建议：prod 不共享 dev 的 agent version；partner demo 订阅不能直接变客户生产订阅。

官方入口：[RBAC for Foundry hubs and projects](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/hub-rbac-azure-ai-foundry)。

## 2. Identity / RBAC / Secrets

v3 用 `DefaultAzureCredential` 是对的，但上线还要拆清楚身份：

| 主体 | 最小要求 |
|---|---|
| 人类 builder | Azure AI Developer / User 等最小角色，不给 Owner 当日常权限 |
| CI/CD | federated credential 或 managed identity，不用长期 secret |
| App runtime | managed identity 调 Foundry、Key Vault、tool backend |
| Tool backend | 单独 scope，不复用 Foundry project identity 做所有事 |
| Secrets | Key Vault 管理，不进 repo、prompt、trace、tool output |

判断规则：

- 能用 Entra ID / managed identity，就不要发 API key。
- `DefaultAzureCredential` 只是客户端拿 token 的方式，不等于权限设计完成。
- tool 调业务系统时，用业务系统自己的授权边界，不能把 agent 当超级用户。

官方入口：[Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview)、[Managed identities](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)。

## 3. Network Security

v3 课中默认走公网 endpoint，方便 4h 内跑通。企业项目要分 inbound / outbound：

| 层 | 要问的问题 | Foundry / Azure 路径 |
|---|---|---|
| Inbound | 用户、应用、CI 从哪里访问 project endpoint？ | Private Endpoint / Private Link、禁用 public network access、企业 DNS、VPN / ExpressRoute |
| Outbound | agent 调 tool / storage / search / 数据库时走哪里？ | Managed virtual network / approved outbound、私有 endpoint、允许列表 |

判断规则：

- 处理客户数据、PII、受监管数据：优先设计 private endpoint + 禁 public access。
- agent 要连企业内部 API：先确认 outbound 规则和私有网络路径，不要等代码写完才补。
- 课中只验证公网路径；不要把课中环境当生产网络样板。

官方入口：[Configure a private link](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/configure-private-link)、[Configure managed networks](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/configure-managed-network)。

## 4. Data Governance / Privacy / Encryption

agent 项目里数据不只在 prompt 里。至少列 6 类：

| 数据 | 可能出现在哪里 | 要定的边界 |
|---|---|---|
| 用户输入 | prompt、trace、eval dataset | 是否含 PII；是否可采样 |
| 模型输出 | response、trace、日志 | 是否可入日志；是否要脱敏 |
| 文件 / 知识 | upload、knowledge store、search index | retention、ACL、Purview / DLP |
| Tool 输入输出 | function args、tool response | 最小字段、禁止 secret、脱敏 |
| Evaluation data | JSONL、report、judge reasoning | 是否能离线导出；谁可看 |
| Operational logs | App Insights、Log Analytics、SIEM | retention、region、RBAC |

加密要问：

- 是否要求 customer-managed keys（CMK）？
- Key Vault firewall / private endpoint 是否影响服务访问？
- system-assigned 还是 user-assigned managed identity？

官方入口：[CMK for Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/encryption-keys-portal)、[Data, privacy, and security](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy)。

## 5. Deployment Topology / Capacity

部署类型决定三件事：请求在哪里处理、吞吐和延迟怎么保证、成本和 quota 怎么算。

| 模式 | 适合什么 | 关键边界 |
|---|---|---|
| **Global Standard** | 通用线上流量、想要更大弹性 | 请求可能由全球基础设施处理；确认客户的数据处理要求 |
| **Data Zone Standard** | 要限制在 EU / US 等数据区域内处理 | 比 Global 更强区域边界，但不是单一 region |
| **Regional Standard** | 明确要求单一区域处理、低风险 POC | 容量和模型可用性受 region 影响更明显 |
| **Batch** | 离线评测、批处理、低成本非实时任务 | 不是在线 agent path；要接受异步完成窗口 |
| **Provisioned / PTU** | 稳定高吞吐、可预测延迟、企业生产流量 | 需要 PTU quota / reservation；区域和模型容量可能售罄 |

课堂样例默认不要讲成“部署建议”。它只是最小公网 + shared capacity path。真实客户要先回答：

- 是否有数据驻留要求？
- 峰值 QPS / TPM 是多少？
- 是否需要 latency SLO？
- 是否愿意为保留吞吐付 PTU 成本？

官方入口：[Deployment types](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/deployment-types)、[Provisioned throughput](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/provisioned-throughput)。

## 6. Model Access / Quota / Lifecycle

不要把 “能看到模型” 等同于 “能生产使用模型”。至少核四层：

| 层 | 要核什么 |
|---|---|
| 模型可用性 | 目标模型是否支持目标 region / deployment type |
| 订阅与层级 | Enterprise / MCA-E / 默认订阅 / 学生订阅的默认 quota 不同 |
| Quota 维度 | 通常按 subscription + region + model / deployment type 管 TPM / RPM |
| PTU 容量 | PTU quota 和实际 capacity 是两件事；大客户要提前锁容量 |
| 模型 lifecycle | 模型升级、退役、fallback model、eval 回归怎么做 |

Day-7 讲师要给学员明确值：`MODEL_DEPLOYMENT_NAME`、deployment type、region/data zone、TPM/RPM、是否 PTU。

官方入口：[Quotas and limits](https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits)、[Model availability](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)。

## 7. Safety Controls：Content Filter / Prompt Shields / Abuse Monitoring

默认口径要讲清楚：这些不是普通开关。

| 项 | 默认 / 边界 |
|---|---|
| Content filtering | 默认启用；可配置不同类别和阈值。关闭过滤或只 annotate 通常需要申请 modified content filtering。 |
| Prompt Shields | 通用 prompt injection / document attack 风险可走平台层；业务越权仍要靠 instructions、eval、output filter、tool approval。 |
| Protected material | 版权材料风险要按客户场景决定是否启用 / 评测。 |
| Abuse monitoring | 默认有自动滥用检测；部分客户可能涉及内容采样 / 人审流程。 |
| Modified abuse monitoring | 不是 portal 随手关闭；通常只给符合条件的 managed customer / partner，经 Microsoft 流程批准。 |

课堂话术：

- “content filter 能挡通用安全类别，不等于能挡‘不准退款’这种业务规则。”
- “关闭 / 降级安全监测不是工程优化，是合规审批。”
- “如果客户要求不存 prompt / 不做人审，先走 eligibility 和审批，再设计日志策略。”

官方入口：[Content filtering](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter)、[Prompt Shields](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-prompt-shields)、[Limited access features](https://learn.microsoft.com/en-us/azure/ai-services/cognitive-services-limited-access)。

## 8. Tool / Action Security

2026 的 agent 风险通常不在“会不会聊天”，而在“会不会调用错工具”。

| 动作类型 | 示例 | 默认策略 |
|---|---|---|
| Query | 查订单、查 ticket、查库存 | 可自动化，但要做参数校验和最小返回字段 |
| Recommend | 建议退款、建议升级、建议下一步 | 可自动化，但要标明不是最终动作 |
| Mutate | 退款、改地址、发券、关 alert、改权限 | 默认 human approval / 二次确认 / 幂等 key |

必须做：

- tool arguments 和 tool output 都当作 untrusted input。
- 不在 tool output 返回 secret、token、connection string。
- 每个 tool 都要有 scope、rate limit、audit log。
- eval 要覆盖 tool misuse：错订单、越权退款、prompt injection 触发 tool。

官方入口：[Function calling security considerations](https://learn.microsoft.com/en-us/azure/ai-services/agents/how-to/tools/function-calling?azure-portal=true)。

## 9. Evaluation / Red Team / Release Gate

课中 3 条 eval 只证明最小闭环。上线至少要分 5 类：

| 类别 | 例子 |
|---|---|
| Functional | happy path、edge case、tool call success |
| Grounding | 是否引用正确数据、是否 hallucinate |
| Safety | harmful content、protected material、jailbreak |
| Business policy | 不承诺退款、不泄露 PII、不越权 |
| Regression | prompt、model、tool、filter 改动后是否退化 |

生产建议：

- 每次 prompt / instructions / model deployment / tool schema 改动都跑 eval gate。
- 上线后用 continuous evaluation 对采样流量做监控。
- red team scan 不是一次性验收；重要 release 前重跑。

官方入口：[Agent Monitoring Dashboard](https://learn.microsoft.com/en-us/azure/ai-foundry/observability/how-to/how-to-monitor-agents-dashboard?view=foundry)、[Risk and safety evaluators](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/risk-safety-evaluators)。

## 10. Observability / Logging / SIEM

v3 动手 0 看的是 portal trace。真实交付要接进客户的日志系统：

| 目标 | 最小做法 | 生产化补充 |
|---|---|---|
| Agent trace | 连接 Application Insights，在 Foundry portal 看 span / token / latency | 用 Azure Monitor / Log Analytics 管 retention、RBAC、查询 |
| 应用日志 | SDK 调用侧打结构化日志：request id、agent version、case id、latency、error type | 不记录 prompt 全文，或做脱敏 / 采样 |
| 外部 observability | OpenTelemetry / OTLP exporter | 接 Datadog、Grafana、Jaeger、Honeycomb 等现有系统 |
| 安全审计 | Azure Monitor diagnostic settings / Event Hub 路由 | 进入 SIEM，保留访问、配额、异常、policy 事件 |

建议课堂话术：

- “Trace 证明能 debug；Log Analytics / SIEM 集成证明能运营。”
- “Prompt 和输出是否可入日志，是客户合规问题，不是工程默认值。”

官方入口：[Agent tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept)、[Set up tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup)、[OpenTelemetry tracing](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agents-sdk)。

## 11. Reliability / DR / Graceful Degradation

Agent Service 是有状态系统，不能只靠“再部署一次代码”恢复。

要问：

- RTO / RPO 是多少？
- agent definitions、threads、files、knowledge、tool connections 谁备份？
- region outage 时是切 region、降级到人工，还是返回 read-only？
- 依赖的 Cosmos DB、Azure AI Search、Storage、App Insights 是否也有恢复策略？

最低要求：

- IaC 保存 project 依赖资源和 app 配置。
- agent instructions / eval dataset / tool schema 进 git。
- runbook 写清楚：模型不可用、quota 爆、trace 断、tool backend 挂、region outage 时怎么降级。

官方入口：[Foundry Agent Service disaster recovery](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/disaster-recovery)、[Azure reliability guidance](https://learn.microsoft.com/en-us/azure/reliability/overview)。

## 12. FinOps / Operations Ownership

最后不是技术问题，是谁运营。

| 项 | 要定什么 |
|---|---|
| Cost | token、PTU、Application Insights ingest、storage、tool backend 成本 |
| Budget | 日预算、月预算、异常增长 alert |
| Owner | 产品 owner、engineering owner、security owner、oncall |
| Runbook | 429、5xx、误回复、越权承诺、数据泄露、成本异常 |
| Versioning | agent version、model deployment、tool schema、eval dataset 一起记录 |
| Rollback | 回滚到哪个 agent version / model / filter policy |

建议：demo 阶段也要打 tag，否则 partner 很快会不知道哪个客户、哪个 POC、哪个环境在花钱。

## 课内怎么讲

- S1 Operate：点到治理、网络、quota、policy、cost，不展开实操。
- S2 收尾：把这页作为上线 checklist 的扩展，不增加动手时间。
- Day-7：讲师必须用真实订阅补齐 deployment type、region、quota、filter、logging、network、RBAC、DR 截图或配置证据。

## Day-7 必填清单

- [ ] Tenant / subscription / RG / project 拓扑已定
- [ ] RBAC 矩阵：human、CI、runtime、tool identity 已定
- [ ] Project endpoint：public 还是 private endpoint？
- [ ] Outbound：agent/tool 是否需要访问私有 API？路径是什么？
- [ ] Data：prompt、trace、eval、tool output 是否含 PII？retention 多久？
- [ ] Encryption：是否需要 CMK？Key Vault / managed identity 是否配好？
- [ ] Logging：Application Insights / Log Analytics / SIEM 是否接好？prompt 是否脱敏？
- [ ] Deployment：Global / Data Zone / Regional / PTU 选哪种？为什么？
- [ ] Quota：目标模型、region、TPM/RPM、PTU quota 是否够？
- [ ] Content filter：默认、custom、modified content filtering 哪一种？
- [ ] Abuse monitoring：默认还是已获 modified abuse monitoring 批准？
- [ ] Tool action：query / recommend / mutate 分类和 human approval 规则已定
- [ ] Eval：functional / safety / business-policy gate 已定
- [ ] Reliability：RTO/RPO、fallback、DR runbook 已定
- [ ] FinOps：budget、tags、owner、cost alert 已定
