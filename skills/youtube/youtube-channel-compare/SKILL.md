---
name: youtube-channel-compare
description: Compare 2-5 YouTube channels by views, engagement rate, trending score, and posting frequency. Use when user asks "Compare @ChannelA vs @ChannelB", "Which channel is stronger in niche X", or needs competitive analysis data.
---

# 📊 YouTube Channel Compare

Compare performance metrics across multiple YouTube channels and generate benchmark reports.

## Usage

```
python scripts/compare_channels.py <url1> <url2> [url3...] [--limit N]
```

**Example:**
- `Compare @MrBeast vs @PewDiePie` → `python scripts/compare_channels.py https://youtube.com/@MrBeast https://youtube.com/@PewDiePie --limit 20`

## Output

```
Youtube_Compare/
└── compare_[Chan1]_vs_[Chan2]_DD_MM_YYYY.txt
```

**Report includes:**

| Metric | Channel A | Channel B |
|--------|-----------|-----------|
| Avg Views | ... | ... |
| Avg Likes | ... | ... |
| Avg Comments | ... | ... |
| Avg Trending Score | ... | ... |
| Posting Frequency | ... | ... |
| Engagement Rate | ... | ... |

**Trending Score**: `(Views x 0.6) + (Likes x 0.3) + (Comments x 0.1)` normalized 1-100

## Notes
- Default fetches 20 most recent videos per channel (`--limit` to change).
- Channels without public stats will show N/A.
