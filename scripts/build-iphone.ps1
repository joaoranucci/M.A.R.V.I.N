# Solicita uma build assinada de iPhone no EAS; nao usa o simulador nem Expo Go.
# Requer conta Expo e Apple Developer Program ativo. Nunca forneca senhas por chat.
[CmdletBinding()]
param([switch]$DeviceAlreadyRegistered)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

function Invoke-MarvinCommand {
  param([string]$Program, [string[]]$Arguments)
  & $Program @Arguments
  if ($LASTEXITCODE -ne 0) {
    throw "Falha ao executar $Program (codigo $LASTEXITCODE). A build nao foi concluida."
  }
}

$mobileRoot = Join-Path (Split-Path -Parent $PSScriptRoot) 'mobile'
Push-Location -LiteralPath $mobileRoot
try {
  Write-Host 'MARVIN - Gerar instalavel para iPhone'
  Write-Host 'Requer: Node 22.13+, conta Expo e Apple Developer Program ativo.'
  Write-Host 'O login sera feito pelas ferramentas oficiais no seu computador.'
  Write-Host ''

  foreach ($program in @('node.exe', 'npm.cmd', 'npx.cmd')) {
    if (-not (Get-Command $program -ErrorAction SilentlyContinue)) {
      throw 'Instale o Node.js LTS 22.13 ou superior: https://nodejs.org/ . Depois reabra este atalho.'
    }
  }
  $nodeText = & node.exe --version
  if ($LASTEXITCODE -ne 0) { throw 'Nao foi possivel consultar a versao do Node.js.' }
  $nodeVersion = [version]($nodeText.Trim().TrimStart('v'))
  if ($nodeVersion -lt [version]'22.13.0') {
    throw "Node $nodeText incompativel. Instale Node.js 22.13 ou superior."
  }

  Write-Host 'Instalando dependencias e verificando o aplicativo...'
  Invoke-MarvinCommand -Program 'npm.cmd' -Arguments @('ci', '--no-audit', '--no-fund')
  Invoke-MarvinCommand -Program 'npm.cmd' -Arguments @('run', 'lint')
  Invoke-MarvinCommand -Program 'npm.cmd' -Arguments @('run', 'typecheck')
  Invoke-MarvinCommand -Program 'npm.cmd' -Arguments @('test')

  # Mantem a sessao existente. Em uma instalacao nova a CLI pede o login Expo.
  & npx.cmd --yes eas-cli@latest whoami
  if ($LASTEXITCODE -ne 0) {
    Invoke-MarvinCommand -Program 'npx.cmd' -Arguments @('--yes', 'eas-cli@latest', 'login')
  }

  # Vincula ao projeto real sem forcar troca de um projectId ja configurado.
  Invoke-MarvinCommand -Program 'npx.cmd' -Arguments @('--yes', 'eas-cli@latest', 'init')

  if (-not $DeviceAlreadyRegistered) {
    Write-Host ''
    Write-Host 'Cadastro do iPhone: abra no Safari do iPhone o link/QR exibido pela CLI.'
    Write-Host 'Conclua o cadastro antes de prosseguir para a compilacao.'
    Invoke-MarvinCommand -Program 'npx.cmd' -Arguments @('--yes', 'eas-cli@latest', 'device:create')
  }

  Write-Host ''
  Write-Host 'A CLI pedira o acesso Apple e a equipe de assinatura, quando necessario.'
  Write-Host 'Selecione o seu iPhone para incluir o UDID no perfil de provisionamento.'
  Write-Host 'A compilacao sera feita na nuvem. Aguarde o resultado e o link do EAS.'
  Invoke-MarvinCommand -Program 'npx.cmd' -Arguments @(
    '--yes', 'eas-cli@latest', 'build', '--platform', 'ios', '--profile', 'preview', '--wait'
  )

  Write-Host ''
  Write-Host 'Build concluida no EAS. Abra o link de instalacao exibido acima no Safari do iPhone.'
  Write-Host 'O .ipa esta disponivel nos detalhes dessa build. Esta previa nao precisa do Metro.'
}
catch {
  Write-Host ''
  Write-Host $_.Exception.Message -ForegroundColor Red
  Write-Host 'Ajuda: docs/mobile/IOS.md - Gerar um instalavel para o seu iPhone'
  exit 1
}
finally {
  Pop-Location
}
