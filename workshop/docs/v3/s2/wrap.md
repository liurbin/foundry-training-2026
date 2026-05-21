# 收尾：可观测 + 上线 checklist（15 min）

> 时长：15 min ｜ 形式：讲师讲 + 学员对照客服 agent 自检 ｜ 不动手
> 蒸馏自 v2 D9 + D10

> 节奏提示：本段 15 min 是建议，五个小节按 4+4+3+2+2 分配。讲师可以在"评分自检"留时间，砍"runbook 模板"细节让学员课后看。

## 一、可观测三件套（4 min）

你的客服 agent 已经在 portal trace 里能看见。**生产化的 minimum 还需要**（蒸馏自 v2 D9）：

1. **Tracing**：每条对话能找到 span → 已有（动手 0 看过）
2. **Cost telemetry**：每个 deployment 的 token 用量 + $ 估算 → portal Metrics 标签
3. **Alert**：超出预算 / 429 飙升 / ASR > X% 触发通知 → portal Alerts 设置

**客服场景特殊关注**：

- 单条对话**多轮** token 累加——单轮看着省，10 轮可能爆
- 高峰期 429——客服流量有日内峰谷，Quotas 要按峰值算

## 二、上线 checklist（4 min）

蒸馏自 v2 D9/06 + D10。**6 项最小生产化清单**（v3 砍到必要项）：

- [ ] **Endpoint + secret 分环境**：dev / staging / prod 独立 deployment 和 key，prod key 进 Key Vault
- [ ] **Eval gate 接 CI**：每次 PR 跑 eval_harness.py，至少 happy path 不退化
- [ ] **Red Team gate 阈值**：ASR > X% 阻塞上线（动手 2 的 guardrail 直接关联这条）
- [ ] **Runbook**：客服 agent 4 类故障（429 / 5xx / 误回复 / 越权承诺）各一条处置流程
- [ ] **Cost alert**：日预算上限 + 触发 webhook
- [ ] **回滚一行命令**：deployment 切回上一个 version 的 `az` / SDK 命令贴在 runbook 里

讨论：你的项目目前命中几条？哪几条是 Day-1 必须有的？

## 三、Runbook 模板（3 min）

蒸馏自 v2 D9/04。**客服 agent 429 限流处置**示例：

```markdown
## 客服 agent 429 限流

### 触发条件
portal Metrics: `RateLimitExceeded` 1min 窗口 > 5 次

### 第一响应（≤ 5 min）
1. 看是哪个 deployment 限流（dev/staging/prod？）
2. 看 LLM 调用量是不是异常 burst（是 → 限流是对的，不是 → 配额问题）

### 处置
- burst 真实：开启限流 503 兜底（agent 返回"系统繁忙，请稍候"），不影响其他用户
- 配额问题：portal 申请扩配额；临时把流量切到备用 deployment

### 通知
- > 10 min 仍未恢复：通知 oncall + 产品负责人
- 客服侧切回人工

### 复盘
- 24h 内填一份 RCA：burst 来源 / 是否符合 capacity plan / 调整 Quotas 阈值
```

讲师 Day-7 完成 4 类故障的完整 runbook，放在 `workshop/docs/v3/code/runbook.md`。

## 四、课后自学包（3 min）

短课没跑完的、你想接着做的：

### 把 v3 跑深

- **综合作业**：把客服 agent 换成你自己项目场景，重跑动手 0/1/2
- **接真接口**：mock_orders.json 换成真 ERP API
- **多 agent 拆分**：把客诉升级拆成独立 agent，主 agent 调它做 as_tool
- **CI 接入**：eval_harness + GitHub Actions

### 系统学完 v2 三天班

| v2 模块 | 你会补到什么 |
|---|---|
| [D1 概念](../../d01_concepts/index.md) | 完整 14 格能力地图 + 4 条反例 |
| [D2 Agent vs SDK](../../d02_agent_vs_sdk/index.md) | 5 类硬约束 + 成本估算 |
| [D3 单 agent](../../d03_single_agent/index.md) | Bicep 部署 + 完整 trace 三件套 |
| [D7 多 agent](../../d07_multi_agent/index.md) | as_tool / Workflows 实操 |
| [D8 Red Team](../../d08_red_team/index.md) | Portal + SDK 完整 baseline |
| [D9 生产化](../../d09_production/index.md) | CI/CD workflow + 完整 runbook |
| [D10 边界](../../d10_boundary/index.md) | 14 行边界表 + 迁移方案 |

### Specs（让 codex CLI 当陪练）

11 个模块的 spec 在 `prep-artifacts/day-7/specs/`，每份是给 AI-pair 当 prompt 用的。挑感兴趣的让 codex 跑一遍。

## 五、你的评分自检（2 min）

回到 [v3 总览](../index.md) §"学完之后你应该能"。3 维全 pass 即课程通过：

- [ ] **决策**：能口头讲"客服 agent 用/不用/部分用 Foundry"+ 一条理由（S1）
- [ ] **实操**：动手 0 跑通 1 条对话 + 动手 1 至少 2 条评测明确 pass/fail
- [ ] **安全**：能讲你的 guardrail 防的是哪类 attack、为什么客服场景重要（挡住与否不影响）

任何 1 维 fail 不影响发放课程材料，讲师会在课后跟进。

## 反馈

课中卡点 / 课后想到的改进，**1 句话**写在群里。讲师会回写到这份 v3 内容里——下一期学员受益。
