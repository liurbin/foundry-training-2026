> 抽自 docs/01-instructor-handbook-v2.md D5 模块；同步规则见 docs/02-instructor-prep-checklist.md

# 让 AI 帮我把 D3 的单 agent 部署到 Hosted Agents（主路径），并补 429 重试 + 缓存 + 成本估算；ACA 仅作对照

## 部署路径分层（开课前讲师必须先讲清）
- **主路径 = Foundry Hosted Agents**（new backend，托管容器，scale-to-zero，15 min idle 后释放）
- **对照路径 = Container Apps 自托管**（走旧 `azd ai agent` 模板）：仅作"自托管时你要操心什么"对照，不作为学员部署目标
- "min replicas ≥ 1"是 ACA 段的硬约束，**不适用 Hosted Agents**

## 前置 15 min：部署与容量模式对照（D5 开场必讲）
> 这 15 min 是 D2 选型决策卡里"硬约束触发条件"栏的实操展开。学员在 D2 已经知道这些维度的存在，D5 这里把维度的实际选项摊开。

### 部署目标对照（agent 运行时跑在哪）
| 模式 | 何时选 | 学员要操心什么 |
|------|-------|---------------|
| **Foundry Hosted Agents**（主路径） | 默认选 | 几乎不用操心，scale-to-zero 默认 |
| Container Apps 自托管 | 必须自托管 / VNet 强约束 / 客户私有 Azure | min replicas、镜像、滚动升级 |
| SDK self-host（AKS / App Service / VM） | 跨云 / 客户自带 K8s / 真私有部署 | 全套 K8s 运维 + 自接观测 |

### 容量模式对照（token 配额怎么买）
| 模式 | 何时选 | 备注 |
|------|-------|------|
| **PAYG + 默认配额**（主路径） | 默认；流量不可预测；POC / 中小规模 | 触发 429 → 加 retry + cache 即可，多数场景够用 |
| Quota increase（PAYG 配额增配） | 流量上涨但仍有抖动；不想买 commitment | 走审批流程，区域 + 模型有上限 |
| PTU / Provisioned Throughput | 高吞吐 + 稳定 SLA + 流量可预测 | 买的是"保留吞吐"，按月起买；区域 + 模型限制更多 |
| Reservation | 长期稳定用量 + 财务上要锁价 | commitment 期限 ≥ 1 年；和 PTU 正交 |

> **超时兜底**：若 Day-7 跑通时发现 15 min 不够，把容量模式压缩为 2 类讲（PAYG / dedicated），把 quota increase / PTU / reservation 作为 dedicated 的子项一句话带过，确保部署目标 3 选 1 一定讲完。

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
- [ ] 已交 deployment/capacity decision note：部署目标 + 容量模式各 1 选 + 为什么不选其他（每条 ≥1 句理由）
- [ ] 用 stub / 讲师提供的 replay response 注入 429，观测到重试 + jitter 行为正确（不抛业务层）
- [ ] 真实 100 RPS × 5min 压测为**可选**（讲师统一演示或录屏；真跑由讲师侧执行，避免学员触发共享配额）
- [ ] 缓存命中率 > 0（说明缓存真的接进去了）
- [ ] 成本估算的 best/worst 差 ≤ 3x（否则假设太松）
