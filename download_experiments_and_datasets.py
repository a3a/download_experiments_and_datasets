import os
import pandas as pd
from datetime import datetime
import argparse
import requests

# === CONFIGURATION ===
def get_output_directory(project_id: str) -> str:
    """Generate a timestamped output directory for a project."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join("output", f"{project_id}_{timestamp}")

# --- Real API get_data implementation ---
def get_data(endpoint: str, api_key: str, project_id: str):
    """
    Fetch data from a given endpoint using the provided API key and project ID.
    This function should return a list of dictionaries representing items.
    Each item should have 'id' and 'data' keys.
    """
    base_url = "https://api.example.com"  # Replace with your real base URL
    url = f"{base_url}/{endpoint}?project_id={project_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch {endpoint}: {response.status_code} {response.text}")
    return response.json()

# --- Mock for offline testing (commented out) ---
"""
def get_data(endpoint: str, api_key: str, project_id: str):
    # Mocked data for offline testing: returns dummy experiments or datasets.
    if api_key != "test_api_key_123" or project_id != "test_project_456":
        raise RuntimeError("Invalid API key or project ID for mock testing.")

    if endpoint == "experiments":
        return [
            {
                "id": "exp001",
                "data": [
                    {"name": "Test Exp 1", "value": 123},
                    {"name": "Test Exp 2", "value": 456},
                ],
            },
            {
                "id": "exp002",
                "data": [
                    {"name": "Test Exp A", "value": 789},
                    {"name": "Test Exp B", "value": 101},
                ],
            },
        ]
    elif endpoint == "datasets":
        return [
            {
                "id": "ds001",
                "data": [
                    {"col1": "A", "col2": 1},
                    {"col1": "B", "col2": 2},
                ],
            },
            {
                "id": "ds002",
                "data": [
                    {"col1": "X", "col2": 42},
                    {"col1": "Y", "col2": 99},
                ],
            },
        ]
    else:
        raise RuntimeError(f"Unknown endpoint: {endpoint}")
"""

def download_experiments(output_dir: str, api_key: str, project_id: str):
    """Download experiments and save each one to a separate CSV file."""
    experiments = get_data("experiments", api_key, project_id)
    for exp in experiments:
        exp_id = exp["id"]
        df = pd.DataFrame(exp["data"])
        filepath = os.path.join(output_dir, f"experiment_{exp_id}.csv")
        df.to_csv(filepath, index=False)

def download_datasets(output_dir: str, api_key: str, project_id: str):
    """Download datasets and save each one to a separate CSV file."""
    datasets = get_data("datasets", api_key, project_id)
    for ds in datasets:
        ds_id = ds["id"]
        df = pd.DataFrame(ds["data"])
        filepath = os.path.join(output_dir, f"dataset_{ds_id}.csv")
        df.to_csv(filepath, index=False)

def main():
    """Main entry point: parses arguments, prepares output directory, and triggers downloads."""
    parser = argparse.ArgumentParser(description="Download experiments and datasets for a given project.")
    parser.add_argument("--api-key", required=True, help="API key for authentication")
    parser.add_argument("--project-id", required=True, help="Project ID to download data for")
    args = parser.parse_args()

    output_dir = get_output_directory(args.project_id)
    os.makedirs(output_dir, exist_ok=True)
    print(f"Saving files to: {output_dir}")

    download_experiments(output_dir, args.api_key, args.project_id)
    download_datasets(output_dir, args.api_key, args.project_id)
    print("Download complete.")

if __name__ == "__main__":
    main()
