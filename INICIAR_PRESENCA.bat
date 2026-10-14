@echo off
setlocal
cd /d "%~dp0"
call EXECUTAR.bat -m marvin.desktop %*
if errorlevel 1 pause
