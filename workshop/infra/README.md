# D3 Foundry 单 agent — Bicep 骨架

> 用途：D3 模块（单 agent 平台路径）讲师演示用模板。学员**看 + 拷走**，不在课堂真跑。

## 状态声明（不假装跑过）

- 本模板 **未在真实 Azure 订阅验证**。
- 具体资源 API 版本与 **Foundry project 资源类型**（`Microsoft.MachineLearningServices` vs `Microsoft.CognitiveServices` vs 新 rebrand 命名空间）需在 **fork 实操阶段校正** —— 见 `docs/03-workshop-fork-mapping.md` 第 51 行"Bicep 模板结构未确认"。
- `modules/foundry-project.bicep` 中标 `TODO(fork)` 的位置是已知漂移点，跑前必查。

## 为什么学员不真跑

参见根 `README.md` 凭证假设：学员侧不要求自带 Azure 订阅。Bicep 真跑需要：
- 订阅 + Owner / Contributor + User Access Administrator（RBAC 模块要）
- Foundry / AI Services 资源提供方注册
- 区域配额（模型部署 TPM）

学员触发真部署会撞共享配额 + 课堂时间不够等部署完成。**讲师演示**部署一次（或放录屏），学员把模板拷回自己环境慢慢跑。

## 模块化结构

```
infra/
├── README.md
├── main.bicep                      # 顶层入口（subscription scope），创建 RG + 调模块
├── parameters.example.json         # 参数样例
├── deploy.sh                       # az deployment sub create 示例命令
└── modules/
    ├── foundry-project.bicep       # Foundry project（上游 Ex01 借鉴 / TODO fork 校正）
    ├── app-insights.bicep          # App Insights + Log Analytics（D3 tracing / D9 复用）
    ├── container-apps.bicep        # Container Apps env（D5 scaling / D9 部署复用）
    └── keyvault.bicep              # Key Vault + RBAC（managed identity 引用，禁 hardcode secret）
```

设计原则（与 D3 spec 约束一致）：

- **模块化**：不写单文件 200 行；每个资源族一个模块。
- **无 secret hardcode**：所有敏感引用走 Key Vault + managed identity RBAC（`Key Vault Secrets User` role）。Bicep 里不出现明文 key。
- **跨模块复用**：`container-apps.bicep`、`app-insights.bicep` 在 D5、D9 会再次引用；这里就按可复用方式写。

## 部署（讲师演示用）

```bash
# 1. 登录 + 选订阅
az login
az account set --subscription <SUBSCRIPTION_ID>

# 2. 复制参数样例并改值
cp parameters.example.json parameters.json
# 编辑 parameters.json：projectName / location / rgName

# 3. what-if 预演（强烈建议先跑这步）
az deployment sub what-if \
  --location <LOCATION> \
  --template-file main.bicep \
  --parameters @parameters.json

# 4. 真部署
./deploy.sh
```

或直接：

```bash
az deployment sub create \
  --location eastus2 \
  --template-file main.bicep \
  --parameters @parameters.json
```

## 上游借鉴

`modules/foundry-project.bicep` 参考 [microsoft/TechWorkshop-L300-AI-Apps-and-agents](https://github.com/microsoft/TechWorkshop-L300-AI-Apps-and-agents) **Ex01 — Deploy and configure resources**（Bicep + Foundry project 连接）。fork 后用上游真实模板替换本文件中的 placeholder 资源块，再校 API 版本。

## 漂移清单（fork 时确认）

- [ ] Foundry project 资源类型 + API 版本
- [ ] 模型部署（gpt-4o / gpt-4o-mini）单独写还是嵌入 project
- [ ] Cosmos DB / AI Search 是否在 D3 必须（上游 Ex01 含，D3 spec 只要 agent + connection，可能裁掉）
- [ ] App Insights connection string 注入 Foundry project 的方式（connection resource? 还是 project 属性?）
- [ ] Container Apps 与 Foundry project 的网络（公网 / VNet 集成）—— D5 决定
