import os
import yaml
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from utils.logging import get_logger

logger = get_logger('local_storage')

class LocalStorage:
    def __init__(self, work_dir: Optional[str] = None):
        self.work_dir = Path(work_dir or os.getenv("WORK_DIR", "/app/data"))
        self.patterns_dir = self.work_dir / "patterns"
        self.refs_dir = self.work_dir / "refs"
        
        self._ensure_directories()
    
    def _ensure_directories(self):
        self.work_dir.mkdir(parents=True, exist_ok=True)
        self.patterns_dir.mkdir(parents=True, exist_ok=True)
        self.refs_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Storage initialized at {self.work_dir}")
    
    def save_pattern(self, pattern_id: str, pattern_data: Dict[str, Any]) -> None:
        pattern_path = self.patterns_dir / f"{pattern_id}.yaml"
        
        try:
            with open(pattern_path, 'w') as f:
                yaml.safe_dump(pattern_data, f, default_flow_style=False, sort_keys=False)
            logger.info(f"Saved pattern {pattern_id} to {pattern_path}")
        except Exception as e:
            logger.error(f"Failed to save pattern {pattern_id}: {e}")
            raise
    
    def load_pattern(self, pattern_id: str) -> Optional[Dict[str, Any]]:
        pattern_path = self.patterns_dir / f"{pattern_id}.yaml"
        
        if not pattern_path.exists():
            logger.warning(f"Pattern file not found: {pattern_path}")
            return None
        
        try:
            with open(pattern_path, 'r') as f:
                pattern_data = yaml.safe_load(f)
            logger.debug(f"Loaded pattern {pattern_id} from {pattern_path}")
            return pattern_data
        except Exception as e:
            logger.error(f"Failed to load pattern {pattern_id}: {e}")
            raise
    
    def save_ref(self, ref_id: str, ref_data: Dict[str, Any]) -> None:
        ref_path = self.refs_dir / f"{ref_id}.ref.yaml"
        
        try:
            with open(ref_path, 'w') as f:
                yaml.safe_dump(ref_data, f, default_flow_style=False, sort_keys=False)
            logger.info(f"Saved ref {ref_id} to {ref_path}")
        except Exception as e:
            logger.error(f"Failed to save ref {ref_id}: {e}")
            raise
    
    def load_ref(self, ref_id: str) -> Optional[Dict[str, Any]]:
        ref_path = self.refs_dir / f"{ref_id}.ref.yaml"
        
        if not ref_path.exists():
            logger.warning(f"Ref file not found: {ref_path}")
            return None
        
        try:
            with open(ref_path, 'r') as f:
                ref_data = yaml.safe_load(f)
            logger.debug(f"Loaded ref {ref_id} from {ref_path}")
            return ref_data
        except Exception as e:
            logger.error(f"Failed to load ref {ref_id}: {e}")
            raise
    
    def get_ref_path(self, ref_id: str) -> str:
        return str(self.refs_dir / f"{ref_id}.ref.yaml")
    
    def list_all_refs(self) -> List[Dict[str, Any]]:
        refs = []
        
        try:
            for ref_file in self.refs_dir.glob("*.ref.yaml"):
                with open(ref_file, 'r') as f:
                    ref_data = yaml.safe_load(f)
                    refs.append(ref_data)
        except Exception as e:
            logger.error(f"Failed to list refs: {e}")
            raise
        
        return refs
    
    def pattern_exists(self, pattern_id: str) -> bool:
        pattern_path = self.patterns_dir / f"{pattern_id}.yaml"
        return pattern_path.exists()
    
    def ref_exists(self, ref_id: str) -> bool:
        ref_path = self.refs_dir / f"{ref_id}.ref.yaml"
        return ref_path.exists()
    
    def delete_pattern(self, pattern_id: str) -> bool:
        pattern_path = self.patterns_dir / f"{pattern_id}.yaml"
        
        if pattern_path.exists():
            try:
                pattern_path.unlink()
                logger.info(f"Deleted pattern {pattern_id}")
                return True
            except Exception as e:
                logger.error(f"Failed to delete pattern {pattern_id}: {e}")
                raise
        
        return False
    
    def delete_ref(self, ref_id: str) -> bool:
        ref_path = self.refs_dir / f"{ref_id}.ref.yaml"
        
        if ref_path.exists():
            try:
                ref_path.unlink()
                logger.info(f"Deleted ref {ref_id}")
                return True
            except Exception as e:
                logger.error(f"Failed to delete ref {ref_id}: {e}")
                raise
        
        return False
