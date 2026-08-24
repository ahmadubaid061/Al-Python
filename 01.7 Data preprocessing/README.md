# Data Preprocessing Guide

A comprehensive collection of Jupyter notebooks covering essential data preprocessing techniques for machine learning.

---

## 📁 Notebooks Overview

| Notebook | Topic | Key Techniques Covered |
|----------|-------|------------------------|
| `01_1 Label_encoding.ipynb` | Label Encoding | Converting categorical labels to numeric values |
| `01_Encoding_Categorical_Vals.ipynb` | Categorical Encoding | One-Hot Encoding, Ordinal Encoding |
| `02_Feature_Scalling.ipynb` | Feature Scaling | Z-Score Scaling, Min-Max Scaling |
| `03_Standard_Scaler.ipynb` | Standard Scaler | Using `StandardScaler` from sklearn |
| `04_transformation_and_outliers_handling.ipynb` | Transformation & Outliers | Log Transform, Clipping, Winsorization |
| `05_TestTrainSplit.ipynb` | Train-Test Split | Splitting data for model evaluation |

---

## 📊 Datasets Included

| File | Description |
|------|-------------|
| `data.csv` | General dataset for train-test split |
| `insurance_dataset.csv` | Insurance data for encoding practice |
| `telecom_customer.csv` | Telecom customer data for scaling & transformation |

---

## 🚀 Getting Started

1. **Install dependencies:**
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

2. **Open any notebook:**
```bash
jupyter notebook <notebook_name>.ipynb
```

---

## 📚 What You'll Learn

### 1. Encoding Categorical Variables
- **Label Encoding** — Convert categories to integers
- **One-Hot Encoding** — Create binary columns for each category
- **Ordinal Encoding** — Encode ordered categories

### 2. Feature Scaling
- **Standardization (Z-Score)** — Center to mean=0, std=1
- **Min-Max Scaling (Normalization)** — Scale to [0, 1] range
- **StandardScaler** — Using scikit-learn's built-in scaler

### 3. Handling Skewness & Outliers
- **Log Transformation** — Fix right-skewed distributions
- **Clipping** — Cap extreme values
- **Winsorization** — Bring outliers to normal range

### 4. Train-Test Split
- Split data for model training and evaluation
- Avoid data leakage

---

## 📦 Requirements

```
Python 3.x
pandas
numpy
scikit-learn
matplotlib
seaborn
jupyter
```

---

## 📖 Quick Reference

| Problem | Solution |
|---------|----------|
| Categorical text data | Label/One-Hot/Ordinal Encoding |
| Features with different scales | StandardScaler / MinMaxScaler |
| Right-skewed data | Log Transform |
| Extreme outliers | Clipping / Winsorization |
| Need to evaluate model | Train-Test Split |