# How to Get Facebook Page Access Token

## Overview

To use the Facebook Graph API to post on a Page, you need a **Page Access Token** (not a regular User Token).

---

## Step 1: Create a Facebook App

1. Go to **[Meta for Developers](https://developers.facebook.com/)**
2. Click **My Apps → Create App**
3. Select **"Other"** → **"Business"** → Name your app → Create
4. Go to **App Dashboard** → Note your **App ID** and **App Secret**

---

## Step 2: Get a temporary User Access Token (for testing)

1. Go to **[Graph API Explorer](https://developers.facebook.com/tools/explorer/)**
2. Select your app from the dropdown
3. Click **"Generate Access Token"**
4. Select permissions:
   - `pages_manage_posts` ✅
   - `pages_read_engagement` ✅
   - `pages_manage_engagement` ✅ (for comment management)
   - `publish_video` ✅ (for video posts)
5. Click **Generate Token** → Allow permissions

> ⚠️ This token only lasts **1-2 hours** — use it for testing only!

---

## Step 3: Get Page Access Token

After getting a User Token, run this command to get your Page list and long-lived token:

```bash
curl "https://graph.facebook.com/v19.0/me/accounts?access_token=YOUR_USER_TOKEN"
```

Response will return:
```json
{
  "data": [
    {
      "access_token": "EAAxxxxxxxx...",   ← THIS IS YOUR PAGE TOKEN
      "category": "Media/News Company",
      "name": "Your Page Name",
      "id": "123456789",                  ← PAGE ID
      "tasks": ["ANALYZE", "ADVERTISE", "MODERATE", "CREATE_CONTENT"]
    }
  ]
}
```

Save the `access_token` (Page Token) and `id` (Page ID).

---

## Step 4: Create a Long-Lived Page Access Token (never expires)

Page Access Tokens from Step 3 usually **don't expire** if the page is published and the app has passed basic review.

To be sure, convert to a long-lived token:

**Step 4a:** Exchange short User Token → Long-lived User Token
```bash
curl "https://graph.facebook.com/oauth/access_token
  ?grant_type=fb_exchange_token
  &client_id=APP_ID
  &client_secret=APP_SECRET
  &fb_exchange_token=SHORT_USER_TOKEN"
```

**Step 4b:** Get Page Token from long-lived User Token
```bash
curl "https://graph.facebook.com/v19.0/me/accounts?access_token=LONG_LIVED_USER_TOKEN"
```

This Page Token will **never expire**.

---

## Step 5: Verify your token

Paste your token into the [Access Token Debugger](https://developers.facebook.com/tools/debug/accesstoken/) to verify:
- Type: `PAGE`
- Expires: `Never` ✅
- All required scopes are present

---

## Step 6: Save config to `fb_config.json`

Create `fb_config.json` in the same folder as `fb_post.py`:

```json
{
  "access_token": "EAAxxxxxxxxxxxxxxxxxxxxxxxx",
  "page_id": "123456789012345"
}
```

> 🔒 **IMPORTANT:** Add `fb_config.json` to `.gitignore` — never commit your token to GitHub!

---

## Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `(#200) Requires manage_pages permission` | Missing permission | Regenerate token with all required scopes |
| `(#100) Invalid parameter` | Wrong page_id or endpoint | Double-check page_id |
| `Token expired` | Token has expired | Redo from Step 4 |
| `(#368) The action attempted...` | Page not published or restricted | Check Page status |
| `Video upload failed` | File too large or wrong format | MP4 H.264, max 10GB, under 240 minutes |

---

## Required Permissions Summary

| Feature | Permission |
|---------|------------|
| Post text/photo | `pages_manage_posts` |
| Post video/Reels | `pages_manage_posts` + `publish_video` |
| Post Story | `pages_manage_posts` |
| View/delete posts | `pages_read_engagement` |
| Schedule posts | `pages_manage_posts` |
| Comment/Reply/Delete | `pages_manage_engagement` |

---

## Note on Stories

Facebook Graph API supports posting Stories via:
- `/{page-id}/photo_stories` (photo)
- `/{page-id}/video_stories` (video)

Stories **do not support scheduling** via API — they post immediately.
