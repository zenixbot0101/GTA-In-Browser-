<div align="center">
  <h1>🎮 Dee VoidCat — GTA 5 免费版</h1>
  <h4>基于浏览器的 GTA 5 游戏，支持本地托管和公共访问</h4>
  
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

## ℹ️ 关于

**Dee VoidCat GTA 5 免费版** 是一个完整的基于浏览器的 GTA 5 实现，可以在您的计算机上本地运行或公开托管。在 Chrome 或 Edge 浏览器中直接玩完整游戏，支持 WebGPU — 无需安装原版游戏。

此仓库提供:
- 🎮 **完整游戏文件** (~21GB GTA 5 浏览器版镜像)
- 🖥️ **本地服务器** 带有 WebGPU 所需的跨域隔离头
- 🌐 **公共托管** 通过 ngrok 隧道或 Cloudflare Pages
- 🎨 **自定义落地页** 带有系统检查和精美 UI
- ⚡ **性能配置** (720p/30fps, 720p/60fps, 1080p/60fps)

**在线演示:** 在您自己的托管实例上在线游玩

---

## 🚀 快速开始

### Windows

1. **下载游戏:**
   ```powershell
   .\Download-Game.ps1
   ```

2. **启动本地服务器:**
   ```powershell
   python server_with_headers.py 3000 .
   ```

3. **在浏览器中打开:**
   - 落地页: http://localhost:3000/public/
   - 游戏: http://localhost:3000/mirror/playgta5.com/index.html

### Mac/Linux

1. **下载游戏:**
   ```bash
   bash Download-Game.command
   ```

2. **启动服务器:**
   ```bash
   python3 serve_local.py --open
   ```

---

## 🌐 公共托管

### 使用 ngrok (快速测试)

```powershell
# 启动服务器
python server_with_headers.py 3000 .

# 启动 ngrok 隧道
ngrok http 3000
```

您的公共 URL: `https://YOUR-SUBDOMAIN.ngrok-free.dev/public/`

### 使用 Cloudflare Pages (生产环境)

```bash
# 构建静态站点
python3 build_pages.py

# 部署
npx wrangler pages deploy pages-output --project-name YOUR_PROJECT
```

---

## 🎮 功能特性

<table>
  <tr>
    <th>功能</th>
    <th>状态</th>
    <th>描述</th>
  </tr>
  <tr>
    <td>🎨 自定义落地页</td>
    <td>✅</td>
    <td>精美UI，带动画、自定义光标、粒子效果</td>
  </tr>
  <tr>
    <td>🔍 系统检查</td>
    <td>✅</td>
    <td>WebGPU、内存、CPU、安全上下文、SharedArrayBuffer 验证</td>
  </tr>
  <tr>
    <td>🖥️ 本地托管</td>
    <td>✅</td>
    <td>Python 服务器带 COOP/COEP 头</td>
  </tr>
  <tr>
    <td>🌐 公共访问</td>
    <td>✅</td>
    <td>ngrok 隧道或 Cloudflare Pages 部署</td>
  </tr>
  <tr>
    <td>⚡ 性能配置</td>
    <td>✅</td>
    <td>720p/30fps (兼容), 720p/60fps (平衡), 1080p/60fps (质量)</td>
  </tr>
  <tr>
    <td>🎮 手柄支持</td>
    <td>🟡</td>
    <td>基本手柄映射（实验性）</td>
  </tr>
  <tr>
    <td>📱 移动端支持</td>
    <td>🟡</td>
    <td>触控控制（实验性，未在真实设备测试）</td>
  </tr>
  <tr>
    <td>🌍 多人游戏</td>
    <td>❌</td>
    <td>未实现</td>
  </tr>
</table>

**图例:** ✅ 完全支持 | 🟡 实验性 | ❌ 不支持

---

## 💻 系统要求

### 最低要求

| 组件 | 要求 |
|------|------|
| **浏览器** | Chrome 90+ 或 Edge 90+ 启用 WebGPU |
| **GPU** | 支持 WebGPU (NVIDIA GTX 1050+, AMD RX 560+, Intel HD 630+) |
| **CPU** | Intel Core i3 / AMD Ryzen 3 或更高 |
| **内存** | 最低 4GB，推荐 8GB |
| **存储** | 25GB 可用空间（保留下载文件需 45GB） |
| **网络** | 初次下载 21GB 需要网络 |

### 1080p/60fps 要求

| 组件 | 要求 |
|------|------|
| **GPU** | NVIDIA RTX 2060+ / AMD RX 5700+ / Intel Arc A380+ |
| **CPU** | Intel Core i5-8400 / AMD Ryzen 5 3600 或更高 |
| **内存** | 最低 8GB，推荐 16GB |

### 浏览器要求

- ✅ WebGPU 支持
- ✅ WebAssembly Memory64
- ✅ SharedArrayBuffer / 跨域隔离
- ✅ 已启用硬件加速

**检查兼容性:** 打开 `http://localhost:3000/public/` 并点击 "🎮 CHƠI NGAY" 运行系统检查。

---

## 🔧 故障排除

### 游戏卡在 66%?

**Chrome:** `chrome://settings/system` → 启用 "Use graphics acceleration when available" → 重启

**Edge:** 设置 → 系统 → 启用图形加速 → 重启

### 打开游戏时出现 404 错误?

确保服务器正在服务根目录:
```powershell
python server_with_headers.py 3000 .
```

然后访问:
- 落地页: `http://localhost:3000/public/`
- 游戏: `http://localhost:3000/mirror/playgta5.com/index.html`

### WebGPU 不可用?

1. 将 Chrome/Edge 更新到最新版本
2. 更新 GPU 驱动程序
3. 检查 `chrome://gpu` 或 `edge://gpu` 查看 WebGPU 状态
4. 确保已启用硬件加速

### 黑屏 / 图形设备丢失?

1. 更新 GPU 驱动程序
2. 关闭其他占用 GPU 的应用程序
3. 尝试较低分辨率: `?low=1&fps=30&res=1280x720`
4. 检查 `chrome://gpu` 中的错误

### 内存不足?

1. 关闭其他标签页和应用程序
2. 使用兼容性配置 (720p/30fps)
3. 增加浏览器内存限制（如果可用）

---

## 📝 性能配置

| 配置 | 分辨率 | FPS 上限 | 设置 | 适用于 |
|------|--------|----------|------|--------|
| **兼容性** | 720p | 30 | 低画质，无阴影 | 最低配置系统 |
| **平衡** | 720p | 60 | 低画质，无阴影 | 大多数系统 |
| **质量** | 1080p | 60 | 低画质，无阴影 | 高端系统 |
| **基准测试** | 540p | 不限 | 低画质，无阴影 | 性能测试 |

---

## 🤝 贡献

欢迎贡献! 请:

1. Fork 仓库
2. 创建功能分支
3. 提交更改
4. 打开 Pull Request

---

## 📄 许可证

这是 GTA 5 的浏览器版本。所有游戏资源和商标属于 Rockstar Games。

---

## 🔗 链接

- **GitHub Repository:** [https://github.com/zenixbot0101/GTA-In-Browser-](https://github.com/zenixbot0101/GTA-In-Browser-)
- **报告问题:** [打开 Issue](https://github.com/zenixbot0101/GTA-In-Browser-/issues)

---

<div align="center">
  <sub>由社区用 ❤️ 构建</sub>
</div>
