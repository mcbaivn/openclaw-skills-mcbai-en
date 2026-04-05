# 📥 Download AIO

> Tải video, audio, playlist, subtitle, thumbnail từ 1000+ nền tảng. Tự động gửi file về Telegram nếu ≤ 50MB.

---

## Cài đặt

```bash
npx clawhub@latest install download-aio
```

> Sau khi cài, chạy lần đầu để setup dependencies:
> ```powershell
> powershell -ExecutionPolicy Bypass -File $env:USERPROFILE\.agents\skills\download-aio\scripts\install.ps1
> ```
> Script tự động cài: yt-dlp, ffmpeg, tạo thư mục Downloads.

---

## Tính năng

| Tính năng | Chi tiết |
|-----------|---------|
| 🎬 Tải video | Best quality hoặc chọn 1080p / 720p / 480p / 360p |
| 🎵 Tải audio | MP3 hoặc M4A |
| 📋 Tải playlist | Toàn bộ hoặc giới hạn số lượng |
| 📝 Tải subtitle | Phụ đề tự động + chính thức, nhiều ngôn ngữ |
| 🖼️ Tải thumbnail | Ảnh bìa chất lượng cao |
| 📤 Auto gửi Telegram | Tự động gửi file ≤ 50MB về chat |

---

## Nền tảng hỗ trợ

YouTube, TikTok, Facebook, Instagram, Twitter/X, Twitch, Vimeo, SoundCloud, Reddit, Bilibili và **1000+ nền tảng** khác.

> Xem danh sách đầy đủ tại [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

---

## Cách dùng

Chỉ cần paste URL vào chat với OpenClaw agent:

```
https://www.youtube.com/watch?v=...
https://www.tiktok.com/@user/video/...
https://www.facebook.com/reel/...
```

Agent tự hiểu, tải về, gửi file Telegram. Xong.

### Tùy chỉnh nâng cao

```
Tải audio mp3 từ https://youtu.be/...
Tải playlist này, chỉ lấy 10 video đầu: https://...
Tải video 720p từ https://...
Tải phụ đề tiếng Việt từ https://youtu.be/...
```

---

## Xử lý sự cố

| Lỗi | Cách fix |
|-----|---------|
| Python không tìm thấy | Cài Python tại [python.org](https://python.org) rồi chạy lại `install.ps1` |
| HTTP 429 / Rate limit | Agent tự thêm delay, hoặc dùng `--cookies-from-browser chrome` |
| Video cần đăng nhập | Mở Chrome, đăng nhập, agent dùng `--cookies-from-browser chrome` |
| ffmpeg not found | Chạy `choco install ffmpeg` hoặc tải tại [ffmpeg.org](https://ffmpeg.org) |
| File > 50MB | File lưu tại `Downloads\yt-dlp\`, agent thông báo đường dẫn |

---

<p align="center">
  <a href="https://www.mcbai.vn">MCB AI</a> ·
  <a href="https://www.youtube.com/@mcbaivn">YouTube</a> ·
  <a href="https://openclaw.mcbai.vn/openclaw101">Khóa học OpenClaw 101</a>
</p>
