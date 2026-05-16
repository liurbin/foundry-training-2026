> 抽自 docs/01-instructor-handbook-v2.md D4 模块；同步规则见 docs/02-instructor-prep-checklist.md

# 让 AI 帮我写一层 provider 抽象

## 目标
我的业务代码不直接依赖 Foundry SDK 或 OpenAI SDK，而是依赖一个 ChatProvider 接口。
今天能在 Foundry / mock 之间切，未来能加第三方 provider（Anthropic / 自托管）。

## 接口定义（学员必须先想清楚）
```python
class ChatProvider(Protocol):
    async def chat(self, messages: list[Message], **opts) -> ChatResponse: ...
```

## 让 AI 生成的产物清单
1. ChatProvider 接口（含 Message / ChatResponse 的最小字段）
2. FoundryProvider 实现（包 Foundry SDK 调用）
3. MockProvider 实现（学员侧，返回写死文本，用于不依赖真 key 跑 abstraction）
4. 一个 switch 配置（env 变量决定加载哪个 provider）
5. 单元测试：MockProvider 通 + FoundryProvider 用 contract test 框（不强求真调）

## 约束
- 接口里不准出现任何 provider 专有概念（不准有 Foundry 的 thread_id、不准有 OpenAI 的 tool_choice）
- 共性参数（temperature / max_tokens / stop）走结构化字段；provider 专有参数走 **opts 透传
- 不写"抽象工厂的工厂"——一个 if/elif 就够

## 自验证
- [ ] MockProvider 在没有任何 Azure 凭证的机器上能跑
- [ ] 业务代码 grep 不到 "azure" 或 "openai" 字符串（除 provider 实现文件外）
- [ ] 加第三个 provider 不需要改业务代码，只加一个文件
