import Ajv from 'ajv';
import addFormats from 'ajv-formats';
import * as YAML from 'yaml';
import { readFileSync } from 'fs';

export function loadSchema(path: string) {
  const raw = readFileSync(path, 'utf-8');
  return YAML.parse(raw);
}

export function validateAgainstSchema(schemaPath: string, yamlPath: string) {
  const schema = loadSchema(schemaPath);
  const docRaw = readFileSync(yamlPath, 'utf-8');
  const doc = YAML.parse(docRaw);
  const ajv = new Ajv({ strict: true, allErrors: true });
  addFormats(ajv);
  const validate = ajv.compile(schema);
  const valid = validate(doc);
  return { valid: !!valid, errors: validate.errors || [], doc };
}

export function formatAjvErrors(errors: any[] = []) {
  return errors.map(e => `- ${e.instancePath || '(root)'} ${e.message} ${e.params ? JSON.stringify(e.params) : ''}`).join('\n');
}
