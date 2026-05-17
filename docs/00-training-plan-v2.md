# 培训方案 v2：AI 原生开发者版（3 天）

> 本文档依据 `docs/04-design-principles.md` 派生。原则改了，本文档必须改。
> v1（`00-training-plan.md`）保留作演化参考。

---

## 一、培训定位（一句话）

> **面向 AI 原生开发者的 Foundry 能力掌握课。**
>
> AI 负责生成实现细节；讲师负责讲清 Foundry 的平台能力、能力边界、组合路径和生产化取舍。

不是 Foundry API 速成。不是泛 AI-pair 编程课。

## 二、学员画像

- AI 原生开发者熟手（Claude Code / Codex / Copilot 飞起）
- 混合背景（startup + partner），共同语言："3 天 MVP，但要生产级"
- 关心：成本 / scaling / 可移植 / 红队 / 生产化（从 Day1 就要）
- 不关心：手把手敲 API、boilerplate、教学环境的简化场景

详见 `docs/04-design-principles.md` 第一节。

## 三、设计原则速览

| # | 原则 | 一句话 |
|---|------|--------|
| 1 | 只讲决策点，不教 API | 讲师讲的内容能被 ChatGPT 替代就讲错了 |
| 2 | AI 不知道的事优先 | rebrand 期 API 漂移、workshop bug、双轨制现状 |
| 3 | 每个模块交付 prompt spec | 不是教代码，是教如何让 AI 写出生产级代码 |
| 4 | Negative example 必须显式 | 每个模块 ≥3 条 |
| 5 | 红队前移；可移植/成本/scaling 必修 | 不是 nice-to-have |

详见 `docs/04-design-principles.md` 第二节。

## 四、议程组织方式（与 v1 最大区别）

**v1**：按原 workshop 的 Ex01-07 顺序排课。
**v2**：按"学员要做的 11 个 Foundry 决策"组织模块，**Ex 是模块的素材，不是骨架**。

每个决策模块统一时间块结构（约 90 分钟）：

```
┌─────────────────────────────────────────────────────┐
│  [25-30 min] 决策点讲解                              │
│  - 这个决策是什么                                    │
│  - AI 不知道的事 / Negative examples                │
│  - 决策卡片模板                                      │
├─────────────────────────────────────────────────────┤
│  [35-45 min] AI-pair 实操                            │
│  - 学员写 spec                                       │
│  - 让 AI 实现                                        │
│  - 自验证                                            │
├─────────────────────────────────────────────────────┤
│  [15-20 min] 评审 + 复盘                             │
│  - 抽 2-3 人展示 AI 输出                            │
│  - 全员点评决策点                                    │
│  - 更新 negative example 库                          │
└─────────────────────────────────────────────────────┘
```

## 五、11 个决策模块总览

| # | 决策模块 | Day | 用到的原 workshop Ex |
|---|---------|-----|---------------------|
| D1 | 何时用 Foundry / 何时不用（Foundry 能力边界初探） | 1 | — |
| D2 | Agent Service vs SDK 选型（架构总览） | 1 | — |
| D3 | 单 agent 平台路径（资源部署 + agent_reference） | 1 | Ex01 + Ex02-01 |
| D4 | Provider 抽象（含非 Azure provider 切换演示） | 1 | — |
| D5 | 部署到 Hosted Agents（主路径）+ scaling / cost 决策；ACA 仅作对照 | 1 | Ex02-03 |
| D6a | Agent Framework SDK 的边界（vs Agent Service） | 2 | Ex03 第一段 |
| D6b | A2A + MCP 的边界（agent 互通 vs 工具协议） | 2 | Ex03 第一段 |
| D7 | 多 agent 编排三选一（Agent Service 原生 / as_tool / Workflows） | 2 | Ex03 第二段 + Workflows 新增 |
| D8 | 红队作为上线门槛——baseline 怎么建 | 2 | Ex06 第一段 |
| D9 | 生产化 checklist（事故、回滚、监控、成本） | 3 | Ex04 + Ex05 + Ex07 |
| D10 | Foundry 能力边界表（什么不能做） | 3 | — |
| D11 | AI-pair 工作流如何成为团队资产 | 3 | — |

**砍掉的旧内容**：
- ❌ Ex02-02 手写 HandoffService（过时模式，并入 D7 作为反例口头讲）
- ❌ OTel KQL 深挖（学员让 AI 写 KQL 即可，D9 只讲必要观测点）
- ❌ Bicep 字段逐行讲解（D3 让 AI 写 Bicep）
- ❌ 演示性讲师手敲代码（全部转 AI-pair）

## 五·五、Foundry 能力地图（D1 必交付）

> 这张表是 D1 的核心交付物，避免"Foundry 能力掌握课"在后续 11 个决策模块里散掉。学员应当能在 Day1 结束时指着这张表说"我现在在哪一格"。
> 与 D10（能力**边界**表）互为镜像：本表讲"覆盖范围"，D10 讲"不能做什么 + 迁移方案"。

| 能力域 | Foundry 提供什么 | 本课在哪个模块讲 | 边界（详见 D10） |
|--------|-----------------|----------------|----------------|
| Agent Service | 托管 agent 运行时、状态、工具调用 | D2 / D3 | 自定义控制流 / 复杂状态机受限 → 见 D10 镜像表（Day-7 实证） |
| Projects | 资源容器、隔离单位 | D3 | 跨 project 资源共享 / 迁移粒度 → 见 D10（Day-7 实证） |
| Connections | 模型 / 数据 / 工具的统一凭证管理 | D3 | 第三方凭证类型覆盖 / 轮换 → 见 D10（Day-7 实证） |
| Identity | Managed Identity / RBAC | D3 / D9 | RBAC 粒度 / 跨租户 → 见 D10（Day-7 实证） |
| Models | Azure OpenAI + 第三方目录 | D2 / D4 | 目录外模型支持有限 / 滞后 → 见 D10（Day-7 实证） |
| Evaluations / Red Team | 内置评测 + 攻击 prompt 生成 | D8 | 内置 attack set 覆盖 / 本地 PyRIT 不兼容 new portal/SDK → 见 D10（Day-7 实证） |
| Tracing / Monitoring | OTel + Application Insights 集成 | D5 / D9 | 采样率 / 自定义维度 / 摄入成本 → 见 D10（Day-7 实证） |
| Deployment | Hosted Agents（主路径）/ Container Apps（legacy 对照） | D5 | Hosted Agents 外部署目标 / 自托管迁移代价 → 见 D10（Day-7 实证） |
| Quotas（PAYG） | TPM / RPM 默认配额 + 成本观测 | D5 / D9 | TPM/RPM 上限 + 增配审批流程 → 见 D10（Day-7 实证） |
| Capacity（dedicated） | PTU / reservation / provisioned throughput | D2（作选型硬约束）/ D5（实操） | dedicated 起买门槛 + 区域 + commitment 期限 → 见 D10（Day-7 实证） |
| SDK / Agent Framework | 代码侧路径，独立于 Agent Service | D2 / D6a | 与 Agent Service 能力差 / 版本节奏 → 见 D10（Day-7 实证） |
| Workflows | visual designer 编排（Agent Service 三选一之一） | D2 / D7 | designer 版本管理 / code review 不友好 → 见 D10（Day-7 实证） |
| Agent 互通协议 | A2A | D6b | 协议成熟度 / 跨 vendor 互通验证 → 见 D10（Day-7 实证） |
| 工具协议 | MCP（含 Foundry MCP server，若可用） | D6b / D11 | Foundry MCP server 可用性二选一 → 见 D10 + D11（Day-7 决定） |

**镜像关系**：本表 14 行边界栏只给"方向 + 指针"；具体"当前边界 + 验证来源（官方文档 URL / portal 截图 / fork 实测）"在 D10 镜像表里填实（讲师手册 v2 D10 章节）。Day-7 由讲师跑 fork 实操时把验证来源补完；plan 侧改 → D10 表同步改。

## 五·六、每模块交付物清单（spec / negative examples / 验收）

> 04 不变量要求：每个模块交付 prompt spec、≥3 条 negative examples、明确验收标准。本节是占位框架，内容随讲师手册 v2 同步填充。
> **本表是 plan → 讲师手册 v2 的契约**：plan 定义接口（每模块必须有 spec/neg/验收 三项），手册负责填实现。
> 没填 = 讲师手册 v2 必须补；空着上课 = 违反原则 3/4。

| 模块 | prompt spec（文件名 / 主题） | negative examples ≥3 | 验收（学员产出怎么算过） |
|------|---------------------------|--------------------|----------------------|
| D1 | ✅ `spec-d1-foundry-fit.md`（D1 无 AI-pair 实操，spec 形态=讲师提供模板，学员当场填"我的项目何时用 Foundry"决策卡） | ✅ ×4 | ✅ |
| D2 | ✅ `spec-d2-service-vs-sdk.md` | ✅ ×4 | ✅ |
| D3 | ✅ `spec-d3-single-agent.md` | ✅ ×4 | ✅ |
| D4 | ✅ `spec-d4-provider-abstraction.md` | ✅ ×4 | ✅ |
| D5 | ✅ `spec-d5-scaling-cost.md` | ✅ ×4 | ✅ |
| D6a | ✅ `spec-d6a-sdk-boundary.md` | ✅ ×4 | ✅ |
| D6b | ✅ `spec-d6b-a2a-mcp.md` | ✅ ×4 | ✅ |
| D7 | ✅ `spec-d7-multi-agent.md` | ✅ ×4 | ✅ |
| D8 | ✅ `spec-d8-redteam-gate.md` | ✅ ×4 | ✅ |
| D9 | ✅ `spec-d9-prod-checklist.md` | ✅ ×4 | ✅ |
| D10 | ✅ `spec-d10-foundry-limits.md` | ✅ ×4 | ✅ |
| D11 | ✅ `spec-d11-ai-pair-team.md` | ✅ ×4 | ✅ |

**状态**：12 个 spec 已抽独立文件，统一放 `prep-artifacts/day-7/specs/`；详细 spec / negative / 验收实现见讲师手册 v2（`docs/01-instructor-handbook-v2.md`）。

**填充节奏建议**（已完成）：
- ~~讲师手册 v2 第 1 轮：先写 spec 文件名 + 1 条 negative example + 验收一句话~~ ✅
- ~~讲师手册 v2 第 2 轮：补齐到 ≥3 条 negative example~~ ✅
- 培训前 1 周（Day-7）：根据 fork 跑通经验补最后 1-2 条新发现的 negative example（待执行）


## 六、Day 1 议程：Foundry 能力地图 + 平台路径 + Provider 抽象

| 时间 | 模块 | 时长 | 时间块结构 |
|------|------|------|----------|
| 09:00-09:45 | **D1：何时用 Foundry / 何时不用**（Foundry 能力地图 + 不用 Foundry 的 4 种场景） | 45 | 30 / 0 / 15（无 AI-pair 实操） |
| 09:45-10:00 | ☕ | — | — |
| 10:00-11:30 | **D2：Agent Service vs SDK 选型**（架构总览 + 4 个真实案例 + 决策卡片） | 90 | 40 / 30 / 20（实操是写自己项目的决策卡） |
| 11:30-12:30 | **D3 第一段：单 agent 平台路径**（决策点 + Bicep 部署 + agent_reference） | 60 | 30 / 30 / 0（评审延到下午） |
| 12:30-13:30 | 🍱 | — | — |
| 13:30-14:30 | **D3 第二段：单 agent AI-pair 实操 + 评审** | 60 | 0 / 45 / 15 |
| 14:30-14:45 | ☕ | — | — |
| 14:45-16:15 | **D4：Provider 抽象**（含非 Azure provider 切换演示，强调可移植决策） | 90 | 30 / 40 / 20 |
| 16:15-16:30 | ☕ | — | — |
| 16:30-18:00 | **D5：部署与容量模式 + Scaling + Cost 决策**（前置 15 min 部署与容量模式对照；Hosted Agents 主路径 + ACA 对照 + 429 重试 + 缓存 + 成本算账） | 90 | 15+20 / 40 / 15 |
| 18:00-18:15 | Day1 匿名反馈 + 公告 | 15 | — |

**Day1 关键产出（每人）**：
- 1 张"我的项目何时用/不用 Foundry"决策卡（D1）
- 1 张 Foundry 能力地图（D1，对应第五·五节模板）
- 1 张"Agent Service vs SDK 选型"决策卡（D2）
- 1 个能跑通的 Foundry 单 agent（D3）
- 1 段 provider 抽象代码（D4）
- 1 个带 429 重试 + 成本估算的部署方案（D5）
- 1 份 deployment/capacity decision note（D5；选 Hosted Agents / ACA / SDK self-host 之一 + 选 PAYG / quota increase / PTU / reservation 之一，并说明理由 + 为什么不选其他）

---

## 七、Day 2 议程：SDK 路径深化 + 多 agent 三选一 + 红队前移

| 时间 | 模块 | 时长 | 时间块结构 |
|------|------|------|----------|
| 09:00-09:30 | Day1 反馈响应 + 路径切换说明（从平台路径切到 SDK 路径） | 30 | 全讲 |
| 09:30-10:30 | **D6a：Agent Framework SDK 的边界**（vs Agent Service：何时切到 SDK；实操先把 SDK 跑通） | 60 | 20 / 30 / 10 |
| 10:30-10:45 | ☕ | — | — |
| 10:45-11:45 | **D6b：A2A + MCP 的边界**（agent 互通 vs 工具协议；实操各跑一个最小 demo） | 60 | 20 / 30 / 10 |
| 11:45-12:30 | D6 叠加实操（在 D6b 的 A2A demo 上加一个 MCP tool；约 30min 完成 + 15min 兜底） | 45 | 0 / 30 / 15 |
| 12:30-13:30 | 🍱 | — | — |
| 13:30-15:30 | **D7：多 agent 编排三选一**（Agent Service 原生跑通主路径；as_tool 用 prepared diff 对照；Workflows 用录屏对照——讲清三者边界，不要求三种全跑通） | 120 | 50 / 50 / 20 |
| 15:30-15:45 | ☕ | — | — |
| 15:45-17:30 | **D8：红队作为上线门槛**（UI + SDK 跑红队 + 把红队接进 CI/CD 思维） | 105 | 30 / 50 / 25 |
| 17:30-17:45 | Day2 匿名反馈 + 综合作业题目预告 | 15 | — |

**Day2 关键产出（每人）**：
- 1 张"何时从 Agent Service 切到 SDK"决策卡（D6a；含成本影响栏）
- 1 张"A2A vs MCP 选型"决策卡（D6b；含成本影响栏：何时不值得引入 A2A/MCP）
- 1 套 SDK 路径跑通的 agent（D6a）+ A2A / MCP 至少一条本机跑通、另一条用 prepared repo / trace 对照（D6b）；叠加 demo 为课堂目标，非必达验收（手册 D6b fallback）
- 1 张"多 agent 三选一"决策卡（D7）
- 1 份红队 baseline 报告（ASR）（D8）

---

## 八、Day 3 议程：生产化 + AI-pair 工作流 + 综合作业

> 节奏说明：D11 从原计划的 Day3 上午尾部移到午饭后开场（轻量、激发型内容），避免连续 3.5 小时全是概念决策导致注意力崩。Day3 上午剩 D9 + D10 两个硬核决策模块。

| 时间 | 模块 | 时长 | 时间块结构 |
|------|------|------|----------|
| 09:00-10:30 | **D9：生产化 checklist**（事故复盘案例 + 回滚 + 监控 + 成本采样 + Azure DevOps 对照 GH Actions） | 90 | 40 / 30 / 20 |
| 10:30-10:45 | ☕ | — | — |
| 10:45-11:45 | **D10：Foundry 能力边界表**（Foundry 不能做什么，配套迁移方案） | 60 | 35 / 15 / 10 |
| 11:45-12:30 | 综合作业开题 + 分组（讲清场景、必做、评分） | 45 | 全讲 |
| 12:30-13:30 | 🍱 | — | — |
| 13:30-14:05 | **D11：AI-pair 工作流如何成为团队资产**（Foundry 文档怎么 prompt、spec 库化；MCP 接 Foundry：若 MCP server 可用则现场连接演示，若不可用则讲 Learn URL / SDK docs / portal evidence 喂给 AI 的替代工作流）—— 午饭后轻量开场 | 35 | 25 / 0 / 10 |
| 14:05-16:30 | **综合作业实做**（3 场景任选；约 2.5 小时 vibe coding） | 145 | — |
| 16:30-16:45 | ☕ | — | — |
| 16:45-17:45 | **综合作业演示**（每组 5 分钟 + 2 分钟 Q&A） | 60 | — |
| 17:45-18:15 | 真实成本回顾 + Ex07 清理 | 30 | — |
| 18:15-18:45 | 结业 + 颁奖 + 后续学习路径 | 30 | — |

**Day3 关键产出（每人）**：
- 1 份生产化 checklist 应用清单（D9）
- 1 份 Foundry 能力边界表（D10）
- 1 份团队 spec 模板库目录 + 2 个示例 spec 大纲（D11；讲师演示，学员誊抄/裁剪）
- 综合作业完整产出

---

## 九、综合作业（Day 3）

### 三场景任选

| 场景 | 适合谁 | 强调维度 |
|------|--------|---------|
| B2C AI 助手 startup | startup 工程师 | 成本、scaling、缓存 |
| Partner POC 给金融客户 | partner SA/实施 | 红队、可移植、合规 |
| 垂直行业 SaaS | 跨场景 | 多租户、扩展性、客户自助 onboard |

### 必做（骨架，约 60%）

1. 至少 1 个 Foundry agent（Agent Service 路径）—— 主路径
2. 多 agent 编排（三种模式任选其一并说明理由）
3. 红队 baseline（`num_objectives=3` 即可）
4. 生产化 checklist 自评（D9 给出的 checklist 勾几项）
5. spec 复用说明（指出本作业里哪段 prompt spec 来自手册 v2 的哪个模块章节 / 对应 `prep-artifacts/day-7/specs/spec-dN-xxx.md`）
6. 综合作业架构选型决策卡（覆盖：Agent Service vs SDK / 多 agent 编排选哪种 / provider 是否抽象 / 红队接入位置——对应评分 25% 的"架构选型决策卡"维度）

### 必做（深度三选二，约 10%）

学员从下面三项中**选 2 项**完成（避免 145min 内组件堆砌挤掉决策质量）：

- A. Agent Framework SDK 路径写的第二个 agent（验证 Day2 D6a/D6b 学到的 SDK 边界判断）
- B. Provider 抽象层（至少演示 Foundry / 直 OpenAI 二选一切换；体现 D4）
- C. OTel + Application Insights 接入（体现 D5/D9 的观测决策）

### 选做加分（30%）

- 三选二之外的第 3 项也完成（A/B/C 全做）
- 第二个非 Azure provider（Anthropic / 自部署）
- 自定义攻击 prompt
- 真实成本估算（按 100 / 1000 / 10000 DAU 三档）
- A2A 暴露专家 agent

### 评分维度

| 维度 | 权重 | 对应原则 |
|------|------|---------|
| 能跑通 | 25% | 基础门槛 |
| 架构选型决策卡（含可移植/成本/scaling 三选一明确说明） | 25% | 原则 1 |
| 红队 baseline | 20% | 原则 5 |
| 生产化 checklist 完成度 | 15% | 原则 5 |
| AI-pair workflow 复用度（spec 让 AI 写出多少可用代码） | 15% | 原则 3 |

### 节奏

3-4 人一组（按学员总数定，目标 ≤4 组），2.5 小时实做 + 5 分钟演示 + 2 分钟 Q&A。

---

## 十、远程交付的关键约束

| 项 | 措施 |
|---|---|
| 助教 | 必配 1 人，专门盯聊天区 + 每模块 AI-pair 实操段巡 breakout room |
| 环境差异 | macOS / Linux / WSL2，Windows 原生不行 |
| 网络 | Azure 国际版，中国区不能用 |
| 录屏 | 每个决策模块的"决策点讲解"段录屏（不录 AI-pair 实操，避免暴露学员代码） |
| 共享文档 | 一份在线文档实时维护"今日 negative example 库"，全员可写 |
| 分组 | Day3 综合作业按 3-4 人分组（与第九节口径一致） |
| 反馈 | Day1/Day2 末尾各 15 分钟匿名反馈，第二天开场响应 |

---

## 十一、人类必须做的 Gating

🚫 培训日期前至少 2 周必须确认：

- MCAPS 外部订阅（EMU 不行）——**讲师侧持票即可**；学员 mock-first 跑通学员路径（见 workshop/README 凭证假设）
- 每个学员的 Foundry 访问权限——**降级为 optional**：学员侧大多步骤走 mock provider / stub / sample JSON；只有想本机真跑 D3 Bicep / D8 SDK 红队的学员才需要订阅，未提供不阻塞验收
- GPT 模型在订阅区域可用 + TPM 配额 ≥ 50K（讲师侧）
- **讲师专用**：1 个非 Azure provider 的 API key（Anthropic / OpenAI 直调），用于 D4 provider 抽象的 live 切换演示。学员不需要个人 key（学员侧用 mock provider 练 abstraction 接口）。

🚫 培训日期前 1 周：

- 学员前置准备清单发出（最低限：Python + 网络可达 GitHub；订阅 / Foundry 访问 optional）
- 报名表加一题"日常用什么 AI 编程工具"——验证 vibe coding 熟手假设
- 一次环境自检（让学员跑 `precheck.sh` 截图给助教；含订阅项标"optional"）

🚫 培训日期前 7 天（讲师本人）—— 下文统称 **Day-7**（贯穿手册 + Day-7 准备清单口径）：

- 跑通改造后的 fork 全套
- 验证 `OpenAIChatOptions(response_format=ResponseFormat)` 在 rc 当前版本是否还可用
- 验证 `OpenAIChatTarget(api_key=token_provider)` 是否还可用
- 登 Foundry portal 核验当前 UI 路径（Models / Agents / Monitoring / Evaluations）
- 跑 `microsoft/agent-framework` repo Workflows samples 至少 2 个

⚠️ 如果 MCAPS 这关过不去——培训直接黄，没 plan B。

---

## 十二、与 v1 的主要差异

| 维度 | v1（旧） | v2（新） |
|------|---------|---------|
| 议程组织 | 按 Ex01-07 顺序 | 按 11 个决策模块 |
| 时间结构 | 讲师 30% / 演示+动手 70% / 评审 0% | 决策讲解 50% / AI-pair 实操 30% / 评审 20% |
| 多 agent | 手写 HandoffService 占 90 min | 砍 HandoffService；新增"三选一决策模块" |
| 可移植 | 仅口头提 | D4 专题（含非 Azure provider 切换） |
| 成本 | Day3 最后 30 min | Day1 D5 模块 + 每个模块带成本说明 + 综合作业评分维度 |
| 红队 | Day3 第二段 | 提前到 Day2 下午（D8） |
| 生产化 | 散落各 Ex | Day3 D9 集中专题 |
| Foundry 能力边界 | 无 | 新增 D10 |
| AI-pair 工作流 | 无 | 新增 D11 |
| 综合作业 | 单一场景 Zava 零售 | 3 场景任选 |
| 综合作业评分 | 跑通 40% / 选型 30% / 观测红队 30% | 跑通 25% / 选型 25% / 红队 20% / 生产化 15% / AI-pair 15% |

---

## 十三、待验证假设（培训前/培训中）

| 假设 | 如何验证 | 不成立怎么办 |
|------|---------|-------------|
| 学员都是 vibe coding 熟手 | 报名表 + Day1 上午观察 AI-pair 完成度 | 不熟手单独 onboarding；或拆双轨 |
| 60 min 单 agent AI-pair 够用 | D3 第二段结束观察完成率 | Day1 实时延长，砍 Day3 buffer |
| 3 个综合作业场景能覆盖学员真实业务 | Day3 开题后看选场景分布 | 加场景 4 或允许自定义 |
| Negative example 真有用 | Day2 末尾匿名反馈问 | 删/改对应模块 |
| 讲师能在 20-40 min 决策讲解段里讲清 D2 / D6a / D6b / D9 等硬核模块 | 每模块结束观察学员评审段提问深度 | 拆分为 2 个模块，砍 buffer |
