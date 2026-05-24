import os
import sys
import time

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential


DATASET_NAME = os.getenv("EVAL_DATASET_NAME", "cs-eval")
DATASET_VERSION = os.getenv("EVAL_DATASET_VERSION", "1")
EVAL_TIMEOUT_SECONDS = int(os.getenv("EVAL_TIMEOUT_SECONDS", "600"))


def get_required_env(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def main():
    dataset_path = sys.argv[1] if len(sys.argv) > 1 else "eval_dataset.jsonl"
    project_endpoint = get_required_env("PROJECT_ENDPOINT")
    agent_name = get_required_env("AGENT_NAME")
    deployment_name = get_required_env("MODEL_DEPLOYMENT_NAME")

    project = AIProjectClient(
        endpoint=project_endpoint,
        credential=DefaultAzureCredential(),
    )

    project.datasets.upload_file(
        name=DATASET_NAME,
        version=DATASET_VERSION,
        file_path=dataset_path,
    )

    client = project.get_openai_client()

    testing_criteria = [
        {
            "type": "azure_ai_evaluator",
            "name": "task_adherence",
            "evaluator": "builtin.task_adherence",
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_items}}",
            },
            "initialization_parameters": {
                "deployment_name": deployment_name,
            },
        },
        {
            "type": "azure_ai_evaluator",
            "name": "coherence",
            "evaluator": "builtin.coherence",
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_text}}",
            },
            "initialization_parameters": {
                "deployment_name": deployment_name,
            },
        },
        {
            "type": "azure_ai_evaluator",
            "name": "violence",
            "evaluator": "builtin.violence",
            "data_mapping": {
                "response": "{{sample.output_text}}",
            },
        },
    ]

    evaluation = client.evals.create(
        name="customer-operations-v3",
        data_source_config={
            "type": "custom",
            "item_schema": {
                "query": "string",
            },
        },
        testing_criteria=testing_criteria,
    )

    target = {
        "type": "azure_ai_agent",
        "name": agent_name,
    }
    agent_version = os.getenv("AGENT_VERSION")
    if agent_version:
        target["version"] = agent_version

    run = client.evals.runs.create(
        eval_id=evaluation.id,
        name="customer-operations-v3-run",
        data_source={
            "type": "azure_ai_target_completions",
            "dataset_name": DATASET_NAME,
            "dataset_version": DATASET_VERSION,
            "target": target,
        },
    )

    print(f"Evaluation run started: {run.id}")
    deadline = time.time() + EVAL_TIMEOUT_SECONDS

    while True:
        current = client.evals.runs.retrieve(
            eval_id=evaluation.id,
            run_id=run.id,
        )
        status = getattr(current, "status", None)
        print(f"Status: {status}")

        if status in {"completed", "failed", "cancelled"}:
            break
        if time.time() > deadline:
            raise TimeoutError(f"Evaluation did not finish within {EVAL_TIMEOUT_SECONDS}s")
        time.sleep(5)

    print(f"Report URL: {getattr(current, 'report_url', None)}")
    print(f"Result counts: {getattr(current, 'result_counts', None)}")

    if status != "completed":
        raise RuntimeError(f"Evaluation ended with status: {status}")


if __name__ == "__main__":
    main()
