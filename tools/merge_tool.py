#!/usr/bin/env python3

import click
import sys
from pathlib import Path
from typing import List

sys.path.insert(0, str(Path(__file__).parent))

from src.merge.core import PatternMerger
from src.io.file_writer import FileWriter
from src.utils.config import Config
from src.utils.logging import setup_logging, get_logger

@click.command()
@click.option('--refs', multiple=True, required=True, 
              help='Reference YAML files to merge (minimum 2 required)')
@click.option('--intent', default='union', 
              type=click.Choice(['intersection', 'union', 'hybrid', 'synthesis']),
              help='Merge intent strategy')
@click.option('--strategy', default='prefer',
              type=click.Choice(['manual', 'prefer', 'annotate', 'synthesis']),
              help='Conflict resolution strategy')
@click.option('--priority', help='Priority order for prefer strategy (space-separated pattern IDs)')
@click.option('--out', required=True, help='Output file or directory path')
@click.option('--config', help='Path to configuration file')
@click.option('--log-level', default='INFO',
              type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR']),
              help='Logging level')
@click.option('--no-summary', is_flag=True, help='Skip creating summary report')
def main(refs, intent, strategy, priority, out, config, log_level, no_summary):
    """
    IdeaMark Pattern Merge Tool
    
    Merges multiple IdeaMark patterns into a new synthesized pattern.
    
    Example usage:
    python merge_tool.py --refs pattern1.ref.yaml pattern2.ref.yaml --strategy prefer --out merged/
    """
    
    try:
        config_obj = Config(config) if config else Config()
        logger = setup_logging(config_obj, log_level)
        
        if len(refs) < 2:
            logger.error("At least 2 reference files are required for merging")
            sys.exit(1)
        
        priority_list = None
        if priority:
            priority_list = priority.split()
        
        logger.info(f"Starting merge of {len(refs)} patterns")
        logger.info(f"Intent: {intent}, Strategy: {strategy}")
        
        merger = PatternMerger(config_obj)
        merged_pattern, summary_data = merger.merge_patterns(
            list(refs), intent, strategy, priority_list
        )
        
        writer = FileWriter()
        written_files = writer.write_merged_output(
            merged_pattern, summary_data, out, not no_summary
        )
        
        logger.info("Merge completed successfully!")
        logger.info(f"Generated pattern ID: {merged_pattern['id']}")
        
        for file_type, file_path in written_files.items():
            logger.info(f"Written {file_type}: {file_path}")
        
        if summary_data['conflicts']:
            logger.warning(f"Detected {len(summary_data['conflicts'])} conflicts during merge")
            for conflict in summary_data['conflicts']:
                logger.warning(f"  - {conflict['field']}: resolved using {conflict['strategy']}")
        
    except Exception as e:
        logger = get_logger('main')
        logger.error(f"Merge failed: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
