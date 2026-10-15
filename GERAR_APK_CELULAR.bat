@echo off
setlocal
cd /d "%~dp0mobile"
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0mobile\scripts\build-apk.ps1" %*
pause