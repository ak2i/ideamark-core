import { join, resolve } from 'path';
import { loadYaml, writeText } from '../core/fsx.js';
import { genTypesFromDomain, genJsonSchemaFromDomain } from '../core/generator.js';
import Mustache from 'mustache';
import { readdirSync, readFileSync, existsSync } from 'fs';

export async function cmdGenerate(opts: { root: string; project: string }) {
  const root = resolve(opts.root);
  const project = opts.project;
  const docPath = join(root, 'projects', project, 'design', `${project}.designdoc.yaml`);
  const doc = loadYaml<any>(docPath);
  const domain = doc?.design?.domain || {};
  const title = doc?.title || project;

  // types.ts
  writeText(join(root, 'projects', project, 'generated', `${project}.types.ts`), genTypesFromDomain(domain, title));

  // schema.json
  writeText(join(root, 'projects', project, 'generated', `${project}.schema.json`), genJsonSchemaFromDomain(domain, title));

  // ADR-XXXX.md
  const adrDir = join(root, 'projects', project, 'adr');
  const files = existsSync(adrDir) ? readdirSync(adrDir).filter(f => /ADR-\d{4}\.md$/.test(f)) : [];
  const next = (Math.max(0, ...files.map(f => parseInt((f.match(/ADR-(\d{4})\.md$/) || [])[1] || '0', 10))) + 1).toString().padStart(4, '0');

  const templatePath = join(root, 'templates', 'adr-0001.mustache');
  const template = readFileSync(templatePath, 'utf-8');
  const adrMd = Mustache.render(template, {
    index: next,
    date: new Date().toISOString().slice(0,10),
    title: doc?.title || project,
    domain: doc?.design?.taxonomy?.domain || '',
    subdomain: doc?.design?.taxonomy?.subdomain || '',
    maturity: doc?.design?.taxonomy?.maturity || '',
    compat: (doc?.design?.taxonomy?.compat || []).join(', '),
    context: doc?.problem?.summary || '',
    approach: doc?.solution?.approach || '',
    consequences: (doc?.design?.applicability?.tradeoffs || [])
      .concat(doc?.design?.comparability?.constraint_set || [])
      .map((s: string)=>`- ${s}`).join('\n') || '- (n/a)',
    regs: (doc?.design?.applicability?.regulatory_notes || []).map((s: string)=>`- ${s}`).join('\n') || '- (none noted)'
  });
  writeText(join(adrDir, `${project}.ADR-${next}.md`), adrMd);

  console.log('Generated types/schema/ADR under projects/%s', project);
}
