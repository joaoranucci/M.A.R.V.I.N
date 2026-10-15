@echo off
setlocal
cd /d "%~dp0"
set "MARVIN_MOBILE_GATEWAY=true"
call EXECUTAR.bat -m marvin.desktop --mobile %*
if errorlevel 1 pause
