@echo off
chcp 65001 >nul
cd /d "%~dp0"
rem Cria atalho na Area de Trabalho sem permissao de administrador.
set "MARVIN_DIR=%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -Command "$d=[Environment]::GetFolderPath('Desktop'); $s=(New-Object -ComObject WScript.Shell).CreateShortcut((Join-Path $d 'C MARVIN.lnk')); $s.TargetPath=(Join-Path $env:MARVIN_DIR 'C MARVIN.bat'); $s.WorkingDirectory=$env:MARVIN_DIR; $s.Description='Abrir MARVIN - assistente pessoal'; $s.Save()"
if errorlevel 1 (
 echo Nao foi possivel criar atalho. Use C MARVIN.bat na pasta.
) else (
 echo Atalho C MARVIN criado na Area de Trabalho.
)
pause
