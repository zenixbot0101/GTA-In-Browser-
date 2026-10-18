<div align="center">
  <h1>🎮 Dee VoidCat — GTA 5 Miễn Phí</h1>
  <h4>Game GTA 5 chạy trên trình duyệt với host local và truy cập công khai</h4>
  
  <p>
    <a href="README.md">English</a> •
    <a href="README.vi.md">Tiếng Việt</a> •
    <a href="README.zh.md">中文</a> •
    <a href="README.ja.md">日本語</a>
  </p>
</div>

<div align="center">
  <a href="https://github.com/zenixbot0101/GTA-In-Browser-"><img src="https://img.shields.io/github/stars/zenixbot0101/GTA-In-Browser-.svg?logo=github&style=for-the-badge" alt="GitHub stars"></a>
  <a href="https://github.com/zenixbot0101/GTA-In-Browser-/issues"><img src="https://img.shields.io/github/issues/zenixbot0101/GTA-In-Browser-.svg?style=for-the-badge&logo=github" alt="GitHub Issues"></a>
  <a href="https://github.com/zenixbot0101/GTA-In-Browser-/network/members"><img src="https://img.shields.io/github/forks/zenixbot0101/GTA-In-Browser-.svg?style=for-the-badge&logo=github" alt="GitHub Forks"></a>
</div>

---

## ℹ️ Giới Thiệu

**Dee VoidCat GTA 5 Free** là phiên bản GTA 5 chạy hoàn toàn trên trình duyệt, có thể chạy local trên máy tính hoặc host công khai. Chơi game đầy đủ trực tiếp trên Chrome hoặc Edge với hỗ trợ WebGPU — không cần cài đặt game gốc.

Repository này cung cấp:
- 🎮 **File game đầy đủ** (~21GB mirror của GTA 5 browser build)
- 🖥️ **Server local** với Cross-Origin Isolation headers cho WebGPU
- 🌐 **Host công khai** qua ngrok tunnel hoặc Cloudflare Pages
- 🎨 **Trang landing tùy chỉnh** với kiểm tra hệ thống và giao diện đẹp
- ⚡ **Cấu hình hiệu suất** (720p/30fps, 720p/60fps, 1080p/60fps)

**Demo trực tuyến:** Chơi online tại instance của bạn

---

## 🚀 Bắt Đầu Nhanh

### Windows

1. **Tải game:**
   ```powershell
   .\Download-Game.ps1
   ```

2. **Khởi động server:**
   ```powershell
   python server_with_headers.py 3000 .
   ```

3. **Mở trình duyệt:**
   - Trang landing: http://localhost:3000/public/
   - Game: http://localhost:3000/mirror/playgta5.com/index.html

### Mac/Linux

1. **Tải game:**
   ```bash
   bash Download-Game.command
   ```

2. **Khởi động server:**
   ```bash
   python3 serve_local.py --open
   ```

---

## 🌐 Host Công Khai

### Dùng ngrok (Test Nhanh)

```powershell
# Khởi động server
python server_with_headers.py 3000 .

# Khởi động ngrok tunnel
ngrok http 3000
```

URL công khai: `https://YOUR-SUBDOMAIN.ngrok-free.dev/public/`

### Dùng Cloudflare Pages (Production)

```bash
# Build static site
python3 build_pages.py

# Deploy
npx wrangler pages deploy pages-output --project-name YOUR_PROJECT
```

---

## 🎮 Tính Năng

<table>
  <tr>
    <th>Tính Năng</th>
    <th>Trạng Thái</th>
    <th>Mô Tả</th>
  </tr>
  <tr>
    <td>🎨 Trang Landing Tùy Chỉnh</td>
    <td>✅</td>
    <td>Giao diện đẹp với animation, cursor tùy chỉnh, hiệu ứng particles</td>
  </tr>
  <tr>
    <td>🔍 Kiểm Tra Hệ Thống</td>
    <td>✅</td>
    <td>Kiểm tra WebGPU, RAM, CPU, secure context, SharedArrayBuffer</td>
  </tr>
  <tr>
    <td>🖥️ Host Local</td>
    <td>✅</td>
    <td>Server Python với COOP/COEP headers</td>
  </tr>
  <tr>
    <td>🌐 Truy Cập Công Khai</td>
    <td>✅</td>
    <td>Ngrok tunnel hoặc Cloudflare Pages deployment</td>
  </tr>
  <tr>
    <td>⚡ Cấu Hình Hiệu Suất</td>
    <td>✅</td>
    <td>720p/30fps (Tương thích), 720p/60fps (Cân bằng), 1080p/60fps (Chất lượng)</td>
  </tr>
  <tr>
    <td>🎮 Hỗ Trợ Tay Cầm</td>
    <td>🟡</td>
    <td>Map tay cầm cơ bản (thử nghiệm)</td>
  </tr>
  <tr>
    <td>📱 Hỗ Trợ Mobile</td>
    <td>🟡</td>
    <td>Điều khiển cảm ứng (thử nghiệm, chưa test trên thiết bị thật)</td>
  </tr>
  <tr>
    <td>🌍 Chơi Nhiều Người</td>
    <td>❌</td>
    <td>Chưa hỗ trợ</td>
  </tr>
</table>

**Chú thích:** ✅ Hỗ Trợ Đầy Đủ | 🟡 Thử Nghiệm | ❌ Chưa Hỗ Trợ

---

## 💻 Yêu Cầu Hệ Thống

### Yêu Cầu Tối Thiểu

| Thành Phần | Yêu Cầu |
|------------|---------|
| **Trình duyệt** | Chrome 90+ hoặc Edge 90+ có bật WebGPU |
| **GPU** | Hỗ trợ WebGPU (NVIDIA GTX 1050+, AMD RX 560+, Intel HD 630+) |
| **CPU** | Intel Core i3 / AMD Ryzen 3 trở lên |
| **RAM** | Tối thiểu 4GB, khuyến nghị 8GB |
| **Ổ cứng** | 25GB trống (45GB nếu giữ file tải về) |
| **Mạng** | Cần thiết cho lần tải đầu 21GB |

### Để Chạy 1080p/60fps

| Thành Phần | Yêu Cầu |
|------------|---------|
| **GPU** | NVIDIA RTX 2060+ / AMD RX 5700+ / Intel Arc A380+ |
| **CPU** | Intel Core i5-8400 / AMD Ryzen 5 3600 trở lên |
| **RAM** | Tối thiểu 8GB, khuyến nghị 16GB |

### Yêu Cầu Trình Duyệt

- ✅ Hỗ trợ WebGPU
- ✅ WebAssembly Memory64
- ✅ SharedArrayBuffer / Cross-Origin Isolation
- ✅ Bật tăng tốc phần cứng

**Kiểm tra tương thích:** Mở `http://localhost:3000/public/` và click "🎮 CHƠI NGAY" để chạy kiểm tra hệ thống.

---

## 🔧 Xử Lý Sự Cố

### Game bị kẹt ở 66%?

**Chrome:** `chrome://settings/system` → Bật "Use graphics acceleration when available" → Relaunch

**Edge:** Settings → System → Bật graphics acceleration → Restart

### Lỗi 404 khi mở game?

Đảm bảo server đang serve thư mục gốc:
```powershell
python server_with_headers.py 3000 .
```

Sau đó truy cập:
- Landing: `http://localhost:3000/public/`
- Game: `http://localhost:3000/mirror/playgta5.com/index.html`

### WebGPU không khả dụng?

1. Cập nhật Chrome/Edge lên phiên bản mới nhất
2. Cập nhật driver GPU
3. Kiểm tra `chrome://gpu` hoặc `edge://gpu` để xem trạng thái WebGPU
4. Đảm bảo tăng tốc phần cứng đã bật

### Màn hình đen / Graphics device lost?

1. Cập nhật driver GPU
2. Đóng các ứng dụng sử dụng GPU khác
3. Thử độ phân giải thấp hơn: `?low=1&fps=30&res=1280x720`
4. Kiểm tra lỗi tại `chrome://gpu`

### Hết bộ nhớ?

1. Đóng các tab và ứng dụng khác
2. Dùng cấu hình tương thích (720p/30fps)
3. Tăng giới hạn bộ nhớ trình duyệt (nếu có)

---

## 📝 Cấu Hình Hiệu Suất

| Cấu Hình | Độ Phân Giải | FPS Tối Đa | Cài Đặt | Phù Hợp Cho |
|----------|--------------|------------|---------|-------------|
| **Tương Thích** | 720p | 30 | Đồ họa thấp, không bóng | Máy cấu hình thấp |
| **Cân Bằng** | 720p | 60 | Đồ họa thấp, không bóng | Hầu hết máy |
| **Chất Lượng** | 1080p | 60 | Đồ họa thấp, không bóng | Máy cao cấp |
| **Benchmark** | 540p | Không giới hạn | Đồ họa thấp, không bóng | Test hiệu suất |

---

## 🤝 Đóng Góp

Contributions are welcome! Vui lòng:

1. Fork repository
2. Tạo feature branch
3. Commit thay đổi
4. Mở Pull Request

---

## 📄 Giấy Phép

Đây là phiên bản browser của GTA 5. Tất cả game assets và trademarks thuộc về Rockstar Games.

---

## 🔗 Liên Kết

- **GitHub Repository:** [https://github.com/zenixbot0101/GTA-In-Browser-](https://github.com/zenixbot0101/GTA-In-Browser-)
- **Báo Lỗi:** [Mở Issue](https://github.com/zenixbot0101/GTA-In-Browser-/issues)

---

<div align="center">
  <sub>Được xây dựng với ❤️ bởi cộng đồng</sub>
</div>
