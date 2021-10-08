import pytest
import pandas as pd

import accidents as acc


def test_read_csv_file_returns_pandas_dataframe():
    """Test if the function returns a pandas dataframe."""
    df = acc.read_csv_file('accidents.csv')
    assert isinstance(df, pd.DataFrame)


def test_read_csv_file_raises_exception_if_file_does_not_exist():
    """Test if the function raises an exception if the file does not exist."""
    with pytest.raises(FileNotFoundError):
        acc.read_csv_file('accidents_does_not_exist.csv')


def test_filter_dataframe_returns_pandas_dataframe():
    """Test if the function returns a pandas dataframe."""
    df = acc.read_csv_file('accidents.csv')
    start_date = pd.to_datetime('01-07-2013', format='%d-%m-%Y')
    end_date = pd.to_datetime('01-07-2013', format='%d-%m-%Y')
    filtered_df = acc.filter_dataframe(df, start_date, end_date)
    assert isinstance(filtered_df, pd.DataFrame)


def test_filter_dataframe_returns_filtered_dataframe():
    """Test if the function returns a filtered dataframe."""
    df = acc.read_csv_file('accidents.csv')
    start_date = pd.to_datetime('01-07-2013', format='%d-%m-%Y')
    end_date = pd.to_datetime('01-07-2013', format='%d-%m-%Y')
    filtered_df = acc.filter_dataframe(df, start_date, end_date)
    # Check if the filtered dataframe contains the correct number of rows.
    # The original dataset has 41 rows for date 01-07-2013.
    assert filtered_df.shape[0] == 41

# TODO: This needs monkey patching
# def test_input_start_end_date():
#     """Test if input_start_end_date() returns pd.Timestamp objects."""
#     start_date, end_date = acc.input_start_end_date()
#     assert isinstance(start_date, pd.Timestamp)
#     assert isinstance(end_date, pd.Timestamp)
