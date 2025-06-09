import yaml
import os
from pathlib import Path
from typing import Dict, Any


class Config:
    def __init__(self, config_path: str = None):
        if config_path is None:
            config_path = (
                Path(__file__).parent.parent.parent / "config" / "default.yaml"
            )

        with open(config_path, "r") as f:
            self._config = yaml.safe_load(f)

    def get(self, key: str, default: Any = None) -> Any:
        keys = key.split(".")
        value = self._config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

    def get_llm_config(self, provider: str) -> Dict[str, Any]:
        return self.get(f"llm.providers.{provider}", {})

    def get_network_config(self) -> Dict[str, Any]:
        return self.get("network", {})

    def get_logging_config(self) -> Dict[str, Any]:
        return self.get("logging", {})

    def get_oauth_config(self) -> Dict[str, Any]:
        oauth_config = self.get("oauth", {})
        expanded = {}
        for key, value in oauth_config.items():
            if (
                isinstance(value, str)
                and value.startswith("${")
                and value.endswith("}")
            ):
                env_var = value[2:-1]
                expanded[key] = os.getenv(env_var, "")
            else:
                expanded[key] = value
        return expanded


def load_prompts(prompts_path: str = None) -> Dict[str, str]:
    if prompts_path is None:
        prompts_path = (
            Path(__file__).parent.parent.parent
            / "config"
            / "prompts"
            / "synthesis.yaml"
        )

    with open(prompts_path, "r") as f:
        prompts = yaml.safe_load(f)

    return prompts.get("synthesis", {})
