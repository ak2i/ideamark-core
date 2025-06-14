# IdeaMark Core コンポーネント設計

このドキュメントでは、IdeaMarkコアライブラリの詳細なコンポーネント設計について説明します。各コンポーネントの責務、インターフェース定義、および相互作用について記述します。

## 1. Core Layer コンポーネント設計

### 1.1 LLM Interface

LLM Interface は、外部の大規模言語モデル（LLM）プロバイダーとの連携を抽象化するためのコンポーネントです。

#### 1.1.1 責務

- 複数のLLMプロバイダー（OpenAI, Anthropic, Google, ローカルモデルなど）を統一インターフェースで抽象化
- プロンプトテンプレート管理とレンダリング
- レスポンスの正規化と構造化
- エラー処理とリトライ戦略
- レート制限と使用量管理

#### 1.1.2 インターフェース定義

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum

class LLMProvider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    LOCAL = "local"
    MOCK = "mock"

@dataclass
class LLMConfig:
    provider: LLMProvider
    api_key: Optional[str] = None
    model_name: str = "default"
    base_url: Optional[str] = None
    max_tokens: int = 4000
    temperature: float = 0.7
    timeout: int = 30
    extra_params: Dict[str, Any] = None

@dataclass
class LLMResponse:
    content: str
    usage: Dict[str, int]
    model: str
    finish_reason: str
    metadata: Dict[str, Any] = None

class LLMInterface(ABC):
    @abstractmethod
    async def generate(self, prompt: str, **kwargs) -> LLMResponse:
        pass
    
    @abstractmethod
    async def stream_generate(self, prompt: str, **kwargs):
        pass
    
    @abstractmethod
    def validate_config(self) -> bool:
        pass

class LLMManager:
    def __init__(self, config_path: str = None):
        self.providers: Dict[LLMProvider, LLMInterface] = {}
        self.default_provider: LLMProvider = LLMProvider.OPENAI
        self.config = self._load_config(config_path)
    
    def register_provider(self, provider: LLMProvider, implementation: LLMInterface):
        self.providers[provider] = implementation
    
    async def generate(self, prompt: str, provider: LLMProvider = None, **kwargs) -> LLMResponse:
        provider = provider or self.default_provider
        if provider not in self.providers:
            raise ValueError(f"Provider {provider} not registered")
        return await self.providers[provider].generate(prompt, **kwargs)
```

#### 1.1.3 実装詳細

- **プロバイダーアダプタパターン**: 各LLMプロバイダー用の具体的な実装クラスを提供
- **設定ローダー**: 環境変数とコンフィグファイルから設定を読み込む
- **プロンプトテンプレートエンジン**: Jinja2ベースのテンプレートレンダリング
- **レスポンスパーサー**: 構造化データの抽出と正規化
- **トークン計算**: プロンプトとレスポンスのトークン使用量計算
- **キャッシュ層**: 結果のキャッシュによるAPI呼び出し削減

#### 1.1.4 依存関係

- **外部依存**: OpenAI SDK, Anthropic SDK, Google AI SDK
- **内部依存**: Config Management

### 1.2 Config Management

Config Managementは、アプリケーション全体の設定を一元管理するコンポーネントです。

#### 1.2.1 責務

- 設定の読み込みと検証
- 環境変数との統合
- デフォルト値の提供
- コンポーネント固有の設定へのアクセス提供

#### 1.2.2 インターフェース定義

```python
from typing import Any, Dict, Optional, TypeVar, Generic, Type
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

class ConfigManager:
    def __init__(self, config_path: Optional[str] = None):
        self.config_path = config_path
        self.config_data = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        # 設定ファイルの読み込みと環境変数の統合処理
        pass
    
    def get_section(self, section_name: str) -> Dict[str, Any]:
        """指定されたセクションの設定データを取得"""
        return self.config_data.get(section_name, {})
    
    def get_typed_config(self, section_name: str, config_model: Type[T]) -> T:
        """指定されたセクションの設定データを型付きモデルとして取得"""
        section_data = self.get_section(section_name)
        return config_model.parse_obj(section_data)

class CoreConfig(BaseModel):
    """コアコンポーネントの設定モデル"""
    debug: bool = False
    log_level: str = "INFO"
    # その他のコア設定項目

class LLMConfig(BaseModel):
    """LLMインターフェースの設定モデル"""
    default_provider: str = "openai"
    providers: Dict[str, Dict[str, Any]] = {}
    timeout: int = 30
    retry_attempts: int = 3
    # その他のLLM固有設定項目
```

#### 1.2.3 実装詳細

- **階層型設定**: ネストされた設定構造のサポート
- **環境オーバーライド**: 開発・テスト・本番環境ごとの設定
- **設定検証**: Pydanticモデルによる型検証
- **シングルトンパターン**: アプリケーション全体での一貫した設定アクセス

#### 1.2.4 依存関係

- **外部依存**: YAML/JSON parser, Pydantic
- **内部依存**: なし (他のコンポーネントから依存される)

### 1.3 Storage Layer

Storage Layerは、IdeaMarkドキュメントの永続化を担当するコンポーネントです。

#### 1.3.1 責務

- ドキュメントの永続化と読み込み
- 異なるストレージバックエンド（ファイル、データベース）の抽象化
- シリアライゼーションとデシリアライゼーション
- バックアップと復元

#### 1.3.2 インターフェース定義

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional, Union
from pathlib import Path
from dataclasses import dataclass

@dataclass
class DocumentMetadata:
    id: str
    version: str
    created_at: str
    updated_at: str
    tags: List[str] = None
    status: str = "active"
    extra: Dict[str, Any] = None

class Document:
    def __init__(self, content: Dict[str, Any], metadata: DocumentMetadata):
        self.content = content
        self.metadata = metadata
    
    @property
    def id(self) -> str:
        return self.metadata.id
    
    @property
    def version(self) -> str:
        return self.metadata.version

class StorageInterface(ABC):
    @abstractmethod
    async def save_document(self, document: Document) -> str:
        """ドキュメントを保存し、IDを返す"""
        pass
    
    @abstractmethod
    async def load_document(self, document_id: str, version: Optional[str] = None) -> Document:
        """指定されたIDとバージョンのドキュメントを読み込む"""
        pass
    
    @abstractmethod
    async def delete_document(self, document_id: str) -> bool:
        """ドキュメントを削除する"""
        pass
    
    @abstractmethod
    async def list_documents(self, filters: Optional[Dict[str, Any]] = None) -> List[DocumentMetadata]:
        """条件に合うドキュメントのメタデータリストを取得"""
        pass
    
    @abstractmethod
    async def document_exists(self, document_id: str) -> bool:
        """ドキュメントの存在確認"""
        pass
    
    @abstractmethod
    async def backup(self, target_path: Union[str, Path]) -> bool:
        """ストレージのバックアップを作成"""
        pass
    
    @abstractmethod
    async def restore(self, source_path: Union[str, Path]) -> bool:
        """バックアップからストレージを復元"""
        pass

class StorageManager:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.storage: StorageInterface = self._initialize_storage()
    
    def _initialize_storage(self) -> StorageInterface:
        """設定に基づいてストレージバックエンドを初期化"""
        storage_type = self.config.get("type", "file")
        if storage_type == "file":
            return FileStorage(self.config)
        elif storage_type == "database":
            return DatabaseStorage(self.config)
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")
```

#### 1.3.3 実装詳細

- **アダプタパターン**: 異なるストレージバックエンドのための実装
- **シリアライザー**: YAML/JSONフォーマット変換
- **リポジトリパターン**: ドキュメントへのアクセス抽象化
- **バージョン管理**: ドキュメントバージョンの管理
- **トランザクション管理**: 書き込み操作の整合性確保

#### 1.3.4 依存関係

- **外部依存**: ファイルI/O、データベースドライバ（オプション）
- **内部依存**: Config Management

### 1.4 IdeaMark Core

IdeaMark Coreは、IdeaMarkドキュメントの基本操作と構造管理を担当するコンポーネントです。

#### 1.4.1 責務

- ドキュメントのCRUD操作
- スキーマ検証と正規化
- refsの処理と解決
- ドキュメント操作のビジネスロジック

#### 1.4.2 インターフェース定義

```python
from typing import Dict, Any, List, Optional, Union
from pathlib import Path
from enum import Enum

class DocumentStatus(Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"

class IdeaMarkCore:
    def __init__(self, storage_manager: StorageManager, config_manager: ConfigManager):
        self.storage = storage_manager
        self.config = config_manager
    
    async def create_document(self, content: Dict[str, Any], metadata: Optional[Dict[str, Any]] = None) -> Document:
        """新規ドキュメントを作成"""
        # 内容の検証とドキュメント作成ロジック
        pass
    
    async def get_document(self, document_id: str, version: Optional[str] = None) -> Document:
        """ドキュメントを取得"""
        return await self.storage.load_document(document_id, version)
    
    async def update_document(self, document_id: str, content: Dict[str, Any]) -> Document:
        """ドキュメントを更新"""
        # 更新ロジックと検証
        pass
    
    async def delete_document(self, document_id: str) -> bool:
        """ドキュメントを削除"""
        return await self.storage.delete_document(document_id)
    
    async def validate_document(self, document: Union[Document, Dict[str, Any]]) -> bool:
        """ドキュメント構造の検証"""
        # スキーマ検証ロジック
        pass
    
    async def resolve_refs(self, document: Document) -> Document:
        """ドキュメント内のrefsを解決"""
        # refs解決ロジック
        pass
    
    async def import_document(self, file_path: Union[str, Path]) -> Document:
        """外部ファイルからドキュメントをインポート"""
        # インポートロジック
        pass
    
    async def export_document(self, document_id: str, format: str = "yaml", path: Optional[Union[str, Path]] = None) -> Union[str, bool]:
        """ドキュメントをエクスポート"""
        # エクスポートロジック
        pass
```

#### 1.4.3 実装詳細

- **ドメイン駆動設計**: 豊かなドメインモデルによる表現
- **バリデーションチェーン**: 段階的な検証プロセス
- **値オブジェクト**: 不変な値の表現
- **ファクトリーパターン**: 複雑なオブジェクト構築の抽象化
- **イベント通知**: 変更時のイベント発火

#### 1.4.4 依存関係

- **内部依存**: Storage Layer, Config Management, LLM Interface (オプション)

## 2. Service Layer コンポーネント設計

### 2.1 Versioning Service

Versioning Serviceは、ドキュメントのバージョン管理と差分計算を担当するコンポーネントです。

#### 2.1.1 責務

- バージョン履歴の追跡
- バージョン間の差分計算
- 変更のマージと競合解決

#### 2.1.2 インターフェース定義

```python
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime

@dataclass
class VersionInfo:
    version_id: str
    timestamp: datetime
    author: Optional[str] = None
    comment: Optional[str] = None
    parent_version: Optional[str] = None

@dataclass
class Diff:
    path: str
    old_value: Any
    new_value: Any
    operation: str  # "add", "remove", "change"

@dataclass
class DiffResult:
    diffs: List[Diff]
    summary: Dict[str, int]  # 変更タイプ別の集計

class VersioningService:
    def __init__(self, ideamark_core: IdeaMarkCore):
        self.core = ideamark_core
    
    async def get_version_history(self, document_id: str) -> List[VersionInfo]:
        """ドキュメントのバージョン履歴を取得"""
        pass
    
    async def create_version(self, document: Document, comment: Optional[str] = None) -> str:
        """新しいバージョンを作成"""
        pass
    
    async def compare_versions(self, document_id: str, version1: str, version2: str) -> DiffResult:
        """2つのバージョン間の差分を計算"""
        pass
    
    async def merge_versions(self, document_id: str, version1: str, version2: str) -> Tuple[Document, List[str]]:
        """2つのバージョンをマージし、結果と競合リストを返す"""
        pass
    
    async def resolve_conflict(self, document_id: str, conflict_id: str, resolution: Dict[str, Any]) -> bool:
        """特定の競合を解決"""
        pass
```

#### 2.1.3 依存関係

- **内部依存**: IdeaMark Core

### 2.2 Search Service

Search Serviceは、ドキュメントの検索とインデックス管理を担当するコンポーネントです。

#### 2.2.1 責務

- 検索インデックスの構築と管理
- 全文検索機能の提供
- 意味検索とタグベース検索

#### 2.2.2 インターフェース定義

```python
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass

@dataclass
class SearchResult:
    document_id: str
    version: str
    score: float
    highlight: Optional[Dict[str, List[str]]] = None
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class SearchQuery:
    query_text: str
    filters: Optional[Dict[str, Any]] = None
    sort: Optional[str] = None
    limit: int = 10
    offset: int = 0

class SearchService:
    def __init__(self, ideamark_core: IdeaMarkCore, config: Dict[str, Any]):
        self.core = ideamark_core
        self.config = config
        self.index_manager = self._initialize_index_manager()
    
    def _initialize_index_manager(self):
        # インデックスマネージャーの初期化
        pass
    
    async def index_document(self, document: Document) -> bool:
        """ドキュメントをインデックスに追加"""
        pass
    
    async def search(self, query: Union[str, SearchQuery]) -> List[SearchResult]:
        """検索を実行"""
        pass
    
    async def semantic_search(self, query: str, **kwargs) -> List[SearchResult]:
        """意味ベースの検索を実行"""
        pass
    
    async def tag_search(self, tags: List[str], **kwargs) -> List[SearchResult]:
        """タグベースの検索を実行"""
        pass
    
    async def rebuild_index(self) -> bool:
        """インデックスを再構築"""
        pass
```

#### 2.2.3 依存関係

- **外部依存**: 検索エンジン (Elasticsearch, FAISS など)
- **内部依存**: IdeaMark Core, LLM Interface (意味検索用)

### 2.3 Document Processing Service

Document Processing Serviceは、ドキュメントの分解、検証、統合を担当するコンポーネントです。

#### 2.3.1 責務

- ドキュメントの論理的分解
- 構造検証と整合性チェック
- 複数ドキュメントの統合

#### 2.3.2 インターフェース定義

```python
from typing import Dict, Any, List, Optional, Union
from dataclasses import dataclass

@dataclass
class ProcessingResult:
    success: bool
    message: Optional[str] = None
    details: Optional[Dict[str, Any]] = None

@dataclass
class DocumentPart:
    id: str
    content: Dict[str, Any]
    type: str
    parent_id: Optional[str] = None

class DocumentProcessingService:
    def __init__(self, ideamark_core: IdeaMarkCore, llm_manager: LLMManager = None):
        self.core = ideamark_core
        self.llm = llm_manager
    
    async def breakdown_document(self, document_id: str) -> List[DocumentPart]:
        """ドキュメントを論理的な部分に分解"""
        pass
    
    async def validate_structure(self, document_id: str) -> ProcessingResult:
        """ドキュメント構造の検証"""
        pass
    
    async def merge_documents(self, document_ids: List[str], merge_strategy: str = "default") -> Document:
        """複数のドキュメントを統合"""
        pass
    
    async def generate_outline(self, topics: List[str], depth: int = 2) -> Dict[str, Any]:
        """トピックリストからドキュメント概要を生成"""
        pass
    
    async def extract_topics(self, document_id: str) -> List[str]:
        """ドキュメントから主要トピックを抽出"""
        pass
```

#### 2.3.3 依存関係

- **内部依存**: IdeaMark Core, LLM Interface (オプション)

### 2.4 その他のサービスコンポーネント

以下は簡略化した他のサービスコンポーネントの概要です：

#### 2.4.1 Discussion Service

- **責務**: 議論スレッド管理、セッション追跡、コメント処理
- **主要インターフェース**: 
  - スレッド作成・取得・更新・削除
  - コメント追加・編集・削除
  - 議論内容の要約と分析

#### 2.4.2 Analytics Service

- **責務**: ドキュメント群の分析、傾向把握、視覚化
- **主要インターフェース**:
  - 統計情報計算
  - トピック分布分析
  - ギャップと重複の検出
  - レポート生成

#### 2.4.3 Link Management Service

- **責務**: 外部リソースの紐付け、リンク検証、同期
- **主要インターフェース**:
  - リンク追加・更新・削除
  - リンク検証と健全性確認
  - リンク先リソースの要約取得
  - 同期スケジュール管理

## 3. コンポーネント間の相互作用

### 3.1 主要ユースケースと相互作用フロー

#### 3.1.1 新規ドキュメント作成フロー

1. ユーザーがドキュメント作成リクエスト (Application Layer)
2. IdeaMarkコアが構造検証 (Core Layer)
3. ストレージレイヤーがドキュメント保存 (Core Layer)
4. バージョニングサービスが初期バージョン作成 (Service Layer)
5. 検索サービスがインデックス更新 (Service Layer)
6. 成功レスポンス返却 (Application Layer)

#### 3.1.2 ドキュメント検索フロー

1. ユーザーが検索クエリ送信 (Application Layer)
2. 検索サービスがクエリ処理 (Service Layer)
3. 必要に応じてLLMインターフェースで意味拡張 (Core Layer)
4. 検索結果取得と整形 (Service Layer)
5. 結果返却 (Application Layer)

#### 3.1.3 バージョン比較フロー

1. ユーザーが2バージョン指定でリクエスト (Application Layer)
2. バージョニングサービスが両バージョン取得 (Service Layer)
3. ドキュメント処理サービスが構造比較 (Service Layer)
4. 差分結果の整形と返却 (Service Layer → Application Layer)

### 3.2 コンポーネント間の依存関係図

```
┌────────────────────────────────────────────────────────────┐
│                   Application Layer                        │
└───────────────────────────┬──────────────────────────────┬─┘
                            │                              │
                            ▼                              ▼
┌─────────────────┐   ┌──────────────────┐   ┌─────────────────────┐
│ Discussion      │──►│ Document         │◄──┤ Analytics           │
│ Service         │   │ Processing       │   │ Service             │
└─────────┬───────┘   │ Service          │   └─────────────────────┘
          │           └────────┬─────────┘              ▲
          │                    │                        │
          │                    ▼                        │
┌─────────▼───────┐   ┌────────────────┐    ┌───────────┴─────────┐
│ Versioning      │◄──┤ IdeaMark Core  │───►│ Link Management     │
│ Service         │   └────────┬───────┘    │ Service             │
└─────────────────┘            │            └─────────────────────┘
                               │
          ┌───────────────────┬┴─────────────────────┐
          ▼                   ▼                     ▼
┌─────────────────┐   ┌───────────────┐    ┌─────────────────┐
│ Storage Layer   │   │ LLM Interface │    │ Config          │
│                 │   │               │    │ Management      │
└─────────────────┘   └───────────────┘    └─────────────────┘
```

## 4. 拡張ポイントと将来の拡張性

### 4.1 プラグイン拡張ポイント

- **LLMプロバイダー拡張**: 新しいLLMプロバイダーを追加可能
- **ストレージバックエンド拡張**: カスタムストレージ実装を追加可能
- **検索エンジン拡張**: 異なる検索バックエンドをサポート
- **カスタム処理パイプライン**: ドキュメント処理のカスタマイズ

### 4.2 将来の拡張計画

- **分散処理サポート**: 大規模データ処理のためのスケーラビリティ強化
- **リアルタイムコラボレーション**: 同時編集と変更通知
- **AIアシスタント統合**: より高度なAIアシスタント機能
- **ビジュアル表現**: グラフィカルなデータ表現とチャート

## 5. 実装ガイドライン

### 5.1 コーディング規約

- PEP 8に準拠したPythonコーディングスタイル
- 型ヒントの一貫した使用
- 詳細なドキュメンテーションコメント
- 単体テストの徹底

### 5.2 エラー処理方針

- 明示的な例外クラス階層
- 詳細なエラーメッセージ
- 回復可能なエラーとクリティカルエラーの区別
- ログ記録の徹底

### 5.3 パフォーマンス最適化

- 早期最適化の回避
- ボトルネック特定のためのプロファイリング
- メモリ使用量の監視と最適化
- 非同期処理の適切な活用
