# Foundry 开发者培训 2026

基于微软官方 `microsoft/TechWorkshop-L300-AI-Apps-and-agents` 改造、按 plan v2 重新组织的 3 天 11 模块培训材料。

## 培训定位

- **人群**：~10 人 Python 开发者，无 Foundry 经验
- **形式**：远程 **3 天**（约 18 课时）
- **深度**：L300，决策驱动 + 平台路径 + 生产化；代码动手为主
- **产出**：每人能独立部署一套 Foundry agent + 接入观测 + 跑红队 baseline + 完成综合作业（5 维度 rubric）

## 4 份核心文档 + workshop 站点

| 文件 | 用途 | 读者 |
|------|------|------|
| `docs/00-training-plan-v2.md` | 课程设计源（11 模块、议程、能力地图、5 维度评分） | 课程负责人、讲师 |
| `docs/01-instructor-handbook-v2.md` | 讲师手册：每模块 spec / negative examples / 验收 | 讲师、助教 |
| `docs/02-instructor-prep-checklist.md` | Day-7 准备清单：现成物、录屏、sample JSON、prepared repo | 讲师 |
| `docs/03-workshop-fork-mapping.md` | 上游 ↔ v2 对照表（🟢 / 🟡 / 🔴 三色） | 讲师、fork 实操者 |
| `docs/04-design-principles.md` | 设计原则（v2 源头依据） | 课程负责人 |
| `workshop/` | 学员侧站点（12 模块 × 45 子任务） | **学员**、助教 |
| `prep-artifacts/day-7/specs/` | 11 个 spec 文件（已从 handbook 抽出） | 讲师、AI-pair |

## 目录结构

```
foundry-training-2026/
├── README.md                          # 本文件
├── docs/
│   ├── 00-training-plan-v2.md         # 课程设计
│   ├── 01-instructor-handbook-v2.md   # 讲师手册
│   ├── 02-instructor-prep-checklist.md # Day-7 清单
│   ├── 03-workshop-fork-mapping.md    # 上游对照
│   ├── 04-design-principles.md        # 设计原则
│   ├── 01-precheck.md                 # 学员前置（最低限：Python；订阅 optional）
│   ├── 00-training-plan.md            # v1 旧版（参考，不维护）
│   └── 02-instructor-manual.md        # v1 旧版（参考，不维护）
├── workshop/                          # 学员侧站点
│   ├── README.md                      # 课程地图入口
│   ├── docs/d01_concepts/ ... d11_ai_pair/   # 12 模块 README + 45 子任务
│   ├── code/                          # mock_provider / stub_429 / load_test / sample_red_team
│   ├── infra/                         # Bicep 骨架（讲师演示用，未在真实订阅验证）
│   └── THIRD_PARTY_NOTICES.md         # 上游 MIT 归属
├── prep-artifacts/day-7/specs/        # 12 个 spec 独立文件
├── requirements-dev.txt               # 学员/助教跑 pytest 用的最小依赖（pytest / httpx）
└── scripts/
    └── precheck.sh                    # 学员环境自检（python3 / git / curl 等）
```

> 跑 workshop/code 下的 pytest 前：`pip install -r requirements-dev.txt`（或用 `uv pip install -r requirements-dev.txt`）。

## 当前进度

- [x] 设计原则（`docs/04-design-principles.md`）
- [x] 课程设计 v2（`docs/00-training-plan-v2.md`）
- [x] 讲师手册 v2（`docs/01-instructor-handbook-v2.md`）
- [x] Day-7 准备清单（`docs/02-instructor-prep-checklist.md`）
- [x] 上游 ↔ v2 对照表（`docs/03-workshop-fork-mapping.md`）
- [x] 学员侧 workshop 站点（`workshop/` 12 模块 × 45 子任务 + code + infra）
- [x] 11 spec 抽独立文件（`prep-artifacts/day-7/specs/`）
- [x] 学员前置准备清单（`docs/01-precheck.md`，订阅项已降为 optional）
- [~] **Day-7 by 讲师**：fork 实操跑通改造 + 各模块录屏 / sample JSON / prepared repo / API 漂移清单（讲师 Day-7 实物，需 Azure 订阅；当前为"课程设计完成"，未达"讲师包完成"）
- [~] **Day-7 by 讲师**：D10 边界表 13 行验证来源——**官方文档 URL 已预填**（agent 2026/05 抓取核对，覆盖 Agent Service / Workflows / Quotas / Hosted agents / Red Teaming / Tracing / A2A 等关键行）；portal 截图 / fork 实测 / 订阅级 region 可用性 **仍待讲师 Day-7 补**
- [ ] **Day-7 by 讲师**：Foundry MCP server 可用性二选一（D11）
- [~] **Day-7 by 讲师**：`workshop/infra/` Bicep 骨架未在真实订阅验证（D3 真部署路径，需讲师 Day-7 跑通或录屏）
- [x] D5（Hosted Agents 主路径 / ACA 对照）与 D8（云端 Red Teaming Agent + SDK 学员真跑 / Portal 讲师演示）口径已统一；具体边界 / 验证来源待 Day-7 实证

> v1 文档（`00-training-plan.md`、`02-instructor-manual.md`）保留作演化参考，不再维护。
> 旧的 `workshop-fork/` 设想已废弃 —— 当前方案是按 plan v2 重新搭 `workshop/`，上游素材按 fork-mapping 表借用（MIT 归属见 `workshop/THIRD_PARTY_NOTICES.md`）。

## 人类必须做的 gating（最新口径）

⚠️ 培训日期前 2 周确认（详见 `docs/00-training-plan-v2.md` §十一）：

- MCAPS 外部订阅（讲师侧持票即可；学员 mock-first，订阅 **optional**）
- 讲师专用：1 个非 Azure provider API key（D4 live switch）
- GPT 模型 + TPM ≥ 50K（讲师侧）

⚠️ 培训日期前 1 周：

- 学员前置准备清单发出（`docs/01-precheck.md`）
- 一次环境自检（`scripts/precheck.sh`）

⚠️ Day-7（培训日期前 7 天，讲师本人）：

- 详见 `docs/02-instructor-prep-checklist.md`
