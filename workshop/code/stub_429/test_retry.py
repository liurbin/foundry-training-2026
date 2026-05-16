"""
D5 — retry + jitter 端到端验证

跑法：
    python -m pytest test_retry.py -v
"""
from __future__ import annotations

import json
import random

import pytest

from retry_client import RetryExhausted, RetryPolicy, retry_call
from stub_server import run_server


@pytest.fixture
def stub():
    """每个用例独立起一个 stub，避免计数串。port=0 让系统选空闲端口。"""
    def _factory(fail_times: int):
        httpd, stop = run_server(port=0, fail_times=fail_times)
        port = httpd.server_address[1]
        return f"http://127.0.0.1:{port}/", stop

    stops = []

    def make(fail_times: int) -> str:
        url, stop = _factory(fail_times)
        stops.append(stop)
        return url

    yield make
    for s in stops:
        s()


def test_succeeds_after_n_429(stub) -> None:
    url = stub(fail_times=3)
    sleeps: list[float] = []
    body, attempts = retry_call(
        url,
        policy=RetryPolicy(max_retries=5, base_delay=0.01, max_delay=0.05),
        sleeper=sleeps.append,
    )
    payload = json.loads(body)
    assert payload["ok"] is True
    assert attempts == 4  # 前 3 次 429 + 第 4 次成功
    assert len(sleeps) == 3


def test_exhaust_when_fail_times_exceeds_budget(stub) -> None:
    url = stub(fail_times=10)
    with pytest.raises(RetryExhausted):
        retry_call(
            url,
            policy=RetryPolicy(max_retries=2, base_delay=0.01, max_delay=0.05),
            sleeper=lambda _s: None,
        )


def test_first_attempt_success(stub) -> None:
    url = stub(fail_times=0)
    body, attempts = retry_call(
        url,
        policy=RetryPolicy(max_retries=3, base_delay=0.01),
        sleeper=lambda _s: None,
    )
    assert attempts == 1
    assert json.loads(body)["ok"] is True


def test_backoff_respects_max_delay() -> None:
    p = RetryPolicy(base_delay=1.0, max_delay=4.0, jitter="none")
    # attempt 1..6 → 1, 2, 4, 4, 4, 4
    seq = [p.backoff(i) for i in range(1, 7)]
    assert seq == [1.0, 2.0, 4.0, 4.0, 4.0, 4.0]


def test_full_jitter_within_bounds() -> None:
    random.seed(42)
    p = RetryPolicy(base_delay=1.0, max_delay=8.0, jitter="full")
    for attempt in range(1, 6):
        for _ in range(50):
            d = p.backoff(attempt)
            assert 0 <= d <= min(8.0, 1.0 * (2 ** (attempt - 1)))


def test_retry_after_header_raises_floor() -> None:
    # 服务端要求等 5s，即便 exp backoff 只有 1s，也应当 ≥ 上界 = 5
    p = RetryPolicy(base_delay=1.0, max_delay=8.0, jitter="none")
    assert p.backoff(1, retry_after=5.0) == 5.0
