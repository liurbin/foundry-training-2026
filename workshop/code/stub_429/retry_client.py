"""
D5 — 带 full jitter 的指数退避

把这套逻辑放到 *provider / HTTP 客户端层*，业务层不要再写第二份
（handbook D5 negative example #2）。

用法（CLI）：
    python retry_client.py --url http://127.0.0.1:18429/ --max-retries 5

库用法：
    from retry_client import retry_call
    body, attempts = retry_call("http://...", max_retries=3)
"""
from __future__ import annotations

import argparse
import json
import logging
import random
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Callable

log = logging.getLogger("retry_client")


# 视为可重试的状态码：429 + 5xx
_RETRYABLE_STATUS = {429, 500, 502, 503, 504}


class RetryExhausted(RuntimeError):
    """重试用尽仍失败。包业务层不该自己再 catch 429。"""


@dataclass
class RetryPolicy:
    max_retries: int = 3          # 不准无限重试
    base_delay: float = 0.5       # 指数底数
    max_delay: float = 8.0        # 退避封顶，防止单次睡太久
    jitter: str = "full"          # "full" | "none"，推荐 full

    def backoff(self, attempt: int, retry_after: float | None = None) -> float:
        """
        attempt 从 1 开始。返回本次应当 sleep 的秒数。

        - 服务端给了 Retry-After 视为**硬下界**：实际 sleep 必须 >= Retry-After。
        - full jitter 在 [exp_backoff, exp_backoff*2) 之间随机，整体再被 max_delay 封顶。
        - 这样既遵守服务端语义，又避免多副本同步重试导致 thundering herd。
        """
        exp = min(self.max_delay, self.base_delay * (2 ** (attempt - 1)))
        if self.jitter == "full":
            # AWS-style full jitter，但下界保留为 exp（不会跌破 Retry-After）
            jittered = random.uniform(exp, exp * 2)
        else:
            jittered = exp
        # Retry-After 是硬下界
        floor = max(jittered, retry_after or 0.0)
        # 再被 max_delay 封顶（避免 Retry-After 异常大时睡几分钟）
        return min(floor, max(self.max_delay, retry_after or 0.0))


def _do_request(url: str, *, timeout: float = 5.0) -> tuple[int, bytes, dict[str, str]]:
    req = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read(), dict(resp.headers.items())
    except urllib.error.HTTPError as e:
        # HTTPError 也有 status / body / headers
        return e.code, e.read() if e.fp else b"", dict(e.headers.items()) if e.headers else {}


def retry_call(
    url: str,
    *,
    policy: RetryPolicy | None = None,
    sleeper: Callable[[float], None] = time.sleep,
    timeout: float = 5.0,
) -> tuple[bytes, int]:
    """
    返回 (response_body, attempts_used)。失败抛 RetryExhausted。

    sleeper 参数化是为了让单测能注入假 sleep 验证退避序列。
    """
    p = policy or RetryPolicy()
    last_status: int | None = None

    # 最多尝试 max_retries + 1 次（首次 + N 次 retry）
    for attempt in range(1, p.max_retries + 2):
        status, body, headers = _do_request(url, timeout=timeout)
        last_status = status

        if status < 400:
            log.info("success on attempt=%d status=%d", attempt, status)
            return body, attempt

        if status not in _RETRYABLE_STATUS:
            # 不可重试错误，直接抛
            raise RetryExhausted(
                f"non-retryable status={status} body={body[:200]!r}"
            )

        if attempt > p.max_retries:
            break

        retry_after = None
        if (ra := headers.get("Retry-After")):
            try:
                retry_after = float(ra)
            except ValueError:
                retry_after = None

        delay = p.backoff(attempt, retry_after=retry_after)
        log.info(
            "retryable status=%d attempt=%d/%d sleep=%.3fs",
            status, attempt, p.max_retries, delay,
        )
        sleeper(delay)

    raise RetryExhausted(f"max_retries exhausted, last_status={last_status}")


def _main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--max-retries", type=int, default=3)
    ap.add_argument("--base-delay", type=float, default=0.5)
    ap.add_argument("--max-delay", type=float, default=8.0)
    args = ap.parse_args()

    policy = RetryPolicy(
        max_retries=args.max_retries,
        base_delay=args.base_delay,
        max_delay=args.max_delay,
    )
    try:
        body, attempts = retry_call(args.url, policy=policy)
    except RetryExhausted as e:
        print(f"FAIL: {e}")
        raise SystemExit(1)

    try:
        parsed = json.loads(body)
    except json.JSONDecodeError:
        parsed = body.decode("utf-8", "replace")
    print(f"OK after {attempts} attempts: {parsed}")


if __name__ == "__main__":
    _main()
