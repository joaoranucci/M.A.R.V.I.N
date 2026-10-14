@echo off
setlocal
cd /d "%~dp0"
call EXECUTAR.bat -m pip install -r requirements-desktop.txt
if errorlevel 1 exit /b 1
cd desktop
call npm.cmd ci --no-fund --no-audit
if errorlevel 1 exit /b 1
call npm.cmd run build
if errorlevel 1 exit /b 1
echo Interface pronta. Abra INICIAR_PRESENCA.bat.
pause
