# D9: 生产化 Checklist

> 讲 + 实操 + 评审 / 90 min（40 讲 / 30 实操 / 20 评审） / 凭证：学员侧阅读 + 填模板，不真部署

## 目标
- 走完一份生产化 checklist：事故 / 回滚、监控、成本采样、CI/CD（含红队 gate）
- 能在自己项目上对 checklist 每项判定"已有 / 部分 / 没有"，并给出最小补法
- 能说出红队 gate 在 pipeline 中的接入位置，以及 Azure DevOps 对照 GH Actions 的差异
- 能在 runbook 模板上填出至少 1 个具体事故场景

## 前置
- D3 单 agent demo 跑通（checklist 中"回滚单元 / Bicep diff"等项依赖 D3 产物）
- D8 红队 baseline 跑通（checklist 中"红队 gate 已接"项依赖 D8 产物）

## 子任务
1. [GH Actions workflow 走查](01.md) — 借鉴上游 Ex05；学员只读 + 标注关键步骤，不必真跑
2. [红队 gate 接入](02.md) — 上游没有，本课新增；在 GH Actions / Azure DevOps pipeline 哪一段挂 D8 红队脚本
3. [事故复盘案例阅读](03.md) — 讲师发脱敏案例，学员读 5 段 timeline 并标"哪步如果有 runbook 就不会炸"
4. [runbook 模板填写](04.md) — 在讲师模板上填 1 个事故场景（触发 → 谁响应 → 怎么定位 → 怎么回滚）
5. [Azure DevOps 对照 GH Actions 差异](05.md) — 学员选用哪条 + 为什么（写进 checklist 应用清单）
6. [生产化 checklist 应用清单](06.md) — 对 spec-d9 的 checklist 每项判定"已有 / 部分 / 没有" + 没有的项给最小补法

> **时长警告**：6 子任务塞满 90 min，零 buffer。如评审段超时，把 05（ADO vs GHA）合并到 06 内部讲，不要砍 04（runbook 填写）。

## 验收
- 学员产出的 checklist 应用清单**所有项都判定**，不留空
- "没有"的项必须有最小补法（不超过 1 周工作量），不接受"加强监控"这种空话
- **全没有 = 生产化预备状态，不阻塞**（项目尚早是合理状态，评审段标记"生产化预备"即可）
- runbook 模板上至少有 1 条具体事故场景的处置流程
- 能口头回答："如果今晚 alert 触发，谁接？怎么响应？"
- 能指出红队 gate 在 pipeline 中的接入位置（PR check / pre-deploy / post-deploy 三选）

## 凭证说明
- 学员侧：阅读 + 填模板；**不真部署**，不依赖真实 Foundry 凭证
- GH Actions：观看讲师演示，或自己 fork 试跑（不需 Azure 凭证；workflow 走 dry-run / skip deploy 步骤）
- 事故复盘案例：讲师发脱敏材料，学员只读不联网

## 上游素材
- Ex05 GH Actions（部署部分）—— 借用 workflow 骨架做走查
- 红队 gate / 事故复盘 / runbook 模板 / Azure DevOps 对照表 —— 上游无，v2 自写

## 参考
- 讲师手册：../../../docs/01-instructor-handbook-v2.md（D9 章节）
- 训练计划：../../../docs/00-training-plan-v2.md（D9 行）
- Fork 映射：../../../docs/03-workshop-fork-mapping.md（D9 标记 🟡 部分复用）
- prompt spec：../../../prep-artifacts/day-7/specs/spec-d9-prod-checklist.md
