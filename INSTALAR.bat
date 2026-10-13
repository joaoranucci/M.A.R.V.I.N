@echo off
chcp 65001 >nul
cd /d "%~dp0"
title Instalar MARVIN v0.7.0
call EXECUTAR.bat setup_marvin.py %*
if errorlevel 1 echo Instalacao incompleta. Confira as mensagens acima. Configuracao e dados preservados.
pause
