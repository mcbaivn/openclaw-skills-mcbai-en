---
name: youtube-scheduler
clawhub_id: mcbaivn-youtube-scheduler
description: |
  Analyze a YouTube channel's posting schedule from its 50 most recent videos to find golden posting times - days and hours with highest views and engagement. Use when user asks "Find best time to post for @Channel", "Best time to post for @Channel", "When does this channel usually post", or wants to optimize content posting schedule.
---

# ⏰ YouTube Scheduler Analyzer

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-scheduler`

Analyze a channel's posting schedule → find the days and hours with the highest performance.

## Installation

### Option 1 — Download directly from GitHub (recommended)

```powershell
# Windows

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-scheduler`
$skillDir = "$env:USERPROFILE\.agents\skills\youtube-scheduler"
New-Item -ItemType Directory -Force "$skillDir\scripts" | Out-Null
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-scheduler/SKILL.md" -OutFile "$skillDir\SKILL.md"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-scheduler/scripts/analyze_schedule.py" -OutFile "$skillDir\scripts\analyze_schedule.py"
```

```bash
# macOS / Linux

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-scheduler`
mkdir -p ~/.agents/skills/youtube-scheduler/scripts
curl -o ~/.agents/skills/youtube-scheduler/SKILL.md \
  https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-scheduler/SKILL.md
curl -o ~/.agents/skills/youtube-scheduler/scripts/analyze_schedule.py \
  https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-scheduler/scripts/analyze_schedule.py
```

### Option 2 — Clone full repo

```powershell
# Windows

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-scheduler`
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git
Copy-Item -Recurse openclaw-skills-mcbai-en\skills\youtube\youtube-scheduler $env:USERPROFILE\.agents\skills\
```

```bash
# macOS / Linux

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-scheduler`
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git
cp -r openclaw-skills-mcbai-en/skills/youtube/youtube-scheduler ~/.agents/skills/
```

## Usage

```
python scripts/analyze_schedule.py <channel_url> [--limit N] [--tz America/New_York]
```

**Examples:**
- `Find golden hours @MrBeast` → `python scripts/analyze_schedule.py https://youtube.com/@MrBeast --limit 50`
- Change timezone → add `--tz America/New_York` (default UTC)

## Output

```
Youtube_Schedule/
└── [Channel]_schedule_DD_MM_YYYY.txt
```

**Report includes:**
- 📅 Best days of the week (sorted by avg views)
- ⏰ Golden time slots (0-23h, by avg views)
- 🗺️ Day × Hour heatmap (ASCII)
- 🏆 Top 5 highest-view videos with their posting day/time
- 💡 Optimal posting schedule recommendation

## Notes
- Analysis is based on the most recent `--limit` videos (recommended: 30-100 videos).
- Default timezone UTC; use `--tz` to convert to local time.
- Results are statistical estimates from historical data, not absolute guarantees.
