# 短课 v3：4 小时压缩版（S1 90min + S2 150min）

> 状态：📝 stub / 设计中，**未经讲师 Day-7 验收**
> 与 v2 关系：独立课程变体，不是 v2 的子集（见下文§"与 v2 的边界"）
> 最后更新：2026-05-21

## 定位

**一句话**：用 AI 工程师的姿势做 AI 工程——4 小时内，让学员体验"自然语言驱动 AI CLI → AI 执行 → 人审 → 提交"的完整闭环，从起 agent 资源到跑评测再到加 guardrail。

**适合谁**：

- 有 Azure 背景的 L300 工程师
- 课前能自助装 codex CLI + 跑通 hello-world（见 prerequisites）
- 想看"AI 起 AI"的实际工作流，而不是 IaC 教学

**不适合谁**：

- 想系统学完 11 模块 → 上 v2 三天班
- 没装机能力 / 公司网络拦截 OpenAI 域名 → 上 v2 无订阅版本

## 与 v2 的边界

| 维度 | v2（3 天 11 模块） | v3（4h 短课） |
|---|---|---|
| 学员凭证假设 | **无** Azure 订阅，全程 mock | **有** Azure OpenAI endpoint+key（讲师发） |
| 模块覆盖 | 11 模块完整（D1..D11） | 抽 D1/D2/D3/D7/D8/D9 精华 |
| 部署 | D5 Bicep / azd | codex CLI 调 SDK，**不用 Bicep** |
| 评分 rubric | 5 维度加权 | **3 维 pass/fail**（决策 / 实操 / 安全） |
| 项目假设 | 学员带自己项目讨论 | **统一 demo 场景**（客服 agent，讲师提供） |
| workshop 代码 | `workshop/code/` mock provider 主路径 | **独立 `workshop/docs/v3/`** 子树（学员只看 v3 nav） |
| 综合作业 | D11 ~2h 完整版 | 课中跑哪段算哪段，**未完成部分进课后自学包**（不强行 4h 内塞完） |

v3 不替代 v2，也不冻结 v2。两份并存。`workshop/docs/v3/` 是 v2 学员站点下的独立分支，nav 隔离即可，物理上共用 mkdocs 配置。

## Prerequisites（课前）

学员侧：

- macOS（其他系统联系讲师）
- 完成 [`workshop/docs/v3/prerequisites/codex-cli-setup.md`](../workshop/v3/prerequisites/codex-cli-setup.md) 全部 4 条自检
- **不要求带项目**——v3 全程用统一 demo 场景（客服 agent），降低节奏风险

讲师侧（Day-7 gating，见§Day-7 清单）：

- Azure OpenAI 资源起好、deployment 暴露、key 私信发放
- 学员引导自己跑过一遍，补完报错表
- `workshop/docs/v3/code/eval_harness.py` 骨架就绪（见§动手 1）

## S1 议程（90min，决策框架，不动手）

| 时长 | 段落 | 产出 / 验收 |
|---|---|---|
| 10min | Foundry 定位：vs Azure OpenAI / vs 自建 / 何时不用 | 学员能口头说出至少 2 条"不应该用 Foundry"的场景 |
| 25min | Prompt + Model 选型决策树 | 学员对照**今天的 demo 客服 agent 场景**，给出"用哪个 model + 为什么"的一行结论 |
| 25min | 单 agent vs 多 agent 决策框架（讲框架，不动手） | 学员能说"客服 agent 场景单 agent 够 / 不够，理由 X" |
| 20min | 讲师 demo：用 codex CLI 起一个最小 agent（学员看不动手） | 学员看完能复述 codex CLI 的"自然语言→命令→人审→执行"循环 |
| 10min | Q&A + S2 预告（学员确认 codex CLI 环境就绪） | 所有学员 `codex --version` 有输出 |

**S1 不动手**——这 90min 全部用来对齐决策口径，避免 S2 动手时学员还在纠结"该不该用 Foundry"。

**统一 demo 场景**：客服 agent（处理订单查询 / 退款请求 / 一般 FAQ）。完整场景见 [`workshop/docs/v3/scenario.md`](../workshop/v3/scenario.md)。S1 第 25min 段和 S2 全程都围绕这个场景。

## S2 议程（150min，codex CLI 副驾驶动手）

> 注：4h 是建议节奏，**完整性优先于"当堂跑完"**——动手 0/1/2 哪段没跑完就进课后自学包接着做。

| 时长 | 段落 | 真订阅用途 |
|---|---|---|
| 10min | S2 开场：评测先行论点 + 今天 endpoint + scenario 说明（动手 0 文件开头） | — |
| 20min | **动手 0**：codex CLI 起一个客服 agent + 连 endpoint，跑通"订单状态查询"对话（hardcode 简化，function calling 留课后） | ✅ 真调用 |
| 55min | **动手 1**：让 codex CLI 往 `eval_harness.py` 骨架里加 3 条评测 case，跑 pass/fail | ✅ 真调用 |
| 15min | Red Team 框架 + 讲师 demo 一条 attack（动手 2 文件开头） | 讲师 demo |
| 35min | **动手 2**：让 codex CLI 帮你加一条 guardrail，跑回评测验证 | ✅ 真调用 |
| 15min | 可观测 + 上线 checklist + 课后自学包（链 v2 / workshop / specs） | — |

合计 150min。

### 动手段落骨架（讲师 Day-7 实测后补完整脚本）

> ⚠️ 以下逐步骤脚本在讲师 Day-7 实测后写入，stub 阶段只列骨架。

**动手 0（20min）骨架**：
- 学员在 `workshop/docs/v3/scenario.md` 里读到"客服 agent 要处理订单查询"
- `codex "帮我用 azure-ai-projects SDK 起一个客服 agent，从环境变量读 endpoint，能回答订单状态查询"`
- 审 → 执行 → 跑通至少一条对话
- `TODO`：讲师实测后补具体话术 / 常见报错 / SDK 包版本锁定

**动手 1（55min）骨架**：
- 讲师提供 `workshop/docs/v3/code/eval_harness.py` 骨架（~30 行 pytest-style，含 1 条示例 case）
- 学员 `codex "往这个 harness 里加 2 条 case：1 条 edge（订单号格式错误，agent 应反问）、1 条对抗（客诉升级伪装，agent 不越权承诺退款）"`
- 跑 `pytest eval_harness.py` 看 pass/fail
- 至少 2 条产出明确 pass/fail 判定才算通过
- `TODO`：3 条 case 的具体 expected 行为；harness 怎么调用真 endpoint（讲师 Day-7 决定 mock judge 还是 LLM-as-judge）

**动手 2（35min）骨架**：
- 学员选 1 条 attack（prompt injection / jailbreak / PII 套取，三选一）
- `codex "帮我在 agent 的 system prompt / input filter / output filter 里加一条 guardrail 防住这个 attack"`
- 跑回动手 1 的 harness + 那条 attack case
- **"挡不住"算 pass**：只要学员能口头讲清"挡不住的原因 + 下一步会怎么做"即可（见§评分）
- `TODO`：3 条 attack 的具体 payload；guardrail 形态是否限制

## 评分口径（3 维 pass/fail）

| 维度 | pass 的标准 |
|---|---|
| **决策** | 能口头说出"客服 agent 场景用 / 不用 / 部分用 Foundry"的明确结论 + 一条理由（覆盖 S1 第 25min 段） |
| **实操** | 动手 0 跑通 1 条对话；动手 1 至少 2 条评测 case 产出明确 pass/fail 判定 |
| **安全** | 能口头讲清"我加的 guardrail 防的是哪类 attack，为什么这一类对客服 agent 场景重要"；guardrail 实际挡住与否不影响 pass |

3 维全 pass = 课程通过。任何 1 维 fail 不影响发放课程材料，但讲师会在课后跟进。

**为什么"挡不住"也算 pass**：短课的目标是让学员**理解 guardrail 的设计动机**，不是让他们 30min 内做出生产级防护。讲清"为什么挡不住"比"看起来挡住了"更接近真实工程。

**不用 5 维**的原因：5 维度评估流程本身要 ~30min，短课塞不下。3 维 pass/fail 学员当堂能自评。

## Day-7 讲师 gating 清单

讲师在课前 7 天必须完成（这部分 agent 帮不上）：

- [ ] Azure OpenAI 资源开通（订阅、region、配额）
- [ ] 起好 deployment（推荐 gpt-4o 或同级），记录 deployment 名 + API version
- [ ] 为每位学员生成 key（或共享 key + 配额告知）
- [ ] 自己跑一遍 `workshop/docs/v3/prerequisites/codex-cli-setup.md`，把"常见报错"表里的占位补成实测案例
- [ ] 校对 [`workshop/docs/v3/scenario.md`](../workshop/v3/scenario.md)：业务设定（GMV / 监管热线 / 客诉口径）符合你的目标受众
- [ ] 写 `workshop/docs/v3/code/eval_harness.py` 骨架（~30 行，pytest-style，1 条示例 case）
- [ ] 写 `workshop/docs/v3/code/mock_orders.json` / `mock_logistics.json` / `mock_kb.md`（场景里列的 mock 数据）
- [ ] 准备 3 条 attack payload（prompt injection / jailbreak / PII），写在内部 runbook
- [ ] 自己跑一遍 S2 动手 0/1/2，把"具体步骤"骨架补成最终脚本
- [ ] **挂 v3 nav 到 `mkdocs.yml` 和 `mkdocs.en.yml`**（英文站可先指向中文 placeholder 或暂时不挂英文）
- [ ] 跑 `mkdocs build --strict` + `mkdocs build --strict -f mkdocs.en.yml`，确认零断链
- [ ] 准备课后订阅/key 失效流程，写在内部 runbook（不入这份学员文档）
- [ ] 准备网络兜底方案（公司网络拦截 OpenAI 域名时的备用 endpoint / 代理建议）

## 课后自学包

学员课后可以接着跑的内容（短课砍掉的综合作业留在这里做）：

- **综合作业**（短课没做的）：把客服 agent 换成你自己项目的场景，重跑动手 0/1/2
- v2 三天班完整版（如果想系统学）：`docs/00-training-plan-v2.md`
- workshop/ 12 模块 × 45 子任务（无订阅可跑）：`workshop/docs/`
- 11 个 spec（拿 codex CLI 自己挂着练）：`prep-artifacts/day-7/specs/`

## 开放问题（待讲师 Day-7 前后拍）

1. `eval_harness.py` 判定方式：mock string match / 正则 / LLM-as-judge？影响动手 1 的"明确 pass/fail"门槛
2. attack payload 是否提前发给学员看，还是动手 2 现场拆？提前发省时间但失去探索感
3. 课后自学包的"综合作业"要不要做一份独立 `v3-followup.md`？还是就在这份文档里
