@echo off
chcp 65001 >nul
cd /d "%~dp0ui_tars_bridge"
title MARVIN v0.6 - Instalar SDK UI-TARS
where node >nul 2>&1
if errorlevel 1 (
 echo Node.js nao encontrado. Instale Node.js 22 LTS: https://nodejs.org/
 pause
 exit /b 1
)
node --version
where npm >nul 2>&1
if errorlevel 1 (echo npm nao encontrado.& pause& exit /b 1)
echo Instalando SDK oficial e operador NutJS. Nao inclui modelo de IA.
call npm install --no-audit --no-fund
if errorlevel 1 (echo Falha na instalacao do SDK.& pause& exit /b 1)
echo SDK instalado. Configure UI_TARS_BASE_URL e UI_TARS_MODEL no .env.
pause
