import pandas as pd

def load_clean_csv(path: str, parse_dates=None) -> pd.DataFrame:
    """Load cleaned CSV and return a DataFrame."""
    return pd.read_csv(path, parse_dates=parse_dates)
