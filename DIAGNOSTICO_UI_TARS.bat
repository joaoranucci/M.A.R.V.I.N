@echo off
chcp 65001 >nul
cd /d "%~dp0"
title MARVIN - Diagnostico UI-TARS
if not exist ".venv\Scripts\python.exe" (echo Rode INSTALAR.bat antes.& pause& exit /b 1)
".venv\Scripts\python.exe" -m marvin.visual_diagnostic
pause
