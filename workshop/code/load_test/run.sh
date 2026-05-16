#!/usr/bin/env bash
# D5 讲师侧 100 RPS × 5min 示例
# 学员不要直接跑这个——会打爆共享配额
set -euo pipefail

URL="${TARGET_URL:-http://127.0.0.1:8000/health}"
QPS="${QPS:-100}"
DURATION="${DURATION:-300}"
CONCURRENCY="${CONCURRENCY:-50}"
TIMEOUT="${TIMEOUT:-10}"

# 鉴权头通过环境变量塞：
#   export AUTH_HEADER="Authorization: Bearer xxx"
EXTRA_ARGS=()
if [[ -n "${AUTH_HEADER:-}" ]]; then
  EXTRA_ARGS+=(--header "${AUTH_HEADER}")
fi

exec python3 "$(dirname "$0")/loadtest.py" \
  --url "${URL}" \
  --qps "${QPS}" \
  --duration "${DURATION}" \
  --concurrency "${CONCURRENCY}" \
  --timeout "${TIMEOUT}" \
  "${EXTRA_ARGS[@]}"
