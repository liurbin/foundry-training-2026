# mock_provider

D4 学员主线配套代码：在 **没有任何 Azure / OpenAI 凭证** 的机器上验证 provider 抽象是否真的解耦。

## 用途

- 给业务代码一个不依赖任何 SDK 的 `ChatProvider` 实现
- 单元测试 / 本地跑通 abstraction（contract test 用）
- 断网 / 无 key 环境下让学员能继续推进 D4

> 不是 mock 框架。如果你想 mock 错误 / 状态机，写 pytest fixture，**不要把状态塞进 MockProvider**（D4 negative example #4）。

## 接口契约（Protocol）

```python
class ChatProvider(Protocol):
    async def chat(self, messages: list[Message], **opts) -> ChatResponse: ...
```

- `Message`：`role`（"system" | "user" | "assistant"）+ `content`
- `ChatResponse`：`content` + `model` + `usage`（prompt_tokens / completion_tokens）
- 共性参数走结构化字段（temperature / max_tokens / stop）
- provider 专有参数走 `**opts` 透传，**不准**进接口签名

> 最小接口原则：现在只有 `chat()`。需要 embedding 时再加 `embed()` 方法 + 测试 + 实现；不准提前加（D4 negative example #1：不要"以备将来"塞抽象）。

## 怎么跑

```bash
cd workshop/code/mock_provider
python3 -m pytest test_provider.py -v
# 或者手跑：
python3 provider.py
```

零依赖，Python 3.10+ stdlib 足够。

## 文件

- `provider.py` — Protocol 定义 + MockProvider 实现
- `test_provider.py` — pytest 契约测试
