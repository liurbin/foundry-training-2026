"""
D5 — 429 注入 stub

用法：
    python stub_server.py --port 18429 --fail-times 3
    # 前 3 次任意请求 → 429（含 Retry-After: 1）
    # 第 4 次起 → 200 {"ok": true, "served_at": ...}

也可以编程方式起：
    from stub_server import run_server
    httpd, stop = run_server(port=0, fail_times=3)
    port = httpd.server_address[1]
    ...
    stop()
"""
from __future__ import annotations

import argparse
import json
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Callable


def _make_handler(state: dict) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        # 关闭默认 access log，跑测试时太吵
        def log_message(self, format: str, *args) -> None:  # noqa: A002
            if state.get("verbose"):
                super().log_message(format, *args)

        def _serve(self) -> None:
            with state["lock"]:
                state["count"] += 1
                n = state["count"]
                fail_times = state["fail_times"]

            if n <= fail_times:
                body = json.dumps(
                    {"error": "rate_limited", "attempt": n, "fail_until": fail_times}
                ).encode("utf-8")
                self.send_response(429)
                self.send_header("Content-Type", "application/json")
                self.send_header("Retry-After", "1")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return

            body = json.dumps(
                {"ok": True, "attempt": n, "served_at": time.time()}
            ).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:  # noqa: N802
            self._serve()

        def do_POST(self) -> None:  # noqa: N802
            length = int(self.headers.get("Content-Length", "0") or 0)
            if length:
                self.rfile.read(length)
            self._serve()

    return Handler


def run_server(
    *, port: int = 18429, fail_times: int = 3, verbose: bool = False
) -> tuple[ThreadingHTTPServer, Callable[[], None]]:
    """启动 stub server，返回 (server, stop_fn)。stop_fn 幂等。"""
    state = {
        "count": 0,
        "fail_times": fail_times,
        "lock": threading.Lock(),
        "verbose": verbose,
    }
    httpd = ThreadingHTTPServer(("127.0.0.1", port), _make_handler(state))
    thread = threading.Thread(target=httpd.serve_forever, daemon=True)
    thread.start()

    stopped = {"flag": False}

    def stop() -> None:
        if stopped["flag"]:
            return
        stopped["flag"] = True
        httpd.shutdown()
        httpd.server_close()
        thread.join(timeout=2)

    return httpd, stop


def _main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=18429)
    ap.add_argument("--fail-times", type=int, default=3, help="前 N 次返回 429")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    httpd, stop = run_server(
        port=args.port, fail_times=args.fail_times, verbose=args.verbose
    )
    print(
        f"[stub_429] listening on http://127.0.0.1:{args.port} "
        f"(fail_times={args.fail_times})  Ctrl-C 退出"
    )
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print("\n[stub_429] 退出")
    finally:
        stop()


if __name__ == "__main__":
    _main()
