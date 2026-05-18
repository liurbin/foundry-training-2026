# D6a: Agent Framework SDK Boundary

> Bilingual mirror. Original source: `workshop/docs/d06a_sdk_boundary/index.md`.

## English Guide

This is the learner-facing bilingual mirror for the workshop page. The English heading and guide identify the task, while the Chinese source below preserves the complete original instructions, checklists, submissions, and references.

- Chinese canonical title: D6a: Agent Framework SDK 的边界
- English navigation title: D6a: Agent Framework SDK Boundary
- Scope: this page is part of the full bilingual Foundry training site.

## Chinese Source with Bilingual Headings

# D6a: Agent Framework SDK Boundary / D6a: Agent Framework SDK 的边界

> 模块类型：决策 + 实操｜时长：60 min（20 讲 / 30 实操 / 10 评审）｜凭证：学员侧 mock 即可

## Goals / 目标

学完你将能：
- 说出 4 个触发"必须切 SDK"的场景，并对照自己项目命中几条
- 用 SDK 路径重写 D3 的 agent（mock provider 跑通），跟 Agent Service 路径做代码量 / 依赖 / 启动方式对比
- 填出"何时切 SDK"决策卡，含成本影响净差额方向
- 区分"代码更优雅"和"业务理由"——前者不是切换理由

## Prerequisites / 前置

- D2 完成（Service vs SDK 宏观选型已建立）
- D3 单 agent 跑通（作为对照基线）

## Subtasks / 子任务

1. [SDK 路径重写 D3 agent](01.md) — mock provider，本机即可
2. [代码量 / 依赖 / 启动方式对比表](02.md) — ≥ 4 行
3. [决策卡填写 + 成本净差额](03.md) — 4 触发条件 + 我项目命中

## Acceptance Criteria / 验收

- [ ] SDK 路径 agent 在 mock provider 下跑通（输入 → 输出）
- [ ] 对比表填实 ≥ 4 行，不接受"差不多一样"
- [ ] 决策卡命中条数与最终选择一致
- [ ] 成本影响栏给出净差额方向（运行时 / 观测 / on-call / 状态四项；不接受空）
- [ ] 如果你打算两条路径都保留，README 写清业务理由（不接受"以防万一"）
- [ ] 能口头讲清"我项目 6 个月内会不会从 Service 切 SDK"

## Credential Notes / 凭证说明

- 学员侧：mock provider，本机即可
- 不需要真实 Azure / Foundry 凭证；Container Apps / Application Insights 部分以"决策卡里估算"代替真部署

## Negative Examples预警（Review段会被点名） / 反例预警（评审段会被点名）

- "SDK 代码更少更优雅所以切 SDK" → 代码量不是切换理由
- SDK agent 跑 Container Apps 但不接 App Insights → 黑盒
- SDK 路径直接 `import openai` → 跳过 D4 抽象，埋第二次 vendor 锁定
- "两条都跑通所以都保留" → 没业务理由就砍一条

## Upstream Materials / 上游素材

- 无（上游锁 Agent Service 路径，SDK 边界讨论是本课新增）

## References / 参考

- 讲师手册：`../../handbook/01-instructor-handbook-v2.md` D6a 章节
- 课程设计：`../../handbook/00-training-plan-v2.md` Day 2 09:30-10:30
- 上游对照：`../../handbook/03-workshop-fork-mapping.md` D6a 行
