> 抽自 docs/01-instructor-handbook-v2.md D11 模块；同步规则见 docs/02-instructor-prep-checklist.md

# 团队 spec 模板库搭建指南（讲师演示用）

## 目录结构（推荐起步）
```
team-specs/
├── README.md              # 本库怎么用、怎么贡献、怎么 review
├── decision-cards/        # 决策卡模板（来自 D1/D2/D6a/D7/D10）
│   ├── foundry-fit.md
│   ├── service-vs-sdk.md
│   └── ...
├── implementation/        # 实现 spec（来自 D3/D4/D5/D6b/D8/D9）
│   ├── single-agent.md
│   ├── provider-abstraction.md
│   └── ...
├── negative-examples/     # 反例库（持续更新）
└── runbooks/              # D9 runbook 模板
```

## 2 个示例 spec 大纲（学员誊抄/裁剪）

### 示例 1：新 agent 上线 spec（基于 D3 + D5 + D9）
- 业务输入：场景 / SLO / 成本预算
- 必填决策：Service vs SDK / provider / 编排模式
- 必交产物：Bicep / 重试策略 / 监控接入 / runbook
- 验收 gate：红队 ASR 阈值 / 成本估算 / checklist 完成度

### 示例 2：新 provider 接入 spec（基于 D4）
- 接口契约（ChatProvider Protocol）
- 必填字段 vs opts 透传规则
- 单测要求（mock provider 必有）
- review checklist（不准污染接口 / 不准超 1 个 if 分支）

## MCP 接 Foundry 的工作流（plan 已说明的两条路径）
- **若 Foundry MCP server 可用**：现场连接演示，学员看 Claude/Cursor 直接读 Foundry 文档
- **若不可用**：讲 Learn URL / SDK docs / portal evidence 喂给 AI 的替代工作流（手动 prompt 模板）

## 团队 spec 库治理
- 谁可以提 spec：所有人
- 谁审 spec：1 个核心维护者 + 1 个使用方
- 反例库怎么更新：每次出事故 → review 是否漏在 spec → 加反例；或新模块/新 provider 上线时主动梳理一轮
- 多久 review 一次全库：季度 + 大模型升级时
