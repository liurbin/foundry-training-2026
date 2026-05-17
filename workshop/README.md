# Microsoft Foundry 3-Day Workshop

> 面向工程师的 Microsoft Foundry 实战培训，3 天 11 模块，决策驱动 + 平台路径 + 生产化。
> 上游参考：[microsoft/TechWorkshop-L300-AI-Apps-and-agents](https://microsoft.github.io/TechWorkshop-L300-AI-Apps-and-agents/)（MIT）。
> 课程设计源：`../docs/00-training-plan-v2.md`；讲师手册：`../docs/01-instructor-handbook-v2.md`。

## 适用对象

- 已有 Python / 云开发基础
- 想把 LLM agent 真正交付到生产、而不是停在 demo
- 团队即将或已经在用 Microsoft Foundry

## 学完能做到

1. 在"用 Agent Service 还是 SDK"这种平台选型上**有判据**
2. 单 / 多 agent 都能跑通端到端（含 tracing / 观测 / 红队 baseline）
3. 知道 Foundry **能做什么、不能做什么**（13 个能力域的边界）
4. 把 AI-pair 编程接入团队工作流，而不是单点炫技

## 凭证假设

学员侧**不要求**自带 Azure 订阅。所有需要真实 Azure / Foundry 的步骤由讲师演示，学员用 mock provider / stub / sample JSON 完成验收。
讲师侧的环境准备见 `../docs/02-instructor-prep-checklist.md`。

## 课程地图

> 时长以 plan v2 第六/七/八节为准。如有出入以 plan 为准。

| Day | 模块 | 时长 | 类型 |
|-----|------|------|------|
| 1 | [D1 概念 + 决策框架](workshop/d01_concepts/) | 45 min | 决策 |
| 1 | [D2 Agent Service vs SDK](workshop/d02_agent_vs_sdk/) | 90 min | 决策 |
| 1 | [D3 单 agent 平台路径](workshop/d03_single_agent/) | 120 min（跨午饭） | 实操 |
| 1 | [D4 Provider 抽象](workshop/d04_provider_abstraction/) | 90 min | 实操 |
| 1 | [D5 Scaling + Cost](workshop/d05_scaling_cost/) | 90 min | 实操 |
| 2 | [D6a Agent Framework SDK 的边界](workshop/d06a_sdk_boundary/) | 60 min | 决策 + 实操 |
| 2 | [D6b A2A + MCP 边界 + 叠加](workshop/d06b_a2a_mcp/) | 60 min 主段 + 45 min 叠加段 | 实操 |
| 2 | [D7 多 agent 编排三选一](workshop/d07_multi_agent/) | 120 min | 实操 |
| 2 | [D8 红队 Baseline](workshop/d08_red_team/) | 105 min | 实操 |
| 3 | [D9 生产化 Checklist](workshop/d09_production/) | 90 min | 决策 |
| 3 | [D10 Foundry 能力边界表](workshop/d10_boundary/) | 60 min | 决策 |
| 3 | [D11 AI-pair 工作流](workshop/d11_ai_pair/) | 35 min | 决策 + 实操 |
| 3 | 综合作业实做 + 演示评分 + 成本回顾 + 结业 | 145 + 60 + 30 + 30 min | 5 维度 rubric |

## 综合作业评分（5 维度）

| 维度 | 权重 |
|------|------|
| 跑通 | 25% |
| 选型 | 25% |
| 红队 | 20% |
| 生产化 | 15% |
| AI-pair | 15% |

## 仓库结构

```
workshop/
├── README.md                # 本文件
├── docs/
│   ├── d01_concepts/        # 每个模块一个目录
│   │   ├── README.md        # 模块概览
│   │   ├── 01.md            # 子任务 1
│   │   └── ...
│   ├── d02_agent_vs_sdk/
│   └── ...
├── code/                    # 学员可拷走的 mock / stub / sample 代码
└── infra/                   # Bicep 模板（讲师演示用）
```

## 上游素材归属

本 workshop 部分素材（Bicep 模板结构、A2A server 实现思路、红队 SDK 调用模式）参考自 [microsoft/TechWorkshop-L300-AI-Apps-and-agents](https://github.com/microsoft/TechWorkshop-L300-AI-Apps-and-agents)，MIT License。完整归属见 [`THIRD_PARTY_NOTICES.md`](https://github.com/your-org/foundry-training-2026/blob/main/workshop/THIRD_PARTY_NOTICES.md)。
