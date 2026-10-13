@echo off
chcp 65001 >nul
cd /d "%~dp0"
title MARVIN - Instalar servidor de inferencia GPU NVIDIA
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0local_model\install.ps1" -Mode CUDA
if errorlevel 1 (echo. & echo ERRO na instalacao. Veja detalhes acima. & pause & exit /b 1)
echo.
echo Concluido. Abra INICIAR_SERVIDOR_IA.bat para iniciar.
pause
