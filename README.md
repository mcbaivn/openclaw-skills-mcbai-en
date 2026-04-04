# OpenClaw Skills — MCBAI

> **Bộ sưu tập Skills mở rộng cho OpenClaw** — được tuyển chọn và phát triển bởi [MCB AI](https://mcbai.vn)

Tất cả skills trong repo này đều plug-and-play: tải về, copy vào `~/.agents/skills/`, dùng ngay — không cần code, không cần cấu hình phức tạp.

---

## Danh sách Skills

### 📥 [download-aio](skills/download-aio/)
**Tải video/audio từ 1000+ nền tảng**

Dùng yt-dlp để tải video, audio, playlist, subtitle từ YouTube, TikTok, Facebook, Instagram, Twitter/X và hơn 1000 trang khác. Sau khi tải tự động gửi file về Telegram.

> Trigger: paste URL vào chat là xong

---

> 🔄 Sẽ cập nhật thêm skills thường xuyên. **Star repo** để không bỏ lỡ 🌟

---

## Cách cài đặt skill

### Bước 1 — Clone repo

```bash
git clone https://github.com/mcb0809/openclaw-skills-mcbai.git
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/mcb0809/openclaw-skills-mcbai.git
```

### Bước 2 — Copy skill muốn dùng vào OpenClaw

```bash
# macOS / Linux
cp -r openclaw-skills-mcbai/skills/<tên-skill> ~/.agents/skills/

# Windows (PowerShell)
Copy-Item -Recurse openclaw-skills-mcbai\skills\<tên-skill> $env:USERPROFILE\.agents\skills\
```

### Bước 3 — Chạy script cài đặt (nếu skill yêu cầu)

Mỗi skill có thể có file `scripts/install.ps1` hoặc `scripts/install.sh` để cài dependencies tự động. Xem README của từng skill để biết chi tiết.

### Bước 4 — Dùng ngay!

Mở chat với OpenClaw agent và gọi skill theo hướng dẫn trong README của từng skill.

---

## Cấu trúc repo

```
openclaw-skills-mcbai/
├── README.md                        ← Bạn đang đọc file này
└── skills/
    ├── download-aio/                ← Skill tải video AIO
    │   ├── README.md                ← Hướng dẫn chi tiết skill
    │   ├── SKILL.md                 ← File điều khiển agent (không cần đọc)
    │   ├── scripts/                 ← Scripts cài đặt + tiện ích
    │   └── references/              ← Tài liệu tham khảo cho agent
    └── (skills tiếp theo...)
```

> **Lưu ý:** `SKILL.md` là file OpenClaw đọc để hiểu cách dùng skill — bạn không cần đọc file này. Chỉ cần đọc `README.md` của từng skill là đủ.

---

## Yêu cầu

- [OpenClaw](https://openclaw.mcbai.vn/) đã được cài đặt và cấu hình
- Mỗi skill có thể có yêu cầu riêng — xem README của từng skill

---

## Về MCB AI

MCB AI là nền tảng AI content & marketing automation của người Việt, dành cho người Việt.

| | |
|--|--|
| 🌐 Website | [mcbai.vn](https://www.mcbai.vn/) |
| 📘 Fanpage | [facebook.com/mcb.ai.vn](https://www.facebook.com/mcb.ai.vn/) |
| 🎬 YouTube | [youtube.com/@mcbaivn](https://www.youtube.com/@mcbaivn) |
| 🛠️ OpenClaw Cheatsheet | [openclaw.mcbai.vn](https://openclaw.mcbai.vn/) |
| 🎓 Khoá học OpenClaw 101 | [openclaw.mcbai.vn/openclaw101](https://openclaw.mcbai.vn/openclaw101) |
| 👥 Cộng đồng Facebook | [OpenClaw AI Kiếm Cơm](https://www.facebook.com/groups/openclawxvn) |
| 📱 MCB AI Academy (Zalo) | [zalo.me/g/mmqkhi259](https://zalo.me/g/mmqkhi259) |

---

## Đóng góp

Có skill hay muốn chia sẻ? Tạo Pull Request hoặc liên hệ qua Fanpage MCB AI.

---

<p align="center">Made with ❤️ by <a href="https://www.mcbai.vn">MCB AI</a> &nbsp;·&nbsp; <a href="https://www.youtube.com/@mcbaivn">YouTube</a> &nbsp;·&nbsp; <a href="https://openclaw.mcbai.vn/openclaw101">Học OpenClaw 101 →</a> &nbsp;·&nbsp; <a href="https://zalo.me/g/mmqkhi259">MCB AI Academy</a></p>
