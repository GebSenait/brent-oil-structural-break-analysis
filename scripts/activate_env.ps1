# Activate venv and set up environment for this project.
# Run from repo root: .\scripts\activate_env.ps1
# Or source it: . .\scripts\activate_env.ps1

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Venv = Join-Path $Root ".venv"
$Activate = Join-Path $Venv "Scripts\Activate.ps1"

if (-not (Test-Path $Activate)) {
    Write-Host "Virtual environment not found. Run: .\scripts\setup_venv.ps1"
    exit 1
}

Set-Location $Root
& $Activate
Write-Host "Virtual environment activated. Python: $(python -c 'import sys; print(sys.executable)')"
