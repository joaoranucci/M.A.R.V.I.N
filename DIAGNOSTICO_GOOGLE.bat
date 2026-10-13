@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Diagnostico Gemini MARVIN 0.6.2
if not exist ".venv\Scripts\python.exe" (
 echo Execute INSTALAR.bat primeiro.
 pause
 exit /b 1
)
".venv\Scripts\python.exe" -m marvin.diagnose
pause
