import logging
import sys
from typing import Optional
from .config import Config

def setup_logging(config: Optional[Config] = None, level: Optional[str] = None) -> logging.Logger:
    if config is None:
        config = Config()
    
    log_config = config.get_logging_config()
    log_level = level or log_config.get('level', 'INFO')
    log_format = log_config.get('format', '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s')
    
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format=log_format,
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    
    logger = logging.getLogger('ideamark.merge_tool')
    return logger

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(f'ideamark.{name}')
