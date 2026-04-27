# ============================================================
# LAB 09: Linear Regression — Insurance Dataset
# Upload insurance.csv to Colab, then run each cell below
# ============================================================

# ── TASK 1: Import Required Libraries ───────────────────────
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

print("All libraries imported successfully!")


# ── TASK 2: Load the Dataset ─────────────────────────────────
# After uploading insurance.csv to Colab via the Files panel:
df = pd.read_csv("insurance.csv")

print("Dataset loaded!")
print(df.head())          # Shows first 5 rows


# ── TASK 3: Understand the Dataset ───────────────────────────

# 3a — Shape: how many rows and columns?
print("\n--- Shape ---")
print(df.shape)
# You'll see something like (1338, 7)
# 1338 patients, 7 columns

# 3b — Data types of each column
print("\n--- Data Types ---")
print(df.dtypes)
# age, children → int
# bmi, charges  → float
# sex, smoker, region → object (text)

# 3c — Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())
# All should be 0 — this dataset has no missing values

# 3d — Statistical summary
print("\n--- Statistical Summary ---")
print(df.describe())
# Shows min, max, mean, std for numeric columns
# Example insight: average charge is ~$13,270


# ── TASK 4: Select Variable + Train Models ───────────────────

# --- Simple Linear Regression ---
# We choose BMI as our single independent variable.
# WHY BMI? Because higher BMI often means more health risks,
# leading to higher insurance charges. It's a continuous
# numerical variable with a visible linear trend with charges.

X_simple = df[['bmi']]      # Single input (must be 2D)
y = df['charges']           # Target variable (what we predict)

print("\nSimple LR — using: bmi to predict charges")

# --- Multiple Linear Regression ---
# We use ALL features: age, bmi, children, sex, smoker, region
# First we need to encode text columns into numbers

df_encoded = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], drop_first=True)
# pd.get_dummies converts:
#   sex     → sex_male (1=male, 0=female)
#   smoker  → smoker_yes (1=smoker, 0=non-smoker)
#   region  → region_northwest, region_southeast, region_southwest

X_multi = df_encoded.drop('charges', axis=1)  # All columns except charges
y_multi  = df_encoded['charges']

print("Multiple LR — using: all features")
print("Encoded columns:", list(X_multi.columns))


# ── TASK 5: Visualize the Relationship ───────────────────────

plt.figure(figsize=(8, 5))
plt.scatter(df['bmi'], df['charges'],
            color='steelblue', alpha=0.5, edgecolors='white', s=50)
plt.xlabel('BMI (Body Mass Index)')
plt.ylabel('Insurance Charges ($)')
plt.title('BMI vs Insurance Charges')
plt.tight_layout()
plt.savefig('scatter_bmi_charges.png', dpi=150)
plt.show()

# OBSERVATION: There's a positive trend — higher BMI tends
# to mean higher charges, though there's a lot of spread.
# This spread is partly because smoking status also matters a lot.
print("\n[Chart saved: scatter_bmi_charges.png]")


# ── TASK 6: Split the Data ───────────────────────────────────

# Simple LR split
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_simple, y, test_size=0.2, random_state=42
)

# Multiple LR split
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X_multi, y_multi, test_size=0.2, random_state=42
)

print(f"\nSimple LR  — Train: {len(X_train_s)}, Test: {len(X_test_s)}")
print(f"Multiple LR — Train: {len(X_train_m)}, Test: {len(X_test_m)}")

# WHY SPLIT?
# If we test on data the model was trained on, it's like giving
# the student the exam answers beforehand — not a fair test.
# We keep 20% hidden during training so we can honestly measure
# how well the model generalizes to NEW, unseen patients.


# ── TASK 7: Train the Model ───────────────────────────────────

# --- Simple Linear Regression model ---
model_simple = LinearRegression()
model_simple.fit(X_train_s, y_train_s)

slope     = model_simple.coef_[0]
intercept = model_simple.intercept_

print("\n--- Simple LR Coefficients ---")
print(f"Slope (BMI coefficient) : {slope:.4f}")
print(f"Intercept               : {intercept:.2f}")
print(f"Formula: charges = {slope:.2f} × BMI + {intercept:.2f}")
# Meaning: for every 1 unit increase in BMI,
# predicted charges increase by ~$slope

# --- Multiple Linear Regression model ---
model_multi = LinearRegression()
model_multi.fit(X_train_m, y_train_m)

print("\n--- Multiple LR Coefficients ---")
for feature, coef in zip(X_multi.columns, model_multi.coef_):
    print(f"  {feature:25s}: {coef:.2f}")
print(f"  {'Intercept':25s}: {model_multi.intercept_:.2f}")


# ── TASK 8: Evaluate Both Models ─────────────────────────────

# Simple LR predictions
y_pred_simple = model_simple.predict(X_test_s)
mae_s = mean_absolute_error(y_test_s, y_pred_simple)
r2_s  = r2_score(y_test_s, y_pred_simple)

# Multiple LR predictions
y_pred_multi = model_multi.predict(X_test_m)
mae_m = mean_absolute_error(y_test_m, y_pred_multi)
r2_m  = r2_score(y_test_m, y_pred_multi)

print("\n--- Model Comparison ---")
print(f"{'Metric':<30} {'Simple LR':>12} {'Multiple LR':>12}")
print("-" * 55)
print(f"{'MAE (Mean Absolute Error)':<30} ${mae_s:>11,.2f} ${mae_m:>11,.2f}")
print(f"{'R² Score':<30} {r2_s:>12.4f} {r2_m:>12.4f}")

# WHAT THESE MEAN:
# MAE = average dollar amount we're off by in predictions
# R²  = percentage of variation in charges explained by model
#       R²=1.0 is perfect, R²=0.0 means the model explains nothing
# Multiple LR should have much lower MAE and higher R²


# ── TASK 9: Plot the Regression Line ─────────────────────────

plt.figure(figsize=(8, 5))

# Actual data points
plt.scatter(X_test_s, y_test_s,
            color='steelblue', alpha=0.6,
            label='Actual charges', edgecolors='white', s=50)

# Regression line — sort X values so line is smooth
x_line = np.linspace(X_test_s['bmi'].min(), X_test_s['bmi'].max(), 100).reshape(-1, 1)
y_line = model_simple.predict(x_line)
plt.plot(x_line, y_line, color='crimson', linewidth=2.5,
         label=f'Regression line (y = {slope:.0f}x + {intercept:.0f})')

plt.xlabel('BMI')
plt.ylabel('Insurance Charges ($)')
plt.title('Simple Linear Regression: BMI vs Charges')
plt.legend()
plt.tight_layout()
plt.savefig('regression_line.png', dpi=150)
plt.show()
print("\n[Chart saved: regression_line.png]")


# ── TASK 10: Actual vs Predicted ─────────────────────────────

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Simple LR
axes[0].scatter(y_test_s, y_pred_simple,
                color='steelblue', alpha=0.6, edgecolors='white', s=50)
mn, mx = y_test_s.min(), y_test_s.max()
axes[0].plot([mn, mx], [mn, mx], 'r--', linewidth=1.5, label='Perfect prediction')
axes[0].set_xlabel('Actual Charges ($)')
axes[0].set_ylabel('Predicted Charges ($)')
axes[0].set_title(f'Simple LR — Actual vs Predicted\n(R² = {r2_s:.3f})')
axes[0].legend()

# Multiple LR
axes[1].scatter(y_test_m, y_pred_multi,
                color='darkorange', alpha=0.6, edgecolors='white', s=50)
mn2, mx2 = y_test_m.min(), y_test_m.max()
axes[1].plot([mn2, mx2], [mn2, mx2], 'r--', linewidth=1.5, label='Perfect prediction')
axes[1].set_xlabel('Actual Charges ($)')
axes[1].set_ylabel('Predicted Charges ($)')
axes[1].set_title(f'Multiple LR — Actual vs Predicted\n(R² = {r2_m:.3f})')
axes[1].legend()

plt.tight_layout()
plt.savefig('actual_vs_predicted.png', dpi=150)
plt.show()
print("\n[Chart saved: actual_vs_predicted.png]")

# INTERPRETATION:
# If dots cluster tightly around the red line → good model
# If dots are scattered widely → model struggles to predict accurately
# Multiple LR should look much tighter than Simple LR


# ── TASK 11: Predictions on New Data ─────────────────────────

# Simple LR — new BMI values
new_bmi = pd.DataFrame({'bmi': [18.5, 25.0, 30.0, 35.0, 40.0]})
pred_simple = model_simple.predict(new_bmi)

print("\n--- Simple LR: New Predictions (BMI → Charges) ---")
for bmi_val, charge in zip(new_bmi['bmi'], pred_simple):
    print(f"  BMI {bmi_val:.1f}  →  ${charge:,.2f}")

# Multiple LR — full hypothetical patient profile
new_patients = pd.DataFrame({
    'age':              [25,  45,  60],
    'bmi':              [22.0, 30.5, 38.0],
    'children':         [0,    2,    1],
    'sex_male':         [1,    0,    1],
    'smoker_yes':       [0,    0,    1],
    'region_northwest': [0,    1,    0],
    'region_southeast': [0,    0,    1],
    'region_southwest': [1,    0,    0],
})

# Make sure columns match training data
new_patients = new_patients.reindex(columns=X_multi.columns, fill_value=0)
pred_multi = model_multi.predict(new_patients)

print("\n--- Multiple LR: New Patient Predictions ---")
profiles = [
    "25yo male, BMI 22, non-smoker, SW",
    "45yo female, BMI 30.5, non-smoker, NW",
    "60yo male, BMI 38, smoker, SE",
]
for profile, charge in zip(profiles, pred_multi):
    print(f"  {profile:45s} → ${charge:,.2f}")


# ── TASK 12: Interpret the Results ───────────────────────────
print(f"""
=======================================================
INTERPRETATION (Task 12 — write this in markdown cells)
=======================================================

SIMPLE LINEAR REGRESSION (BMI only):
-------------------------------------
Slope = {slope:.2f}
→ For every 1-unit increase in BMI, insurance charges
  increase by approximately ${slope:.2f}.
→ Example: going from BMI 25 to BMI 35 (10 units)
  adds about ${slope*10:,.0f} to predicted charges.

R² = {r2_s:.4f} ({r2_s*100:.1f}%)
→ BMI alone explains only {r2_s*100:.1f}% of the variation
  in charges. This is a weak-to-moderate fit.
→ The remaining ~{(1-r2_s)*100:.0f}% is influenced by other
  factors like smoking, age, and region.

MAE = ${mae_s:,.2f}
→ On average, our BMI-only predictions are off by
  ${mae_s:,.2f}. Given charges range from ~$1,000 to
  ~$63,000, this is a large error — confirming BMI
  alone is not enough.

MULTIPLE LINEAR REGRESSION (all features):
-------------------------------------------
R² = {r2_m:.4f} ({r2_m*100:.1f}%)
→ Using all features explains {r2_m*100:.1f}% of variation.
  This is a much better fit than BMI alone.

MAE = ${mae_m:,.2f}
→ Average error drops to ${mae_m:,.2f} — significantly
  more accurate than Simple LR.

CONCLUSION:
→ The most important predictors are smoking status and age.
→ Simple LR with BMI gives a baseline but is insufficient.
→ Multiple LR with all features is the better model.
=======================================================
""")
