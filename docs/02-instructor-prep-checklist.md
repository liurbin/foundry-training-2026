# 讲师 Day-7 准备清单

> 本清单汇总 `docs/01-instructor-handbook-v2.md` 中散落在各模块的讲师现成物要求。
> 它不是学员材料，也不是课程大纲；它是开课前 7 天讲师必须跑通、截图、录屏、打包好的执行清单。

## 使用方式

- Day-7 前完成本清单；未完成项必须在 Day-3 前有明确替代方案。
- 每个现成物都要能在无解释情况下交给助教使用。
- 每个录屏 / trace / sample JSON 都要标注生成日期、SDK/package 版本、Azure region、模型部署名。
- 如果 fork 或 Foundry UI/API 在 Day-7 后发生变化，只更新对应现成物，不改 `00-training-plan-v2.md`。
- **现成物索引路径**：所有产物统一放到 `prep-artifacts/day-7/<module>/`（如 `.../d4/`, `.../d10/`），并在本清单的"产物"列追加相对路径（例：`d4/live-switch-demo.md`）。助教只看清单就能找到全部物件。（注：旧设想里的 `workshop-fork/prep-artifacts/...` 已废弃——见 README.md "v1 旧版" 段；现 specs 已在 `prep-artifacts/day-7/specs/`，其他模块产物按同一根目录放）

## 全局核验

| 状态 | 项 | 产物 | 来源 |
|------|----|------|------|
| [ ] | 跑通改造后的 fork 全套 | 终端日志 + 失败项说明 | `00-training-plan-v2.md` 第十一节 |
| [ ] | 验证 rc 期 API 漂移点 | `OpenAIChatOptions(response_format=ResponseFormat)` 当前状态记录 | `00-training-plan-v2.md` 第十一节 |
| [ ] | 验证 token provider 写法 | `OpenAIChatTarget(api_key=token_provider)` 当前状态记录 | `00-training-plan-v2.md` 第十一节 |
| [ ] | 核验 Foundry portal UI 路径 | Models / Agents / Monitoring / Evaluations 截图 | `00-training-plan-v2.md` 第十一节 |
| [ ] | 跑通 Workflows samples | 至少 2 个 sample 的命令日志 + trace 截图 | `00-training-plan-v2.md` 第十一节 |
| [ ] | 综合作业评分 rubric（完整 5 维度） | 一页 rubric，覆盖跑通 25% / 选型 25% / 红队 20% / 生产化 15% / AI-pair 15% | 演示评分时讲师 / 助教 / 学员自评同口径 |
| [✅] | spec 模板库抽独立文件 | 12 个 `spec-dN-xxx.md` 放 `prep-artifacts/day-7/specs/`（D6 拆 a/b，故 12 个） | 与手册 v2 各模块 spec 章节同源；学员综合作业 spec 复用栏可直接引用文件路径 |

## D2: Agent Service vs SDK 选型

| 状态 | 项 | 产物 | 验收 |
|------|----|------|------|
| [ ] | D2 决策卡模板可投屏 | Markdown 模板（手册 D2 spec 同源） | 课堂可直接投屏 / 复制到共享文档 |
| [ ] | 4 维度评分参考样本 ≥ 2 个 | 真实场景填好的决策卡（如 startup B2C / partner POC 各 1 份） | 学员对照可校准自己的打分 |
| [ ] | 成本影响样本数字 | 小/中/大三档对应 Agent Service vs SDK 总成本估算 | 与 D5 成本三档参考一致 |

## D3: 单 agent 平台路径

| 状态 | 项 | 产物 | 验收 |
|------|----|------|------|
| [ ] | rebrand 期 API 漂移清单 | Markdown 短表（产物路径：`d3/api-drift.md`） | D3 spec 约束栏要求"不要用 deprecated API"，必须给学员看到当前漂移点 |
| [ ] | Bicep 参考模板 | 模块化 Bicep + 部署脚本 | 学员 AI-pair 生成卡壳时讲师可对照展示 |
| [ ] | tracing 启用前置确认 | portal 截图 + 启用步骤 | 对应 D3 spec 观测前置；Day1 上午统一确认 |

## D4: Provider 抽象

| 状态 | 项 | 产物 | 验收 |
|------|----|------|------|
| [ ] | 非 Azure provider API key 验证 | key 可调通的脱敏记录（provider / region / 配额上限） | plan 第十一节 gating；学员侧不发 key |
| [ ] | Foundry → 非 Azure provider live switch demo | 可投屏脚本 + 切换命令 | 课堂能在 60s 内完成切换且两侧返回均成功 |
| [ ] | mock provider 学员侧样例 | 学员可拷走的代码 + README | 无 Azure 凭证 / 断网可跑通；与手册 D4 接口契约一致 |
| [ ] | live demo 失败时录屏 fallback | 3-5 分钟录屏 | 含 Foundry 调用 + 切换 + 非 Azure provider 调用全链路 |

## D5: Scaling + Cost

| 状态 | 项 | 产物 | 验收 |
|------|----|------|------|
| [ ] | 429 注入 stub / replay response | 可复用 stub 代码或 replay fixture | 学员不依赖真实配额也能验证 retry + jitter |
| [ ] | 100 RPS x 5min 压测脚本 | 脚本 + README + 参数说明 | 讲师侧可复跑，学员侧不要求真实执行 |
| [ ] | 压测录屏 | 3-5 分钟录屏或终端日志摘要 | 能看到压测启动、429 注入、retry 成功、缓存命中 |
| [ ] | 成本三档参考 | 小/中/大三档估算表 | 覆盖 1k / 10k / 100k DAU，包含模型费、容器费、AI 摄入费 |

## D6b: A2A + MCP

| 状态 | 项 | 产物 | 验收 |
|------|----|------|------|
| [ ] | A2A prepared repo | 可 clone / 可运行 repo 或 fork 分支 | 能展示跨进程 A2A 调用，不是同进程函数伪装 |
| [ ] | MCP prepared repo | 可 clone / 可运行 repo 或 fork 分支 | MCP tool 至少有一次真实 HTTP / 文件 / 计算动作 |
| [ ] | A2A + MCP trace 对照 | trace 截图或导出文件 | 能看出 agent A -> agent B -> MCP tool 链路 |
| [ ] | rebrand 期坑清单 | Markdown 短表 | 包含当前包版本、字段/API 漂移、已知文档不一致 |
| [ ] | 反例 demo | 同进程函数调用伪装 multi-agent 的最小示例 | 上课能打开对比，让学员看出为什么不算 A2A |

## D7: 多 Agent 编排三选一

| 状态 | 项 | 产物 | 验收 |
|------|----|------|------|
| [ ] | Agent Service 原生主路径 trace | trace 截图或导出文件 | 能看到 orchestrator -> 专家 1 -> 专家 2 |
| [ ] | `as_tool` prepared diff | patch 文件 + apply 说明 | 可在主路径代码上一键 apply 并看出差异 |
| [ ] | Workflows 录屏 | 10-15 分钟录屏 | 包含 visual designer 操作 + 一次完整运行 trace |
| [ ] | D7 兜底演示包 | 主路径可运行代码 + trace 截图 | 学员主路径跑不通时，讲师可直接展示 |

## D8: 红队 Baseline

| 状态 | 项 | 产物 | 验收 |
|------|----|------|------|
| [ ] | Portal 红队 baseline 截图 | UI 截图 + ASR 数字 | 讲师本人 Day-7 跑过，`num_objectives=3` 起步 |
| [ ] | SDK 红队 sample JSON | JSON 文件 + 对应 attack set 说明 | 学员 SDK 跑超时时可用来完成 baseline 报告结构 |
| [ ] | 红队工具已知坑清单 | Markdown 短表 | 包含 false positive 高发类型、耗时风险、解释口径 |
| [ ] | D8 红队分项细则 | 一页 rubric，红队 baseline 20% 内部如何打分 | 与全局综合作业 rubric 红队那行展开对齐 |

## D9: 生产化 Checklist

| 状态 | 项 | 产物 | 验收 |
|------|----|------|------|
| [ ] | 事故复盘真实案例 | 脱敏 Markdown，≥1 个完整 timeline | 含触发 / 响应 / 定位 / 回滚 / 后续动作五段 |
| [ ] | runbook 模板 | Markdown，学员可裁剪填 | 至少覆盖 1 个事故场景的处置流程骨架 |
| [ ] | Azure DevOps 对照 GH Actions 差异表 | 一页对照表 | 含红队 gate 接入位置、Bicep apply 审批、回滚命令 |

## D10: Foundry 能力边界表

| 状态 | 项 | 产物 | 验收 |
|------|----|------|------|
| [ ] | 边界表实物（核心交付物） | Markdown，覆盖 plan 五·五能力地图的 13 个能力域 | 每行含：能力域 / 当前边界描述 / 验证来源 / 迁移方案样本 |
| [ ] | 验证来源标注 | 每条边界标注：官方文档 URL / portal 截图 / fork 实测 | 三选一为硬要求；"未验证假设"只能作为风险备注列在边界表脚注，不进入主表、不作为课堂边界结论 |
| [ ] | 能力地图镜像校对 | 与 plan 第五·五节逐行对照 | 13 项能力域一一对应；plan 改 → 本表同步改 |
| [ ] | 迁移方案样本 ≥ 3 个 | Markdown 短文 | 覆盖常见边界（如 Models 目录外 / Agent Service 自定义控制流 / 配额上限）|

## D11: AI-pair 工作流团队资产

| 状态 | 项 | 产物 | 验收 |
|------|----|------|------|
| [ ] | Foundry MCP server 可用性验证 | 二选一结论 + 备份方案 | 决定 Day3 走"现场连接演示"还是"Learn URL 替代工作流" |
| [ ] | spec 库 demo 仓库 | 可投屏的 Git repo | 含 README / decision-cards / implementation / negative-examples / runbooks 5 个目录 |
| [ ] | 示例 spec 完整文件 ×2 | Markdown，学员可拷走 | "新 agent 上线 spec" + "新 provider 接入 spec"，与手册大纲对齐 |
| [ ] | MCP 替代工作流模板 | 手动 prompt 模板 | MCP 不可用时仍能演示如何把 Learn URL / SDK docs / portal evidence 喂给 AI |

## 未完成项处理

| 场景 | 处理 |
|------|------|
| Day-7 未跑通，但 Day-3 前可修 | 标注 owner、阻塞原因、预计修复命令 |
| Day-3 仍未跑通 | 准备录屏 / sample JSON / trace 截图作为 fallback |
| 现场 Foundry UI/API 漂移 | 以 Day-7 产物为保底，现场只讲漂移原因和替代路径 |
| 现成物依赖私密 key 或订阅 | 给助教准备脱敏版，禁止把 key 写进 repo 或共享文档 |

