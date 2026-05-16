"""
D4 — MockProvider 契约测试

跑法：
    python -m pytest test_provider.py -v

这里测的是 *接口契约*，不是 mock 内部细节。
将来真接 FoundryProvider，可以把 fixture 换成它，同一组用例应当通过
（除了显式 mock-only 的几条）。
"""
from __future__ import annotations

import asyncio
import inspect

import pytest

from provider import ChatProvider, ChatResponse, Message, MockProvider, Usage


# ---------------------------------------------------------------------------
# fixture：换 provider 时只动这里
# ---------------------------------------------------------------------------
@pytest.fixture
def provider() -> ChatProvider:
    return MockProvider()


# ---------------------------------------------------------------------------
# 接口契约
# ---------------------------------------------------------------------------
def test_provider_satisfies_protocol(provider: ChatProvider) -> None:
    # runtime_checkable Protocol：isinstance 必须真
    assert isinstance(provider, ChatProvider)


def test_chat_signature_has_no_provider_specific_fields() -> None:
    # 接口里不准出现 thread_id / tool_choice 这类专有字段
    sig = inspect.signature(MockProvider.chat)
    forbidden = {"thread_id", "tool_choice", "tool_resources", "assistant_id"}
    leaked = forbidden & set(sig.parameters)
    assert not leaked, f"接口被污染：{leaked}"


def test_chat_returns_chat_response(provider: ChatProvider) -> None:
    r = asyncio.run(provider.chat([Message("user", "ping")]))
    assert isinstance(r, ChatResponse)
    assert isinstance(r.usage, Usage)
    assert r.content
    assert r.usage.total_tokens > 0


def test_chat_keyword_trigger(provider: ChatProvider) -> None:
    r = asyncio.run(provider.chat([Message("user", "ping")]))
    assert "pong" in r.content.lower()


def test_chat_default_reply_when_no_keyword(provider: ChatProvider) -> None:
    r = asyncio.run(provider.chat([Message("user", "随便说点别的")]))
    assert "[mock]" in r.content


def test_chat_swallows_provider_specific_opts(provider: ChatProvider) -> None:
    # 任意 opts 都不该让接口炸——这是 **opts 透传的意义
    r = asyncio.run(
        provider.chat(
            [Message("user", "hello")],
            thread_id="abc",  # Foundry 专有
            tool_choice="auto",  # OpenAI 专有
        )
    )
    assert isinstance(r, ChatResponse)


# ---------------------------------------------------------------------------
# 反例守护：让"MockProvider 太聪明"早点被发现
# ---------------------------------------------------------------------------
def test_mock_provider_is_stateless() -> None:
    """两次同样的调用，结果应当一致——禁止偷偷加状态。"""
    p = MockProvider()
    r1 = asyncio.run(p.chat([Message("user", "ping")]))
    r2 = asyncio.run(p.chat([Message("user", "ping")]))
    assert r1.content == r2.content
