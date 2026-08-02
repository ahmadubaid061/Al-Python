# Loan Risk Analysis

A mini data analysis project exploring loan data to understand default risk, using pandas, seaborn, and matplotlib.

## Files

- **`loan_data.csv`** — the raw dataset (~1000 rows). Columns: `loan_id`, `age`, `income`, `loan_amount`, `credit_score`, `default`.
- **`Loan_data_analysis.ipynb`** — the Jupyter Notebook containing the full analysis.

## What the Notebook Does

1. **Data Loading & Cleaning**
   Loads the CSV and fills missing `income` values with the median.

2. **Statistical Summary**
   Uses `.describe()` to get a quick overview of the numerical columns.

3. **Correlation Analysis**
   A heatmap showing how `age`, `income`, `loan_amount`, `credit_score`, and `default` relate to each other.

4. **Outlier Detection & Handling**
   - A boxplot of `loan_amount` to visually spot outliers.
   - Outliers are then handled by **clipping**: values below the 5th percentile and above the 95th percentile are capped, creating a new `loan_amount_cleaned` column.
   - A second boxplot confirms the outliers are reduced.

5. **Feature Engineering**
   - `dti_ratio` (debt-to-income ratio) — calculated as `loan_amount_cleaned / income`.
   - `risk_category` — buckets each loan into `High Risk`, `Fair`, `Good`, or `Excellent` based on `credit_score` ranges (using `pd.cut`).

6. **Risk Insight**
   Groups the data by `risk_category` and calculates the **default rate (%)** for each group — showing whether riskier credit categories actually default more often.

## Key Concepts Used

- Handling missing values with `.fillna()`
- Outlier detection with boxplots and handling with `.clip()` (percentile-based capping)
- Feature engineering: creating a ratio feature (`dti_ratio`) and a binned categorical feature (`risk_category`) with `pd.cut()`
- Grouped aggregation with `.groupby()` to connect a feature back to the outcome (`default`)

## How to Run

Make sure the required libraries are installed:

```bash
pip install pandas seaborn matplotlib
```

Then open the notebook and run the cells in order:

```bash
jupyter notebook Loan_data_analysis.ipynb
```

Keep `loan_data.csv` in the same folder as the notebook, since it's loaded using a relative path (`pd.read_csv("loan_data.csv")`).
