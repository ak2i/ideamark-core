import uuid
from typing import Dict, Any, List, Optional
from ..utils.logging import get_logger
from ..llm.providers import LLMProvider

logger = get_logger('strategies')

class ConflictResolver:
    def __init__(self, llm_provider: Optional[LLMProvider] = None):
        self.llm_provider = llm_provider
    
    def resolve_manual(self, field_name: str, values: List[Dict[str, Any]], source_ids: List[str]) -> Any:
        source_list = ", ".join(source_ids)
        
        if field_name == "metadata.scalefactor" and values and isinstance(values[0]['value'], dict):
            return {
                "TODO": f"resolve conflict between {source_list} for {field_name}",
                "options": {f"option_{i}": val['value'] for i, val in enumerate(values)}
            }
        
        placeholder = f"TODO: resolve conflict between {source_list} for {field_name}"
        logger.debug(f"Created manual placeholder for {field_name}")
        return placeholder
    
    def resolve_prefer(self, field_name: str, values: List[Dict[str, Any]], priority_order: List[str]) -> Any:
        for source_id in priority_order:
            for value_info in values:
                if value_info['source_id'] == source_id:
                    logger.debug(f"Resolved {field_name} using prefer strategy: chose {source_id}")
                    return value_info['value']
        
        logger.warning(f"No value found in priority order for {field_name}, using first available")
        return values[0]['value'] if values else None
    
    def resolve_annotate(self, field_name: str, values: List[Dict[str, Any]], priority_order: List[str]) -> Any:
        if field_name == "metadata.scalefactor" and values and isinstance(values[0]['value'], dict):
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
        
        annotated_parts = []
        
        for source_id in priority_order:
            for value_info in values:
                if value_info['source_id'] == source_id:
                    annotated_parts.append(f"[From {source_id}] {value_info['value']}")
                    break
        
        result = "\n".join(annotated_parts)
        logger.debug(f"Created annotated resolution for {field_name}")
        return result
    
    def resolve_synthesis(self, field_name: str, values: List[Dict[str, Any]], prompt_template: str) -> str:
        if not self.llm_provider:
            logger.warning(f"No LLM provider available for synthesis, falling back to manual for {field_name}")
            return self.resolve_manual(field_name, values, [v['source_id'] for v in values])
        
        if len(values) < 2:
            return values[0]['value'] if values else ""
        
        try:
            text_a = values[0]['value']
            text_b = values[1]['value']
            
            prompt = prompt_template.format(
                field_name=field_name,
                text_a=text_a,
                text_b=text_b
            )
            
            result = self.llm_provider.generate(prompt)
            logger.debug(f"Successfully synthesized {field_name} using LLM")
            return result
            
        except Exception as e:
            logger.error(f"LLM synthesis failed for {field_name}: {e}")
            return self.resolve_manual(field_name, values, [v['source_id'] for v in values])

class MergeStrategy:
    def __init__(self, strategy_name: str, conflict_resolver: ConflictResolver, priority_order: List[str] = None):
        self.strategy_name = strategy_name
        self.conflict_resolver = conflict_resolver
        self.priority_order = priority_order or []
        self.conflicts_detected = []
    
    def merge_field(self, field_name: str, field_values: List[Dict[str, Any]], prompt_template: str = None) -> Any:
        if len(field_values) <= 1:
            return field_values[0]['value'] if field_values else None
        
        unique_values = []
        seen_values = set()
        
        for value_info in field_values:
            value_str = str(value_info['value']).strip()
            if value_str not in seen_values:
                unique_values.append(value_info)
                seen_values.add(value_str)
        
        if len(unique_values) <= 1:
            return unique_values[0]['value'] if unique_values else None
        
        self.conflicts_detected.append({
            'field': field_name,
            'values': unique_values,
            'strategy': self.strategy_name
        })
        
        if self.strategy_name == 'manual':
            return self.conflict_resolver.resolve_manual(field_name, unique_values, [v['source_id'] for v in unique_values])
        elif self.strategy_name == 'prefer':
            return self.conflict_resolver.resolve_prefer(field_name, unique_values, self.priority_order)
        elif self.strategy_name == 'annotate':
            return self.conflict_resolver.resolve_annotate(field_name, unique_values, self.priority_order)
        elif self.strategy_name == 'synthesis':
            return self.conflict_resolver.resolve_synthesis(field_name, unique_values, prompt_template or "")
        else:
            logger.warning(f"Unknown strategy {self.strategy_name}, falling back to manual")
            return self.conflict_resolver.resolve_manual(field_name, unique_values, [v['source_id'] for v in unique_values])
    
    def merge_list_field(self, field_values: List[List[Any]]) -> List[Any]:
        merged = []
        seen = set()
        
        for value_list in field_values:
            if value_list:
                for item in value_list:
                    item_str = str(item).strip()
                    if item_str not in seen:
                        merged.append(item)
                        seen.add(item_str)
        
        return merged
    
    def merge_dict_field(self, field_name: str, field_values: List[Dict[str, Any]], prompt_template: str = None) -> Dict[str, Any]:
        merged = {}
        
        all_keys = set()
        for value_dict in field_values:
            if value_dict:
                all_keys.update(value_dict.keys())
        
        for key in all_keys:
            key_values = []
            for i, value_dict in enumerate(field_values):
                if value_dict and key in value_dict:
                    key_values.append({
                        'value': value_dict[key],
                        'source_id': f"pattern_{i}"
                    })
            
            if isinstance(key_values[0]['value'], list) if key_values else False:
                merged[key] = self.merge_list_field([v['value'] for v in key_values])
            else:
                merged[key] = self.merge_field(f"{field_name}.{key}", key_values, prompt_template)
        
        return merged
