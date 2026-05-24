# Customer Operations Agent Runbooks

These are course examples, not production runbooks. Real projects must adapt owner, alert source, data policy, and escalation path.

## 1. 429 Rate Limit

### Trigger

Application Insights or Foundry metrics show `RateLimitExceeded` more than 5 times in 1 minute.

### First Response

1. Identify the deployment and environment.
2. Check whether traffic is a real business peak or an abnormal burst.
3. If abnormal, enable app-side throttling and return a "system busy" fallback.

### Recovery

- For real peak: request quota or move traffic to an approved fallback deployment.
- For abnormal burst: keep throttling, inspect source, and notify oncall.

## 2. Unauthorized Refund Promise

### Trigger

Eval, trace review, or user report shows the agent saying "已为您退款", "立即退款", or equivalent wording.

### First Response

1. Disable the affected agent version or roll back to the previous version.
2. Search traces for similar outputs.
3. Route affected conversations to human support.

### Recovery

- Add or tighten business instructions.
- Add output filter for refund-commitment phrases.
- Re-run Story 4 and Story 5 eval cases before re-enabling.

## 3. Missing Traces

### Trigger

Agent calls succeed, but no trace appears in the portal after 5 minutes.

### First Response

1. Confirm the request really reached the agent.
2. Check Application Insights connection for the project.
3. Check whether the tracing feature is enabled and supported in the current tenant / region.

### Recovery

- Reconnect Application Insights if needed.
- Fall back to app-side structured logs: request id, agent name, version, latency, error type.

## 4. Model or Region Outage

### Trigger

5xx errors, deployment unavailable, or region outage alerts affect production traffic.

### First Response

1. Switch to read-only or human-support fallback if customer impact is high.
2. Confirm whether the issue is model deployment, quota, network, or tool backend.
3. Notify owner and support channel.

### Recovery

- Route to approved fallback deployment if available.
- If no fallback exists, keep human-support mode and publish status updates.
- After recovery, run eval regression before restoring full automation.
