> 抽自 docs/01-instructor-handbook-v2.md D8 模块；同步规则见 docs/02-instructor-prep-checklist.md

# 让 AI 帮我跑红队 baseline + 设计上线门槛

## 输入
- 一个被测 agent（D3 或 D6a/b 任选一个）
- 业务可接受的 ASR 上限（Attack Success Rate；学员自己定，必须 < 100%）

## 产品口径（2026 当前，讲师必须先和学员讲清）
- 微软现在有两个 Red Teaming Agent：
  1. **云端 Red Teaming Agent**（Foundry 内置）—— 唯一支持把 **Foundry Agents 当 target** 的路径；本课走这条
  2. 本地 PyRIT-based Red Teaming Agent —— **不兼容** Foundry new portal/SDK；本课不用，只在边界澄清时提一下
- 学员真跑走 SDK（指向云端 Red Teaming Agent，target = D3/D6a/b 的 Foundry agent）
- Portal 路径作为讲师演示视图，让学员看一次端到端结果如何呈现；**学员不要求每人当场在 portal 里跑**

## 让 AI 生成的产物清单
1. 看一次讲师 portal 演示（num_objectives=3 起步），理解结果界面 + ASR 数字读法
2. SDK 跑一次云端红队（同 agent 同 attack set），拿到自己的结果 JSON
3. baseline 报告：ASR、按攻击类型分类、Top 3 失败 case
4. CI/CD 接入设计稿（不要求实接，画一张图 + 写 3 条 gate 规则）

## CI/CD gate 设计模板
- gate A：ASR > X% 阻塞 merge
- gate B：新增攻击类型失败率 > Y% 报警
- gate C：[学员自定义]

## 约束
- SDK 必须学员自己跑（target = 自己的 Foundry agent）；portal 是讲师演示，不要求每人当场跑
- baseline 报告必须有数字，不接受"看起来还行"
- Top 3 失败 case 必须人工 review（红队工具能找 case，判定要不要修是人的活）

## Fallback（SDK 跑超时时）
- 若 50min 内 SDK 跑不通：至少完成 SDK 命令 + 配置文件 + 用讲师 sample JSON 完成 baseline 报告结构
- 真实跑通 SDK 转课后 / 综合作业加分项
- portal 由讲师演示完成，不存在"portal 跑不通"的学员场景

## 自验证
- [ ] SDK 跑出的 ASR 是具体数字，且与讲师 portal 演示的量级一致（差 ≤ 2x 算合理）
- [ ] baseline 报告含至少 2-3 个攻击类型分类（取决于 attack set；不足 3 类需在报告说明覆盖缺口及下一步补法）
- [ ] CI/CD gate 3 条规则全填，能给具体阈值
- [ ] Top 3 失败 case 学员能口头判定"修 / 不修 / 加 system prompt 兜底"
