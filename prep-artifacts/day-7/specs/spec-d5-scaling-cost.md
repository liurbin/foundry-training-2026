> 抽自 docs/01-instructor-handbook-v2.md D5 模块；同步规则见 docs/02-instructor-prep-checklist.md

# 让 AI 帮我把 D3 的单 agent 部署到 Hosted Agents（主路径），并补 429 重试 + 缓存 + 成本估算；ACA 仅作对照

## 部署路径分层（开课前讲师必须先讲清）
- **主路径 = Foundry Hosted Agents**（new backend，托管容器，scale-to-zero，15 min idle 后释放）
- **对照路径 = Container Apps 自托管**（走旧 `azd ai agent` 模板）：仅作"自托管时你要操心什么"对照，不作为学员部署目标
- "min replicas ≥ 1"是 ACA 段的硬约束，**不适用 Hosted Agents**

## 输入
- 来自 D2 成本估算表：日请求量 / 平均 token / QPS（直接搬过来）
- 来自 D3：可调用的 Foundry agent + agent_reference 代码
- 目标 SLO：[p95 延迟 / 月度可用率，至少给一个数]

## 让 AI 生成的产物清单
1. Hosted Agents 部署配置（主路径；scale-to-zero 默认，15 min idle 释放）
2. （对照视角，可选）ACA 自托管 Bicep 骨架：含 min/max replicas + scale rules——讲清为什么自托管要踩 min replicas ≥ 1
3. 429 + 5xx 重试策略（带 jitter 的指数退避，不允许无脑 retry-once；Retry-After 视为硬下界）
4. 一层缓存（按 prompt+model hash，TTL 学员定，写清楚为什么这个 TTL）
5. 成本估算脚本：输入 DAU/QPS → 输出月度 $ 上下限（模型费 + 运行时费 + 缓存命中率影响）
6. TPM/RPM 配额对照：估算的 token/min 是否超 D1 prep 时确认的配额

## 约束
- **主路径（Hosted Agents）**：使用产品默认 scale-to-zero；冷启动取舍由 SLO 决定要不要做保活探针，不要自己写 min replicas 限制
- **对照路径（ACA 自托管）**：如果选自托管，min replicas 不准为 0（冷启动 + 第一次 429 会同时炸）
- 重试上限明确写死（默认 3 次），不准无限重试
- 缓存键不准包含 user_id / 个人数据（合规雷区）
- 成本估算必须给区间（best/worst），不准给单点数字

## 自验证
- [ ] 用 stub / 讲师提供的 replay response 注入 429，观测到重试 + jitter 行为正确（不抛业务层）
- [ ] 真实 100 RPS × 5min 压测为**可选**（讲师统一演示或录屏；真跑由讲师侧执行，避免学员触发共享配额）
- [ ] 缓存命中率 > 0（说明缓存真的接进去了）
- [ ] 成本估算的 best/worst 差 ≤ 3x（否则假设太松）
