# 讲师手册（Foundry 培训 3 天版）

## 使用说明
- 每个模块给出：**核心目标 / 必讲 / 必演示 / 常见坑 / Q&A 预案 / 节奏建议**
- "必讲"是讲解员**口头**要说清楚的，"必演示"是要屏幕共享操作的
- 节奏 = 讲解 : 演示 : 学员动手 的时间比例

---

## 第 0 章 - 讲师培训前 Checklist

### 开课前 7 天

- [ ] 自己跑通改造后的 fork 全套 Ex（**不能只看代码**）
- [ ] 验证 Ex03 三处 bug 已修复且能跑
- [ ] 验证 `OpenAIChatOptions(response_format=ResponseFormat)` 在 rc6 实际可用——如果 API 已改名，提前更新手册
- [ ] 验证 `OpenAIChatTarget(api_key=token_provider)` 实际可用——同样验证后再上课
- [ ] 登一遍 Foundry portal，确认 UI 路径（Models / Agents / Monitoring / Evaluations 菜单当前位置）
- [ ] 跑 `microsoft/agent-framework` repo 的 Workflows sample 至少 2 个，确认 API 现状

### 开课前 3 天

- [ ] 跑 `scripts/precheck.sh` 验证讲师自己环境
- [ ] 准备好备用订阅（万一主订阅集体 429）
- [ ] 准备好 Ex03 完整修复版代码包（学员卡住时可直接发）
- [ ] 联系助教，对齐分工（聊天区主守谁、综合作业评委分组）
- [ ] 检查每个学员的 precheck 截图，对未达标学员单独沟通

### 开课当天

- [ ] 提前 30 分钟开 Zoom，测试屏幕共享/录屏/分组
- [ ] 把"今日已知问题"在线文档链接发群里
- [ ] 把当天 PPT、命令清单、参考链接发群里

---

## Day 1 - 开场：架构总览（45 分钟）

### 核心目标
让学员**第一时间分清** Foundry Agent Service vs Agent Framework SDK，避免后续 Ex02/Ex03 风格差异引发混乱。通过 4 个案例让"选型决策"在他们脑子里落地。

### 必讲
1. **微软 agent 生态当前是双轨制**：平台路径 vs SDK 路径，没合并
2. **Agent Service = Foundry 平台原生**：Responses API + `agent_reference`，平台托管，内置观测/管理，**强平台锁定**
3. **Agent Framework SDK = `agent-framework` 1.0 GA**：Python/.NET 库，跨模型可移植，**自己接观测**
4. **本次培训为什么两条都讲**：Ex02 走平台路径，Ex03 走 SDK 路径，**学完两条才能做架构选型**
5. **历史包袱**：AutoGen 和 Semantic Kernel 都被 Agent Framework 吸收，老代码迁移要参考官方迁移指南
6. **过完 4 个案例**：让学员对"选型"有感觉，不是抽象概念

### 4 个案例讲法

| 案例 | 选型 | 讲解要点 |
|------|------|---------|
| 企业内部 IT 工单 chatbot | Agent Service | "强治理 + 平台审计 + 单一团队"——典型 SaaS 场景，平台锁定不是问题 |
| SaaS 产品里的 AI 助手（要支持私有部署） | SDK | "客户可能要部署到自己的 Azure 或他云"——平台锁定致命，必须 SDK |
| 多 agent 协作的内部研究工具 | SDK + Workflows | "流程明确 + 需要 checkpoint + human-in-the-loop"——Workflows 强项 |
| 一次性 demo / POC | Agent Service | "30 分钟出活，UI 也能改"——速度第一 |

### 必演示
- 打开 Foundry portal（https://ai.azure.com），快速过一遍 Agents 菜单和 Models 菜单
- 打开 `microsoft/agent-framework` GitHub repo 的 `python/samples/getting_started/` 目录

### 常见坑
- 学员问"那我以后到底用哪个"——**别给标准答案**，引导他们看 4 个案例选最像的
- 学员问"这和 LangChain/LangGraph 比怎么样"——简短回答"是同一类问题的不同生态，微软这套强绑 Azure"，不要展开

### Q&A 预案
| 问题 | 回答要点 |
|------|----------|
| Foundry 和 Azure OpenAI 什么关系 | Foundry 是上层平台，Azure OpenAI 是底层模型服务 |
| Agent Framework 稳定吗 | core 1.0 GA，Foundry 连接器还是 rc，beta API 可能小变 |
| 能不能用国内模型 | 不能，Foundry 只支持微软自己的+合作伙伴模型清单 |
| 双轨会不会以后合并 | 不知道，目前没看到合并信号 |

### 节奏
讲解 30 分钟（含 4 案例） + Q&A 15 分钟。

---

## Day 1 - Ex01 资源部署（75 分钟，含 15 min buffer）

### 核心目标
每个学员独立用 Bicep 部署一套 Foundry 资源 + Cosmos + Container Apps 环境。

### 必讲
1. **Bicep = Azure 的 IaC 语言**，编译成 ARM template
2. **为什么不用 Terraform**：微软自家工具链对 Foundry 的预览功能跟得更快
3. **资源命名规则**：每人加唯一后缀（如姓名首字母+日期），避免冲突
4. **成本预警**：GPT 部署默认 1K TPM 不够，Day2 红队会触发 429，**提前在 Foundry 把 TPM 拉到 50K**

### 必演示
1. `az login` + `az account set --subscription <ID>`
2. 跑 workshop 的 Bicep 部署命令
3. 部署完打开 Foundry portal 确认资源
4. **演示去 Models → Deployments 把 TPM 改到 50K**

### 常见坑
| 坑 | 症状 | 解法 |
|----|------|------|
| MCAPS 订阅没分配 | `az account show` 没结果 | 救不了，让学员旁听 |
| 区域配额不够 | Bicep 部署 ResourceQuotaExceeded | 换 `swedencentral` 或 `eastus2` |
| GPT 模型在此区域不可用 | 部署成功但 Foundry 看不到模型 | 改 Bicep `location` 参数重部署 |
| Container Apps env 部署超慢 | 卡 10 分钟+ | 正常，让学员先去看下一节预习 |
| 学员误删资源 | Foundry portal 看不到东西 | `az group list` 查 RG 是不是还在 |

### Q&A 预案
- "为什么要建 Cosmos"——Ex02 多 agent 的 session/handoff 状态用 Cosmos 存
- "可以共用一个资源组吗"——技术上行，但实际上学员互相干扰，不推荐

### 节奏
讲解 15 分钟 + 演示 15 分钟 + 学员动手 30 分钟 + 15 分钟 buffer。**助教全程盯聊天区**。

---

## Day 1 - Ex02-01 单 agent（第一段 75 + 学员动手 60 = 135 分钟）

### 核心目标
学员能用 `AIProjectClient` + `PromptAgentDefinition` + Responses API 创建并调用单 agent。

### 必讲
1. **这是 Foundry Agent Service 平台路径**——agent 定义存在 Foundry 平台上，代码只是引用
2. **关键 API**：
   - `project_client.agents.create_version()` 创建/更新 agent 版本
   - `openai_client.responses.create(extra_body={"agent_reference": ...})` 调用 agent
3. **为什么用 Responses API 而不是 Chat Completions**——支持 agent_reference、conversation thread、内置工具
4. **agent 在 Foundry portal 可见**：演示完代码立刻去 portal 看创建的 agent

### 必演示
1. 打开 `src/app/agents/agent_initializer.py`，逐行讲 `PromptAgentDefinition` 字段含义
2. 跑 chat app，发一个消息，看响应
3. 切到 Foundry portal 看 agent 版本历史
4. 看 Cosmos 里的 thread 数据

### 常见坑
| 坑 | 症状 | 解法 |
|----|------|------|
| `.env` 没配 | 启动报 KeyError | 检查 `gpt_endpoint`/`gpt_deployment`/`FOUNDRY_ENDPOINT` |
| `DefaultAzureCredential` 拿不到 token | 401 | `az login` 重登；macOS 装 `keyring` |
| agent 调用 429 | TPM 不够 | 提前已经拉到 50K，没拉的现在拉 |
| Responses API 返回格式陌生 | 学员看不懂 `output` 结构 | 屏幕共享 `print(response.model_dump_json(indent=2))` 一起看 |

### Q&A 预案
- "agent_reference 是什么魔法"——Foundry 服务端解析这个 reference，注入 agent 的 instructions/tools
- "为什么不直接用 Agent Framework SDK"——这就是平台路径的核心：把 agent 定义和管理交给平台

### 节奏
第一段（午餐前）：讲解 25 分钟 + 演示 20 分钟 + 学员开始动手 30 分钟。
第二段（午餐后）：学员继续动手 60 分钟，助教巡场。

---

## Day 1 - Ex02-02 多 agent（90 分钟）

### 核心目标
学员理解"手写 orchestrator + 意图分类"这种**朴素多 agent 编排**模式。

### 必讲
1. **本练习的多 agent ≠ Agent Framework 的 Workflows**——这里是手写路由，Day2 会讲 Workflows
2. **Handoff 模式**：用一个轻量 LLM 做意图分类（Pydantic schema），然后字典路由到专家 agent
3. **session 状态**存在 Cosmos，handoff 时 thread 传递
4. **优缺点**：好懂、可控、但路由逻辑硬编码，难扩展——这就是 Workflows 要解决的问题

### 必演示
1. 看 `src/services/handoff_service.py` 的意图分类代码
2. 看 `multi_agent_handler.py` 的路由代码
3. 跑 chat app，问不同类型的问题，看路由日志
4. 在 Foundry portal 看多个 agent 同时存在

### 常见坑
- Cosmos 连接字符串错——给标准 `.env` 模板让学员复制
- 意图分类不准——讲清楚是 prompt 设计问题，不是框架问题
- 学员问"这和 Day2 的 A2A 啥区别"——这里是**同进程内**多 agent，A2A 是**跨服务**多 agent

### 节奏
讲解 25 分钟 + 演示 15 分钟 + 学员动手 50 分钟。

---

## Day 1 - Ex02-03 部署到 Azure（45 分钟）

### 核心目标
把 chat app 容器化部署到 Container Apps。

### 必讲
1. **生产化 = 容器 + 环境变量注入 + 托管身份**
2. **Container Apps vs App Service vs AKS**：Container Apps 是 PaaS Kubernetes，对 agent 类工作负载最省心
3. **Managed Identity 替代 connection string**——演示 Bicep 里怎么配 RBAC

### 必演示
1. `docker build` 本地构建
2. `az containerapp update` 部署
3. 浏览器访问公网 URL，发消息成功

### 常见坑
- ACR 镜像权限——Container Apps 的 system-assigned identity 需要 `AcrPull` 角色
- 环境变量没生效——检查是不是用了 `--set-env-vars` 而不是 `--replace-env-vars`
- 部署后 401——Managed Identity 没分配 `Azure AI Developer`

### 节奏
讲解 10 分钟 + 演示 15 分钟 + 学员动手 20 分钟。**这块比 2 天版砍了 15 分钟动手**，因为部署本身比写代码快。

---

## Day 1 - 匿名反馈（15 分钟）

### 必做
1. 群里发匿名表单链接（Google Form / Microsoft Forms）
2. 5 个问题：
   - 今天节奏快/慢/合适？
   - 哪个模块讲得最不清楚？
   - 现在最大的疑问是什么？
   - Day2 想多讲什么？
   - 助教响应速度怎么样？
3. **当晚讲师 + 助教必须看完**，Day2 开场针对性回应

---

## Day 2 - 回顾 + 反馈响应 + 架构再澄清（30 分钟）

### 必讲
1. **响应 Day1 匿名反馈** —— 至少回答 3 个高频问题
2. **快速复盘 Day1**：5 个 Ex 各做了什么，**全部都是平台路径**
3. **Day2 切换轨道**：Ex03 开始走 SDK 路径，**注意 import 不一样了**
4. **再次强调**：两条路不是互斥，生产环境经常混用

### 必演示
- 对比 `agent_initializer.py`（Day1 用的）和 `product_management_agent.py`（Day2 要用的），让学员肉眼看 import 差异

### 节奏
反馈响应 10 分钟 + 复盘 10 分钟 + 架构对比 10 分钟。

---

## Day 2 - Ex04 观测（75 分钟）

### 核心目标
启用 OTel + Azure Monitor，能在 Foundry 监控面板看 trace。**3 天版给了完整时间深挖 Foundry 监控面板**。

### 必讲
1. **workshop 原版代码把 OTel 注释掉了**——本次改造已启用
2. **三件套**：`configure_azure_monitor()` + `OpenAIInstrumentor().instrument()` + `tracer.start_as_current_span()`
3. **Foundry 监控面板**在 portal 哪里看
4. **agent 调用 → OTel span → Application Insights → Foundry 面板**这条链路
5. **进阶**：自定义 span 属性、采样率、PII 脱敏

### 必演示
1. 看改造后的 `chat_app.py`，指出之前被注释的几行已经放出来
2. 跑 chat app，发几条消息
3. 去 Foundry portal → Monitoring 面板看 trace
4. 去 Application Insights → Transaction search 看完整 span
5. **演示 KQL 查询**：按 agent 名/会话 ID 查最慢的 N 条 trace
6. **演示如何加自定义属性**：`tracer.start_as_current_span("custom", attributes={"user_id": ...})`

### 常见坑
- AI Connection String 没配——`APPLICATIONINSIGHTS_CONNECTION_STRING` 必须在 env
- Trace 延迟——AI 数据延迟 2-5 分钟，不要让学员死等
- 多个 instrumentor 冲突——只用 `OpenAIInstrumentor`，不要叠加 `RequestsInstrumentor`

### Q&A 预案
- "为什么不用 Langfuse/Arize"——可以，但本课只讲 Azure 原生
- "成本怎么算"——AI 按 GB 计费，开发期不贵，生产期注意采样率（建议生产 10% 采样）
- "怎么追多 agent 调用链"——用 OTel context propagation，跨 agent 共享 trace_id

### 节奏
讲解 25 分钟 + 演示 30 分钟 + 学员动手 20 分钟。

---

## Day 2 - Ex03 A2A + Agent Framework SDK（90 + 90 = 180 分钟）

### 核心目标
学员能用 `agent-framework` 1.0 写 agent，并用 `a2a-sdk` 暴露成 A2A 服务。

### 必讲
1. **这是 workshop 唯一真正用 Agent Framework SDK 的部分**
2. **A2A 协议**：Google 推的开放协议，目标是 agent 间互操作
3. **关键 API**：
   - `agent_framework.Agent(client=, instructions=, tools=)`
   - `agent.run()` / `agent.run_stream()`
   - `agent.as_tool()` 让 agent 当工具用
   - `a2a.server.apps.A2AStarletteApplication`
4. **as_tool 模式 vs Workflows**：下个模块对比

### ⚠️ 必修 bug（讲师本人务必先确认 fork 已修）
1. **L876** `tools=get_products` → 应为 `tools=[get_products]`
2. **L854** 文档说 `@ai_function`，代码用 `@tool` → 文档说法以代码为准
3. **L182** `OpenAIChatOptions(response_format=ResponseFormat)` → 跑前在自己机器验证一遍，rc6 期间这个字段可能改名

### 必演示
1. 逐个文件创建：`product_management_agent.py` → `agent_executor.py` → `a2a_server.py` → `chat.py`
2. **每创建一个文件，立刻 import 检查**，避免最后一起报错
3. 启动后访问 `http://127.0.0.1:8001/agent-card/`，展示 A2A agent card
4. 在浏览器问"Which paint roller is best for smooth surfaces"

### 常见坑
| 坑 | 症状 | 解法 |
|----|------|------|
| 路径不对 | `ImportError: cannot import name 'agent'` | 强调 `from agent.product_management_agent import ...` 是相对 `src/a2a/` |
| Pydantic 校验失败 | `ValidationError: status field required` | LLM 没返回 JSON，prompt 重申"必须 JSON" |
| `as_tool()` 报错 | rc6 可能 API 变 | 临时降级用 function tool 替代 |
| A2A server 端口冲突 | 8001 被占 | 改 port 或 `lsof -i:8001` 杀进程 |

### Q&A 预案
- "A2A 和 MCP 啥区别"——MCP 是 LLM 调工具，A2A 是 agent 调 agent
- "Python 的 A2A 是不是不官方"——目前微软自己的 Learn 文档说 .NET 才有官方集成，Python 用社区 `a2a-sdk`

### 节奏
第一段：讲解 30 分钟 + 演示 60 分钟（完整跟着敲 4 个文件）。
第二段：学员动手 60 分钟 + A2A 联调 + Q&A 30 分钟。

---

## Day 2 - Workflows 补充模块（90 分钟）

### 核心目标
学员理解 `WorkflowBuilder` 图式编排，能改写 Ex03 的 `as_tool` 多 agent 为 Workflow。

### 必讲
1. **Workflows 是 Learn 文档主推的多 agent 编排方式**——workshop 没讲，所以我们补
2. **核心抽象**：节点（agent/function）+ 边（路由条件）+ checkpoint + human-in-the-loop
3. **vs as_tool**：as_tool 简单但路由由 LLM 决定，Workflows 显式控制执行图
4. **何时用哪种**：流程明确用 Workflows，开放式用 as_tool

### 必演示
1. 打开 `microsoft/agent-framework` repo 的 `python/samples/getting_started/workflows/` 目录
2. 跑一个最简单的 sequential workflow sample
3. 跑一个 conditional routing sample
4. **现场把 Ex03 的 Marketing + Ranker + Product 改写成 Workflow**（提前准备好对照代码）

### 常见坑
- Workflow API 还在快速演进，sample 可能比文档新——以 sample 为准
- Checkpoint 状态序列化对 Pydantic v2 敏感

### 节奏
讲解 25 分钟 + 演示 35 分钟 + 学员动手 30 分钟（真正改写一段，不是只看）。

---

## Day 2 - Ex05 Agentic DevOps（45 分钟）

### 核心目标
学员理解"用 GitHub Actions 把 agent 定义当软件制品部署"。

### 必讲
1. **agent 部署 = `az rest` 调 Foundry REST API**，没有 SDK 等价物
2. **agent 定义文件**：prompt + JSON 模板合成后 POST 到 `agents/<name>/versions`
3. **版本管理**：每次 PR merge 都创建新 agent version，可回滚
4. **生产价值**：把 agent 纳入正常的 CI/CD，而不是手动在 Foundry portal 改

### 必演示
1. 看 `.github/workflows/0501_deployment.yml` 和 `0502_sample_agent_deployment.yml`
2. **讲师演示触发一次给大家看**——不让 10 个学员同时跑 Actions
3. 去 Foundry portal 看新的 agent 版本

### 学员动手
- 学员 fork 后改一个 prompt，push，**不等 Actions 跑完**，去做别的
- Day3 早上回看结果

### 常见坑
- Service Principal 凭据没配——讲怎么在 GitHub Secrets 配 `AZURE_CREDENTIALS`
- REST API 版本变化——`api-version=2025-11-15-preview` 可能已不是最新

### 节奏
讲解 15 分钟 + 演示 15 分钟 + 学员 push 15 分钟。

---

## Day 2 - 匿名反馈（15 分钟）

同 Day1，加一个问题："对综合作业题目有什么疑问？"

---

## Day 3 - 回看 Day2 push 的 Actions + Q&A（30 分钟）

### 必做
1. 让每个学员展示自己昨天 push 的 Actions 结果
2. 对失败的现场 debug
3. 把成功的 agent version 在 Foundry portal 展示出来

---

## Day 3 - Ex06 红队评估（120 分钟）

### 核心目标
学员能跑红队评估（UI + 代码两种），能自定义攻击 prompt 和 strategy。

### 必讲
1. **红队 = AI 安全测试**：模拟攻击找 agent 弱点
2. **两种入口**：Foundry UI（无代码）+ `azure-ai-evaluation[redteam]` SDK（代码）
3. **关键 API**：
   - `RedTeam(azure_ai_project=, credential=, risk_categories=, num_objectives=)`
   - `await red_team_agent.scan(target=, attack_strategies=)`
4. **PyRIT 集成**：`OpenAIChatTarget` 是 PyRIT 的，不是 azure-ai-evaluation 的
5. **攻击策略层次**：单技术（Flip/ROT13/Base64）→ EASY 预设 → MODERATE → custom

### 必演示
1. **先 UI 跑一次**（提交后会跑 30+ 分钟，先提交再讲代码）
2. 写 `redTeamingAgent_initializer.py`，本地跑一次（5 分钟）
3. 改 target 为 cora agent，再跑
4. 用 custom_attack_seed_prompts JSON
5. 加 `attack_strategies=[Flip, ROT13, Base64, AnsiAttack, Tense]`
6. **回头看最早提交的 UI 红队**结果，对比分析

### 常见坑
| 坑 | 症状 | 解法 |
|----|------|------|
| RiskCategory 枚举名变化 | `AttributeError: SelfHarm` | 1.16 实际枚举名以 `dir(RiskCategory)` 为准 |
| PyRIT target 用 token_provider 报错 | API 要 str，传了 callable | 这是 workshop 的"巧用"，跑前自己验过 |
| 异步 vs 同步 target | `coroutine was never awaited` | scan 内部会调用，确保 target 函数签名匹配 |
| 红队跑 1 小时还没完 | 正常，去做别的 | num_objectives 调小到 3 测试 |

### Q&A 预案
- "ASR 是什么"——Attack Success Rate，攻击成功率，越低越安全
- "结果在哪里看"——本地 JSON 文件 + Foundry UI 评估面板
- "生产环境多久跑一次"——每次重大 prompt 改动 + 上线前 + 季度

### 节奏
讲解 30 分钟 + 演示 50 分钟 + 学员动手 40 分钟。

---

## Day 3 - 综合作业开题 + 分组 + 设计（60 分钟）

### 必讲
1. 念题：场景"Zava 客服分诊系统"
2. 必做和选做清单
3. **强调评分维度**：架构选型理由占 40%，跑通只占 40%
4. 分组（3 人一组），breakout room 分配

### 学员动手
1. 30 分钟设计（不写代码，只画图 + 说选型理由）
2. 每组提交一张架构图到共享文档
3. 讲师/助教 walkthrough 每组的设计，给反馈

---

## Day 3 - 综合作业实做（150 分钟）

### 讲师 + 助教任务
- 巡场（breakout room 之间切换）
- 不直接给代码，引导思考
- 记录每组的关键决策，演示时点评

### 常见坑（综合作业版）
| 坑 | 表现 | 提示 |
|----|------|------|
| 全用 SDK 写 | 不用 Agent Service | 提醒题目要求"分诊用 Agent Service" |
| 跳过红队 | 时间紧只跑了跑通 | 提醒红队即使 num_objectives=1 也要跑 |
| 架构图没画 | 直接撸代码 | 强制要求先画图，否则演示不及格 |

---

## Day 3 - 综合作业演示（45 分钟）

### 讲师要做的事
1. 每组 5 分钟演示 + 2 分钟提问
2. **每组必须回答**：你们为什么这样选型？
3. 现场打分（讲师 + 助教各打一份，平均）
4. 结业时公布前 3 名

### 评分维度
- 能跑通（40%）
- 架构选型理由（40%）—— **回收开场架构课**
- 观测和评估完整性（20%）

---

## Day 3 - Ex07 清理 + 成本回顾（30 分钟）

### 必讲
1. **清理顺序**：Container Apps → Cosmos → AI Foundry → Resource Group
2. **不清理的成本**：
   - **真实数字以 Azure 定价计算器为准**，培训前 1 天讲师上 https://azure.microsoft.com/pricing/calculator 自己算一遍
   - Cosmos serverless 模式：按 RU 计费，培训规模约几美元/天
   - GPT 部署不删按 TPM 月租，**50K TPM 不部署成本是 0，但部署后即使不用也按容量收费**——这是最容易忽略的成本
3. **生产环境成本控制**：缓存、采样、模型选型（mini vs full）

### 必演示
- `az group delete --name <rg> --yes --no-wait`
- 截图发助教确认清理

### 节奏
10 分钟讲解 + 20 分钟学员清理 + 截图验收。

---

## Day 3 - 结业 + 后续学习路径（30 分钟）

### 必讲
1. **推荐后续学习顺序**：
   - `microsoft/agent-framework` repo 的所有 samples
   - Learn 文档的 Workflows 进阶
   - PyRIT 官方文档（红队深挖）
   - Foundry Agent Service 生产化最佳实践（Learn）
2. **本次培训的局限**：没讲 Azure AI Search RAG、没讲 voice agent、没讲生产可观测性调优
3. **培训交流群保持开放**，遇到问题继续讨论
4. 颁奖（前 3 名小组）
5. 合影

---

## 附录 A：助教记录模板

每个时段开始时新建一行，记录：

| 时间 | 学员 | 问题 | 解决方案 | 是否升级到主讲 |
|------|------|------|----------|----------------|
| 10:15 | 张三 | Bicep 部署 403 | 检查 RBAC，加 Contributor | 否 |
| 10:30 | 李四 | DefaultAzureCredential 失败 | az login 重登 + 装 keyring | 否 |
| 11:20 | 全体 | GPT 429 | 主讲拉 TPM 到 50K | **是** |

每天结束发给主讲，作为次日开场的反馈输入。

---

## 附录 B：备用方案

| 风险 | 备用方案 |
|------|----------|
| 个别学员订阅没开 | 让他/她结对动手，跟着别人看 |
| 整体网络问题 | 切到 Foundry portal 演示部分，跳过代码部分 |
| GPT 集体 429 | 启用预备的备用订阅 / 模型 |
| Ex03 代码 bug 改造没生效 | 现场打补丁（使用准备好的修复版代码包） |
| Foundry portal UI 已变化 | 讲师培训前 1 天验过的截图救场 |
| Day2 综合作业题目反馈不满意 | Day3 开场可现场调整必做/选做范围 |

---

## 附录 C：通用讲师注意事项

### 时间管理
- **每 60-75 分钟必须休息 15 分钟**，远程注意力集中度低
- **Ex02 和 Ex03 是大块**，给学员留充足动手时间
- **3 天版有 buffer**，不要主动加内容把 buffer 吃掉

### 远程教学技巧
- **每讲完一个概念就问"有疑问吗"**，远程学员不会主动打断
- **关键命令打在聊天区**，避免学员抄错
- **学员屏幕共享 debug**——比讲师远程指导高效 5 倍

### 助教协作
- 助教全程开聊天区，**3 分钟无人回应的问题升级给主讲**
- 助教维护一份"今日已知问题"文档（用附录 A 模板），避免重复回答
- 助教负责按时间表喊节奏，主讲只管讲
