#!/usr/bin/env bash
# deploy.sh — D3 Bicep 部署示例（讲师演示）
#
# 学员不在课堂跑此脚本。见 README.md "为什么学员不真跑"。
#
# 用法：
#   1. cp parameters.example.json parameters.json && 编辑
#   2. az login && az account set --subscription <SUB_ID>
#   3. ./deploy.sh [what-if|deploy]   (默认 what-if)

set -euo pipefail

LOCATION="${LOCATION:-eastus2}"
TEMPLATE_FILE="${TEMPLATE_FILE:-main.bicep}"
PARAMETERS_FILE="${PARAMETERS_FILE:-parameters.json}"
DEPLOYMENT_NAME="${DEPLOYMENT_NAME:-foundry-d3-$(date +%Y%m%d-%H%M%S)}"
ACTION="${1:-what-if}"

if [[ ! -f "$PARAMETERS_FILE" ]]; then
  echo "ERROR: $PARAMETERS_FILE 不存在。先 cp parameters.example.json parameters.json 并填值。" >&2
  exit 1
fi

# 自动补 deployerPrincipalId（如果还是占位）
if grep -q "REPLACE_WITH_YOUR_OBJECT_ID" "$PARAMETERS_FILE"; then
  CURRENT_OID=$(az ad signed-in-user show --query id -o tsv 2>/dev/null || true)
  if [[ -n "$CURRENT_OID" ]]; then
    echo "INFO: 自动用当前登录用户 objectId ($CURRENT_OID) 替换 placeholder。"
    sed -i.bak "s/REPLACE_WITH_YOUR_OBJECT_ID/$CURRENT_OID/" "$PARAMETERS_FILE"
  else
    echo "ERROR: parameters.json 里 deployerPrincipalId 还是 placeholder，且无法获取当前用户 objectId。" >&2
    exit 1
  fi
fi

echo "=== 模板:     $TEMPLATE_FILE"
echo "=== 参数文件: $PARAMETERS_FILE"
echo "=== 区域:     $LOCATION"
echo "=== 部署名:   $DEPLOYMENT_NAME"
echo "=== 动作:     $ACTION"
echo

case "$ACTION" in
  what-if)
    az deployment sub what-if \
      --name "$DEPLOYMENT_NAME" \
      --location "$LOCATION" \
      --template-file "$TEMPLATE_FILE" \
      --parameters @"$PARAMETERS_FILE"
    ;;
  deploy)
    az deployment sub create \
      --name "$DEPLOYMENT_NAME" \
      --location "$LOCATION" \
      --template-file "$TEMPLATE_FILE" \
      --parameters @"$PARAMETERS_FILE"
    ;;
  *)
    echo "未知动作: $ACTION (允许 what-if | deploy)" >&2
    exit 2
    ;;
esac
