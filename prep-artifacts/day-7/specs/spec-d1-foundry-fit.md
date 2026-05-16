> 抽自 docs/01-instructor-handbook-v2.md D1 模块；同步规则见 docs/02-instructor-prep-checklist.md

# 我的项目：是否用 Foundry 决策卡

## 项目一句话描述
（业务目标 + 当前阶段，1 行）

## 决策维度勾选
- [ ] 我需要托管 agent 运行时 + 状态管理 → 倾向 Foundry
- [ ] 我需要 Azure 生态（AAD / Key Vault / App Insights）原生集成 → 倾向 Foundry
- [ ] 我有合规/数据驻留要求（金融、医疗、政企）→ 倾向 Foundry
- [ ] 我需要 portal 上让非工程师配 agent / 看 trace → 倾向 Foundry
- [ ] 我只需要单次 LLM call，无 agent 概念 → 不用 Foundry
- [ ] 我的核心模型在 Azure 目录外（Claude / Gemini / 自托管）且不打算切 → 不用 Foundry
- [ ] 我做的是研究 demo / hackathon，下周扔 → 不用 Foundry
- [ ] 我已经有成熟 LangGraph / CrewAI 生产栈，无迁移动机 → 不用 Foundry

## 结论
[用 / 不用 / 部分用]

## 部分用的话，哪一部分？
（对照五·五能力地图：只用 Evaluations？只用 Models？只用 Agent Service 但 SDK 路径？）

## 我不确定的地方
（这一栏讲师评审段必看）
