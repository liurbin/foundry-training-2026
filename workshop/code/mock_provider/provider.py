"""
D4 — Provider 抽象（学员侧 mock 实现）

约束（来自 handbook D4）：
- 接口里不准出现 provider 专有字段（thread_id / tool_choice 等）
- 共性参数走结构化字段，专有参数走 **opts
- MockProvider 不要带状态、不要模拟错误（那是 fixture 的活）
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal, Protocol, runtime_checkable


Role = Literal["system", "user", "assistant"]


@dataclass(frozen=True)
class Message:
    """对话消息。字段刻意保持最小集——加字段先问自己是不是 provider 专有。"""
    role: Role
    content: str


@dataclass(frozen=True)
class Usage:
    prompt_tokens: int
    completion_tokens: int

    @property
    def total_tokens(self) -> int:
        return self.prompt_tokens + self.completion_tokens


@dataclass(frozen=True)
class ChatResponse:
    content: str
    model: str
    usage: Usage
    # provider 专有的原始响应放这里，业务层不该读
    raw: dict[str, Any] = field(default_factory=dict)


@runtime_checkable
class ChatProvider(Protocol):
    """业务层依赖这个，不依赖任何具体 SDK。"""

    async def chat(
        self,
        messages: list[Message],
        *,
        model: str = "default",
        temperature: float = 0.7,
        max_tokens: int = 512,
        stop: list[str] | None = None,
        **opts: Any,
    ) -> ChatResponse: ...


# ---------------------------------------------------------------------------
# MockProvider
# ---------------------------------------------------------------------------

# 写死的关键词触发表——故意做得很笨，不要扩成"小型 LLM"
_KEYWORD_RESPONSES: dict[str, str] = {
    "ping": "pong",
    "hello": "你好，我是 MockProvider，仅用于本地跑通 abstraction。",
    "你好": "你好，我是 MockProvider，仅用于本地跑通 abstraction。",
    "error": "[mock] 不要让我模拟错误，去 pytest fixture 里写 raise。",
}

_DEFAULT_REPLY = "[mock] 已收到 {n} 条消息，最后一条预览：{preview}"


def _last_user_text(messages: list[Message]) -> str:
    for m in reversed(messages):
        if m.role == "user":
            return m.content
    return ""


def _fake_token_count(text: str) -> int:
    # 简单近似：4 字符 ≈ 1 token；够 D4 跑通就行
    return max(1, len(text) // 4)


class MockProvider:
    """
    无依赖、无网络、可复现的 ChatProvider 实现。

    用途：
        - 让业务代码在没有 Azure / OpenAI 凭证时也能跑通
        - 给契约测试当被测对象

    不该做：
        - 不模拟 429 / 5xx（让 stub_server 干）
        - 不维护对话状态
        - 不调任何 SDK
    """

    def __init__(self, *, model_name: str = "mock-1") -> None:
        self.model_name = model_name

    async def chat(
        self,
        messages: list[Message],
        *,
        model: str = "default",
        temperature: float = 0.7,
        max_tokens: int = 512,
        stop: list[str] | None = None,
        **opts: Any,
    ) -> ChatResponse:
        # 故意忽略 temperature / max_tokens / stop：mock 不模拟采样
        # opts 故意吞掉：provider 专有参数到这里就该消失
        last = _last_user_text(messages).strip().lower()
        reply: str | None = None
        for kw, text in _KEYWORD_RESPONSES.items():
            if kw in last:
                reply = text
                break
        if reply is None:
            preview = last[:40] + ("…" if len(last) > 40 else "")
            reply = _DEFAULT_REPLY.format(n=len(messages), preview=preview)

        prompt_tokens = sum(_fake_token_count(m.content) for m in messages)
        return ChatResponse(
            content=reply,
            model=f"{self.model_name}/{model}",
            usage=Usage(
                prompt_tokens=prompt_tokens,
                completion_tokens=_fake_token_count(reply),
            ),
            raw={"mock": True},
        )


# ---------------------------------------------------------------------------
# 手跑入口：python3 provider.py
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import asyncio

    async def _demo() -> None:
        p = MockProvider()
        r = await p.chat([Message("user", "ping")])
        print("chat:", r.content, "| usage:", r.usage)

    asyncio.run(_demo())
