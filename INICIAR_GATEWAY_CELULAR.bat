@echo off
setlocal
cd /d "%~dp0"
echo MARVIN - gateway para o celular (sem janela e sem audio no PC)
echo Para usar junto com a interface Presenca, use INICIAR_PRESENCA_COM_CELULAR.bat
call EXECUTAR.bat -m marvin.gateway serve %*
pause
