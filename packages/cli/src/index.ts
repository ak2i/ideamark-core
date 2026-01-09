import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { randomUUID } from 'node:crypto';
import { Command } from 'commander';
import { extractTemplateSlots, parse, validate } from '@ideamark/core';
import { parse as parseYaml, stringify as stringifyYaml } from 'yaml';

const program = new Command();

program.name('ideamark').description('IdeaMark CLI');

program
  .command('new')
  .argument('<filename>', 'Output filename (e.g. sample.ideamark.md)')
  .requiredOption('--template <path>', 'Template file path')
  .option('--out-dir <path>', 'Output directory (default: cwd)')
  .option('--created-by <value>', 'created_by value in frontmatter')
  .action((filename, options) => {
    const templatePath = options.template as string;
    let templateText: string;
    try {
      templateText = readFileSync(templatePath, 'utf8');
    } catch (error) {
      const result = {
        ok: false,
        errors: [
          {
            code: 'template_read_error',
            message: `failed to read template: ${templatePath}`,
          },
        ],
      };
      console.error(JSON.stringify(result, null, 2));
      process.exitCode = 1;
      return;
    }

    const parsedTemplate = parseFrontmatter(templateText);
    if ('errors' in parsedTemplate) {
      const result = { ok: false, errors: parsedTemplate.errors };
      console.error(JSON.stringify(result, null, 2));
      process.exitCode = 1;
      return;
    }

    const config = loadConfig();
    const outputDir =
      options.outDir ??
      process.env.IDEAMARK_OUTPUT_DIR ??
      config.output_dir ??
      process.cwd();
    const resolvedOutDir = resolve(outputDir);
    if (!existsSync(resolvedOutDir)) {
      mkdirSync(resolvedOutDir, { recursive: true });
    }

    const frontmatter = { ...parsedTemplate.frontmatter };
    const templateId =
      typeof frontmatter.template_id === 'string'
        ? frontmatter.template_id
        : 'template';
    const timestamp = new Date().toISOString();
    const compactTime = timestamp.replace(/[:.]/g, '').replace('Z', 'Z');
    const uuid = randomUUID();

    frontmatter.doc_id = `doc.${templateId}.${compactTime}.${uuid}`;
    frontmatter.created_at = timestamp;
    if (!frontmatter.ideamark_version) {
      frontmatter.ideamark_version = 1;
    }
    if (!frontmatter.lang) {
      frontmatter.lang = 'en';
    }
    if (options.createdBy) {
      frontmatter.created_by = options.createdBy;
    } else if (!frontmatter.created_by) {
      frontmatter.created_by = 'human';
    }

    const renderedFrontmatter = stringifyYaml(frontmatter).trimEnd();
    const outputText = `---\n${renderedFrontmatter}\n---\n${parsedTemplate.body}`;
    const outputPath = join(resolvedOutDir, filename);
    writeFileSync(outputPath, outputText, 'utf8');
    console.log(outputPath);
  });

program
  .command('validate')
  .argument('<file>', 'Markdown file to validate')
  .option('--json', 'output machine-readable result')
  .action((file, options) => {
    let input: string;
    try {
      input = readFileSync(file, 'utf8');
    } catch (error) {
      const result = {
        ok: false,
        errors: [
          {
            code: 'file_read_error',
            message: `failed to read file: ${file}`,
          },
        ],
      };
      console.error(JSON.stringify(result, null, 2));
      process.exitCode = 1;
      return;
    }

    const parsed = parse(input);
    if ('errors' in parsed) {
      const result = { ok: false, errors: parsed.errors };
      console.error(JSON.stringify(result, null, 2));
      process.exitCode = 1;
      return;
    }

    const validated = validate(parsed.document);
    if ('errors' in validated) {
      const result = { ok: false, errors: validated.errors };
      console.error(JSON.stringify(result, null, 2));
      process.exitCode = 1;
      return;
    }

    const warnings = [...parsed.warnings, ...validated.warnings];
    if (options.json) {
      console.log(JSON.stringify({ ok: true, warnings }, null, 2));
      return;
    }

    if (warnings.length > 0) {
      console.log('ok (with warnings)');
      return;
    }

    console.log('ok');
  });

type FrontmatterParseResult =
  | { ok: true; frontmatter: Record<string, unknown>; body: string }
  | { ok: false; errors: Array<{ code: string; message: string; line?: number }> };

function parseFrontmatter(markdown: string): FrontmatterParseResult {
  const lines = markdown.split(/\r?\n/);
  if (lines[0] !== '---') {
    return {
      ok: false,
      errors: [
        {
          code: 'frontmatter_missing',
          message: 'frontmatter must start with --- on the first line',
          line: 1,
        },
      ],
    };
  }

  let closingIndex = -1;
  for (let i = 1; i < lines.length; i += 1) {
    if (lines[i] === '---') {
      closingIndex = i;
      break;
    }
  }

  if (closingIndex === -1) {
    return {
      ok: false,
      errors: [
        {
          code: 'frontmatter_invalid_yaml',
          message: 'frontmatter closing delimiter not found',
          line: 1,
        },
      ],
    };
  }

  const frontmatterText = lines.slice(1, closingIndex).join('\n');
  let frontmatter: unknown;
  try {
    frontmatter = parseYaml(frontmatterText);
  } catch (error) {
    return {
      ok: false,
      errors: [
        {
          code: 'frontmatter_invalid_yaml',
          message: 'frontmatter is not valid YAML',
          line: 1,
        },
      ],
    };
  }

  if (
    !frontmatter ||
    typeof frontmatter !== 'object' ||
    Array.isArray(frontmatter)
  ) {
    return {
      ok: false,
      errors: [
        {
          code: 'frontmatter_not_object',
          message: 'frontmatter must be a YAML mapping object',
          line: 1,
        },
      ],
    };
  }

  const body = lines.slice(closingIndex + 1).join('\n');
  return { ok: true, frontmatter: frontmatter as Record<string, unknown>, body };
}

function loadConfig(): { output_dir?: string } {
  const configPath = resolve(process.cwd(), 'ideamark.config.json');
  if (!existsSync(configPath)) {
    return {};
  }

  try {
    const text = readFileSync(configPath, 'utf8');
    const data = JSON.parse(text);
    if (data && typeof data === 'object' && !Array.isArray(data)) {
      return { output_dir: (data as { output_dir?: string }).output_dir };
    }
  } catch (error) {
    return {};
  }

  return {};
}

const templateCommand = program.command('template').description('Template utilities');

templateCommand
  .command('slots')
  .argument('<file>', 'Template markdown file')
  .option('--json', 'output machine-readable result')
  .action((file, options) => {
    let input: string;
    try {
      input = readFileSync(file, 'utf8');
    } catch (error) {
      const result = {
        ok: false,
        errors: [
          {
            code: 'file_read_error',
            message: `failed to read file: ${file}`,
          },
        ],
      };
      console.error(JSON.stringify(result, null, 2));
      process.exitCode = 1;
      return;
    }

    const result = extractTemplateSlots(input);
    if (options.json) {
      console.log(JSON.stringify(result, null, 2));
      return;
    }

    if (result.slots.length === 0) {
      console.log('no slots found');
      return;
    }

    for (const slot of result.slots) {
      const lineInfo = slot.meta.blockStartLine
        ? `L${slot.meta.blockStartLine}`
        : `L${slot.meta.headingLine}`;
      console.log(`- ${slot.heading} (${lineInfo})`);
    }

    if (result.warnings.length > 0) {
      console.error(JSON.stringify({ warnings: result.warnings }, null, 2));
    }
  });

program.parse();
