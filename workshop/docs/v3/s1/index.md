# S1：决策框架（90min，不动手）

> 时长：90 min ｜ 形式：讲师讲 + 现场决策卡 ｜ 凭证要求：无（S1 不连 endpoint）

## 这一段的目标

S1 不写代码。90 分钟全部用来对齐**决策口径**——等 S2 动手时，不再纠结"客服 agent 到底该不该上 Foundry / 单 agent 够不够"。

学完 S1 你应该能：

- 在一张 Foundry 能力地图上指出"客服 agent 用得到哪几格"
- 当场给出"客服 agent 用 / 不用 / 部分用 Foundry"的明确结论
- 选 Agent Service 还是 SDK，给出 4 维度打分依据
- 看一眼客服 agent 的能力清单，判断"单 agent 够不够、需不需要拆"

## 90min 节奏

| 时长 | 段落 | 产出 |
|---|---|---|
| 10min | Foundry 定位 + 不该用的场景 | 学员口头说出 ≥2 条"不该用 Foundry"的场景 |
| 25min | Prompt + Model 选型决策树 | 当场对照客服 agent 填一份决策卡 |
| 25min | 单 agent vs 多 agent 决策框架 | 客服 agent 单 agent 够 / 不够 + 一条理由 |
| 20min | 讲师 demo：codex CLI 起 agent | 学员看完能复述"自然语言 → 命令 → 人审 → 执行"循环 |
| 10min | Q&A + S2 预告 | 所有学员 `codex --version` 有输出 |

## 一、Foundry 能力地图（10 min）

蒸馏自 v2 D1。完整 14 格地图见 v2，v3 短课聚焦客服 agent 用得到的 **7 格**：

| 格子 | 客服 agent 用法 |
|---|---|
| Agent Service | 托管 agent 运行时（替代自己写 loop） |
| Models | 选 LLM（gpt-4o / 4o-mini 在客服场景的取舍） |
| Connections | 接 mock_orders.json 数据源（生产替换为真接口） |
| Tracing | 看每条对话的 span / token 消耗 |
| Evaluations | 跑评测数据集（S2 动手 1 用） |
| Red Team | 跑对抗数据集（S2 动手 2 参考） |
| Quotas | 看 deployment 配额 / 限流 |

**不该用 Foundry 的 4 类场景**（决策训练，学员口头答 2 条即可）：

1. agent 形态不成立——业务里 LLM 只是"翻译/分类"，没有 tool use / 多轮，直接 Azure OpenAI 即可
2. 私有部署强制——客户合同要求模型权重落到自己数据中心
3. 编排已自建——已有成熟的 LangGraph / 自己的 orchestrator，迁移成本 > 收益
4. 数据驻留特殊——客户要求数据不出某个 region 而该 region 没有 Foundry

**讨论**（5 min）：客服 agent 这 4 条命中哪几条？默认不命中，但要能讲清"为什么不命中"。

## 二、客服 agent 决策卡（25 min）

> 决策卡蒸馏自 v2 D1/02 + D2/01-02。v3 把"我的项目"全部替换为客服 agent 作为统一示例。

### 决策卡（学员当场填，**不要看下面的参考答案**）

| 维度 | 你的判断 | 你的理由 |
|---|---|---|
| **托管 vs 自建** | 托管 / 自建 / 部分 | |
| **模型选择**（gpt-4o / 4o-mini / 其他） | | |
| **多模态**（需要 / 不需要） | | |
| **Tool use**（必需 / 不需要） | | |
| **多轮上下文**（必需 / 不需要） | | |
| **流式输出**（必需 / 可选 / 不要） | | |
| **结论**（一句话） | | — |

填完之后再翻下面的参考答案对照——讨论 5 min 后讲师收一份当面 review。

??? note "参考答案（先填完自己的再展开）"
    | 维度 | 客服 agent 倾向 | 理由 |
    |---|---|---|
    | 托管 vs 自建 | 倾向托管（Agent Service） | 客服没有"自定义控制流"诉求，省 ops |
    | 模型选择 | gpt-4o-mini 起步，复杂 case 升 4o | 客服多数 query 简单，省成本 |
    | 多模态 | 不需要 | 客服文本即可（除非有图片上传需求） |
    | Tool use | 必需 | 查订单/物流/退款工单都要 tool |
    | 多轮上下文 | 必需 | 至少要记得用户问的是哪个订单 |
    | 流式输出 | 可选 | 体验加分但不阻塞 |
    | 结论 | Agent Service + gpt-4o-mini + function calling | — |

讨论点：

- 如果业务要求 SLA 30s 内回复，gpt-4o vs 4o-mini 的延迟差怎么权衡？
- 如果客服要支持图片（"我的快递盒破了"上传图片），决策卡哪几行要改？

## 三、单 vs 多 agent 框架（25 min）

蒸馏自 v2 D7 决策段。**v3 只讲框架，不做 handoff 实操**。

### 三问决策

1. **职责能不能在一个 system prompt 里讲清**？能 → 单 agent
2. **需不需要在子任务间显式编排**（例如"先查订单 → 判断是否符合退货 → 创建工单"必须按序）？需要 → 考虑 as_tool 或 Agent Service 的 multi-step
3. **是否要稳定的 tool 调用图**（生产化要 trace / replay）？要 → Agent Service 原生多 agent

### 客服 agent 落点

- **v3 课中**：单 agent + function calling 就够（订单查询 / 物流 / 退款工单 = 三个 tool）
- **生产化路径**：客诉升级走另一个 agent（"客诉处理 agent"），主 agent 调它做 as_tool
- **不要做**：HandoffService 那种全自动 agent 间 handoff——客服场景不允许 agent 间无审计的状态转移

讨论点：客服场景的"客诉升级"是不是必须独立 agent？口头答即可。

## 四、讲师 demo：codex CLI 起 agent（20 min）

学员**看不动手**。讲师在投屏上完整演示：

1. `cd ~/foundry-training-tmp` + 确认 `OPENAI_BASE_URL` 指向真 endpoint
2. 进 codex 交互模式：`codex`，把 prompt"用 azure-ai-projects SDK 起一个最小 agent，连环境变量里的 endpoint，回答 hello world"贴进去
3. 学员观察：codex 给的方案 → 讲师审 → 让 codex 执行 → 看到 hello world
4. 讲师指出三件事：
   - codex CLI 的"建议 → 人审 → 执行"循环（**人不放权，但人不写代码**）
   - 它装包 / 写 .env / 调用 SDK 全程在做，讲师在审而不在敲
   - 这就是 S2 全程动手的姿势

学员产出：能口头复述这个循环。

## 五、Q&A + S2 预告（10 min）

- 所有学员当场跑一次 `codex --version` + `echo $OPENAI_BASE_URL`，确认环境就绪
- S2 第一段动手 0 把刚才讲师 demo 的事情你自己做一遍

## 课后扩展

S1 没讲透的内容（4h 课只能这样）：

- v2 D1：14 格能力地图完整版 + 4 条反例（LangGraph 对比 / 锁定担忧）→ `workshop/docs/d01_concepts/`
- v2 D2：成本估算 + 5 类硬约束 → `workshop/docs/d02_agent_vs_sdk/`
- v2 D7：多 agent 三选一实操 → `workshop/docs/d07_multi_agent/`
- v2 D10：边界表 14 行完整版 → `workshop/docs/d10_boundary/`
