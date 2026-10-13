@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (echo Execute INSTALAR.bat primeiro.& pause & exit /b 1)
".venv\Scripts\python.exe" -m marvin.model_probe --vision
if errorlevel 1 (echo. & echo Falha ao processar imagem. Verifique os detalhes acima.& pause & exit /b 1)
pause
