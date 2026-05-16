"""
D5 — 讲师侧压测脚本（学员看，不真跑）

依赖：httpx>=0.27

设计原则：
- QPS 整形：用简单 token bucket，避免 worker 各自抢导致 burst
- 并发 worker 池：固定 N 个 worker 轮询从 queue 取 token 后发请求
- 统计：成功 / 失败 / 状态码分布 / p50 / p95 / p99
- 失败定义：HTTP >=400 或超时；不在客户端做 retry（要看清楚原始失败率）
"""
from __future__ import annotations

import argparse
import asyncio
import statistics
import time
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import httpx


@dataclass
class Stats:
    success: int = 0
    failure: int = 0
    timeouts: int = 0
    status_counts: Counter = field(default_factory=Counter)
    latencies_ms: list[float] = field(default_factory=list)

    def record(self, *, ok: bool, status: int | None, latency_ms: float, timeout: bool) -> None:
        if timeout:
            self.timeouts += 1
            self.failure += 1
            self.status_counts["TIMEOUT"] += 1
            return
        self.status_counts[status if status is not None else "ERR"] += 1
        self.latencies_ms.append(latency_ms)
        if ok:
            self.success += 1
        else:
            self.failure += 1

    def snapshot(self) -> dict:
        lat = self.latencies_ms or [0.0]
        lat_sorted = sorted(lat)

        def pct(p: float) -> float:
            if not lat_sorted:
                return 0.0
            idx = min(len(lat_sorted) - 1, int(len(lat_sorted) * p))
            return lat_sorted[idx]

        return {
            "success": self.success,
            "failure": self.failure,
            "timeouts": self.timeouts,
            "p50_ms": round(statistics.median(lat), 2),
            "p95_ms": round(pct(0.95), 2),
            "p99_ms": round(pct(0.99), 2),
            "status": dict(self.status_counts),
        }


async def _emitter(queue: asyncio.Queue, qps: int, duration: float, stop: asyncio.Event) -> None:
    """按 qps 速率往 queue 里丢"开火令牌"，duration 秒后停止。"""
    interval = 1.0 / qps
    deadline = time.monotonic() + duration
    next_tick = time.monotonic()
    while time.monotonic() < deadline and not stop.is_set():
        await queue.put(None)
        next_tick += interval
        sleep_for = next_tick - time.monotonic()
        if sleep_for > 0:
            await asyncio.sleep(sleep_for)
    # 通知所有 worker 收工：放等量哨兵
    for _ in range(queue.maxsize or 1):
        await queue.put("STOP")


async def _worker(
    client: httpx.AsyncClient,
    queue: asyncio.Queue,
    stats: Stats,
    method: str,
    url: str,
    headers: dict[str, str],
    body: bytes | None,
    timeout: float,
) -> None:
    while True:
        token = await queue.get()
        if token == "STOP":
            queue.task_done()
            return
        t0 = time.monotonic()
        try:
            resp = await client.request(
                method, url, headers=headers, content=body, timeout=timeout
            )
            lat = (time.monotonic() - t0) * 1000
            stats.record(
                ok=resp.status_code < 400,
                status=resp.status_code,
                latency_ms=lat,
                timeout=False,
            )
        except (httpx.TimeoutException, asyncio.TimeoutError):
            stats.record(ok=False, status=None, latency_ms=0, timeout=True)
        except httpx.HTTPError:
            lat = (time.monotonic() - t0) * 1000
            stats.record(ok=False, status=None, latency_ms=lat, timeout=False)
        finally:
            queue.task_done()


async def _ticker(stats: Stats, stop: asyncio.Event) -> None:
    last_success = 0
    last_failure = 0
    t = 0
    while not stop.is_set():
        await asyncio.sleep(1)
        t += 1
        snap = stats.snapshot()
        ds = snap["success"] - last_success
        df = snap["failure"] - last_failure
        last_success = snap["success"]
        last_failure = snap["failure"]
        print(
            f"[t={t:>4d}s] +ok={ds:>4d} +fail={df:>4d} "
            f"p50={snap['p50_ms']:>6.1f}ms p95={snap['p95_ms']:>6.1f}ms"
        )


def _parse_headers(items: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for raw in items:
        if ":" not in raw:
            raise SystemExit(f"--header 格式应为 'Name: value'，收到：{raw!r}")
        k, v = raw.split(":", 1)
        out[k.strip()] = v.strip()
    return out


async def run(args: argparse.Namespace) -> dict:
    body: bytes | None = None
    if args.body_file:
        body = Path(args.body_file).read_bytes()

    headers = _parse_headers(args.header or [])

    stats = Stats()
    stop = asyncio.Event()
    queue: asyncio.Queue = asyncio.Queue(maxsize=args.concurrency * 2)

    limits = httpx.Limits(
        max_connections=args.concurrency * 2,
        max_keepalive_connections=args.concurrency,
    )
    async with httpx.AsyncClient(limits=limits) as client:
        workers = [
            asyncio.create_task(
                _worker(client, queue, stats, args.method, args.url, headers, body, args.timeout)
            )
            for _ in range(args.concurrency)
        ]
        ticker = asyncio.create_task(_ticker(stats, stop))
        emitter = asyncio.create_task(_emitter(queue, args.qps, args.duration, stop))

        await emitter
        await queue.join()
        stop.set()
        await asyncio.gather(*workers, return_exceptions=True)
        ticker.cancel()

    return stats.snapshot()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--qps", type=int, default=100)
    ap.add_argument("--duration", type=float, default=300, help="秒")
    ap.add_argument("--concurrency", type=int, default=50)
    ap.add_argument("--timeout", type=float, default=10)
    ap.add_argument("--method", default="GET")
    ap.add_argument("--body-file", default=None)
    ap.add_argument(
        "--header", action="append", default=[], help="可多次：--header 'Authorization: Bearer ...'"
    )
    args = ap.parse_args()

    print(
        f"[loadtest] {args.method} {args.url} "
        f"qps={args.qps} duration={args.duration}s concurrency={args.concurrency}"
    )
    snap = asyncio.run(run(args))
    print("\n=== 汇总 ===")
    for k, v in snap.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
