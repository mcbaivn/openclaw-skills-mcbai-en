---
name: youtube-scheduler
description: Analyze a YouTube channel's posting schedule from its 50 most recent videos to find golden posting times — days and hours with highest views and engagement. Use when user asks "Find best time to post for @Channel", "Best time to post for @Channel", "When does this channel usually post", or wants to optimize content posting schedule.
---

# ⏰ YouTube Scheduler Analyzer

Analyze a channel's posting schedule → find the days and hours with the highest performance.

## Usage

```
python scripts/analyze_schedule.py <channel_url> [--limit N] [--tz Asia/Ho_Chi_Minh]
```

**Examples:**
- `Find golden hours @MrBeast` → `python scripts/analyze_schedule.py https://youtube.com/@MrBeast --limit 50`
- Change timezone → `--tz Asia/Ho_Chi_Minh` (default UTC)

## Output

```
Youtube_Schedule/
└── [Channel]_schedule_DD_MM_YYYY.txt
```

**Report includes:**
- 📅 Best days of the week (sorted by avg views)
- ⏰ Golden time slots (0-23h, by avg views)
- 🗓️ Day × Hour heatmap (ASCII)
- 🏆 Top 5 highest-view videos with their posting day/time
- 💡 Optimal posting schedule recommendation

## Notes
- Analysis is based on the most recent `--limit` videos (recommended: 30-100 videos).
- Default timezone UTC; use `--tz` to convert to local time.
- Results are statistical estimates from historical data, not absolute guarantees.
