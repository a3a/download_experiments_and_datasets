import os
import requests
import pandas as pd

# Replace with project-specific API endpoint and authentication token
API_BASE_URL = "https://api.example.com/projects/{project_id}"
AUTH_TOKEN = "your_auth_token_here"
OUTPUT_DIRECTORY = "output_directory"

# Ensure the output directory exists
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

def get_data(endpoint):
    """Fetch data from the API endpoint."""
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def save_to_csv(data, filename):
    """Save the data to a CSV file."""
    df = pd.DataFrame(data)
    output_path = os.path.join(OUTPUT_DIRECTORY, filename)
    df.to_csv(output_path, index=False)
    print(f"Saved: {output_path}")

def main():
    try:
        # Fetch all experiments
        experiments_url = f"{API_BASE_URL}/experiments"
        experiments = get_data(experiments_url)
        
        # Save each experiment to its own CSV
        for experiment in experiments:
            file_name = f"experiment_{experiment['id']}.csv"
            save_to_csv(experiment["data"], file_name)

        # Fetch all datasets
        datasets_url = f"{API_BASE_URL}/datasets"
        datasets = get_data(datasets_url)
        
        # Save each dataset to its own CSV
        for dataset in datasets:
            file_name = f"dataset_{dataset['id']}.csv"
            save_to_csv(dataset["data"], file_name)

        print("All experiments and datasets have been downloaded.")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while communicating with the API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()