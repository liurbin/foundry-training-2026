// modules/container-apps.bicep — Container Apps Environment
//
// 用途：
//   - D5：单 agent 上 Container Apps + scaling/cost
//   - D9：生产化部署链路复用
//
// 注意：本模块只创建 environment，不创建具体 Container App。
//   D5 spec 才决定 min/max replicas、scale rules、镜像 —— 那时再加 container-app.bicep。

@description('部署区域')
param location string

@description('Container Apps environment 名称')
param envName string

@description('Log Analytics workspace resource ID（来自 app-insights 模块）')
param logAnalyticsWorkspaceId string

@description('Tags')
param tags object

// Log Analytics workspace 的 customerId / sharedKey 需从 ID 解析
// 这里通过 existing reference 拿
resource logAnalyticsRef 'Microsoft.OperationalInsights/workspaces@2023-09-01' existing = {
  name: last(split(logAnalyticsWorkspaceId, '/'))
}

resource cae 'Microsoft.App/managedEnvironments@2024-03-01' = {
  name: envName
  location: location
  tags: tags
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: logAnalyticsRef.properties.customerId
        sharedKey: logAnalyticsRef.listKeys().primarySharedKey
      }
    }
    workloadProfiles: [
      {
        name: 'Consumption'
        workloadProfileType: 'Consumption'
      }
    ]
    zoneRedundant: false
  }
}

output envId string = cae.id
output envName string = cae.name
output envDefaultDomain string = cae.properties.defaultDomain
