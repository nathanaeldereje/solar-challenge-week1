"""
Analysis Module
Handles correlation analysis and cleaning impact.
"""

import pandas as pd

def cleaning_impact(df, module_cols=["ModA","ModB"], cleaning_col="Cleaning"):
    """Calculate average module readings pre/post cleaning."""
    return df.groupby(cleaning_col)[module_cols].mean()
