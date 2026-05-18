# Ask AI to Run Minimal A2A and MCP Demos, Then Overlay Them

> Bilingual mirror. Original source: `prep-artifacts/day-7/specs/spec-d6b-a2a-mcp.md`.

## English Guide

This is the bilingual mirror for a prompt spec or decision card. Use the English heading for discovery, then rely on the full Chinese source below for the exact template, constraints, and self-verification checklist.

- Chinese canonical title: 让 AI 帮我跑通 A2A 和 MCP 两个最小 demo，再叠加
- English navigation title: Ask AI to Run Minimal A2A and MCP Demos, Then Overlay Them
- Scope: this page is part of the full bilingual Foundry training site.

## Chinese Source with Bilingual Headings

> 抽自 docs/01-instructor-handbook-v2.md D6b 模块；同步规则见 docs/02-instructor-prep-checklist.md

# Ask AI to Run Minimal A2A and MCP Demos, Then Overlay Them / 让 AI 帮我跑通 A2A 和 MCP 两个最小 demo，再叠加

## Goals / 目标
分别理解 A2A（agent ↔ agent）和 MCP（agent → 工具）的边界；叠加场景能复现真实多 agent + 工具集成。

## 让 AI 生成的产物Checklist / 让 AI 生成的产物清单
1. A2A 最小 demo：两个 agent 互相调用（不准用同进程函数调用伪装）
2. MCP 最小 demo：一个 agent 调一个 MCP server 提供的 tool
3. 叠加 demo：在 #1 基础上，给其中一个 agent 加一个 MCP tool
4. "A2A vs MCP 选型"决策卡

## Decision Card四问 / 决策卡四问
- 我要让两个独立 agent 协作（各自有 LLM）？ → A2A
- 我要让一个 agent 调结构化工具/资源？ → MCP
- 既要又要？ → 叠加（但要算成本，见下）
- 都不要（单 agent 直接 function call 够）？ → 不引入，写明拒绝理由

## 成本影响（Decision Card必填） / 成本影响（决策卡必填）
- A2A：多一次 agent 调用 = 多一倍 token + 一跳延迟
- MCP：多一个 server 进程 / 网络跳；tool schema 进 prompt 也占 token
[我这个 demo 引入 A2A/MCP 后，每次请求 token 增加估算：_]

## Constraints / 约束
- A2A 两个 agent 不准同进程函数调用伪装——必须走 A2A 协议
- MCP tool 不准只 echo 输入——至少有一次真实外部副作用（HTTP / 文件 / 计算）
- 叠加 demo 必须能 trace 到"agent A → agent B → MCP tool"完整链路

## Fallback（rebrand 期漂移高发，留兜底）
- A2A 和 MCP 至少**学员本机跑通 1 个**；另 1 个可用讲师 prepared repo + trace 对照
- 叠加 demo 跑不通**不阻塞**"A2A vs MCP 边界判断"的验收——决策卡填实即可
- 真实跑通两条 + 叠加 = 课堂目标；只跑通 1 条 + 决策卡 = 验收过线

## Self-Verification / 自验证
- [ ] 三个 demo 各自能跑（不互相依赖才算）
- [ ] 叠加 demo 链路 trace 看得到三段
- [ ] 决策卡四问全答 + token 增量估算非空
