@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (echo Falta Python configurado. Execute INSTALAR.bat antes. & pause & exit /b 1)
".venv\Scripts\python.exe" -m marvin.model_probe
if errorlevel 1 (echo. & echo Teste falhou. Confira se INICIAR_SERVIDOR_IA.bat esta aberto. & pause & exit /b 1)
pause
