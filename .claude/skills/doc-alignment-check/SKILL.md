---
name: doc-alignment-check
description: Cross-check the 5 core docs (plan v2 / handbook v2 / Day-7 checklist / fork-mapping / design principles) and 11 module specs for consistency. Use when the user edits any one of them and wants to verify the others still align — checks module count, durations, 5-dimension rubric, 🟢🟡🔴 fork tags, learner vs instructor scope, and Day-7 gating items.
disable-model-invocation: true
---

# doc-alignment-check

This repo's课程材料是分散在 5 份核心文档 + 11 个 spec 里的，互为引用。
改一处常常需要核对其他几处口径。这个 skill 把"该核对什么"打包成一份清单，
跑一次输出 diff 报告。

## 检查目标

权威源：

- `docs/00-training-plan-v2.md` — 课程设计源（11 模块 / 议程 / 5 维度评分 / 能力地图）
- `docs/01-instructor-handbook-v2.md` — 每模块 spec + negative examples + 验收
- `docs/02-instructor-prep-checklist.md` — Day-7 讲师准备物清单
- `docs/03-workshop-fork-mapping.md` — 上游 ↔ v2 对照（🟢/🟡/🔴）
- `docs/04-design-principles.md` — 设计原则
- `prep-artifacts/day-7/specs/spec-d{1..11}-*.md` — 从 handbook 抽出的 11 个独立 spec
- `workshop/docs/d{01..11}_*/` — 学员侧 12 模块 × 45 子任务（D6 拆 6a/6b）

不要读 v1（已冻结，且 PreToolUse hook 会拒写）：
`docs/00-training-plan.md`、`docs/02-instructor-manual.md`。

## 执行步骤

1. **模块编号 / 标题对齐**
   - 列出 plan v2 §六/七/八里 11 个模块（D1 … D11，D6 拆 6a/6b）。
   - 对齐 handbook v2 章节标题、`workshop/docs/d*_*/` 目录名、`prep-artifacts/day-7/specs/spec-d*` 文件名。
   - 输出不一致项（例：plan 写 "D6a SDK 边界"，handbook 写 "D6 SDK 边界"）。

2. **时长 / 议程**
   - 从 plan v2 抽每模块时长。
   - 对齐 `workshop/README.md` 课程地图表格和 handbook 验收章节。
   - 输出不一致项。

3. **5 维度评分 rubric**
   - 从 plan v2 §X 抽 5 个评分维度的名称与权重。
   - 检查 handbook 验收 / 综合作业 / specs 中是否用同一套口径。

4. **🟢/🟡/🔴 fork 标记**
   - 在 `docs/03-workshop-fork-mapping.md` 每一行检查三色标记是否一致。
   - 抽样核对 `workshop/THIRD_PARTY_NOTICES.md` 是否覆盖所有 🟢 / 🟡 行用到的上游素材。

5. **学员 vs 讲师边界**
   - 任何要求"自带 Azure 订阅"的步骤是否只出现在讲师侧。
   - 学员侧 (`workshop/`) 是否都有 mock provider / stub / sample JSON 路径。

6. **Day-7 gating 状态**
   - README "当前进度" 里 `[~]` / `[ ]` 条目是否在 `docs/02-instructor-prep-checklist.md` 有对应清单项。
   - 反过来：checklist 里每项是否在 README 进度有体现。

7. **specs ↔ handbook 同步**
   - 对 spec-d1 … spec-d11，每个 spec 的 success criteria / negative examples 应与 handbook 对应章节一致。
   - 抽样 3 个 spec 做字段级比对（不需要全文 diff）。

## 输出格式

按章节输出，每节列：
- ✅ 一致 / ⚠️ 漂移 / ❌ 缺失
- 涉及文件与行号（如能定位）
- 建议改哪一份对齐哪一份（默认以 plan v2 为权威）

最后给一个 "需要人工决策" 清单（凡是涉及讲师 Day-7 实物、订阅、外部 API 漂移的，
不要替讲师下结论，只列出）。
