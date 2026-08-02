# Data Analysis Projects

A collection of small, self-contained data analysis mini-projects using pandas, matplotlib, and seaborn. Each subfolder has its own README with more detail.

## Projects

**`00-retail_sales_data_analysis/`**
Analyzes a retail sales dataset — cleaning, monthly/category/regional trends, correlation analysis, a 4-chart dashboard, and business insights based on the findings.

**`01-Loan-Risk-analysis/`**
Analyzes a loan dataset to explore default risk — cleaning, outlier handling, feature engineering (debt-to-income ratio, risk category), and default rate by risk category.

## How to Explore

Go into each subfolder, read its `README.md`, then open the notebook:

```bash
cd 00-retail_sales_data_analysis
jupyter notebook retail_sales_analysis_project.ipynb
```

```bash
cd 01-Loan-Risk-analysis
jupyter notebook Loan_data_analysis.ipynb
```

Each project's CSV file must stay in the same folder as its notebook, since the data is loaded with a relative path.

## Requirements

```bash
pip install pandas numpy matplotlib seaborn jupyter
```
