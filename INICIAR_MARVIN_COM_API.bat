@echo off
setlocal
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" goto missing
echo MARVIN com API local - interface classica integrada
echo Mantenha INICIAR_API.bat aberto na pasta da API.
".venv\Scripts\python.exe" -X utf8 main.py --legacy
set "MARVIN_LAUNCH_EXIT=%errorlevel%"
pause
exit /b %MARVIN_LAUNCH_EXIT%
:missing
echo Python do MARVIN nao encontrado. Verifique a instalacao em .venv.
pause
exit /b 1
