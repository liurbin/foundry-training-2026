> 抽自 docs/01-instructor-handbook-v2.md D10 模块；同步规则见 docs/02-instructor-prep-checklist.md

# 让 AI 帮我对照 Foundry 能力边界表，找出我项目命中的边界

## 输入
- plan 第五·五能力地图 + 本节边界表（讲师 Day3 发）
- 我项目 D2 / D6a 决策卡产物

## 边界表（讲师当天发实物，学员对照勾选）
> 13 个能力域与 plan 五·五能力地图一一对应（镜像）；plan 改 → 本表同步改。
> "验证来源"列由讲师 Day-7 填实（官方文档 URL / portal 截图 / fork 实测 三选一）；未验证假设只能列脚注、不进主表、不作为课堂边界结论。

| 能力域 | Foundry 的边界（不能做 / 有限制） | 验证来源 | 命中？ | 迁移方案 |
|--------|--------------------------------|---------|--------|----------|
| Agent Service | 自定义控制流 / 复杂状态机受限 | TODO（Day-7） | [ ] | 切 SDK 路径（D6a） |
| Workflows | visual designer 的版本管理 / code review 不友好 | TODO（Day-7） | [ ] | 用 Agent Service 原生编排或 SDK 自写状态机 |
| Projects | 跨 project 资源共享 / 迁移粒度 | TODO（Day-7） | [ ] | … |
| Connections | 第三方凭证类型覆盖 / 轮换支持 | TODO（Day-7） | [ ] | … |
| Identity | RBAC 粒度 / 跨租户访问 | TODO（Day-7） | [ ] | … |
| Models | 模型目录外的模型支持有限 / 滞后 | TODO（Day-7） | [ ] | … |
| Evaluations / Red Team | 内置 attack set 覆盖范围 / 自定义攻击集成 | TODO（Day-7） | [ ] | … |
| Tracing / Monitoring | 采样率 / 自定义维度 / 摄入成本 | TODO（Day-7） | [ ] | … |
| Deployment | Hosted Agents 外的部署目标支持 / 自托管（ACA）迁移代价 | TODO（Day-7） | [ ] | … |
| Quotas / Cost | TPM / RPM 配额上限 + 增配审批流程 | TODO（Day-7） | [ ] | … |
| SDK / Agent Framework | 与 Agent Service 的能力差 / 版本节奏 | TODO（Day-7） | [ ] | … |
| A2A | 协议成熟度 / 跨 vendor 互通验证 | TODO（Day-7） | [ ] | … |
| MCP | MCP server 集成限制（rebrand 期） | TODO（Day-7） | [ ] | … |

（如需补充：合规 / 数据驻留 / 多租户隔离粒度作为跨能力域的"非功能"边界，由讲师 Day-7 评估是否单列。）

## 让 AI 帮我做的事
1. 我项目命中的边界项打勾
2. 每命中一项，让 AI 给 2 个迁移方案备选
3. 我从备选里选 1 个 + 写出选择理由

## 约束
- 不准把"边界"当"缺点"——边界是中性的，关键是我项目是否命中
- 命中的项必须给迁移方案；没命中的项不要硬找

## 自验证
- [ ] 边界表 13 行全部判定（命中 / 未命中）
- [ ] 命中项都有迁移方案 + 理由
- [ ] 边界表"验证来源"列已由讲师填实（学员看到"TODO"应当反馈）
- [ ] 与 D1 决策卡一致（如果 D1 说"用 Foundry"但 D10 命中 ≥3 项关键边界，需要回去 review D1）
