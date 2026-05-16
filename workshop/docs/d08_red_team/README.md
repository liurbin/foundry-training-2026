# D8: 红队 Baseline

> 时长 105 min（30 讲 / 50 实操 / 25 评审）｜Day 2 下午
> 凭证要求：Portal 讲师演示即可；SDK 学员本机真跑，跑不通用讲师提供的 sample JSON 兜底

## 目标
- 跑通一次红队 baseline，理解 ASR（Attack Success Rate）指标怎么读
- 能区分 false positive（工具误判"成功"）vs 真问题
- 理解"红队是 gate，不是 checkbox"——模型/prompt/工具变了都要重跑

## 前置
- D3 单 agent（作为被测对象；也可换 D6a/D6b 的 agent）
- 业务可接受的 ASR 上限（学员自己定，必须 < 100%）

## 子任务
1. [Portal 红队 baseline 观看](01.md) — 讲师演示，`num_objectives=3` 起步，看一次端到端
2. [SDK 红队跑一次](02.md) — 学员本机或讲师共享凭证，同 agent 同 attack set，对比 Portal 结果
3. [SDK 跑超时的 fallback](03.md) — 50 min 内跑不通则用讲师 sample JSON 完成 baseline 报告结构（真跑转课后）
4. [结果分析与 false positive 识别](04.md) — 按攻击类型分类 + Top 3 失败 case 人工 review

## 验收
- 能解读 ASR 数字（如 "23.4%" 是什么意思、和业务阈值怎么比）
- 能从结果中识别至少 1 个 false positive 类型，并说出为什么是误判
- 能产出 baseline 报告：真跑 SDK 或用 sample JSON 拼出来，必须有具体数字、≥ 2-3 个攻击类型分类、Top 3 失败 case 处置决策
- Portal 和 SDK 的 ASR 量级一致（差 ≤ 2x 算合理）

## D8 子 rubric（红队 20% 内部如何打分）
- baseline 报告完整度（ASR 数字 / 攻击分类 / Top 3 case）
- false positive 识别能力（能说出 1 个具体类型 + 判定理由）
- CI/CD gate 设计（3 条规则全填、阈值与业务可接受 ASR 一致）
- 详见讲师手册 D8 章节

## 凭证说明
- **Portal**：讲师演示，学员看流程；不要求每人当场跑
- **SDK**：学员真跑；跑不通用讲师 sample JSON 完成 baseline 报告结构
- **已知坑**：某类攻击 false positive 高发（讲师手册有清单）；单次 baseline 耗时长，`num_objectives` 设大容易超 50 min 实操窗口

## 上游素材
- Ex06：UI + SDK + 自定义 attack，是上游最强复用模块（🟢 基本照搬）
- 本模块只在上游基础上补：D8 子 rubric + SDK 超时 sample JSON fallback

## 参考
- 训练计划 v2 D8 行（`docs/00-training-plan-v2.md`）
- 讲师手册 D8 章节（`../../../docs/01-instructor-handbook-v2.md` "D8 — 红队作为上线门槛"）
- Fork 映射表 D8 行（`../../../docs/03-workshop-fork-mapping.md`）
- spec 文件：[../../../prep-artifacts/day-7/specs/spec-d8-redteam-gate.md](../../../prep-artifacts/day-7/specs/spec-d8-redteam-gate.md)
