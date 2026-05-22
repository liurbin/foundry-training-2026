# 收尾：可观测 + 上线 checklist（15 min）

> 时长：15 min ｜ 形式：讲师讲 + 学员对照 Customer Operations Agent 自检 ｜ 不动手
> 状态：⚠️ 蒸馏自 v2 D9/D10 + Foundry 2026/05 [Agent tracing 概念](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept) + [Monitor agents dashboard](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard)
>
> 节奏提示：本段 15 min 是建议，五个小节按 4+4+3+2+2 分配。讲师可以在"评分自检"留时间，砍"runbook 模板"细节让学员课后看。

## 一、可观测三件套（4 min）

你的 Customer Operations Agent 已经在 portal trace 里能看见。**生产化的 minimum 还需要**：

1. **Tracing**：每条对话能找到 span → 动手 0 看过
   - **Prompt agents tracing = GA**（v3 走的路径，落在 GA 范围）
   - **Hosted / Workflow / Custom agent tracing 仍是 Preview**——上生产前要确认 GA 状态
   - Trace 数据落在你 project 关联的 **Application Insights**——⚠️ 这会**单独计费**（按 ingest GB + 保留天数算）；上线前估一下高峰 trace 体量，否则月底账单容易爆
2. **Agent Monitoring Dashboard**（Foundry portal Observability → Monitor）：运营指标 + 评测结果汇总，比自己拼 Datadog 快
3. **Continuous evaluation**：在 Control Plane → **Assets** pane 给已部署 agent 开 continuous evaluation——线上请求按采样率自动跑 eval，结果回流到 dashboard。生产化首选 vs 只靠 CI pre-merge 跑

**Customer Operations 场景特殊关注**：

- 单条对话**多轮** token 累加——单轮看着省，10 轮可能爆
- 高峰期 429——服务运营类流量有日内峰谷，Quota 要按峰值算（Control Plane → **Quota** pane 看）

## 二、上线 checklist（4 min）

**6 项最小生产化清单**（v3 课内只保留必要项；完整 12 类见 [Enterprise Readiness](../enterprise-readiness.md)）：

- [ ] **环境分离**：dev / staging / prod 各自 Foundry project（或至少独立 deployment）；prod 不共享 dev 的 agent version
- [ ] **Eval gate 接 CI**：每次 PR 跑动手 1 的 evaluation，至少 task_adherence happy path 不退化
- [ ] **Guardrail policy 已开**：content safety + prompt injection + protected materials；业务规则另走 instructions / output filter / tool approval
- [ ] **Observability / logging**：Application Insights + 结构化日志路径明确，prompt 是否入日志已决定
- [ ] **Runbook / rollback**：429 / 5xx / 误回复 / 越权承诺有处置流程，能回滚 agent version
- [ ] **Cost / quota alert**：TPM/RPM、PTU、Application Insights ingest、日/月预算和告警已设

课堂串法：

- **今天已触达**：agent version、eval、guardrail、trace、quota 429、runbook。
- **课后必须补**：identity、private networking、data retention、deployment type、CMK、SIEM、DR、FinOps。
- **需要客户 / Microsoft 前置条件**：PTU capacity、modified abuse monitoring、private networking、enterprise RBAC。

讨论：你的项目目前命中几条？哪几条是 Day-1 必须有的？

## 三、Runbook 模板（3 min）

**Customer Operations Agent 429 限流处置**示例：

```markdown
## Customer Operations Agent 429 限流

### 触发条件
Foundry portal Metrics / Application Insights：`RateLimitExceeded` 1min 窗口 > 5 次

### 第一响应（≤ 5 min）
1. 看是哪个 deployment 限流（dev/staging/prod？）
2. 看 LLM 调用量是不是异常 burst（是 → 限流是对的，不是 → 配额问题）

### 处置
- burst 真实：开启限流 503 兜底（agent 返回"系统繁忙，请稍候"），不影响其他用户
- 配额问题：Control Plane → Quota 申请扩配额；临时把流量切到备用 deployment 或开 **Priority processing**（preview，保留吞吐）

### 通知
- > 10 min 仍未恢复：通知 oncall + 产品负责人
- 运营侧切回人工

### 复盘
- 24h 内填一份 RCA：burst 来源 / 是否符合 capacity plan / 调整 Quota 阈值
```

讲师 Day-7 完成 4 类故障的完整 runbook，放在 `workshop/docs/v3/code/runbook.md`。

## 四、课后自学包（3 min）

短课没跑完的、你想接着做的：

### 把 v3 跑深

- **真实项目评估**：用 [AI Solution Readiness Blueprint](../ai-solution-readiness-blueprint.md) 先做通用 AI solution assessment，再做 Foundry-specific evidence pack
- **Product startup**：把课堂 agent 换成产品内 support / research / workflow assistant，重跑动手 0/1/2
- **Solution partner**：把课堂 agent 换成客户运营、现场服务、销售运营或合规审核方案，重跑 eval + guardrail
- **Platform / infra builder**：把课堂 agent 换成 eval gate、tool gateway、agent registry 或 observability workflow
- **接真接口**：把 instructions 里 hardcode 的订单换成 **function calling / OpenAPI tool / MCP** 调真后端
- **接 Foundry IQ**：FAQ / 退货政策做成 knowledge base，agent 用 agentic retrieval（带 ACL/Purview）而不是塞 system prompt
- **补 enterprise readiness**：按 [Enterprise Readiness](../enterprise-readiness.md) 核 12 类上线边界
- **多 agent 拆分**：把客诉升级拆成独立 agent，主 agent 用 connected agents / A2A protocol 调它
- **CI 接入**：eval + GitHub Actions 当 merge gate
- **Continuous evaluation**：给 staging deployment 开，看一周的真实 task_adherence 漂移

### Foundry 平台延伸阅读

| 想深入哪块 | 官方入口 |
|---|---|
| 三种 agent 类型详细对比（Prompt/Workflow/Hosted） | [What is Foundry Agent Service?](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) |
| 1,400+ tools（公共 + 私有 catalog）+ agent 内置 12+4 子集 + Toolbox preview | [Tool catalog](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog) |
| 企业知识 + agentic retrieval + ACL | [What is Foundry IQ?](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq) |
| 跨订阅 fleet 治理 | [Foundry Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview) |
| Tracing + OTel 语义约定 | [Agent tracing 概念](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept) |
| 完整 evaluator 列表 | [Agent evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators) |
| AI Red Teaming Agent（preview） | [AI red teaming agent](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent) |
| 上线边界速查 | [Enterprise Readiness](../enterprise-readiness.md) |
| 真实项目评估带走物 | [AI Solution Readiness Blueprint](../ai-solution-readiness-blueprint.md) |

### v2 三天班（系统学）

v2 11 模块完整版在仓库 `docs/00-training-plan-v2.md`。**⚠️ 注意**：v2 仍基于 Foundry classic 旧口径（Assistants API / 多包 SDK / 月度 api-version），2026 上半年 partially outdated——课程概念结构可用，具体 API 调用以最新 Foundry 文档为准。

## 五、你的评分自检（2 min）

回到 [v3 总览](../index.md) §"学完之后你应该能"。4 项全 pass 即课程通过：

- [ ] **认知**：能口头讲 Foundry 7 能力域中至少 4 个 + Control Plane 5 panes 各做什么（S1）
- [ ] **实操**：动手 0 跑通 1 条对话 + 动手 1 至少 2 条评测明确 pass/fail
- [ ] **迁移**：能讲把这个 Customer Operations Agent pattern 用到你的产品 / 客户方案 / 平台工具时，哪些 Foundry 能力 Day-1 就接、哪些课后补、哪些不接
- [ ] **安全**：能讲你的 guardrail 防的是哪类 attack、为什么这个 workflow 重要、平台层 vs 业务层各能解决什么（挡住与否不影响）

任何 1 项 fail 不影响发放课程材料，讲师会在课后跟进。

## 反馈

课中卡点 / 课后想到的改进，**1 句话**写在群里。讲师会回写到这份 v3 内容里——下一期学员受益。
