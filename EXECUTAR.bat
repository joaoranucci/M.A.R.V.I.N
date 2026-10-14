@echo off
setlocal
set "PYTHONUTF8=1"
chcp 65001 >nul
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" (
  ".venv\Scripts\python.exe" -c "import sys, tkinter; assert (3, 11) <= sys.version_info[:2] < (3, 15)" >nul 2>&1
  if not errorlevel 1 (
    ".venv\Scripts\python.exe" %*
    exit /b
  )
)
echo Ambiente local indisponivel. Tentando Python do sistema em modo degradado.
if exist "%LocalAppData%\Programs\Python\Python312\python.exe" (
  "%LocalAppData%\Programs\Python\Python312\python.exe" %*
  exit /b
)
where py >nul 2>&1
if not errorlevel 1 (
  py -3 %*
  exit /b
)
where python >nul 2>&1
if not errorlevel 1 (
  python %*
  exit /b
)
echo Python nao encontrado. Execute INSTALAR.bat apos instalar Python 3.12 x64.
exit /b 1
