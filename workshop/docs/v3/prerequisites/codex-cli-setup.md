# 学员课前准备：codex CLI + Microsoft Foundry SDK

> 适用：v3 短课（S1+S2 共 4h，AI CLI 副驾驶主线）
> 目标耗时：**15 分钟以内**完成
> 系统：macOS（其他系统请联系讲师）
> 状态：⚠️ 未经讲师 Day-7 实测验收，以讲师课前发出的最终版为准

## 你会拿到什么

讲师在课前会发给你**一封私信**，内容包含：

- `PROJECT_ENDPOINT`：形如 `https://<resource-name>.services.ai.azure.com/api/projects/<project-name>`
- `MODEL_DEPLOYMENT_NAME`：模型部署名（讲师 Day-7 在 Foundry 里部好；rebrand 期模型目录会漂，**以讲师私信为准**）
- 一个 Azure 账户邀请（你用自己的 Microsoft 账号 `az login` 后会拿到 **Foundry User** 角色）

**重要**：v3 用的是 Microsoft Foundry 当前主路径——**Entra ID 鉴权（`DefaultAzureCredential` + `az login`）**，不是 API key。课程结束后讲师会回收你在 Foundry project 上的 RBAC。

> 为什么不在文档里写死模型名 / API version：Foundry 仍在 rebrand 期（Azure AI Foundry → Microsoft Foundry / Assistants API → Responses API），model 目录、SDK 版本、portal UI 都在演化。讲师 Day-7 实测后的私信值才是当天的真相。

## 步骤

### 1. 装 Azure CLI + Python ≥ 3.8

```bash
# Azure CLI（如果没有）
brew install azure-cli

# Python ≥ 3.8
python --version    # 应 ≥ 3.8；不够用 brew install python@3.12 或 pyenv

# 验证
az --version
python --version
```

### 2. 装 codex CLI 和 Node.js 20+

```bash
# Node（codex 依赖）
brew install node
node --version   # 应 ≥ v20

# codex CLI
npm install -g @openai/codex
codex --version
```

如果 `npm install -g` 报权限错，**不要用 sudo**，而是：

```bash
mkdir -p ~/.npm-global
npm config set prefix ~/.npm-global
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.zshrc
source ~/.zshrc
npm install -g @openai/codex
```

### 3. 装 Foundry Python SDK

```bash
# 建议建一个隔离 venv
python -m venv ~/foundry-v3-env
source ~/foundry-v3-env/bin/activate

# 装 Foundry projects SDK（必须 2.x；1.x 对应 Foundry classic）
pip install "azure-ai-projects>=2.0.0" "azure-identity"
```

> codex CLI 课中会替你装/升级包；建好 venv 是为了课中 codex 装的东西不污染全局环境。

### 4. 配置 Foundry 项目环境变量

在你的 shell rc 文件（macOS 默认 `~/.zshrc`）末尾追加，**把值替换成讲师发的**：

```bash
# Microsoft Foundry for v3 training
export PROJECT_ENDPOINT="<讲师私信发的 PROJECT_ENDPOINT>"
export MODEL_DEPLOYMENT_NAME="<讲师私信发的模型部署名>"
export AGENT_NAME="customer-service-agent-v3-$(whoami)"   # 加你自己的名字避免冲突
```

让配置生效：

```bash
source ~/.zshrc
```

### 5. Azure 登录（Entra ID）

```bash
az login
# 浏览器会弹出微软登录页，用讲师邀请你的账号登录
az account show    # 应能看到 subscription + tenant
```

> v3 不让你保管 API key——身份由 Entra ID 管。`DefaultAzureCredential` 在 SDK 里会自动捡 `az login` 留下的凭证。

### 6. 跑通第一个 Foundry 调用

新开终端 tab（确认 venv + env 都生效）：

```bash
source ~/foundry-v3-env/bin/activate
cd ~ && mkdir -p foundry-v3-tmp && cd foundry-v3-tmp
```

把下面代码存成 `hello.py`：

```python
import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
openai = project.get_openai_client()

response = openai.responses.create(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    input="用一句话介绍 Microsoft Foundry。",
)
print(response.output_text)
```

跑：

```bash
python hello.py
```

期望看到一段中文回复。

### 7. 跑一次 codex CLI（确认副驾驶环境就绪）

```bash
codex
```

进入交互模式后输入：

```
读一下当前目录的 hello.py，告诉我这段代码在做什么。
```

期望 codex 给出一段总结。退出用 `/exit` 或 Ctrl-D。

### 8. 自检 checklist

把下面 6 条都打勾再来上课：

- [ ] `az account show` 输出包含 subscription + tenant
- [ ] `python --version` ≥ 3.8
- [ ] `pip show azure-ai-projects` 显示 ≥ 2.0.0
- [ ] `node --version` ≥ v20，`codex --version` 有输出
- [ ] `echo $PROJECT_ENDPOINT` 输出讲师发的 endpoint
- [ ] 步骤 6 的 `hello.py` 跑出真实模型回复（不是异常 stacktrace）

## 常见报错（基于公开模式整理，讲师 Day-7 会补充实测案例）

| 现象 | 可能原因 | 处理 |
|---|---|---|
| `command not found: codex` | 全局 npm bin 不在 PATH | 见步骤 2 的 `~/.npm-global` 方案 |
| `DefaultAzureCredential failed to retrieve a token` | 没 `az login`，或登录的账号没 Foundry User 角色 | 重跑 `az login`；找讲师确认角色已分配 |
| `404 Not Found` / `Connection refused` | `PROJECT_ENDPOINT` 拼接错，或 resource/project 名错 | 对照讲师发的字符串，格式是 `https://<resource>.services.ai.azure.com/api/projects/<project>` |
| `model not found` | `MODEL_DEPLOYMENT_NAME` 错，或该 deployment 未在 project 暴露 | 对照讲师发的部署名；rebrand 期模型目录会漂，不要自己猜 |
| `ModuleNotFoundError: azure.ai.projects` | 没进 venv，或 SDK 版本错 | `source ~/foundry-v3-env/bin/activate` + `pip install "azure-ai-projects>=2.0.0"` |
| `AttributeError` on `evals` / `responses` | 装到了 1.x（Foundry classic） | `pip install --upgrade "azure-ai-projects>=2.0.0"` |
| Network timeout | 本地代理 / 公司网络拦截 `*.services.ai.azure.com` | 切手机热点重试，或问讲师备用 endpoint |

## 失败兜底

- 10 分钟内卡住：在群里 @讲师贴**完整报错 + 你跑的命令**（**不要贴 endpoint URL 全文，也不要贴 token**）
- 课前彻底搞不定：上课用同桌的环境结对完成动手；课后讲师单独帮你过一遍

## 安全提醒

- `PROJECT_ENDPOINT` 里的 resource 名不算高敏，但**不要 commit 到 public repo**（含子域信息）
- `az login` 留下的 token 缓存在 `~/.azure/`，课程结束后可以 `az logout` 清掉
- 课程结束后讲师会撤掉你的 Foundry RBAC，你不需要做清理
- 如果怀疑账号异常（被钓鱼 / 设备丢失），立刻 `az logout` + 在 Microsoft 账号页面终止 session，再告诉讲师

## 反馈

课前/课中遇到的卡点，请在课后**1 句话**写在群里，讲师会回写到这份引导里——下一期学员受益。
