# D5: Scaling + Cost

> 实操 + 讲师演示 / 90 min（30 讲 / 40 练 / 20 演示） / 凭证：学员侧全 stub，不依赖真实 Foundry 配额

## 目标
- 能在 provider/HTTP 客户端层写出带 jitter 的 429 + 5xx 指数退避重试，并用 stub 验证
- 能解释一层 prompt+model 缓存的命中条件、TTL 取值理由、以及键里不能放什么
- 能用成本估算脚本跑出 1k / 10k / 100k DAU 三档月度成本上下限
- 看完讲师 100 RPS × 5min 压测，能指出 retry 行为和缓存命中两个观察点

## 前置
- D3 单 agent demo 跑通（本模块在 D3 产物上加 retry / cache / 成本脚本）
- 本地能跑 stub 注入脚本（不需要真实 Foundry quota）

## 子任务
1. [429 retry + jitter](01.md) — 用 stub 注入 429，在 provider 层加指数退避，禁止业务层 catch-retry
2. [缓存策略与雷区](02.md) — prompt+model hash 一层缓存，TTL 自定 + 写理由；键禁含 user_id / 个人数据
3. [成本三档估算](03.md) — 跑脚本输出 1k / 10k / 100k DAU 的月度 $ 上下限（模型费 + 容器费 + 缓存命中率影响）
4. [压测脚本观看](04.md) — 讲师演示 100 RPS × 5min，学员只看不跑，记录 retry 触发点和 cache hit 曲线

## 验收
- retry + jitter 代码在 stub 注入 429 下能恢复，且不在业务层抛
- 能解释 cache key 不能含 user_id / 个人数据，以及为什么（合规雷区 + 命中率失真）
- 能填出三档（1k / 10k / 100k DAU）成本表，标注假设
- 看完压测能说出两个观察点：retry 触发是否有 jitter 错峰、缓存命中率是否随时间上升

## 部署路径分层（开课前必读）
- **主路径 = Foundry Hosted Agents**（new backend）：托管容器、scale-to-zero、15 min idle 后释放。学员的 D5 部署目标。
- **对照路径 = Container Apps 自托管**（走旧 `azd ai agent` 模板）：仅作"自托管时你要操心什么"对照，不作为学员部署目标。
- `min replicas ≥ 1` 是 ACA 段的硬约束，**不适用 Hosted Agents**——Hosted Agents 的 scale-to-zero 是产品默认行为。

## 凭证说明
- 学员侧：用 stub / replay response 注入 429，**不依赖真实 Foundry 配额**
- 真压测：讲师演示一次 100 RPS × 5min，学员不真跑（避免打爆共享配额 + 真实账单）
- 缓存约束（硬性）：缓存键不准包含 user_id / 个人数据 —— 既是合规雷区，也会让命中率失真
- 部署约束补充（仅 ACA 对照路径）：min replicas 不准为 0（冷启动 + 第一次 429 会同时炸）；Hosted Agents 主路径不写这条

## 上游素材
- 借鉴上游 Ex02-03（部署到 Azure 的段落）作为部署上下文；scaling / cost 决策（429 stub、压测脚本、成本三档）为本模块 v2 新增，上游 Ex05 只覆盖 CI/CD 不涉及。

## 参考
- 链回 ../../handbook/01-instructor-handbook-v2.md#d5
- 训练计划：../../handbook/00-training-plan-v2.md（D5 行）
- Fork 映射：../../handbook/03-workshop-fork-mapping.md（D5 标记为新增）
