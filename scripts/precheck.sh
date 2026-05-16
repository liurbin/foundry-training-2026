#!/usr/bin/env bash
# Foundry 培训环境自检脚本
# 用法：chmod +x precheck.sh && ./precheck.sh
# 把结果截图发助教

set +e
echo "===== Foundry 培训环境自检 ====="

# Python 3（macOS / Linux 默认无 `python`，统一用 python3）
PY=$(python3 --version 2>&1)
if [[ "$PY" == *"3.12"* || "$PY" == *"3.13"* ]]; then
  echo "✅ Python: $PY"
else
  echo "❌ Python: $PY (需 3.12+；用 pyenv / brew install python@3.12)"
fi

# uv
if uv --version >/dev/null 2>&1; then
  echo "✅ uv: $(uv --version)"
else
  echo "❌ uv 未安装"
fi

# Azure CLI
if az --version >/dev/null 2>&1; then
  echo "✅ az: $(az version --query '"azure-cli"' -o tsv)"
else
  echo "❌ Azure CLI 未安装"
fi

# Bicep
if az bicep version >/dev/null 2>&1; then
  echo "✅ Bicep: $(az bicep version 2>&1 | head -1)"
else
  echo "❌ Bicep 未安装（运行 az bicep install）"
fi

# Docker
if docker ps >/dev/null 2>&1; then
  echo "✅ Docker 运行中"
else
  echo "❌ Docker 未运行"
fi

# GitHub CLI
if gh auth status >/dev/null 2>&1; then
  echo "✅ gh 已登录"
else
  echo "❌ gh 未登录"
fi

# Azure 登录与订阅
if az account show >/dev/null 2>&1; then
  echo "✅ Azure 已登录: $(az account show --query name -o tsv) / $(az account show --query id -o tsv)"
else
  echo "❌ Azure 未登录，运行 az login"
fi

# Foundry 访问粗略检查
SUB=$(az account show --query id -o tsv 2>/dev/null)
if [[ -n "$SUB" ]]; then
  COUNT=$(az resource list --resource-type "Microsoft.CognitiveServices/accounts" --query "length(@)" -o tsv 2>/dev/null)
  echo "ℹ️  当前订阅可见的 Cognitive Services 资源数: $COUNT (培训会创建新的，不必非零)"
fi

# 网络连通性
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" https://ai.azure.com)
if [[ "$HTTP_CODE" =~ ^(200|302|401)$ ]]; then
  echo "✅ 能访问 ai.azure.com (HTTP $HTTP_CODE)"
else
  echo "❌ 无法访问 ai.azure.com (HTTP $HTTP_CODE)，检查 VPN/防火墙"
fi

echo "===== 自检完成 ====="
