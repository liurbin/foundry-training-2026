# D3: 单 agent 平台路径

> 类型：实操 + 评审（借上游 Ex01 + Ex02 + Ex04） / 时长：120 min（Day1 11:30-12:30 + 13:30-14:30，跨午饭） / 凭证：真跑 Bicep 需 Azure 订阅 + Foundry project；无凭证学员可看讲师演示并拿模板

## 目标

- 在自己（或讲师共享的）Foundry project 里部署一个最小 agent
- 用 `agent_reference` 从外部代码调起 agent，拿到非空返回
- 在 portal Monitoring → Traces 里看到这次调用，能说出"trace 里观察到了什么"
- 能口头讲清"如果换 region / 换模型部署名，要改 Bicep 哪几行"

## 前置

- D1（Foundry 能力地图）+ D2（Agent Service vs SDK 决策卡）已完成
- 本机有 Python（或学员选用的 SDK 语言运行时）
- 真跑 Bicep 路径：需要 Azure 订阅 + 一个已建好的 Foundry project + 模型部署名
- 无订阅：跟讲师演示走，拿到 Bicep 模板与 agent_reference 代码拷回去；trace 那段对照官方文档完成观察清单
- Day1 上午讲师已统一确认 project 是否接入 Application Insights / tracing 开关

## 子任务

1. [Bicep 资源部署](01.md) — 借鉴上游 Ex01，让 AI 生成 module 化 Bicep（agent + connection），学员审 diff 再 `az deployment`
2. [单 agent 跑通](02.md) — 借鉴上游 Ex02 单 agent 路径，写 `agent_reference` 调用代码，含 429 / 5xx 捕获 + 日志
3. [tracing 启用与验证](03.md) — 借鉴上游 Ex04，确认 trace 已上报，对照官方文档完成"已观察到 X / Y / Z"清单

## 验收

学员自检清单（对应讲师手册 D3 验收）：

- [ ] Bicep 在自己的 Foundry project 跑通（不接受"讲师那边能跑"）；无订阅学员：拿到模板 + 能讲清 module 拆分
- [ ] `agent_reference` 代码在本机成功调用一次，返回 200 且文本非空
- [ ] portal Monitoring → Traces 看到这次调用（tracing 未启用时此项转可选，留到 D5/D9 补）
- [ ] 能口头讲清"换 region 要改 Bicep 哪几行"
- [ ] secret 100% 不在源码里（讲师 grep 抽查）；用 Key Vault 引用或 env，不写死 connection string
- [ ] model deployment name 不写死在 Bicep 里，走 parameter

## 凭证说明

- **Bicep 部署**：有订阅学员自跑；无订阅学员看讲师演示 + 拿模板拷走，回去自跑
- **单 agent 代码**：学员本机可跑；无真 endpoint 时用 mock provider（D4 会正式引入）或讲师共享的临时端点
- **tracing 截图**：讲师在 portal 上展示一次完整 trace；学员对照官方文档完成"已观察到 X / Y / Z"清单（X/Y/Z 由讲师在课中指定，例如 span 层级、token 计数、tool call 节点）

## 上游素材

- Ex01：Bicep 模板结构（agent + connection 创建）
- Ex02：单 agent 实现（具体 SDK 名待 fork 实操确认，见 `docs/03-workshop-fork-mapping.md` 未确认事项）
- Ex04：tracing 启用（是否基于 OTel 待 fork 确认，影响本模块观测口径）

## 参考

- 讲师手册 D3 模块：[../../../docs/01-instructor-handbook-v2.md](../../../docs/01-instructor-handbook-v2.md)（搜 "D3 — 单 agent 平台路径"）
- 训练计划 D3 议程：[../../../docs/00-training-plan-v2.md](../../../docs/00-training-plan-v2.md)（Day1 第六节）
- fork 映射表 D3 行：[../../../docs/03-workshop-fork-mapping.md](../../../docs/03-workshop-fork-mapping.md)
- prompt spec：[../../../prep-artifacts/day-7/specs/spec-d3-single-agent.md](../../../prep-artifacts/day-7/specs/spec-d3-single-agent.md)
