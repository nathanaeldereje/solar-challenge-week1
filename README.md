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

\`\`\`

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

\`\`\`

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

## 🧪 Continuous Integration

This project uses **GitHub Actions** to automatically run tests and ensure environment consistency.

- **Workflow file**: `.github/workflows/unittests.yml`
- Tests run on every push to validate data processing and analysis utilities

---
