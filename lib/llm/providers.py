"""LLM provider interfaces and implementations.

This module defines lightweight wrappers around various language model services.
The providers use environment variables for authentication:

```
OPENAI_API_KEY      API key for OpenAI models
ANTHROPIC_API_KEY   API key for Anthropic models
MISTRAL_API_KEY     API key for Mistral AI models
GOOGLE_API_KEY      API key for Google Gemini / Vertex AI models
```

Each provider reads these variables during initialization. Missing keys will
result in runtime errors when trying to generate completions.
"""

import os
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any
from ..utils.config import Config
from ..utils.logging import get_logger

logger = get_logger('llm_providers')

class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

class OpenAIProvider(LLMProvider):
    def __init__(self, config: Dict[str, Any]):
        try:
            import openai
            self.client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
            self.model = config.get('model', 'gpt-4')
            self.max_tokens = config.get('max_tokens', 2000)
            self.temperature = config.get('temperature', 0.3)
            logger.info(f"Initialized OpenAI provider with model {self.model}")
        except ImportError:
            raise ImportError("OpenAI library not available. Install with: pip install openai")
        except Exception as e:
            raise Exception(f"Failed to initialize OpenAI provider: {e}")
    
    def generate(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"OpenAI generation failed: {e}")
            raise

class AnthropicProvider(LLMProvider):
    def __init__(self, config: Dict[str, Any]):
        try:
            import anthropic
            self.client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
            self.model = config.get('model', 'claude-3-sonnet-20240229')
            self.max_tokens = config.get('max_tokens', 2000)
            self.temperature = config.get('temperature', 0.3)
            logger.info(f"Initialized Anthropic provider with model {self.model}")
        except ImportError:
            raise ImportError("Anthropic library not available. Install with: pip install anthropic")
        except Exception as e:
            raise Exception(f"Failed to initialize Anthropic provider: {e}")
    
    def generate(self, prompt: str) -> str:
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text.strip()
        except Exception as e:
            logger.error(f"Anthropic generation failed: {e}")
            raise

class LocalLLMProvider(LLMProvider):
    def __init__(self, config: Dict[str, Any]):
        self.endpoint = config.get('endpoint', 'http://localhost:8000/generate')
        self.model = config.get('model', 'local')
        logger.info(f"Initialized local LLM provider with endpoint {self.endpoint}")
    
    def generate(self, prompt: str) -> str:
        try:
            import requests
            response = requests.post(
                self.endpoint,
                json={'prompt': prompt, 'model': self.model},
                timeout=60
            )
            response.raise_for_status()
            return response.json().get('text', '').strip()
        except Exception as e:
            logger.error(f"Local LLM generation failed: {e}")
            raise

class MistralProvider(LLMProvider):
    def __init__(self, config: Dict[str, Any]):
        self.endpoint = "https://api.mistral.ai/v1/chat/completions"
        self.api_key = os.getenv("MISTRAL_API_KEY")
        self.model = config.get("model", "mistral-small")
        self.max_tokens = config.get("max_tokens", 2000)
        self.temperature = config.get("temperature", 0.3)
        logger.info(f"Initialized Mistral provider with model {self.model}")

    def generate(self, prompt: str) -> str:
        try:
            import requests
            headers = {"Authorization": f"Bearer {self.api_key}"}
            data = {
                "model": self.model,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": self.max_tokens,
                "temperature": self.temperature,
            }
            response = requests.post(
                self.endpoint, json=data, timeout=60, headers=headers
            )
            response.raise_for_status()
            return (
                response.json()["choices"][0]["message"]["content"].strip()
            )
        except Exception as e:
            logger.error(f"Mistral generation failed: {e}")
            raise


class GoogleProvider(LLMProvider):
    def __init__(self, config: Dict[str, Any]):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.model = config.get("model", "gemini-pro")
        self.max_tokens = config.get("max_tokens", 2000)
        self.temperature = config.get("temperature", 0.3)
        self.endpoint = (
            f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent"
        )
        logger.info(f"Initialized Google provider with model {self.model}")

    def generate(self, prompt: str) -> str:
        try:
            import requests
            params = {"key": self.api_key}
            data = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "maxOutputTokens": self.max_tokens,
                    "temperature": self.temperature,
                },
            }
            response = requests.post(
                self.endpoint, params=params, json=data, timeout=60
            )
            response.raise_for_status()
            return (
                response.json()["candidates"][0]["content"]["parts"][0]["text"].strip()
            )
        except Exception as e:
            logger.error(f"Google generation failed: {e}")
            raise

def create_llm_provider(provider_name: str, config: Config) -> Optional[LLMProvider]:
    provider_config = config.get_llm_config(provider_name)
    
    if not provider_config:
        logger.warning(f"No configuration found for LLM provider: {provider_name}")
        return None
    
    try:
        if provider_name == 'openai':
            return OpenAIProvider(provider_config)
        elif provider_name == 'anthropic':
            return AnthropicProvider(provider_config)
        elif provider_name == 'mistral':
            return MistralProvider(provider_config)
        elif provider_name == 'google':
            return GoogleProvider(provider_config)
        elif provider_name == 'local':
            return LocalLLMProvider(provider_config)
        else:
            logger.error(f"Unknown LLM provider: {provider_name}")
            return None
    except Exception as e:
        logger.error(f"Failed to create LLM provider {provider_name}: {e}")
        return None
