# Ask AI to Run a Foundry Single Agent (Bicep + agent_reference)

> Bilingual mirror. Original source: `prep-artifacts/day-7/specs/spec-d3-single-agent.md`.

## English Guide

This is the bilingual mirror for a prompt spec or decision card. Use the English heading for discovery, then rely on the full Chinese source below for the exact template, constraints, and self-verification checklist.

- Chinese canonical title: 让 AI 帮我跑通 Foundry 单 agent（Bicep + agent_reference）
- English navigation title: Ask AI to Run a Foundry Single Agent (Bicep + agent_reference)
- Scope: this page is part of the full bilingual Foundry training site.

## Chinese Source with Bilingual Headings

> 抽自 docs/01-instructor-handbook-v2.md D3 模块；同步规则见 docs/02-instructor-prep-checklist.md

# Ask AI to Run a Foundry Single Agent (Bicep + agent_reference) / 让 AI 帮我跑通 Foundry 单 agent（Bicep + agent_reference）

## Goals / 目标
在我的 Foundry project 里部署一个最小 agent，从外部代码用 agent_reference 调起来，能返回。

## 输入（Learner现场填） / 输入（学员现场填）
- Foundry project 名：[…]
- Region：[…]
- 模型部署名：[…]
- 我要让 agent 做什么（一句话）：[…]
- 我用的语言 / SDK：[Python / .NET / TS …]

## 让 AI 生成的产物Checklist / 让 AI 生成的产物清单
1. Bicep 模板（创建 agent + connection）
2. 部署脚本（az deployment …）
3. 用 agent_reference 调 agent 的最小代码
4. 一次成功调用的 trace 链接（学员自己跑后贴）

## 约束（告诉 AI 必须遵守）
- 不要 hardcode 任何 secret，必须用 Key Vault 引用或 env
- 不要用 deprecated API（讲师当天给出 rebrand 期已知漂移清单）
- Bicep 必须用 module 化，不写成单文件 200 行
- 调用代码必须捕获 429 + 5xx 并打日志（具体重试策略放 D5）

## 观测前置（影响验收第 3 条）
- 确认 project 已接 Application Insights / tracing 开关（讲师 Day1 上午统一确认 1 次）
- 如果 project 未启用 tracing：本模块"trace 链接"验收转为可选，留到 D5/D9 补；学员不应被卡在观测配置问题上

## Self-Verification / 自验证
- [ ] az deployment 成功无 error
- [ ] 调用返回 200 且文本非空
- [ ] portal 能看到本次调用 trace
