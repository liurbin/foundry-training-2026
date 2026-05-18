# D2: Agent Service vs SDK Selection

> Bilingual mirror. Original source: `workshop/docs/d02_agent_vs_sdk/index.md`.

## English Guide

This is the learner-facing bilingual mirror for the workshop page. The English heading and guide identify the task, while the Chinese source below preserves the complete original instructions, checklists, submissions, and references.

- Chinese canonical title: D2: Agent Service vs SDK 选型
- English navigation title: D2: Agent Service vs SDK Selection
- Scope: this page is part of the full bilingual Foundry training site.

## Chinese Source with Bilingual Headings

# D2: Agent Service vs SDK Selection / D2: Agent Service vs SDK 选型

> 决策模块 / 90 min（40 讲 / 30 实操 / 20 评审）/ 无需 Azure 凭证

## Goals / 目标
- 理解 Agent Service 与 Agent Framework SDK 的能力边界与适用场景
- 掌握 4 维度打分（托管运行时 / portal 可视化 / 代码控制 / 跨 provider 移植性）
- 学会用决策规则（前两项 vs 后两项）输出选型结论，包含"混合"路径
- **能识别 5 类硬约束触发条件**（私有部署 / 网络隔离 / 最少运维 / 高吞吐 SLA / 预算敏感），并把部署与容量作为选型输入而非输出
- 能用日请求量 / token / QPS / on-call 等输入估算两条路径的成本量级
- 能识别 4 类常见错误判断（"SDK 更灵活就选 SDK"、"托管就一定贵"等）

## Prerequisites / 前置
- D1 完成（概念 + 决策模块设计框架）

## Subtasks / 子任务
1. [架构总览与能力边界](01.md) — Agent Service / SDK / Workflows 三条路径各自负责什么
2. [4 维度打分与决策规则](02.md) — 填决策卡的前两项 vs 后两项启发式 + **硬约束触发条件检查**
3. [成本估算与混合路径](03.md) — 用自己项目的 DAU / token / QPS 算出量级，判断是否走混合

## Acceptance Criteria / 验收
- [ ] 学员能填出 D2 决策卡（4 维度全部打分 + **硬约束触发条件全部判定**（命中/未命中）+ 成本估算输入全部填齐）
- [ ] **填硬约束栏前已预读 D5-0 对照表**（防"我就靠常识猜"）
- [ ] 决策结论与 4 维度分数一致，不一致时能写出解释（如"分数倾向 SDK 但团队无人值班所以选 Service"，或"硬约束命中私有部署，覆盖打分直接选 SDK"）
- [ ] 成本影响一栏有具体数字方向（$/月量级 + 主导成本项），不接受"差不多"
- [ ] 评审段能回答："如果团队 6 个月后翻倍，这个决策要不要重做？"
- [ ] 能解释为什么不默认选 SDK（灵活 ≠ 合适：自己负责运行时、状态、failover）
- [ ] 容量类硬约束（高吞吐 SLA / 预算敏感）已带进 D5 capacity planning（评审段口头检查）

## Credential Notes / 凭证说明
- 纯决策模块，无需 Azure 凭证

## References / 参考
- 链回 ../../handbook/01-instructor-handbook-v2.md#d2
