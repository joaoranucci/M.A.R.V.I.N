# Gera o APK de prévia (release assinado com a chave de debug) sem servidor de desenvolvimento.
# Uso: powershell -ExecutionPolicy Bypass -File scripts\build-apk.ps1 [-Clean]
param([switch]$Clean)
$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

function Find-Jdk {
  $candidates = @($env:JAVA_HOME, "$env:ProgramFiles\Microsoft\jdk-17*", "$env:ProgramFiles\Android\Android Studio\jbr", "$env:ProgramFiles\Eclipse Adoptium\jdk-17*")
  foreach ($pattern in $candidates) {
    if (-not $pattern) { continue }
    foreach ($dir in (Get-Item $pattern -ErrorAction SilentlyContinue)) {
      if (Test-Path (Join-Path $dir.FullName 'bin\java.exe')) { return $dir.FullName }
    }
  }
  throw 'JDK 17 não encontrado. Instale o Microsoft OpenJDK 17 ou o Android Studio.'
}

$env:JAVA_HOME = Find-Jdk
$env:Path = "$env:JAVA_HOME\bin;$env:Path"
if (-not $env:ANDROID_HOME) { $env:ANDROID_HOME = "$env:LOCALAPPDATA\Android\Sdk" }
if (-not (Test-Path $env:ANDROID_HOME)) { throw "Android SDK não encontrado em $env:ANDROID_HOME" }
# Evita "Unable to establish loopback connection" do JDK quando o TEMP tem caminho longo/restrito.
New-Item -ItemType Directory -Force 'C:\tmp\uds' | Out-Null
$env:JAVA_TOOL_OPTIONS = '-Djdk.net.unixdomain.tmpdir=C:\tmp\uds'

if (-not (Test-Path 'node_modules')) { npm ci }
if ($Clean -or -not (Test-Path 'android')) { npx expo prebuild -p android --clean }

& .\android\gradlew.bat -p android assembleRelease --console=plain
if ($LASTEXITCODE -ne 0) { throw "Gradle falhou ($LASTEXITCODE)" }

$version = (Get-Content app.json -Raw | ConvertFrom-Json).expo.version
New-Item -ItemType Directory -Force 'dist' | Out-Null
$target = "dist\MARVIN-Mobile-$version-preview.apk"
Copy-Item 'android\app\build\outputs\apk\release\app-release.apk' $target -Force
Write-Host "APK pronto: $((Resolve-Path $target).Path)"
