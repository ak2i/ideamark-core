import { Ajv2020 } from 'ajv/dist/2020.js';
import { parse as parseYaml } from 'yaml';
import schema from '../spec/ideamark.schema.json' with { type: 'json' };

export type SchemaValidationResult =
  | { ok: true }
  | { ok: false; errors: unknown };

const ajv = new Ajv2020({ allErrors: true, strict: false });
const validateFn = ajv.compile(schema);

export function validateIdeaMark(doc: unknown): SchemaValidationResult {
  const ok = validateFn(doc);
  if (ok) return { ok: true };
  return { ok: false, errors: validateFn.errors };
}

// placeholder: link/reference resolver to be implemented
export function resolveReferences(_doc: unknown) {
  return { ok: true as const };
}

export type ParseResult =
  | { ok: true; document: IdeaMarkDocument; warnings: ParseWarning[] }
  | { ok: false; errors: ParseError[] };

export type ValidateResult =
  | { ok: true; warnings: ValidationWarning[] }
  | { ok: false; errors: ValidationError[] };

export type IdeaMarkDocument = {
  frontmatter: Record<string, unknown>;
  body: string;
  structuredBlocks: StructuredBlock[];
  raw: {
    markdown: string;
    frontmatterText: string | null;
  };
};

export type StructuredBlock = {
  lang: 'yaml' | 'json' | 'unknown';
  content: string;
  data?: unknown;
  meta: {
    startLine: number;
    endLine: number;
  };
};

export type ParseError = {
  code:
    | 'frontmatter_missing'
    | 'frontmatter_invalid_yaml'
    | 'frontmatter_not_object';
  message: string;
  line?: number;
};

export type ParseWarning = {
  code: 'structured_block_invalid';
  message: string;
  line: number;
};

export type ValidationError = {
  code:
    | 'required_field_missing'
    | 'invalid_ideamark_version'
    | 'invalid_field_type'
    | 'invalid_created_at'
    | 'invalid_lang';
  message: string;
  field?: string;
};

export type ValidationWarning = {
  code: 'recommended_field_missing';
  message: string;
  field?: string;
};

const REQUIRED_FIELDS = [
  'ideamark_version',
  'template_id',
  'doc_id',
  'created_at',
  'lang',
] as const;

const RECOMMENDED_FIELDS = ['created_by', 'provenance'] as const;

export function parse(markdown: string): ParseResult {
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
  const baseLine = closingIndex + 2;
  const { blocks, warnings } = extractStructuredBlocks(body, baseLine);

  return {
    ok: true,
    document: {
      frontmatter: frontmatter as Record<string, unknown>,
      body,
      structuredBlocks: blocks,
      raw: {
        markdown,
        frontmatterText,
      },
    },
    warnings,
  };
}

export function validate(doc: IdeaMarkDocument): ValidateResult {
  const errors: ValidationError[] = [];
  const warnings: ValidationWarning[] = [];

  for (const field of REQUIRED_FIELDS) {
    if (!(field in doc.frontmatter)) {
      errors.push({
        code: 'required_field_missing',
        message: `required field missing: ${field}`,
        field,
      });
    }
  }

  const ideamarkVersion = doc.frontmatter.ideamark_version;
  if (ideamarkVersion !== undefined) {
    if (typeof ideamarkVersion !== 'number') {
      errors.push({
        code: 'invalid_field_type',
        message: 'ideamark_version must be a number',
        field: 'ideamark_version',
      });
    } else if (ideamarkVersion !== 1) {
      errors.push({
        code: 'invalid_ideamark_version',
        message: 'ideamark_version must be 1',
        field: 'ideamark_version',
      });
    }
  }

  const stringFields: Array<'template_id' | 'doc_id' | 'created_at' | 'lang'> =
    ['template_id', 'doc_id', 'created_at', 'lang'];
  for (const field of stringFields) {
    const value = doc.frontmatter[field];
    if (value !== undefined) {
      if (typeof value !== 'string' || value.trim() === '') {
        errors.push({
          code: 'invalid_field_type',
          message: `${field} must be a non-empty string`,
          field,
        });
      }
    }
  }

  const createdAt = doc.frontmatter.created_at;
  if (typeof createdAt === 'string' && createdAt.trim() !== '') {
    const timestamp = Date.parse(createdAt);
    if (Number.isNaN(timestamp)) {
      errors.push({
        code: 'invalid_created_at',
        message: 'created_at must be a valid ISO 8601 timestamp',
        field: 'created_at',
      });
    }
  }

  const lang = doc.frontmatter.lang;
  if (typeof lang === 'string' && lang.trim() !== '') {
    const langPattern = /^[A-Za-z]{2,3}(-[A-Za-z0-9]{2,8})*$/;
    if (!langPattern.test(lang)) {
      errors.push({
        code: 'invalid_lang',
        message: 'lang must be a valid BCP-47 tag',
        field: 'lang',
      });
    }
  }

  for (const field of RECOMMENDED_FIELDS) {
    if (!(field in doc.frontmatter)) {
      warnings.push({
        code: 'recommended_field_missing',
        message: `recommended field missing: ${field}`,
        field,
      });
    }
  }

  if (errors.length > 0) {
    return { ok: false, errors };
  }

  return { ok: true, warnings };
}

function extractStructuredBlocks(
  body: string,
  baseLine: number,
): { blocks: StructuredBlock[]; warnings: ParseWarning[] } {
  const blocks: StructuredBlock[] = [];
  const warnings: ParseWarning[] = [];
  const lines = body.split(/\r?\n/);

  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    const match = line.match(/^```(\S+)?\s*$/);
    if (!match) {
      i += 1;
      continue;
    }

    const info = (match[1] ?? '').toLowerCase();
    const lang = info === 'yaml' || info === 'yml' ? 'yaml' : info === 'json' ? 'json' : 'unknown';
    const startLine = baseLine + i;
    let endIndex = -1;

    for (let j = i + 1; j < lines.length; j += 1) {
      if (lines[j].startsWith('```')) {
        endIndex = j;
        break;
      }
    }

    if (endIndex === -1) {
      break;
    }

    if (lang !== 'unknown') {
      const content = lines.slice(i + 1, endIndex).join('\n');
      const endLine = baseLine + endIndex;
      const block: StructuredBlock = {
        lang,
        content,
        meta: {
          startLine,
          endLine,
        },
      };

      if (content.trim() !== '') {
        try {
          block.data =
            lang === 'yaml' ? parseYaml(content) : JSON.parse(content);
        } catch (error) {
          warnings.push({
            code: 'structured_block_invalid',
            message: `invalid ${lang} block`,
            line: startLine,
          });
        }
      }

      blocks.push(block);
    }

    i = endIndex + 1;
  }

  return { blocks, warnings };
}
