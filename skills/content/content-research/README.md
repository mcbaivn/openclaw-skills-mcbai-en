# 🔍 Content Research - MCB AI

> Tìm kiếm bài viết, tin tức và nguồn nội dung về bất kỳ chủ đề nào từ web. Sử dụng **Brave Search + Tavily** song song để cho kết quả phong phú nhất. Thường dùng trước `content-writer` để chuẩn bị nguồn bài.

---

## Cài đặt

```bash
npx clawhub@latest install content-research-mcbai
```

> **Yêu cầu API keys:**
> - **Brave Search** — cấu hình qua `openclaw configure --section web`
> - **Tavily** — thêm vào `~/.openclaw/.env`: `TAVILY_API_KEY=tvly-your-key-here` (miễn phí tại [tavily.com](https://tavily.com))

---

## Tính năng

| Tính năng | Chi tiết |
|-----------|---------|
| 🔄 Dual Search Engine | Brave Search + Tavily chạy song song |
| 🔀 Fallback tự động | Nếu 1 engine lỗi → dùng engine còn lại |
| 🏷️ Auto-tag | Tự động gán tag: AI, Funding, SaaS, Tools, Trends, Startup, Growth |
| 📰 Phân loại nguồn | News / Blog / Report / Video / LinkedIn |
| 🔃 Dedup tự động | Loại bỏ bài trùng lặp giữa 2 engine |
| 🔗 Tích hợp | Kết nối trực tiếp với `content-writer` |

---

## Cách dùng

```
Research chủ đề: AI agents 2026
Tìm bài về "OpenAI funding" chỉ từ news, 1 tuần gần đây
Research "AI marketing tools" từ blog, lấy 15 bài
```

---

## Tích hợp với content-writer

Sau khi có kết quả, chọn bài muốn dùng và chuyển sang viết:
```
Dùng bài 1, 3, 5 để viết LinkedIn post
```

---

<p align="center">
  <a href="https://www.mcbai.vn">MCB AI</a> ·
  <a href="https://www.youtube.com/@mcbaivn">YouTube</a> ·
  <a href="https://openclaw.mcbai.vn/openclaw101">Khóa học OpenClaw 101</a>
</p>
