@echo off
setlocal
cd /d "%~dp0"
title MARVIN - Importar biblioteca
echo MARVIN - Biblioteca preparada
echo Mantenha a janela INICIAR_API.bat aberta durante a importacao.
echo.
where py >nul 2>&1
if errorlevel 1 goto tentar_python
py -3 -X utf8 "%~dp0importar_tudo.py" %*
set "MARVIN_IMPORT_EXIT=%errorlevel%"
goto finalizar

:tentar_python
where python >nul 2>&1
if errorlevel 1 goto sem_python
python -X utf8 "%~dp0importar_tudo.py" %*
set "MARVIN_IMPORT_EXIT=%errorlevel%"
goto finalizar

:sem_python
echo ERRO: Python nao encontrado. Instale os requisitos da MARVIN Vault API.
set "MARVIN_IMPORT_EXIT=1"

:finalizar
echo.
if "%MARVIN_IMPORT_EXIT%"=="0" echo Concluido. Confira o resultado acima.
if not "%MARVIN_IMPORT_EXIT%"=="0" echo A importacao nao terminou. Confira o erro acima.
pause
exit /b %MARVIN_IMPORT_EXIT%
