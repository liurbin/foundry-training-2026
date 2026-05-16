// main.bicep — D3 顶层入口（subscription scope）
//
// 作用：创建 Resource Group，调用 4 个模块（foundry-project / app-insights / container-apps / keyvault）。
// 不在本文件写资源细节 —— 模块化是 D3 spec 约束之一。
//
// 状态：未在真实订阅验证。API 版本与 Foundry 资源类型在 fork 实操阶段校正。

targetScope = 'subscription'

// ----------------------------- 参数 -----------------------------

@description('部署区域，例如 eastus2 / swedencentral')
param location string

@description('Resource Group 名称')
param rgName string

@description('Foundry project 名称（短名，会用于其他资源命名前缀）')
@minLength(3)
@maxLength(20)
param projectName string

@description('Container Apps 环境名称，默认基于 projectName 派生')
param containerAppsEnvName string = '${projectName}-cae'

@description('Key Vault 名称（全局唯一，3-24 字符）')
param keyVaultName string = '${projectName}-kv-${uniqueString(subscription().id, rgName)}'

@description('部署人/服务主体的 objectId —— 用于初始 Key Vault RBAC 授权')
param deployerPrincipalId string

@description('通用 tags')
param tags object = {
  workshop: 'foundry-training-2026'
  module: 'D3'
  owned_by: 'instructor'
}

// ----------------------------- RG -----------------------------

resource rg 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: rgName
  location: location
  tags: tags
}

// ----------------------------- 模块 -----------------------------

module appInsights 'modules/app-insights.bicep' = {
  name: 'appInsights-deploy'
  scope: rg
  params: {
    location: location
    projectName: projectName
    tags: tags
  }
}

module keyvault 'modules/keyvault.bicep' = {
  name: 'keyvault-deploy'
  scope: rg
  params: {
    location: location
    keyVaultName: keyVaultName
    deployerPrincipalId: deployerPrincipalId
    tags: tags
  }
}

module containerApps 'modules/container-apps.bicep' = {
  name: 'containerApps-deploy'
  scope: rg
  params: {
    location: location
    envName: containerAppsEnvName
    logAnalyticsWorkspaceId: appInsights.outputs.logAnalyticsWorkspaceId
    tags: tags
  }
}

module foundry 'modules/foundry-project.bicep' = {
  name: 'foundry-project-deploy'
  scope: rg
  params: {
    location: location
    projectName: projectName
    appInsightsConnectionString: appInsights.outputs.appInsightsConnectionString
    keyVaultId: keyvault.outputs.keyVaultId
    tags: tags
  }
}

// ----------------------------- Outputs -----------------------------

output rgNameOut string = rg.name
output foundryProjectId string = foundry.outputs.projectId
output containerAppsEnvId string = containerApps.outputs.envId
output keyVaultUri string = keyvault.outputs.keyVaultUri
output appInsightsConnectionString string = appInsights.outputs.appInsightsConnectionString
