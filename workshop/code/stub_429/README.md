# stub_429

D5 学员主线配套：本地起一个会**前 N 次返回 429** 的小服务，配套一个带 jitter 的重试客户端，验证 retry 行为。

## 用途

handbook D5 自验证项之一：

> 用 stub / 讲师提供的 replay response 注入 429，观测到重试 + jitter 行为正确（不抛业务层）

不依赖任何真实 Azure 配额。学员在断网环境也能跑。

## 怎么跑

### 1. 启 stub server（一个终端）

```bash
cd workshop/code/stub_429
python stub_server.py --port 18429 --fail-times 3
# 前 3 次请求 → 429（带 Retry-After: 1）
# 第 4 次起 → 200 {"ok": true}
```

### 2. 跑 retry 客户端验证（另一个终端）

```bash
python retry_client.py --url http://127.0.0.1:18429/ --max-retries 5
# 期待：看到 3 次 retry log + 最终 200
```

### 3. 跑 pytest（自动起 server）

```bash
# 一次性装依赖（仓库根目录的 requirements-dev.txt）
pip install -r ../../../requirements-dev.txt

python3 -m pytest test_retry.py -v
```

## 注入到自己的 retry 逻辑里

把 `retry_client.py` 的 `retry_call` 当模板抄到自己的 provider 层（**不要散落在业务层**，handbook D5 negative example #2）。

关键参数：

| 参数 | 默认 | 说明 |
|------|------|------|
| `max_retries` | 3 | 重试上限，handbook 约束「不准无限重试」 |
| `base_delay` | 0.5s | 指数退避基数 |
| `max_delay` | 8s | 退避封顶 |
| `jitter` | "full" | full jitter，避免 thundering herd |

## 文件

- `stub_server.py` — stdlib `http.server`，前 N 次 429
- `retry_client.py` — 带 full jitter 的指数退避
- `test_retry.py` — 端到端验证

零依赖，stdlib 足够。
