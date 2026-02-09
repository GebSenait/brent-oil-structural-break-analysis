# Register the project .venv as a Jupyter kernel so notebooks can use it without timeout issues.
# Run from repo root: .\scripts\register_kernel.ps1

$ErrorActionPreference = "Stop"
$Root = (Get-Item $PSScriptRoot).Parent.FullName
$VenvPython = Join-Path $Root ".venv\Scripts\python.exe"

if (-not (Test-Path $VenvPython)) {
    Write-Host "ERROR: .venv not found. Create it first: python -m venv .venv"
    exit 1
}

Write-Host "Installing ipykernel into .venv (if needed)..."
& $VenvPython -m pip install --quiet ipykernel

Write-Host "Registering Jupyter kernel 'brent-task2'..."
& $VenvPython -m ipykernel install --user --name brent-task2 --display-name "Python (brent-task2)"

Write-Host "Done. In the notebook, use Select Kernel -> Python (brent-task2)."
Write-Host "If the kernel still times out, increase Jupyter kernel startup timeout in settings (e.g. 120 or 180 seconds)."
