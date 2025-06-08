import yaml
import requests
import time
from pathlib import Path
from typing import Dict, Any, Tuple
from urllib.parse import urlparse
from ..utils.config import Config
from ..utils.logging import get_logger
from ..merge.validators import validate_ref_structure

logger = get_logger('pattern_loader')

class PatternLoader:
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.network_config = self.config.get_network_config()
        self.retries = self.network_config.get('retries', 3)
        self.backoff_factor = self.network_config.get('backoff_factor', 2)
        self.timeout = self.network_config.get('timeout', 30)
    
    def load_ref_file(self, ref_path: str) -> Dict[str, Any]:
        logger.info(f"Loading reference file: {ref_path}")
        
        try:
            with open(ref_path, 'r') as f:
                ref_data = yaml.safe_load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Reference file not found: {ref_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in reference file {ref_path}: {e}")
        
        errors = validate_ref_structure(ref_data)
        if errors:
            error_msg = f"Invalid reference file structure in {ref_path}:\n" + "\n".join(f"  - {error}" for error in errors)
            raise ValueError(error_msg)
        
        logger.debug(f"Successfully loaded reference file: {ref_path}")
        return ref_data
    
    def load_pattern_from_uri(self, uri: str) -> Dict[str, Any]:
        logger.info(f"Loading pattern from URI: {uri}")
        
        parsed_uri = urlparse(uri)
        
        if parsed_uri.scheme in ('http', 'https'):
            return self._load_pattern_from_url(uri)
        elif parsed_uri.scheme == 'file' or not parsed_uri.scheme:
            file_path = parsed_uri.path if parsed_uri.scheme == 'file' else uri
            return self._load_pattern_from_file(file_path)
        else:
            raise ValueError(f"Unsupported URI scheme: {parsed_uri.scheme}")
    
    def _load_pattern_from_url(self, url: str) -> Dict[str, Any]:
        raw_url = self._convert_to_raw_url(url)
        last_exception = None
        
        for attempt in range(self.retries + 1):
            try:
                logger.debug(f"Attempting to fetch URL (attempt {attempt + 1}): {raw_url}")
                response = requests.get(raw_url, timeout=self.timeout)
                response.raise_for_status()
                
                pattern_data = yaml.safe_load(response.text)
                logger.debug(f"Successfully loaded pattern from URL: {raw_url}")
                return pattern_data
                
            except (requests.RequestException, yaml.YAMLError) as e:
                last_exception = e
                if attempt < self.retries:
                    wait_time = self.backoff_factor ** attempt
                    logger.warning(f"Failed to load pattern from {raw_url} (attempt {attempt + 1}), retrying in {wait_time}s: {e}")
                    time.sleep(wait_time)
                else:
                    logger.error(f"Failed to load pattern from {raw_url} after {self.retries + 1} attempts: {e}")
        
        raise Exception(f"Failed to load pattern from {raw_url} after {self.retries + 1} attempts. Last error: {last_exception}")
    
    def _convert_to_raw_url(self, url: str) -> str:
        """Convert GitHub blob URLs to raw content URLs."""
        if 'github.com' in url and '/blob/' in url:
            return url.replace('github.com', 'raw.githubusercontent.com').replace('/blob/', '/')
        return url
    
    def _load_pattern_from_file(self, file_path: str) -> Dict[str, Any]:
        try:
            with open(file_path, 'r') as f:
                pattern_data = yaml.safe_load(f)
            
            logger.debug(f"Successfully loaded pattern from file: {file_path}")
            return pattern_data
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Pattern file not found: {file_path}")
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in pattern file {file_path}: {e}")
    
    def load_pattern_from_ref(self, ref_path: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        ref_data = self.load_ref_file(ref_path)
        ref = ref_data['ref']
        
        pattern_uri = ref['access']['uri']
        pattern_data = self.load_pattern_from_uri(pattern_uri)
        
        if pattern_data.get('id') != ref.get('id'):
            logger.warning(f"Pattern ID mismatch: ref has {ref.get('id')}, pattern has {pattern_data.get('id')}")
        
        return pattern_data, ref_data
