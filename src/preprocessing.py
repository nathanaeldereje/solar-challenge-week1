"""
Preprocessing Module
Handles data cleaning, feature engineering, and outlier removal.
"""
import pandas as pd
import numpy as np
from scipy.stats import zscore

def drop_columns(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    """Drop unwanted columns from dataframe."""
    return df.drop(cols, axis=1)

def remove_outliers(df: pd.DataFrame, cols: list, z_thresh: float = 3.0) -> pd.DataFrame:
    """Remove rows with outliers using Z-score method."""
    z_scores = np.abs(df[cols].apply(zscore, nan_policy='omit'))
    mask = (z_scores > z_thresh).any(axis=1)
    return df[~mask]

def add_time_features(df: pd.DataFrame, time_col="Timestamp") -> pd.DataFrame:
    """Add Hour, DayOfWeek, Month, Year, and TimeOfDay features."""
    df = df.copy()
    df["Hour"] = df[time_col].dt.hour
    df["DayOfWeek"] = df[time_col].dt.day_name()
    df["Month"] = df[time_col].dt.month_name()
    df["Year"] = df[time_col].dt.year

    def get_time_of_day(hour):
        if 5 <= hour < 12:
            return "Morning"
        elif 12 <= hour < 17:
            return "Afternoon"
        elif 17 <= hour < 21:
            return "Evening"
        else:
            return "Night"

    df["TimeOfDay"] = df["Hour"].apply(get_time_of_day)
    return df
