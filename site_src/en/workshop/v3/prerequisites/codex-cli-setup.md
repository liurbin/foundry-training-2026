# Learner pre-class setup: codex CLI + Microsoft Foundry SDK

> Applies to: v3 short course (S1+S2 total 4h, AI CLI copilot as the main thread)
> Target time: **complete in under 15 minutes**
> System: macOS (for other systems, contact the instructor)
> Status: ⚠️ Not yet verified by the instructor on Day-7; defer to the final version the instructor sends pre-class.

## What you'll receive

The instructor will send you **a DM before class** containing:

- `PROJECT_ENDPOINT`: copy the full project endpoint from the Foundry portal project overview (may be a `.ai.azure.com` or `.services.ai.azure.com` domain; **do not change the domain by hand**)
- `MODEL_DEPLOYMENT_NAME`: model deployment name (the instructor deploys it in Foundry on Day-7; during the rebrand period the model catalog drifts, **defer to the instructor's DM**)
- An Azure account invitation (after `az login` with your own Microsoft account you'll get the **Foundry User** role)

**Important**: v3 uses Microsoft Foundry's current main path—**Entra ID auth (`DefaultAzureCredential` + `az login`)**, not API keys. After the course the instructor will revoke your RBAC on the Foundry project.

> Why model deployment names / SDK version details are not hard-coded in this doc: Foundry is still in the rebrand period (Azure AI Foundry → Microsoft Foundry); **model catalog, portal UI, preview feature GA status** are all evolving. The values in the instructor's post-Day-7 DM are the day's truth.
>
> No need to worry about API version—Foundry has moved from a monthly `api-version` parameter to **v1 stable routes** (`/openai/v1/`); the SDK takes the stable route automatically.

## Steps

### 1. Install Azure CLI + Python ≥ 3.8

```bash
# Azure CLI (if missing)
brew install azure-cli

# Python ≥ 3.8
python --version    # should be ≥ 3.8; if not, brew install python@3.12 or pyenv

# Verify
az --version
python --version
```

### 2. Install codex CLI and Node.js 20+

```bash
# Node (codex dependency)
brew install node
node --version   # should be ≥ v20

# codex CLI
npm install -g @openai/codex
codex --version
```

If `npm install -g` errors on permissions, **do not use sudo**; instead:

```bash
mkdir -p ~/.npm-global
npm config set prefix ~/.npm-global
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.zshrc
source ~/.zshrc
npm install -g @openai/codex
```

### 3. Install the Foundry Python SDK

```bash
# Recommended: create an isolated venv
python -m venv ~/foundry-v3-env
source ~/foundry-v3-env/bin/activate

# Install Foundry projects SDK (must be 2.x; 1.x corresponds to Foundry classic)
pip install "azure-ai-projects>=2.0.0" "azure-identity"
```

> The codex CLI will install/upgrade packages for you during class; the venv exists so that what codex installs doesn't pollute the global environment.

### 4. Configure Foundry project environment variables

Append to the end of your shell rc file (default on macOS is `~/.zshrc`), **replacing the values with what the instructor sent**:

```bash
# Microsoft Foundry for v3 training
export PROJECT_ENDPOINT="<PROJECT_ENDPOINT from instructor DM>"
export MODEL_DEPLOYMENT_NAME="<model deployment name from instructor DM>"
export AGENT_NAME="customer-service-agent-v3-$(whoami)"   # add your own name to avoid collisions
```

Apply the config:

```bash
source ~/.zshrc
```

### 5. Azure login (Entra ID)

```bash
az login
# Browser opens the Microsoft sign-in page; log in with the account the instructor invited
az account show    # should show subscription + tenant
```

> v3 doesn't hand you an API key—identity is managed by Entra ID. `DefaultAzureCredential` in the SDK automatically picks up the credentials `az login` leaves behind.

### 6. Make the first Foundry call work

Open a new terminal tab (confirm venv + env are both active):

```bash
source ~/foundry-v3-env/bin/activate
cd ~ && mkdir -p foundry-v3-tmp && cd foundry-v3-tmp
```

Save the following as `hello.py`:

```python
import os
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

project = AIProjectClient(
    endpoint=os.environ["PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
openai = project.get_openai_client()

response = openai.responses.create(
    model=os.environ["MODEL_DEPLOYMENT_NAME"],
    input="用一句话介绍 Microsoft Foundry。",
)
print(response.output_text)
```

Run:

```bash
python hello.py
```

You should see a Chinese reply.

### 7. Run codex CLI once (confirm the copilot environment is ready)

```bash
codex
```

In interactive mode, type:

```
Read hello.py in the current directory and tell me what this code does.
```

You should get a summary from codex. Exit with `/exit` or Ctrl-D.

### 8. Self-check checklist

Tick all 6 before showing up to class:

- [ ] `az account show` output includes subscription + tenant
- [ ] `python --version` ≥ 3.8
- [ ] `pip show azure-ai-projects` shows ≥ 2.0.0
- [ ] `node --version` ≥ v20, `codex --version` has output
- [ ] `echo $PROJECT_ENDPOINT` outputs the endpoint the instructor sent
- [ ] `hello.py` in step 6 produces a real model reply (not an exception stacktrace)

## Common errors (compiled from public patterns; the instructor will add Day-7 live cases)

| Symptom | Possible cause | Fix |
|---|---|---|
| `command not found: codex` | global npm bin not on PATH | see the `~/.npm-global` solution in step 2 |
| `DefaultAzureCredential failed to retrieve a token` | no `az login`, or the login account doesn't have the Foundry User role | rerun `az login`; check with the instructor that the role is assigned |
| `404 Not Found` / `Connection refused` | `PROJECT_ENDPOINT` is wrong, or resource/project name is wrong | match against the full string the instructor sent or the project endpoint in portal overview; do not hand-convert between `.ai.azure.com` and `.services.ai.azure.com` |
| `model not found` | `MODEL_DEPLOYMENT_NAME` wrong, or that deployment is not exposed to the project | match against the deployment name the instructor sent; during rebrand the model catalog drifts, don't guess |
| `ModuleNotFoundError: azure.ai.projects` | venv not active, or wrong SDK version | `source ~/foundry-v3-env/bin/activate` + `pip install "azure-ai-projects>=2.0.0"` |
| `AttributeError` on `evals` / `responses` | installed 1.x (Foundry classic) | `pip install --upgrade "azure-ai-projects>=2.0.0"` |
| Network timeout | local proxy / company network blocking `*.ai.azure.com` or `*.services.ai.azure.com` | retry on a phone hotspot, or ask the instructor for a backup endpoint |

## Failure fallback

- Stuck for over 10 minutes: in the group chat, @instructor with the **complete error + the command you ran** (**do not paste the full endpoint URL or any token**)
- Completely unable to set up before class: pair up with a neighbor in class to do the hands-on; the instructor will walk you through it 1:1 after class

## Security reminders

- The resource name in `PROJECT_ENDPOINT` is not highly sensitive, but **do not commit it to a public repo** (it contains subdomain info)
- The token left behind by `az login` is cached in `~/.azure/`; you can clear it with `az logout` after the course
- After the course the instructor will revoke your Foundry RBAC; no cleanup needed on your side
- If you suspect the account has been compromised (phishing / device loss), immediately `az logout` + terminate sessions on the Microsoft account page, then tell the instructor

## Feedback

Blockers hit before or during class—please write **1 sentence** in the group chat after class; the instructor will fold it back into this guide—the next cohort benefits.
