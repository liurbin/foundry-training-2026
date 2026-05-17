# D7: 多 agent 编排三选一

> 时长 120 min（50 讲 / 50 实操 / 20 评审） · 主路径需 Foundry 端点（或讲师共享 / mock），对照路径仅本机

## 目标
- 理解三种编排路径的取舍：Agent Service 原生 / `as_tool` / Workflows
- 主路径（Agent Service 原生）AI-pair 跑通 orchestrator → 专家 1 → 专家 2
- 对 as_tool 与 Workflows 的差异能口头讲清，不要求三种全跑通
- 产出"多 agent 三选一"决策卡，并显式拒绝 HandoffService 手写状态机这条已废路径

## 前置
- D3 单 agent 跑通（Agent Service + Bicep + trace 三段都看过）
- D6a/D6b 看过 SDK / A2A / MCP 边界（理解"多 agent ≠ 一定要 A2A"）
- 本机已具备 D3 的运行环境与凭证；如无 Foundry 端点，准备走讲师共享端点或 mock

## 子任务
1. [主路径：Agent Service 原生](01.md) — AI-pair 生成 orchestrator + 两个专家 agent，跑通三段 trace
2. [对照路径 A：as_tool](02.md) — 在主路径代码上 apply 讲师 prepared diff，对比差异
3. [对照路径 B：Workflows 录屏](03.md) — 看 10-15 min visual designer 录屏 + 一次完整运行 trace
4. [三路径选型决策](04.md) — 填"三选一"决策卡，回答三问 + 拒绝 HandoffService 反例

## 验收
- 主路径 trace 三段完整（orchestrator → 专家 1 → 专家 2），讲师当场看 trace；跑不通则观看讲师演示并记录卡点
- 能 apply as_tool diff 并口头讲清与主路径的本质差异（控制流、可测性、状态归属）
- 看完 Workflows 录屏能说出 1 个适用场景（复杂分支 / 长时间运行 / 非工程师可视化）+ 1 个不适用场景（80% 简单编排）
- 决策卡三问全答，且选择与答案一致；若选 Workflows / as_tool，必须答出"为什么不用主路径"
- 能显式拒绝"重写 HandoffService 手写状态机"这条 AI 可能推荐的旧路径

## 凭证说明
- 主路径：需 Foundry 项目 + Agent Service 端点；无端点学员走讲师共享端点或 mock，trace 看讲师截图兜底
- as_tool：纯代码 diff，本机 apply 即可，不需要额外凭证
- Workflows：录屏观看，无需 portal 访问；课后想自己玩需 Foundry portal 权限

## 上游素材
- Ex02 multi-agent（仅展示一种路径） — 主路径参考起点
- as_tool diff / Workflows 录屏为 v2 新增对照素材（讲师 Day-7 准备清单）

## 参考
- plan v2 §七 Day2 D7 行 + §五·五能力地图 Workflows 行
- 讲师手册 v2 §D7（spec / negative examples / 验收 / 讲师准备清单）
- fork mapping §D7（🟡 上游 Ex02 单一路径，对照需自补）
- 反例口头讲：HandoffService 手写模式（plan v1 旧路径，已废）
