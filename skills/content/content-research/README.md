# content-research — Find Trending Articles & News

> OpenClaw skill that automatically searches for articles, news, and content sources on any topic from the web. Uses **Brave Search + Tavily** in parallel for the richest results. Typically used before `content-writer` to prepare source material.

---

## What is this skill for?

Before writing a great LinkedIn post, you need quality source material. This skill helps you:
- Quickly find 10-15 latest articles on any topic
- Filter by source type: news, blog, LinkedIn, YouTube
- Auto-tag results (AI, Funding, SaaS, Startup...) for easy selection
- Combine 2 search engines (Brave + Tavily) to never miss good articles

---

## Features

| Feature | Details |
|---------|---------|
| 🔍 Dual Search Engine | Brave Search + Tavily running in parallel |
| 🔄 Auto Fallback | If 1 engine fails → use the other engine |
| 🏷️ Auto-tag | Automatically tag: AI, Funding, SaaS, Tools, Trends, Startup, Growth |
| 📰 Source Classification | News / Blog / Report / Video / LinkedIn |
| 🗑️ Auto Dedup | Remove duplicate articles between 2 engines |
| 🔗 Integration | Direct connection with `content-writer` |

---

## Installation

### Requirements
- OpenClaw installed
- Brave Search API key (free 1,000 req/month)
- Tavily API key (free 1,000 req/month)

### Configure API keys

**Brave Search** — already integrated in OpenClaw. Configure via:
```powershell
openclaw configure --section web
```

**Tavily** — add to OpenClaw's `.env` file:
```
# File: ~/.openclaw/.env
TAVILY_API_KEY=tvly-your-key-here
```

Get free Tavily API key at: [tavily.com](https://tavily.com)

### Copy skill to OpenClaw

```powershell
# Windows
Copy-Item -Recurse content-research $env:USERPROFILE\.agents\skills\

# macOS / Linux
cp -r content-research ~/.agents/skills/
```

---

## Usage

### Basic
```
Research topic: AI agents 2026
```

### Custom sources
```
Find articles about "OpenAI funding" from news only, past week

Research "AI marketing tools" from blogs, get 15 articles
```

### Sample output

```
## Research Results: "AI agents 2026"
Found 14 articles from 11 sources
Sources: Brave (8) + Tavily (9) → merged 14 unique

### 📰 News
1. OpenAI Launches New Agent Framework — TechCrunch (2 hours ago) [Tavily]
   OpenAI announced a major update to its agent infrastructure...
   🏷️ AI | 🔗 techcrunch.com/...

### 📝 Articles & Blogs
2. The State of AI Agents in 2026 — a16z (3 days ago) [Brave]
   ...
```

---

## Integration with content-writer

After getting results, select articles to use and move to writing:
```
Use articles 1, 3, 5 to write a LinkedIn post
```

Agent will automatically call `content-writer` with the selected articles.

---

## File Structure

```
content-research/
├── README.md              ← You are reading this
├── SKILL.md               ← Agent instructions
└── references/
    └── source-filters.md  ← Detailed source filter configuration
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
