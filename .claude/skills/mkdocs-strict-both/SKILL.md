---
name: mkdocs-strict-both
description: Run mkdocs --strict for BOTH the zh and en sites (mkdocs.yml + mkdocs.en.yml), the same two builds CI runs. Use before pushing any doc / nav change to avoid GitHub Pages deploy failures from broken links in the English mirror.
disable-model-invocation: true
---

# mkdocs-strict-both

CI (`.github/workflows/pages.yml`) runs **two** strict builds — zh and en. Local
contributors often only run the zh build and discover broken-link failures in
the English mirror only after pushing.

## 执行

```bash
# 在仓库根目录
mkdocs build --strict
mkdocs build --strict -f mkdocs.en.yml
```

如果用了 venv：`source .venv/bin/activate && pip install -r requirements-docs.txt`
确保 mkdocs-material 已装。

## 期望输出

两次都 exit 0。任何 WARNING (broken link / missing nav item) 在 `--strict` 下都会
变 error。常见失败：

- 中文新增页面但 `mkdocs.en.yml` 的 nav 未对应新增 → en 报 "nav item not found"
- 删/重命名文件后另一份 config 仍引用旧路径
- 中文文档里的相对链接在英文 `site_src/en/` 目录下断了
- `site_src/` 下 symlink 目标被移动

## 修复策略

- 优先改 nav config，不要为了过 strict 把 strict 关掉
- 中文是源、英文是镜像（`site_src/en/`，非 symlink），英文站缺页时复制中文版做翻译占位也比删 nav 强
- 真的属于"暂未翻译"的页面，在英文 nav 里整页移除而不是留空链接
