# IdeaMark Core アーキテクチャ詳細仕様

このドキュメントは、IdeaMark コアライブラリのアーキテクチャの詳細な技術仕様を定義します。このドキュメントは[アーキテクチャ要件定義](./ideamark_core_architecture.md)に基づいた具体的な実装仕様を提供します。

## 1. Core Layer 詳細仕様

### 1.1 LLM Interface 実装仕様

外部LLMとの連携を統一インターフェースで抽象化し、プロバイダーの切り替えを容易にするための具体的実装を定義します。

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

### 1.2 Config Management 実装仕様

全コンポーネントで共通利用される設定を一元管理するための実装仕様を定義します。

```yaml
# config/ideamark.yaml
llm:
  default_provider: "openai"
  providers:
    openai:
      api_key: "${OPENAI_API_KEY}"
      model_name: "gpt-4"
      base_url: null
      max_tokens: 4000
      temperature: 0.7
    anthropic:
      api_key: "${ANTHROPIC_API_KEY}"
      model_name: "claude-3-sonnet-20240229"
      max_tokens: 4000
      temperature: 0.7
    local:
      base_url: "http://localhost:11434"
      model_name: "llama2"
      api_key: null

ideamark:
  storage:
    type: "file"  # file | database
    path: "./ideamark_data"
  versioning:
    enabled: true
    max_history: 100
  search:
    index_type: "simple"  # simple | elasticsearch
    enable_tags: true
```

```python
class ConfigManager:
    def __init__(self, config_path: str = None):
        self.config_path = config_path or self._find_config_file()
        self.config = self._load_config()
    
    def _find_config_file(self) -> str:
        # プロジェクトルート、ホームディレクトリ、システム設定の順で探索
        candidates = [
            "./ideamark.yaml",
            "~/.ideamark/config.yaml",
            "/etc/ideamark/config.yaml"
        ]
        for path in candidates:
            if Path(path).exists():
                return path
        return "./ideamark.yaml"  # デフォルト
    
    def get_llm_config(self, provider: str = None) -> LLMConfig:
        pass
    
    def get_storage_config(self) -> Dict:
        pass
```

### 1.3 Storage Layer 実装仕様

IdeaMarkドキュメントの永続化を抽象化し、ファイルシステムやデータベース等の実装を切り替え可能にします。

```python
from abc import ABC, abstractmethod
from typing import List, Optional, Dict
from ideamark.core.models import IdeaMarkDocument

class StorageInterface(ABC):
    @abstractmethod
    async def save_document(self, doc: IdeaMarkDocument) -> str:
        pass
    
    @abstractmethod
    async def load_document(self, doc_id: str) -> Optional[IdeaMarkDocument]:
        pass
    
    @abstractmethod
    async def list_documents(self, filters: Dict = None) -> List[str]:
        pass
    
    @abstractmethod
    async def delete_document(self, doc_id: str) -> bool:
        pass

class FileStorage(StorageInterface):
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)

class DatabaseStorage(StorageInterface):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
```

## 2. Service Layer 詳細仕様

### 2.1 Discussion Service 実装仕様

複数ユーザーによる議論やセッション管理を提供します。

```python
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class DiscussionSession:
    session_id: str
    participants: List[str]
    ideamark_refs: List[str]
    created_at: datetime
    status: str  # active | closed | archived

@dataclass
class DiscussionMessage:
    message_id: str
    session_id: str
    author: str
    content: str
    message_type: str  # comment | suggestion | question | decision
    ideamark_ref: Optional[str]
    timestamp: datetime
    parent_message_id: Optional[str]

class DiscussionService:
    def __init__(self, storage: StorageInterface, llm_manager: LLMManager):
        self.storage = storage
        self.llm_manager = llm_manager
    
    async def create_session(self, participants: List[str], ideamark_refs: List[str]) -> DiscussionSession:
        pass
    
    async def add_message(self, session_id: str, message: DiscussionMessage) -> str:
        pass
    
    async def get_session_history(self, session_id: str) -> List[DiscussionMessage]:
        pass
    
    async def ai_suggest_response(self, session_id: str, context: str) -> str:
        # LLMを使って応答案を生成
        pass
```

### 2.2 Versioning Service 実装仕様

IdeaMarkのrefsを活用したバージョン管理と差分計算を提供します。

```python
class VersioningService:
    def __init__(self, storage: StorageInterface):
        self.storage = storage
    
    async def create_version(self, doc: IdeaMarkDocument, parent_id: Optional[str] = None) -> str:
        # refsを使ってバージョン管理
        if parent_id:
            doc.add_ref("previous_version", parent_id)
        return await self.storage.save_document(doc)
    
    async def get_version_history(self, doc_id: str) -> List[IdeaMarkDocument]:
        pass
    
    async def calculate_diff(self, old_id: str, new_id: str) -> Dict:
        # 差分計算ロジック
        pass
    
    async def merge_versions(self, base_id: str, branch_ids: List[str]) -> str:
        # 複数バージョンのマージ
        pass
```

### 2.3 Search Service 実装仕様

インデックス構築、検索、タグ管理を提供します。

```python
class SearchService:
    def __init__(self, storage: StorageInterface):
        self.storage = storage
        self.index = {}
        self.vocabulary = {}
    
    async def index_document(self, doc: IdeaMarkDocument):
        pass
    
    async def search(self, query: str, filters: Dict = None) -> List[str]:
        pass
    
    async def get_tags(self) -> Dict[str, int]:
        pass
    
    async def build_vocabulary(self, docs: List[IdeaMarkDocument]) -> Dict[str, Any]:
        # 語彙辞書の構築
        pass
    
    async def suggest_related_terms(self, term: str) -> List[str]:
        # 関連語の提案
        pass
    
    async def build_index(self, doc_paths: List[str], merge: bool = False) -> Dict:
        # 逆引きインデックス構築
        pass
    
    async def build_vocabulary(self, doc_paths: List[str]) -> Dict:
        # 語彙辞書構築
        pass
    
    async def suggest_terms(self, term: str, expand: bool = False) -> Dict:
        # 類義語・関連語提示
        pass
    
    async def fuzzy_search(self, query: str, threshold: float = 0.8) -> List[str]:
        # ファジー検索（語彙辞書活用）
        pass
```

### 2.4 Document Processing Service 実装仕様

Document Processing Serviceは、ドキュメントの処理に関する機能を提供します。主要機能として、ドキュメントの分解（breakdown）、マージ（merge）、構造検証（validate）があります。

```python
from typing import Dict, Any, List, Tuple, Optional
from enum import Enum

class MergeIntent(Enum):
    UNION = "union"            # 2つのパターンを組み合わせる
    EXTENSION = "extension"    # 既存のパターンを拡張する
    REFINEMENT = "refinement"  # 既存のパターンを洗練する

class MergeStrategy(Enum):
    PREFER = "prefer"         # 優先順位に基づいてセクションを選択
    ANNOTATE = "annotate"     # すべてのソースからのコンテンツを注釈付きで保持
    SYNTHESIS = "synthesis"   # LLMを使用してコンテンツを統合
    MANUAL = "manual"         # 手動での解決を要求（TODO項目として）

class DocumentProcessingService:
    def __init__(self, storage: StorageInterface, llm_manager: LLMManager, config_manager: ConfigManager):
        self.storage = storage
        self.llm_manager = llm_manager
        self.config = config_manager
        self.validator = self._create_validator()
        self.prompt_manager = self._create_prompt_manager()
    
    def _create_validator(self) -> 'DocumentValidator':
        return DocumentValidator(self.config.get_schema_path())
    
    def _create_prompt_manager(self) -> 'PromptManager':
        return PromptManager(self.config.get_prompts_path())
    
    async def breakdown_document(self, doc_id: str, strategy: str = "patterns") -> List[str]:
        """
        抽象ドキュメントを具体的サブドキュメントに分解します
        
        Args:
            doc_id: 分解するドキュメントのID
            strategy: 分解戦略（patterns/hierarchical/domain など）
            
        Returns:
            生成されたサブドキュメントIDのリスト
        """
        doc = await self.storage.load_document(doc_id)
        if not doc:
            raise ValueError(f"Document not found: {doc_id}")
            
        # TODO: 実装の詳細を追加
        pass
    
    async def merge_documents(self, 
                             doc_ids: List[str], 
                             intent: MergeIntent = MergeIntent.UNION,
                             strategy: MergeStrategy = MergeStrategy.PREFER,
                             priority_order: List[str] = None) -> Tuple[str, Dict[str, Any]]:
        """
        複数のドキュメントをマージして新しいドキュメントを生成します
        
        Args:
            doc_ids: マージするドキュメントIDのリスト
            intent: マージの意図（統合/拡張/洗練）
            strategy: 競合解決戦略
            priority_order: ドキュメントの優先順位（指定がない場合はdoc_idsの順序を使用）
            
        Returns:
            (新しいドキュメントID, マージサマリー情報)のタプル
        """
        if not doc_ids or len(doc_ids) < 2:
            raise ValueError("At least two documents are required for merging")
        
        docs = []
        for doc_id in doc_ids:
            doc = await self.storage.load_document(doc_id)
            if not doc:
                raise ValueError(f"Document not found: {doc_id}")
            docs.append(doc)
        
        if not priority_order:
            priority_order = doc_ids.copy()
        
        conflict_resolver = ConflictResolver(self.llm_manager, self.prompt_manager)
        merge_processor = MergeProcessor(strategy, conflict_resolver, priority_order)
        
        merged_doc, summary = merge_processor.merge(docs, intent)
        
        # ドキュメント検証
        validation_result = await self.validate_structure(merged_doc)
        if validation_result.get('errors', []):
            summary['validation_errors'] = validation_result['errors']
        
        # 保存
        new_doc_id = await self.storage.save_document(merged_doc)
        summary['new_doc_id'] = new_doc_id
        
        return new_doc_id, summary
    
    async def validate_structure(self, doc: IdeaMarkDocument) -> Dict[str, Any]:
        """
        ドキュメント構造の妥当性を検証します
        
        Args:
            doc: 検証するドキュメント
            
        Returns:
            検証結果（errors, warnings, suggestions を含む辞書）
        """
        validation_result = {
            'errors': [],
            'warnings': [],
            'suggestions': []
        }
        
        # スキーマ検証
        schema_errors = self.validator.validate_against_schema(doc)
        if schema_errors:
            validation_result['errors'].extend(schema_errors)
        
        # コンテンツ整合性チェック
        content_issues = self.validator.check_content_consistency(doc)
        if content_issues.get('errors'):
            validation_result['errors'].extend(content_issues['errors'])
        if content_issues.get('warnings'):
            validation_result['warnings'].extend(content_issues['warnings'])
        
        # 改善提案（オプション）
        if self.config.get_enable_suggestions():
            suggestions = await self._generate_improvement_suggestions(doc)
            validation_result['suggestions'] = suggestions
        
        return validation_result
    
    async def _generate_improvement_suggestions(self, doc: IdeaMarkDocument) -> List[str]:
        """LLMを使用してドキュメント改善の提案を生成します"""
        if not self.llm_manager:
            return []
        
        prompt = self.prompt_manager.get_prompt('document_suggestions', document=doc.to_dict())
        try:
            response = await self.llm_manager.generate(prompt)
            return self._parse_suggestions(response)
        except Exception as e:
            logger.error(f"Failed to generate suggestions: {e}")
            return []
    
    def _parse_suggestions(self, llm_response: str) -> List[str]:
        """LLMレスポンスから改善提案を抽出します"""
        # TODO: 実装の詳細を追加
        pass
```

#### ConflictResolver 実装仕様

マージ処理での競合解決を担当するクラスです。

```python
class ConflictResolver:
    def __init__(self, llm_manager: LLMManager, prompt_manager: PromptManager):
        self.llm_manager = llm_manager
        self.prompt_manager = prompt_manager
    
    async def resolve_manual(self, field_name: str, values: List[Dict[str, Any]], 
                           source_ids: List[str]) -> Any:
        """
        手動解決のためのプレースホルダを生成します
        
        Args:
            field_name: 競合しているフィールド名
            values: 競合している値のリスト (各値は {'value': 値, 'source_id': ソースID} の形式)
            source_ids: ソースドキュメントIDのリスト
            
        Returns:
            TODOプレースホルダまたはオプション付きの辞書
        """
        source_list = ", ".join(source_ids)
        
        # 特殊ケース: メタデータフィールド
        if field_name.startswith("metadata.") and values and isinstance(values[0]['value'], dict):
            return {
                "TODO": f"resolve conflict between {source_list} for {field_name}",
                "options": {f"option_{i}": val['value'] for i, val in enumerate(values)}
            }
        
        placeholder = f"TODO: resolve conflict between {source_list} for {field_name}"
        logger.debug(f"Created manual placeholder for {field_name}")
        return placeholder
    
    async def resolve_prefer(self, field_name: str, values: List[Dict[str, Any]], 
                           priority_order: List[str]) -> Any:
        """
        優先順位に基づいて競合を解決します
        
        Args:
            field_name: 競合しているフィールド名
            values: 競合している値のリスト
            priority_order: 優先順位（ドキュメントIDのリスト）
            
        Returns:
            優先順位に基づいて選択された値
        """
        for source_id in priority_order:
            for value_info in values:
                if value_info['source_id'] == source_id:
                    logger.debug(f"Resolved {field_name} using prefer strategy: chose {source_id}")
                    return value_info['value']
        
        logger.warning(f"No value found in priority order for {field_name}, using first available")
        return values[0]['value'] if values else None
    
    async def resolve_annotate(self, field_name: str, values: List[Dict[str, Any]], 
                             priority_order: List[str]) -> Any:
        """
        すべての値を注釈付きで保持します
        
        Args:
            field_name: 競合しているフィールド名
            values: 競合している値のリスト
            priority_order: 優先順位
            
        Returns:
            注釈付きの統合値
        """
        # 特殊ケース: メタデータフィールド
        if field_name.startswith("metadata.") and values and isinstance(values[0]['value'], dict):
            annotated_obj = {
                "annotation": f"Merged from {len(values)} sources",
                "sources": {}
            }
            
            for source_id in priority_order:
                for value_info in values:
                    if value_info['source_id'] == source_id:
                        annotated_obj["sources"][source_id] = value_info['value']
                        break
            
            if values:
                annotated_obj.update(values[0]['value'])
            
            logger.debug(f"Created annotated object resolution for {field_name}")
            return annotated_obj
        
        # テキストフィールドの場合
        annotated_parts = []
        
        for source_id in priority_order:
            for value_info in values:
                if value_info['source_id'] == source_id:
                    annotated_parts.append(f"[From {source_id}] {value_info['value']}")
                    break
        
        result = "\n".join(annotated_parts)
        logger.debug(f"Created annotated resolution for {field_name}")
        return result
    
    async def resolve_synthesis(self, field_name: str, values: List[Dict[str, Any]], 
                              prompt_template: str) -> str:
        """
        LLMを使用して競合値を統合します
        
        Args:
            field_name: 競合しているフィールド名
            values: 競合している値のリスト
            prompt_template: LLMへのプロンプトテンプレート
            
        Returns:
            統合されたテキスト
        """
        if not self.llm_manager:
            logger.warning(f"No LLM provider available for synthesis, falling back to manual for {field_name}")
            return await self.resolve_manual(field_name, values, [v['source_id'] for v in values])
        
        if len(values) < 2:
            return values[0]['value'] if values else ""
        
        try:
            # 単純化のため2つの値のみサポート（複数の場合は再帰的に処理する必要がある）
            text_a = values[0]['value']
            text_b = values[1]['value']
            
            # プロンプト生成
            prompt = self.prompt_manager.get_prompt('merge_field', 
                                                  field_name=field_name,
                                                  text_a=text_a,
                                                  text_b=text_b)
            
            # LLMによる統合
            result = await self.llm_manager.generate(prompt)
            logger.debug(f"Successfully synthesized {field_name} using LLM")
            return result
            
        except Exception as e:
            logger.error(f"LLM synthesis failed for {field_name}: {e}")
            return await self.resolve_manual(field_name, values, [v['source_id'] for v in values])
```

#### MergeProcessor 実装仕様

マージプロセスの中核ロジックを担当するクラスです。

```python
class MergeProcessor:
    def __init__(self, strategy: MergeStrategy, conflict_resolver: ConflictResolver, 
                priority_order: List[str] = None):
        """
        Args:
            strategy: マージ戦略
            conflict_resolver: 競合解決ハンドラ
            priority_order: ドキュメント優先順位
        """
        self.strategy = strategy
        self.conflict_resolver = conflict_resolver
        self.priority_order = priority_order or []
        self.conflicts_detected = []
        self.summary = {}
    
    def merge(self, documents: List[IdeaMarkDocument], 
             intent: MergeIntent) -> Tuple[IdeaMarkDocument, Dict[str, Any]]:
        """
        複数のドキュメントをマージします
        
        Args:
            documents: マージするドキュメントのリスト
            intent: マージの意図
            
        Returns:
            (マージされたドキュメント, サマリー情報)のタプル
        """
        # 新しいドキュメントIDを生成
        new_id = f"IdeaMark-{uuid.uuid4()}"
        source_ids = [doc.id for doc in documents]
        
        # マージ基本構造の作成
        merged_doc = IdeaMarkDocument(
            id=new_id,
            title=self._merge_title(documents),
            type=self._merge_type(documents),
            linked_documents=source_ids,
            created_at=datetime.now(),
            modified_at=datetime.now()
        )
        
        # 各セクションのマージ
        merged_doc.context = self._merge_context(documents, intent)
        merged_doc.problem = self._merge_problem(documents)
        merged_doc.solution = self._merge_solution(documents)
        merged_doc.metadata = self._merge_metadata(documents)
        
        # オプションフィールドのマージ（存在する場合のみ）
        optional_fields = ['author', 'children', 'relations', 'usage_scenarios']
        for field in optional_fields:
            merged_field = self._merge_optional_field(documents, field)
            if merged_field:
                setattr(merged_doc, field, merged_field)
        
        # サマリー情報を作成
        self.summary = {
            'sources': source_ids,
            'titles': {doc.id: doc.title for doc in documents},
            'intent': intent.value,
            'strategy': self.strategy.value,
            'conflicts': self.conflicts_detected,
            'timestamp': datetime.now().isoformat(),
            'total_documents_merged': len(documents)
        }
        
        return merged_doc, self.summary
    
    async def _merge_field(self, field_name: str, field_values: List[Dict[str, Any]], 
                         prompt_template: str = None) -> Any:
        """
        フィールドをマージします（競合がある場合は戦略に基づいて解決）
        
        Args:
            field_name: マージするフィールド名
            field_values: マージする値のリスト
            prompt_template: LLM用のプロンプトテンプレート（synthesis戦略の場合）
            
        Returns:
            マージされた値
        """
        if len(field_values) <= 1:
            return field_values[0]['value'] if field_values else None
        
        # 重複値を除去
        unique_values = []
        seen_values = set()
        
        for value_info in field_values:
            value_str = str(value_info['value']).strip()
            if value_str not in seen_values:
                unique_values.append(value_info)
                seen_values.add(value_str)
        
        if len(unique_values) <= 1:
            return unique_values[0]['value'] if unique_values else None
        
        # 競合検出
        self.conflicts_detected.append({
            'field': field_name,
            'values': unique_values,
            'strategy': self.strategy.value
        })
        
        # 戦略に基づいた解決
        if self.strategy == MergeStrategy.MANUAL:
            return await self.conflict_resolver.resolve_manual(
                field_name, unique_values, [v['source_id'] for v in unique_values])
        elif self.strategy == MergeStrategy.PREFER:
            return await self.conflict_resolver.resolve_prefer(
                field_name, unique_values, self.priority_order)
        elif self.strategy == MergeStrategy.ANNOTATE:
            return await self.conflict_resolver.resolve_annotate(
                field_name, unique_values, self.priority_order)
        elif self.strategy == MergeStrategy.SYNTHESIS:
            return await self.conflict_resolver.resolve_synthesis(
                field_name, unique_values, prompt_template or "")
        else:
            logger.warning(f"Unknown strategy {self.strategy}, falling back to manual")
            return await self.conflict_resolver.resolve_manual(
                field_name, unique_values, [v['source_id'] for v in unique_values])
    
    # 以下、具体的なフィールドごとのマージロジック
    async def _merge_title(self, documents: List[IdeaMarkDocument]) -> str:
        title_values = [{'value': doc.title, 'source_id': doc.id} for doc in documents]
        return await self._merge_field('title', title_values, 'merge_title')
    
    async def _merge_type(self, documents: List[IdeaMarkDocument]) -> str:
        type_values = [{'value': doc.type, 'source_id': doc.id} for doc in documents]
        return await self._merge_field('type', type_values)
    
    async def _merge_context(self, documents: List[IdeaMarkDocument], intent: MergeIntent) -> List[str]:
        all_contexts = []
        for doc in documents:
            if doc.context:
                all_contexts.extend(doc.context)
        
        # コンテキストは常にユニークな値をすべて集約
        unique_contexts = []
        seen = set()
        for context in all_contexts:
            context_str = str(context).strip()
            if context_str not in seen:
                unique_contexts.append(context)
                seen.add(context_str)
        
        return unique_contexts
    
    async def _merge_problem(self, documents: List[IdeaMarkDocument]) -> Dict[str, Any]:
        problem_summaries = [{'value': doc.problem.summary, 'source_id': doc.id} for doc in documents]
        merged_problem = {
            'summary': await self._merge_field('problem.summary', problem_summaries, 'merge_problem_summary')
        }
        
        # 要因（factors）の統合
        all_factors = []
        for doc in documents:
            if doc.problem.factors:
                all_factors.extend(doc.problem.factors)
        
        if all_factors:
            unique_factors = []
            seen = set()
            for factor in all_factors:
                factor_str = str(factor).strip()
                if factor_str not in seen:
                    unique_factors.append(factor)
                    seen.add(factor_str)
            merged_problem['factors'] = unique_factors
        
        return merged_problem
    
    async def _merge_solution(self, documents: List[IdeaMarkDocument]) -> Dict[str, Any]:
        # 同様のパターンで他のセクションもマージ
        # ...
        pass
    
    async def _merge_metadata(self, documents: List[IdeaMarkDocument]) -> Dict[str, Any]:
        # ...
        pass
    
    async def _merge_optional_field(self, documents: List[IdeaMarkDocument], field_name: str) -> Any:
        # ...
        pass
    
    async def _merge_list_field(self, field_values: List[List[Any]]) -> List[Any]:
        # リスト型フィールドのマージ
        # ...
        pass
    
    async def _merge_dict_field(self, field_name: str, field_values: List[Dict[str, Any]]) -> Dict[str, Any]:
        # 辞書型フィールドのマージ
        # ...
        pass
```

#### DocumentValidator 実装仕様

```python
class DocumentValidator:
    def __init__(self, schema_path: str):
        """
        Args:
            schema_path: JSONスキーマのパス
        """
        with open(schema_path, 'r') as f:
            self.schema = yaml.safe_load(f)
        
        self.validator = jsonschema.Draft202012Validator(self.schema)
    
    def validate_against_schema(self, doc: IdeaMarkDocument) -> List[str]:
        """
        ドキュメントをスキーマに対して検証します
        
        Args:
            doc: 検証するドキュメント
            
        Returns:
            エラーメッセージのリスト（空リストは検証成功を意味する）
        """
        errors = []
        doc_dict = doc.to_dict()
        
        for error in self.validator.iter_errors(doc_dict):
            error_path = '.'.join(str(p) for p in error.path) if error.path else 'root'
            errors.append(f"Validation error at {error_path}: {error.message}")
        
        return errors
    
    def check_content_consistency(self, doc: IdeaMarkDocument) -> Dict[str, List[str]]:
        """
        ドキュメントのコンテンツ整合性をチェックします
        
        Args:
            doc: 検証するドキュメント
            
        Returns:
            {'errors': [...], 'warnings': [...]} 形式の辞書
        """
        result = {
            'errors': [],
            'warnings': []
        }
        
        # タイトルのチェック
        if not doc.title or len(doc.title.strip()) < 3:
            result['errors'].append("Title is missing or too short")
        
        # コンテキストチェック
        if not doc.context or not isinstance(doc.context, list) or len(doc.context) == 0:
            result['warnings'].append("Context section is empty or invalid")
        
        # 問題と解決策のチェック
        if not doc.problem or not doc.problem.summary:
            result['errors'].append("Problem summary is required")
        
        if not doc.solution or not doc.solution.approach:
            result['errors'].append("Solution approach is required")
        
        # 相互参照の整合性チェック
        if hasattr(doc, 'linked_documents') and doc.linked_documents:
            # リンクの検証ロジック
            pass
        
        return result
```

### 2.5 Analytics Service 実装仕様

```python
class AnalyticsService:
    def __init__(self, storage: StorageInterface, search_service: SearchService):
        self.storage = storage
        self.search_service = search_service
    
    async def analyze_corpus(self, filters: Dict = None) -> Dict[str, Any]:
        # 文書群の統計分析
        pass
    
    async def find_gaps(self) -> List[str]:
        # 未処理領域、空欄フィールドの特定
        pass
    
    async def calculate_trends(self, time_range: str = None) -> Dict[str, Any]:
        # 傾向分析、頻出パターン抽出
        pass
    
    async def generate_dashboard_data(self) -> Dict[str, Any]:
        # MCP Server用ダッシュボードデータ生成
        pass
```

### 2.6 Link Management Service 実装仕様

```python
class LinkManagementService:
    def __init__(self, storage: StorageInterface):
        self.storage = storage
    
    async def attach_external_source(self, doc_id: str, link_type: str, url: str) -> bool:
        # 外部リソースの紐付け
        pass
    
    async def validate_links(self, doc_id: str) -> Dict[str, bool]:
        # リンクの有効性チェック
        pass
    
    async def get_linked_resources(self, doc_id: str) -> List[Dict]:
        # 紐付けられたリソース一覧取得
        pass
    
    async def sync_with_external_source(self, doc_id: str, link_type: str) -> bool:
        # 外部ソースとの同期（GitHub、データファイル等）
        pass
```

## 3. Application Layer 実装仕様例

### 3.1 CLI Application 実装仕様

```python
class IdeaMarkCLI:
    def __init__(self, config_path: str = None):
        self.config = load_config(config_path)
        self.llm_manager = LLMManager(config_path)
        self.storage = self._create_storage()
        self.discussion_service = DiscussionService(self.storage, self.llm_manager)
        self.versioning_service = VersioningService(self.storage)
        self.search_service = SearchService(self.storage)
    
    def _create_storage(self) -> StorageInterface:
        storage_config = self.config.get('ideamark', {}).get('storage', {})
        if storage_config.get('type') == 'database':
            return DatabaseStorage(storage_config.get('connection_string'))
        else:
            return FileStorage(storage_config.get('path', './ideamark_data'))
    
    async def search_command(self, query: str, **kwargs):
        return await self.search_service.search(query, kwargs)
    
    async def extend_command(self, doc_id: str, discussion_prompt: str):
        # 既存ドキュメントを拡張する議論を開始
        pass
    
    async def compare_command(self, doc_ids: List[str]):
        # 複数ドキュメントの構造比較
        pass
```

### 3.2 MCP Server 実装仕様

```python
class IdeaMarkMCPServer:
    def __init__(self, config_path: str = None):
        # CLI と同じコア機能を利用
        self.core = IdeaMarkCLI(config_path)
        self.session_manager = {}
    
    async def handle_multi_user_session(self, session_id: str, user_id: str, message: str):
        # マルチユーザーセッションの処理
        pass
    
    async def broadcast_update(self, session_id: str, update: Dict):
        # 参加者への更新通知
        pass
```

### 3.3 Agent Library 実装仕様

```python
class IdeaMarkAgent:
    def __init__(self, agent_config: Dict, llm_manager: LLMManager):
        self.config = agent_config
        self.llm_manager = llm_manager
        self.capabilities = self._load_capabilities()
    
    async def process_request(self, request: str) -> str:
        # リクエストを解析し、適切なサービスを呼び出し
        pass
    
    async def auto_suggest_improvements(self, doc_id: str) -> List[str]:
        # LLMを使ってドキュメント改善案を自動生成
        pass
    
    async def monitor_and_react(self, watch_patterns: List[str]):
        # ファイル変更を監視し、自動的に処理
        pass
```

## 4. 拡張性設計の実装仕様

### 4.1 プラグインシステム実装仕様

```python
class PluginManager:
    def __init__(self):
        self.plugins = {}
    
    def register_plugin(self, name: str, plugin_class):
        self.plugins[name] = plugin_class
    
    def load_plugins_from_config(self, config: Dict):
        # 設定ファイルからプラグインを動的ロード
        pass
```

### 4.2 イベント駆動アーキテクチャ実装仕様

```python
from enum import Enum
from typing import Callable, Any

class EventType(Enum):
    DOCUMENT_CREATED = "document_created"
    DOCUMENT_UPDATED = "document_updated"
    DISCUSSION_STARTED = "discussion_started"
    VERSION_CREATED = "version_created"

class EventBus:
    def __init__(self):
        self.listeners = {}
    
    def subscribe(self, event_type: EventType, callback: Callable):
        pass
    
    async def publish(self, event_type: EventType, data: Any):
        pass
```

### 4.3 API設計実装仕様

REST APIとしても公開可能な設計により、Web アプリケーションや他のシステムとの統合を容易にします。

```python
from fastapi import FastAPI
from ideamark.core import IdeaMarkCLI

app = FastAPI()
core = IdeaMarkCLI()

@app.post("/api/v1/documents")
async def create_document(document_data: Dict):
    return await core.create_document(document_data)

@app.get("/api/v1/search")
async def search_documents(q: str):
    return await core.search_command(q)
```

## 5. 実装優先度詳細

### Phase 1: Core Foundation

実装すべき具体的なコンポーネントと機能：

1. **基本的なLLM Interface実装**
   - OpenAIプロバイダー実装
   - 基本的なプロンプト管理
   - エラーハンドリング

2. **File Storage実装**
   - YAMLベースのファイル永続化
   - 基本的なCRUD操作
   - シンプルなリスト・フィルタ機能

3. **基本的なConfig Management**
   - 環境変数のサポート
   - ファイルベースの設定
   - デフォルト値の管理

4. **CLI基本コマンド実装**
   - search: 基本検索機能
   - build-index: シンプルなインデックス構築
   - build-vocab: 基本的な語彙辞書構築

### Phase 2: Core Services

1. **Versioning Service実装**
   - 基本的なバージョン管理
   - シンプルな差分計算
   - 履歴追跡機能

2. **Search Service拡張実装**
   - 類義語展開検索
   - タグベース検索
   - ファジー検索

3. **Document Processing Service実装**
   - 基本的な構造分解
   - スキーマ検証
   - シンプルなマージ機能

4. **Agent Library基礎実装**
   - 基本的なリクエスト処理
   - シンプルな自動化機能
   - 設定ベースの動作定義

### Phase 3: Advanced Features

1. **Discussion Service実装**
   - セッション管理
   - メッセージスレッド
   - AI支援提案

2. **Analytics Service実装**
   - 基本的な統計分析
   - シンプルな可視化データ生成
   - ギャップ検出

3. **Link Management Service実装**
   - 外部リソース紐付け
   - リンク検証
   - 基本的な同期機能

4. **MCP Server実装**
   - 基本的なMCPエンドポイント
   - 認証機能
   - チャットセッション管理

### Phase 4: Production Ready

1. **Database Storage実装**
   - SQLiteサポート
   - PostgreSQLサポート
   - マイグレーション機能

2. **イベント駆動機能・プラグインシステム**
   - イベントサブスクリプション
   - プラグイン検出・ロード
   - イベントバス実装

3. **監視・ログ機能**
   - 構造化ログ
   - パフォーマンス指標収集
   - アラート設定

4. **パフォーマンス最適化**
   - キャッシュ層実装
   - 遅延ロード
   - バッチ処理

## 6. 機能とアーキテクチャの対応関係詳細

### 6.1 Core Layer 対応機能の実装詳細

| 機能 | 対応コンポーネント | 実装内容 |
|------|------------------|----------|
| Storage | Storage Layer | IdeaMarkドキュメントの永続化・読み込み・一覧・削除 |
| Document Management | IdeaMark Core | ドキュメント操作、refs処理、基本CRUD |

### 6.2 Service Layer 対応機能の実装詳細

| 機能カテゴリ | 対応サービス | 実装内容 |
|-------------|-------------|----------|
| Search | Search Service | 全文検索、フィールド指定検索、類義語展開検索 |
| Index Build | Search Service | 逆引きインデックス構築、語句-ドキュメント双方向マッピング |
| Vocab Build | Search Service | 語彙辞書構築、類義語・語幹・関連語マッピング |
| Suggest | Search Service | 類義語・関連語提示、語彙候補表示 |
| Extend | Versioning Service + Discussion Service | ドキュメント拡張（追記/派生）、議論記録管理 |
| Compare | Versioning Service | 複数ドキュメント構造比較、差分計算 |
| Merge | Document Processing Service | パターンマージ、競合解決、統合戦略 |
| Breakdown | Document Processing Service | 抽象ドキュメントの具体化分解 |
| Analyze | Analytics Service | ローカル文書群の統計分析・傾向可視化 |
| Attach/Link | Link Management Service | 外部リソース紐付け管理 |

### 6.3 Application Layer 対応機能の実装詳細

| アプリケーション | 提供機能 |
|----------------|----------|
| CLI | 全機能のコマンドライン実装（search, extend, compare, breakdown, analyze, attach, build-index, build-vocab, suggest） |
| MCP Server | マルチユーザー向け機能（extend議論、リアルタイム検索、分析ダッシュボード） |
| Agent | 自動化機能（定期分析、自動提案、監視・反応） |
