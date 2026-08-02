# Data and Data Libraries

Basics of the core Python libraries used for data analysis: NumPy, and an intro to scikit-learn/matplotlib/seaborn.

## Files

**`00 pandas and numpy.py`**
Explains the difference between NumPy (fast numerical arrays, all one data type) and pandas (labeled, tabular data — mixed types, like a spreadsheet). Also creates a basic 2D NumPy array and checks its `shape`, `ndim`, and `dtype`. Ends with a speed comparison: adding 5 to a million numbers using NumPy vs. a plain Python loop, to show why NumPy is much faster for numerical operations.

**`001 creating arrays with numpy.py`**
Different ways to create NumPy arrays:

- `np.array()` — 1D and 2D arrays from lists
- `np.zeros()` — array filled with zeros
- `np.full()` — array filled with a specific value
- `np.arange()` — array from a range with a step size
- `np.linspace()` — array of evenly spaced values between two numbers
- `np.eye()` — identity matrix
- Creating arrays with a specific `dtype`, and converting dtypes with `.astype()`

**`002 indexing and slicing numpy arrays.py`**
How to access elements in a 2D NumPy array:

- Indexing with `array[row, col]`
- Slicing with `array[row_start:row_end, col_start:col_end]`
- Step slicing (e.g. every 2nd row/column)

**`003 random number generator in numpy.py`**
Uses `np.random.default_rng()` to generate random numbers — simulates 100 coin flips (0s and 1s) and estimates the probability of getting heads using `np.mean()`.

**`01 sklearn and matplotlib.py`**
Just short notes (no code yet) introducing:

- **scikit-learn** — the standard library for classical machine learning (building predictive models).
- **matplotlib** — used for data visualization (graphs, charts).
- **seaborn** — built on top of matplotlib, geared toward statistical data visualization.

## Key Concepts

- NumPy arrays are much faster than plain Python loops for numerical operations, because operations run in optimized, compiled code instead of Python's interpreter loop.
- NumPy arrays require all elements to be the same data type, unlike Python lists.
- Indexing/slicing in NumPy works with `[row, column]` pairs for 2D arrays, similar to Python list slicing but extended to multiple dimensions.

## How to Run

```bash
pip install numpy
python "00 pandas and numpy.py"
```

Each file can be run independently.
