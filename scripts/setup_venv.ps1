# Setup virtual environment and install dependencies for Task-2 notebook.
# Run from repo root:  .\scripts\setup_venv.ps1
# If execution is blocked: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not (Test-Path (Join-Path $Root "requirements.txt"))) {
    Write-Host "Run this script from repo root or ensure scripts/setup_venv.ps1 lives in repo."
    exit 1
}
Set-Location $Root

$Venv = Join-Path $Root ".venv"
$VenvPython = Join-Path $Venv "Scripts\python.exe"
$VenvPip = Join-Path $Venv "Scripts\pip.exe"

if (-not (Test-Path $Venv)) {
    Write-Host "Creating virtual environment at .venv ..."
    if (Get-Command py -ErrorAction SilentlyContinue) {
        py -m venv .venv
    } else {
        python -m venv .venv
    }
}
if (-not (Test-Path $VenvPython)) {
    Write-Host "Venv Python not found at $VenvPython"
    exit 1
}

Write-Host "Installing dependencies (this may take a few minutes) ..."
& $VenvPython -m pip install --quiet --upgrade pip
& $VenvPython -m pip install -r requirements.txt

Write-Host "Verifying Task-2 packages ..."
& $VenvPython (Join-Path $Root "scripts\verify_task2_env.py")
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host ""
Write-Host "To activate the venv (PowerShell):"
Write-Host "  .\.venv\Scripts\Activate.ps1"
Write-Host ""
Write-Host "To register Jupyter kernel and run Task-2 notebook:"
Write-Host "  .\.venv\Scripts\python.exe -m ipykernel install --user --name=brent-task2 --display-name 'Python (brent-task2)'"
Write-Host "  Then open notebooks/task-2-change-point-analysis.ipynb and select kernel 'Python (brent-task2)'."
Write-Host ""
Write-Host "Done."
