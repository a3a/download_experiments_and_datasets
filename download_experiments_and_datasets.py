import os
import pandas as pd
from datetime import datetime

# === CONFIGURATION ===
def get_output_directory(project_id: str) -> str:
    """Generate a timestamped output directory for a project."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join("output", f"{project_id}_{timestamp}")

# Dummy placeholder for API or data fetching logic
def get_data(endpoint: str):
    """
    Simulate or fetch data from a given endpoint.
    This function should return a list of dictionaries representing items.
    Each item should have 'id' and 'data' keys.
    """
    raise NotImplementedError("You must implement get_data() to fetch real data.")

def download_experiments(output_dir: str):
    """Download experiments and save each one to a separate CSV file."""
    experiments = get_data("experiments")  # Returns list of {id, data}
    for exp in experiments:
        exp_id = exp["id"]
        df = pd.DataFrame(exp["data"])
        filepath = os.path.join(output_dir, f"experiment_{exp_id}.csv")
        df.to_csv(filepath, index=False)

def download_datasets(output_dir: str):
    """Download datasets and save each one to a separate CSV file."""
    datasets = get_data("datasets")  # Returns list of {id, data}
    for ds in datasets:
        ds_id = ds["id"]
        df = pd.DataFrame(ds["data"])
        filepath = os.path.join(output_dir, f"dataset_{ds_id}.csv")
        df.to_csv(filepath, index=False)

def main(project_id="project123"):
    """Main entry point: prepares output directory and triggers downloads."""
    output_dir = get_output_directory(project_id)
    os.makedirs(output_dir, exist_ok=True)
    print(f"Saving files to: {output_dir}")
    download_experiments(output_dir)
    download_datasets(output_dir)

if __name__ == "__main__":
    main()
