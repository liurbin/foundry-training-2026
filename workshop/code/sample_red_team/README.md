# sample_red_team

D8 学员 fallback 资料：当 SDK 50min 内跑不通时，用这份**伪造**的 baseline 结果，把 baseline 报告的**结构**完成掉。真实跑通 SDK 转课后 / 综合作业加分项（handbook D8 spec）。

## 什么时候用

| 场景 | 用这里的东西吗 |
|------|----------------|
| portal 跑通了，SDK 也跑通了 | ❌ 用你自己的真实 JSON |
| portal 跑通了，SDK 50min 内跑不动 | ✅ 用 `baseline_result.json` 走完报告结构 |
| portal 没跑通 | ❌ 不接受 fallback，先去把 portal 跑通（handbook 硬约束） |

## 文件

- `baseline_result.json` — 伪造的 baseline 结果，结构对齐 SDK 真实输出
  - **开头字段 `_DISCLAIMER` 明确写了"伪造数据"，提交报告时不要删，让 reviewer 看见**
  - `num_objectives = 3`
  - 含 2 个 false positive 示例（工具标"成功"但实际无害——handbook D8 negative example #2 的典型场景）
- `learner_fill_in.md` — 基于 JSON 写 baseline 报告的填空模板（学员复制后填）

## 字段说明（baseline_result.json）

| 字段 | 含义 |
|------|------|
| `run_id` | 本次红队 run 的 ID |
| `target` | 被测 agent 标识（agent_id / endpoint） |
| `num_objectives` | 攻击 objective 数（≥3） |
| `attack_types` | 本次覆盖的攻击类型集合 |
| `results[]` | 每个 (objective × attack) 的 trial |
| `results[].attack_type` | 攻击类型（如 `prompt_injection` / `jailbreak` / `harmful_content`） |
| `results[].objective` | 攻击目标描述（agent 不该做的事） |
| `results[].attack_prompt` | 攻击使用的 prompt（精简版） |
| `results[].response` | agent 的实际响应 |
| `results[].scored_pass` | 工具判定：true = 攻击成功 / agent 失守 |
| `results[].human_review` | 人工 review 结论（含 false_positive 标注） |
| `asr_summary` | ASR 汇总：overall + 按 attack_type |

## 用法

```bash
# 看一眼数据
python -c "import json; print(json.dumps(json.load(open('baseline_result.json'))['asr_summary'], indent=2, ensure_ascii=False))"

# 把模板复制成自己的报告
cp learner_fill_in.md ../../d8-baseline-analysis.md
# 然后按模板里的 TODO 填
```
