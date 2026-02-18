# Run Task-1 notebook with correct environment.
# Usage: .\scripts\run_task1.ps1
# Run from repo root. Installs the 6 required packages if missing, then opens/runs the notebook.

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$VenvPython = Join-Path $Root ".venv\Scripts\python.exe"
$Notebook = Join-Path $Root "notebooks\task1_ingest_clean_diagnose.ipynb"

if (-not (Test-Path $VenvPython)) {
    Write-Host "Creating venv..."; & (Join-Path $Root "scripts\setup_venv.ps1"); if ($LASTEXITCODE -ne 0) { exit 1 }
}

# Ensure the 6 required packages are installed
$packages = "pandas", "numpy", "matplotlib", "seaborn", "scipy", "statsmodels"
& $VenvPython -m pip install --quiet $packages
if ($LASTEXITCODE -ne 0) { Write-Host "Failed to install packages."; exit 1 }
Write-Host "Packages OK. Starting Jupyter notebook..."
Set-Location $Root
& $VenvPython -m jupyter notebook $Notebook
