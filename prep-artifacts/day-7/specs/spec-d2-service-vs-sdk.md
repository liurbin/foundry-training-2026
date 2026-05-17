> 抽自 docs/01-instructor-handbook-v2.md D2 模块；同步规则见 docs/02-instructor-prep-checklist.md

# Agent Service vs Agent Framework SDK 选型决策卡

## 上下文
- 项目：[一句话]
- 团队规模：[人数 + AI 熟手占比]
- 是否需要非工程师在 portal 配 agent：[是/否]

## 四个维度打分（1-5，5 = 强需求）
| 维度 | 分 | 说明 |
|------|----|----|
| 托管运行时（不想自己跑 worker） | _ | |
| portal 可视化（PM/SA 直接配） | _ | |
| 代码完全控制（自定义编排 / 自定义状态） | _ | |
| 跨 provider 移植性 | _ | |

## 决策规则（讲师给的启发式）
- 前两项 ≥ 后两项 → Agent Service
- 后两项 ≥ 前两项 → SDK
- 接近 → 混合（Service 跑入口 agent，SDK 跑专家 agent）

## 硬约束触发条件（部署与容量是选型的输入，不是输出）
> 硬约束**优先于**四维度打分检查。其中：
> - 私有部署 / 网络隔离 / 最少运维 → **可直接覆盖打分**（决定 Service vs SDK / Hosted vs self-host）
> - 容量类约束（高吞吐 SLA / 预算敏感）→ **作为额外决策输入**带进 D5 capacity planning，与 Service/SDK 选型正交

| 触发条件 | 选型方向 | 备注 |
|---------|---------|------|
| 客户/合规要求私有部署 / 自带云 / 跨云 | SDK | Agent Service 是 Foundry 托管，无法搬出去 |
| 高吞吐 + 稳定 SLA | 必须做 capacity planning；PAYG 不一定够，需评估 quota increase / PTU / reservation | 与 Service/SDK 选型正交——两条路径都要面对 |
| 网络隔离（VNet / 私有 endpoint） | Hosted Agents 看 VNet 集成能力 vs SDK self-host（ACA/AKS）自己接 | D5 展开 |
| 最少运维 / 没人值班 | Agent Service + Hosted Agents | 自托管 SDK 第一个 incident 就吃掉价差 |
| 预算敏感 + 流量稳定可预测 | 评估 reservation / PTU 是否比 PAYG 划算 | 流量不可预测则反过来：PAYG + cache 更安全 |

## 我的选择 + 理由（≥3 句）
[…]

## 成本影响
- Agent Service：托管费 + 平台调用费
- SDK：自托管运行时（Container Apps / 自己 VM）+ 模型调用费

### 估算输入（必填，不接受"差不多"）
| 项 | 值 |
|----|----|
| 日请求量（DAU × 人均次数） | _ |
| 平均输入 token / 输出 token | _ / _ |
| 并发峰值（QPS） | _ |
| 是否需要 7×24 on-call | 是 / 否 |
| 运行时规格（SDK 路径才填，如 Container App 2vCPU/4GB×N 实例） | _ |

[我这个项目，哪一边总成本低？给出数量级（$/月）和主导成本项]

## 我没想清楚的地方
[…]
