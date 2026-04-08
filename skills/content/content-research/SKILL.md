---
name: content-research
clawhub_id: mcbaivn-content-research
description: |
  Search and discover trending content sources for any topic using dual web search
  (Brave + Tavily in parallel). Powers the MCB AI content research pipeline.
---

# Content Research Skill

> 📦 **Install:** `npx clawhub@latest install mcbaivn-content-research`

Search the web for trending articles, news, and content sources on any topic. Uses Brave Search + Tavily API in parallel for maximum coverage.

## When to Use

- Research a topic before writing content
- Find recent articles, news, or data about a subject
- Discover trending sources for LinkedIn/social media
- Curate sources for toplist, POV, case study, or how-to posts

## Search Strategy

- **Brave Search** — via `web_search` tool (built-in)
- **Tavily** — via API call using `TAVILY_API_KEY`

### Fallback Logic
- Run both in parallel
- If one fails, use the other
- If both succeed, merge and deduplicate by URL

## Workflow

1. **Understand** the research request (topic, source filter, freshness, count)
2. **Search** with both Brave and Tavily (2 queries each)
3. **Merge** and deduplicate results by URL
4. **Organize** — title, source, URL, date, summary, type, tag, engine
5. **Present** results in scannable format

## Integration

After research, hand off selected articles to `content-writer` skill.
See `references/source-filters.md` for source filter configurations.
