# 动手 0：起客服 agent + 跑通第一条对话（10min 开场 + 20min 动手 = 30min）

> 时长：30 min（含 S2 开场 10min）｜ 形式：codex CLI 动手 ｜ 凭证：环境变量已配好（见课前引导）
> 状态：⚠️ 具体话术待讲师 Day-7 实测后补；当前是骨架

## 开场：评测先行（10 min，讲师讲）

蒸馏自 v2 D7 + D9 的核心论点：

- **写功能前先写评测**——agent 输出是概率性的，没评测就没"做完"的客观标准
- v3 的姿势：动手 0 先把 agent 跑通（最小集），动手 1 立刻写评测，动手 2 加防护再跑回评测——**评测贯穿 S2 全程**
- 今天用的 endpoint 是讲师统一发的 Azure OpenAI，业务数据全 mock（见 [scenario.md](../scenario.md)）

## 这一段你要做什么（20 min 动手）

用 codex CLI 让 AI 帮你：

1. 装 `azure-ai-projects` SDK（或同等 Foundry SDK）
2. 写一个最小 agent，从环境变量读 endpoint
3. 让 agent 回答一次"我要查订单 ORD-T-12345"
4. 在 portal / trace 里看到这次调用的 span

**简化约定**：动手 0 把订单数据**hardcode 在 agent 代码里**（不调 function / 不读 mock JSON）。这是为了 20min 内能跑通——function calling + mock JSON 留到课后扩展。scenario.md 里描述的"调 mock_orders.json"是 P1 目标，不是动手 0 目标。

## 准备

新开终端，cd 到一个工作目录：

```bash
mkdir -p ~/foundry-v3 && cd ~/foundry-v3
# 确认环境变量在
echo $OPENAI_BASE_URL    # 应该是讲师发的 endpoint
echo $OPENAI_API_KEY | head -c 8 && echo "..."  # 别全打
```

## 步骤 1：让 codex 起 agent（10 min）

进入 codex 交互模式：

```bash
codex
```

进入后，给它这段需求（**这是 v3 推荐 prompt 模板，讲师 Day-7 会迭代**）：

```
帮我用 azure-ai-projects SDK（或当前 Foundry 推荐 SDK）写一个最小 Python agent：

1. 从环境变量 OPENAI_BASE_URL / OPENAI_API_KEY / OPENAI_API_VERSION 读凭证
2. agent 名字叫 customer_service_agent
3. system prompt 告诉它："你是一家电商的客服助手。可以查询订单状态、物流、退款进度。
   不要承诺退款，不要主动外呼，遇到客诉升级类话术转人工。"
4. 现在不需要真接 tool，先 hardcode 返回"订单 ORD-T-12345 已发货，预计明日到达"
5. main 里跑一次："我要查订单 ORD-T-12345"，把回复打印出来

写完执行它，把输出贴回来。
```

**关键**：codex 给你方案时**先审再让它执行**——看它装的包对不对、凭证读法对不对、有没有把 key 泄到日志里。

### 期望输出（讲师 Day-7 补真实示例）

```
[预期 agent 回复样例：]
您查询的订单 ORD-T-12345 已发货，预计明日到达，
物流单号 SF1234567890。如有其他问题请告诉我。
```

`TODO 讲师 Day-7`：贴一段真实跑出来的对话 + 截图。

## 步骤 2：在 portal / trace 里看这次调用（5 min）

打开讲师发的 Azure AI Foundry portal 链接，找到你的 deployment → Tracing 标签。

期望看到（蒸馏自 v2 D3/03）：

- ✅ 至少 1 个顶层 span（agent 调用本身）
- ✅ token 计数（输入 + 输出）
- ✅ 时延（端到端 ms）

看不到？常见原因：

- portal 链接错（讲师发的链接是否对应你的 deployment？）
- trace 异步未到（等 30s 刷新）
- agent 没真跑（步骤 1 输出是 codex 编的样例文字，不是真 LLM 调用——回去审 codex 给的代码）

## 步骤 3：自检（5 min）

- [ ] 步骤 1 的 Python 脚本在你机器上**真跑过一次**（不是 codex 编的示例）
- [ ] 看到一段中文回复，内容含订单号 + ETA + 物流单号
- [ ] portal trace 看到至少 1 个 span + token 计数
- [ ] 你能用一句话讲清"刚才 codex 做了什么、我审了哪几个点"

3 项打勾即动手 0 pass（对应§评分"实操"维度的第一条）。

## 常见卡点（讲师 Day-7 补）

| 现象 | 处理 |
|---|---|
| `ModuleNotFoundError: azure.ai.projects` | codex 装包用 `--user` 装到了用户目录，PYTHONPATH 没指过去——让 codex 用 venv |
| 401 from endpoint | `OPENAI_API_KEY` 没生效；新开 terminal `source ~/.zshrc` |
| API version 报错 | `OPENAI_API_VERSION` 拼错 / 太老，用讲师给的版本 |
| codex 反复改代码不收敛 | 明确告诉它"先停下，把当前错误 stacktrace 完整贴出来再改" |
| 真跑了但 trace 看不到 | tracing 默认开启吗？讲师 Day-7 确认 |

## 课后扩展

- 把 hardcode 的"订单已发货"替换成真的从 `mock_orders.json` 读（场景文件已列）
- 加 function calling：定义 `query_order(order_id)` tool，让 agent 自己调
- 把 agent 改成流式输出（streaming）

→ 下一段 [动手 1：写评测](01-eval.md)
