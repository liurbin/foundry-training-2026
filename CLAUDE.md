# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库性质

这是一个**培训材料仓库**，不是产品代码。产物是一个 MkDocs 站点 + 少量学员侧 Python 示例代码。
课程：Microsoft Foundry（formerly Azure AI Foundry）3 天 11 模块培训，L300，决策驱动 + 生产化。

权威源文档在 `docs/` 下（v2 系列）。`workshop/` 是学员侧站点内容，`prep-artifacts/day-7/specs/` 是
每个模块的 prompt spec。**v1 文档（`docs/00-training-plan.md`、`docs/02-instructor-manual.md`）已冻结，
不要再改**。

## 常用命令

```bash
# 站点本地预览（中文）
pip install -r requirements-docs.txt
mkdocs serve                       # http://127.0.0.1:8000

# CI 等价构建（broken link / strict 模式失败即视为错）
mkdocs build --strict              # 中文站
mkdocs build --strict -f mkdocs.en.yml  # 英文站，必须同时通过

# 学员侧代码测试（workshop/code/mock_provider, stub_429）
pip install -r requirements-dev.txt
pytest workshop/code/mock_provider
pytest workshop/code/stub_429
pytest workshop/code/mock_provider/test_provider.py::TEST_NAME  # 单测

# 学员环境自检
bash scripts/precheck.sh
```

推送到 `main` 由 `.github/workflows/pages.yml` 自动构建并发布到 GitHub Pages。CI 跑的是
**两个 mkdocs build --strict**（中 + 英），任何一个 broken link 都会让发布失败。

## 站点结构（关键：symlink 聚合）

`mkdocs.yml` 的 `docs_dir` 指向 `site_src/`，而不是 `docs/` 或 `workshop/`。`site_src/` 用 symlink
把分散的源聚合起来：

```
site_src/
├── index.md   -> ../workshop/README.md
├── handbook/  -> ../docs              # 课程设计 + 讲师手册
├── workshop/  -> ../workshop/docs     # 学员 12 模块 × 45 子任务
├── specs/     -> ../prep-artifacts/day-7/specs
└── en/                                # 英文版独立目录（非 symlink），由 mkdocs.en.yml 使用
```

**改 nav 必须改 `mkdocs.yml`**（中文）+ `mkdocs.en.yml`（英文）两处。新增页面要同时检查英文站是否有
对应文件，否则英文 strict build 会断。

## 文档之间的对齐关系

四份核心文档互为引用，改一处通常要核对其他几处口径：

- `docs/00-training-plan-v2.md` — 课程设计源（11 模块议程 / 5 维度评分 / 能力地图）
- `docs/01-instructor-handbook-v2.md` — 每模块 spec + negative examples + 验收
- `docs/02-instructor-prep-checklist.md` — Day-7（培训前 7 天）讲师准备物清单
- `docs/03-workshop-fork-mapping.md` — 与上游 `microsoft/TechWorkshop-L300-AI-Apps-and-agents` 对照（🟢/🟡/🔴）
- `docs/04-design-principles.md` — 上述四份的原则依据
- `prep-artifacts/day-7/specs/spec-d{1..11}-*.md` — 每模块从 handbook 抽出的独立 spec，是
  给 AI-pair / 讲师当 prompt 用的，应与 handbook 对应章节保持一致

学员侧 `workshop/docs/d{01..11}_*/` 各模块下是 `index.md` + `01.md` `02.md` … 子任务，对应 plan v2
里"45 子任务"的拆分。

## 凭证 / 真实订阅边界

- **学员侧不假设有 Azure 订阅**。所有需要真实 Foundry 资源的步骤都用 `workshop/code/` 下的
  mock provider / stub 429 / sample JSON 替代。改学员内容时不要引入"必须有订阅"的硬依赖。
- **讲师侧需要订阅**。`workshop/infra/` 的 Bicep 骨架、D5 真部署、D8 云端 Red Teaming 是讲师 Day-7
  实操项，README 标 `[~]` 的条目表示"课程设计完成、讲师包未完成"，不要把它们当成已验证过的事实陈述。

## 上游归属

学员 `workshop/` 借用了上游 MIT 素材，归属在 `workshop/THIRD_PARTY_NOTICES.md`。新增借用素材
要同步更新 fork-mapping 表 + notices。

## 协作风格备注

- 中文为主，英文站是镜像。
- 文档语气偏"决策驱动 + 生产化 + 边界明确"——避免空泛赞美、避免给没有落地路径的建议；改文档时保持这种口径。
- 标 `[~]` / `⚠️` 的"Day-7 by 讲师"条目属于人类讲师的 gating，不要替它们写"已完成"。
