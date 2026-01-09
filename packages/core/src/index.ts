import { Ajv } from 'ajv';
import schema from '../spec/ideamark.schema.json' with { type: 'json' };

export type ValidationResult =
  | { ok: true }
  | { ok: false; errors: unknown };

const ajv = new Ajv({ allErrors: true, strict: false });
const validateFn = ajv.compile(schema);

export function validateIdeaMark(doc: unknown): ValidationResult {
  const ok = validateFn(doc);
  if (ok) return { ok: true };
  return { ok: false, errors: validateFn.errors };
}

// placeholder: link/reference resolver to be implemented
export function resolveReferences(_doc: unknown) {
  return { ok: true as const };
}
