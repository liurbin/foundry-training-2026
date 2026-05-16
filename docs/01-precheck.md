# 学员前置准备清单

> 培训日 -7 天发出。请在培训日 -3 天前完成所有检查项并把 `scripts/precheck.sh` 输出截图发助教。

## 一、硬件与系统要求

| 项 | 要求 | 备注 |
|---|------|------|
| 操作系统 | macOS / Linux / Windows + WSL2 | **Windows 原生不行**，Bicep/uv/Container 全链路有坑 |
| 内存 | ≥ 16GB | 同时跑 VS Code + Docker + 浏览器 |
| 磁盘 | ≥ 20GB 可用 | Container 镜像 + Python 虚拟环境 |
| 网络 | 能直连 Azure 国际版 + GitHub | **公司 VPN 可能拦 `*.azure.com`，提前测** |
| 摄像头 | 必开 | 远程培训要求 |

## 二、账号 gating（最重要，过不去培训作废）

### 培训日 -14 天 必须完成

- [ ] **MCAPS 外部订阅**已开通且分配给你
  - ❌ Microsoft EMU 账号权限不够
  - ❌ 个人 Azure 免费订阅不行（Foundry 需企业订阅）
  - ✅ 公司 MCAPS Subscription，或 Microsoft Partner MCAPS
  - 验证：`az account show` 能看到订阅 ID
- [ ] **Foundry 资源访问权限**已配置
  - 角色至少：`Azure AI Developer` + `Cognitive Services User`
  - 验证：能登录 https://ai.azure.com 并看到分配的 project
- [ ] **GPT 模型配额**已申请
  - `gpt-5.4-mini` 或 `gpt-4o`，TPM ≥ 50K（培训中会跑红队）
  - 验证：Foundry → Models → Deployments 能看到模型

### ⚠️ 这三项任意一项不满足 → 直接联系培训组协调，不要硬等

## 三、必装工具清单

```bash
# 1. Python 3.12+
python --version  # 必须 3.12 或更高
# 装法：pyenv install 3.12 或 brew install python@3.12

# 2. uv（包管理，workshop 用的）
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version  # ≥ 0.4

# 3. Azure CLI
brew install azure-cli   # macOS
# 或：curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash  # Linux
az --version  # ≥ 2.60

# 4. Bicep（Azure CLI 子命令）
az bicep install
az bicep version

# 5. Docker Desktop
docker --version  # ≥ 24
docker ps         # 必须能跑

# 6. GitHub CLI
brew install gh   # macOS
gh auth login

# 7. Git
git --version  # ≥ 2.40

# 8. VS Code + 推荐扩展
# - Python
# - Bicep
# - Azure Account
# - GitHub Copilot（可选）
```

## 四、培训前自检脚本

跑 `scripts/precheck.sh`，**把结果截图发助教**。如果有 ❌，培训日 -3 天前必须解决。

```bash
chmod +x scripts/precheck.sh && ./scripts/precheck.sh
```

## 五、必读资料（培训前预习，1-2 小时）

按重要性排序：

1. **必读**（30 分钟）：[Microsoft Agent Framework Overview](https://learn.microsoft.com/en-us/agent-framework/overview/?pivots=programming-language-python) ——只读 Python 部分
2. **必读**（20 分钟）：[Foundry Agent Service 介绍](https://learn.microsoft.com/azure/ai-foundry/agents/overview) ——理解平台原生路径
3. **选读**（30 分钟）：[A2A 协议规范](https://a2a-protocol.org/latest/) ——Day2 Ex03 会用
4. **选读**（20 分钟）：[AI Red Teaming Agent 概念](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-red-teaming-agent) ——Day2 Ex06 会用

**不要预先跑 workshop 源码**——里面有 bug，会被误导，等培训当天用我们改造后的 fork。

## 六、培训当天要带的东西

- [ ] 笔记本（充满电 + 电源）
- [ ] 已登录的 `az`、`gh`、`docker`
- [ ] 已读 1、2 两份必读资料
- [ ] 一个安静、网络稳定的环境
- [ ] 培训群已加，助教联系方式已存

## 七、常见问题速查

| 问题 | 原因 | 解决 |
|------|------|------|
| `az login` 后看不到订阅 | 公司 AD 没分配 | 找 IT 申请 MCAPS 订阅访问 |
| Bicep 部署 403 | 角色不够 | 申请 `Contributor` + `Azure AI Developer` |
| Foundry 看不到模型 | 模型未在你的区域部署 | 选 `eastus2` / `swedencentral`，配额最稳 |
| Container Apps 部署超时 | 镜像拉取慢 | 用 ACR 而不是 Docker Hub |
| GPT 调用 429 | TPM 不够 | 提前在 Foundry 把 TPM 拉到 50K+ |

## 八、紧急联系

- 培训组邮箱：`<待填>`
- 助教微信/钉钉：`<待填>`
- 培训前问题反馈截止：**培训日 -3 天 18:00**
