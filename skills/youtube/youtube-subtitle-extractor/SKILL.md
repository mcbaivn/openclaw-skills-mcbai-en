---
name: youtube-subtitle-extractor
clawhub_id: mcbaivn-youtube-subtitle-extractor
description: |
  Download subtitles (SRT/VTT/TXT) from YouTube videos using yt-dlp.
  Supports auto-generated and manual subtitles, multi-language.
---

# YouTube Subtitle Extractor

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-subtitle-extractor`

Download subtitles from YouTube videos or channels, export as clean `.srt` files.

## Install

```bash
npx clawhub@latest install mcbaivn-youtube-subtitle-extractor
```

## Usage

```
python scripts/extract_subtitles.py <video_or_channel_url> [--lang vi,en] [--format srt] [--auto]
```

**Examples:**
- Download subtitles: `python scripts/extract_subtitles.py https://youtu.be/xxxx`
- Vietnamese only: add `--lang vi`
- Auto-generated only: add `--auto`

## Output

```
Youtube_Subtitles/
  [Video_Title]/
    [title].vi.srt
    [title].en.srt
    [title]_plain.txt    (plain text without timestamps)
```

## Notes
- Prioritizes manual subtitles, falls back to auto-generated
- `_plain.txt` file is for use with `youtube-content-analyzer`
- For channel URLs: downloads subtitles for all videos (limit with `--limit N`)
