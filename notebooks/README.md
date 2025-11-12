

## 📓 Updated `notebooks/README.md`

This version now reflects that the notebooks comparison work:

```markdown
# 📘 Notebooks

This folder contains Jupyter notebooks for data profiling, cleaning, and exploratory analysis
of solar datasets for multiple countries.

## Structure

| Notebook | Description |
|-----------|--------------|
| `benin_eda.ipynb` | Profiling, cleaning, and exploratory analysis for Benin |
| `sierra_leone_eda.ipynb` | Profiling and EDA for Sierra Leone |
| `togo_eda.ipynb` | Profiling and EDA for Togo |
| `compare_countries.ipynb` | Cross-country comparison and statistical analysis |

## Purpose

Each notebook:
- Loads country-specific cleaned data (`data/<country>_clean.csv`)
- Conducts EDA (summary stats, outlier detection, visualizations)
- Produces comparative metrics and plots
- Documents insights and conclusions

> ⚠️ Note: CSV data files are excluded from Git (`data/` folder is in `.gitignore`).
