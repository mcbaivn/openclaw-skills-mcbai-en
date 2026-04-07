# 📘 Facebook Page Manager — by MCB AI

Skill to **automatically** manage and post content to Facebook Fanpage via **Graph API v19.0**.

> 🌍 [Phiên bản tiếng Việt](https://github.com/mcbaivn/openclaw-skills-mcbai/tree/main/skills/social-media/facebook-page-manager)

---

## ✨ Features

| Feature | Supported |
|---------|-----------|
| Post text | ✅ |
| Post single photo | ✅ |
| Carousel (multiple photos) | ✅ up to 10 photos |
| Post video | ✅ |
| Reels | ✅ 3–90 seconds |
| Photo/Video Story | ✅ |
| Schedule posts | ✅ |
| View/delete/reschedule posts | ✅ |
| Comment on posts | ✅ |
| Reply to comments | ✅ |
| Delete comments | ✅ |

---

## 🚀 Quick Install

```bash
npx clawhub@latest install facebook-management-skills-by-mcbai
```

Or manually copy to `~/.agents/skills/`

---

## ⚙️ Setup

### 1. Install dependencies
```bash
pip install requests
```

### 2. Get Page Access Token
- Go to [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
- Select permissions: `pages_manage_posts`, `pages_read_engagement`, `pages_manage_engagement`, `publish_video`
- Call `GET /me/accounts` → get **Page Access Token** and **Page ID**
- See detailed guide: [`references/get-token.md`](./references/get-token.md)

### 3. Create config file
Create `scripts/fb_config.json`:
```json
{
  "access_token": "EAAxxxxxxxxxxxxxxx",
  "page_id": "123456789012345"
}
```

---

## 📖 Usage

### Post content
```bash
python fb_post.py text --message "Post content"
python fb_post.py photo --message "Caption" --images photo1.jpg photo2.jpg
python fb_post.py video --message "Caption" --video clip.mp4
python fb_post.py video --message "Caption" --video clip.mp4 --reel
python fb_post.py story --type photo --media story.jpg
python fb_post.py story --type video --media story.mp4
```

### Schedule posts
```bash
python fb_post.py text --message "Monday morning post" --schedule "2024-12-25 08:00"
python fb_post.py photo --message "Caption" --images photo.jpg --schedule "2024-12-25 10:00"
```

### Manage scheduled posts
```bash
python fb_post.py list-scheduled
python fb_post.py delete --post-id PAGE_ID_POST_ID
python fb_post.py reschedule --post-id PAGE_ID_POST_ID --schedule "2024-12-26 09:00"
```

### Comment & Reply
```bash
python fb_post.py comment --post-id PAGE_ID_POST_ID --message "Comment content"
python fb_post.py reply --comment-id COMMENT_ID --message "Reply content"
python fb_post.py list-comments --post-id PAGE_ID_POST_ID
python fb_post.py delete-comment --comment-id COMMENT_ID
```

---

## 🔑 Required Permissions

| Feature | Permission |
|---------|------------|
| Post text/photo/video/story | `pages_manage_posts` |
| Post video/Reels | `pages_manage_posts` + `publish_video` |
| View/delete posts | `pages_read_engagement` |
| Comment/Reply/Delete comment | `pages_manage_engagement` |

---

## 📁 Structure

```
facebook-page-manager/
├── SKILL.md                    ← OpenClaw reads this file
├── README.md                   ← This guide
├── scripts/
│   └── fb_post.py              ← Main script
└── references/
    ├── get-token.md            ← Step-by-step token guide
    └── api-reference.md        ← Endpoint details & formats
```

---

## ⚠️ Notes

- Page must be in **Published** state (not Unpublished/Restricted)
- Video uploads may take a few minutes to process
- Story **does not support** scheduling
- **Do not commit** `fb_config.json` to GitHub

---

## 🔗 Links

🌐 [mcbai.vn](https://www.mcbai.vn) · 📘 [MCB AI Fanpage](https://www.facebook.com/mcb.ai.vn) · 🎬 [YouTube @mcbaivn](https://www.youtube.com/@mcbaivn)

Made with ❤️ by [MCB AI](https://www.mcbai.vn)
