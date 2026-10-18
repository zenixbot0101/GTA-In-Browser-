<div align="center">
  <h1>🎮 Dee VoidCat — GTA 5 Free</h1>
  <h4>Browser-based GTA 5 game with local hosting and public access</h4>
  
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

## ℹ️ About

**Dee VoidCat GTA 5 Free** is a complete browser-based implementation of GTA 5 that runs locally on your computer or can be hosted publicly. Play the full game directly in Chrome or Edge with WebGPU support — no installation of the original game required.

This repository provides:
- 🎮 **Complete game files** (~21GB mirror of GTA 5 browser build)
- 🖥️ **Local server** with Cross-Origin Isolation headers for WebGPU
- 🌐 **Public hosting** via ngrok tunnel or Cloudflare Pages
- 🎨 **Custom landing page** with system checks and beautiful UI
- ⚡ **Performance profiles** (720p/30fps, 720p/60fps, 1080p/60fps)

**Live Demo:** Play online at your own hosted instance

---

## 🚀 Quick Start

### Windows

1. **Download the game:**
   ```powershell
   .\Download-Game.ps1
   ```

2. **Start the local server:**
   ```powershell
   python server_with_headers.py 3000 .
   ```

3. **Open in browser:**
   - Landing page: http://localhost:3000/public/
   - Game: http://localhost:3000/mirror/playgta5.com/index.html

### Mac/Linux

1. **Download the game:**
   ```bash
   bash Download-Game.command
   ```

2. **Start the server:**
   ```bash
   python3 serve_local.py --open
   ```

---

## 🌐 Public Hosting

### Using ngrok (Quick Test)

```powershell
# Start server
python server_with_headers.py 3000 .

# Start ngrok tunnel
ngrok http 3000
```

Your public URL: `https://YOUR-SUBDOMAIN.ngrok-free.dev/public/`

### Using Cloudflare Pages (Production)

```bash
# Build static site
python3 build_pages.py

# Deploy
npx wrangler pages deploy pages-output --project-name YOUR_PROJECT
```

---

## 🎮 Features

<table>
  <tr>
    <th>Feature</th>
    <th>Status</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>🎨 Custom Landing Page</td>
    <td>✅</td>
    <td>Beautiful UI with animations, custom cursor, particle effects</td>
  </tr>
  <tr>
    <td>🔍 System Check</td>
    <td>✅</td>
    <td>WebGPU, memory, CPU, secure context, SharedArrayBuffer validation</td>
  </tr>
  <tr>
    <td>🖥️ Local Hosting</td>
    <td>✅</td>
    <td>Python server with COOP/COEP headers</td>
  </tr>
  <tr>
    <td>🌐 Public Access</td>
    <td>✅</td>
    <td>ngrok tunnel or Cloudflare Pages deployment</td>
  </tr>
  <tr>
    <td>⚡ Performance Profiles</td>
    <td>✅</td>
    <td>720p/30fps (Compatibility), 720p/60fps (Balanced), 1080p/60fps (Quality)</td>
  </tr>
  <tr>
    <td>🎮 Controller Support</td>
    <td>🟡</td>
    <td>Basic controller mapping (experimental)</td>
  </tr>
  <tr>
    <td>📱 Mobile Support</td>
    <td>🟡</td>
    <td>Touch controls (experimental, not tested on real devices)</td>
  </tr>
  <tr>
    <td>🌍 Multiplayer</td>
    <td>❌</td>
    <td>Not implemented</td>
  </tr>
</table>

**Legend:** ✅ Fully Supported | 🟡 Experimental | ❌ Not Supported

---

## 💻 System Requirements

### Minimum Requirements

| Component | Requirement |
|-----------|-------------|
| **Browser** | Chrome 90+ or Edge 90+ with WebGPU enabled |
| **GPU** | WebGPU-compatible (NVIDIA GTX 1050+, AMD RX 560+, Intel HD 630+) |
| **CPU** | Intel Core i3 / AMD Ryzen 3 or higher |
| **RAM** | 4GB minimum, 8GB recommended |
| **Storage** | 25GB free space (45GB if keeping download archives) |
| **Network** | Required for initial 21GB download |

### For 1080p/60fps

| Component | Requirement |
|-----------|-------------|
| **GPU** | NVIDIA RTX 2060+ / AMD RX 5700+ / Intel Arc A380+ |
| **CPU** | Intel Core i5-8400 / AMD Ryzen 5 3600 or higher |
| **RAM** | 8GB minimum, 16GB recommended |

### Browser Requirements

- ✅ WebGPU support
- ✅ WebAssembly Memory64
- ✅ SharedArrayBuffer / Cross-Origin Isolation
- ✅ Hardware acceleration enabled

**Check compatibility:** Open `http://localhost:3000/public/` and click "🎮 CHƠI NGAY" to run system checks.

---

## 📋 File Structure

```
playgta5/
├── public/                    # Landing page
│   ├── index.html            # Main landing page
│   └── res/                  # Images and resources
├── mirror/                    # Game files (21GB)
│   └── playgta5.com/
│       ├── index.html        # Game engine entry
│       ├── data/             # Game data files
│       └── b/                # Binary assets
├── runtime/                   # Bundled Python (Windows only)
├── support/                   # Support tools
├── server_with_headers.py    # Local server with COOP/COEP headers
├── Download-Game.ps1         # Windows download script
├── Download-Game.command     # Mac download script
└── README.md                 # This file
```

---

## 🔧 Troubleshooting

### Game stuck at 66%?

**Chrome:** `chrome://settings/system` → Enable "Use graphics acceleration when available" → Relaunch

**Edge:** Settings → System → Enable graphics acceleration → Restart

### Error 404 when opening game?

Make sure server is serving root directory:
```powershell
python server_with_headers.py 3000 .
```

Then access:
- Landing: `http://localhost:3000/public/`
- Game: `http://localhost:3000/mirror/playgta5.com/index.html`

### WebGPU not available?

1. Update Chrome/Edge to latest version
2. Update GPU drivers
3. Check `chrome://gpu` or `edge://gpu` for WebGPU status
4. Ensure hardware acceleration is enabled

### Black screen / Graphics device lost?

1. Update GPU drivers
2. Close other GPU-intensive applications
3. Try lower resolution: `?low=1&fps=30&res=1280x720`
4. Check `chrome://gpu` for errors

### Out of memory?

1. Close other tabs and applications
2. Use compatibility profile (720p/30fps)
3. Increase browser memory limit (if available)

**More troubleshooting:** [Open an issue](https://github.com/zenixbot0101/GTA-In-Browser-/issues/new) for additional help.

---

## 🛠️ Development

### Verify Installation

```powershell
# Windows
.\Verify-Game.cmd

# Mac/Linux
bash Verify-Game.command
```

### Run Tests

```bash
python3 -m unittest discover -s tests -v
node --check support/check.js
```

### Build for Cloudflare Pages

```bash
python3 build_pages.py
npx wrangler pages deploy pages-output --project-name YOUR_PROJECT
```

---

## 📝 Performance Profiles

| Profile | Resolution | FPS Cap | Settings | Best For |
|---------|-----------|---------|----------|----------|
| **Compatibility** | 720p | 30 | Low graphics, no shadows | Minimum spec systems |
| **Balanced** | 720p | 60 | Low graphics, no shadows | Most systems |
| **Quality** | 1080p | 60 | Low graphics, no shadows | High-end systems |
| **Benchmark** | 540p | Uncapped | Low graphics, no shadows | Performance testing |

**Custom URL parameters:**
```
http://localhost:3000/mirror/playgta5.com/?low=1&fps=60&res=1280x720&shadows=0
```

---

## ⚠️ Known Issues

- 🐛 Minimap roads may not render correctly
- 🐛 Some vehicles missing engine sounds
- 🐛 Occasional graphics device lost errors
- 🐛 Black world with working HUD

**Report issues:** [GitHub Issues](https://github.com/zenixbot0101/GTA-In-Browser-/issues)

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This is a browser-based implementation of GTA 5. All game assets and trademarks belong to Rockstar Games.

---

## 🔗 Links

- **GitHub Repository:** [https://github.com/zenixbot0101/GTA-In-Browser-](https://github.com/zenixbot0101/GTA-In-Browser-)
- **Report Issues:** [Open an Issue](https://github.com/zenixbot0101/GTA-In-Browser-/issues)

---

## ⭐ Support This Project

<div align="center">
  <a href="https://github.com/zenixbot0101/GTA-In-Browser-">
    <img alt="Star this repository" src="https://img.shields.io/github/stars/zenixbot0101/GTA-In-Browser-.svg?style=social" />
  </a>
</div>

---

<div align="center">
  <sub>Built with ❤️ by the community</sub>
</div>
