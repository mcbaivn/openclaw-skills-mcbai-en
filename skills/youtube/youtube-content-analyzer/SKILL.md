---
name: youtube-content-analyzer
description: Analyze YouTube video content from SRT/VTT/TXT files or direct URL. Summarize content, extract key points, analyze main topics, generate reports. Use when user requests "Summarize video X", "Analyze content from SRT", "Key points from [URL]", "Read video content without watching", or needs to quickly understand large batches of videos.
---

# 🤖 YouTube Content Analyzer

Read subtitles → summarize content, key points, topic analysis. No need to watch the video.

## Installation

### Option 1 — Download directly from GitHub (recommended)

```powershell
# Windows
$skillDir = "$env:USERPROFILE\.agents\skills\youtube-content-analyzer"
New-Item -ItemType Directory -Force "$skillDir\scripts" | Out-Null
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-content-analyzer/SKILL.md" -OutFile "$skillDir\SKILL.md"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-content-analyzer/scripts/analyze_content.py" -OutFile "$skillDir\scripts\analyze_content.py"
```

```bash
# macOS / Linux
mkdir -p ~/.agents/skills/youtube-content-analyzer/scripts
curl -o ~/.agents/skills/youtube-content-analyzer/SKILL.md \
  https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-content-analyzer/SKILL.md
curl -o ~/.agents/skills/youtube-content-analyzer/scripts/analyze_content.py \
  https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-content-analyzer/scripts/analyze_content.py
```

### Option 2 — Clone full repo

```powershell
# Windows
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git
Copy-Item -Recurse openclaw-skills-mcbai-en\skills\youtube\youtube-content-analyzer $env:USERPROFILE\.agents\skills\
```

```bash
# macOS / Linux
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git
cp -r openclaw-skills-mcbai-en/skills/youtube/youtube-content-analyzer ~/.agents/skills/
```

## Workflow

**Method 1 - From existing SRT/TXT file:**
```
python scripts/analyze_content.py --file path/to/subtitle.srt
```

**Method 2 - From URL (auto-download subtitle then analyze):**
```
python scripts/analyze_content.py --url https://youtu.be/xxxx [--lang en]
```

**Method 3 - Batch analysis:**
```
python scripts/analyze_content.py --folder Youtube_Subtitles/ChannelName/
```

## Output

```
Youtube_Analysis/
└── [Video_Title]_analysis_DD_MM_YYYY.txt
```

**Each analysis file includes:**
- 📝 **Summary** (3-5 sentences)
- 🔑 **Key Points** (bullet list)
- 🏷️ **Main Topics** (tags)
- 💬 **Notable Quotes**
- 📊 **Stats**: length, language, information density

## Notes
- For long videos (>30 min), the script splits into chunks before analyzing.
- Combine with `youtube-subtitle-extractor` for a complete pipeline.
