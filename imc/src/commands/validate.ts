import { join, resolve } from 'path';
import { validateAgainstSchema, formatAjvErrors } from '../core/validator.js';
import { resolveSchemaPath } from '../core/llm.js';

export async function cmdValidate(opts: { root: string; project: string; schema?: string }) {
  const root = resolve(opts.root);
  const project = opts.project;
  const schemaPath = resolveSchemaPath(root, opts.schema);
  const docPath = join(root, 'projects', project, 'design', `${project}.designdoc.yaml`);
  const res = validateAgainstSchema(schemaPath, docPath);
  if (res.valid) console.log('Validation PASS');
  else { console.error('Validation FAIL:\n' + formatAjvErrors(res.errors)); process.exitCode = 1; }
}
