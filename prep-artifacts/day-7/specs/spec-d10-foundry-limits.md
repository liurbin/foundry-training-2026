> 抽自 docs/01-instructor-handbook-v2.md D10 模块；同步规则见 docs/02-instructor-prep-checklist.md

# 让 AI 帮我对照 Foundry 能力边界表，找出我项目命中的边界

## 输入
- plan 第五·五能力地图 + 本节边界表（讲师 Day3 发）
- 我项目 D2 / D6a 决策卡产物

## 边界表（讲师当天发实物，学员对照勾选）
> 14 个能力域与 plan 五·五能力地图一一对应（镜像）；plan 改 → 本表同步改。
> "验证来源"列**已预填官方文档锚点**（agent 在 2026/05 抓取核对）；portal 截图 / fork 实测仍由讲师 Day-7 补充，作为"二次验证"。文档措辞如有漂移，以 Day-7 重新抓取为准。

| # | 能力域 | Foundry 的边界（不能做 / 有限制） | 验证来源（官方文档 + Day-7 补 portal/fork） | 命中？ | 迁移方案 |
|---|--------|--------------------------------|---------------------------------------------|--------|----------|
| 1 | Agent Service | 三种 agent 类型分层：prompt / workflow / hosted；"完全自定义控制流"是 Hosted agents 的定位，prompt/workflow 无法承载 | [Agent Service overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview)（"Compare agent types"表 + "Hosted agents"段）| [ ] | 控制流复杂 → Hosted agent（D6a SDK 路径）；多步编排 → Workflow |
| 2 | Workflows | 主要靠 visual designer / YAML，hosted agents **不被 workflow designer 支持**；版本通过"每次 save 创建 immutable 版本"管理，没有原生 git PR / code review 流程 | [Build a workflow](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow)（"Note: Hosted agents aren't supported in the workflow designer" + "Versioning"段）| [ ] | 复杂编排 → Hosted agent 内用 Agent Framework workflows；要 PR review → 走 YAML + git 自管 |
| 3 | Projects | quotas 不在租户级强制，**最高在 Azure 订阅级**；TPM/RPM 是 *per region × per subscription × per model/deployment type* | [Azure OpenAI quotas-limits](https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits)（"Scope of quota" + "Regional quota allocation"段）| [ ] | 跨 project 共享配额不行 → 在订阅维度规划；迁移走资源 export + 重建 |
| 4 | Connections | 支持 Key / Microsoft Entra（managed identity / OBO）/ unauthenticated；轮换 / 第三方凭证类型由 connection 元数据管理 | [Agent Service overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview)（Tools 段"managed authentication"）+ Day-7 portal 截图 connection 创建页 | [ ] | 不在内置 auth 列表 → 走 custom MCP server 包一层；轮换自己写脚本 |
| 5 | Identity | 用 Microsoft Entra ID + Azure RBAC；最近 rename（Foundry User / Owner / Account Owner / Project Manager 替代旧 Azure AI 角色名）；agent 可有专属 managed identity | [Hosted agent quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-hosted-agent)（"Required Permission"段，含 RBAC rename 说明）| [ ] | 跨租户 → 多租户 app 注册 + B2B；粒度不够 → 自管 OBO 转 fine-grained |
| 6 | Models | 模型目录（Azure OpenAI 直供 + 第三方）；quota 按 Tier 1-6 自动升级 | [Quotas-limits "Quota tiers"段](https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits) + [Models sold directly by Azure](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure) | [ ] | 目录外模型 → 自托管 + 走 SDK provider 抽象（D4） |
| 7 | Evaluations / Red Team | **本地 AI Red Teaming Agent (PyRIT) 不兼容 Foundry (new) portal/SDK**；要把 Foundry agent 当 target 必须走云端 Red Teaming Agent；区域受限（East US 2 / France Central / Sweden Central / Switzerland West / US North Central）；仅 single-turn text-only | [Run AI Red Teaming Agent Locally](https://learn.microsoft.com/en-us/azure/foundry/how-to/develop/run-scans-ai-red-teaming-agent)（"Note: AI Red Teaming Agent local is not compatible with the Foundry(new) portal and SDK" + "Region support" + "AI Red Teaming Agent only supports single-turn"）| [ ] | 需 multi-turn / 区域外 → 自建 PyRIT pipeline；CI 集成 → 云端 Red Teaming Agent SDK |
| 8 | Tracing / Monitoring | 走 OTel + Application Insights；**采样、保留、计费跟随 App Insights 配置**；hosted/workflow/custom agents 的 tracing 仍 preview，仅 prompt agents GA | [Agent tracing concept](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept)（"Note: Tracing is generally available for prompt agents only" + "Trace data retention and sampling follow your Application Insights configuration"）| [ ] | 摄入费爆 → App Insights 侧调采样率；自定义维度 → OTel attribute 自加 |
| 9 | Deployment | **Hosted agents 是当前主路径**：托管容器、scale-to-zero、~15 分钟 idle 释放、session 文件最长 30 天；legacy ACA 路径走旧 `azd ai agent` 0.1.25-preview | [Hosted agent quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-hosted-agent)（"Runtime behavior: Hosted agents use scale-to-zero compute. Idle compute deprovisions after approximately 15 minutes" + Warning 段提到 legacy 走 0.1.25-preview）| [ ] | 必须自托管 → ACA legacy（min replicas ≥ 1）/ 自己 VM；BYO VNet → Hosted agents 支持 |
| 10 | Quotas（PAYG） | TPM/RPM 自动 Tier 升级（Tier 1-6），可 opt-out；超 tier 会有更高 latency 抖动；增配走 [quota request form](https://aka.ms/oai/stuquotarequest) | [Quotas-limits "Quota tiers" + "Usage tiers"](https://learn.microsoft.com/en-us/azure/foundry/openai/quotas-limits) | [ ] | 配额不够 → form 申请增配；仍不够 → 升 Capacity（dedicated），见下一行 |
| 11 | Capacity（dedicated） | PTU / Provisioned Throughput / Reservation：按月起买、commitment 期限 ≥ 1 年；区域 + 模型限制比 PAYG 更窄；与 PAYG 正交（可叠加） | [Provisioned throughput](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput) + [Reservation discounts](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/provisioned-throughput#reservation-discounts) | [ ] | 流量不可预测 → 留 PAYG；要 SLA + 稳定 latency → PTU；要锁价 → reservation；区域/模型不支持 → 换 region 或回 PAYG |
| 12 | SDK / Agent Framework | Hosted agents = code-based，框架自选（Agent Framework / LangGraph / 自己写）；workflow designer 不支持 hosted agents 编排 | [Hosted agent quickstart "Step 1"](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/quickstart-hosted-agent) + [Workflow note](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/workflow)（hosted not supported in designer）| [ ] | 想用 hosted 编排多 agent → Agent Framework workflows / 自写 |
| 13 | A2A | 仅 **协议版本 0.3**；仅 text modality；transports 仅 HTTP+JSON / JSONRPC（**无 gRPC**）；要求 Microsoft Entra ID 鉴权，不支持 key-based / anonymous；预览期 | [Enable A2A endpoint](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/enable-agent-to-agent-endpoint)（"Foundry Agent Service supports A2A protocol version 0.3 only" + "Supported A2A transports"表 + "Limitations"段）| [ ] | 跨 vendor 互通 → 对方也须 A2A 0.3 + Entra；要 gRPC → 自包一层 |
| 14 | MCP | 支持 remote MCP servers（含 Azure DevOps MCP preview）+ Azure Functions custom MCP；auth 选项：Key / Entra（agent 或 project managed identity）/ OBO / unauthenticated；Toolbox（preview）统一暴露多 tool | [Agent Service overview "Tools"段](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview) + [Toolbox 文档](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/toolbox) | [ ] | 内置 MCP server 不够 → 自写 MCP server on Azure Functions；rebrand 期 → Day-7 重抓最新 catalog |

（合规 / 数据驻留 / 多租户隔离粒度作为跨能力域的"非功能"边界，参考 [Agent Service overview "Security, privacy, and compliance" + "Private networking"](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview) 一段；Day-7 由讲师按行业法规要求评估是否单列。）

> **预填 URL 的限制**：以上 URL 来源于 agent 在 2026/05 抓取核对；agent 没有 Foundry 订阅 / portal 权限，所以 portal 截图、fork 实测、订阅级 region 可用性这三类**仍是 Day-7 实证项**。

## 让 AI 帮我做的事
1. 我项目命中的边界项打勾
2. 每命中一项，让 AI 给 2 个迁移方案备选
3. 我从备选里选 1 个 + 写出选择理由

## 约束
- 不准把"边界"当"缺点"——边界是中性的，关键是我项目是否命中
- 命中的项必须给迁移方案；没命中的项不要硬找

## 自验证
- [ ] 边界表 14 行全部判定（命中 / 未命中）
- [ ] 命中项都有迁移方案 + 理由
- [ ] 边界表"验证来源"列已由讲师补充 portal/fork 二次证据；纯 URL 行可上课但学员应反馈
- [ ] 与 D1 决策卡一致（如果 D1 说"用 Foundry"但 D10 命中 ≥3 项关键边界，需要回去 review D1）
