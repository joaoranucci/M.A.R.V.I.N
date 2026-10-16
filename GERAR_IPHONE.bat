@echo off
setlocal
cd /d "%~dp0"
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\build-iphone.ps1" %*
set "marvin_result=%ERRORLEVEL%"
echo.
if not "%marvin_result%"=="0" echo A geracao do instalavel nao foi concluida. Confira o erro acima.
pause
exit /b %marvin_result%
