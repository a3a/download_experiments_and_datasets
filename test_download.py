import os
import pandas as pd
import pytest
from unittest.mock import patch

# Import your script (assumes it's in the same directory or in PYTHONPATH)
import download_experiments_and_datasets as ded

@pytest.fixture(scope="function")
def setup_output_dir():
    """Ensure base output directory exists before test (no cleanup after)."""
    os.makedirs("output", exist_ok=True)
    yield

@patch("download_experiments_and_datasets.get_data")
def test_download_all(mock_get_data, setup_output_dir):
    """
    Test that experiments and datasets are downloaded into separate CSV files.
    Mocked data is used to avoid real API calls.
    """
    # Define mock experiments
    exp1_data = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    exp2_data = [{"a": 5, "b": 6}]
    mock_experiments = [
        {"id": 1, "data": exp1_data},
        {"id": 2, "data": exp2_data}
    ]

    # Define mock datasets
    ds100_data = [{"x": "foo", "y": "bar"}]
    ds200_data = [{"x": "baz", "y": "qux"}, {"x": "quux", "y": "corge"}]
    mock_datasets = [
        {"id": 100, "data": ds100_data},
        {"id": 200, "data": ds200_data}
    ]

    # The mocked get_data() will return experiments first, then datasets
    mock_get_data.side_effect = [mock_experiments, mock_datasets]

    # Run the script with a known project ID
    test_project_id = "testproject"
    ded.main(project_id=test_project_id)

    # Resolve the expected output directory path
    matching_dirs = [d for d in os.listdir("output") if d.startswith(test_project_id)]
    assert len(matching_dirs) == 1, "Expected exactly one output directory"
    output_path = os.path.join("output", matching_dirs[0])
    print("Output dir:", output_path)

    # Define helper to verify CSV file contents
    def assert_csv(filename, expected_data):
        filepath = os.path.join(output_path, filename)
        assert os.path.exists(filepath), f"Missing file: {filename}"
        actual_df = pd.read_csv(filepath)
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(actual_df, expected_df)

    # Verify all expected files exist and match data
    assert_csv("experiment_1.csv", exp1_data)
    assert_csv("experiment_2.csv", exp2_data)
    assert_csv("dataset_100.csv", ds100_data)
    assert_csv("dataset_200.csv", ds200_data)
