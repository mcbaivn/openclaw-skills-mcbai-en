---
name: youtube-channel-compare
clawhub_id: mcbaivn-youtube-channel-compare
description: |
  Compare 2-5 YouTube channels by views, engagement rate, trending score, and posting frequency. Use when user asks "Compare @ChannelA vs @ChannelB", "Which channel is stronger in niche X", or needs competitive analysis data.
---

# 📊 YouTube Channel Compare

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-channel-compare`

Compare performance metrics across multiple YouTube channels and generate benchmark reports.

## Installation

### Option 1 — Download directly from GitHub (recommended)

```powershell
# Windows

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-channel-compare`
$skillDir = "$env:USERPROFILE\.agents\skills\youtube-channel-compare"
New-Item -ItemType Directory -Force "$skillDir\scripts" | Out-Null
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-channel-compare/SKILL.md" -OutFile "$skillDir\SKILL.md"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-channel-compare/scripts/compare_channels.py" -OutFile "$skillDir\scripts\compare_channels.py"
```

```bash
# macOS / Linux

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-channel-compare`
mkdir -p ~/.agents/skills/youtube-channel-compare/scripts
curl -o ~/.agents/skills/youtube-channel-compare/SKILL.md \
  https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-channel-compare/SKILL.md
curl -o ~/.agents/skills/youtube-channel-compare/scripts/compare_channels.py \
  https://raw.githubusercontent.com/mcbaivn/openclaw-skills-mcbai-en/main/skills/youtube/youtube-channel-compare/scripts/compare_channels.py
```

### Option 2 — Clone full repo

```powershell
# Windows

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-channel-compare`
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git
Copy-Item -Recurse openclaw-skills-mcbai-en\skills\youtube\youtube-channel-compare $env:USERPROFILE\.agents\skills\
```

```bash
# macOS / Linux

> 📦 **Install:** `npx clawhub@latest install mcbaivn-youtube-channel-compare`
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git
cp -r openclaw-skills-mcbai-en/skills/youtube/youtube-channel-compare ~/.agents/skills/
```

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
| Trending Score | ... | ... |
| Posting Frequency | ... | ... |
| Engagement Rate | ... | ... |

**Trending Score**: `(Views × 0.6) + (Likes × 0.3) + (Comments × 0.1)` normalized 1-100

## Notes
- Default fetches 20 most recent videos per channel (use `--limit` to change).
- Channels without public stats will show N/A.
