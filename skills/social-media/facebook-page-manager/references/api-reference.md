# API Reference - Facebook Page Manager

## Endpoints used in this skill

| Feature | Method | Endpoint |
|---------|--------|----------|
| Post text | POST | `/{page-id}/feed` |
| Post photo | POST | `/{page-id}/photos` |
| Carousel | POST | `/{page-id}/feed` (with `attached_media`) |
| Video/Reels | POST | `/{page-id}/videos` |
| Photo Story | POST | `/{page-id}/photo_stories` |
| Video Story | POST | `/{page-id}/video_stories` |
| Scheduled posts | GET | `/{page-id}/scheduled_posts` |
| Delete post | DELETE | `/{post-id}` |
| Edit scheduled | POST | `/{post-id}` |
| Comment on post | POST | `/{post-id}/comments` |
| Reply to comment | POST | `/{comment-id}/comments` |
| List comments | GET | `/{post-id}/comments` |
| Delete comment | DELETE | `/{comment-id}` |

---

## Schedule Posts

`scheduled_publish_time` must be a **Unix timestamp** and must be:
- At least **10 minutes** in the future
- No more than **6 months** from now

Include `"published": "false"` in the request.

Python example:
```python
from datetime import datetime
ts = int(datetime(2024, 12, 25, 8, 0).timestamp())
```

---

## Carousel

Upload each photo with `published=false` → get photo IDs → combine into feed post:

```json
{
  "message": "Caption here",
  "attached_media": [
    {"media_fbid": "photo_id_1"},
    {"media_fbid": "photo_id_2"},
    {"media_fbid": "photo_id_3"}
  ]
}
```

---

## Video/Reels

- Format: MP4 (H.264 video, AAC audio)
- Reels: add `"video_type": "REELS"`
- Max size: 10GB, max duration: 240 minutes
- Reels: 3–90 seconds

---

## Story

- Photo story: JPEG/PNG, 9:16 ratio recommended
- Video story: MP4, max 15 seconds
- **Scheduling not supported** — posts immediately

---

## Comments

- Comment on post: `POST /{post-id}/comments` with `message` param
- Reply to comment: `POST /{comment-id}/comments` with `message` param
- List comments: `GET /{post-id}/comments?fields=id,message,from,created_time`
- Delete comment: `DELETE /{comment-id}`
- Required permission: `pages_manage_engagement`

---

## Graph API Version

Skill uses `v19.0`. Check latest version at:
https://developers.facebook.com/docs/graph-api/changelog
