# 讲师 Day-7 彩排清单

> 这页给讲师用，不是学员动手步骤。目标是在开课前 7 天用真实 tenant 把 v3 短课跑通一遍，避免现场调 SDK / portal / RBAC。

## 必须实跑

按学员路径完整跑一遍：

1. `hello.py`：确认 `PROJECT_ENDPOINT`、`MODEL_DEPLOYMENT_NAME`、Entra ID 鉴权可用。
2. 动手 0：创建 prompt agent，跑两轮 `responses.create`，确认 agent name / version。
3. Trace：在 portal 找到对应调用，确认入口、延迟、Application Insights 连接状态。
4. 动手 1：用 `eval_dataset.jsonl` 跑 4 条 eval，拿到 `report_url`。
5. Fallback：直接跑 `workshop/docs/v3/code/run_eval.py`，确认脚本在当天 SDK 上仍可用。
6. 动手 2：创建 agent 新 version，加 Story 4 / Story 5 防护，再跑回 eval。
7. 收尾：打开 Monitor / Quota / Compliance，确认截图和当天口径。

## 必须截图

- Project overview：project endpoint 完整值，遮住敏感资源名后可投屏。
- Build → Agents：agent name、version。
- Build → Agents → Traces：至少 1 条顶层 span、token、latency。
- Build → Evaluations：4 条 case 的 report。
- Operate → Compliance：Policies / Guardrails / Security posture / Data security and governance。
- Operate → Quota：目标 model deployment、region / data zone、TPM / RPM 或 PTU 状态。

## 必须确认

- SDK：`pip show azure-ai-projects` 版本；`create_version`、`agent_reference`、`evals.create` 仍按文档工作。
- Endpoint：portal 给出的 project endpoint 域名，不手工转换 `.ai.azure.com` / `.services.ai.azure.com`。
- Model：部署名、deployment type、region / data zone、quota、是否 PTU。
- Identity：学员账号是否至少能跑 S2；讲师账号是否能演示 Compliance / Guardrails。
- Observability：Application Insights 是否已连接；trace 是否进入 portal。
- Guardrails：Build → Guardrails 当天能看什么、谁能创建 / 分配。
- Safety：content filter、Prompt Shields、abuse monitoring、modified 设置当天如何展示。

## 失败兜底

- 装机失败：10 分钟内未解决，直接结对完成 S2。
- Codex 不收敛：5 分钟内未产出可跑脚本，复制 `workshop/docs/v3/code/run_eval.py`。
- Eval API 漂移：讲师演示提前跑好的 evaluation report，并把 SDK 变化记录到课后更新。
- Trace 不出现：切到 Application Insights / app-side 日志解释观测链路，保留 portal trace 为 Day-7 blocker。
- Guardrails 权限不足：只演示入口和截图，学员当堂只做 agent instructions 加固。
- Quota / model 不可用：换备用 deployment；如果仍失败，用截图讲解并把 S2 改成讲师演示。

## 开课前发给学员

- `PROJECT_ENDPOINT`
- `MODEL_DEPLOYMENT_NAME`
- Azure 账号邀请和登录 tenant
- 课前装机链接
- 失败上报格式：命令、完整错误、操作系统、Python / Node / SDK 版本；不要贴 token 或完整 endpoint。
