---
name: youtube-content-analyzer
description: Analyze YouTube video content from SRT/VTT/TXT files or direct URL. Summarize content, extract key points, analyze main topics, generate reports. Use when user requests "Summarize video X", "Analyze content from SRT", "Key points from [URL]", "Read video content without watching", or needs to quickly understand large batches of videos.
---

# 📊 YouTube Content Analyzer

Read subtitles → summarize content, key points, topic analysis. No need to watch the video.

## Workflow

**Method 1 - From existing SRT/TXT file:**
```
python scripts/analyze_content.py --file path/to/subtitle.srt
```

**Method 2 - From URL (auto-download subtitle then analyze):**
```
python scripts/analyze_content.py --url https://youtu.be/xxxx [--lang vi]
```

**Method 3 - Batch analysis:**
```
python scripts/analyze_content.py --folder Youtube_Subtitles/ChannelName/
```

## Output

```
Youtube_Analysis/
└── [Channel]/
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
- See `references/analysis-prompt.md` to customize the analysis prompt.
