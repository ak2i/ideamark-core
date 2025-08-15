import { join, resolve } from 'path';
import { readFileSync } from 'fs';
import { writeText } from '../core/fsx.js';
import { buildOpenAiClient, systemPromptFromAbout, resolveSchemaPath } from '../core/llm.js';
import { validateAgainstSchema, formatAjvErrors } from '../core/validator.js';

export async function cmdSynth(opts: { root: string; project: string; brief: string; schema?: string; about?: string; fix?: boolean }) {
  const root = resolve(opts.root);
  const project = opts.project;
  const brief = readFileSync(resolve(opts.brief), 'utf-8');
  const aboutContent = systemPromptFromAbout(root, opts.about); // returns content
  const schemaPath = resolveSchemaPath(root, opts.schema);
  const outPath = join(root, 'projects', project, 'design', `${project}.designdoc.yaml`);

  const system = aboutContent; // contains AboutSchema.md content
  const user = [
    'Task: Generate <project>.designdoc.yaml (DesignDoc v0.1).',
    'Must validate against the IdeaMark JSON Schema (draft 2020-12).',
    'Return YAML only. No commentary.',
    'Brief:', brief
  ].join('\n\n');

  const llm = buildOpenAiClient();
  if (!llm) {
    console.warn('No OPENAI_API_KEY set. Writing a stub DesignDoc.');
    writeText(outPath, [
      '$schema: https://json-schema.org/draft/2020-12/schema',
      `id: IdeaMark-00000000-0000-0000-0000-000000000000`,
      `title: ${project}`,
      'type: system_design',
      'problem: { summary: "stub"}',
      'solution: { approach: "stub"}',
      'design: { version: ideamark-design/0.1 }'
    ].join('\n'));
  } else {
    const content = await llm.chat([ {role:'system', content: system}, {role:'user', content: user} ]);
    writeText(outPath, content);
  }

  let { valid, errors } = validateAgainstSchema(schemaPath, outPath);
  if (valid) { console.log('Validation PASS'); return; }
  console.error('Validation FAIL:\n' + formatAjvErrors(errors));
  if (!opts.fix) return;

  const llm2 = buildOpenAiClient();
  if (!llm2) return;
  const fixPrompt = [
    'The YAML below failed validation. Fix minimally and return corrected YAML only.',
    'Errors:', formatAjvErrors(errors),
    'YAML:', readFileSync(outPath, 'utf-8')
  ].join('\n\n');
  const fixed = await llm2.chat([ {role:'system', content: system}, {role:'user', content: fixPrompt} ]);
  writeText(outPath, fixed);

  ({ valid, errors } = validateAgainstSchema(schemaPath, outPath));
  console.log(valid ? 'Validation PASS after auto-fix' : 'Still failing:\n' + formatAjvErrors(errors));
}
