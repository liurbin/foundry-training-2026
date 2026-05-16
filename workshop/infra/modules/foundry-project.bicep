// modules/foundry-project.bicep — Foundry project 资源（骨架）
//
// 上游借鉴：microsoft/TechWorkshop-L300-AI-Apps-and-agents
//   Ex01 — Deploy and configure resources（Bicep + AI Foundry project + connection）
//   https://microsoft.github.io/TechWorkshop-L300-AI-Apps-and-agents/
//
// TODO(fork)：以下资源类型 / API 版本属于 rebrand 期高漂移区，fork 实操时按上游真实模板替换：
//   - Foundry project 当前可能落在以下任一命名空间：
//       * Microsoft.MachineLearningServices/workspaces (kind: 'Project')   ← 旧 AI Studio 路径
//       * Microsoft.CognitiveServices/accounts + projects                  ← AI Services 路径
//       * Microsoft.AIFoundry/...（如已 GA 独立命名空间）                   ← rebrand 后可能
//   - 模型部署（gpt-4o / gpt-4o-mini）单独 resource 还是 project 子资源
//   - App Insights connection 用 `connections` 子资源还是 project 属性

@description('部署区域')
param location string

@description('Foundry project 名称')
param projectName string

@description('App Insights connection string，用于 project 观测接入')
@secure()
param appInsightsConnectionString string

@description('Key Vault resource ID，用于 project secret 引用')
param keyVaultId string

@description('Tags')
param tags object

// -----------------------------------------------------------------
// PLACEHOLDER —— 以下块为骨架占位。fork 实操时按上游 Ex01 真实模板替换。
// 当前用 Cognitive Services 路径作为占位（rebrand 后常见落点）；
// 真实跑前需确认 sku / kind / 子资源结构。
// -----------------------------------------------------------------

resource foundryAccount 'Microsoft.CognitiveServices/accounts@2024-10-01' = {
  name: '${projectName}-foundry'
  location: location
  tags: tags
  // TODO(fork): kind 在 rebrand 期可能是 'AIServices' / 'AIFoundry' / 'OpenAI'，按上游模板校正
  kind: 'AIServices'
  sku: {
    name: 'S0'
  }
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    customSubDomainName: '${projectName}-foundry'
    publicNetworkAccess: 'Enabled'
    // TODO(fork): disableLocalAuth = true 强制 AAD，避免 key auth；上游可能保留 key 以简化教学
    disableLocalAuth: false
  }
}

// TODO(fork): project 子资源（如果走 AIServices accounts/projects 模型）
//
// resource foundryProject 'Microsoft.CognitiveServices/accounts/projects@2024-10-01-preview' = {
//   parent: foundryAccount
//   name: projectName
//   location: location
//   properties: {
//     displayName: projectName
//   }
// }

// TODO(fork): 模型部署 —— 上游 Ex01 包含 gpt-4o-mini 部署，按真实模板补
//
// resource modelDeployment 'Microsoft.CognitiveServices/accounts/deployments@2024-10-01' = {
//   parent: foundryAccount
//   name: 'gpt-4o-mini'
//   sku: { name: 'GlobalStandard', capacity: 50 }
//   properties: {
//     model: { format: 'OpenAI', name: 'gpt-4o-mini', version: '2024-07-18' }
//   }
// }

// TODO(fork): connections（App Insights / Key Vault / AI Search / Cosmos）
//   接入方式与命名空间高度相关；占位不写，避免误导

// -----------------------------------------------------------------
// Outputs（最小集合，上游确定结构后再扩）
// -----------------------------------------------------------------

output projectId string = foundryAccount.id
output projectName string = foundryAccount.name
output foundryEndpoint string = foundryAccount.properties.endpoint
output foundryPrincipalId string = foundryAccount.identity.principalId

// 引用参数避免编译警告；真实模板会把它们注入 connection 资源
output _appInsightsBoundLength int = length(appInsightsConnectionString)
output _keyVaultBoundId string = keyVaultId
