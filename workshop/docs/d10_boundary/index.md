# D10: Foundry 能力边界表

> 时长：60 min（35 讲 / 15 实操 / 10 评审） · Day 3 · 凭证：纯阅读 + 讨论，无需 Azure

## 目标
- 拿到一份 **14 行**能力域 × 当前边界 × 迁移方案的实物表（与 plan 五·五能力地图镜像）
- 能说出至少 3 个常见边界场景的迁移方向
- 能把自己项目对照到边界表，识别 ≥1 个命中项

## 前置
- D2-D9 完成（尤其是 D1 决策卡、D2 选型卡、D6a SDK 边界判断）

## 子任务
1. [14 行能力域速览](01.md) — 镜像 plan 五·五能力地图，逐项点名
2. [边界表实物走读](02.md) — 讲师投屏，每行含"当前边界 + 验证来源"标注（官方文档 URL / portal 截图 / fork 实测，三选一硬要求）
3. [3 个迁移方案样本讨论](03.md) — 覆盖 Models 目录外 / Agent Service 自定义控制流 / 配额上限 三类常见命中
4. [给自己的项目填一行边界](04.md) — 在边界表上勾出命中项 + 写迁移方案 + 与 D1 决策卡做一致性检查

## 验收
- 能在边界表上找到自己项目相关的 ≥ 1 个能力域
- 能解释该能力域当前边界是"官方文档 / portal 截图 / fork 实测"中哪一种验证来源
- 能说出至少 1 个迁移方案（不接受"考虑切到其他平台"这种空话）
- 与 D1 决策卡一致性自检通过：若 D1 说"用 Foundry"但 D10 命中 ≥3 项关键边界，需回去 review D1

## 凭证说明
- 纯阅读 + 讨论，无需 Azure 凭证
- 边界表"验证来源"列三选一为硬要求：**官方文档 URL / portal 截图 / fork 实测**
- **"未验证假设"口径**：只能作为风险备注列在边界表脚注，**不进入主表、不作为课堂边界结论**；学员在主表上看到 "TODO" 应当现场反馈

## 上游素材
- 无（上游 workshop 教"怎么用"，不讲边界；D10 为 v2 新增 🔴）

## 参考
- 链回 [../../handbook/01-instructor-handbook-v2.md#d10](../../handbook/01-instructor-handbook-v2.md#d10)
- 链回 [../../handbook/00-training-plan-v2.md](../../handbook/00-training-plan-v2.md) 五·五能力地图（14 行镜像源）
- 链回 [../../handbook/02-instructor-prep-checklist.md](../../handbook/02-instructor-prep-checklist.md) D10 节（边界表实物 + 验证来源验收口径）
- 链回 [../../handbook/03-workshop-fork-mapping.md](../../handbook/03-workshop-fork-mapping.md) D10 行（🔴 新增定位）
