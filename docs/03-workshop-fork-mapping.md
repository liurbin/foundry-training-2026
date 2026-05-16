# 原 workshop ↔ v2 课程对照表

> 上游：`microsoft/TechWorkshop-L300-AI-Apps-and-agents`
> 站点：https://microsoft.github.io/TechWorkshop-L300-AI-Apps-and-agents/
> 用途：fork 改造前定级——哪些模块可直接复用、哪些要补、哪些要从零写。
> 本表只基于 exercise overview 页面，未读子页 / 未 clone 源码；具体 SDK 名、API 细节、Bicep 结构需 fork 实操阶段进一步确认。

## 上游模块速览

| Ex | 标题 | 时长 | 关键内容 |
|----|------|------|---------|
| 01 | Deploy and configure resources | 60 min | Bicep + Cosmos DB + AI Search + Foundry project 连接 |
| 02 | Multimodal AI shopping assistant | 60 min | 单 agent → 多 agent → 部署 Azure（SDK 选型未明示）|
| 03 | Extend with A2A Protocol | 40 min | 构建 A2A server + 接入 Zava Product Manager |
| 04 | Observability in Foundry | — | Foundry dashboard + App Insights + Evaluators |
| 05 | Agentic DevOps | 60 min | Copilot 生成 GH Actions：容器部署 + agent 部署 |
| 06 | AI-enhanced red teaming | 40 min | UI 红队 + SDK Red Teaming Agent + 自定义 attack |
| 07 | Resource cleanup | — | 资源回收 |

## v2 模块对照

| v2 模块 | 上游对应 | 状态 | 改造工作量 |
|---------|---------|------|----------|
| **D1** 概念 + 决策模块设计 | 无 | 🔴 新增 | "决策 vs API 教程"框架原 workshop 不存在 |
| **D2** Agent Service vs SDK 选型 | Ex02 隐含选了一个 SDK，未呈现决策 | 🔴 新增 | 决策卡 + 4 维度评分 + 成本三档要自写 |
| **D3** 单 agent 平台路径 | Ex01 (Bicep) + Ex02 (single agent) + Ex04 (tracing) | 🟢 基本照搬 | Bicep / 单 agent / tracing 三件齐；只需 spec 化 + 漂移清单 |
| **D4** Provider 抽象 | 无 | 🔴 新增 | 上游锁 Azure OpenAI；mock provider、live switch、非 Azure key 全自写 |
| **D5** Scaling + Cost | 无（Ex05 只做 CI/CD） | 🔴 新增 | 429 stub、压测脚本、成本三档全自写 |
| **D6a** Agent Framework SDK 的边界 | Ex03 第一段（用作 SDK 跑通基线） | 🟡 部分 | 实操片段可复用作 SDK 起点；"SDK vs Agent Service 边界 + 决策卡 + 成本净差额"为本课新增 |
| **D6b** A2A + MCP 边界 + 叠加 | Ex03（仅 A2A） | 🟡 部分 | A2A demo 由本模块主段承担；MCP 部分上游没有 |
| **D7** 多 agent 编排三选一 | Ex02 (multi-agent，单一路径) | 🟡 部分 | 上游只展示一种；as_tool / Workflows 对照要补 |
| **D8** 红队 baseline | Ex06 (UI + SDK + 自定义) | 🟢 基本照搬 | 上游此模块最强；只需补 rubric + sample JSON fallback |
| **D9** 生产化 checklist | Ex05 (GH Actions) 部分 | 🟡 部分 | 上游只做部署自动化；事故复盘 / runbook / 红队 gate 要补 |
| **D10** Foundry 能力边界表 | 无 | 🔴 新增 | 上游教"怎么用"，不讲边界 |
| **D11** AI-pair 工作流 | Ex05 提到 Copilot 生成 workflow，不是 spec 库 | 🔴 新增 | spec 库 / negative example / decision card 全自写 |

## 汇总

- 🟢 直接复用：**2 个**（D3、D8）
- 🟡 部分复用：**4 个**（D6a、D6b、D7、D9）
- 🔴 新增：**6 个**（D1、D2、D4、D5、D10、D11）

上游 ≈ 5 小时课时，v2 ≈ 18 小时（3 天）；课时比 ≈ 1:3.6。原 workshop 提供约 30% 素材，其余 70% 为 v2 原创设计（决策模块、provider 抽象、scaling、能力边界、AI-pair）。

## 已知未确认事项（fork 实操阶段补）

- Ex02 用的 SDK 名（Agent Service REST / Agent Framework SDK / Semantic Kernel）→ 影响 D2 spec 写法
- Ex03 A2A 实现（`python-a2a` / 自写 / 同进程伪 A2A）→ 影响 D6b 反例展示
- Ex04 tracing 是否基于 OTel → 影响 D3 / D9 观测章节口径
- Ex06 attack 分类、`num_objectives` 默认值、评估指标口径 → 影响 D8 baseline 描述
- Bicep 模板结构 / Foundry 项目连接方式 → 影响 D3 模板复用

## 维护规则

- 上游 repo 更新（新 exercise / API 漂移）→ 同步本表 + 同步影响到的 v2 模块 spec
- fork 改造完成后，本表 + Day-7 准备清单 D3 / D6a / D6b / D7 / D8 / D9 行需对齐"哪些直接用上游、哪些已替换"
