# IdeaMark Core

**IdeaMark**は、社会インフラからビジネスモデルの転換まで、複雑な問題を構造化された再利用可能な知識ブロックとしてエンコードするフレームワークです。  
ドメインを横断してパターンを接続することで、AIと人間の協働による解決策の認識、構成、進化を可能にします。

このリポジトリは、IdeaMarkテンプレートの作成と統合のためのコアスキーマ、例、ツールを提供します。

## 🚀 クイックスタート

### ローカル開発環境のセットアップ

1. **リポジトリのクローン**
   ```bash
   git clone https://github.com/ak2i/ideamark-core.git
   cd ideamark-core
   ```

2. **環境変数の設定**
   ```bash
   cp .env.example .env
   ```

3. **MCPサーバーの依存関係をインストール**
   ```bash
   cd lib/mcp_server
   pip install -r requirements.txt
   cd ../../
   ```

4. **MCPサーバーをローカルで実行**
   ```bash
   python -m uvicorn lib.mcp_server.main:app --host 0.0.0.0 --port 8000
   ```

サーバーは`http://localhost:8000`で利用可能になり、APIドキュメントは`http://localhost:8000/docs`で確認できます。

## 🌐 Fly.ioデプロイメント

### 前提条件

1. **Fly CLIのインストール**
   ```bash
   curl -L https://fly.io/install.sh | sh
   export FLYCTL_INSTALL="$HOME/.fly"
   export PATH="$FLYCTL_INSTALL/bin:$PATH"
   ```

2. **Fly.ioでの認証**
   ```bash
   fly auth login
   ```

### デプロイメント手順

1. **Flyアプリケーションの初期化**
   ```bash
   fly launch --no-deploy
   ```

2. **必要なシークレットの設定**
   ```bash
   # JWT認証シークレット
   fly secrets set JWT_SECRET_KEY="$(openssl rand -hex 32)"
   
   # LLMプロバイダーAPIキー（すべて必須）
   fly secrets set OPENAI_API_KEY="your-openai-api-key"
   fly secrets set ANTHROPIC_API_KEY="your-anthropic-api-key"
   fly secrets set MISTRAL_API_KEY="your-mistral-api-key"
   fly secrets set GOOGLE_API_KEY="your-google-generative-ai-key"
   
   # オプション：GitHub統合
   fly secrets set GITHUB_TOKEN="your-github-token"
   ```

3. **アプリケーションのデプロイ**
   ```bash
   fly deploy
   ```

4. **デプロイメントの確認**
   ```bash
   fly status
   fly logs
   ```

### デプロイ後の検証

デプロイされたエンドポイントをテスト：

```bash
# ヘルスチェック
curl https://your-app-name.fly.dev/health

# MCPエンドポイント
curl https://your-app-name.fly.dev/mcp/tools/list
curl https://your-app-name.fly.dev/mcp/resources/list
curl https://your-app-name.fly.dev/mcp/prompts/list
```

## 🔧 設定

### 環境変数

| 変数名 | 必須 | 説明 |
|--------|------|------|
| `JWT_SECRET_KEY` | ✅ | JWTトークン署名用の秘密鍵 |
| `OPENAI_API_KEY` | ✅ | OpenAI APIアクセスキー |
| `ANTHROPIC_API_KEY` | ✅ | Anthropic Claude APIキー |
| `MISTRAL_API_KEY` | ✅ | Mistral AI APIキー |
| `GOOGLE_API_KEY` | ✅ | Google Generative AI APIキー |
| `GITHUB_TOKEN` | ⚠️ | GitHub APIトークン（オプション） |
| `PORT` | ⚠️ | サーバーポート（デフォルト：8000） |
| `HOST` | ⚠️ | サーバーホスト（デフォルト：0.0.0.0） |
| `LOG_LEVEL` | ⚠️ | ログレベル（デフォルト：info） |
| `WORK_DIR` | ⚠️ | 作業ディレクトリ（デフォルト：/app/data） |

### MCPサーバー機能

- **標準MCPエンドポイント**: Model Context Protocol仕様の実装
- **JWT認証**: 高度なクレームを持つセキュアなトークンベース認証
- **ヘルスモニタリング**: 依存関係検証を含む包括的なヘルスチェック
- **マルチLLMサポート**: OpenAI、Anthropic、Mistral、Googleとの統合
- **パターン検証**: 既存コンポーネントを使用したスキーマベース検証

## 🏗️ アーキテクチャ

### コアコンポーネント

- **MCPサーバー** (`lib/mcp_server/`): FastAPIベースのModel Context Protocolサーバー
- **パターン検証** (`lib/merge/validators.py`): IdeaMarkパターンのスキーマ検証
- **LLMプロバイダー** (`lib/llm/providers.py`): マルチプロバイダーLLM統合
- **設定** (`lib/utils/config.py`): 集中設定管理
- **パターンローディング** (`lib/io/pattern_loader.py`): パターンファイルの読み込みと処理

### APIエンドポイント

#### ヘルス＆ステータス
- `GET /health` - 依存関係ステータスを含む包括的ヘルスチェック
- `GET /mcp/v1/ping` - 軽量ヘルスピング
- `GET /mcp/v1/initialize` - サーバー初期化情報

#### MCP標準エンドポイント
- `GET /mcp/tools/list` - MCPクライアント用利用可能ツール
- `GET /mcp/resources/list` - MCPクライアント用利用可能リソース
- `GET /mcp/prompts/list` - MCPクライアント用利用可能プロンプト

#### 認証
- `POST /auth/token` - JWTトークン生成
- OAuth統合エンドポイント

## 🧪 テスト

### ローカルテスト

```bash
# JWT認証のテスト
python test_jwt.py

# ヘルスチェックエンドポイントのテスト
python test_health.py

# サーバーを実行してエンドポイントをテスト
python -m uvicorn lib.mcp_server.main:app --reload
curl http://localhost:8000/health
```

### Claude.aiとの統合

デプロイ後、デプロイメントURLをMCPサーバーエンドポイントとして設定することで、Claude.aiブラウザ版とMCPサーバーを統合できます。

## 🔒 セキュリティ

- JWTトークンには発行者（`iss`）、対象者（`aud`）、スコープ、権限が含まれます
- すべてのAPIキーは暗号化されたFly.ioシークレットとして保存
- セキュアなクロスオリジンリクエスト用のCORS設定
- ヘルスチェックで依存関係の接続性を検証

## 📚 ドキュメント

- [MCP統合要件](docs/dev/mcp_integration/01_requirements.md)
- [MCPサーバー仕様](docs/dev/mcp_integration/02_specifications.md)
- [設定リファレンス](tools/config/default.yaml)

## 🐛 トラブルシューティング

### よくある問題

1. **認証エラー**
   - すべての必要なAPIキーがFlyシークレットとして設定されていることを確認
   - JWT_SECRET_KEYが適切に設定されていることを確認

2. **ヘルスチェックエラー**
   - ストレージボリュームが`/app/data`にマウントされていることを確認
   - LLMプロバイダーAPIキーが有効であることを確認

3. **デプロイメント問題**
   - Fly.ioログを確認：`fly logs`
   - Dockerfileがローカルでビルドできることを確認：`docker build -f lib/mcp_server/Dockerfile .`

### サポート

問題や質問については：
- [GitHub Issues](https://github.com/ak2i/ideamark-core/issues)を確認
- `fly logs`でデプロイメントログを確認
- `fly secrets list`で設定を確認

## 🔗 Claude.aiとの接続設定

### MCPサーバーの設定

1. **デプロイ完了後のURL確認**
   ```bash
   fly status
   # アプリケーションのURLを確認（例：https://your-app-name.fly.dev）
   ```

2. **Claude.aiでのMCP設定**
   - Claude.aiのブラウザ版にアクセス
   - 設定メニューからMCPサーバーの設定を開く
   - サーバーURLとして`https://your-app-name.fly.dev`を追加
   - 必要に応じて認証情報を設定

3. **接続テスト**
   ```bash
   # MCPエンドポイントが応答することを確認
   curl https://your-app-name.fly.dev/mcp/tools/list
   curl https://your-app-name.fly.dev/mcp/resources/list
   curl https://your-app-name.fly.dev/mcp/prompts/list
   ```

### 認証設定

MCPクライアントで認証が必要な場合：

1. **開発用トークンの生成**
   ```bash
   # ローカルでテスト用トークンを生成
   python test_jwt.py
   ```

2. **本番環境での認証**
   - `/auth/token`エンドポイントを使用してJWTトークンを取得
   - Authorizationヘッダーに`Bearer <token>`として設定

## License

This repository is licensed under [Creative Commons Zero v1.0 Universal (CC0 1.0)](https://creativecommons.org/publicdomain/zero/1.0/).

You are free to use, modify, and distribute all contents for any purpose, without asking permission.

We kindly request attribution where feasible, to help propagate the IdeaMark ecosystem.
