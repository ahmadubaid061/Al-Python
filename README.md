# AI Lab Tasks (Weekly)

This repository contains my weekly lab assignments for the Artificial Intelligence course.  
Each week's folder includes:

- **Problem statement** (PDF)  
- **Report** (DOCX)  
- **Jupyter notebook** (IPYNB) originally created in Google Colab  

The notebooks are ready to run in Google Colab, but you can also execute them locally on your own machine. This guide will walk you through running the notebooks in **Visual Studio Code**.

---

## Repository Structure

```
.
├── Week01/
│   ├── statement.pdf
│   ├── report.docx
│   └── notebook.ipynb
├── Week02/
│   ├── statement.pdf
│   ├── report.docx
│   └── notebook.ipynb
├── Week03/
│   ├── statement.pdf
│   ├── report.docx
│   └── notebook.ipynb
└── ...
```

---

## How to Run the Notebooks Locally in VS Code

### Prerequisites

- [Python](https://www.python.org/downloads/) (version 3.7 or later) installed.
- [Visual Studio Code](https://code.visualstudio.com/download) installed.
- [Jupyter extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) – install it from the Extensions view (`Ctrl+Shift+X`).

### Step 1: Get the Repository

Clone the repository using Git:

```bash
git clone https://github.com/ahmadubaid061/Al-Python
```

Alternatively, you can download the ZIP archive from GitHub and extract it.

### Step 2: Open the Repository in VS Code

Launch VS Code and open the cloned/extracted folder:  
`File > Open Folder...` → select the repository folder.

### Step 3: Set Up a Python Virtual Environment (Recommended)

Open a terminal in VS Code (`Terminal > New Terminal`) and create a virtual environment:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` appear in your terminal prompt, indicating the environment is active.

### Step 4: Install Required Packages

Each notebook may depend on libraries like `numpy`, `pandas`, `matplotlib`, `scikit-learn`, etc.  
Check the first few code cells of a notebook for `import` statements, then install them with pip:

```bash
pip install numpy pandas matplotlib scikit-learn
```

If a `requirements.txt` file exists in the repository, you can install all dependencies at once:

```bash
pip install -r requirements.txt
```

### Step 5: Open and Run a Notebook

- In VS Code, navigate to a weekly folder (e.g., `Week01`) and click on the `.ipynb` file.  
- The notebook will open in the built‑in Jupyter editor.  
- At the top‑right corner, click on the kernel picker (it may show “Python 3...” or “Select Kernel”). Choose the interpreter that corresponds to your virtual environment (it often contains `./venv` in the path).  
- Now you can run cells using the **play** button next to each cell or by pressing `Shift+Enter`.

---

## Additional Tips

- **Data files:** If a notebook reads external data (e.g., CSV, images), make sure those files are in the same folder as the notebook (or adjust the file paths accordingly).  
- **Colab‑specific syntax:** Some notebooks may contain `!pip install` or `!wget` commands. These will also work in a local Jupyter environment because `!` runs shell commands – but be aware that they install packages system‑wide unless you are inside a virtual environment.  
- **Running in Colab directly:** You can always upload the `.ipynb` file to [Google Colab](https://colab.research.google.com/) and run it there without any local setup.

---
