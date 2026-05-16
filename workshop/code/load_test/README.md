# load_test

D5 **讲师演示** 用脚本。学员看脚本理解参数 / 形状，**不真跑**。

## 为什么学员不真跑

handbook D5 自验证项：

> 真实 100 RPS × 5min 压测为**可选**（讲师统一演示或录屏；真跑由讲师侧执行，避免学员触发共享配额）

学员真跑 100 RPS × 5min 会把共享的 Foundry 配额打爆，影响同班其他人，也容易触发账单告警。所以：

- **学员**：读脚本 → 理解参数怎么算（QPS、并发、duration、超时）→ 看讲师演示 / 录屏
- **讲师**：在自己的独立订阅 / 沙箱 endpoint 上跑，把数字截图带回课堂

## 怎么跑（讲师侧）

```bash
# 装依赖（讲师侧；学员不需要）
pip install httpx

# 100 RPS × 5min（默认 concurrency=50）
./run.sh

# 或者直接调
python loadtest.py \
    --url https://your-endpoint.example.com/chat \
    --qps 100 \
    --duration 300 \
    --concurrency 50 \
    --timeout 10
```

## 参数说明

| 参数 | 含义 | 默认 | 备注 |
|------|------|------|------|
| `--url` | 打靶 URL | （必填） | 不要打公共服务 |
| `--qps` | 目标 QPS | 100 | 用 token bucket 整形 |
| `--duration` | 持续秒数 | 300 | 5min |
| `--concurrency` | 并发 worker 数 | 50 | 受单连接 RTT 影响，通常 ≥ qps × p95_latency |
| `--timeout` | 单请求超时（秒） | 10 | 超时计为失败 |
| `--method` | HTTP 方法 | GET | POST 时用 `--body-file` 指定 body |

输出：实时 tick（每秒成功 / 失败 / p50 / p95）+ 末尾汇总（含状态码分布）。

## 不做的事

- 不写复杂报告（HTML / Grafana 集成）——讲师演示完截图就够
- 不内置鉴权流程——`--header "Authorization: Bearer ..."` 自己塞
- 不绕开 429——遇到 429 就计入失败，看清楚配额墙在哪里

## 文件

- `loadtest.py` — 基于 `asyncio + httpx` 的并发打靶
- `run.sh` — 100 RPS × 5min 示例命令
