# OpenClaw Skills - MCBAI (English)

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

> **Extended Skills collection for OpenClaw** - curated and developed by [MCB AI](https://www.mcbai.vn)

> 🌍 **Also available in:** [🇻🇳 Vietnamese Version](https://github.com/mcbaivn/openclaw-skills-mcbai)

All skills are plug-and-play: download, copy to `~/.agents/skills/`, use immediately.
A skill can belong to multiple categories.

---

## ⚡ Install Skills

### Install individual skills via ClawhHub (easiest)

```bash
npx clawhub@latest install youtube-content-analyzer
npx clawhub@latest install youtube-channel-compare
npx clawhub@latest install youtube-scheduler
npx clawhub@latest install youtube-subtitle-extractor
npx clawhub@latest install download-aio
npx clawhub@latest install subtitle-translator-mcbai
npx clawhub@latest install content-research-mcbai
npx clawhub@latest install content-writer-mcbai
npx clawhub@latest install facebook-management-skills-by-mcbai
```

> Skills are automatically downloaded to `~/.agents/skills/` — no git required.

### Install all at once (clone repo)

```powershell
# Windows
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git && `
Copy-Item -Recurse openclaw-skills-mcbai-en\skills\*\* $env:USERPROFILE\.agents\skills\
```

```bash
# macOS / Linux
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git && \
cp -r openclaw-skills-mcbai-en/skills/*/* ~/.agents/skills/
```

---

## All Skills

| Skill | Description | Category |
|-------|-------------|----------|
| [download-aio](skills/tien-ich/download-aio/) | Download video/audio from 1000+ platforms | 🔧 Utilities · 📱 Social Media · 🎬 YouTube |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Translate SRT subtitle files to any language (AI cinematic) | 🔧 Utilities · 📱 Social Media · 🎬 YouTube |
| [content-research](skills/content/content-research/) | Find trending articles & news (Brave + Tavily) | ✍️ Content · 📱 Social Media |
| [content-writer](skills/content/content-writer/) | Write multi-platform posts (6 formats, 8 tones, EN/VI) | ✍️ Content · 📱 Social Media |
| [youtube-subtitle-extractor](skills/youtube/youtube-subtitle-extractor/) | Download SRT/VTT subtitles from YouTube (auto + manual, multilingual) | 🎬 YouTube · 🔧 Utilities |
| [youtube-content-analyzer](skills/youtube/youtube-content-analyzer/) | Read SRT/TXT → summary, key points, tags, notable quotes | 🎬 YouTube · ✍️ Content |
| [youtube-channel-compare](skills/youtube/youtube-channel-compare/) | Compare 2-5 channels: views, engagement, trending score, posting frequency | 🎬 YouTube · 📊 Analytics |
| [youtube-scheduler](skills/youtube/youtube-scheduler/) | Analyze 50 recent videos → find golden posting time + ASCII heatmap | 🎬 YouTube · 📊 Analytics |
| [facebook-page-manager](skills/social-media/facebook-page-manager/) | Auto-post & manage Facebook Page: text/photo/video/Reels/Story, schedule, comments | 📱 Social Media |

> 🔄 Updated regularly. **Star this repo** to stay updated!

---

## Skills by Category

### 🔧 Utilities
*Tools to support daily work*

| Skill | Description |
|-------|-------------|
| [download-aio](skills/tien-ich/download-aio/) | Download video/audio from 1000+ platforms (YouTube, TikTok, Facebook...) |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Translate SRT subtitle files, auto-detect encoding, supports all languages |
| [youtube-subtitle-extractor](skills/youtube/youtube-subtitle-extractor/) | Download SRT/VTT/TXT subtitles from YouTube (auto-generated + manual) |

---

### ✍️ Content
*Research, writing, content creation*

| Skill | Description |
|-------|-------------|
| [content-research](skills/content/content-research/) | Find trending articles & news from web (Brave + Tavily in parallel) |
| [content-writer](skills/content/content-writer/) | Write posts for LinkedIn, Facebook, Twitter/X, TikTok, Threads |
| [youtube-content-analyzer](skills/youtube/youtube-content-analyzer/) | Analyze SRT/TXT → content summary, key points, suggested tags, notable quotes |

---

### 📱 Social Media
*Manage and optimize content across platforms*

| Skill | Description | Install |
|-------|-------------|---------|
| [download-aio](skills/tien-ich/download-aio/) | Download videos/reels/shorts from any platform | `npx clawhub@latest install download-aio` |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Translate video subtitles before posting to social media | `npx clawhub@latest install subtitle-translator-mcbai` |
| [content-research](skills/content/content-research/) | Find trending content to write about | `npx clawhub@latest install content-research-mcbai` |
| [content-writer](skills/content/content-writer/) | Write Facebook posts, LinkedIn articles, TikTok captions... | `npx clawhub@latest install content-writer-mcbai` |
| [facebook-page-manager](skills/social-media/facebook-page-manager/) | Post text/photo/video/Reels/Story, schedule posts, manage comments on Facebook Page | `npx clawhub@latest install facebook-management-skills-by-mcbai` |

---

### 🔵 Facebook

| Skill | Description | When to use | Install |
|-------|-------------|-------------|---------|
| [facebook-page-manager](skills/social-media/facebook-page-manager/) | Post text/photo/video/Reels/Story to Fanpage | Auto-post content to Facebook Page | `npx clawhub@latest install facebook-management-skills-by-mcbai` |
| [facebook-page-manager](skills/social-media/facebook-page-manager/) | Schedule posts with exact time | Plan content calendar in advance | `npx clawhub@latest install facebook-management-skills-by-mcbai` |
| [facebook-page-manager](skills/social-media/facebook-page-manager/) | Manage comments & auto-reply | Engage with audience via API | `npx clawhub@latest install facebook-management-skills-by-mcbai` |

**Suggested pipeline:**
```
content-research → content-writer → facebook-page-manager (post + schedule)
```

---

### 🎬 YouTube
*Tools built specifically for YouTube creators*

> [→ See detailed YouTube category guide](skills/youtube/README.md)

| Skill | Description | When to use |
|-------|-------------|-------------|
| [youtube-subtitle-extractor](skills/youtube/youtube-subtitle-extractor/) | Download SRT/VTT subtitles from YouTube | Need subtitle files for translation or analysis |
| [youtube-content-analyzer](skills/youtube/youtube-content-analyzer/) | Read SRT/TXT → summary, key points, tags, quotes | Want to understand video content without watching |
| [youtube-channel-compare](skills/youtube/youtube-channel-compare/) | Compare 2-5 channels by views, engagement, trending score | Research competitors, find strong channels in niche |
| [youtube-scheduler](skills/youtube/youtube-scheduler/) | Analyze posting schedule → find golden hours + ASCII heatmap | Want to optimize video posting time |
| [download-aio](skills/tien-ich/download-aio/) | Download YouTube videos, playlists, audio, subtitles | Need to download content locally |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Translate English subtitles to Vietnamese (and vice versa) | Translate SRT after downloading |

**Suggested pipeline:**
```
youtube-subtitle-extractor → youtube-content-analyzer → content-writer
youtube-channel-compare + youtube-scheduler → optimize posting schedule
```

---

### 📊 Analytics
*Data analysis, performance measurement*

| Skill | Description |
|-------|-------------|
| [youtube-channel-compare](skills/youtube/youtube-channel-compare/) | Compare metrics of 2-5 channels: views, likes, comments, trending score, posting frequency |
| [youtube-scheduler](skills/youtube/youtube-scheduler/) | Heatmap of optimal video posting days/times based on last 50 videos |

---

## Installation

### Install All Skills (fastest)

```powershell
# Windows
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git && `
Copy-Item -Recurse openclaw-skills-mcbai-en\skills\*\* $env:USERPROFILE\.agents\skills\
```

```bash
# macOS / Linux
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git && \
cp -r openclaw-skills-mcbai-en/skills/*/* ~/.agents/skills/
```

### Install a Single Skill

#### Step 1 - Clone repo
```powershell
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git
```

#### Step 2 - Copy skill to OpenClaw
```powershell
# Windows - example: install youtube-content-analyzer
Copy-Item -Recurse openclaw-skills-mcbai-en\skills\youtube\youtube-content-analyzer $env:USERPROFILE\.agents\skills\

# macOS / Linux
cp -r openclaw-skills-mcbai-en/skills/youtube/youtube-content-analyzer ~/.agents/skills/
```

> The skill can be in any folder - just copy the skill folder directly into `~/.agents/skills/`

### Step 3 - Install dependencies (if needed)
```powershell
powershell -ExecutionPolicy Bypass -File $env:USERPROFILE\.agents\skills\<skill-name>\scripts\install.ps1
```

### Step 4 - Use it!
Open chat with your OpenClaw agent and invoke the skill following the README in each skill folder.

---

## Repository Structure

```
openclaw-skills-mcbai-en/
├── README.md
└── skills/
    ├── tien-ich/                     🔧 Utilities
    │   ├── download-aio/
    │   └── subtitle-translator/
    ├── content/                      ✍️ Content
    │   ├── content-research/
    │   └── content-writer/
    ├── youtube/                      🎬 YouTube
    │   ├── README.md
    │   ├── youtube-subtitle-extractor/
    │   ├── youtube-content-analyzer/
    │   ├── youtube-channel-compare/
    │   └── youtube-scheduler/
    └── social-media/                 📱 Social Media
        └── facebook-page-manager/
```

> **Note:** Skills are placed in folders by primary category. A skill can belong to multiple categories (see table above).
> `SKILL.md` is the file OpenClaw reads to control the agent - you only need to read `README.md`.

---

## About MCB AI

| | |
|--|--|
| 🌐 Website | [mcbai.vn](https://www.mcbai.vn/) |
| 📘 Facebook | [facebook.com/mcb.ai.vn](https://www.facebook.com/mcb.ai.vn/) |
| 🎬 YouTube | [youtube.com/@mcbaivn](https://www.youtube.com/@mcbaivn) |
| 🗒️ OpenClaw Cheatsheet | [openclaw.mcbai.vn](https://openclaw.mcbai.vn/) |
| 📚 OpenClaw 101 Course | [openclaw.mcbai.vn/openclaw101](https://openclaw.mcbai.vn/openclaw101) |
| 💬 Facebook Community | [OpenClaw AI Kiếm Cơm](https://www.facebook.com/groups/openclawxvn) |
| 🎓 MCB AI Academy (Zalo) | [zalo.me/g/mmqkhi259](https://zalo.me/g/mmqkhi259) |

---

## Contributing

Have a great skill to share? Create a Pull Request or contact us via MCB AI Fanpage.

---

<p align="center">Made with ❤️ by <a href="https://www.mcbai.vn">MCB AI</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/@mcbaivn">YouTube</a> &nbsp;·&nbsp; <a href="https://openclaw.mcbai.vn/openclaw101">OpenClaw 101</a> &nbsp;·&nbsp; <a href="https://zalo.me/g/mmqkhi259">MCB AI Academy</a></p>

