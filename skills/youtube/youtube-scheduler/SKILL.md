---
name: youtube-scheduler
clawhub_id: mcbaivn-youtube-scheduler
description: |
  Analyze a YouTube channel posting schedule to find golden hours
  with the highest views and engagement. Optimize your content publishing schedule.
---

# YouTube Scheduler Analyzer

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-scheduler`

Analyze channel posting schedule to find the best days and hours for maximum performance.

## Install

```bash
npx clawhub@latest install mcbaivn-youtube-scheduler
```

## Usage

```
python scripts/analyze_schedule.py <channel_url> [--limit N] [--tz Asia/Ho_Chi_Minh]
```

**Example:**
```
python scripts/analyze_schedule.py https://youtube.com/@MrBeast --limit 50
```

## Report Includes

- Best day of week (sorted by avg views)
- Golden hours (0-23h, by avg views)
- Day x Hour Heatmap (ASCII)
- Top 5 highest-view videos with posting day/time
- Optimized posting schedule recommendation

## Notes
- Analyzes the `--limit` most recent videos (recommended: 30-100)
- Default timezone is UTC, use `--tz` for local time
- Results are statistical estimates from historical data
