# Instructor Day-7 rehearsal checklist

> This page is for the instructor, not learner hands-on steps. The goal is, 7 days before class, to run the v3 short course end to end against a real tenant, to avoid debugging SDK / portal / RBAC live.

## Must-run

Run the learner path end to end:

1. `hello.py`: confirm `PROJECT_ENDPOINT`, `MODEL_DEPLOYMENT_NAME`, Entra ID auth work.
2. Hands-on 0: create the prompt agent, run two rounds of `responses.create`, confirm agent name / version.
3. Trace: find the corresponding call in the portal, confirm entry point, latency, Application Insights connection status.
4. Hands-on 1: run 4 evals with `eval_dataset.jsonl`, get a `report_url`.
5. Fallback: run `workshop/docs/v3/code/run_eval.py` directly, confirm the script still works against the day's SDK.
6. Hands-on 2: create a new agent version, add Story 4 / Story 5 protection, re-run the eval.
7. Wrap-up: open Monitor / Quota / Compliance, confirm screenshots and day-of phrasing.

## Must-screenshot

- Project overview: full project endpoint value, OK to project after masking sensitive resource names.
- Build → Agents: agent name, version.
- Build → Agents → Traces: at least 1 top-level span, tokens, latency.
- Build → Evaluations: report for the 4 cases.
- Operate → Compliance: Policies / Guardrails / Security posture / Data security and governance.
- Operate → Quota: target model deployment, region / data zone, TPM / RPM or PTU status.

## Must-confirm

- SDK: `pip show azure-ai-projects` version; `create_version`, `agent_reference`, `evals.create` still work as documented.
- Endpoint: project endpoint domain as given by the portal; do not hand-convert `.ai.azure.com` / `.services.ai.azure.com`.
- Model: deployment name, deployment type, region / data zone, quota, PTU or not.
- Identity: can the learner account at least run S2; can the instructor account demo Compliance / Guardrails.
- Observability: is Application Insights connected; does the trace land in the portal.
- Guardrails: what can be seen on Build → Guardrails on the day, who can create / assign.
- Safety: how content filter, Prompt Shields, abuse monitoring, modified settings present on the day.

## Failure fallback

- Setup failure: if not resolved in 10 min, pair up to finish S2.
- Codex doesn't converge: if no runnable script in 5 min, copy `workshop/docs/v3/code/run_eval.py`.
- Eval API drift: the instructor demos a pre-run evaluation report and logs the SDK change as a post-class update.
- Trace doesn't appear: switch to Application Insights / app-side logs to explain the observability chain; keep portal trace as a Day-7 blocker.
- Guardrails insufficient permissions: demo entry point and screenshots only; learners only harden agent instructions in class.
- Quota / model unavailable: switch to a backup deployment; if that also fails, use screenshots to explain and convert S2 into an instructor demo.

## Send to learners before class

- `PROJECT_ENDPOINT`
- `MODEL_DEPLOYMENT_NAME`
- Azure account invite and login tenant
- Pre-class setup link
- Failure-reporting format: command, full error, OS, Python / Node / SDK versions; do not paste tokens or full endpoints.
