# Ask AI to Apply the Production Checklist to My Project

> Bilingual mirror. Original source: `prep-artifacts/day-7/specs/spec-d9-prod-checklist.md`.

## English Guide

This is the bilingual mirror for a prompt spec or decision card. Use the English heading for discovery, then rely on the full Chinese source below for the exact template, constraints, and self-verification checklist.

- Chinese canonical title: 让 AI 帮我把生产化 checklist 应用到我项目
- English navigation title: Ask AI to Apply the Production Checklist to My Project
- Scope: this page is part of the full bilingual Foundry training site.

## Chinese Source with Bilingual Headings

> 抽自 docs/01-instructor-handbook-v2.md D9 模块；同步规则见 docs/02-instructor-prep-checklist.md

# Ask AI to Apply the Production Checklist to My Project / 让 AI 帮我把生产化 checklist 应用到我项目

## Inputs / 输入
- 我项目当前状态（来自 D3/D5/D6a/b 的产物）
- 业务可接受的事故级别 SLO（例：单次事故 ≤ 30min 恢复 / 月度可用率 ≥ 99.5%）

## checklist（Instructor Day3 上午统一发，Learner逐项打勾 + 写差距） / checklist（讲师 Day3 上午统一发，学员逐项打勾 + 写差距）

### 事故 / 回滚
- [ ] 有 runbook（事故触发 → 谁响应 → 怎么定位 → 怎么回滚）
- [ ] 回滚单元明确（agent 版本？Bicep stack？模型版本？）
- [ ] 上一次 deploy 的回滚命令现在能否一行跑通

### 监控
- [ ] 三个核心指标接 alert：错误率 / p95 延迟 / 月度成本预算（**阈值从 SLO 反推**，不接受拍脑袋数字）
- [ ] alert 接到真人（不是只发邮件到 noreply）
- [ ] trace 采样率合理（100% 烧钱，10% 找不到长尾）

### 成本采样
- [ ] 每天有自动报表（cost-per-call / cost-per-DAU）
- [ ] 预算超阈值触发硬动作（不是只发邮件）

### CI/CD
- [ ] D8 红队 gate 已接（或明确计划接的时间）
- [ ] Bicep diff 必须人审才能 apply
- [ ] Azure DevOps / GH Actions 对照表（学员选用哪条 + 为什么）

## What to Ask AI To Do / 让 AI 帮我做的事
1. 把 checklist 每项转成"我项目当前状态：已有 / 部分 / 没有"
2. 没有的项给出最小补法（不超过 1 周工作量）
3. 输出"我项目离生产化还差几项"清单

## Constraints / 约束
- 不准让 AI 帮你"以后补"——每项必须有明确"已有 / 部分 / 没有"判定
- 部分 / 没有的项必须给具体补法，不接受"加强监控"这种空话

## Self-Verification / 自验证
- [ ] checklist 所有项都判定（不留空）
- [ ] 没有 / 部分的项都有最小补法
- [ ] 能口头讲清"我项目离上线还差几项 + 哪项最关键"
