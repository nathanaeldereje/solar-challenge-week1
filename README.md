# 🌞 Solar Challenge - Week 1: Cross-Country Comparison

This branch (`compare-countries`) focuses on **Task 3: Cross-Country Comparison**, where we synthesize and analyze cleaned solar datasets from **Benin**, **Sierra Leone**, and **Togo**. The goal is to identify relative solar potential, assess statistical differences, and summarize actionable insights for regional ranking.

---

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Project Overview](#-project-overview)
- [Continuous Integration](#-continuous-integration)

---

## 🚀 Quick Start

### 1. Clone the repository

\`\`\`bash
git clone https://github.com/<USER>/solar-challenge-week1.git
cd solar-challenge-week1
\`\`\`

### 2. Create a virtual environment

\`\`\`bash
# Windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
\`\`\`

### 3. Install dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

## 🧩 Project Structure



solar-challenge-week1/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── eda_utils.py
│   └── compare_utils.py
├── notebooks/
│   └── compare_countries.ipynb
├── tests/
│   ├── __init__.py
│   └── test_compare_utils.py
├── requirements.txt
├── .gitignore
└── README.md



---

## 📊 Project Overview

### Notebook: `compare_countries.ipynb`

The main analysis notebook contains:

- **Data Loading**: Cleaned CSVs from `data/benin_clean.csv`, `data/sierra_leone_clean.csv`, and `data/togo_clean.csv`
- **Exploratory Analysis**: Side-by-side boxplots for GHI, DNI, and DHI
- **Summary Statistics**: Mean, median, and standard deviation comparisons
- **Statistical Tests**: One-way ANOVA and Kruskal–Wallis tests on GHI
- **Insights & Rankings**: Observations and comparative rankings of solar potential

### Key Outputs

- **Summary Table**: Comparative metrics for solar radiation across countries
- **Statistical Test Results**: P-values for GHI comparisons between regions
- **Visual Insights**: Boxplots, bar charts, and solar potential rankings

---

### `.github/workflows/ci.yml`
```yaml
name: CI

on:
  push:
    branches: [ main, setup-task ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      - name: Check Python version
        run: python --version
      - name: Run tests
        run: |
          if [ -d tests ]; then pytest -q || true; fi
.vscode/settings.json
json
Copy code
{
  "python.pythonPath": ".venv/bin/python",
  "python.formatting.provider": "black",
  "editor.formatOnSave": true
}

# Togo Solar Data EDA – MoonLight Energy Solutions

## Project Overview
This project explores and cleans the Benin solar dataset (Malanville station) to identify trends, anomalies, and insights that can help optimize solar energy solutions.

**Objective:** Profile, clean, and explore the solar dataset to prepare for downstream analysis and modeling.

---

## Completed Tasks
1. **Data Loading**
   - Load CSV dataset into pandas DataFrame
   - Parse timestamps

2. **Data Cleaning**
   - Checked for missing values and dropped columns with all nulls (`Comments`)
   - Identified and removed outliers using Z-score

3. **Feature Engineering**
   - Added `DayOfWeek`, `Month`, `Year`, `Hour`, `TimeOfDay`
   - Created aggregated features for analysis (e.g., pre/post cleaning averages)

4. **Exploratory Data Analysis**
   - Timeseries line plots (`GHI`, `DNI`, `DHI`, `Tamb`)
   - Bar plots by DayOfWeek, Month, Year, and TimeOfDay
   - Correlation analysis & heatmaps
   - Scatter plots of `GHI` vs `WS`, `WSgust`, `WD`
   - Cleaning impact analysis (`ModA`/`ModB`)
   - Wind rose visualization for wind speed & direction
   - Bubble chart: `GHI` vs `Tamb` colored by `RH`

5. **Interim Insights**
   - High correlation between `TModA` and `TModB` (redundant sensors)
   - Strong correlation between `GHI`, `DNI`, `DHI` and module temperatures
   - Cleaning slightly improves module readings

---

## Next Steps
- Implement predictive models for solar output
- Automate data cleaning & feature engineering
- Expand visualization dashboards
- Add unit tests for all modules
- Integrate with CI/CD pipeline for automated EDA

---

## Environment Setup
- Python >= 3.10
- Required packages: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `windrose`
- Install via: `pip install -r requirements.txt`

---

## File Overview
| File | Description |
|------|-------------|
| `src/data_loader.py` | Load CSV and basic validation |
| `src/preprocessing.py` | Cleaning, outlier removal, feature engineering |
| `src/visualization.py` | All plotting functions (line, bar, scatter, heatmap, windrose, bubble) |
| `notebooks/benin_eda.ipynb` | Notebook calling the modules for interim analysis |
| `tests/test_modules.py` | Unit tests for modules |
| `data/raw/benin-malanville.csv` | Raw dataset (ignored in git) |
| `data/processed/benin_clean.csv` | Cleaned dataset (ignored in git) |
