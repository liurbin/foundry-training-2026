# 学员课前准备：codex CLI + Azure OpenAI

> 适用：v3 短课（S1+S2 共 4h，AI CLI 副驾驶主线）
> 目标耗时：**10 分钟以内**完成
> 系统：macOS（其他系统请联系讲师）
> 状态：⚠️ 未经讲师 Day-7 实测验收，以讲师课前发出的最终版为准

## 你会拿到什么

讲师在课前会发给你**一封私信**，内容包含：

- `AZURE_OPENAI_ENDPOINT`：形如 `https://<resource-name>.openai.azure.com/`
- `AZURE_OPENAI_API_KEY`：长串密钥
- `AZURE_OPENAI_DEPLOYMENT`：部署名（讲师 Day-7 实测后给具体值——本文档不写死，rebrand 期 model 目录漂移频繁）
- `AZURE_OPENAI_API_VERSION`：API 版本（同上，以讲师私信为准）

> 为什么不写死示例值：v3 设计阶段写过 `gpt-4o` / `2024-10-21` 这样的占位，但 Foundry 模型目录和 API version 处在 rebrand 期，半年内会漂。**以讲师课前私信发的最终值为准**，文档里出现的写死值都视为过期。

**不要把这些粘到聊天 / 公开仓库 / 截图里。**课后讲师会回收/失效这些 key。

## 步骤

### 1. 装 Node.js 20+（如果没有）

```bash
# 用 Homebrew
brew install node

# 验证
node --version   # 应 ≥ v20
```

如果你已经有 nvm / volta / asdf 管 Node 版本，用你熟悉的方式装 20+ 即可。

### 2. 装 codex CLI

```bash
npm install -g @openai/codex
codex --version
```

如果 `npm install -g` 报权限错，**不要用 sudo**，而是：

```bash
# 设一个用户级全局目录
mkdir -p ~/.npm-global
npm config set prefix ~/.npm-global
# 把 ~/.npm-global/bin 加到 PATH（zsh）
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.zshrc
source ~/.zshrc
# 重试
npm install -g @openai/codex
```

### 3. 配置环境变量（指向 Azure OpenAI）

在你的 shell rc 文件（macOS 默认 `~/.zshrc`）末尾追加，**把值替换成讲师发的**：

```bash
# Azure OpenAI for codex CLI (training v3)
export OPENAI_API_KEY="<AZURE_OPENAI_API_KEY>"
export OPENAI_BASE_URL="<AZURE_OPENAI_ENDPOINT>openai/deployments/<AZURE_OPENAI_DEPLOYMENT>"
export OPENAI_API_VERSION="<AZURE_OPENAI_API_VERSION>"
```

注意 `OPENAI_BASE_URL` 的拼接形式（Azure OpenAI 的兼容 endpoint 是
`<endpoint>openai/deployments/<deployment>`，不要漏掉 trailing path）。

让配置生效：

```bash
source ~/.zshrc
```

> 如果讲师发的是别的环境变量名约定（例如直接给 `AZURE_OPENAI_*`），以讲师课前最终说明为准。

### 4. 跑通第一个 prompt

新开一个终端 tab（确保新的 env 生效），cd 到一个**临时空目录**：

```bash
mkdir -p ~/foundry-training-tmp && cd ~/foundry-training-tmp
codex
```

进入 codex 交互模式后，输入：

```
用一句话介绍 Azure OpenAI 和 OpenAI 直连的区别。
```

期望看到一段中文回答输出。退出用 `/exit` 或 Ctrl-D。

### 5. 自检 checklist

把下面 4 条都打勾再来上课，不通过的提前在群里问：

- [ ] `node --version` ≥ v20
- [ ] `codex --version` 能输出版本号
- [ ] `echo $OPENAI_BASE_URL` 输出包含 `openai/deployments/` 的 URL
- [ ] 第 4 步那条 codex 命令返回了一段文字（不是报错）

## 常见报错（基于公开模式整理，讲师 Day-7 会补充实测案例）

| 现象 | 可能原因 | 处理 |
|---|---|---|
| `command not found: codex` | 全局 npm bin 不在 PATH | 见步骤 2 的 `~/.npm-global` 方案 |
| 401 / Unauthorized | key 错 / key 已失效 / 复制时带了空格 | 重新从讲师私信复制，确认无前后空格 |
| 404 Not Found | `OPENAI_BASE_URL` 拼接错（漏 deployment 或多/少斜杠） | 对照步骤 3 的格式 |
| `model not found` | deployment 名拼错 / 该 deployment 没暴露给这个 key | 对照讲师发的 deployment 名 |
| API version 报错 | `OPENAI_API_VERSION` 拼写错 / 太老 | 用讲师给的版本，不要自己改 |
| Network timeout | 本地代理 / 公司网络拦截 *.openai.azure.com | 切手机热点重试，或问讲师备用 endpoint |

## 失败兜底

- 5 分钟内卡住：在群里 @讲师贴**完整报错 + 你跑的命令**（**不要贴 key**）
- 课前彻底搞不定：上课用同桌的环境结对完成动手；课后讲师单独帮你过一遍

## 安全提醒

- key 不要 commit 到任何 git 仓库（包括 private repo）
- 课程结束后讲师会失效这批 key，你不需要做清理
- 如果你怀疑 key 已经泄露（贴错地方了），立刻告诉讲师，不要等

## 反馈

课前/课中遇到的卡点，请在课后**1 句话**写在群里，讲师会回写到这份引导里——下一期学员受益。
