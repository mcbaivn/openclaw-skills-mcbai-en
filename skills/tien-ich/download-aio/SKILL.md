---
name: download-aio
clawhub_id: mcbaivn-download-aio
description: |
  Download videos, audio, playlists, subtitles and thumbnails from ANY platform
  (YouTube, TikTok, Instagram, Facebook, Twitter/X, Twitch, Vimeo, SoundCloud,
  Reddit and 1000+ more) using yt-dlp. Auto-send file to Telegram if under 50MB.
---

# Download AIO

> 📦 **Install:** `npx clawhub@latest install mcbaivn-download-aio`

Download video, audio, playlist, subtitle, thumbnail from 1000+ platforms. Auto-send to Telegram if file is under 50MB.

## Install

```bash
npx clawhub@latest install mcbaivn-download-aio
```

> First-time setup:
> ```powershell
> powershell -ExecutionPolicy Bypass -File scripts/install.ps1
> ```

## Usage

Just paste a URL into chat:
```
https://www.youtube.com/watch?v=...
https://www.tiktok.com/@user/video/...
https://www.facebook.com/reel/...
```

### Advanced options
- "Download audio mp3 from [URL]"
- "Download this playlist, only first 10: [URL]"
- "Download 720p video from [URL]"
- "Download Vietnamese subtitles from [URL]"
- "Download thumbnail from [URL]"

## Parameters

| Parameter | Default | Options |
|-----------|---------|---------|
| URL | (required) | - |
| Type | video | video / audio / playlist / subtitle / thumbnail |
| Quality | best | best / 1080p / 720p / 480p / 360p |
| Format | mp4/mp3 | mp4 / webm / mkv / mp3 / m4a |

## Notes
- Playlist > 50 videos: ask user how many to download first
- Private content: use `--cookies-from-browser chrome`
- File > 50MB: report local save path to user
- See `references/platforms.md` for full platform list
