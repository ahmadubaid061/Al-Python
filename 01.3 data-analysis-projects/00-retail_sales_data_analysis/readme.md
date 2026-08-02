# Retail Sales Data Analysis

A mini data analysis project exploring retail sales data using pandas, matplotlib, and seaborn.

## Files

- **`retail_sales.csv`** — the raw dataset (~1825 rows). Columns: `Date`, `Category`, `Sales`, `Quantity`, `Profit`, `Region`.
- **`retail_sales_analysis_project.ipynb`** — the Jupyter Notebook containing the full analysis.

## What the Notebook Does

1. **Data Cleaning**
   Loads the CSV, fixes fake null values (like the strings `"Null"`, `"NaN?"`), and fills missing values — categorical columns with the mode, numeric columns with the median.

2. **Data Preparation**
   Converts `Date` to a proper datetime type and extracts new columns from it: `Month`, `Quarter`, `MonthName`, and `DayofWeek`.

3. **Statistical Summary**
   Basic `.describe()` stats, plus grouped summaries (count, sum, mean, median, min, max) by `Category` and by `Region`.

4. **Trend & Performance Analysis**
   - Monthly sales and profit trends
   - Sales performance by product category
   - Sales distribution by region
   - Sales patterns by day of the week
   - Correlation between Sales, Profit, Quantity, and Month

5. **Visualizations**
   Line charts, bar charts, a pie chart, a correlation heatmap, and a combined 4-chart dashboard summarizing the analysis.

6. **Key Insights & Recommendations**
   The notebook wraps up by printing out the top-performing category, best region, best month, best day of the week, total sales/profit, overall profit margin, and category-wise profit margins — along with a few basic business recommendations based on the findings.

## How to Run

Make sure the required libraries are installed:

```bash
pip install pandas numpy matplotlib seaborn
```

Then open the notebook and run the cells in order:

```bash
jupyter notebook retail_sales_analysis_project.ipynb
```

Keep `retail_sales.csv` in the same folder as the notebook, since it's loaded using a relative path (`pd.read_csv("retail_sales.csv")`).
