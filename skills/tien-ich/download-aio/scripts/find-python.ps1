# find-python.ps1 - Tìm Python path trên hệ thống
# Usage: $python = & scripts/find-python.ps1

# Thử đọc từ file cache trước
$cachePath = "$PSScriptRoot\python-path.txt"
if (Test-Path $cachePath) {
    $cached = Get-Content $cachePath -Raw | ForEach-Object { $_.Trim() }
    try {
        $ver = & $cached --version 2>&1
        if ($ver -match "Python 3") {
            Write-Output $cached
            exit 0
        }
    } catch {}
}

# Auto detect
$pythonPaths = @(
    "python",
    "python3",
    "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python310\python.exe",
    "C:\Python311\python.exe",
    "C:\Python312\python.exe"
)

foreach ($p in $pythonPaths) {
    try {
        $ver = & $p --version 2>&1
        if ($ver -match "Python 3") {
            $p | Out-File $cachePath -Encoding UTF8
            Write-Output $p
            exit 0
        }
    } catch {}
}

Write-Error "Python khong tim thay! Chay scripts/install.ps1 de cai dat."
exit 1
