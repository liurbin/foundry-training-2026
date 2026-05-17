# D4: Provider 抽象

> 实操 + 讲师演示 / 90 min（30 讲 / 40 实操 / 20 评审） / 学员侧零凭证（mock），讲师侧需 1 个非 Azure provider key

## 目标

- 能写一层 `ChatProvider` 接口，把业务代码与 Foundry / OpenAI / 第三方 SDK 解耦
- 能用 MockProvider 在无任何 Azure 凭证的环境下跑通业务逻辑
- 能判断"我这个项目 1 年内会不会真换 provider"，从而决定这层抽象值不值得加
- 看完讲师 live switch，能说出 Foundry ↔ 非 Azure provider 至少 2 个差异点（响应格式 / 错误码 / 配额行为 / 工具调用语义之一）

## 前置

- D3 单 agent 已跑通（业务代码当前直接依赖 Foundry SDK，本模块要把它"剥"出来）
- Python `Protocol` / 类型提示基础
- 本机有 mock 运行环境（无需任何云端凭证）

## 子任务

1. [Provider 接口设计](01.md) — 学员主线：定义 `ChatProvider` / `Message` / `ChatResponse` 最小字段
2. [MockProvider 实现 + 业务代码改造](02.md) — 学员主线：把 D3 的 agent 调用切到接口背后，MockProvider 返回写死文本跑通
3. [Foundry ↔ 非 Azure provider live switch 观看](03.md) — 讲师演示：仅讲师持非 Azure key，学员观看切换瞬间并记差异点

## 验收

- 学员业务代码 `grep` 不到 `azure` / `openai` 字符串（provider 实现文件除外）
- MockProvider 在断网 / 无 key 环境能跑通业务流程
- 学员能写出"加第三个 provider 只新增一个文件，不改业务代码"的结构
- 能解释接口契约：哪些是共性字段（temperature / max_tokens / stop），哪些走 `**opts` 透传
- 看完 live switch 能口头说出 2 个 Foundry vs 非 Azure provider 差异点
- 抽象层级 ≤ 2 层（不允许"工厂的工厂"，单 if/elif 加载即可）

## 凭证说明

- **学员侧**：只用 MockProvider，**无需任何凭证**。这是刻意设计——abstraction 课不应该被 key 卡住
- **讲师侧**：自备 1 个非 Azure provider 的 API key（Anthropic / OpenAI 直调 / 自托管均可），仅用于课堂上 live switch demo
- 学员**不发** key、不传 key、不在自己机器上跑非 Azure provider；如课后想自己试，自付费自配 key

## 上游素材

- 无。上游 workshop 锁 Azure OpenAI，不涉及 provider 抽象；本模块为 v2 完全新增（参见 `03-workshop-fork-mapping.md` 中 D4 标记为 🔴 新增）

## 参考

- 链回 [../../handbook/01-instructor-handbook-v2.md](../../handbook/01-instructor-handbook-v2.md) D4 节（含 negative examples、验收 checklist 完整版）
- prompt spec：[../../specs/spec-d4-provider-abstraction.md](../../specs/spec-d4-provider-abstraction.md)
- 训练大纲 [../../handbook/00-training-plan-v2.md](../../handbook/00-training-plan-v2.md) D4 行
- Fork 映射 [../../handbook/03-workshop-fork-mapping.md](../../handbook/03-workshop-fork-mapping.md)
