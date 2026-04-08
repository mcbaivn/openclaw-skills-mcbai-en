---
name: facebook-page-manager
clawhub_id: mcbaivn-facebook-page-manager
description: |
  Manage and auto-post content to Facebook Fanpage via Graph API.
  Supports text/photo posts, carousel (multi-image), video, Reels, Story (photo/video),
  scheduled publishing, edit/delete scheduled posts, comment on posts,
  reply to comments, and delete comments.
---

# Facebook Page Manager

> 📦 **Install:** `npx clawhub@latest install mcbaivn-facebook-page-manager`

Post and manage Facebook Page content via **Graph API v19.0** using Python.

## Quick Setup

### 1. Install dependencies
```bash
pip install requests
```

### 2. Get Access Token
See detailed guide: `references/get-token.md`

**Quick summary:**
- Go to [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
- Create token with permissions: `pages_manage_posts`, `pages_read_engagement`, `pages_manage_engagement`, `publish_video`
- Call `GET /me/accounts` to get **Page Access Token** and **Page ID**

### 3. Create config
Create file `scripts/fb_config.json`:
```json
{
  "access_token": "EAAxxxxxxxxxxxxxxx",
  "page_id": "123456789012345"
}
```

## Main Script: `scripts/fb_post.py`

### Post text
```bash
python fb_post.py text --message "Post content"
```

### Post photo
```bash
python fb_post.py photo --message "Caption" --images photo1.jpg
```

### Carousel (multiple images)
```bash
python fb_post.py photo --message "Caption" --images a.jpg b.jpg c.jpg
```

### Video
```bash
python fb_post.py video --message "Caption" --video clip.mp4
```

### Reels
```bash
python fb_post.py video --message "Caption" --video clip.mp4 --reel
```

### Story (photo/video)
```bash
python fb_post.py story --type photo --media story.jpg
python fb_post.py story --type video --media story.mp4
```

## Schedule Posts

Add `--schedule "YYYY-MM-DD HH:MM"` to any text/photo/video command:

```bash
python fb_post.py text --message "Monday morning post" --schedule "2024-12-25 08:00"
```

## Comment Management

```bash
python fb_post.py comment --post-id POST_ID --message "Comment text"
python fb_post.py reply --comment-id COMMENT_ID --message "Reply text"
python fb_post.py list-comments --post-id POST_ID
python fb_post.py delete-comment --comment-id COMMENT_ID
```

## References

- `references/get-token.md` — Step-by-step Access Token guide
- `references/api-reference.md` — Endpoint details, formats, limits
