---
name: youtube-subtitle-extractor
description: Download subtitles (SRT/VTT/TXT) from YouTube videos using yt-dlp. Supports auto-generated and manual subtitles, multilingual. Use when user asks "Download subtitles for video X", "Get subtitles from [URL]", "Extract SRT from @Channel", or needs subtitle files for content analysis.
---

# 📥 YouTube Subtitle Extractor

Download subtitles from YouTube videos or entire channels, output clean `.srt` files.

## Installation

### Option 1 — Download directly from GitHub (recommended)

```powershell
# Windows
$skillDir = "$env:USERPROFILE\.agents\skills\youtube-subtitle-extractor"
New-Item -ItemType Directory -Force "$skillDir\scripts" | Out-Null
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-subtitle-extractor/SKILL.md" -OutFile "$skillDir\SKILL.md"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-subtitle-extractor/scripts/extract_subtitles.py" -OutFile "$skillDir\scripts\extract_subtitles.py"
```

```bash
# macOS / Linux
mkdir -p ~/.agents/skills/youtube-subtitle-extractor/scripts
curl -o ~/.agents/skills/youtube-subtitle-extractor/SKILL.md \
  https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-subtitle-extractor/SKILL.md
curl -o ~/.agents/skills/youtube-subtitle-extractor/scripts/extract_subtitles.py \
  https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-subtitle-extractor/scripts/extract_subtitles.py
```

### Option 2 — Clone full repo

```powershell
# Windows
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git
Copy-Item -Recurse openclaw-skills-mcbai-en\skills\youtube\youtube-subtitle-extractor $env:USERPROFILE\.agents\skills\
```

```bash
# macOS / Linux
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git
cp -r openclaw-skills-mcbai-en/skills/youtube/youtube-subtitle-extractor ~/.agents/skills/
```

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
    └── [title]_plain.txt    (plain text without timestamps)
```

## Notes
- Prioritizes manual subtitles first, falls back to auto-generated if unavailable.
- The `_plain.txt` file is used by `youtube-content-analyzer`.
- If URL is a channel, downloads subtitles for all videos (limit with `--limit N`).
