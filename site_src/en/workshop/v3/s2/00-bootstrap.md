# Hands-on 0: Stand up the Customer Operations Agent + run the first conversation (10 min opener + 20 min hands-on = 30 min)

> Duration: 30 min (includes the 10 min S2 opener) | Format: codex CLI hands-on | Credentials: environment variables pre-configured (see pre-class guide)
> Status: ⚠️ Concrete wording pending instructor Day-7 validation; the current page is a skeleton, but the SDK call structure is aligned with the Microsoft Foundry 2026/05 official quickstart

## Opener: evaluation first (10 min, instructor-led)

Distilled from v2 D7 + D9 and the Foundry official [Evaluate your AI agents](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/evaluate-agent):

- **Write the evaluation before the feature** — agent output is probabilistic; without an evaluation there is no objective standard for "done"
- The v3 posture: Hands-on 0 stands up the agent → Hands-on 1 immediately runs an evaluation with **Foundry built-in evaluators** → Hands-on 2 adds a **Control Plane guardrail policy** and re-runs the evaluation → **evaluation runs throughout S2**
- Today's endpoint is the Foundry project endpoint issued by the instructor; all business data is mocked (see [scenario.md](../scenario.md))

## What you will do in this segment (20 min hands-on)

Use codex CLI to have AI help you:

1. Create a **prompt agent** in the Foundry project (type = prompt, the agent type currently GA in Foundry)
2. Call it with the `azure-ai-projects` 2.x SDK + Responses API
3. Have the agent answer "I want to check order ORD-T-12345"
4. See the trace span for this call in the Foundry portal (the entry point and GA / preview status are to be confirmed by instructor Day-7 validation)

### The capability you are practicing

Compress a business workflow into a **minimum runnable baseline agent**, and leave behind the version and trace evidence that later eval / guardrail steps can trace back to.

### Deliverables of this segment

- A callable `AGENT_NAME` + baseline version.
- Two real agent responses: happy path + edge input.
- One portal trace evidence.
- A baseline evidence record for use by Hands-on 1 / 2.

### Not the goal of this segment

- Not building a full customer-service system.
- Not wiring a real order API.
- Not making the system prompt production-ready.

**Simplifying conventions** (important):

- Order data is **hardcoded in the agent's instructions (system prompt)** — no tool calls, no reading from mock JSON
- The real production shape: use **Function calling / OpenAPI tool** to call an external API, or use **Foundry IQ** to connect a knowledge base; these are post-class extensions
- The three P0 query capabilities in scenario.md are the **target blueprint**; Hands-on 0 only does the minimum subset

## Preparation

Open a new terminal, activate the venv, check environment variables:

```bash
source ~/foundry-v3-env/bin/activate
cd ~/foundry-v3-tmp     # or the working directory you created before class

# Confirm credentials + environment variables
az account show | head -5
echo $PROJECT_ENDPOINT
echo $MODEL_DEPLOYMENT_NAME
echo $AGENT_NAME
```

## Step 1: have codex stand up the agent (10 min)

Enter codex interactive mode:

```bash
codex
```

Once inside, give it this requirement (**this is the v3 recommended prompt template; the instructor will iterate it on Day-7**):

```
Help me create a prompt agent in Microsoft Foundry using the azure-ai-projects 2.x SDK. Read the name from the environment variable AGENT_NAME. Requirements:

1. Authenticate with DefaultAzureCredential, read the endpoint from PROJECT_ENDPOINT
2. Read model from MODEL_DEPLOYMENT_NAME
3. instructions (system prompt):
   "You are the customer-service assistant for a mid-sized e-commerce company, and can look up order status, logistics, and refund progress.
    Important constraints: do not commit to refunds, do not initiate outbound calls; for complaint-escalation phrasing (threats of complaints / 12315 / full refund demands, etc.) transfer to a human.
    You currently hardcode-know one order: ORD-T-12345 has been shipped, expected to arrive tomorrow, tracking number SF1234567890.
    For any other order number, ask the user to provide a valid order number or phone number."
4. Call PromptAgentDefinition + project.agents.create_version
5. Print agent.name / agent.version

Execute it after you finish writing.
```

**Key**: when codex gives you a plan, **review before letting it execute** — review 4 things:

- Whether the package name is right (must be `azure-ai-projects`, not something else)
- How credentials are read (must be `DefaultAzureCredential`; don't let it read something like `OPENAI_API_KEY`)
- That it doesn't write endpoint / token into logs
- That it doesn't hardcode the instructions into the code (they should go through a variable so they're easy to change later)

### Expected output

```
Agent created (name: customer-service-agent-v3-yourname, version: 1)
```

`TODO instructor Day-7`: paste a real console output + Foundry portal screenshot (you should be able to see this agent under Build → Agents).

## Step 2: run one conversation (5 min)

Continue in codex:

```
Now write another script that calls the agent we just created:

1. Use project.get_openai_client() to get an OpenAI-compatible client
2. openai.conversations.create() to start a conversation
3. openai.responses.create(
       conversation=conversation.id,
       extra_body={"agent_reference": {"name": AGENT_NAME, "type": "agent_reference"}},
       input="I want to check order ORD-T-12345",
   )
4. Print response.output_text
5. In the same conversation, ask "what about my order abc123" and see how the agent asks back

Execute it.
```

### Expected output (instructor Day-7 to fill real example)

```
[Round 1]
Your order ORD-T-12345 has been shipped, expected to arrive tomorrow, tracking number SF1234567890.

[Round 2]
The "abc123" you provided is not a valid order-number format. Please provide an order number in the form ORD-YYYYMMDD-XXXXX,
or leave a phone number and I will check for you.
```

## Step 3: view the trace in the Foundry portal (5 min)

Open the Foundry portal link the instructor sent (`https://ai.azure.com`, with the **New Foundry** toggle at the top turned on), find your project:

1. From the 5 sections at the top, choose **Build**
2. In the left panel choose **Agents** → you should see the agent you just created, version = 1
3. At the **top of the Agents page**, switch to the **Traces** tab → you should see the two `responses.create` calls

> ⚠️ The trace entry point is **Build → Agents → Traces tab** (at the top, not in the Operate left panel). Source: [Set up tracing in Foundry](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup) "In the left navigation, select Agents. At the top, select Traces."

Expected to see (from the Foundry official [Agent tracing concepts](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept)):

- ✅ Top-level span: agent call
- ✅ Child span: LLM call (model = your deployment)
- ✅ Token counts (prompt + completion)
- ✅ Latency (end-to-end ms)
- ✅ Input / output text

> v3 uses prompt agent server-side tracing; the Tracing docs and parts of the portal experience may still be marked preview. The instructor must, on Day-7, confirm the entry point, data latency, and GA / preview status against the tenant on the day.

Can't see it? Common reasons:

- Your project is not yet connected to Application Insights (trace data is stored there — instructor Day-7 confirms the project is configured; if the portal prompts "Connect Application Insights", the project is not connected yet)
- Trace is async and hasn't arrived (wait 30s and refresh)
- The agent didn't actually run (the output in Step 1/2 was sample text fabricated by codex rather than a real return — go back and review the code)

### Baseline evidence record

Write down the 5 items below; later eval and guardrail steps both refer to them:

| Item | Your value |
|---|---|
| Agent name |  |
| Baseline version |  |
| Model deployment |  |
| Trace visible? | yes / no |
| Trace entry time / screenshot |  |

## Step 4: self-check (5 min)

- [ ] `project.agents.create_version` actually ran once (codex executed it + you saw agent name / version)
- [ ] `openai.responses.create` ran twice, output contains order number + ETA + tracking number; the second turn shows ask-back behavior
- [ ] Portal trace shows at least 1 top-level span + token counts
- [ ] You can explain in one sentence "what codex just did, and which points I reviewed"

### You should be able to restate

- Which minimum workflow does this baseline agent solve?
- Which agent version did you create?
- Why does this step hardcode data instead of connecting a real system?
- What does the trace prove, and what does it not prove?

Four boxes checked = Hands-on 0 pass (corresponds to the first item in the §scoring "implementation" dimension).

## Enterprise Readiness checkpoint

In class this step only validates that the instructor-issued project endpoint + current model deployment work end to end. Before production, also cover:

- **Identity**: runtime uses managed identity, not a personal `az login`.
- **Network**: confirm public vs private endpoint, and the outbound path for tools.
- **Deployment**: confirm Global / Data Zone / Regional / PTU; do not treat the class's shared capacity as a production recommendation.
- **Quota**: confirm the target model has sufficient TPM/RPM under the target region / deployment type.

## Common pitfalls (instructor Day-7 to fill)

| Symptom | Action |
|---|---|
| `DefaultAzureCredential failed` | `az login` and re-run; check the Foundry User role |
| `ModuleNotFoundError: azure.ai.projects` | Not in venv, or 1.x installed; `pip install --upgrade "azure-ai-projects>=2.0.0"` |
| `404 Not Found` | `PROJECT_ENDPOINT` was concatenated wrong; copy the full project endpoint from the instructor DM or portal overview, do not hand-edit the domain |
| `AttributeError: 'AgentsOperations' object has no attribute 'create_version'` | 1.x installed; reinstall 2.x as above |
| codex keeps revising the code without converging | Tell it explicitly "stop, paste the full current stacktrace before changing anything" |
| Runs through but no trace in portal | Project is not connected to Application Insights — this is not a learner problem; tell the instructor |

## Post-class extensions

- **Add a tool (function calling or MCP)**: change order lookup from hardcoded-in-instructions to a tool call; see an extra `execute_tool` span in the trace
- **Connect Foundry IQ**: turn "FAQ / return policy" into a knowledge base and let the agent use agentic retrieval instead of stuffing the system prompt
- **Use an OpenAPI tool to connect a mock order API**: wrap `mock_orders.json` as a FastAPI service, write an OpenAPI spec, and let the agent call it

→ Next segment: [Hands-on 1: run evaluations with Foundry built-in evaluators](01-eval.md)
