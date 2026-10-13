@echo off
chcp 65001 >nul
cd /d "%~dp0"
title MARVIN - Diagnostico do microfone
if not exist ".venv\Scripts\python.exe" (
  echo Python do MARVIN nao encontrado. Execute INSTALAR.bat.
  pause
  exit /b 1
)
".venv\Scripts\python.exe" -m marvin.microphones --test
echo.
pause
