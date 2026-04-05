---
name: youtube-subtitle-extractor
description: Download subtitles (SRT/VTT/TXT) from YouTube videos using yt-dlp. Supports auto-generated and manual subtitles, multilingual. Use when user asks "Download subtitles for video X", "Get subtitles from [URL]", "Extract SRT from @Channel", or needs subtitle files for content analysis.
---

# 📥 YouTube Subtitle Extractor

Download subtitles from YouTube videos or entire channels, output clean `.srt` files.

## Usage

```
python scripts/extract_subtitles.py <video_or_channel_url> [--lang vi,en] [--format srt] [--auto]
```

**Examples:**
- `Get subtitles from https://youtu.be/xxxx` → `python scripts/extract_subtitles.py https://youtu.be/xxxx`
- `Download Vietnamese subtitles` → add `--lang vi`
- Auto-generated only → add `--auto`

## Output

```
Youtube_Subtitles/
└── [Video_Title]/
    ├── [title].vi.srt
    ├── [title].en.srt
    └── [title]_plain.txt    plain text without timestamps
```

## Notes
- Prioritizes manual subtitles first, falls back to auto-generated if unavailable.
- The `_plain.txt` file is used by youtube-content-analyzer.
- If URL is a channel, downloads subtitles for all videos in channel (limit with `--limit N`).
