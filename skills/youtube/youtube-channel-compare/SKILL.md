---
name: youtube-channel-compare
clawhub_id: mcbaivn-youtube-channel-compare
description: |
  Compare 2-5 YouTube channels by views, engagement rate, trending score
  and posting frequency. Generate benchmark reports with competitive analysis data.
---

# YouTube Channel Compare

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-channel-compare`

Compare performance of multiple YouTube channels and generate benchmark reports.

## Install

```bash
npx clawhub@latest install mcbaivn-youtube-channel-compare
```

## Usage

```
python scripts/compare_channels.py <url1> <url2> [url3...] [--limit N]
```

**Example:**
```
python scripts/compare_channels.py https://youtube.com/@MrBeast https://youtube.com/@PewDiePie --limit 20
```

## Output

| Metric | Channel A | Channel B |
|--------|-----------|-----------|
| Avg Views | ... | ... |
| Avg Likes | ... | ... |
| Avg Comments | ... | ... |
| Trending Score | ... | ... |
| Post Frequency | ... | ... |
| Engagement Rate | ... | ... |

**Trending Score**: `(Views x 0.6) + (Likes x 0.3) + (Comments x 0.1)` normalized 1-100

## Notes
- Default: 20 most recent videos per channel (use `--limit` to change)
- Channels without public stats will show N/A
