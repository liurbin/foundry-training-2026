# Ask AI to Run Native Agent Service Multi-Agent Orchestration and Understand Two Alternatives

> Bilingual mirror. Original source: `prep-artifacts/day-7/specs/spec-d7-multi-agent.md`.

## English Guide

This is the bilingual mirror for a prompt spec or decision card. Use the English heading for discovery, then rely on the full Chinese source below for the exact template, constraints, and self-verification checklist.

- Chinese canonical title: 让 AI 帮我用 Agent Service 原生模式跑通多 agent 编排（主路径）+ 看懂另两种
- English navigation title: Ask AI to Run Native Agent Service Multi-Agent Orchestration and Understand Two Alternatives
- Scope: this page is part of the full bilingual Foundry training site.

## Chinese Source with Bilingual Headings

> 抽自 docs/01-instructor-handbook-v2.md D7 模块；同步规则见 docs/02-instructor-prep-checklist.md

# Ask AI to Run Native Agent Service Multi-Agent Orchestration and Understand Two Alternatives / 让 AI 帮我用 Agent Service 原生模式跑通多 agent 编排（主路径）+ 看懂另两种

## Goals / 目标
主路径学员自己 AI-pair 跑通；as_tool 看讲师 prepared diff；Workflows 看讲师录屏。
最终输出"三选一"决策卡。

## 让 AI 生成的产物Checklist（仅主路径） / 让 AI 生成的产物清单（仅主路径）
1. 两个专家 agent + 一个 orchestrator agent（Agent Service 原生编排）
2. 三段 trace 链路截图
3. "三选一"决策卡

## Decision Card三问 / 决策卡三问
- 编排逻辑稳定 + 不需要自定义控制流？ → Agent Service 原生
- 编排逻辑要自定义 + 但每个子 agent 独立可测？ → as_tool 模式
- 复杂分支 / 长时间运行 / 需要 visual designer？ → Workflows
- 选 Workflows 必须额外写：为什么不能 Service 原生或 as_tool 解决

## Negative Examples栏（口头讲，不要求跑） / 反例栏（口头讲，不要求跑）
HandoffService 手写模式：plan v1 旧路径，多 agent 状态机自己写——已废，因为 Agent Service 原生覆盖了 80% 场景

## Constraints / 约束
- 主路径必须真跑通（不准只看讲师演示）
- as_tool / Workflows 不要求跑通，但学员必须能口头讲清"这两种相比主路径多/少什么"

## Self-Verification / 自验证
- [ ] 主路径 trace 看到三段（orchestrator → 专家 1 → 专家 2）
- [ ] 决策卡三问全答
- [ ] 能讲出为什么不选另外两种
