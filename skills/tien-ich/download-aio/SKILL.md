---
name: download-aio
description: Download videos, audio, playlists, subtitles, and thumbnails from ANY platform (YouTube, TikTok, Instagram, Facebook, Twitter/X, Twitch, Vimeo, SoundCloud, Reddit, and 1000+ more) using yt-dlp. After download, automatically send file to Telegram if under 50MB. Use this skill when the user wants to download video, audio, playlist, reel, short, clip, subtitle, or thumbnail from any website or social media platform. Triggers on phrases like "tải video", "download video", "tải nhạc", "download audio", "tải playlist", "download từ YouTube/TikTok/Facebook/Instagram", "lưu video", "save video", or when user pastes a URL from a video platform.
---

# 📥 Download AIO

Tải video, audio, playlist, subtitle, thumbnail từ 1000+ nền tảng. Tự động gửi file về Telegram nếu ≤ 50MB.

## Cài đặt

```bash
npx clawhub@latest install download-aio
```

> Sau khi cài, chạy script setup dependencies lần đầu:
> ```powershell
> powershell -ExecutionPolicy Bypass -File $env:USERPROFILE\.agents\skills\download-aio\scripts\install.ps1
> ```
> Script tự động cài: Python check, yt-dlp, ffmpeg.

## Cách dùng

Chỉ cần paste URL vào chat:
```
https://www.youtube.com/watch?v=...
https://www.tiktok.com/@user/video/...
https://www.facebook.com/reel/...
```

Agent sẽ tự tải về + gửi vào Telegram.

### Tùy chỉnh nâng cao
- "Tải audio mp3 từ [URL]"
- "Tải playlist này, chỉ lấy 10 video đầu: [URL]"
- "Tải video 720p từ [URL]"
- "Tải phụ đề tiếng Việt từ [URL]"
- "Tải thumbnail từ [URL]"

## Workflow

| Tham số | Default | Tùy chọn |
|---------|---------|-----------|
| URL | (bắt buộc) | - |
| Loại tải | video | video / audio / playlist / subtitle / thumbnail |
| Chất lượng | best | best / 1080p / 720p / 480p / 360p |
| Format | mp4/mp3 | mp4 / webm / mkv / mp3 / m4a |

## Lưu ý
- Playlist > 50 video: hỏi user muốn tải bao nhiêu trước
- Nội dung private: dùng `--cookies-from-browser chrome`
- File > 50MB: báo user đường dẫn lưu trên máy
- Xem `references/platforms.md` cho danh sách nền tảng đầy đủ
