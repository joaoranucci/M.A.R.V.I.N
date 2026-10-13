# MARVIN local UI-TARS 1.5 model installer. Sources: official llama.cpp releases + Hugging Face.
param([ValidateSet('CUDA','CPU')][string]$Mode = 'CUDA')
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$Bin = Join-Path $Root 'runtime\llama'
$ModelDir = Join-Path $Root 'runtime\models'
$Temp = Join-Path $Root 'runtime\downloads'
if (-not [Environment]::Is64BitOperatingSystem) { throw 'Windows 64 bits e necessario.' }
if (-not (Get-Command curl.exe -ErrorAction SilentlyContinue)) { throw 'curl.exe nao encontrado. Atualize o Windows ou instale o curl.' }
New-Item -ItemType Directory -Force -Path @($Bin, $ModelDir, $Temp) | Out-Null
$Drive = ([System.IO.Path]::GetPathRoot($Root))
$Free = (Get-PSDrive -Name $Drive.Substring(0,1)).Free
if ((-not (Test-Path (Join-Path $ModelDir 'UI-TARS-1.5-7B-q4_k_m.gguf'))) -and $Free -lt 9GB) {
    throw "Pouco espaco livre em $Drive. Recomendo pelo menos 9 GB livres para o download inicial."
}
Write-Host "MARVIN - instalacao do motor visual (modo: $Mode)" -ForegroundColor Cyan
Write-Host 'Usando release fixa validada do llama.cpp + pesos publicos do UI-TARS. Nenhuma API paga.'

function Download-Checked([string]$URL, [string]$Destination, [string]$ExpectedHash, [int64]$MinimumBytes) {
    if (Test-Path $Destination) {
        if ((Get-Item $Destination).Length -ge $MinimumBytes) {
            $hash = (Get-FileHash $Destination -Algorithm SHA256).Hash.ToLowerInvariant()
            if ($hash -eq $ExpectedHash.ToLowerInvariant()) {
                Write-Host "OK cache: $(Split-Path $Destination -Leaf)"
                return
            }
            Write-Host 'Hash invalido, baixando novamente.' -ForegroundColor Yellow
            Remove-Item $Destination -Force
        }
    }
    Write-Host "Baixando: $(Split-Path $Destination -Leaf)" -ForegroundColor Yellow
    # curl.exe -C - is resumable. Do not print any remote API keys.
    & curl.exe --fail --location --retry 4 --retry-delay 5 --connect-timeout 30 --continue-at - --output $Destination $URL
    if ($LASTEXITCODE -ne 0) { throw "Falha ao baixar $(Split-Path $Destination -Leaf) (curl codigo $LASTEXITCODE). Verifique rede/GitHub/Hugging Face e rode novamente." }
    if ((Get-Item $Destination).Length -lt $MinimumBytes) { throw "Arquivo incompleto: $Destination" }
    $hash = (Get-FileHash $Destination -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($hash -ne $ExpectedHash.ToLowerInvariant()) {
        Remove-Item $Destination -Force
        throw "SHA256 nao confere. Arquivo descartado: $Destination"
    }
    Write-Host 'SHA256 validado.' -ForegroundColor Green
}

# v0.6.1: fixed, verified upstream artifacts. No fragile GitHub release discovery.
# Official release: https://github.com/ggml-org/llama.cpp/releases/tag/b11583
# Manifests validated against GitHub release assets on 2026-10-13.
$ReleaseTag = 'b11583'
$ReleaseRoot = "https://github.com/ggml-org/llama.cpp/releases/download/$ReleaseTag"
$artifacts = @{
    'llama-b11583-bin-win-cuda-12.4-x64.zip' = @{
        SHA256 = 'db709bfc5ee1a8eb34e03cf6cb5f936a985aaf8cd7b15af967e137c4a7d0191b'
        Bytes = [int64]265226766
    }
    'cudart-llama-bin-win-cuda-12.4-x64.zip' = @{
        SHA256 = '8c79a9b226de4b3cacfd1f83d24f962d0773be79f1e7b75c6af4ded7e32ae1d6'
        Bytes = [int64]391443627
    }
    'llama-b11583-bin-win-cpu-x64.zip' = @{
        SHA256 = '2bceb716d9d93b950c008c9d81701650965c33e957de9e1d4da325c35c41abfe'
        Bytes = [int64]19509591
    }
}
$names = if ($Mode -eq 'CUDA') {
    @('llama-b11583-bin-win-cuda-12.4-x64.zip', 'cudart-llama-bin-win-cuda-12.4-x64.zip')
} else {
    @('llama-b11583-bin-win-cpu-x64.zip')
}
Write-Host "Release fixa verificada: $ReleaseTag | Modo: $Mode"

foreach ($name in $names) {
    $asset = $artifacts[$name]
    $archive = Join-Path $Temp $name
    Download-Checked "$ReleaseRoot/$name" $archive $asset.SHA256 ([int64]($asset.Bytes * 0.95))
    Write-Host "Extraindo $name"
    Expand-Archive -Path $archive -DestinationPath $Bin -Force
}
# Ensure executable and DLLs are together even if ZIP archives have nested folders.
$found = Get-ChildItem -Path $Bin -Filter 'llama-server.exe' -File -Recurse | Select-Object -First 1
if (-not $found) { throw 'Extracao concluida, mas llama-server.exe nao foi encontrado.' }
if ($found.DirectoryName -ne $Bin) {
    Get-ChildItem -Path $found.DirectoryName -File | Copy-Item -Destination $Bin -Force
}
# cudart archive may have DLLs in a different nested folder.
$allDlls = @(Get-ChildItem -Path $Bin -Filter '*.dll' -File -Recurse)
foreach ($dll in $allDlls) {
    if ($dll.DirectoryName -ne $Bin) {
        $dest = Join-Path $Bin $dll.Name
        if (-not (Test-Path $dest)) { Copy-Item -Path $dll.FullName -Destination $dest }
    }
}
if (-not (Test-Path (Join-Path $Bin 'llama-server.exe'))) {
    throw 'llama-server.exe nao ficou na pasta runtime\llama.'
}

$repo = 'https://huggingface.co/Mungert/UI-TARS-1.5-7B-GGUF/resolve/main/'
Download-Checked ($repo + 'UI-TARS-1.5-7B-q4_k_m.gguf') (Join-Path $ModelDir 'UI-TARS-1.5-7B-q4_k_m.gguf') 'b65488bf94d3f0525cf609c8bc5d03fa4800589546189bdfdc2f6cea0356e7f8' 4000000000
Download-Checked ($repo + 'UI-TARS-1.5-7B-q8_0.mmproj') (Join-Path $ModelDir 'UI-TARS-1.5-7B-q8_0.mmproj') '27dde5528b1476e9aa44a7213408b389dd4c4ce4222aba8d1db9f105fb67e4de' 750000000

$modeFile = Join-Path $Root 'runtime\mode.txt'
Set-Content -Path $modeFile -Value $Mode -Encoding ascii
$envPath = Join-Path $Root '.env'
if (-not (Test-Path $envPath)) { Copy-Item (Join-Path $Root '.env.example') $envPath }
$content = Get-Content $envPath -Raw -Encoding UTF8
$settings = [ordered]@{
 'MARVIN_VISUAL'='true'
 'UI_TARS_BASE_URL'='http://127.0.0.1:8080/v1'
 'UI_TARS_MODEL'='ui-tars-local'
 'UI_TARS_API_KEY'='local'
 'UI_TARS_ALLOW_REMOTE'='false'
 'UI_TARS_MAX_STEPS'='8'
}
foreach ($key in $settings.Keys) {
    $value = $settings[$key]
    $pattern = '(?m)^' + [regex]::Escape($key) + '\s*=.*$'
    if ($content -match $pattern) { $content = [regex]::Replace($content, $pattern, "$key=$value") }
    else { $content += "`r`n$key=$value" }
}
[System.IO.File]::WriteAllText($envPath, $content, (New-Object System.Text.UTF8Encoding($false)))
Write-Host "`nModelo instalado! Inicio: INICIAR_SERVIDOR_IA.bat" -ForegroundColor Green
Write-Host 'A primeira resposta visual pode demorar. Teste o servidor antes do controle do Windows.'
