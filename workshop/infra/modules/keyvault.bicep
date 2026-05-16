// modules/keyvault.bicep — Key Vault + RBAC
//
// D3 spec 约束（必须遵守）：
//   - 不准 hardcode 任何 secret
//   - 所有 secret 引用走 Key Vault + managed identity
//   - 启用 RBAC authorization（不用 access policies —— legacy）
//
// 本模块只授权 deployer（让 deploy 时能手动放种子 secret）；
// 其它消费者（Foundry / Container App 的 managed identity）的 RBAC
// 在各自模块创建后通过 keyvault-rbac 子模块按需追加。

@description('部署区域')
param location string

@description('Key Vault 名称（全局唯一）')
@minLength(3)
@maxLength(24)
param keyVaultName string

@description('部署人/服务主体 objectId —— 授予 Key Vault Administrator')
param deployerPrincipalId string

@description('Tags')
param tags object

@description('SKU')
@allowed([
  'standard'
  'premium'
])
param skuName string = 'standard'

resource kv 'Microsoft.KeyVault/vaults@2024-04-01-preview' = {
  name: keyVaultName
  location: location
  tags: tags
  properties: {
    tenantId: subscription().tenantId
    sku: {
      family: 'A'
      name: skuName
    }
    enableRbacAuthorization: true            // 强制 RBAC，禁用 access policies
    enableSoftDelete: true
    softDeleteRetentionInDays: 7             // 培训环境，短保留
    enablePurgeProtection: null              // 培训环境不开 purge protection 便于反复创建删除
    publicNetworkAccess: 'Enabled'           // 培训简化；生产应走 private endpoint
  }
}

// RBAC: 授予 deployer "Key Vault Administrator"，能放入种子 secret
// role definition id 来源：https://learn.microsoft.com/azure/role-based-access-control/built-in-roles
var kvAdministratorRoleId = '00482a5a-887f-4fb3-b363-3b7fe8e74483'

resource deployerKvAdmin 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  scope: kv
  name: guid(kv.id, deployerPrincipalId, kvAdministratorRoleId)
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', kvAdministratorRoleId)
    principalId: deployerPrincipalId
    principalType: 'User'  // 若是 service principal，改 'ServicePrincipal'
  }
}

// 用于其它模块为 managed identity 授权的 role id 暴露
// （Foundry / Container App 的 system-assigned MI 需要 "Key Vault Secrets User" = 4633458b-17de-408a-b874-0445c86b69e6）
output keyVaultId string = kv.id
output keyVaultName string = kv.name
output keyVaultUri string = kv.properties.vaultUri
output secretsUserRoleId string = '4633458b-17de-408a-b874-0445c86b69e6'
