# D5: 部署与容量模式 + Scaling + Cost

> 实操 + 讲师演示 / 90 min（15 部署与容量对照 + 20 讲 / 40 练 / 15 评审） / 凭证：学员侧全 stub，不依赖真实 Foundry 配额

## 目标
- **能在 3 种部署目标里说出自己项目选哪种 + 为什么不选其他**（Hosted Agents / ACA 自托管 / SDK self-host）
- **能在 4 种容量模式里说出自己项目选哪种 + 为什么不选其他**（PAYG / quota increase / PTU / reservation）
- 能在 provider/HTTP 客户端层写出带 jitter 的 429 + 5xx 指数退避重试，并用 stub 验证
- 能解释一层 prompt+model 缓存的命中条件、TTL 取值理由、以及键里不能放什么
- 能用成本估算脚本跑出 1k / 10k / 100k DAU 三档月度成本上下限，**且每档对应一种容量模式**
- 看完讲师 100 RPS × 5min 压测，能指出 retry 行为和缓存命中两个观察点

## 前置
- D3 单 agent demo 跑通（本模块在 D3 产物上加 retry / cache / 成本脚本）
- D2 决策卡（含硬约束栏，本模块把容量类硬约束承接到 decision note）
- 本地能跑 stub 注入脚本（不需要真实 Foundry quota）

## 子任务
0. [部署与容量模式对照](00.md) — **前置 15 min**：3 部署目标 × 4 容量模式对照表，先选再做 retry/cache/成本；产出 decision note
1. [429 retry + jitter](01.md) — 用 stub 注入 429，在 provider 层加指数退避，禁止业务层 catch-retry
2. [缓存策略与雷区](02.md) — prompt+model hash 一层缓存，TTL 自定 + 写理由；键禁含 user_id / 个人数据
3. [成本三档估算 + 容量模式承接](03.md) — 跑脚本输出 1k / 10k / 100k DAU 的月度 $ 上下限，每档明确容量模式
4. [压测脚本观看](04.md) — 讲师演示 100 RPS × 5min，学员只看不跑，记录 retry 触发点和 cache hit 曲线

## 验收
- **deployment/capacity decision note 已交**：部署目标 + 容量模式各 1 选 + 为什么不选其他（每条 ≥1 句理由）
- retry + jitter 代码在 stub 注入 429 下能恢复，且不在业务层抛
- 能解释 cache key 不能含 user_id / 个人数据，以及为什么（合规雷区 + 命中率失真）
- 能填出三档（1k / 10k / 100k DAU）成本表，标注假设 + 每档对应的容量模式
- 看完压测能说出两个观察点：retry 触发是否有 jitter 错峰、缓存命中率是否随时间上升

## 部署路径分层（开课前必读）
- **主路径 = Foundry Hosted Agents**（new backend）：托管容器、scale-to-zero、15 min idle 后释放。默认部署目标。
- **对照路径 = Container Apps 自托管**（走旧 `azd ai agent` 模板）：必须自托管 / VNet 强约束 / 客户私有 Azure 时选；不作为默认。
- **跨云 / 真私有 = SDK self-host**（AKS / App Service / VM）：全套 K8s 运维 + 自接观测；命中"客户自带 K8s / 跨云"才选。
- `min replicas ≥ 1` 是 ACA 段的硬约束，**不适用 Hosted Agents**——Hosted Agents 的 scale-to-zero 是产品默认行为。

## 容量模式分层（开课前必读）
- **主路径 = PAYG + 默认配额**：流量不可预测 / POC / 中小规模；触发 429 → 加 retry + cache 即可
- **Quota increase**：流量上涨但仍有抖动，不想买 commitment；走 [quota request form](https://aka.ms/oai/stuquotarequest)，区域 + 模型有上限
- **PTU / Provisioned Throughput**：高吞吐 + 稳定 SLA + 流量可预测；按月起买，区域 + 模型限制更严
- **Reservation**：长期稳定用量 + 财务上要锁价；commitment 期限 ≥ 1 年，和 PTU 正交（可叠加）

## 凭证说明
- 学员侧：用 stub / replay response 注入 429，**不依赖真实 Foundry 配额**
- 真压测：讲师演示一次 100 RPS × 5min，学员不真跑（避免打爆共享配额 + 真实账单）
- 缓存约束（硬性）：缓存键不准包含 user_id / 个人数据 —— 既是合规雷区，也会让命中率失真
- 部署约束补充（仅 ACA 对照路径）：min replicas 不准为 0（冷启动 + 第一次 429 会同时炸）；Hosted Agents 主路径不写这条
- 容量约束：本课不需要真实 PTU 订阅；PTU / reservation 的"选不选"在 decision note 里讲理由即可，不要求真实 provision

## 上游素材
- 借鉴上游 Ex02-03（部署到 Azure 的段落）作为部署上下文；scaling / cost 决策（429 stub、压测脚本、成本三档）+ 部署/容量模式决策为本模块 v2 新增，上游 Ex05 只覆盖 CI/CD 不涉及。

## 参考
- 链回 ../../handbook/01-instructor-handbook-v2.md#d5
- 训练计划：../../handbook/00-training-plan-v2.md（D5 行）
- Fork 映射：../../handbook/03-workshop-fork-mapping.md（D5 标记为新增）
