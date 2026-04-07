---
name: facebook-page-manager
description: >
  Manage and auto-post content to Facebook Fanpage via Graph API.
  Supports: post text/photo, carousel (multiple images), video, Reels, Story (photo/video),
  schedule posts (scheduled_publish_time), view/edit/delete scheduled posts,
  comment on posts, reply to comments, delete comments.
  Use when user asks to "post to Facebook Page", "schedule Facebook post",
  "upload video to Fanpage", "post Facebook story", "Facebook carousel",
  "manage Facebook schedule", "comment on Facebook post", "reply to Facebook comment",
  or any post/manage content operation on Facebook Page.
---

# Facebook Page Manager

Skill to post and manage Facebook Page content via **Graph API v19.0** using Python.

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
> ⚠️ Add to `.gitignore`, do not commit this file!

---

## Main script: `scripts/fb_post.py`

### Post text
```bash
python fb_post.py text --message "Post content here"
```

### Post photo
```bash
python fb_post.py photo --message "Caption" --images photo1.jpg
```

### Carousel (multiple photos)
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

### Photo Story
```bash
python fb_post.py story --type photo --media story.jpg
```

### Video Story
```bash
python fb_post.py story --type video --media story.mp4
```

---

## Schedule Posts

Add `--schedule "YYYY-MM-DD HH:MM"` to any text/photo/video command:

```bash
python fb_post.py text --message "Monday morning post" --schedule "2024-12-25 08:00"
python fb_post.py photo --message "Caption" --images photo.jpg --schedule "2024-12-25 10:00"
python fb_post.py video --message "New video" --video clip.mp4 --schedule "2024-12-25 20:00"
```

> ⏰ Time must be at least **10 minutes** in the future and no more than **6 months** ahead.
> Story **does not support** scheduling.

---

## Manage Scheduled Posts

### List scheduled posts
```bash
python fb_post.py list-scheduled
```

### Delete post
```bash
python fb_post.py delete --post-id 123456789_987654321
```

### Reschedule post
```bash
python fb_post.py reschedule --post-id 123456789_987654321 --schedule "2024-12-26 09:00"
```

---

## Manage Comments

> **Required permission:** `pages_manage_engagement`

### Comment on a post
```bash
python fb_post.py comment --post-id 123456789_987654321 --message "Comment content"
```

### Reply to a comment
```bash
python fb_post.py reply --comment-id COMMENT_ID --message "Reply content"
```

### List comments on a post
```bash
python fb_post.py list-comments --post-id 123456789_987654321
```

### Delete a comment
```bash
python fb_post.py delete-comment --comment-id COMMENT_ID
```

---

## References

- `references/get-token.md` — Step-by-step guide to get Access Token
- `references/api-reference.md` — Endpoint details, formats, limits

## Important Notes

- **Page must be Published** (not Unpublished/Restricted)
- **Video** upload may take a few minutes to process
- **Carousel** maximum 10 photos per Facebook's limit
- **Reels** must be 3–90 seconds
- **Comment/Reply** requires `pages_manage_engagement` permission
- If you get a permission error, see `references/get-token.md` Troubleshooting section
