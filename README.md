# OpenClaw Skills - MCBAI (English)

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

> **Extended Skills collection for OpenClaw** - curated and developed by [MCB AI](https://www.mcbai.vn)

> 🌍 **Also available in:** [🇻🇳 Vietnamese Version](https://github.com/mcbaivn/openclaw-skills-mcbai)

All skills are plug-and-play: install via ClawHub, copy to `~/.agents/skills/`, use immediately.

---

## ⚡ Install Skills

### Install individually (fastest, no git required)

```bash
npx clawhub@latest install mcbaivn-download-aio
npx clawhub@latest install mcbaivn-subtitle-translator
npx clawhub@latest install mcbaivn-youtube-subtitle-extractor
npx clawhub@latest install mcbaivn-youtube-content-analyzer
npx clawhub@latest install mcbaivn-youtube-channel-compare
npx clawhub@latest install mcbaivn-youtube-scheduler
npx clawhub@latest install mcbaivn-content-research
npx clawhub@latest install mcbaivn-content-writer
npx clawhub@latest install mcbaivn-facebook-page-manager
```

> Skills are automatically downloaded to `~/.agents/skills/` — no git knowledge required.

### Install all at once

```powershell
# Windows
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git
Copy-Item -Recurse openclaw-skills-mcbai-en\skills\*\* $env:USERPROFILE\.agents\skills\
```

```bash
# macOS / Linux
git clone https://github.com/mcbaivn/openclaw-skills-mcbai-en.git && \
cp -r openclaw-skills-mcbai-en/skills/*/* ~/.agents/skills/
```

---

## All Skills (9 skills)

| Skill | Description | Install | Category |
|-------|-------------|---------|----------|
| [download-aio](skills/tien-ich/download-aio/) | Download video/audio from 1000+ platforms | `npx clawhub@latest install mcbaivn-download-aio` | 🔧 Utilities |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Translate SRT subtitle files to any language (AI) | `npx clawhub@latest install mcbaivn-subtitle-translator` | 🔧 Utilities |
| [youtube-subtitle-extractor](skills/youtube/youtube-subtitle-extractor/) | Download SRT/VTT subtitles from YouTube | `npx clawhub@latest install mcbaivn-youtube-subtitle-extractor` | 🎬 YouTube |
| [youtube-content-analyzer](skills/youtube/youtube-content-analyzer/) | Read SRT/TXT → summary, key points, tags, quotes | `npx clawhub@latest install mcbaivn-youtube-content-analyzer` | 🎬 YouTube |
| [youtube-channel-compare](skills/youtube/youtube-channel-compare/) | Compare 2-5 channels: views, engagement, trending score | `npx clawhub@latest install mcbaivn-youtube-channel-compare` | 🎬 YouTube |
| [youtube-scheduler](skills/youtube/youtube-scheduler/) | Find golden posting hours, ASCII heatmap | `npx clawhub@latest install mcbaivn-youtube-scheduler` | 🎬 YouTube |
| [content-research](skills/content/content-research/) | Find trending articles & news (Brave + Tavily) | `npx clawhub@latest install mcbaivn-content-research` | ✍️ Content |
| [content-writer](skills/content/content-writer/) | Write multi-platform posts (6 formats, 8 tones, EN/VI) | `npx clawhub@latest install mcbaivn-content-writer` | ✍️ Content |
| [facebook-page-manager](skills/social-media/facebook-page-manager/) | Auto-post & manage Facebook Page content | `npx clawhub@latest install mcbaivn-facebook-page-manager` | 📱 Social Media |

> 🔄 Updated regularly. **Star the repo** to stay notified!

---

## Skills by Category

### 🔧 Utilities

| Skill | Description | Install |
|-------|-------------|---------|
| [download-aio](skills/tien-ich/download-aio/) | Download video/audio from 1000+ platforms (YouTube, TikTok, Facebook...) | `npx clawhub@latest install mcbaivn-download-aio` |
| [subtitle-translator](skills/tien-ich/subtitle-translator/) | Translate SRT subtitle files, auto-detect encoding, any language | `npx clawhub@latest install mcbaivn-subtitle-translator` |

---

### 🎬 YouTube

> [→ Detailed YouTube category guide](skills/youtube/README.md)

| Skill | Description | When to use | Install |
|-------|-------------|-------------|---------|
| [youtube-subtitle-extractor](skills/youtube/youtube-subtitle-extractor/) | Download SRT/VTT/TXT from YouTube | Need subtitle files for translation or analysis | `npx clawhub@latest install mcbaivn-youtube-subtitle-extractor` |
| [youtube-content-analyzer](skills/youtube/youtube-content-analyzer/) | Read SRT/TXT → summary, key points, tags, quotes | Understand video content without watching | `npx clawhub@latest install mcbaivn-youtube-content-analyzer` |
| [youtube-channel-compare](skills/youtube/youtube-channel-compare/) | Compare 2-5 channels by views, engagement, trending score | Competitor research, find top channels in niche | `npx clawhub@latest install mcbaivn-youtube-channel-compare` |
| [youtube-scheduler](skills/youtube/youtube-scheduler/) | Analyze posting schedule → find golden hours + ASCII heatmap | Optimize video posting time | `npx clawhub@latest install mcbaivn-youtube-scheduler` |

**Suggested pipeline:**
```
youtube-subtitle-extractor → youtube-content-analyzer → content-writer
youtube-channel-compare + youtube-scheduler → optimize posting schedule
```

---

### ✍️ Content

| Skill | Description | Install |
|-------|-------------|---------|
| [content-research](skills/content/content-research/) | Find trending articles & news from the web (Brave + Tavily in parallel) | `npx clawhub@latest install mcbaivn-content-research` |
| [content-writer](skills/content/content-writer/) | Write posts for LinkedIn, Facebook, Twitter/X, TikTok, Threads | `npx clawhub@latest install mcbaivn-content-writer` |

**Suggested pipeline:**
```
content-research → content-writer → facebook-page-manager
```

---

### 📱 Social Media

| Skill | Description | Install |
|-------|-------------|---------|
| [facebook-page-manager](skills/social-media/facebook-page-manager/) | Post text/photo/video/Reels/Story, schedule, manage comments on Facebook Page | `npx clawhub@latest install mcbaivn-facebook-page-manager` |

---

## Repository Structure

```
openclaw-skills-mcbai-en/
├── README.md
└── skills/
    ├── tien-ich/          🔧 Utilities
    │   ├── download-aio/
    │   └── subtitle-translator/
    ├── youtube/           🎬 YouTube
    │   ├── README.md
    │   ├── youtube-subtitle-extractor/
    │   ├── youtube-content-analyzer/
    │   ├── youtube-channel-compare/
    │   └── youtube-scheduler/
    ├── content/           ✍️ Content
    │   ├── content-research/
    │   ├── content-writer/
    └── social-media/      📱 Social Media
        └── facebook-page-manager/
```

---

## About MCB AI

| | |
|--|--|
| 🌐 Website | [mcbai.vn](https://www.mcbai.vn/) |
| 📘 Fanpage | [facebook.com/mcb.ai.vn](https://www.facebook.com/mcb.ai.vn/) |
| 🎬 YouTube | [youtube.com/@mcbaivn](https://www.youtube.com/@mcbaivn) |
| 🗒️ OpenClaw Cheatsheet | [openclaw.mcbai.vn](https://openclaw.mcbai.vn/) |
| 📚 OpenClaw 101 Course | [openclaw.mcbai.vn/openclaw101](https://openclaw.mcbai.vn/openclaw101) |
| 💬 Facebook Community | [OpenClaw AI](https://www.facebook.com/groups/openclawxvn) |
| 🎓 MCB AI Academy (Zalo) | [zalo.me/g/mmqkhi259](https://zalo.me/g/mmqkhi259) |

---

## Contributing

Have a great skill to share? Open a Pull Request or contact us via the MCB AI Fanpage.

---

<p align="center">Made with ❤️ by <a href="https://www.mcbai.vn">MCB AI</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/@mcbaivn">YouTube</a> &nbsp;·&nbsp; <a href="https://openclaw.mcbai.vn/openclaw101">OpenClaw 101</a> &nbsp;·&nbsp; <a href="https://zalo.me/g/mmqkhi259">MCB AI Academy</a></p>
