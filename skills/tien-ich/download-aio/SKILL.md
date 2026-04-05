---
name: download-aio
description: Download videos, audio, playlists, subtitles, and thumbnails from ANY platform (YouTube, TikTok, Instagram, Facebook, Twitter/X, Twitch, Vimeo, SoundCloud, Reddit, and 1000+ more) using yt-dlp. After download, automatically send file to Telegram if under 50MB. Use this skill when the user wants to download video, audio, playlist, reel, short, clip, subtitle, or thumbnail from any website or social media platform. Triggers on phrases like "download video", "download audio", "download playlist", "download from YouTube/TikTok/Facebook/Instagram", "save video", or when user pastes a URL from a video platform.
---

# Download AIO Skill

Download video, audio, playlist, subtitle, thumbnail from 1000+ platforms using yt-dlp. After downloading, automatically send file to Telegram if size <= 50MB.

## Installation (first time)

Before using, run the install script to check and install all dependencies:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/install.ps1
```

The script will automatically:
1. Check Python → guide installation if missing
2. Install yt-dlp
3. Check ffmpeg → install via Chocolatey if missing
4. Create default Downloads folder
5. Verify entire setup

## Usage (User Guide)

### Simplest way
Just paste a URL into chat:
```
https://www.youtube.com/watch?v=...
https://www.tiktok.com/@user/video/...
https://www.facebook.com/reel/...
```

Agent will auto-download + send to Telegram.

### Advanced options
You can also specify:
- "Download audio mp3 from [URL]"
- "Download this playlist, first 10 videos only: [URL]"
- "Download video 720p from [URL]"
- "Download Vietnamese subtitles from [URL]"
- "Download thumbnail from [URL]"

## Workflow

### Step 1: Check dependencies

Run scripts/check.ps1 to verify yt-dlp and ffmpeg are available. If missing, run scripts/install.ps1.

### Step 2: Identify requirements

Collect from user (use defaults if not specified):

| Parameter | Default | Options |
|-----------|---------|---------|
| URL | (required) | - |
| Download type | video | video / audio / playlist / subtitle / thumbnail |
| Quality | best | best / 1080p / 720p / 480p / 360p |
| Format | mp4 (video), mp3 (audio) | mp4 / webm / mkv / mp3 / m4a |
| Save folder | Downloads\yt-dlp\ | any path |

### Step 3: Run download command

See `references/commands.md` for commands for each use case.

Basic command (best quality video):
```powershell
$PYTHON = scripts/find-python.ps1  # auto-detect Python path
& $PYTHON -m yt_dlp `
  -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" `
  --merge-output-format mp4 `
  -o "$env:USERPROFILE\Downloads\yt-dlp\%(title)s.%(ext)s" `
  "<URL>"
```

### Step 4: Send to Telegram (auto)

After download completes:

```powershell
$file = Get-ChildItem "$env:USERPROFILE\Downloads\yt-dlp\" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
$sizeMB = [math]::Round($file.Length / 1MB, 2)
```

- File <= 50MB:
  1. Copy file to temp workspace: `$env:USERPROFILE\.openclaw\workspace\tmp_send.<ext>`
  2. Use `message` tool: action=send, filePath=workspace path, caption="✅ {title} ({sizeMB}MB)"
  3. Delete temp file after sending

- File > 50MB: Notify user "File {sizeMB}MB exceeds Telegram's 50MB limit. Saved at: {path}"

- If send error: notify error + file path on machine

## Supported Platforms

See `references/platforms.md` for full list and platform-specific notes.

Popular platforms: YouTube, TikTok, Facebook, Instagram, Twitter/X, Twitch, Vimeo, SoundCloud, Reddit, Bilibili, Dailymotion, Pinterest, LinkedIn...

## Troubleshooting

See `references/troubleshooting.md` for common errors:
- Installation errors / Python not found
- HTTP 429 (rate limit)
- Bot detection / login required
- ffmpeg not found
- File too large

## Important Notes

- Playlist > 50 videos: ask user how many to download before running
- Private content (Instagram, Twitter): use `--cookies-from-browser chrome`
- Rate limit: add `--sleep-interval 3 --max-sleep-interval 8`
- Update yt-dlp regularly: `python -m pip install -U yt-dlp`
