"""
Data Loader Module
Handles loading of raw and processed CSV files.
"""

import pandas as pd

def load_clean_csv(path: str, parse_dates=None) -> pd.DataFrame:
    """Load cleaned CSV and return a DataFrame."""
    return pd.read_csv(path, parse_dates=parse_dates)

def load_csv(path: str, parse_dates=None) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        path (str): Path to CSV file
        parse_dates (list[str], optional): Columns to parse as dates

    Returns:
        pd.DataFrame: Loaded data
    """
    df = pd.read_csv(path, parse_dates=parse_dates)
    return df
