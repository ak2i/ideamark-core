import uuid
from typing import Dict, Any, List, Tuple, Optional
from datetime import datetime
from ..utils.logging import get_logger
from ..utils.config import Config
from ..io.pattern_loader import PatternLoader
from ..merge.validators import PatternValidator
from ..merge.strategies import MergeStrategy, ConflictResolver
from ..llm.providers import create_llm_provider
from ..llm.prompts import PromptManager

logger = get_logger('merge_core')

class PatternMerger:
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.loader = PatternLoader(self.config)
        self.validator = PatternValidator()
        self.prompt_manager = PromptManager()
        
        self.llm_provider = None
        self._initialize_llm()
    
    def _initialize_llm(self):
        llm_providers = ['openai', 'anthropic', 'local']
        
        for provider_name in llm_providers:
            try:
                self.llm_provider = create_llm_provider(provider_name, self.config)
                if self.llm_provider:
                    logger.info(f"Successfully initialized LLM provider: {provider_name}")
                    break
            except Exception as e:
                logger.debug(f"Failed to initialize {provider_name}: {e}")
                continue
        
        if not self.llm_provider:
            logger.warning("No LLM provider available, synthesis strategy will fall back to manual")
    
    def merge_patterns(self, ref_paths: List[str], intent: str = 'union', 
                      strategy: str = 'prefer', priority: List[str] = None) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        
        logger.info(f"Starting merge of {len(ref_paths)} patterns with intent={intent}, strategy={strategy}")
        
        patterns_data = []
        refs_data = []
        
        for ref_path in ref_paths:
            pattern, ref = self.loader.load_pattern_from_ref(ref_path)
            
            self.validator.validate_and_raise(pattern)
            
            patterns_data.append(pattern)
            refs_data.append(ref)
        
        if priority is None:
            priority = [ref['ref']['id'] for ref in refs_data]
        
        conflict_resolver = ConflictResolver(self.llm_provider)
        merge_strategy = MergeStrategy(strategy, conflict_resolver, priority)
        
        merged_pattern = self._merge_pattern_data(patterns_data, refs_data, merge_strategy, intent)
        
        self.validator.validate_and_raise(merged_pattern)
        
        summary_data = self._create_summary_data(patterns_data, refs_data, merge_strategy, intent, strategy)
        
        logger.info(f"Successfully merged {len(ref_paths)} patterns into new pattern {merged_pattern['id']}")
        
        return merged_pattern, summary_data
    
    def _merge_pattern_data(self, patterns: List[Dict[str, Any]], refs: List[Dict[str, Any]], 
                           merge_strategy: MergeStrategy, intent: str) -> Dict[str, Any]:
        
        new_id = f"IdeaMark-{uuid.uuid4()}"
        source_ids = [pattern['id'] for pattern in patterns]
        
        merged = {
            'id': new_id,
            'title': self._merge_titles(patterns, merge_strategy),
            'type': self._merge_types(patterns, merge_strategy),
            'context': self._merge_context(patterns, intent),
            'problem': self._merge_problem(patterns, merge_strategy),
            'solution': self._merge_solution(patterns, merge_strategy),
            'metadata': self._merge_metadata(patterns, merge_strategy),
            'access': {
                'uri': f"https://github.com/ak2i/ideamark-core/blob/main/patterns/merged-{new_id.split('-', 1)[1]}.yaml",
                'visibility': 'public'
            },
            'linked_patterns': source_ids
        }
        
        optional_fields = ['author', 'children', 'relations', 'usage_scenarios']
        for field in optional_fields:
            merged_field = self._merge_optional_field(patterns, field, merge_strategy)
            if merged_field:
                merged[field] = merged_field
        
        return merged
    
    def _merge_titles(self, patterns: List[Dict[str, Any]], merge_strategy: MergeStrategy) -> str:
        title_values = [{'value': p['title'], 'source_id': p['id']} for p in patterns]
        prompt = self.prompt_manager.get_prompt('metadata_field', field_name='title', 
                                               text_a=title_values[0]['value'] if len(title_values) > 0 else '',
                                               text_b=title_values[1]['value'] if len(title_values) > 1 else '')
        return merge_strategy.merge_field('title', title_values, prompt)
    
    def _merge_types(self, patterns: List[Dict[str, Any]], merge_strategy: MergeStrategy) -> str:
        type_values = [{'value': p['type'], 'source_id': p['id']} for p in patterns]
        prompt = self.prompt_manager.get_prompt('metadata_field', field_name='type',
                                               text_a=type_values[0]['value'] if len(type_values) > 0 else '',
                                               text_b=type_values[1]['value'] if len(type_values) > 1 else '')
        return merge_strategy.merge_field('type', type_values, prompt)
    
    def _merge_context(self, patterns: List[Dict[str, Any]], intent: str) -> List[str]:
        all_contexts = []
        for pattern in patterns:
            if 'context' in pattern and pattern['context']:
                all_contexts.extend(pattern['context'])
        
        unique_contexts = []
        seen = set()
        for context in all_contexts:
            context_str = str(context).strip()
            if context_str not in seen:
                unique_contexts.append(context)
                seen.add(context_str)
        
        return unique_contexts
    
    def _merge_problem(self, patterns: List[Dict[str, Any]], merge_strategy: MergeStrategy) -> Dict[str, Any]:
        problem_summaries = [{'value': p['problem']['summary'], 'source_id': p['id']} for p in patterns]
        prompt = self.prompt_manager.get_prompt('problem_summary',
                                               text_a=problem_summaries[0]['value'] if len(problem_summaries) > 0 else '',
                                               text_b=problem_summaries[1]['value'] if len(problem_summaries) > 1 else '')
        
        merged_problem = {
            'summary': merge_strategy.merge_field('problem.summary', problem_summaries, prompt)
        }
        
        all_factors = []
        for pattern in patterns:
            if 'factors' in pattern['problem'] and pattern['problem']['factors']:
                all_factors.extend(pattern['problem']['factors'])
        
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
    
    def _merge_solution(self, patterns: List[Dict[str, Any]], merge_strategy: MergeStrategy) -> Dict[str, Any]:
        solution_approaches = [{'value': p['solution']['approach'], 'source_id': p['id']} for p in patterns]
        prompt = self.prompt_manager.get_prompt('solution_approach',
                                               text_a=solution_approaches[0]['value'] if len(solution_approaches) > 0 else '',
                                               text_b=solution_approaches[1]['value'] if len(solution_approaches) > 1 else '')
        
        merged_solution = {
            'approach': merge_strategy.merge_field('solution.approach', solution_approaches, prompt)
        }
        
        all_components = []
        for pattern in patterns:
            if 'components' in pattern['solution'] and pattern['solution']['components']:
                all_components.extend(pattern['solution']['components'])
        
        if all_components:
            unique_components = []
            seen = set()
            for component in all_components:
                component_str = str(component).strip()
                if component_str not in seen:
                    unique_components.append(component)
                    seen.add(component_str)
            merged_solution['components'] = unique_components
        
        all_examples = []
        for pattern in patterns:
            if 'examples' in pattern['solution'] and pattern['solution']['examples']:
                all_examples.extend(pattern['solution']['examples'])
        
        if all_examples:
            unique_examples = []
            seen = set()
            for example in all_examples:
                example_str = str(example).strip()
                if example_str not in seen:
                    unique_examples.append(example)
                    seen.add(example_str)
            merged_solution['examples'] = unique_examples
        
        return merged_solution
    
    def _merge_metadata(self, patterns: List[Dict[str, Any]], merge_strategy: MergeStrategy) -> Dict[str, Any]:
        metadata_dicts = [p.get('metadata', {}) for p in patterns]
        return merge_strategy.merge_dict_field('metadata', metadata_dicts)
    
    def _merge_optional_field(self, patterns: List[Dict[str, Any]], field_name: str, merge_strategy: MergeStrategy) -> Any:
        field_values = []
        for pattern in patterns:
            if field_name in pattern and pattern[field_name]:
                field_values.append(pattern[field_name])
        
        if not field_values:
            return None
        
        if isinstance(field_values[0], list):
            return merge_strategy.merge_list_field(field_values)
        elif isinstance(field_values[0], dict):
            return merge_strategy.merge_dict_field(field_name, field_values)
        else:
            value_dicts = [{'value': v, 'source_id': f'pattern_{i}'} for i, v in enumerate(field_values)]
            return merge_strategy.merge_field(field_name, value_dicts)
    
    def _create_summary_data(self, patterns: List[Dict[str, Any]], refs: List[Dict[str, Any]], 
                           merge_strategy: MergeStrategy, intent: str, strategy: str) -> Dict[str, Any]:
        
        return {
            'sources': [p['id'] for p in patterns],
            'titles': {p['id']: p['title'] for p in patterns},
            'intent': intent,
            'strategy': strategy,
            'conflicts': merge_strategy.conflicts_detected,
            'timestamp': datetime.now().isoformat(),
            'total_patterns_merged': len(patterns)
        }
