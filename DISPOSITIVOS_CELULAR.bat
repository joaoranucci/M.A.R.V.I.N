@echo off
setlocal
cd /d "%~dp0"
call EXECUTAR.bat -m marvin.gateway devices
echo.
echo Para revogar: EXECUTAR.bat -m marvin.gateway revoke ID_DO_DISPOSITIVO
pause
