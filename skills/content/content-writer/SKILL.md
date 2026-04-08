---
name: content-writer
clawhub_id: mcbaivn-content-writer
description: |
  Generate high-quality social media posts from research articles and source data.
  Supports LinkedIn, Facebook, Twitter/X, TikTok, Threads.
  6 content formats, 8 tone presets, 3 lengths, 2 languages (EN/VI).
---

# Content Writer Skill

> 📦 **Install:** `npx clawhub@latest install mcbaivn-content-writer`

Generate professional social media posts from research articles. Platform-optimized, multi-format, multi-tone.

## When to Use

- User has articles/data and wants social media posts
- User wants a post in a specific format
- Works best after `content-research` skill

## Workflow

### 1. Gather Inputs
- **Source material** (required)
- **Platform** (default: LinkedIn)
- **Format** (default: toplist)
- **Tone** (default: default)
- **Length** (default: medium)
- **Language** (default: Vietnamese)

### 2. Select Format

| Format | Best For |
|--------|----------|
| Toplist | Numbered lists with data |
| POV | Bold opinions backed by data |
| Case Study | Deep-dive one story |
| How-to | Step-by-step guides |
| Story | Narrative, emotional journey |
| Hook-List-CTA | Facebook viral format |

### 3. Platform Rules

| Platform | Max Length | Hashtags |
|----------|-----------|----------|
| LinkedIn | 3,000 chars | 3-5 |
| Facebook | 63,206 chars | 0-3 |
| Twitter/X | 280 chars | 1-2 |
| TikTok | 2,200 chars | 5-10 |
| Threads | 500 chars | 0-2 |

## Critical Rules

1. NO asterisks (*) — plain text only
2. NO markdown formatting
3. NO source URLs in post body
4. Short paragraphs (1-2 sentences max)
5. Emphasis = CAPS on 1-2 words
6. Lists = numbers or arrows only

## Reference Files

- `references/brand-context.md` — Brand identity
- `references/format-*.md` — Format instructions
- `references/tone-presets.md` — Tone details
- `references/platform-rules.md` — Platform constraints
- `references/formatting-rules.md` — Must-read formatting rules
