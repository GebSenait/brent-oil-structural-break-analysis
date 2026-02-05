# Project setup

## Python version

- **Recommended**: Python **3.10 or newer** (3.14 is fine).  
- The notebook `notebooks/task1_ingest_clean_diagnose.ipynb` and `notebooks/run_diagnostics.py` use standard libraries plus `requirements.txt` dependencies.

## Virtual environment

From the repo root:

```powershell
# Create venv
python -m venv .venv

# Activate (PowerShell)
.\.venv\Scripts\Activate.ps1

# Or on Cmd
.\.venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
```

If PowerShell blocks running scripts, run once: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.

## Verify installation

With the venv activated:

```powershell
python --version
pip list
```

You should see `pandas`, `numpy`, `scipy`, `statsmodels`, `matplotlib`, `seaborn` and their version numbers (e.g. pandas>=2.0, numpy>=1.24, etc.).

Quick test:

```powershell
python -c "import pandas, numpy, scipy, statsmodels, matplotlib, seaborn; print('OK')"
```

## Running the Task-1 notebook

1. Activate the virtual environment (see above).
2. In Cursor/VS Code: open `notebooks/task1_ingest_clean_diagnose.ipynb`, then choose the kernel that points to `.venv` (e.g. **Python 3.x.x ('.venv': venv)**).
3. Run all cells. The notebook will write `docs/task-1/DIAGNOSTIC-RESULTS.md` and figures under `docs/task-1/`.

Alternatively, from repo root with venv activated:

```powershell
pip install jupyter
jupyter notebook notebooks\task1_ingest_clean_diagnose.ipynb
```

Select the kernel that uses `.venv` if prompted.

## Troubleshooting

- **"The process cannot access the file because it is being used"**: Close other Python processes, Jupyter, or IDEs that might be using the venv, then run `pip install -r requirements.txt` again from the activated venv.
- **ExecutionPolicy** (PowerShell): If `.ps1` scripts are blocked, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once.
- **Kernel not found**: In Cursor/VS Code, choose "Select Kernel" and pick the interpreter at `.venv\Scripts\python.exe`.
