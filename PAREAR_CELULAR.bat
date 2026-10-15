@echo off
setlocal
cd /d "%~dp0"
call EXECUTAR.bat -m marvin.gateway pair %*
pause
