param([ValidateSet('AUTO','CPU','CUDA')][string]$Mode='AUTO')
$ErrorActionPreference = 'Stop'
$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$exe = Join-Path $Root 'runtime\llama\llama-server.exe'
$model = Join-Path $Root 'runtime\models\UI-TARS-1.5-7B-q4_k_m.gguf'
$mmproj = Join-Path $Root 'runtime\models\UI-TARS-1.5-7B-q8_0.mmproj'
if (-not (Test-Path $exe)) { throw 'Nao achei llama-server.exe. Execute INSTALAR_SERVIDOR_IA.bat.' }
if (-not ((Test-Path $model) -and (Test-Path $mmproj))) { throw 'Arquivos do modelo ausentes. Execute INSTALAR_SERVIDOR_IA.bat.' }
if ($Mode -eq 'AUTO') {
    $modeFile = Join-Path $Root 'runtime\mode.txt'
    $Mode = if (Test-Path $modeFile) { (Get-Content $modeFile -Raw).Trim() } else { 'CPU' }
}
$gpu = if ($Mode -eq 'CUDA') { 12 } else { 0 }
Write-Host "MARVIN UI-TARS local | modo: $Mode | camadas GPU: $gpu" -ForegroundColor Cyan
Write-Host 'URL: http://127.0.0.1:8080/v1 | Feche esta janela para parar o servidor.'
Write-Host 'Caso apareca erro de memoria CUDA, diminua de 12 para 6 camadas em local_model\start.ps1.'
$argsList = @('--model',$model,'--mmproj',$mmproj,'--no-mmproj-offload', '--alias','ui-tars-local', '--host','127.0.0.1', '--port','8080','--ctx-size','4096','--parallel','1','--n-gpu-layers',"$gpu")
& $exe @argsList
if ($LASTEXITCODE -ne 0) { throw "O servidor terminou com codigo $LASTEXITCODE. Confira as mensagens acima." }
