# Download AIO - Script cài đặt tự động
# Chạy: powershell -ExecutionPolicy Bypass -File scripts/install.ps1

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Download AIO - Setup & Install" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$errors = 0

# ── 1. Kiểm tra Python ──────────────────────────────────────────────
Write-Host "[1/4] Kiểm tra Python..." -ForegroundColor Yellow

$pythonPaths = @(
    "python",
    "python3",
    "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python310\python.exe",
    "C:\Python311\python.exe",
    "C:\Python312\python.exe"
)

$pythonExe = $null
foreach ($p in $pythonPaths) {
    try {
        $ver = & $p --version 2>&1
        if ($ver -match "Python 3") {
            $pythonExe = $p
            Write-Host "  OK Python: $ver at $p" -ForegroundColor Green
            break
        }
    } catch {}
}

if (-not $pythonExe) {
    Write-Host "  MISSING Python chua duoc cai!" -ForegroundColor Red
    Write-Host "  -> Tai Python tai: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host "  -> Tick 'Add Python to PATH' khi cai" -ForegroundColor Yellow
    $errors++
} else {
    # Lưu python path ra file để scripts khác dùng
    $pythonExe | Out-File "$PSScriptRoot\python-path.txt" -Encoding UTF8
}

# ── 2. Cài yt-dlp ───────────────────────────────────────────────────
Write-Host ""
Write-Host "[2/4] Cài yt-dlp..." -ForegroundColor Yellow

if ($pythonExe) {
    try {
        $ytdlpVersion = & $pythonExe -m yt_dlp --version 2>&1
        if ($ytdlpVersion -match "\d{4}\.\d+\.\d+") {
            Write-Host "  OK yt-dlp $ytdlpVersion (da co san)" -ForegroundColor Green
        } else {
            throw "not installed"
        }
    } catch {
        Write-Host "  Dang cai yt-dlp..." -ForegroundColor Yellow
        & $pythonExe -m pip install yt-dlp 2>&1 | Where-Object { $_ -match "Successfully|already" } | ForEach-Object { Write-Host "  $_" -ForegroundColor Green }
        $ytdlpVersion = & $pythonExe -m yt_dlp --version 2>&1
        Write-Host "  OK yt-dlp $ytdlpVersion" -ForegroundColor Green
    }

    # Update nếu cũ
    Write-Host "  Kiem tra update yt-dlp..." -ForegroundColor Gray
    & $pythonExe -m pip install -U yt-dlp --quiet 2>&1 | Out-Null
    $newVersion = & $pythonExe -m yt_dlp --version 2>&1
    Write-Host "  yt-dlp version hien tai: $newVersion" -ForegroundColor Green
}

# ── 3. Kiểm tra / Cài ffmpeg ────────────────────────────────────────
Write-Host ""
Write-Host "[3/4] Kiểm tra ffmpeg..." -ForegroundColor Yellow

$ffmpegOk = $false
try {
    $ffVer = ffmpeg -version 2>&1 | Select-Object -First 1
    if ($ffVer -match "ffmpeg version") {
        Write-Host "  OK ffmpeg da co san" -ForegroundColor Green
        $ffmpegOk = $true
    }
} catch {}

if (-not $ffmpegOk) {
    Write-Host "  ffmpeg chua co - can de merge video+audio va convert format" -ForegroundColor Yellow

    # Thử cài qua Chocolatey
    $chocoExists = Get-Command choco -ErrorAction SilentlyContinue
    if ($chocoExists) {
        Write-Host "  Dang cai ffmpeg qua Chocolatey..." -ForegroundColor Yellow
        choco install ffmpeg -y 2>&1 | Where-Object { $_ -match "installed|already" } | ForEach-Object { Write-Host "  $_" -ForegroundColor Green }
        $ffmpegOk = $true
    } else {
        Write-Host "  Chocolatey khong co san." -ForegroundColor Yellow
        Write-Host "  -> Option 1: Cai Chocolatey: https://chocolatey.org/install" -ForegroundColor Cyan
        Write-Host "               Sau do chay: choco install ffmpeg" -ForegroundColor Cyan
        Write-Host "  -> Option 2: Tai ffmpeg thu cong: https://ffmpeg.org/download.html" -ForegroundColor Cyan
        Write-Host "               Giai nen va them vao PATH" -ForegroundColor Cyan
        Write-Host "  NOTE: Khong co ffmpeg van tai duoc nhung chi o dinh dang webm/mp4 goc" -ForegroundColor Gray
    }
}

# ── 4. Tạo thư mục Downloads ────────────────────────────────────────
Write-Host ""
Write-Host "[4/4] Tao thu muc Downloads..." -ForegroundColor Yellow

$downloadDir = "$env:USERPROFILE\Downloads\yt-dlp"
New-Item -ItemType Directory -Path $downloadDir -Force | Out-Null
Write-Host "  OK Thu muc: $downloadDir" -ForegroundColor Green

# ── Tổng kết ────────────────────────────────────────────────────────
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
if ($errors -eq 0) {
    Write-Host "  SETUP HOAN TAT! San sang su dung." -ForegroundColor Green
} else {
    Write-Host "  SETUP HOAN TAT (co $errors loi can xu ly)" -ForegroundColor Yellow
}
Write-Host "  Thu muc tai ve: $downloadDir" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
