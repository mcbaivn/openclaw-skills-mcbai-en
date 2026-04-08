---
name: youtube-content-analyzer
clawhub_id: mcbaivn-youtube-content-analyzer
description: |
  Analyze YouTube video content from SRT/VTT/TXT files or direct URL.
  Summarize content, extract key points, analyze main topics, generate reports.
---

# YouTube Content Analyzer

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-content-analyzer`

Read subtitles, summarize content, extract key points, analyze topics. No need to watch the video.

## Install

```bash
npx clawhub@latest install mcbaivn-youtube-content-analyzer
```

## Workflow

**Option 1 — From existing SRT/TXT file:**
```
python scripts/analyze_content.py --file path/to/subtitle.srt
```

**Option 2 — From URL (auto-download subtitle then analyze):**
```
python scripts/analyze_content.py --url https://youtu.be/xxxx [--lang vi]
```

**Option 3 — Batch analysis:**
```
python scripts/analyze_content.py --folder Youtube_Subtitles/ChannelName/
```

## Output

Each analysis file includes:
- **Summary** (3-5 sentences)
- **Key Points** (bullet list)
- **Main Topics** (tags)
- **Notable Quotes**
- **Stats**: duration, language, information density

## Notes
- Long videos (>30 min): script splits into chunks before analysis
- Combine with `youtube-subtitle-extractor` for a complete pipeline
