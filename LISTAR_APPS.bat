@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo MARVIN - Aplicativos encontrados no Windows
if not exist ".venv\Scripts\python.exe" (
 echo Execute INSTALAR.bat primeiro.
 pause
 exit /b 1
)
".venv\Scripts\python.exe" -m marvin.list_apps_cli
pause
