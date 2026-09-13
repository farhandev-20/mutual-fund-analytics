Bluestock Mutual Fund Analytics Capstone

Project Overview

This project analyzes mutual fund data to build an end-to-end analytics pipeline covering data ingestion, cleaning, SQLite storage, exploratory analysis, performance and risk analytics, advanced analytics, and an interactive Power BI dashboard.

Objectives

Build a reusable ETL pipeline for mutual fund CSV datasets.

Clean and validate raw data while preserving meaningful missing values.

Store structured data in SQLite with relational integrity.

Analyze fund returns, volatility, drawdown, VaR, beta and Sharpe ratio.

Perform investor cohort retention analysis.

Build a rule-based mutual fund recommendation model.

Deliver an interactive Power BI dashboard.

Project Structure

bluestock_mf_capstone/
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── compute_metrics.py
│   └── recommender.py
├── sql/
│   ├── schema.sql
│   └── queries.sql
├── dashboard/
│   └── bluestock_mf.pbix
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
└── README.md

Data Processing

The ETL pipeline reads CSV files from data/raw, removes completely empty rows/columns and exact duplicates, standardizes column names and text whitespace, and writes cleaned datasets to data/processed.

Database

SQLite is used for structured storage. The schema contains fund master, NAV history, AUM, SIP inflows, category inflows, folio counts, scheme performance, portfolio holdings, investor transactions and benchmark index data. Foreign-key relationships are defined against the fund master.

Analytics

Key analytics include:

1Y, 3Y and 5Y return analysis

CAGR using actual elapsed years

Annualized volatility

Maximum drawdown

Historical 95% daily VaR

Beta against a benchmark index

Sharpe ratio

Fund-house and category analysis

SIP inflow trends

Investor cohort retention

Rule-based fund recommendation ranking

Recommendation Method

The recommendation score uses rank-based components:

3-year return: 30%

Sharpe ratio: 25%

Volatility: 20%

Maximum drawdown: 15%

Expense ratio: 10%

For volatility, drawdown and expense ratio, lower values are preferred. Drawdown is evaluated using the absolute magnitude of the negative drawdown.

Power BI Dashboard

The dashboard contains four pages:

Executive Overview

Fund Performance & Risk

Investor & SIP Analytics

Advanced Analytics

Interactive slicers are included on the dashboard pages to allow filtering by relevant fund and investor dimensions.

Data Quality

Validation covered missing values, duplicate records, numeric ranges, date fields and AMFI-code consistency. The SIP dataset contains missing yoy_growth_pct values that are retained as meaningful missing observations rather than being blindly imputed.

Tools & Technologies

Python

Pandas

NumPy

Matplotlib / Seaborn

SQLite

SQL

Jupyter Notebook

Power BI

Git / GitHub

Notes

The SQLite database file should remain local and should not be committed to GitHub. The project uses dynamic paths rather than hard-coded machine-specific paths.
