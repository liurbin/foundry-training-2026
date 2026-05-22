# v3 短课：Foundry Builder Onboarding（4 小时）

> 课程类型：4h 短课 ｜ 节奏：S1 90min 决策 + S2 150min 动手 ｜ 凭证：讲师统一发 Foundry project endpoint + Azure 账号邀请（Entra ID / RBAC，**不是 API key**）+ model deployment name

## 课程定位

这是一门 **Foundry platform onboarding for builders**，不是项目设计工作坊。

- 课内目标：看懂 Foundry-native agentic solution 的最小闭环，并亲手跑通一个可迁移 pattern
- 课内不做：逐个帮 startup / partner 设计自己的项目方案
- 课后延伸：把课堂 pattern 换成你的产品、客户方案或平台工具场景

## 这门课你会做什么

围绕一个 **Customer Operations Agent（电商客服样例）**，体验完整的 Foundry-native agentic solution 闭环：

1. **看懂 Foundry**：project endpoint / model / agent / tool / knowledge / eval / guardrail / trace 各自解决什么
2. **起 agent**：用 codex CLI 自然语言驱动，把 agent 接到讲师发的 Foundry project endpoint
3. **评测**：让 codex CLI 帮你写 3 条 case（happy / edge / 对抗），跑出明确 pass/fail
4. **加防护**：选 1 条 attack，加 business guardrail，再跑评测验证
5. **上线 checklist**：12 类 enterprise readiness 边界（身份、网络、数据、部署、quota、安全、工具、eval、日志、DR、成本、运营）

## 4h 节奏

| 段 | 时长 | 形式 | 链接 |
|---|---|---|---|
| 课前 | 10min | 自助装机 | [codex CLI 装机引导](prerequisites/codex-cli-setup.md) |
| S1 | 90min | Foundry builder orientation，不动手 | [S1 Foundry 平台导览](s1/index.md) |
| S2-开场 | 10min | 评测先行论点 + endpoint 说明 | [s2/00-bootstrap.md](s2/00-bootstrap.md) 开头 |
| S2-0 | 20min | 动手：起 agent（hardcode 简化） | [s2/00-bootstrap.md](s2/00-bootstrap.md) |
| S2-1 | 55min | 动手：写评测 | [s2/01-eval.md](s2/01-eval.md) |
| S2-Red Team 框架 | 15min | 讲师讲 + demo 1 条 attack | [s2/02-guard.md](s2/02-guard.md) 开头 |
| S2-2 | 35min | 动手：加 guardrail | [s2/02-guard.md](s2/02-guard.md) |
| S2-收尾 | 15min | 可观测 + 上线 | [s2/wrap.md](s2/wrap.md) |

合计：S1 90min + S2 (10+20+55+15+35+15)=150min = **240min / 4h**

**节奏约定**：4h 是建议，不是死线。哪一段没跑完就进课后接着做——见各页底部"课后扩展"。

上线边界单独放在 [Enterprise Readiness：12 个上线边界](enterprise-readiness.md)。真实项目迁移使用 [AI Solution Readiness Blueprint](ai-solution-readiness-blueprint.md)：先做通用 AI solution 评估，再做 Foundry-specific 文档取证和实现路径。

## 统一样例场景

全程使用同一个虚构样例：**Customer Operations Agent（中等规模电商客服）**。

选择客服不是因为 startup / partner 只能做客服，而是因为它能在 4h 内同时覆盖：业务边界、mock 数据、评测、prompt injection、越权承诺、trace 和上线 runbook。详见 [`scenario.md`](scenario.md)。S2 动手代码和评测 case 都对照这个样例，不需要你自带项目。

## 学完之后你应该能

- 口头讲清 Foundry 里 project / agent / model / eval / guardrail / trace 的职责边界
- 用 codex CLI 让 agent 跑通至少 1 条评测 case 的明确 pass/fail
- 讲清你加的那条 guardrail 防的是哪类 attack、为什么对这个 workflow 重要
- 讲清你的场景**怎么把 Foundry 用透**：把这个 pattern 迁到你的产品 / 客户方案 / 平台工具时，哪些能力 Day-1 就接、哪些课后补、哪些不接

4 项全 pass = 课程通过。**"挡不住"也算 pass**（讲清原因即可，见 [s2/02-guard.md](s2/02-guard.md)）。

## 这门课不教什么

- ❌ 逐个团队的项目设计工作坊——课内给 pattern，不替你完成项目选型
- ❌ Bicep / azd 部署 IaC——v3 用 codex CLI + SDK 起 agent，不走 IaC
- ❌ 多 agent 编排实操——只在 S1 决策段讲框架，不做 handoff / Workflows
- ❌ 真实业务系统对接——业务数据全 mock（讲师在 `code/` 下提供 mock JSON）
- ❌ 5 维度评分流程——简化为 4 项 pass/fail

想系统学完 11 模块 → 上 v2 三天班（站内入口：[`handbook/00-training-plan-v2.md`](../../handbook/00-training-plan-v2.md)）。

## 课后

每一段都有"课后扩展"小节，列出如果你想接着做：

- Product startup：把 Customer Operations Agent 换成你产品里的 support / research / workflow assistant
- Solution partner：把样例换成客户的服务运营、现场服务、销售运营或合规审核场景
- Platform / infra builder：把样例换成 eval gate、tool gateway、agent registry 或 observability workflow
- 用 [AI Solution Readiness Blueprint](ai-solution-readiness-blueprint.md) 评估你的真实场景，先 general，再 Foundry-specific
- 把 mock 业务数据替换成真接口
- 补齐 [enterprise readiness](enterprise-readiness.md)：身份、私网、数据治理、部署模式、quota、安全控制、tool action、eval、日志、DR、成本和运营责任
- 加更多 guardrail / 多 agent 协作 / CI/CD 接入

讲师会持续维护这份 v3 内容，遇到问题在课后群反馈。
