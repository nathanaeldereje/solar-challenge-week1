# tests/test_compare.py
import pytest
import pandas as pd
from src.data_loader import load_clean_csv
from src.analysis import summary_table, anova_test, kruskal_test


@pytest.fixture(scope="module")
def sample_data():
    """Load all cleaned datasets once for reuse."""
    ben = load_clean_csv("data/benin_clean.csv")
    tog = load_clean_csv("data/togo_clean.csv")
    sl = load_clean_csv("data/sierraleone_clean.csv")

    df = pd.concat([
        ben.assign(country='Benin'),
        tog.assign(country='Togo'),
        sl.assign(country='SierraLeone')
    ], ignore_index=True)

    return ben, tog, sl, df


def test_load_clean_csv(sample_data):
    """Ensure all CSVs load correctly."""
    ben, tog, sl, _ = sample_data
    assert isinstance(ben, pd.DataFrame)
    assert isinstance(tog, pd.DataFrame)
    assert isinstance(sl, pd.DataFrame)
    assert not ben.empty and not tog.empty and not sl.empty


def test_summary_table(sample_data):
    """Ensure summary table returns expected structure."""
    _, _, _, df = sample_data
    tbl = summary_table(df, group_col='country', metrics=['GHI'])
    assert isinstance(tbl, pd.DataFrame)
    assert 'country' in tbl.columns
    # Adjusted to match your output naming convention
    assert any(col.startswith('GHI_') for col in tbl.columns)


def test_statistical_tests(sample_data):
    """Run smoke tests for ANOVA and Kruskal-Wallis."""
    _, _, _, df = sample_data
    res_a = anova_test(df, 'country', 'GHI')
    res_k = kruskal_test(df, 'country', 'GHI')

    # Acceptable output types
    if isinstance(res_a, dict):
        assert 'p' in res_a or 'pvalue' in res_a
        assert 0 <= res_a.get('p', res_a.get('pvalue')) <= 1
    else:
        assert isinstance(res_a, (float, int))
        assert 0 <= res_a <= 1

    if isinstance(res_k, dict):
        assert 'p' in res_k or 'pvalue' in res_k
        assert 0 <= res_k.get('p', res_k.get('pvalue')) <= 1
    else:
        assert isinstance(res_k, (float, int))
        assert 0 <= res_k <= 1
