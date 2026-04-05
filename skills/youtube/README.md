# 🎬 YouTube

Skills for analyzing, extracting, and optimizing YouTube content — from downloading subtitles to analyzing posting schedules and comparing channels.

| Skill | Description |
|-------|-------------|
| [youtube-subtitle-extractor](youtube-subtitle-extractor/) | Download SRT/VTT subtitles from YouTube videos (auto-generated + manual, multilingual) |
| [youtube-content-analyzer](youtube-content-analyzer/) | Read SRT/TXT → summary, key points, tags, notable quotes |
| [youtube-channel-compare](youtube-channel-compare/) | Compare 2-5 channels: views, engagement, trending score, posting frequency |
| [youtube-scheduler](youtube-scheduler/) | Analyze 50 recent videos → find golden posting day/time, ASCII heatmap |

## Suggested Pipeline

```
youtube-subtitle-extractor → youtube-content-analyzer → content-writer
         
youtube-channel-compare  +  youtube-scheduler → optimize posting schedule
```

## Example Workflows

**Research competitor content:**
1. Use `youtube-channel-compare` → find the strongest channel in the niche
2. Use `youtube-subtitle-extractor` → download SRT of top videos from that channel
3. Use `youtube-content-analyzer` → analyze key points, quotes, structure
4. Use `content-writer` → create posts from insights gathered

**Optimize posting schedule:**
1. Use `youtube-scheduler` → analyze your own channel (or a competitor's)
2. View the heatmap → pick the golden time slot
3. Schedule posts following the recommendations

---
[← Back to home](../../README.md)
