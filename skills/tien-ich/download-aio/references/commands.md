# Download AIO - Detailed yt-dlp Commands

## Setup Python path

```powershell
# Always use find-python.ps1 to find the correct Python
$PYTHON = & "$PSScriptRoot\..\scripts\find-python.ps1"
$OUT = "$env:USERPROFILE\Downloads\yt-dlp"
New-Item -ItemType Directory -Path $OUT -Force | Out-Null
```

## Download video (best quality - mp4)

```powershell
& $PYTHON -m yt_dlp `
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" `
  --merge-output-format mp4 `
  -o "$OUT\%(title)s.%(ext)s" `
  "<URL>"
```

## Download video at specific quality

```powershell
# 1080p
-f "bestvideo[height<=1080][ext=mp4]+bestaudio[ext=m4a]/best[height<=1080]"

# 720p
-f "bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720]"

# 480p
-f "bestvideo[height<=480]+bestaudio/best[height<=480]"

# 360p (lightest)
-f "bestvideo[height<=360]+bestaudio/best[height<=360]"
```

## Download audio only

```powershell
# MP3 (requires ffmpeg)
& $PYTHON -m yt_dlp `
  -x --audio-format mp3 --audio-quality 0 `
  -o "$OUT\%(title)s.%(ext)s" `
  "<URL>"

# M4A (no ffmpeg needed)
& $PYTHON -m yt_dlp `
  -f "bestaudio[ext=m4a]/bestaudio" `
  -o "$OUT\%(title)s.%(ext)s" `
  "<URL>"
```

## Download playlist

```powershell
# Full playlist
& $PYTHON -m yt_dlp `
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" `
  --merge-output-format mp4 `
  -o "$OUT\%(playlist_title)s\%(playlist_index)s - %(title)s.%(ext)s" `
  "<PLAYLIST_URL>"

# Limit count (first 10 videos)
--playlist-end 10

# Start from video N
--playlist-start 5

# Only download videos 3, 5, 7
--playlist-items 3,5,7
```

## Download subtitles

```powershell
# Auto-generated subtitles
& $PYTHON -m yt_dlp `
  --write-auto-sub --sub-lang "vi,en" --skip-download `
  -o "$OUT\%(title)s.%(ext)s" `
  "<URL>"

# Official subtitles
--write-sub --sub-lang "vi,en"

# Embed subtitles into video
--embed-subs --sub-lang "vi,en"

# Download both video and subtitles
& $PYTHON -m yt_dlp `
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" `
  --merge-output-format mp4 `
  --write-sub --write-auto-sub --sub-lang "vi,en" `
  -o "$OUT\%(title)s.%(ext)s" `
  "<URL>"
```

## Download thumbnail

```powershell
& $PYTHON -m yt_dlp `
  --write-thumbnail --skip-download --convert-thumbnails jpg `
  -o "$OUT\%(title)s.%(ext)s" `
  "<URL>"
```

## View video info (without downloading)

```powershell
# Basic info
& $PYTHON -m yt_dlp --dump-json "<URL>" | ConvertFrom-Json | `
  Select-Object title, duration, view_count, like_count, upload_date, uploader

# List all available formats
& $PYTHON -m yt_dlp -F "<URL>"
```

## Using cookies (for content requiring login)

```powershell
# Use cookies from Chrome (most common)
--cookies-from-browser chrome

# Use cookies from Firefox
--cookies-from-browser firefox

# Manual cookie export (if auto doesn't work)
# Use extension "Get cookies.txt LOCALLY" on Chrome
# Export to cookies.txt then use:
--cookies path/to/cookies.txt
```

## Useful options

```powershell
--no-playlist              # Only download 1 video, skip playlist
--yes-playlist             # Force download full playlist
--download-archive "$OUT\downloaded.txt"  # Save history, skip already downloaded
--concurrent-fragments 4   # Faster download (4 parallel threads)
--retries 10               # Retry 10 times on network error
--sleep-interval 2         # Wait 2s between requests (avoid rate limit)
--max-sleep-interval 5     # Max wait 5s
--limit-rate 5M            # Limit speed to 5MB/s
--no-overwrites            # Don't overwrite existing files
-k                         # Keep original files after merge
```

## Send file to Telegram (via OpenClaw message tool)

```powershell
# After download completes, get the newest file
$file = Get-ChildItem $OUT -Filter "*.mp4" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
$sizeMB = [math]::Round($file.Length / 1MB, 2)

if ($sizeMB -le 50) {
    # Copy to workspace to send (OpenClaw only allows sending from workspace)
    $tmpPath = "$env:USERPROFILE\.openclaw\workspace\tmp_send$($file.Extension)"
    Copy-Item $file.FullName $tmpPath -Force

    # Use OpenClaw message tool:
    # action: send
    # channel: telegram
    # filePath: $tmpPath
    # caption: "✅ $($file.BaseName) ($sizeMB MB)"

    # After sending, delete temp file
    Remove-Item $tmpPath -Force
} else {
    Write-Host "File $sizeMB MB exceeds Telegram's 50MB limit. Saved at: $($file.FullName)"
}
```

## Update yt-dlp

```powershell
$PYTHON = & scripts/find-python.ps1
& $PYTHON -m pip install -U yt-dlp
```
