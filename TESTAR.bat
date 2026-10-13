@echo off
cd /d "%~dp0"
call EXECUTAR.bat -B -m unittest discover -s tests
pause
