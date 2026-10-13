@echo off
chcp 65001 >nul
cd /d "%~dp0"
title MARVIN - Servidor UI-TARS 1.5 local
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0local_model\start.ps1"
if errorlevel 1 (echo. & echo Servidor nao iniciou. Verifique detalhes acima. & pause & exit /b 1)
pause
