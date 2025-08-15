import { join, resolve } from 'path';
import { readFileSync } from 'fs';
import { writeText } from '../core/fsx.js';
import { buildOpenAiClient, systemPromptFromAbout } from '../core/llm.js';

export async function cmdOutline(opts: { root: string; project: string; brief: string; about?: string }) {
  const root = resolve(opts.root);
  const project = opts.project;
  const brief = readFileSync(resolve(opts.brief), 'utf-8');
  const sys = systemPromptFromAbout(root, opts.about);

  const user = [
    'Create a structured outline for a DesignDoc based on this brief.',
    'Return JSON strictly matching:',
    '{ "taxonomy": {...}, "domain": {"entities":[], "valueObjects":[]}, "capabilities": {"commands":[], "queries":[]}, "constraints": [] }',
    'Brief:', brief
  ].join('\n\n');

  const llm = buildOpenAiClient();
  if (!llm) {
    console.warn('No OPENAI_API_KEY set. Writing a stub outline.');
    writeText(join(root, 'projects', project, 'design', `${project}.outline.json`), JSON.stringify({ taxonomy:{}, domain:{}, capabilities:{}, constraints:[] }, null, 2));
    return;
  }
  const content = await llm.chat([ {role:'system', content: sys}, {role:'user', content: user} ], { json: true });
  writeText(join(root, 'projects', project, 'design', `${project}.outline.json`), content);
  console.log('Outline written.');
}
