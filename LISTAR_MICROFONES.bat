@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
 echo Execute INSTALAR.bat antes.
 pause
 exit /b 1
)
".venv\Scripts\python.exe" -m marvin.microphones
pause
