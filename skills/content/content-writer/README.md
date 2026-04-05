# content-writer — Write Posts for Any Social Media Platform

> OpenClaw skill that generates high-quality posts for **LinkedIn, Facebook, Twitter/X, TikTok, Threads** from any source material. Supports **6 formats, 8 tones, 2 languages**. Output is plain text ready to publish — no editing needed.

---

## What is this skill for?

You have ideas, research articles, or great data — but writing posts takes too much time? This skill helps you:
- Turn any source material into a publish-ready post
- Choose the right format for each platform (Facebook needs Story/Hook-List, LinkedIn needs Toplist/POV)
- Adjust tone to match your goal (viral, educational, storytelling, analytical...)
- Write naturally in English or Vietnamese
- Output is ready to go — no markdown, no strange formatting

---

## Supported Platforms

| Platform | Style | Best Formats |
|----------|-------|-------------|
| LinkedIn | Professional, data-driven | Toplist, POV, Case Study, How-to |
| Facebook | Conversational, emotional | Story, Hook-List-CTA, POV |
| Twitter/X | Punchy, opinionated | Short POV, Short Hook-List |
| TikTok | Casual, FOMO | Hook-List-CTA, Short How-to |
| Threads | Casual, unfiltered | POV, Short Story |

---

## 6 Built-in Formats

### 📋 Toplist
Numbered list with data points.
```
HOOK: Bold claim + specific number
CONTEXT: Why this matters now
LIST: Numbered items + metrics
TAKEAWAY: Pattern that emerges
CTA: Engagement question
```

### 💡 POV
Bold opinion backed by data. Creates debate.
```
HOOK: Contrarian opening
DATA: Evidence with numbers
ANALYSIS: What this means
PREDICTION: Clear prediction
CTA: Comment-provoking question
```

### 🏢 Case Study
Deep-dive into a specific story.
```
HOOK: Most impressive metric
CONTEXT: The original problem
WHAT THEY DID: Strategy + numbers
RESULTS: Concrete outcomes
LESSON: Non-obvious takeaway
CTA: Engagement question
```

### 🛠️ How-to
Step-by-step guide you can act on immediately.
```
HOOK: Promise a clear outcome
WHY: What people get wrong
STEPS: 3-7 steps with action verbs
PRO TIP: Shortcut few people know
RESULT: What you'll achieve
CTA: "Try step 1 today"
```

### 📖 Story *(Facebook-optimized)*
Emotional narrative, high share rate.
```
OPENING SCENE: Specific moment
TENSION: Conflict escalates
TURNING POINT: Aha moment
RESOLUTION: Results + numbers
LESSON: Non-obvious takeaway
CTA: Relatable question / tag prompt
```

### 🎯 Hook-List-CTA *(Facebook viral)*
Simplest format, most viral on Facebook.
```
HOOK (1 line): Stop-the-scroll
LIST: 5-10 short, specific items
CTA: Tag / Share / Comment prompt
```

---

## 8 Built-in Tones

| Tone | Style | Best For |
|------|-------|---------|
| Default | Data-driven, confident | All platforms |
| Bold | Provocative, contrarian | LinkedIn, Twitter/X |
| Educational | Teaching, uses examples | LinkedIn, Facebook |
| Storytelling | Narrative, emotional | Facebook, LinkedIn |
| Analytical | Analysis, comparisons | LinkedIn, Twitter/X |
| Viral | FOMO, urgency, share-bait | Facebook, TikTok |
| Empathetic | Warm, relatable, community | Facebook, Threads |
| Custom | You describe your own | All platforms |

---

## Installation

```powershell
# Windows
Copy-Item -Recurse content-writer $env:USERPROFILE\.agents\skills\

# macOS / Linux
cp -r content-writer ~/.agents/skills/
```

---

## Usage

### Simplest way
```
Write a Facebook post from this article: [paste content]
```

### Full specification
```
Write a Story post for Facebook, Viral tone, English, medium length from this article: [URL or content]
```

### Multiple platforms at once
```
Write the same content in 3 versions: LinkedIn (Toplist), Facebook (Story), Twitter (short POV)
```

### After finishing research
```
Use articles 1 and 3 to write a Hook-List-CTA for Facebook, in English
```

---

## Output Rules

Posts are always pure plain text:
- No asterisks (`*`) — never
- No markdown (`**`, `#`, `[]`)
- No em dashes (`—`) — use `-` or commas
- No URLs in post body
- Emphasis uses CAPS: `"This is a REAL opportunity"`
- Lists: use numbers or `→` arrows
- Emoji: natural per platform style (Facebook is more relaxed than LinkedIn)

---

## File Structure

```
content-writer/
├── README.md                      ← You are reading this
├── SKILL.md                       ← Agent instructions
└── references/
    ├── brand-context.md           ← MCB AI brand identity
    ├── platform-rules.md          ← Rules per platform
    ├── format-toplist.md          ← Toplist format
    ├── format-pov.md              ← POV format
    ├── format-case-study.md       ← Case Study format
    ├── format-how-to.md           ← How-to format
    ├── format-story.md            ← Story format (Facebook)
    ├── format-hook-list-cta.md    ← Hook-List-CTA viral format
    ├── tone-presets.md            ← 8 detailed tone presets
    └── formatting-rules.md        ← Mandatory rules
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
