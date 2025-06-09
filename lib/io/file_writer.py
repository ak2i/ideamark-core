import yaml
import json
from pathlib import Path
from typing import Dict, Any
from ..utils.logging import get_logger

logger = get_logger('file_writer')

class FileWriter:
    def __init__(self):
        pass
    
    def write_merged_output(self, merged_pattern: Dict[str, Any], summary_data: Dict[str, Any], 
                           output_path: str, create_summary: bool = True) -> Dict[str, str]:
        
        output_path = Path(output_path)
        written_files = {}
        
        if output_path.is_dir() or str(output_path).endswith('/'):
            written_files = self._write_to_directory(merged_pattern, summary_data, output_path, create_summary)
        else:
            written_files = self._write_to_file(merged_pattern, summary_data, output_path, create_summary)
        
        logger.info(f"Successfully wrote {len(written_files)} files")
        return written_files
    
    def _write_to_directory(self, merged_pattern: Dict[str, Any], summary_data: Dict[str, Any], 
                           output_dir: Path, create_summary: bool) -> Dict[str, str]:
        
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        pattern_id = merged_pattern['id']
        uuid_part = pattern_id.split('-', 1)[1]
        
        patterns_dir = output_dir / 'patterns'
        refs_dir = output_dir / 'refs'
        summary_dir = output_dir / 'summary'
        
        patterns_dir.mkdir(exist_ok=True)
        refs_dir.mkdir(exist_ok=True)
        if create_summary:
            summary_dir.mkdir(exist_ok=True)
        
        written_files = {}
        
        pattern_file = patterns_dir / f"merged-{uuid_part}.yaml"
        with open(pattern_file, 'w') as f:
            yaml.dump(merged_pattern, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        written_files['pattern'] = str(pattern_file)
        logger.debug(f"Wrote pattern file: {pattern_file}")
        
        ref_data = self._create_ref_from_pattern(merged_pattern)
        ref_file = refs_dir / f"merged-{uuid_part}.ref.yaml"
        with open(ref_file, 'w') as f:
            yaml.dump(ref_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        written_files['ref'] = str(ref_file)
        logger.debug(f"Wrote ref file: {ref_file}")
        
        if create_summary:
            summary_file = summary_dir / f"merged-{uuid_part}.md"
            summary_content = self._create_summary_markdown(merged_pattern, summary_data)
            with open(summary_file, 'w') as f:
                f.write(summary_content)
            written_files['summary'] = str(summary_file)
            logger.debug(f"Wrote summary file: {summary_file}")
        
        return written_files
    
    def _write_to_file(self, merged_pattern: Dict[str, Any], summary_data: Dict[str, Any], 
                      output_file: Path, create_summary: bool) -> Dict[str, str]:
        
        output_file = Path(output_file)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        written_files = {}
        
        with open(output_file, 'w') as f:
            yaml.dump(merged_pattern, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        written_files['pattern'] = str(output_file)
        logger.debug(f"Wrote pattern file: {output_file}")
        
        if create_summary:
            summary_file = output_file.with_suffix('.summary.md')
            summary_content = self._create_summary_markdown(merged_pattern, summary_data)
            with open(summary_file, 'w') as f:
                f.write(summary_content)
            written_files['summary'] = str(summary_file)
            logger.debug(f"Wrote summary file: {summary_file}")
        
        return written_files
    
    def _create_ref_from_pattern(self, pattern: Dict[str, Any]) -> Dict[str, Any]:
        ref_data = {
            'ref': {
                'id': pattern['id'],
                'title': pattern['title'],
                'access': pattern['access']
            }
        }
        
        if 'metadata' in pattern:
            ref_data['ref']['metadata'] = pattern['metadata']
        
        return ref_data
    
    def _create_summary_markdown(self, merged_pattern: Dict[str, Any], summary_data: Dict[str, Any]) -> str:
        lines = [
            f"# Merge Summary: {merged_pattern['title']}",
            "",
            f"**Pattern ID:** {merged_pattern['id']}",
            f"**Merge Strategy:** {summary_data['strategy']}",
            f"**Merge Intent:** {summary_data['intent']}",
            f"**Timestamp:** {summary_data['timestamp']}",
            "",
            "## Source Patterns",
            ""
        ]
        
        for source_id in summary_data['sources']:
            title = summary_data['titles'].get(source_id, 'Unknown')
            lines.append(f"- **{source_id}**: {title}")
        
        lines.extend(["", "## Conflicts Detected", ""])
        
        if summary_data['conflicts']:
            for conflict in summary_data['conflicts']:
                lines.append(f"### {conflict['field']}")
                lines.append(f"**Resolution Strategy:** {conflict['strategy']}")
                lines.append("**Conflicting Values:**")
                for value_info in conflict['values']:
                    lines.append(f"- {value_info['source_id']}: {value_info['value']}")
                lines.append("")
        else:
            lines.append("No conflicts detected during merge.")
        
        lines.extend([
            "",
            "## Linked Patterns",
            ""
        ])
        
        for linked_id in merged_pattern.get('linked_patterns', []):
            lines.append(f"- {linked_id}")
        
        return "\n".join(lines)
