# IdeaMark Core API設計

このドキュメントでは、IdeaMarkコアライブラリが提供する内部APIと外部APIの設計仕様を定義します。各APIの目的、エンドポイント、パラメーター、認証方式などを詳細に説明します。

## 1. API設計原則

IdeaMarkのAPIは以下の設計原則に従います：

### 1.1 一般原則

- **一貫性**: すべてのAPIで一貫した命名規則、エラー処理、レスポンス形式を使用
- **バージョニング**: APIの互換性を確保するためのバージョン管理
- **自己記述性**: APIの使用方法が直感的に理解できる設計
- **軽量インターフェース**: 最小限のオーバーヘッドで必要な機能を提供
- **ステートレス設計**: セッション状態に依存しない設計
- **冪等性**: 同じ操作を複数回実行しても安全であることを保証

### 1.2 エラー処理原則

- **標準化されたエラー形式**: 一貫したエラー応答構造
- **詳細なエラーメッセージ**: 問題の解決に役立つ情報を提供
- **適切なHTTPステータスコード**: 状況に応じた正確なステータスコードを使用
- **エラーの分類**: ビジネスロジックエラーとシステムエラーの区別

### 1.3 セキュリティ原則

- **最小権限の原則**: 必要最小限の権限でのAPI操作
- **入力検証**: すべての入力パラメータの厳密な検証
- **出力エンコード**: センシティブデータの適切な処理
- **レート制限**: APIの過剰使用を防止するための制限

## 2. 内部API

内部APIは、IdeaMarkコアライブラリを使用するアプリケーションに提供される主要なインターフェースです。

### 2.1 ドキュメント管理API

#### 2.1.1 IdeaMarkCore クラス

```python
class IdeaMarkCore:
    def __init__(self, storage_manager: StorageManager, config_manager: ConfigManager):
        self.storage = storage_manager
        self.config = config_manager
    
    # ドキュメント基本操作
    async def create_document(self, content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> Document:
        """新規ドキュメントを作成します"""
        # パラメーター:
        #   content: ドキュメント本体のコンテンツ
        #   metadata: (オプション) ドキュメントメタデータ
        # 戻り値:
        #   作成されたドキュメント
        pass
    
    async def get_document(self, document_id: str, version: Optional[str] = None) -> Document:
        """ドキュメントを取得します"""
        # パラメーター:
        #   document_id: ドキュメント識別子
        #   version: (オプション) 特定バージョンの指定
        # 戻り値:
        #   取得したドキュメント
        pass
    
    async def update_document(self, document_id: str, content: Dict[str, Any]) -> Document:
        """ドキュメントを更新します"""
        # パラメーター:
        #   document_id: 更新対象ドキュメントの識別子
        #   content: 更新内容
        # 戻り値:
        #   更新されたドキュメント
        pass
    
    async def delete_document(self, document_id: str) -> bool:
        """ドキュメントを削除します"""
        # パラメーター:
        #   document_id: 削除対象ドキュメントの識別子
        # 戻り値:
        #   削除が成功したかのブール値
        pass
    
    # メタデータ操作
    async def update_metadata(self, document_id: str, metadata: Dict[str, Any]) -> Document:
        """ドキュメントのメタデータを更新します"""
        # パラメーター:
        #   document_id: ドキュメント識別子
        #   metadata: 更新するメタデータ
        # 戻り値:
        #   更新されたドキュメント
        pass
    
    async def add_tags(self, document_id: str, tags: List[str]) -> Document:
        """ドキュメントにタグを追加します"""
        # パラメーター:
        #   document_id: ドキュメント識別子
        #   tags: 追加するタグのリスト
        # 戻り値:
        #   更新されたドキュメント
        pass
    
    # ドキュメント検証と処理
    async def validate_document(self, document: Union[Document, Dict[str, Any]]) -> ValidationResult:
        """ドキュメント構造の検証を行います"""
        # パラメーター:
        #   document: 検証対象のドキュメントまたはその内容
        # 戻り値:
        #   検証結果
        pass
    
    async def resolve_refs(self, document: Document) -> Document:
        """ドキュメント内のrefsを解決します"""
        # パラメーター:
        #   document: refs解決対象のドキュメント
        # 戻り値:
        #   refs解決済みのドキュメント
        pass
    
    # インポート/エクスポート
    async def import_document(self, file_path: Union[str, Path]) -> Document:
        """外部ファイルからドキュメントをインポートします"""
        # パラメーター:
        #   file_path: インポート元のファイルパス
        # 戻り値:
        #   インポートされたドキュメント
        pass
    
    async def export_document(
        self, document_id: str, format: str = "yaml", path: Optional[Union[str, Path]] = None
    ) -> Union[str, bool]:
        """ドキュメントをエクスポートします"""
        # パラメーター:
        #   document_id: エクスポート対象のドキュメント識別子
        #   format: 出力形式 (yaml, json)
        #   path: (オプション) 出力先ファイルパス
        # 戻り値:
        #   pathが指定された場合は成功フラグ、そうでない場合はエクスポートされた内容の文字列
        pass
```

#### 2.1.2 エラー処理

```python
class IdeaMarkError(Exception):
    """IdeaMarkの基本例外クラス"""
    def __init__(self, message: str, error_code: str, details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.error_code = error_code
        self.details = details or {}
        super().__init__(self.message)

class ValidationError(IdeaMarkError):
    """ドキュメント検証エラー"""
    def __init__(self, message: str, validation_errors: List[Dict[str, Any]]):
        super().__init__(
            message=message,
            error_code="VALIDATION_ERROR",
            details={"errors": validation_errors}
        )

class DocumentNotFoundError(IdeaMarkError):
    """ドキュメント未検出エラー"""
    def __init__(self, document_id: str, version: Optional[str] = None):
        details = {"document_id": document_id}
        if version:
            details["version"] = version
        super().__init__(
            message=f"Document not found: {document_id}" + (f" (version {version})" if version else ""),
            error_code="DOCUMENT_NOT_FOUND",
            details=details
        )

class StorageError(IdeaMarkError):
    """ストレージ操作エラー"""
    def __init__(self, message: str, operation: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            message=message,
            error_code=f"STORAGE_{operation.upper()}_ERROR",
            details=details
        )
```

### 2.2 検索API

#### 2.2.1 SearchService クラス

```python
class SearchService:
    def __init__(self, ideamark_core: IdeaMarkCore, config: Dict[str, Any]):
        self.core = ideamark_core
        self.config = config
        self.index_manager = self._initialize_index_manager()
    
    # 基本検索
    async def search(self, query: Union[str, SearchQuery]) -> List[SearchResult]:
        """検索を実行します"""
        # パラメーター:
        #   query: 検索クエリ文字列またはSearchQueryオブジェクト
        # 戻り値:
        #   検索結果のリスト
        pass
    
    # 意味検索
    async def semantic_search(self, query: str, **kwargs) -> List[SearchResult]:
        """意味ベースの検索を実行します"""
        # パラメーター:
        #   query: 検索クエリ文字列
        #   **kwargs: 追加の検索オプション
        # 戻り値:
        #   検索結果のリスト
        pass
    
    # タグ検索
    async def tag_search(self, tags: List[str], **kwargs) -> List[SearchResult]:
        """タグベースの検索を実行します"""
        # パラメーター:
        #   tags: 検索対象のタグリスト
        #   **kwargs: 追加の検索オプション
        # 戻り値:
        #   検索結果のリスト
        pass
    
    # 複合検索
    async def combined_search(self, text_query: Optional[str], tags: Optional[List[str]], filters: Optional[Dict[str, Any]], **kwargs) -> List[SearchResult]:
        """テキスト検索とタグ検索を組み合わせた検索を実行します"""
        # パラメーター:
        #   text_query: (オプション) テキスト検索クエリ
        #   tags: (オプション) 検索対象のタグリスト
        #   filters: (オプション) 追加のフィルター
        #   **kwargs: 追加の検索オプション
        # 戻り値:
        #   検索結果のリスト
        pass
    
    # インデックス管理
    async def index_document(self, document: Document) -> bool:
        """ドキュメントをインデックスに追加します"""
        # パラメーター:
        #   document: インデックスに追加するドキュメント
        # 戻り値:
        #   インデックス操作の成功フラグ
        pass
    
    async def remove_from_index(self, document_id: str) -> bool:
        """ドキュメントをインデックスから削除します"""
        # パラメーター:
        #   document_id: 削除するドキュメントのID
        # 戻り値:
        #   インデックス操作の成功フラグ
        pass
    
    async def rebuild_index(self) -> bool:
        """インデックスを再構築します"""
        # 戻り値:
        #   インデックス操作の成功フラグ
        pass
```

### 2.3 バージョニングAPI

#### 2.3.1 VersioningService クラス

```python
class VersioningService:
    def __init__(self, ideamark_core: IdeaMarkCore):
        self.core = ideamark_core
    
    # バージョン履歴
    async def get_version_history(self, document_id: str) -> List[VersionInfo]:
        """ドキュメントのバージョン履歴を取得します"""
        # パラメーター:
        #   document_id: ドキュメント識別子
        # 戻り値:
        #   バージョン情報のリスト
        pass
    
    # バージョン作成
    async def create_version(self, document: Document, comment: Optional[str] = None) -> str:
        """新しいバージョンを作成します"""
        # パラメーター:
        #   document: バージョン作成対象のドキュメント
        #   comment: (オプション) バージョン作成コメント
        # 戻り値:
        #   新しいバージョン番号
        pass
    
    # バージョン比較
    async def compare_versions(self, document_id: str, version1: str, version2: str) -> DiffResult:
        """2つのバージョン間の差分を計算します"""
        # パラメーター:
        #   document_id: ドキュメント識別子
        #   version1: 比較元バージョン
        #   version2: 比較先バージョン
        # 戻り値:
        #   差分結果
        pass
    
    # バージョンマージ
    async def merge_versions(self, document_id: str, version1: str, version2: str) -> Tuple[Document, List[str]]:
        """2つのバージョンをマージします"""
        # パラメーター:
        #   document_id: ドキュメント識別子
        #   version1: マージ元バージョン1
        #   version2: マージ元バージョン2
        # 戻り値:
        #   マージ結果ドキュメントと競合リスト
        pass
    
    # 競合解決
    async def resolve_conflict(self, document_id: str, conflict_id: str, resolution: Dict[str, Any]) -> bool:
        """特定の競合を解決します"""
        # パラメーター:
        #   document_id: ドキュメント識別子
        #   conflict_id: 競合識別子
        #   resolution: 解決内容
        # 戻り値:
        #   解決成功フラグ
        pass
```

### 2.4 LLMインターフェースAPI

#### 2.4.1 LLMManager クラス

```python
class LLMManager:
    def __init__(self, config_path: str = None):
        self.providers: Dict[LLMProvider, LLMInterface] = {}
        self.default_provider: LLMProvider = LLMProvider.OPENAI
        self.config = self._load_config(config_path)
    
    # LLM管理
    def register_provider(self, provider: LLMProvider, implementation: LLMInterface) -> None:
        """LLMプロバイダーの実装を登録します"""
        # パラメーター:
        #   provider: プロバイダータイプ
        #   implementation: プロバイダー実装
        pass
    
    def get_provider(self, provider: Optional[LLMProvider] = None) -> LLMInterface:
        """LLMプロバイダーのインスタンスを取得します"""
        # パラメーター:
        #   provider: (オプション) プロバイダータイプ
        # 戻り値:
        #   LLMインターフェース実装
        pass
    
    # テキスト生成
    async def generate(self, prompt: str, provider: Optional[LLMProvider] = None, **kwargs) -> LLMResponse:
        """LLMによるテキスト生成を行います"""
        # パラメーター:
        #   prompt: 生成プロンプト
        #   provider: (オプション) 使用するプロバイダー
        #   **kwargs: 追加の生成オプション
        # 戻り値:
        #   生成レスポンス
        pass
    
    async def stream_generate(self, prompt: str, provider: Optional[LLMProvider] = None, **kwargs) -> AsyncIterator[LLMResponse]:
        """LLMによるストリーミングテキスト生成を行います"""
        # パラメーター:
        #   prompt: 生成プロンプト
        #   provider: (オプション) 使用するプロバイダー
        #   **kwargs: 追加の生成オプション
        # 戻り値:
        #   生成レスポンスのイテレータ
        pass
    
    # プロンプト管理
    def render_prompt_template(self, template_name: str, **kwargs) -> str:
        """プロンプトテンプレートをレンダリングします"""
        # パラメーター:
        #   template_name: テンプレート名
        #   **kwargs: テンプレート変数
        # 戻り値:
        #   レンダリング済みのプロンプト文字列
        pass
    
    def register_prompt_template(self, name: str, template: str) -> None:
        """プロンプトテンプレートを登録します"""
        # パラメーター:
        #   name: テンプレート名
        #   template: テンプレート内容
        pass
```

## 3. 外部API（REST API）

アプリケーションが外部システムに提供するRESTful APIの定義です。

### 3.1 認証とセキュリティ

#### 3.1.1 認証方式

- **API Key認証**:
  - リクエストヘッダー: `X-Api-Key: <API_KEY>`
  - すべてのAPIエンドポイントで要求

- **JWT認証**:
  - リクエストヘッダー: `Authorization: Bearer <JWT_TOKEN>`
  - ユーザー固有の権限が必要なAPIエンドポイントで要求

#### 3.1.2 レート制限

- **基本制限**: 1 IPあたり1分間に最大60リクエスト
- **認証済み制限**: 1ユーザーあたり1分間に最大120リクエスト
- **ヘッダー**: 
  - `X-RateLimit-Limit`: 制限値
  - `X-RateLimit-Remaining`: 残りリクエスト数
  - `X-RateLimit-Reset`: 制限リセット時間（Unix時間）

### 3.2 ドキュメント管理API

#### 3.2.1 ドキュメント操作

```
# ドキュメント一覧取得
GET /api/v1/documents
パラメーター:
  - limit: 取得件数 (デフォルト: 20)
  - offset: スキップ件数 (デフォルト: 0)
  - status: ステータスフィルター (オプション)
  - tags: タグフィルター (オプション、カンマ区切り)
レスポンス:
  - 200 OK: ドキュメントメタデータの配列と総件数
  - 401 Unauthorized: 認証エラー
  - 403 Forbidden: 権限エラー

# ドキュメント作成
POST /api/v1/documents
リクエストボディ:
  - content: ドキュメント内容 (必須)
  - metadata: メタデータ (オプション)
レスポンス:
  - 201 Created: 作成されたドキュメントデータ
  - 400 Bad Request: 入力検証エラー
  - 401 Unauthorized: 認証エラー
  - 403 Forbidden: 権限エラー

# ドキュメント取得
GET /api/v1/documents/{document_id}
パラメーター:
  - version: 特定バージョンを取得 (オプション)
レスポンス:
  - 200 OK: ドキュメントデータ
  - 404 Not Found: ドキュメントが存在しない
  - 401 Unauthorized: 認証エラー
  - 403 Forbidden: 権限エラー

# ドキュメント更新
PUT /api/v1/documents/{document_id}
リクエストボディ:
  - content: 更新内容 (必須)
レスポンス:
  - 200 OK: 更新されたドキュメントデータ
  - 400 Bad Request: 入力検証エラー
  - 404 Not Found: ドキュメントが存在しない
  - 401 Unauthorized: 認証エラー
  - 403 Forbidden: 権限エラー

# ドキュメント削除
DELETE /api/v1/documents/{document_id}
レスポンス:
  - 204 No Content: 削除成功
  - 404 Not Found: ドキュメントが存在しない
  - 401 Unauthorized: 認証エラー
  - 403 Forbidden: 権限エラー
```

#### 3.2.2 メタデータ操作

```
# メタデータ更新
PATCH /api/v1/documents/{document_id}/metadata
リクエストボディ:
  - metadata: 更新するメタデータフィールド
レスポンス:
  - 200 OK: 更新されたメタデータ
  - 400 Bad Request: 入力検証エラー
  - 404 Not Found: ドキュメントが存在しない
  - 401 Unauthorized: 認証エラー

# タグ管理
PUT /api/v1/documents/{document_id}/tags
リクエストボディ:
  - tags: タグのリスト
レスポンス:
  - 200 OK: 更新されたタグリスト
  - 400 Bad Request: 入力検証エラー
  - 404 Not Found: ドキュメントが存在しない
  - 401 Unauthorized: 認証エラー
```

### 3.3 バージョン管理API

```
# バージョン履歴取得
GET /api/v1/documents/{document_id}/versions
パラメーター:
  - limit: 取得件数 (デフォルト: 20)
  - offset: スキップ件数 (デフォルト: 0)
レスポンス:
  - 200 OK: バージョン情報の配列
  - 404 Not Found: ドキュメントが存在しない
  - 401 Unauthorized: 認証エラー

# 特定バージョン取得
GET /api/v1/documents/{document_id}/versions/{version}
レスポンス:
  - 200 OK: 指定バージョンのドキュメント
  - 404 Not Found: ドキュメントまたはバージョンが存在しない
  - 401 Unauthorized: 認証エラー

# バージョン作成
POST /api/v1/documents/{document_id}/versions
リクエストボディ:
  - comment: バージョン作成コメント (オプション)
レスポンス:
  - 201 Created: 作成されたバージョン情報
  - 400 Bad Request: 入力検証エラー
  - 404 Not Found: ドキュメントが存在しない
  - 401 Unauthorized: 認証エラー

# バージョン比較
GET /api/v1/documents/{document_id}/versions/compare
パラメーター:
  - from: 比較元バージョン (必須)
  - to: 比較先バージョン (必須)
レスポンス:
  - 200 OK: 差分情報
  - 400 Bad Request: パラメータエラー
  - 404 Not Found: ドキュメントまたはバージョンが存在しない
  - 401 Unauthorized: 認証エラー

# バージョンマージ
POST /api/v1/documents/{document_id}/versions/merge
リクエストボディ:
  - source_versions: マージ元バージョン配列 (必須)
  - strategy: マージ戦略 (オプション、デフォルト: "automatic")
レスポンス:
  - 200 OK: マージ結果
  - 400 Bad Request: 入力検証エラー
  - 404 Not Found: ドキュメントまたはバージョンが存在しない
  - 409 Conflict: マージ競合情報
  - 401 Unauthorized: 認証エラー
```

### 3.4 検索API

```
# 基本検索
GET /api/v1/search
パラメーター:
  - q: 検索クエリ (必須)
  - limit: 取得件数 (デフォルト: 20)
  - offset: スキップ件数 (デフォルト: 0)
  - filter: JSONフィルター (オプション)
  - sort: ソート順 (オプション)
レスポンス:
  - 200 OK: 検索結果と総件数
  - 400 Bad Request: クエリパラメータエラー
  - 401 Unauthorized: 認証エラー

# 意味検索
GET /api/v1/search/semantic
パラメーター:
  - q: 検索クエリ (必須)
  - limit: 取得件数 (デフォルト: 10)
  - offset: スキップ件数 (デフォルト: 0)
  - min_score: 最小スコア (オプション、デフォルト: 0.5)
レスポンス:
  - 200 OK: 検索結果と総件数
  - 400 Bad Request: クエリパラメータエラー
  - 401 Unauthorized: 認証エラー

# タグ検索
GET /api/v1/search/tags
パラメーター:
  - tags: カンマ区切りタグリスト (必須)
  - operator: タグ結合演算子 (オプション、"and" または "or"、デフォルト: "and")
  - limit: 取得件数 (デフォルト: 20)
  - offset: スキップ件数 (デフォルト: 0)
レスポンス:
  - 200 OK: 検索結果と総件数
  - 400 Bad Request: クエリパラメータエラー
  - 401 Unauthorized: 認証エラー

# 複合検索
POST /api/v1/search/advanced
リクエストボディ:
  - text_query: テキスト検索クエリ (オプション)
  - tags: タグリスト (オプション)
  - filters: フィルター条件 (オプション)
  - sort: ソート条件 (オプション)
  - limit: 取得件数 (オプション)
  - offset: スキップ件数 (オプション)
レスポンス:
  - 200 OK: 検索結果と総件数
  - 400 Bad Request: 入力検証エラー
  - 401 Unauthorized: 認証エラー
```

### 3.5 LLM操作API

```
# テキスト生成
POST /api/v1/llm/generate
リクエストボディ:
  - prompt: 生成プロンプト (必須)
  - provider: LLMプロバイダー (オプション)
  - model: モデル名 (オプション)
  - params: 生成パラメーター (オプション)
レスポンス:
  - 200 OK: 生成テキストと使用量情報
  - 400 Bad Request: 入力検証エラー
  - 401 Unauthorized: 認証エラー
  - 429 Too Many Requests: レート制限超過
  - 503 Service Unavailable: LLMサービス利用不能

# ストリーミングテキスト生成
POST /api/v1/llm/generate/stream
リクエストボディ:
  - prompt: 生成プロンプト (必須)
  - provider: LLMプロバイダー (オプション)
  - model: モデル名 (オプション)
  - params: 生成パラメーター (オプション)
レスポンス:
  - 200 OK: Server-Sent Eventsストリーム
  - 400 Bad Request: 入力検証エラー
  - 401 Unauthorized: 認証エラー
  - 429 Too Many Requests: レート制限超過
  - 503 Service Unavailable: LLMサービス利用不能

# モデル一覧取得
GET /api/v1/llm/models
パラメーター:
  - provider: 特定プロバイダーのみ取得 (オプション)
レスポンス:
  - 200 OK: 利用可能なモデルリスト
  - 401 Unauthorized: 認証エラー
  - 503 Service Unavailable: LLMサービス利用不能
```

## 4. MCP (Model Context Protocol) API

Model Context Protocol用のAPIインターフェース仕様です。

### 4.1 MCP基本構造

```json
{
  "messages": [
    {
      "role": "user",
      "content": "IdeaMarkで新しいドキュメントを作成してください。"
    }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "create_document",
        "description": "Create a new IdeaMark document",
        "parameters": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "Document title"
            },
            "content": {
              "type": "object",
              "description": "Document content"
            },
            "tags": {
              "type": "array",
              "description": "Document tags",
              "items": {
                "type": "string"
              }
            }
          },
          "required": ["title", "content"]
        }
      }
    }
  ]
}
```

### 4.2 MCP ツール定義

```json
{
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "create_document",
        "description": "Create a new IdeaMark document",
        "parameters": {
          "type": "object",
          "properties": {
            "title": {
              "type": "string",
              "description": "Document title"
            },
            "content": {
              "type": "object",
              "description": "Document content"
            },
            "tags": {
              "type": "array",
              "description": "Document tags",
              "items": {
                "type": "string"
              }
            }
          },
          "required": ["title", "content"]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "search_documents",
        "description": "Search for IdeaMark documents",
        "parameters": {
          "type": "object",
          "properties": {
            "query": {
              "type": "string",
              "description": "Search query"
            },
            "tags": {
              "type": "array",
              "description": "Filter by tags",
              "items": {
                "type": "string"
              }
            },
            "limit": {
              "type": "integer",
              "description": "Maximum number of results",
              "default": 5
            }
          },
          "required": ["query"]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "get_document",
        "description": "Get a specific IdeaMark document",
        "parameters": {
          "type": "object",
          "properties": {
            "document_id": {
              "type": "string",
              "description": "Document identifier"
            },
            "version": {
              "type": "string",
              "description": "Optional document version"
            }
          },
          "required": ["document_id"]
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "update_document",
        "description": "Update an existing IdeaMark document",
        "parameters": {
          "type": "object",
          "properties": {
            "document_id": {
              "type": "string",
              "description": "Document identifier"
            },
            "content": {
              "type": "object",
              "description": "Updated document content"
            },
            "comment": {
              "type": "string",
              "description": "Update comment"
            }
          },
          "required": ["document_id", "content"]
        }
      }
    }
  ]
}
```

### 4.3 MCP APIエンドポイント

```
# MCP対応リクエスト処理
POST /api/v1/mcp/chat
リクエストボディ:
  - messages: メッセージ履歴配列 (必須)
  - tools: 使用できるツール定義配列 (オプション)
  - tool_choice: 使用するツールの選択 (オプション)
レスポンス:
  - 200 OK: MCP応答
  - 400 Bad Request: 入力検証エラー
  - 401 Unauthorized: 認証エラー
  - 429 Too Many Requests: レート制限超過
  - 503 Service Unavailable: サービス利用不能
```

## 5. エラー処理とバリデーション

### 5.1 標準エラーレスポンス形式

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error message",
    "details": {
      "field1": "Field specific error",
      "field2": "Another field error"
    },
    "request_id": "unique-request-identifier",
    "timestamp": "2025-06-14T08:15:30Z"
  }
}
```

### 5.2 主要エラーコード

| エラーコード | HTTPステータス | 説明 |
|-------------|---------------|-----|
| INVALID_REQUEST | 400 | リクエスト形式エラー |
| VALIDATION_ERROR | 400 | 入力検証エラー |
| AUTHENTICATION_ERROR | 401 | 認証失敗 |
| PERMISSION_DENIED | 403 | 権限不足 |
| RESOURCE_NOT_FOUND | 404 | リソース未検出 |
| CONFLICT | 409 | リソース競合 |
| RATE_LIMIT_EXCEEDED | 429 | レート制限超過 |
| INTERNAL_ERROR | 500 | 内部サーバーエラー |
| SERVICE_UNAVAILABLE | 503 | 外部サービス利用不能 |

### 5.3 バリデーション方式

- **スキーマバリデーション**: リクエストボディのJSONスキーマ検証
- **セマンティックバリデーション**: ビジネスルールに基づく検証
- **クロスフィールドバリデーション**: 複数フィールド間の関係検証
- **型変換**: 適切な型への自動変換と検証

## 6. APIドキュメント

### 6.1 OpenAPI仕様

IdeaMark Core APIは、OpenAPI 3.0仕様に準拠したAPIドキュメントを提供します。

```yaml
openapi: 3.0.0
info:
  title: IdeaMark Core API
  description: API for managing IdeaMark documents and related operations
  version: 1.0.0
servers:
  - url: https://api.ideamark.example/v1
    description: Production API server
  - url: https://dev-api.ideamark.example/v1
    description: Development API server
tags:
  - name: Documents
    description: Document management operations
  - name: Search
    description: Search operations
  - name: Versions
    description: Version management operations
  - name: LLM
    description: LLM operations
paths:
  /documents:
    get:
      summary: List documents
      tags:
        - Documents
      # ... 詳細は省略
```

### 6.2 インタラクティブドキュメント

- **Swagger UI**: `/api/docs` でAPIのインタラクティブドキュメント提供
- **ReDoc**: `/api/redoc` で読みやすいAPIドキュメント提供
- **APIエクスプローラー**: 実際にAPIを試せる環境の提供

## 7. API拡張と進化戦略

### 7.1 バージョニング戦略

- **URLパスバージョニング**: `/api/v1/resource`, `/api/v2/resource`
- **後方互換性**: 可能な限り維持
- **非推奨プロセス**: 機能廃止前の十分な告知期間

### 7.2 API拡張点

- **カスタムヘッダー**: `X-IdeaMark-Feature-*` で拡張機能の制御
- **クエリパラメーター**: `feature=*` で実験的機能の有効化
- **APIファサード**: 複雑なユースケースのための高レベルAPIの提供

### 7.3 フィードバックループ

- **使用状況監視**: API使用パターンの分析
- **ユーザーフィードバック**: フィードバックチャネルの提供
- **継続的改善**: 定期的なAPI改善と更新
