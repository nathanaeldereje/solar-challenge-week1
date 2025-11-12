# tests/test_modules.py
import pandas as pd
from src.data_loader import load_csv
from src.preprocessing import clean_data, remove_outliers, add_time_features

def test_load_csv():
    df = load_csv("data/raw/sierraleone-bumbuna.csv")
    assert isinstance(df, pd.DataFrame)
    assert "Timestamp" in df.columns

def test_clean_data():
    df = load_csv("data/raw/sierraleone-bumbuna.csv")
    df_clean = clean_data(df)
    assert "Comments" not in df_clean.columns

def test_remove_outliers():
    df = load_csv("data/raw/sierraleone-bumbuna.csv")
    df_clean = clean_data(df)
    df_no_outliers = remove_outliers(df_clean, ["GHI","DNI"])
    assert len(df_no_outliers) <= len(df_clean)

def test_add_time_features():
    df = load_csv("data/raw/sierraleone-bumbuna.csv")
    df_clean = clean_data(df)
    df_time = add_time_features(df_clean)
    assert "DayOfWeek" in df_time.columns
    assert "Month" in df_time.columns
    assert "TimeOfDay" in df_time.columns
