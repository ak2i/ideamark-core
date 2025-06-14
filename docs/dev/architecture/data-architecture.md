# IdeaMark Core データアーキテクチャ

このドキュメントでは、IdeaMarkコアライブラリのデータモデル、データフロー、永続化戦略について詳細に説明します。

## 1. データモデル設計

### 1.1 コアデータモデル

IdeaMarkのコアデータモデルは、ドキュメントとその関連メタデータを表現するための構造を定義します。

#### 1.1.1 Document

メインのドキュメントエンティティで、コンテンツとメタデータを持ちます。

```yaml
# Document構造の例
Document:
  metadata:
    id: "doc-123456"
    version: "1.2.0"
    created_at: "2025-01-15T10:30:00Z"
    updated_at: "2025-06-10T14:22:33Z"
    author: "user@example.com"
    status: "active"
    tags: ["project-x", "planning", "2025-Q2"]
    title: "Project X Implementation Plan"
  content:
    # ドキュメント本体のコンテンツ
    schema_version: "1.0"
    sections:
      - id: "sec-overview"
        title: "Overview"
        content: "This document outlines the implementation plan for Project X..."
      - id: "sec-timeline"
        title: "Timeline"
        content: "The project will be executed in three phases..."
    references:
      - id: "ref-1"
        type: "external"
        url: "https://example.com/standards"
        description: "Industry standards document"
```

#### 1.1.2 DocumentMetadata

ドキュメントの属性情報を格納する構造です。

```python
@dataclass
class DocumentMetadata:
    id: str  # ドキュメント一意識別子
    version: str  # セマンティックバージョニング準拠のバージョン
    created_at: datetime  # 作成日時
    updated_at: datetime  # 最終更新日時
    author: Optional[str] = None  # 作成者
    status: str = "active"  # ドキュメントステータス (active, draft, archived, deleted)
    tags: List[str] = field(default_factory=list)  # 分類タグ
    title: Optional[str] = None  # ドキュメントタイトル
    description: Optional[str] = None  # 簡単な説明
    extra: Dict[str, Any] = field(default_factory=dict)  # 拡張メタデータ
```

#### 1.1.3 ContentSection

ドキュメントの内容を構造化するためのセクションモデルです。

```python
@dataclass
class ContentSection:
    id: str  # セクション識別子
    title: str  # セクションタイトル
    content: str  # セクション本文
    type: str = "text"  # セクションタイプ (text, code, table, etc.)
    parent_id: Optional[str] = None  # 親セクションID (階層構造用)
    order: int = 0  # 表示順序
    metadata: Dict[str, Any] = field(default_factory=dict)  # セクション固有メタデータ
```

#### 1.1.4 Reference

ドキュメント内の参照情報を表現するモデルです。

```python
@dataclass
class Reference:
    id: str  # 参照識別子
    type: str  # 参照タイプ (internal, external, etc.)
    target: str  # 参照先 (URL, ドキュメントID, etc.)
    description: Optional[str] = None  # 参照の説明
    metadata: Dict[str, Any] = field(default_factory=dict)  # 参照固有メタデータ
```

### 1.2 スキーマ設計

IdeaMarkドキュメントのスキーマはYAML形式で定義され、JSONスキーマ互換の検証ルールを提供します。

#### 1.2.1 IdeaMarkスキーマの基本構造

```yaml
# schema/ideamark.schema.yaml
$schema: "https://json-schema.org/draft/2020-12/schema"
title: "IdeaMark Document Schema"
type: "object"
required: ["metadata", "content"]

properties:
  metadata:
    type: "object"
    required: ["id", "version", "created_at", "updated_at"]
    properties:
      id:
        type: "string"
        pattern: "^[a-z0-9-]+$"
      version:
        type: "string"
        pattern: "^\\d+\\.\\d+\\.\\d+$"
      created_at:
        type: "string"
        format: "date-time"
      updated_at:
        type: "string"
        format: "date-time"
      author:
        type: "string"
      status:
        type: "string"
        enum: ["draft", "active", "archived", "deleted"]
      tags:
        type: "array"
        items:
          type: "string"
      title:
        type: "string"
      description:
        type: "string"
  
  content:
    type: "object"
    required: ["schema_version"]
    properties:
      schema_version:
        type: "string"
      sections:
        type: "array"
        items:
          type: "object"
          required: ["id", "title", "content"]
          properties:
            id:
              type: "string"
              pattern: "^[a-z0-9-]+$"
            title:
              type: "string"
            content:
              type: "string"
            type:
              type: "string"
            parent_id:
              type: ["string", "null"]
            order:
              type: "integer"
      
      references:
        type: "array"
        items:
          type: "object"
          required: ["id", "type", "target"]
          properties:
            id:
              type: "string"
              pattern: "^ref-[a-z0-9-]+$"
            type:
              type: "string"
              enum: ["internal", "external", "document", "section"]
            target:
              type: "string"
            description:
              type: "string"
```

#### 1.2.2 特化型ドキュメントスキーマ

特定の用途に特化したドキュメント型を定義できます。

```yaml
# schema/project_plan.schema.yaml
$schema: "https://json-schema.org/draft/2020-12/schema"
title: "Project Plan Document Schema"
allOf:
  - $ref: "ideamark.schema.yaml"  # 基本スキーマを継承
  - type: "object"
    properties:
      content:
        type: "object"
        properties:
          project_info:
            type: "object"
            required: ["start_date", "end_date", "stakeholders"]
            properties:
              start_date:
                type: "string"
                format: "date"
              end_date:
                type: "string"
                format: "date"
              stakeholders:
                type: "array"
                items:
                  type: "object"
                  required: ["name", "role"]
                  properties:
                    name:
                      type: "string"
                    role:
                      type: "string"
```

### 1.3 リレーショナルモデル

データベースストレージバックエンドを使用する場合のリレーショナルデータモデル定義です。

#### 1.3.1 テーブル構造

```
+-------------------+       +-------------------+       +-------------------+
| documents         |       | sections          |       | references        |
+-------------------+       +-------------------+       +-------------------+
| id                |<----->| document_id       |       | id                |
| version           |       | id                |<----->| document_id       |
| created_at        |       | title             |       | type              |
| updated_at        |       | content           |       | target            |
| author            |       | type              |       | description       |
| status            |       | parent_id         |       | created_at        |
| title             |       | order             |       | metadata          |
| description       |       | created_at        |       +-------------------+
| metadata          |       | updated_at        |               ^
+-------------------+       +-------------------+               |
        ^                            ^                          |
        |                            |                          |
        |                            |                          |
+-------------------+       +-------------------+               |
| document_tags     |       | document_versions |               |
+-------------------+       +-------------------+               |
| document_id       |       | document_id       |---------------+
| tag               |       | version           |
+-------------------+       | created_at        |
                            | change_summary    |
                            | author            |
                            | parent_version    |
                            +-------------------+
```

## 2. データフローと処理パイプライン

### 2.1 主要データフロー

#### 2.1.1 ドキュメント作成フロー

```
┌──────────┐     ┌─────────────┐     ┌───────────────┐     ┌────────────┐
│          │     │             │     │               │     │            │
│ User     │────>│ Application │────>│ IdeaMarkCore  │────>│ Validator  │
│ Request  │     │ Layer       │     │               │     │            │
│          │     │             │     │               │     │            │
└──────────┘     └─────────────┘     └───────┬───────┘     └─────┬──────┘
                                             │                   │
                                             │                   │
                                             ▼                   ▼
┌──────────┐     ┌─────────────┐     ┌───────────────┐     ┌────────────┐
│          │     │             │     │               │     │            │
│ Response │<────│ Application │<────│ Storage Layer │<────│ Document   │
│ to User  │     │ Layer       │     │               │     │ Factory    │
│          │     │             │     │               │     │            │
└──────────┘     └─────────────┘     └───────────────┘     └────────────┘
```

1. ユーザーがドキュメント作成リクエストを送信
2. アプリケーション層がリクエストを受け取りIdeaMarkCoreに転送
3. ドキュメントバリデーターがスキーマと整合性を検証
4. ドキュメントファクトリーが検証済みドキュメントを生成
5. ストレージレイヤーがドキュメントを永続化
6. 結果がユーザーに返される

#### 2.1.2 検索とインデックス更新フロー

```
┌──────────┐     ┌─────────────┐     ┌───────────────┐     ┌────────────┐
│          │     │             │     │               │     │            │
│ Document │────>│ Change      │────>│ Index         │────>│ Search     │
│ Update   │     │ Detector    │     │ Updater       │     │ Index      │
│          │     │             │     │               │     │            │
└──────────┘     └─────────────┘     └───────────────┘     └────────────┘

┌──────────┐     ┌─────────────┐     ┌───────────────┐     ┌────────────┐
│          │     │             │     │               │     │            │
│ Search   │────>│ Query       │────>│ Search        │────>│ Result     │
│ Request  │     │ Parser      │     │ Executor      │     │ Formatter  │
│          │     │             │     │               │     │            │
└──────────┘     └─────────────┘     └───────┬───────┘     └─────┬──────┘
                                             │                   │
                                             ▼                   ▼
                                     ┌───────────────┐     ┌────────────┐
                                     │               │     │            │
                                     │ Search Index  │     │ Search     │
                                     │               │     │ Results    │
                                     │               │     │            │
                                     └───────────────┘     └────────────┘
```

### 2.2 データ変換パイプライン

#### 2.2.1 ドキュメント処理パイプライン

```
┌───────────┐     ┌───────────┐     ┌───────────┐     ┌───────────┐
│           │     │           │     │           │     │           │
│ Raw Input │────>│ Parser    │────>│ Validator │────>│ Normalizer│
│           │     │           │     │           │     │           │
└───────────┘     └───────────┘     └───────────┘     └─────┬─────┘
                                                            │
                                                            ▼
┌───────────┐     ┌───────────┐     ┌───────────┐     ┌───────────┐
│           │     │           │     │           │     │           │
│ Processed │<────│ Assembler │<────│ Enricher  │<────│ Schema    │
│ Document  │     │           │     │           │     │ Applier   │
│           │     │           │     │           │     │           │
└───────────┘     └───────────┘     └───────────┘     └───────────┘
```

1. パーサー: 入力をパースして初期構造を作成
2. バリデーター: 基本的な構文と構造を検証
3. ノーマライザー: フォーマットの標準化と正規化
4. スキーマアプライヤー: スキーマを適用して型を保証
5. エンリッチャー: メタデータなどで情報を充実
6. アセンブラー: 最終的なドキュメント構造を組み立て

#### 2.2.2 検索インデックスパイプライン

```
┌───────────┐     ┌───────────┐     ┌───────────┐     ┌───────────┐
│           │     │           │     │           │     │           │
│ Document  │────>│ Content   │────>│ Tokenizer │────>│ Analyzer  │
│           │     │ Extractor │     │           │     │           │
└───────────┘     └───────────┘     └───────────┘     └─────┬─────┘
                                                            │
                                                            ▼
┌───────────┐     ┌───────────┐     ┌───────────┐     ┌───────────┐
│           │     │           │     │           │     │           │
│ Index     │<────│ Index     │<────│ Vector    │<────│ Filter    │
│ Entry     │     │ Writer    │     │ Generator │     │ Pipeline  │
│           │     │           │     │           │     │           │
└───────────┘     └───────────┘     └───────────┘     └───────────┘
```

## 3. 永続化戦略

### 3.1 ファイルストレージ実装

ファイルシステムをベースにしたストレージバックエンドの実装方針です。

#### 3.1.1 ディレクトリ構造

```
ideamark_data/
├── documents/
│   ├── doc-123456/
│   │   ├── current.yaml        # 最新バージョンのドキュメント
│   │   ├── metadata.json       # ドキュメントメタデータ
│   │   └── versions/
│   │       ├── 1.0.0.yaml      # バージョン1.0.0
│   │       ├── 1.1.0.yaml      # バージョン1.1.0
│   │       └── 1.2.0.yaml      # バージョン1.2.0
│   └── doc-789012/
│       └── ...
├── indexes/
│   ├── fulltext/               # 全文検索インデックス
│   ├── semantic/               # 意味検索インデックス
│   └── tags/                   # タグインデックス
├── refs/                       # 参照リンク情報
│   └── ...
├── backups/                    # バックアップデータ
│   └── ...
└── config/                     # 設定ファイル
    └── ...
```

#### 3.1.2 ファイル形式

- **ドキュメント本体**: YAML形式（人間可読性と編集のしやすさ）
- **メタデータ**: JSON形式（処理効率の高さ）
- **インデックス**: バイナリ形式またはSQLite（効率的なクエリ）
- **設定**: YAML形式（階層構造の表現とコメント対応）

#### 3.1.3 ファイルロック戦略

- **読み取り/書き込みロック**: 複数プロセスからのアクセスを制御
- **一時ファイル**: 書き込み中の破損防止のための一時ファイル使用
- **アトミック操作**: 名前変更によるアトミックな更新

### 3.2 データベースストレージ実装

リレーショナルデータベースをベースにしたストレージバックエンドの実装方針です。

#### 3.2.1 データベーススキーマ

```sql
-- ドキュメントテーブル
CREATE TABLE documents (
    id VARCHAR(64) PRIMARY KEY,
    current_version VARCHAR(16) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL,
    author VARCHAR(128),
    status VARCHAR(16) NOT NULL DEFAULT 'active',
    title TEXT,
    description TEXT,
    metadata JSONB
);

-- ドキュメントバージョンテーブル
CREATE TABLE document_versions (
    document_id VARCHAR(64) REFERENCES documents(id),
    version VARCHAR(16) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    content JSONB NOT NULL,
    change_summary TEXT,
    author VARCHAR(128),
    parent_version VARCHAR(16),
    PRIMARY KEY (document_id, version)
);

-- ドキュメントタグテーブル
CREATE TABLE document_tags (
    document_id VARCHAR(64) REFERENCES documents(id),
    tag VARCHAR(64) NOT NULL,
    PRIMARY KEY (document_id, tag)
);

-- セクションテーブル
CREATE TABLE sections (
    id VARCHAR(64) NOT NULL,
    document_id VARCHAR(64) REFERENCES documents(id),
    version VARCHAR(16) NOT NULL,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    type VARCHAR(32) DEFAULT 'text',
    parent_id VARCHAR(64),
    section_order INT DEFAULT 0,
    metadata JSONB,
    PRIMARY KEY (id, document_id, version),
    FOREIGN KEY (document_id, version) REFERENCES document_versions(document_id, version)
);

-- 参照テーブル
CREATE TABLE references (
    id VARCHAR(64) NOT NULL,
    document_id VARCHAR(64) REFERENCES documents(id),
    version VARCHAR(16) NOT NULL,
    type VARCHAR(32) NOT NULL,
    target TEXT NOT NULL,
    description TEXT,
    metadata JSONB,
    PRIMARY KEY (id, document_id, version),
    FOREIGN KEY (document_id, version) REFERENCES document_versions(document_id, version)
);
```

#### 3.2.2 インデックス戦略

```sql
-- パフォーマンス向上のためのインデックス
CREATE INDEX idx_documents_status ON documents(status);
CREATE INDEX idx_documents_updated ON documents(updated_at);
CREATE INDEX idx_document_tags ON document_tags(tag);
CREATE INDEX idx_sections_parent ON sections(parent_id);
CREATE INDEX idx_references_target ON references(target);

-- 全文検索インデックス
CREATE INDEX idx_document_title_trgm ON documents USING GIN (title gin_trgm_ops);
CREATE INDEX idx_sections_content_trgm ON sections USING GIN (content gin_trgm_ops);
```

#### 3.2.3 トランザクション管理

- **ACID準拠**: データ整合性を確保するための完全なトランザクション
- **楽観的ロック**: バージョン番号を用いた競合検出
- **バッチ処理**: 大量更新時のパフォーマンス最適化

### 3.3 ストレージ抽象化レイヤー

異なるストレージバックエンドを透過的に使用するための抽象化レイヤーです。

#### 3.3.1 StorageInterface

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional, Union
from pathlib import Path
from dataclasses import dataclass

@dataclass
class StorageOptions:
    """ストレージバックエンド固有のオプション"""
    cache_enabled: bool = True
    auto_backup: bool = False
    compression: bool = False
    extra_options: Dict[str, Any] = None

class StorageInterface(ABC):
    @abstractmethod
    async def initialize(self, options: Optional[StorageOptions] = None) -> bool:
        """ストレージバックエンドの初期化"""
        pass
    
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
    async def list_versions(self, document_id: str) -> List[str]:
        """ドキュメントの全バージョンリストを取得"""
        pass
    
    @abstractmethod
    async def backup(self, target_path: Union[str, Path]) -> bool:
        """ストレージのバックアップを作成"""
        pass
    
    @abstractmethod
    async def restore(self, source_path: Union[str, Path]) -> bool:
        """バックアップからストレージを復元"""
        pass

    @abstractmethod
    async def health_check(self) -> Dict[str, Any]:
        """ストレージの健全性チェック"""
        pass
```

#### 3.3.2 ストレージファクトリー

```python
class StorageFactory:
    """ストレージインスタンスの生成を担当するファクトリークラス"""
    
    @staticmethod
    def create_storage(storage_type: str, config: Dict[str, Any]) -> StorageInterface:
        """設定に基づいて適切なストレージインスタンスを生成"""
        if storage_type == "file":
            return FileStorage(config)
        elif storage_type == "database":
            return DatabaseStorage(config)
        elif storage_type == "memory":
            return MemoryStorage(config)
        elif storage_type == "remote":
            return RemoteStorage(config)
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")
```

### 3.4 バックアップと復元戦略

#### 3.4.1 バックアップ種別

- **フルバックアップ**: 全データの完全コピー
- **増分バックアップ**: 前回バックアップからの変更のみ
- **スケジュールバックアップ**: 時間ベースの自動バックアップ
- **オンデマンドバックアップ**: ユーザー起動のバックアップ

#### 3.4.2 バックアップ実装

```python
class BackupService:
    def __init__(self, storage: StorageInterface, config: Dict[str, Any]):
        self.storage = storage
        self.config = config
        self.backup_path = Path(config.get("backup_path", "./ideamark_backups"))
        self.backup_format = config.get("backup_format", "zip")
    
    async def create_backup(self, backup_type: str = "full") -> str:
        """バックアップを作成し、バックアップファイルのパスを返す"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"ideamark_backup_{backup_type}_{timestamp}"
        
        if backup_type == "full":
            backup_path = self.backup_path / f"{backup_name}.{self.backup_format}"
            await self.storage.backup(backup_path)
            return str(backup_path)
        elif backup_type == "incremental":
            # 増分バックアップの実装
            pass
        else:
            raise ValueError(f"Unsupported backup type: {backup_type}")
    
    async def restore_backup(self, backup_path: Union[str, Path]) -> bool:
        """バックアップからデータを復元"""
        return await self.storage.restore(backup_path)
    
    async def list_backups(self) -> List[Dict[str, Any]]:
        """利用可能なバックアップの一覧を取得"""
        backups = []
        for file in self.backup_path.glob(f"ideamark_backup_*.{self.backup_format}"):
            # バックアップ情報の抽出
            backups.append({
                "path": str(file),
                "size": file.stat().st_size,
                "created_at": datetime.fromtimestamp(file.stat().st_mtime).isoformat(),
                "type": "full" if "full" in file.name else "incremental"
            })
        return backups
    
    async def cleanup_old_backups(self, max_age_days: int = 30) -> int:
        """古いバックアップを削除し、削除数を返す"""
        cutoff_time = datetime.now() - timedelta(days=max_age_days)
        deleted_count = 0
        
        for file in self.backup_path.glob(f"ideamark_backup_*.{self.backup_format}"):
            if datetime.fromtimestamp(file.stat().st_mtime) < cutoff_time:
                file.unlink()
                deleted_count += 1
        
        return deleted_count
```

## 4. キャッシュ戦略

### 4.1 キャッシュレベル

- **メモリキャッシュ**: 頻繁にアクセスされるデータ用
- **ディスクキャッシュ**: 大きいが比較的頻繁に使用されるデータ用
- **結果キャッシュ**: 計算コストの高いクエリ結果用

### 4.2 キャッシュ実装

```python
from functools import lru_cache
from typing import Dict, Any, Optional, TypeVar, Generic
from datetime import datetime, timedelta

T = TypeVar('T')

class CacheEntry(Generic[T]):
    def __init__(self, value: T, ttl_seconds: Optional[int] = None):
        self.value = value
        self.created_at = datetime.now()
        self.expires_at = self.created_at + timedelta(seconds=ttl_seconds) if ttl_seconds else None
    
    @property
    def is_expired(self) -> bool:
        if self.expires_at is None:
            return False
        return datetime.now() > self.expires_at

class Cache(Generic[T]):
    def __init__(self, max_size: int = 100, default_ttl: Optional[int] = 300):
        self.max_size = max_size
        self.default_ttl = default_ttl
        self.cache: Dict[str, CacheEntry[T]] = {}
    
    def get(self, key: str) -> Optional[T]:
        """キャッシュからアイテムを取得。存在しないか期限切れならNone"""
        entry = self.cache.get(key)
        if entry is None or entry.is_expired:
            if entry and entry.is_expired:
                self.delete(key)
            return None
        return entry.value
    
    def set(self, key: str, value: T, ttl: Optional[int] = None) -> None:
        """キャッシュにアイテムを設定"""
        # キャッシュサイズチェック
        if len(self.cache) >= self.max_size and key not in self.cache:
            self._evict_oldest()
        
        ttl_seconds = ttl if ttl is not None else self.default_ttl
        self.cache[key] = CacheEntry(value, ttl_seconds)
    
    def delete(self, key: str) -> bool:
        """キャッシュからアイテムを削除"""
        if key in self.cache:
            del self.cache[key]
            return True
        return False
    
    def clear(self) -> None:
        """キャッシュをクリア"""
        self.cache.clear()
    
    def _evict_oldest(self) -> None:
        """最も古いキャッシュエントリを削除"""
        oldest_key = None
        oldest_time = None
        
        for key, entry in self.cache.items():
            if oldest_time is None or entry.created_at < oldest_time:
                oldest_key = key
                oldest_time = entry.created_at
        
        if oldest_key:
            self.delete(oldest_key)

# デコレーターとしても使用可能
@lru_cache(maxsize=128)
def expensive_computation(arg1, arg2):
    # 計算コストの高い処理
    return result
```

## 5. データバージョニングと移行戦略

### 5.1 スキーマバージョニング

- **スキーマバージョン番号**: すべてのスキーマに明示的なバージョン番号
- **後方互換性**: 新バージョンは旧バージョンのドキュメントを読み取り可能
- **スキーマ履歴**: 以前のスキーマバージョンの保存

### 5.2 データ移行

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, List

class Migration(ABC):
    """マイグレーション基底クラス"""
    
    @property
    @abstractmethod
    def source_version(self) -> str:
        """移行元のスキーマバージョン"""
        pass
    
    @property
    @abstractmethod
    def target_version(self) -> str:
        """移行先のスキーマバージョン"""
        pass
    
    @abstractmethod
    async def migrate(self, document: Dict[str, Any]) -> Dict[str, Any]:
        """ドキュメントを移行"""
        pass

class MigrationManager:
    def __init__(self):
        self.migrations: Dict[str, Dict[str, Migration]] = {}
    
    def register_migration(self, migration: Migration) -> None:
        """マイグレーションを登録"""
        if migration.source_version not in self.migrations:
            self.migrations[migration.source_version] = {}
        
        self.migrations[migration.source_version][migration.target_version] = migration
    
    async def migrate_document(self, document: Dict[str, Any], target_version: str) -> Dict[str, Any]:
        """ドキュメントを特定のバージョンに移行"""
        current_version = document.get("content", {}).get("schema_version", "unknown")
        
        if current_version == target_version:
            return document
        
        path = self._find_migration_path(current_version, target_version)
        if not path:
            raise ValueError(f"No migration path from {current_version} to {target_version}")
        
        result = document
        for i in range(len(path) - 1):
            source = path[i]
            target = path[i + 1]
            migration = self.migrations[source][target]
            result = await migration.migrate(result)
        
        return result
    
    def _find_migration_path(self, source: str, target: str) -> List[str]:
        """利用可能なマイグレーションから最短パスを見つける"""
        # 簡易的な幅優先探索で最短パスを探索
        visited = {source}
        queue = [[source]]
        
        while queue:
            path = queue.pop(0)
            node = path[-1]
            
            if node == target:
                return path
            
            for next_node in self.migrations.get(node, {}):
                if next_node not in visited:
                    visited.add(next_node)
                    queue.append(path + [next_node])
        
        return []  # パスが見つからない
```

### 5.3 ダウングレード対応

- **リバースマイグレーション**: 新バージョンから旧バージョンへの移行
- **データ損失の最小化**: ダウングレード時のデータ保持戦略
- **バージョン互換性マトリックス**: サポート対象バージョンの明確化

## 6. データセキュリティ

### 6.1 暗号化戦略

- **保存時の暗号化**: データベースまたはファイルに保存されるデータの暗号化
- **転送時の暗号化**: API通信やリモートストレージアクセス時の暗号化
- **キー管理**: 暗号化キーの安全な管理と定期的な更新

### 6.2 アクセス制御

- **オーナーシップ**: ドキュメント所有者の概念
- **アクセスレベル**: 読取・更新・削除などの権限
- **ロールベースアクセス制御**: ユーザーロールに基づく権限管理

### 6.3 監査ログ

- **変更追跡**: すべてのドキュメント変更を記録
- **アクセスログ**: 参照・検索操作の記録
- **セキュリティイベント**: 認証・権限関連イベントのログ記録
