# download-aio — Download Videos from 1000+ Platforms

> OpenClaw skill that automatically downloads video, audio, playlists, subtitles from YouTube, TikTok, Facebook, Instagram and 1000+ other platforms. After downloading, **automatically sends file to Telegram**.

---

## What is this skill for?

Want to save a great TikTok video? Download music from YouTube? Save an entire playlist? Before, you had to:
1. Use web converters → full of ads → low quality
2. Install apps → computer bloat
3. Copy complex yt-dlp commands → easy to get wrong

With this skill, just **paste the URL into chat** — the agent handles everything and sends the file straight to your Telegram.

---

## Features

| Feature | Details |
|---------|---------|
| 🎬 Download video | Best quality or choose 1080p / 720p / 480p / 360p |
| 🎵 Download audio | MP3 or M4A (no ffmpeg needed) |
| 📋 Download playlist | Full or limited quantity |
| 📝 Download subtitles | Auto-generated + official, multiple languages |
| 🖼️ Download thumbnail | High quality cover image |
| 📤 Auto send Telegram | Automatically sends files <= 50MB to chat |
| 🔧 Auto install | Script auto-installs Python, yt-dlp, ffmpeg |

---

## Supported Platforms

**Most popular:**

| Platform | Notes |
|----------|-------|
| YouTube | Video, Shorts, Live, Playlist, Channel |
| TikTok | Most without watermark |
| Facebook | Public video, Reel, Watch |
| Instagram | Public post, Reel (private requires login) |
| Twitter / X | Video tweets |
| Twitch | VOD, Clips |
| Vimeo | Full support |
| SoundCloud | Audio tracks |
| Reddit | Video posts |
| Bilibili | Chinese videos |

> Total support for **1000+ platforms**. See full list at [supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

---

## Installation

### Requirements
- Windows 10/11 (PowerShell)
- Python 3.10+ (script will prompt if not installed)
- OpenClaw installed

### Step 1 — Copy skill to OpenClaw

```powershell
Copy-Item -Recurse download-aio $env:USERPROFILE\.agents\skills\
```

### Step 2 — Run auto-install script

```powershell
powershell -ExecutionPolicy Bypass -File $env:USERPROFILE\.agents\skills\download-aio\scripts\install.ps1
```

The script will automatically:
- ✅ Check Python (prompts to install if missing)
- ✅ Install / update yt-dlp to latest version
- ✅ Install ffmpeg via Chocolatey (if available)
- ✅ Create `Downloads\yt-dlp\` directory

---

## Usage

### Simplest way

Just paste a URL into chat with the OpenClaw agent:

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Agent understands, downloads, sends file to your Telegram. Done.

### Advanced options

You can request more specifically in natural language:

```
Download audio mp3 from https://youtu.be/...

Download this playlist, first 10 videos only: https://youtube.com/playlist?list=...

Download video 720p from https://www.tiktok.com/@...

Download Vietnamese subtitles from https://youtu.be/...

Download thumbnail from https://www.facebook.com/reel/...
```

### Telegram send logic

| File size | Action |
|-----------|--------|
| <= 50MB | Automatically sends file to Telegram |
| > 50MB | Reports file location on machine, does not send |

---

## File Structure

```
download-aio/
├── README.md              ← You are reading this file
├── SKILL.md               ← Agent instructions (no need to read)
├── scripts/
│   ├── install.ps1        ← Auto-install all dependencies
│   ├── check.ps1          ← Quick check if everything is ready
│   └── find-python.ps1    ← Auto detect Python path on machine
└── references/
    ├── commands.md        ← Detailed yt-dlp commands for every use case
    ├── platforms.md       ← Platform list + specific notes
    └── troubleshooting.md ← Common error handling
```

---

## Troubleshooting

| Error | Fix |
|-------|-----|
| Python not found | Re-run `install.ps1`, install Python from [python.org](https://python.org) |
| HTTP 429 / Rate limit | Agent auto-adds delay, or use `--cookies-from-browser chrome` |
| Video requires login | Open Chrome, log in, agent uses `--cookies-from-browser chrome` |
| ffmpeg not found | Run `choco install ffmpeg` or download from [ffmpeg.org](https://ffmpeg.org) |
| File > 50MB | File saved at `Downloads\yt-dlp\`, agent reports the path |

---

## Update yt-dlp

Platforms change frequently, so update yt-dlp regularly:

```powershell
python -m pip install -U yt-dlp
```

---

<p align="center">
  <a href="https://www.mcbai.vn">MCB AI</a> &nbsp;·&nbsp;
  <a href="https://www.youtube.com/@mcbaivn">YouTube</a> &nbsp;·&nbsp;
  <a href="https://openclaw.mcbai.vn">OpenClaw Cheatsheet</a> &nbsp;·&nbsp;
  <a href="https://openclaw.mcbai.vn/openclaw101">OpenClaw 101 Course</a> &nbsp;·&nbsp;
  <a href="https://www.facebook.com/groups/openclawxvn">Facebook Community</a> &nbsp;·&nbsp;
  <a href="https://zalo.me/g/mmqkhi259">MCB AI Academy (Zalo)</a>
</p>
