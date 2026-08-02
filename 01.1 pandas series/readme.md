# Pandas Series & DataFrames

Basics of pandas — Series, DataFrames, indexing, and importing/exporting data files.

## Files

**`01 pandas.py`**
Introduces `pd.Series` — a labeled 1D array, like a single column of an Excel sheet. Shows how to create one with custom labels, and how to view its `.values`, `.index`, and `.value_counts()`.

**`02 complexDataInPandas.py`**
Introduces `pd.DataFrame` — a table made of multiple labeled columns (like a full spreadsheet), built here from a Python dictionary. Covers common DataFrame inspection methods: `.shape`, `.dtypes`, `.info()`, `.head()`, `.describe()`, `.isnull()`, and `.isna().sum()`.

**`03 indexingAndSelecting.py`**
Covers selecting data from a DataFrame:

- Selecting a single column or multiple columns
- `.loc[]` — label/position-based row selection (and combined with column selection)
- `.iloc[]` — purely integer-position-based row/column selection
- Exporting a DataFrame to CSV with `.to_csv()`

**`importingAndExportingFiles.py`**
Shows how to read an external CSV file into a DataFrame with `pd.read_csv()` instead of typing data manually, and briefly touches on inspecting its columns.

## Data Files

These are sample datasets used across the scripts above:

- **`students_data.csv`** — columns: `Student_ID`, `Student_Name`, `Degree`, `Age`
- **`employees_data.xlsx`** — columns: `Employee_ID`, `Employee_Name`, `Age`, `Salary`
- **`teachers_data.json`** — a list of teacher records with `Teacher_ID`, `Teacher_Name`, `Subject_ID`, `Subject_Name`, `Email`

## Key Concepts

- A **Series** is one labeled column; a **DataFrame** is a table of multiple Series (columns) sharing the same row index.
- `.loc[]` selects by label, `.iloc[]` selects by integer position — both work on rows and columns.
- pandas can read/write multiple file formats: `pd.read_csv()`, `pd.read_excel()`, `pd.read_json()`, and their `.to_csv()` / `.to_excel()` / `.to_json()` counterparts.

## How to Run

```bash
pip install pandas openpyxl
python "01 pandas.py"
```

Each file can be run independently. For `importingAndExportingFiles.py`, update the file path to point to `students_data.csv` in your own folder before running.
