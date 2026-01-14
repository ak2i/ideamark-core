import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { join, resolve } from 'node:path';
import { randomUUID } from 'node:crypto';
import { Command } from 'commander';
import { extractTemplateSlots, parse, validate } from '@ideamark/core';
import { parse as parseYaml, stringify as stringifyYaml } from 'yaml';
import { fetch } from 'undici';

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

const assistCommand = program.command('assist').description('AI-assisted helpers');

assistCommand
  .command('fill')
  .argument('<file>', 'IdeaMark document to fill')
  .option('--source <path_or_url...>', 'Source files or URLs (repeatable)')
  .option('--block <name>', 'Only fill the specified Slot')
  .option('--model <name>', 'Model identifier (OpenAI-compatible)')
  .option('--base-url <url>', 'OpenAI-compatible base URL')
  .option('--api-key <key>', 'API key')
  .option('--chunk-size <number>', 'Max characters per source chunk', '3000')
  .option('--max-chunks <number>', 'Max chunks per slot', '4')
  .option('--dry-run', 'Do not write changes')
  .option('--json', 'Output machine-readable result')
  .action(async (file, options) => {
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

    const slotResult = extractTemplateSlots(input);
    if (slotResult.slots.length === 0) {
      console.error(
        JSON.stringify(
          { ok: false, errors: [{ code: 'no_slots', message: 'no slots found' }] },
          null,
          2,
        ),
      );
      process.exitCode = 1;
      return;
    }

    const selectedSlots = options.block
      ? slotResult.slots.filter((slot) => slot.name === options.block)
      : slotResult.slots;
    if (selectedSlots.length === 0) {
      console.error(
        JSON.stringify(
          {
            ok: false,
            errors: [
              {
                code: 'slot_not_found',
                message: `slot not found: ${options.block}`,
              },
            ],
          },
          null,
          2,
        ),
      );
      process.exitCode = 1;
      return;
    }

    let updated: AssistResult;
    try {
      const sources = await collectSources(options.source ?? []);
      updated = await fillSlotsWithAi({
        markdown: input,
        slots: selectedSlots,
        sources,
        model: options.model,
        baseUrl: options.baseUrl,
        apiKey: options.apiKey,
        chunkSize: Number(options.chunkSize),
        maxChunks: Number(options.maxChunks),
      });
    } catch (error) {
      const message = error instanceof Error ? error.message : 'unknown error';
      console.error(
        JSON.stringify(
          { ok: false, errors: [{ code: 'assist_failed', message }] },
          null,
          2,
        ),
      );
      process.exitCode = 1;
      return;
    }

    if (!updated.ok) {
      console.error(JSON.stringify(updated, null, 2));
      process.exitCode = 1;
      return;
    }

    if (options.json) {
      console.log(JSON.stringify(updated, null, 2));
      return;
    }

    if (options.dryRun) {
      console.log(updated.markdown);
      return;
    }

    writeFileSync(file, updated.markdown, 'utf8');
    console.log(file);
  });

type AssistResult =
  | {
      ok: true;
      markdown: string;
      warnings: Array<{ code: string; message: string }>;
      report: Array<{
        slot: string;
        chunks: Array<{ id: string; index: number }>;
      }>;
    }
  | { ok: false; errors: Array<{ code: string; message: string }> };

async function collectSources(
  inputs: string[],
): Promise<Array<{ id: string; content: string }>> {
  const sources: Array<{ id: string; content: string }> = [];
  for (const input of inputs) {
    if (/^https?:\/\//i.test(input)) {
      const response = await fetch(input);
      if (!response.ok) {
        throw new Error(`source_fetch_failed: ${input} (${response.status})`);
      }
      const text = await response.text();
      sources.push({ id: input, content: text });
      continue;
    }

    const content = readFileSync(input, 'utf8');
    sources.push({ id: input, content });
  }
  return sources;
}

type SourceChunk = {
  id: string;
  content: string;
  index: number;
};

async function fillSlotsWithAi(params: {
  markdown: string;
  slots: ReturnType<typeof extractTemplateSlots>['slots'];
  sources: Array<{ id: string; content: string }>;
  model?: string;
  baseUrl?: string;
  apiKey?: string;
  chunkSize: number;
  maxChunks: number;
}): Promise<AssistResult> {
  const baseUrl =
    params.baseUrl ??
    process.env.IDEAMARK_OPENAI_BASE_URL ??
    process.env.OPENAI_BASE_URL ??
    'https://api.openai.com/v1';
  const apiKey =
    params.apiKey ??
    process.env.IDEAMARK_OPENAI_API_KEY ??
    process.env.OPENAI_API_KEY;
  const model = params.model ?? process.env.IDEAMARK_OPENAI_MODEL ?? 'gpt-4o-mini';

  if (!apiKey) {
    return {
      ok: false,
      errors: [{ code: 'missing_api_key', message: 'API key is required' }],
    };
  }

  const warnings: Array<{ code: string; message: string }> = [];
  const report: Array<{ slot: string; chunks: Array<{ id: string; index: number }> }> =
    [];
  const lines = params.markdown.split(/\r?\n/);
  const updates: Array<{ yaml: string; start: number; end: number; slot: string }> =
    [];
  const sourceChunks = buildSourceChunks(params.sources, params.chunkSize);

  for (const slot of params.slots) {
    if (!slot.meta.blockStartLine || !slot.meta.blockEndLine) {
      warnings.push({
        code: 'slot_missing_block',
        message: `slot "${slot.name}" has no YAML block to fill`,
      });
      continue;
    }

    const selectedChunks = selectSourceChunksForSlot(
      slot,
      sourceChunks,
      params.maxChunks,
    );
    const prompt = buildSlotPrompt(slot, selectedChunks);
    const response = await callOpenAi({
      baseUrl,
      apiKey,
      model,
      messages: [
        {
          role: 'system',
          content:
            'You are a template filler. Output only valid YAML. Do not add commentary.',
        },
        { role: 'user', content: prompt },
      ],
      temperature: 0.2,
    });

    report.push({
      slot: slot.name,
      chunks: selectedChunks.map((chunk) => ({ id: chunk.id, index: chunk.index })),
    });

    const yamlText = extractYamlFromResponse(response);
    try {
      parseYaml(yamlText);
    } catch (error) {
      warnings.push({
        code: 'invalid_yaml',
        message: `slot "${slot.name}" produced invalid YAML`,
      });
      continue;
    }

    updates.push({
      slot: slot.name,
      yaml: yamlText,
      start: slot.meta.blockStartLine,
      end: slot.meta.blockEndLine,
    });
  }

  updates.sort((a, b) => b.start - a.start);
  for (const update of updates) {
    const contentStart = update.start;
    const contentLength = update.end - update.start - 1;
    const yamlLines = update.yaml.split(/\r?\n/);
    lines.splice(contentStart, contentLength, ...yamlLines);
  }

  const provenanceResult = applyProvenance(lines.join('\n'), {
    model,
    baseUrl,
    sources: params.sources.map((source) => source.id),
    slots: params.slots.map((slot) => slot.name),
  });

  if ('message' in provenanceResult) {
    warnings.push({
      code: 'provenance_update_failed',
      message: provenanceResult.message,
    });
    return { ok: true, markdown: lines.join('\n'), warnings, report };
  }

  return { ok: true, markdown: provenanceResult.markdown, warnings, report };
}

function buildSlotPrompt(
  slot: ReturnType<typeof extractTemplateSlots>['slots'][number],
  sources: SourceChunk[],
): string {
  const parts: string[] = [];
  parts.push(`Slot: ${slot.heading}`);
  if (slot.description) {
    parts.push('Slot Description:');
    parts.push(slot.description);
  }
  parts.push('YAML Skeleton:');
  parts.push('```yaml');
  parts.push(slot.yaml.trim());
  parts.push('```');
  parts.push('Sources:');
  if (sources.length === 0) {
    parts.push('- (none)');
  }
  for (const source of sources) {
    parts.push(`--- SOURCE: ${source.id} [chunk ${source.index}] ---`);
    parts.push(source.content);
  }
  parts.push(
    [
      'Instructions:',
      '- Fill only the YAML keys provided in the skeleton.',
      '- Do not add new keys.',
      '- If information is missing, use empty strings or empty lists.',
      '- Output YAML only.',
    ].join('\n'),
  );
  return parts.join('\n\n');
}

function extractYamlFromResponse(response: string): string {
  const fenceMatch = response.match(/```(?:yaml|yml)?\s*([\s\S]*?)```/i);
  if (fenceMatch) {
    return fenceMatch[1].trim();
  }
  return response.trim();
}

function buildSourceChunks(
  sources: Array<{ id: string; content: string }>,
  maxChars: number,
): SourceChunk[] {
  const chunks: SourceChunk[] = [];
  for (const source of sources) {
    const parts = splitSourceContent(source.content, maxChars);
    parts.forEach((content, index) => {
      chunks.push({ id: source.id, content, index });
    });
  }
  return chunks;
}

function splitSourceContent(content: string, maxChars: number): string[] {
  const paragraphs = content.split(/\n{2,}/);
  const chunks: string[] = [];
  let current = '';

  for (const paragraph of paragraphs) {
    if (paragraph.trim() === '') {
      continue;
    }
    if (current.length + paragraph.length + 2 <= maxChars) {
      current = current ? `${current}\n\n${paragraph}` : paragraph;
      continue;
    }
    if (current) {
      chunks.push(current);
      current = '';
    }
    if (paragraph.length > maxChars) {
      for (let i = 0; i < paragraph.length; i += maxChars) {
        chunks.push(paragraph.slice(i, i + maxChars));
      }
    } else {
      current = paragraph;
    }
  }

  if (current) {
    chunks.push(current);
  }

  return chunks;
}

function applyProvenance(
  markdown: string,
  meta: {
    model: string;
    baseUrl: string;
    sources: string[];
    slots: string[];
  },
): { ok: true; markdown: string } | { ok: false; message: string } {
  const parsed = parseFrontmatter(markdown);
  if ('errors' in parsed) {
    return { ok: false, message: 'frontmatter is missing or invalid' };
  }

  const frontmatter = { ...parsed.frontmatter };
  const provenance = Array.isArray(frontmatter.provenance)
    ? frontmatter.provenance.slice()
    : [];
  provenance.push({
    source: 'ideamark-cli',
    at: new Date().toISOString(),
    task: 'assist.fill',
    model: meta.model,
    base_url: meta.baseUrl,
    slots: meta.slots,
    inputs: meta.sources,
  });
  frontmatter.provenance = provenance;

  const renderedFrontmatter = stringifyYaml(frontmatter).trimEnd();
  const outputText = `---\n${renderedFrontmatter}\n---\n${parsed.body}`;
  return { ok: true, markdown: outputText };
}

function selectSourceChunksForSlot(
  slot: ReturnType<typeof extractTemplateSlots>['slots'][number],
  chunks: SourceChunk[],
  maxChunks: number,
): SourceChunk[] {
  const query = [
    slot.heading,
    slot.description,
    slot.yaml,
  ]
    .join(' ')
    .toLowerCase()
    .split(/[^a-z0-9_]+/g)
    .filter((token) => token.length >= 3);
  const uniqueTerms = Array.from(new Set(query));

  const scored = chunks.map((chunk) => {
    const text = chunk.content.toLowerCase();
    let score = 0;
    for (const term of uniqueTerms) {
      if (text.includes(term)) {
        score += 1;
      }
    }
    return { chunk, score };
  });

  scored.sort((a, b) => b.score - a.score);
  const selected = scored.filter((item) => item.score > 0).slice(0, maxChunks);
  if (selected.length > 0) {
    return selected.map((item) => item.chunk);
  }

  return chunks.slice(0, maxChunks);
}

async function callOpenAi(params: {
  baseUrl: string;
  apiKey: string;
  model: string;
  messages: Array<{ role: 'system' | 'user' | 'assistant'; content: string }>;
  temperature: number;
}): Promise<string> {
  const response = await fetch(`${params.baseUrl.replace(/\/+$/, '')}/chat/completions`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${params.apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: params.model,
      messages: params.messages,
      temperature: params.temperature,
    }),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(`openai_error: ${response.status} ${text}`);
  }

  const data = (await response.json()) as {
    choices?: Array<{ message?: { content?: string } }>;
  };
  const content = data.choices?.[0]?.message?.content;
  if (!content) {
    throw new Error('openai_error: empty response');
  }
  return content;
}

program.parse();
