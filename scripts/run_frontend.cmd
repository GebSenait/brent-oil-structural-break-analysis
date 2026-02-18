@echo off
REM Run React frontend from project root:  scripts\run_frontend.cmd
REM Uses frontend folder next to scripts folder; works on any drive.

set "FRONTEND_DIR=%~dp0..\frontend"
cd /d "%FRONTEND_DIR%"
if not exist package.json (
  echo Error: package.json not found in %FRONTEND_DIR%
  exit /b 1
)
echo Running npm in: %CD%
call npm install
call npm run dev
