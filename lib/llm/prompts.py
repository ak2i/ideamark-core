from typing import Dict, Any
from ..utils.config import load_prompts
from ..utils.logging import get_logger

logger = get_logger('prompts')

class PromptManager:
    def __init__(self, prompts_config: Dict[str, str] = None):
        self.prompts = prompts_config or load_prompts()
        logger.debug(f"Loaded {len(self.prompts)} prompt templates")
    
    def get_prompt(self, prompt_type: str, **kwargs) -> str:
        template = self.prompts.get(prompt_type)
        if not template:
            logger.warning(f"No prompt template found for type: {prompt_type}")
            return self._get_default_prompt(prompt_type, **kwargs)
        
        try:
            return template.format(**kwargs)
        except KeyError as e:
            logger.error(f"Missing required parameter for prompt {prompt_type}: {e}")
            return self._get_default_prompt(prompt_type, **kwargs)
    
    def _get_default_prompt(self, prompt_type: str, **kwargs) -> str:
        if prompt_type == 'problem_summary':
            return f"Combine the following problem summaries:\nA: {kwargs.get('text_a', '')}\nB: {kwargs.get('text_b', '')}"
        elif prompt_type == 'solution_approach':
            return f"Combine the following solution approaches:\nA: {kwargs.get('text_a', '')}\nB: {kwargs.get('text_b', '')}"
        elif prompt_type == 'metadata_field':
            return f"Combine the following {kwargs.get('field_name', 'values')}:\nA: {kwargs.get('text_a', '')}\nB: {kwargs.get('text_b', '')}"
        else:
            return f"Combine the following texts:\nA: {kwargs.get('text_a', '')}\nB: {kwargs.get('text_b', '')}"
