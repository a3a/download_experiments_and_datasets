import os
import shutil
import pytest
import pandas as pd
from unittest.mock import patch, MagicMock

# Import functions from the script under test
import download_experiments_and_datasets as ded

@pytest.fixture(scope="function")
def temp_output_dir(tmp_path):
    # Patch the OUTPUT_DIRECTORY to a temporary path
    original_output_dir = ded.OUTPUT_DIRECTORY
    ded.OUTPUT_DIRECTORY = str(tmp_path)
    yield tmp_path
    ded.OUTPUT_DIRECTORY = original_output_dir

@patch("download_experiments_and_datasets.get_data")
def test_download_experiments_and_datasets(mock_get_data, temp_output_dir):
    # Prepare mock experiments and datasets
    mock_experiments = [
        {"id": 1, "data": [{"a": 1, "b": 2}, {"a": 3, "b": 4}]},
        {"id": 2, "data": [{"a": 5, "b": 6}]}
    ]
    mock_datasets = [
        {"id": 100, "data": [{"x": "foo", "y": "bar"}]},
        {"id": 200, "data": [{"x": "baz", "y": "qux"}, {"x": "quux", "y": "corge"}]}
    ]

    # The order of get_data calls: experiments endpoint, then datasets endpoint
    mock_get_data.side_effect = [mock_experiments, mock_datasets]

    # Call main (which will use the mocked get_data)
    ded.main()

    # Check that experiment CSVs were created
    exp1_path = os.path.join(ded.OUTPUT_DIRECTORY, "experiment_1.csv")
    exp2_path = os.path.join(ded.OUTPUT_DIRECTORY, "experiment_2.csv")
    assert os.path.exists(exp1_path)
    assert os.path.exists(exp2_path)
    df1 = pd.read_csv(exp1_path)
    df2 = pd.read_csv(exp2_path)
    pd.testing.assert_frame_equal(
        df1, pd.DataFrame(mock_experiments[0]["data"])
    )
    pd.testing.assert_frame_equal(
        df2, pd.DataFrame(mock_experiments[1]["data"])
    )

    # Check that dataset CSVs were created
    ds1_path = os.path.join(ded.OUTPUT_DIRECTORY, "dataset_100.csv")
    ds2_path = os.path.join(ded.OUTPUT_DIRECTORY, "dataset_200.csv")
    assert os.path.exists(ds1_path)
    assert os.path.exists(ds2_path)
    df_ds1 = pd.read_csv(ds1_path)
    df_ds2 = pd.read_csv(ds2_path)
    pd.testing.assert_frame_equal(
        df_ds1, pd.DataFrame(mock_datasets[0]["data"])
    )
    pd.testing.assert_frame_equal(
        df_ds2, pd.DataFrame(mock_datasets[1]["data"])
    )
