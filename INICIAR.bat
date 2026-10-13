@echo off
chcp 65001 >nul
cd /d "%~dp0"
title MARVIN v0.7.0
call EXECUTAR.bat main.py
if errorlevel 1 (
 echo MARVIN foi interrompido por erro. Verifique mensagens acima.
 pause
)
