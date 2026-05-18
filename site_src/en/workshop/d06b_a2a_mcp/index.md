# D6b: A2A + MCP Overlay

> Bilingual mirror. Original source: `workshop/docs/d06b_a2a_mcp/index.md`.

## English Guide

This is the learner-facing bilingual mirror for the workshop page. The English heading and guide identify the task, while the Chinese source below preserves the complete original instructions, checklists, submissions, and references.

- Chinese canonical title: D6b: A2A + MCP 叠加
- English navigation title: D6b: A2A + MCP Overlay
- Scope: this page is part of the full bilingual Foundry training site.

## Chinese Source with Bilingual Headings

# D6b: A2A + MCP Overlay / D6b: A2A + MCP 叠加

> 时长：60 min 主段 + 衔接 45 min 叠加段（在 D6b 主段的 A2A demo 上加 MCP tool；产物归属 D6b）

## Goals / 目标
- 能讲清 MCP 与 tool calling 的区别：MCP 是跨进程的 tool/resource 协议，不是 prompt 里塞一段 function schema
- 能在 D6b 主段的 A2A 链路上挂一个真实有副作用的 MCP tool（本地文件读取 / HTTP / 计算，不准只 echo）
- 能在 trace 中识别 `agent A → agent B → MCP tool` 三段链路
- 能填"A2A vs MCP 选型"决策卡，含每次请求的 token / 延迟成本估算

## Prerequisites / 前置
- D6a 跑通（SDK 路径基础；本模块的 A2A / MCP demo 都跑在 SDK 上）
- 本模块主段 A2A demo 先于叠加段跑通（或学员侧切到讲师 prepared repo 看 trace）
- 本地能跑一个最小 MCP server（本地实现即可，不依赖远端）

## Subtasks / 子任务
1. [MCP 是什么、与 tool calling 的区别](01.md) — 协议层 vs prompt schema；为什么纯本地函数包成 MCP 是给自己加运维负担
2. [在 A2A 链路上挂 MCP tool](02.md) — 给本模块 A2A demo 的 agent B 加一个 MCP tool（本地文件读取作为最小副作用）
3. [trace 对照：A → B → MCP tool](03.md) — 三段链路必须在 trace 里能数出来；同进程函数调用伪装直接判负
4. [A2A vs MCP 决策卡 + 成本估算](04.md) — 四问 + token 增量栏必填，叠加 = 双倍成本 + 双倍故障面

## Acceptance Criteria / 验收
- A2A / MCP 至少**一条本机跑通**，另一条用 prepared repo / trace 对照（fallback 口径与 plan 一致，不要求 3 个 demo 都本机跑通）
- 能在 trace 中看出 `agent A → agent B → MCP tool` 完整链路（叠加 demo 跑通时）
- 叠加 demo 为课堂目标，**非必达验收**——只跑通 1 条 + 决策卡填实即过线
- 决策卡 token 增量栏有具体数字；学员能口头讲清"我综合作业场景会不会用 A2A / MCP"——选不用也算过

## Credential Notes / 凭证说明
- 学员侧：A2A 部分用本模块主段产出 / 讲师 prepared repo；MCP tool 用**本地实现**（如本地文件读取），不依赖任何远端 MCP server
- 不要求 Foundry MCP server 可用（rebrand 期漂移高发，本模块不押）
- 叠加 demo 跑不通不阻塞"A2A vs MCP 边界判断"的验收

## Upstream Materials / 上游素材
- Ex03 A2A 第一段（🟡 部分借用，对应 D6b 的 A2A 主段；D6a 用 Ex03 第一段建 SDK 基线，与本模块共享同一段上游素材）
- MCP 部分上游 fork 没有，本模块自写（最小本地 MCP server + 一个有副作用的 tool）

## References / 参考
- 链回 ../../handbook/01-instructor-handbook-v2.md#d6b--a2a--mcp-的边界
- 训练计划：../../handbook/00-training-plan-v2.md（D6b 行 + 11:45-12:30 衔接叠加段）
- Fork 映射：../../handbook/03-workshop-fork-mapping.md（D6b 标记 🟡 部分借 Ex03，MCP 部分上游无）
