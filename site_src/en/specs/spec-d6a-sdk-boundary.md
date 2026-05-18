# Ask AI to Rewrite the D3 Agent with Agent Framework SDK

> Bilingual mirror. Original source: `prep-artifacts/day-7/specs/spec-d6a-sdk-boundary.md`.

## English Guide

This is the bilingual mirror for a prompt spec or decision card. Use the English heading for discovery, then rely on the full Chinese source below for the exact template, constraints, and self-verification checklist.

- Chinese canonical title: 让 AI 帮我用 Agent Framework SDK 重写 D3 的 agent
- English navigation title: Ask AI to Rewrite the D3 Agent with Agent Framework SDK
- Scope: this page is part of the full bilingual Foundry training site.

## Chinese Source with Bilingual Headings

> 抽自 docs/01-instructor-handbook-v2.md D6a 模块；同步规则见 docs/02-instructor-prep-checklist.md

# Ask AI to Rewrite the D3 Agent with Agent Framework SDK / 让 AI 帮我用 Agent Framework SDK 重写 D3 的 agent

## Goals / 目标
同样的业务逻辑，用 SDK 路径再实现一遍，对比 Agent Service 路径，得出"何时切 SDK"的判断。

## Inputs / 输入
- D3 的 Agent Service 实现（作为对照）
- 我的业务里有没有 Agent Service 不支持的需求（自定义状态？自定义编排？特殊 provider？）

## 让 AI 生成的产物Checklist / 让 AI 生成的产物清单
1. SDK 路径 agent 实现（最小可跑）
2. 与 Agent Service 路径的代码量 / 依赖 / 启动方式对比表
3. "何时切 SDK"决策卡（4 触发条件 + 我项目目前命中几条）

## Decision Card模板 / 决策卡模板
- [ ] Agent Service 不支持我要的编排模式（如自定义状态机）
- [ ] 我需要把 agent 嵌入已有服务进程（不想多一个托管运行时）
- [ ] 我对延迟敏感，托管层多一跳无法接受
- [ ] 我要 provider 不在 Foundry 模型目录里
→ 命中 ≥1 条：考虑 SDK；命中 0 条：留在 Agent Service

## 成本影响（Decision Card必填） / 成本影响（决策卡必填）
SDK 路径相比 Agent Service 新增的成本项：
- 运行时：Container Apps / VM 实例费（参考 D5 估算表）
- 观测：自接 Application Insights 摄入费 + dashboard 维护
- 维护：on-call 轮值（24/7 还是工作时间）
- 状态：自建状态存储（Redis / Cosmos）
[我这个项目，省下的托管费 vs 上述新增项，净差额方向？]

## Constraints / 约束
- 不准把 Agent Service 的代码直接复制改名——必须重写、对照
- 必须留下 README 说明"为什么我项目里两条路径都保留 / 只保留一条"

## Self-Verification / 自验证
- [ ] SDK 路径 agent 能跑通（输入 → 输出）
- [ ] 对比表填实，不接受"差不多一样"
- [ ] 决策卡命中条数 + 结论一致
- [ ] 成本影响栏给出净差额方向（不接受空）
