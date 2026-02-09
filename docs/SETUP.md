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

You should see `pandas`, `numpy`, `scipy`, `statsmodels`, `matplotlib`, `seaborn`, `pymc`, `arviz`, `flask`, and (for notebooks) `jupyter`, `ipykernel`.

**Quick test (Task-1 + Task-2):**

```powershell
python -c "import pandas, numpy, scipy, statsmodels, matplotlib, seaborn, pymc, arviz; print('OK')"
```

**Full check before running Task-2 notebook:**

```powershell
python scripts/verify_task2_env.py
```

If that script reports all packages present, you can run `notebooks/task-2-change-point-analysis.ipynb`.

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

## Running the Task-2 notebook

1. **Ensure the venv has all packages** (from repo root):

   ```powershell
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python scripts/verify_task2_env.py
   ```

2. **Register the venv as a Jupyter kernel** (optional but recommended, so the notebook uses this env):

   ```powershell
   python -m ipykernel install --user --name=brent-task2 --display-name "Python (brent-task2)"
   ```

3. **Open the notebook** in Cursor/VS Code: `notebooks/task-2-change-point-analysis.ipynb`.  
   Use **Select Kernel** → choose **Python (brent-task2)** or **.venv (venv)**.

4. **Run All**. The notebook will run MCMC (a few minutes), then write `data/processed/change_point_posterior.json` and figures under `docs/task-2/`.

If you prefer not to activate (e.g. activation fails), install into the venv and run the notebook using the venv interpreter:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --user --name=brent-task2 --display-name "Python (brent-task2)"
```

Then in the IDE, select the **brent-task2** kernel for the notebook.

## Troubleshooting

- **"The process cannot access the file because it is being used"**: Close other Python processes, Jupyter, or IDEs that might be using the venv, then run `pip install -r requirements.txt` again from the activated venv.
- **ExecutionPolicy** (PowerShell): If `.ps1` scripts are blocked, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once.
- **Kernel not found**: In Cursor/VS Code, choose "Select Kernel" and pick the interpreter at `.venv\Scripts\python.exe`.

### "Unable to start Kernel" or "timeout waiting for the ports to get used"

This usually means the kernel took too long to start (common with heavy packages like PyMC/numba). Do the following:

1. **Increase kernel startup timeout** (already set in this repo): The workspace `.vscode/settings.json` includes `"jupyter.kernelStartupTimeout": 120` (seconds). If it still times out, increase it (e.g. to `180`) in File → Preferences → Settings, search for `jupyter kernel startup`, and set **Jupyter: Kernel Startup Timeout**.

2. **Register the venv as a Jupyter kernel** so the IDE can start it reliably (from repo root):
   ```powershell
   .\.venv\Scripts\python.exe -m pip install ipykernel
   .\.venv\Scripts\python.exe -m ipykernel install --user --name brent-task2 --display-name "Python (brent-task2)"
   ```
   Then in the notebook use **Select Kernel** → **Python (brent-task2)**.

3. **Use the interpreter directly**: In the notebook, click **Select Kernel** → **Python Environments** → choose **.venv (Python 3.x.x)** that points to `e:\brent-oil-structural-break-analysis\.venv\Scripts\python.exe`. Avoid selecting a kernel that launches a *new* process if you already have a slow-starting env.

4. **Close and reopen the notebook** after changing kernel or settings; restart the IDE if the timeout persists.

5. **Run from command line** if the IDE keeps timing out: from repo root with venv activated, run `jupyter notebook notebooks/task-2-change-point-analysis.ipynb` and select the kernel from the Jupyter UI.
