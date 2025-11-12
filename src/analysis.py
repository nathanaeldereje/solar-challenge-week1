"""
Analysis utilities for cross-country comparison.
"""

import pandas as pd
import numpy as np
from scipy import stats

def summary_table(df: pd.DataFrame, group_col: str, metrics: list):
    """
    Produce a summary table (mean, median, std) grouped by group_col for metrics.
    Returns a DataFrame with MultiIndex (group, metric) or a tidy DataFrame.
    """
    agg_funcs = {m: ['mean', 'median', 'std'] for m in metrics}
    summary = df.groupby(group_col)[metrics].agg(agg_funcs)
    # flatten columns
    summary.columns = ['_'.join(col).strip() for col in summary.columns.values]
    return summary.reset_index()

def anova_test(df: pd.DataFrame, group_col: str, value_col: str):
    """
    Run one-way ANOVA on value_col across groups defined in group_col.
    Returns (F_statistic, p_value) and group samples dict.
    """
    groups = [g[value_col].dropna().values for _, g in df.groupby(group_col)]
    if any(len(g)==0 for g in groups):
        raise ValueError("One or more groups are empty.")
    F, p = stats.f_oneway(*groups)
    return {'F': float(F), 'p': float(p)}

def kruskal_test(df: pd.DataFrame, group_col: str, value_col: str):
    """
    Run Kruskal-Wallis H-test (nonparametric alternative) across groups.
    Returns (H_statistic, p_value).
    """
    groups = [g[value_col].dropna().values for _, g in df.groupby(group_col)]
    H, p = stats.kruskal(*groups)
    return {'H': float(H), 'p': float(p)}

def cleaning_impact(df, module_cols=["ModA","ModB"], cleaning_col="Cleaning"):
    """Calculate average module readings pre/post cleaning."""
    return df.groupby(cleaning_col)[module_cols].mean()
