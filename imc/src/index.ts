#!/usr/bin/env node
import { Command } from 'commander';
import { cmdInit } from './commands/init.js';
import { cmdOutline } from './commands/outline.js';
import { cmdSynth } from './commands/synth.js';
import { cmdValidate } from './commands/validate.js';
import { cmdGenerate } from './commands/generate.js';
import { cmdCheck } from './commands/check.js';

const program = new Command();
program.name('imc').description('IdeaMark Compiler').version('0.1.0');

program
  .command('init')
  .description('Initialize repository structure and seed files')
  .requiredOption('--root <path>', 'root directory to place project structure')
  .requiredOption('--project <name>', 'project name (used for file names and folders)')
  .action(cmdInit);

program
  .command('outline')
  .description('Create an outline JSON from a brief using LLM (optional stage)')
  .requiredOption('--root <path>', 'repo root')
  .requiredOption('--project <name>', 'project name')
  .requiredOption('--brief <path>', 'path to brief markdown/text')
  .option('--about <path>', 'path to AboutSchema.md (default: root/schema or root/docs)')
  .action(cmdOutline);

program
  .command('synth')
  .description('Synthesize <project>.designdoc.yaml from brief (LLM). YAML-only, must validate.')
  .requiredOption('--root <path>', 'repo root')
  .requiredOption('--project <name>', 'project name')
  .requiredOption('--brief <path>', 'path to brief markdown/text')
  .option('--schema <path>', 'path to ideamark.schema.yaml (default: root/schema/ideamark.schema.yaml)')
  .option('--about <path>',  'path to AboutSchema.md (default: root/schema or root/docs)')
  .option('--fix', 'attempt auto-fix on validation error', true)
  .action(cmdSynth);

program
  .command('validate')
  .description('Validate <project>.designdoc.yaml against ideamark schema')
  .requiredOption('--root <path>', 'repo root')
  .requiredOption('--project <name>', 'project name')
  .option('--schema <path>', 'path to ideamark.schema.yaml (default: root/schema/ideamark.schema.yaml)')
  .action(cmdValidate);

program
  .command('generate')
  .description('Generate <project>.types.ts / <project>.schema.json / <project>.ADR-XXXX.md')
  .requiredOption('--root <path>', 'repo root')
  .requiredOption('--project <name>', 'project name')
  .action(cmdGenerate);

program
  .command('check')
  .description('Run checks: ADR index, naming, formatting')
  .requiredOption('--root <path>', 'repo root')
  .requiredOption('--project <name>', 'project name')
  .action(cmdCheck);

program.parseAsync(process.argv);
