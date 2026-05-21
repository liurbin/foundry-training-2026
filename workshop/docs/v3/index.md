# v3 短课：4 小时压缩版

> 课程类型：4h 短课 ｜ 节奏：S1 90min 决策 + S2 150min 动手 ｜ 凭证：讲师统一发 Azure OpenAI endpoint+key

## 这门课你会做什么

围绕一个**电商客服 agent**场景，体验完整的"AI 副驾驶工程化"闭环：

1. **决策**：客服 agent 该不该用 Foundry？用 Agent Service 还是 SDK？单 agent 还是多 agent？
2. **起 agent**：用 codex CLI 自然语言驱动，3 行命令把 agent 接到讲师发的 endpoint，跑通"订单状态查询"对话
3. **评测**：让 codex CLI 帮你写 3 条评测 case（happy / edge / 对抗），跑 pass/fail
4. **加防护**：选 1 条 attack，让 codex CLI 帮你写 guardrail，再跑评测验证
5. **上线 checklist**：可观测 + runbook + 5 项最小生产化清单

## 4h 节奏

| 段 | 时长 | 形式 | 链接 |
|---|---|---|---|
| 课前 | 10min | 自助装机 | [codex CLI 装机引导](prerequisites/codex-cli-setup.md) |
| S1 | 90min | 全程讨论，不动手 | [S1 决策框架](s1/index.md) |
| S2-开场 | 10min | 评测先行论点 + endpoint 说明 | [s2/00-bootstrap.md](s2/00-bootstrap.md) 开头 |
| S2-0 | 20min | 动手：起 agent（hardcode 简化） | [s2/00-bootstrap.md](s2/00-bootstrap.md) |
| S2-1 | 55min | 动手：写评测 | [s2/01-eval.md](s2/01-eval.md) |
| S2-Red Team 框架 | 15min | 讲师讲 + demo 1 条 attack | [s2/02-guard.md](s2/02-guard.md) 开头 |
| S2-2 | 35min | 动手：加 guardrail | [s2/02-guard.md](s2/02-guard.md) |
| S2-收尾 | 15min | 可观测 + 上线 | [s2/wrap.md](s2/wrap.md) |

合计：S1 90min + S2 (10+20+55+15+35+15)=150min = **240min / 4h**

**节奏约定**：4h 是建议，不是死线。哪一段没跑完就进课后接着做——见各页底部"课后扩展"。

## 统一场景

全程使用同一个虚构场景：**中等规模电商的客服 agent**。

详见 [`scenario.md`](scenario.md)。S1 决策卡、S2 动手代码、评测 case 都对照这个场景，不需要你自带项目。

## 学完之后你应该能

- 口头讲清"我的项目用 / 不用 / 部分用 Foundry"的明确结论 + 一条理由
- 用 codex CLI 让 agent 跑通至少 1 条评测 case 的明确 pass/fail
- 讲清你加的那条 guardrail 防的是哪类 attack、为什么对客服场景重要

3 维全 pass = 课程通过。**"挡不住"也算 pass**（讲清原因即可，见 [s2/02-guard.md](s2/02-guard.md)）。

## 这门课不教什么

- ❌ Bicep / azd 部署 IaC——v3 用 codex CLI + SDK 起 agent，不走 IaC
- ❌ 多 agent 编排实操——只在 S1 决策段讲框架，不做 handoff / Workflows
- ❌ 真实电商接口对接——业务数据全 mock（讲师在 `code/` 下提供 mock JSON）
- ❌ 5 维度评分流程——简化为 3 维 pass/fail

想系统学完 11 模块 → 上 v2 三天班（站内入口：[`handbook/00-training-plan-v2.md`](../../handbook/00-training-plan-v2.md)）。

## 课后

每一段都有"课后扩展"小节，列出如果你想接着做：

- 把客服 agent 换成你自己项目场景
- 把 mock 业务数据替换成真接口
- 加更多 guardrail / 多 agent 协作 / CI/CD 接入

讲师会持续维护这份 v3 内容，遇到问题在课后群反馈。
