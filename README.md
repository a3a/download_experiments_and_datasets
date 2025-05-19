# Download Experiments and Datasets

This repository provides a Python script to download **all experiments** and **datasets** associated with a specified project. Each experiment and dataset is saved as an individual CSV file inside a timestamped output directory for easy organization and version control.

---

## Features

- Fetches **all experiments** and **datasets** from a data API.
- Saves each experiment and dataset to separate CSV files.
- Automatically organizes outputs into timestamped directories.
- Includes a test suite with mocked data to verify functionality without requiring API access.

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- `pandas` (for CSV handling)
- `pytest` (for running tests)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/a3a/download_experiments_and_datasets.git
   cd download_experiments_and_datasets


### Running the Script
Run the downloader script with an optional project ID argument:

python download_experiments_and_datasets.py [project_id]
If you omit [project_id], it defaults to "project123".

The script downloads all experiments and datasets and saves each as a separate CSV.

Output files are saved in a directory named:
output/<project_id>_<YYYYMMDD_HHMMSS>/

For example:
python download_experiments_and_datasets.py myproject
creates files like:

output/myproject_20250518_162530/experiment_1.csv
output/myproject_20250518_162530/dataset_100.csv

### Running Tests
Tests use mocked data and can be run without API access:
pytest test_download.py -v

