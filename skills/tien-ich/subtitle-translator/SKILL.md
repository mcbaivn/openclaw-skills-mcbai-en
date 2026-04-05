---
name: subtitle-translator
description: Translate SRT subtitle files into any target language using AI. Processes subtitles in batches to handle large files efficiently, preserves exact SRT format and timing, and outputs a new translated SRT file. Use this skill when the user wants to translate subtitles, translate an SRT file, translate movie subtitles, or asks to convert subtitles to another language. Triggers on phrases like "translate subtitles", "translate srt", "translate to Vietnamese", or when user uploads/pastes an SRT file and asks for translation.
---

# Subtitle Translator Skill

Translate SRT files into any language. Processes in batches, preserves SRT format and timing, outputs a new SRT file.

## Workflow

### Step 1: Gather inputs

Ask user if not provided:
1. **SRT file** - path to file or paste content directly
2. **Target language** - e.g.: "Vietnamese", "English", "Japanese" (default: Vietnamese)
3. **Batch size** - number of text lines per API call (default: 50, max: 100)
4. **Output path** - default: same folder as original file, append `_vi` or `_<lang>` to filename

### Step 2: Parse SRT file

Use `scripts/parse-srt.py` to read and parse the SRT file. Script auto-detects encoding:

**Supported encodings:**
- UTF-8, UTF-8 BOM, UTF-16 LE/BE, UTF-32
- GB18030 / GBK / GB2312 (Simplified Chinese)
- Big5 (Traditional Chinese)
- Shift-JIS, EUC-JP (Japanese)
- EUC-KR, CP949 (Korean)
- Windows-1252/1250/1251 (Latin/Central European/Cyrillic)
- Latin-1 (last resort, never fails)

**Detection order:**
1. BOM bytes (most accurate)
2. chardet library (if installed: `pip install chardet`)
3. Try each common encoding + validate with timecode pattern
4. Fallback latin-1

```python
# Each subtitle block:
{
  "id": 1,
  "timecode": "00:00:01,000 --> 00:00:03,000",
  "text": "Hello world"  # may be multi-line, joined with \n
}
```

Run:
```powershell
python scripts/parse-srt.py "path/to/file.srt"
# Output: JSON array to stdout (UTF-8)
# Detected encoding logged to stderr
```

### Step 3: Translate in batches

Split subtitle list into batches of `batch_size` lines. For each batch:

**System prompt:**
```
You are a professional subtitle translator for movies and cinema.
Your ABSOLUTE task is to translate subtitle lines into {targetLanguage}.
STRICT RULES:
1. EVERY word must be translated into {targetLanguage}.
2. DO NOT include any original language text in the output.
3. Use natural, cinematic, and emotional language suitable for {targetLanguage} culture.
4. Keep the exact same ID for each line.
5. If a line is untranslatable, provide a creative interpretation in {targetLanguage} instead of leaving it as is.
6. Return a valid JSON array only: [{"id": 1, "text": "translation"}]
```

**User message (per batch):**
```json
[
  {"id": 1, "text": "Hello world"},
  {"id": 2, "text": "How are you?"},
  ...
]
```

Call AI (using built-in LLM - no external API needed):
- Parse JSON response
- If parse error: retry batch once
- Map results back to subtitle objects by `id`

Report progress: `Translating batch {n}/{total}... ({percent}%)`

### Step 4: Build new SRT file

Use `scripts/build-srt.py` to reassemble into a complete SRT file:

```powershell
# Input: translated subtitles JSON array + original file for timecodes
python scripts/build-srt.py "original.srt" "translated.json" "output.srt"
```

Standard SRT format:
```
1
00:00:01,000 --> 00:00:03,000
Hello world

2
00:00:04,000 --> 00:00:06,000
How are you?

```

### Step 5: Report results

- Notify where output file was created
- Number of subtitle blocks translated
- Ask if user wants to review or edit

## Important Notes

- Preserve **all timecodes** - do not alter `-->` timestamps
- Blank lines between blocks are mandatory in SRT
- Subtitle text may be multi-line - join with `\n` when sending, split back when outputting
- HTML tags in subs (like `<i>`, `<b>`, `<font>`) - preserve them, only translate text inside
- If large file (>500 lines): estimate time for user before running

## Error Handling

- JSON parse error from AI: retry batch, if still fails keep original text and notify user
- Malformed SRT file: `scripts/parse-srt.py` will attempt recovery, report skipped lines
- Encoding: always read/write UTF-8
