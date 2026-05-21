# 收尾：可观测 + 上线 checklist（15 min）

> 时长：15 min ｜ 形式：讲师讲 + 学员对照客服 agent 自检 ｜ 不动手
> 状态：⚠️ 蒸馏自 v2 D9/D10 + Foundry 2026/05 [Agent tracing 概念](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept) + [Monitor agents dashboard](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard)
>
> 节奏提示：本段 15 min 是建议，五个小节按 4+4+3+2+2 分配。讲师可以在"评分自检"留时间，砍"runbook 模板"细节让学员课后看。

## 一、可观测三件套（4 min）

你的客服 agent 已经在 portal trace 里能看见。**生产化的 minimum 还需要**：

1. **Tracing**：每条对话能找到 span → 动手 0 看过
   - **Prompt agents tracing = GA**（v3 走的路径，落在 GA 范围）
   - **Hosted / Workflow / Custom agent tracing 仍是 Preview**——上生产前要确认 GA 状态
   - Trace 数据落在你 project 关联的 **Application Insights**——⚠️ 这会**单独计费**（按 ingest GB + 保留天数算）；上线前估一下高峰 trace 体量，否则月底账单容易爆
2. **Agent Monitoring Dashboard**（Foundry portal Observability → Monitor）：运营指标 + 评测结果汇总，比自己拼 Datadog 快
3. **Continuous evaluation**：在 Control Plane → **Assets** pane 给已部署 agent 开 continuous evaluation——线上请求按采样率自动跑 eval，结果回流到 dashboard。生产化首选 vs 只靠 CI pre-merge 跑

**客服场景特殊关注**：

- 单条对话**多轮** token 累加——单轮看着省，10 轮可能爆
- 高峰期 429——客服流量有日内峰谷，Quota 要按峰值算（Control Plane → **Quota** pane 看）

## 二、上线 checklist（4 min）

**6 项最小生产化清单**（v3 砍到必要项）：

- [ ] **环境分离**：dev / staging / prod 各自 Foundry project（或至少独立 deployment）；prod 不共享 dev 的 agent version
- [ ] **Eval gate 接 CI**：每次 PR 跑动手 1 的 evaluation，至少 task_adherence happy path 不退化（[GitHub Action for evaluations](https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluation-github-action)）
- [ ] **Guardrail policy 已在 Control Plane → Compliance 开**：content safety + prompt injection + protected materials（动手 2 的平台层）
- [ ] **Runbook**：客服 agent 4 类故障（429 / 5xx / 误回复 / 越权承诺）各一条处置流程
- [ ] **Cost + Budget alert**：portal Cost analysis 设日预算 + webhook；同时确认 Application Insights ingest 额度也在监控里
- [ ] **回滚一行命令**：`project.agents.create_version` 留下的 version 链可以一键切回上一个——把切换命令贴 runbook 里

讨论：你的项目目前命中几条？哪几条是 Day-1 必须有的？

## 三、Runbook 模板（3 min）

**客服 agent 429 限流处置**示例：

```markdown
## 客服 agent 429 限流

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
- 客服侧切回人工

### 复盘
- 24h 内填一份 RCA：burst 来源 / 是否符合 capacity plan / 调整 Quota 阈值
```

讲师 Day-7 完成 4 类故障的完整 runbook，放在 `workshop/docs/v3/code/runbook.md`。

## 四、课后自学包（3 min）

短课没跑完的、你想接着做的：

### 把 v3 跑深

- **综合作业**：把客服 agent 换成你自己项目场景，重跑动手 0/1/2
- **接真接口**：把 instructions 里 hardcode 的订单换成 **function calling / OpenAPI tool / MCP** 调真后端
- **接 Foundry IQ**：FAQ / 退货政策做成 knowledge base，agent 用 agentic retrieval（带 ACL/Purview）而不是塞 system prompt
- **多 agent 拆分**：把客诉升级拆成独立 agent，主 agent 用 connected agents / A2A protocol 调它
- **CI 接入**：eval + GitHub Actions 当 merge gate
- **Continuous evaluation**：给 staging deployment 开，看一周的真实 task_adherence 漂移

### Foundry 平台延伸阅读

| 想深入哪块 | 官方入口 |
|---|---|
| 三种 agent 类型详细对比（Prompt/Workflow/Hosted） | [What is Foundry Agent Service?](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) |
| 12 built-in + 4 custom tools + Toolbox preview | [Tool catalog](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-catalog) |
| 企业知识 + agentic retrieval + ACL | [What is Foundry IQ?](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/what-is-foundry-iq) |
| 跨订阅 fleet 治理 | [Foundry Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview) |
| Tracing + OTel 语义约定 | [Agent tracing 概念](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept) |
| 完整 evaluator 列表 | [Agent evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators) |
| AI Red Teaming Agent（preview） | [AI red teaming agent](https://learn.microsoft.com/en-us/azure/foundry/concepts/ai-red-teaming-agent) |

### v2 三天班（系统学）

v2 11 模块完整版在仓库 `docs/00-training-plan-v2.md`。**⚠️ 注意**：v2 仍基于 Foundry classic 旧口径（Assistants API / 多包 SDK / 月度 api-version），2026 上半年 partially outdated——课程概念结构可用，具体 API 调用以最新 Foundry 文档为准。

## 五、你的评分自检（2 min）

回到 [v3 总览](../index.md) §"学完之后你应该能"。3 维全 pass 即课程通过：

- [ ] **认知**：能口头讲 Foundry 7 能力域中至少 4 个 + Control Plane 5 panes 各做什么（S1）
- [ ] **实操**：动手 0 跑通 1 条对话 + 动手 1 至少 2 条评测明确 pass/fail
- [ ] **安全**：能讲你的 guardrail 防的是哪类 attack、为什么客服场景重要、平台层 vs 业务层各能解决什么（挡住与否不影响）

任何 1 维 fail 不影响发放课程材料，讲师会在课后跟进。

## 反馈

课中卡点 / 课后想到的改进，**1 句话**写在群里。讲师会回写到这份 v3 内容里——下一期学员受益。
