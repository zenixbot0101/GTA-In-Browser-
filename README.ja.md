<div align="center">
  <h1>🎮 Dee VoidCat — GTA 5 無料版</h1>
  <h4>ブラウザベースの GTA 5 ゲーム、ローカルホスティングとパブリックアクセスに対応</h4>
  
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

## ℹ️ 概要

**Dee VoidCat GTA 5 無料版** は、ローカルまたはパブリックホスティングで実行できる、完全なブラウザベースの GTA 5 実装です。Chrome または Edge で WebGPU サポートを使用して、完全なゲームを直接プレイできます — オリジナルゲームのインストールは不要です。

このリポジトリは以下を提供します:
- 🎮 **完全なゲームファイル** (~21GB の GTA 5 ブラウザビルドミラー)
- 🖥️ **ローカルサーバー** WebGPU 用のクロスオリジン分離ヘッダー付き
- 🌐 **パブリックホスティング** ngrok トンネルまたは Cloudflare Pages 経由
- 🎨 **カスタムランディングページ** システムチェックと美しい UI
- ⚡ **パフォーマンスプロファイル** (720p/30fps, 720p/60fps, 1080p/60fps)

**ライブデモ:** 自分でホストしたインスタンスでオンラインプレイ

---

## 🚀 クイックスタート

### Windows

1. **ゲームをダウンロード:**
   ```powershell
   .\Download-Game.ps1
   ```

2. **ローカルサーバーを起動:**
   ```powershell
   python server_with_headers.py 3000 .
   ```

3. **ブラウザで開く:**
   - ランディングページ: http://localhost:3000/public/
   - ゲーム: http://localhost:3000/mirror/playgta5.com/index.html

### Mac/Linux

1. **ゲームをダウンロード:**
   ```bash
   bash Download-Game.command
   ```

2. **サーバーを起動:**
   ```bash
   python3 serve_local.py --open
   ```

---

## 🌐 パブリックホスティング

### ngrok を使用 (クイックテスト)

```powershell
# サーバーを起動
python server_with_headers.py 3000 .

# ngrok トンネルを起動
ngrok http 3000
```

パブリック URL: `https://YOUR-SUBDOMAIN.ngrok-free.dev/public/`

### Cloudflare Pages を使用 (本番環境)

```bash
# 静的サイトをビルド
python3 build_pages.py

# デプロイ
npx wrangler pages deploy pages-output --project-name YOUR_PROJECT
```

---

## 🎮 機能

<table>
  <tr>
    <th>機能</th>
    <th>ステータス</th>
    <th>説明</th>
  </tr>
  <tr>
    <td>🎨 カスタムランディングページ</td>
    <td>✅</td>
    <td>アニメーション、カスタムカーソル、パーティクルエフェクト付きの美しいUI</td>
  </tr>
  <tr>
    <td>🔍 システムチェック</td>
    <td>✅</td>
    <td>WebGPU、メモリ、CPU、セキュアコンテキスト、SharedArrayBuffer 検証</td>
  </tr>
  <tr>
    <td>🖥️ ローカルホスティング</td>
    <td>✅</td>
    <td>COOP/COEP ヘッダー付き Python サーバー</td>
  </tr>
  <tr>
    <td>🌐 パブリックアクセス</td>
    <td>✅</td>
    <td>ngrok トンネルまたは Cloudflare Pages デプロイ</td>
  </tr>
  <tr>
    <td>⚡ パフォーマンスプロファイル</td>
    <td>✅</td>
    <td>720p/30fps (互換性), 720p/60fps (バランス), 1080p/60fps (品質)</td>
  </tr>
  <tr>
    <td>🎮 コントローラーサポート</td>
    <td>🟡</td>
    <td>基本的なコントローラーマッピング（実験的）</td>
  </tr>
  <tr>
    <td>📱 モバイルサポート</td>
    <td>🟡</td>
    <td>タッチコントロール（実験的、実機テスト未実施）</td>
  </tr>
  <tr>
    <td>🌍 マルチプレイヤー</td>
    <td>❌</td>
    <td>未実装</td>
  </tr>
</table>

**凡例:** ✅ 完全サポート | 🟡 実験的 | ❌ 未サポート

---

## 💻 システム要件

### 最小要件

| コンポーネント | 要件 |
|--------------|------|
| **ブラウザ** | Chrome 90+ または Edge 90+ で WebGPU 有効 |
| **GPU** | WebGPU 対応 (NVIDIA GTX 1050+, AMD RX 560+, Intel HD 630+) |
| **CPU** | Intel Core i3 / AMD Ryzen 3 以上 |
| **RAM** | 最低 4GB、推奨 8GB |
| **ストレージ** | 25GB の空き容量（ダウンロードファイル保持時 45GB） |
| **ネットワーク** | 初回 21GB ダウンロードに必要 |

### 1080p/60fps 要件

| コンポーネント | 要件 |
|--------------|------|
| **GPU** | NVIDIA RTX 2060+ / AMD RX 5700+ / Intel Arc A380+ |
| **CPU** | Intel Core i5-8400 / AMD Ryzen 5 3600 以上 |
| **RAM** | 最低 8GB、推奨 16GB |

### ブラウザ要件

- ✅ WebGPU サポート
- ✅ WebAssembly Memory64
- ✅ SharedArrayBuffer / クロスオリジン分離
- ✅ ハードウェアアクセラレーション有効

**互換性チェック:** `http://localhost:3000/public/` を開いて「🎮 CHƠI NGAY」をクリックしてシステムチェックを実行。

---

## 🔧 トラブルシューティング

### ゲームが 66% で停止?

**Chrome:** `chrome://settings/system` → 「Use graphics acceleration when available」を有効 → 再起動

**Edge:** 設定 → システム → グラフィックアクセラレーションを有効 → 再起動

### ゲームを開くと 404 エラー?

サーバーがルートディレクトリを提供していることを確認:
```powershell
python server_with_headers.py 3000 .
```

次にアクセス:
- ランディング: `http://localhost:3000/public/`
- ゲーム: `http://localhost:3000/mirror/playgta5.com/index.html`

### WebGPU が利用できない?

1. Chrome/Edge を最新バージョンに更新
2. GPU ドライバーを更新
3. `chrome://gpu` または `edge://gpu` で WebGPU ステータスを確認
4. ハードウェアアクセラレーションが有効であることを確認

### 黒い画面 / グラフィックデバイス喪失?

1. GPU ドライバーを更新
2. 他の GPU 負荷の高いアプリケーションを閉じる
3. 低解像度を試す: `?low=1&fps=30&res=1280x720`
4. `chrome://gpu` でエラーを確認

### メモリ不足?

1. 他のタブとアプリケーションを閉じる
2. 互換性プロファイルを使用 (720p/30fps)
3. ブラウザのメモリ制限を増やす（可能な場合）

---

## 📝 パフォーマンスプロファイル

| プロファイル | 解像度 | FPS 上限 | 設定 | 適している環境 |
|------------|--------|----------|------|--------------|
| **互換性** | 720p | 30 | 低グラフィック、影なし | 最小スペックシステム |
| **バランス** | 720p | 60 | 低グラフィック、影なし | ほとんどのシステム |
| **品質** | 1080p | 60 | 低グラフィック、影なし | ハイエンドシステム |
| **ベンチマーク** | 540p | 無制限 | 低グラフィック、影なし | パフォーマンステスト |

---

## 🤝 コントリビューション

コントリビューション歓迎! 以下の手順で:

1. リポジトリをフォーク
2. フィーチャーブランチを作成
3. 変更をコミット
4. プルリクエストを開く

---

## 📄 ライセンス

これは GTA 5 のブラウザ版です。すべてのゲームアセットと商標は Rockstar Games に帰属します。

---

## 🔗 リンク

- **GitHub Repository:** [https://github.com/zenixbot0101/GTA-In-Browser-](https://github.com/zenixbot0101/GTA-In-Browser-)
- **問題を報告:** [Issue を開く](https://github.com/zenixbot0101/GTA-In-Browser-/issues)

---

<div align="center">
  <sub>コミュニティによって ❤️ で構築</sub>
</div>
