---
name: subtitle-translator
clawhub_id: mcbaivn-subtitle-translator
description: |
  Translate SRT subtitle files into any language using AI.
  Batch processing for large files, preserves exact SRT format and timing,
  outputs a new translated SRT file.
---

# Subtitle Translator

> 📦 **Install:** `npx clawhub@latest install mcbaivn-subtitle-translator`

Translate SRT files to any language. Batch processing, preserves format and timing.

## Install

```bash
npx clawhub@latest install mcbaivn-subtitle-translator
```

## Usage

```
Translate this subtitle to Vietnamese: [path/to/file.srt]
Translate this subtitle to English: [path/to/file.srt]
```

Or paste SRT content directly into chat and request translation.

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| Target language | Vietnamese | Any language |
| Batch size | 50 lines | Lines per AI call |
| Output | Same directory + `_vi` | Output filename |

## Workflow

1. **Parse** SRT file (auto-detect encoding: UTF-8, GBK, Shift-JIS, etc.)
2. **Batch** — 50 lines per batch, translate in parallel
3. **Build** — reassemble into proper SRT with original timecodes
4. **Export** `[original_name]_[lang].srt`

## Notes
- Preserves all original timecodes
- HTML tags (`<i>`, `<b>`) are kept, only text inside is translated
- Large files (>500 lines): report estimated time before running
