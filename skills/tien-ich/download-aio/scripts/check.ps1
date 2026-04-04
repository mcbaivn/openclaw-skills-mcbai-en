# check.ps1 - Kiểm tra nhanh dependencies
# Usage: scripts/check.ps1

$ok = $true

# Python
$pythonExe = & "$PSScriptRoot\find-python.ps1" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "MISSING Python - chay install.ps1" -ForegroundColor Red
    $ok = $false
} else {
    $ver = & $pythonExe --version 2>&1
    Write-Host "OK Python: $ver" -ForegroundColor Green
}

# yt-dlp
if ($pythonExe -and $LASTEXITCODE -eq 0) {
    try {
        $ytVer = & $pythonExe -m yt_dlp --version 2>&1
        Write-Host "OK yt-dlp: $ytVer" -ForegroundColor Green
    } catch {
        Write-Host "MISSING yt-dlp - chay install.ps1" -ForegroundColor Red
        $ok = $false
    }
}

# ffmpeg
try {
    $ffVer = ffmpeg -version 2>&1 | Select-Object -First 1
    if ($ffVer -match "ffmpeg version") {
        Write-Host "OK ffmpeg: co san" -ForegroundColor Green
    } else { throw }
} catch {
    Write-Host "WARN ffmpeg: khong co (can de merge video+audio)" -ForegroundColor Yellow
}

if ($ok) { exit 0 } else { exit 1 }
