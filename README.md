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
