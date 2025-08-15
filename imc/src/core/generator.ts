// Deterministic generators: TS types and JSON Schema from DesignDoc.domain
import { writeText } from './fsx.js';

type Attr = { name: string; type: string; required?: boolean; enum?: string[]; enum_ref?: string; example?: any };
type Entity = { name: string; ns?: string; attrs?: Attr[] };
type ValueObject = { name: string; attrs?: Attr[] };
type Domain = { entities?: Entity[]; valueObjects?: ValueObject[]; enums?: any[]; relations?: any[] };

export function genTypesFromDomain(domain: Domain, title: string) {
  const lines: string[] = [];
  lines.push('// Auto-generated from IdeaMark DesignDoc');
  lines.push(`// Source: ${title}`);
  lines.push('');
  lines.push('export type Id = string; // URN-like: "user:123"');
  lines.push('');

  const renderInterface = (name: string, attrs?: Attr[]) => {
    const rows: string[] = [];
    rows.push(`export interface ${name} {`);
    for (const a of (attrs || [])) {
      let tsType = mapTs(a.type);
      if (a.enum && a.enum.length) {
        tsType = a.enum.map(v => JSON.stringify(v)).join(' | ');
      }
      const opt = a.required ? '' : '?';
      const comments: string[] = [];
      if (a.example !== undefined) comments.push(`example: ${a.example}`);
      if (a.enum_ref) comments.push(`enum_ref: ${a.enum_ref}`);
      if (comments.length) rows.push(`  /** ${comments.join(' ; ')} */`);
      rows.push(`  ${a.name}${opt}: ${tsType};`);
    }
    rows.push('}');
    return rows.join('\n');
  };

  for (const e of (domain.entities || [])) {
    lines.push(renderInterface(e.name, e.attrs));
    lines.push('');
  }
  for (const v of (domain.valueObjects || [])) {
    lines.push(renderInterface(v.name, v.attrs));
    lines.push('');
  }
  return lines.join('\n');
}

function mapTs(t: string): string {
  const m = t.trim();
  if (m === 'Id') return 'Id';
  if (m === 'string') return 'string';
  if (m === 'number') return 'number';
  if (m === 'boolean') return 'boolean';
  if (m === 'timestamp') return 'string';
  if (m === 'timestamp|null') return 'string | null';
  if (m === 'map<string, any>') return 'Record<string, unknown>';
  const arr = m.match(/^(\w+)\[\]$/);
  if (arr) return mapTs(arr[1]) + '[]';
  return m; // assume reference to VO/Entity
}

export function genJsonSchemaFromDomain(domain: Domain, title: string) {
  const defs: any = {};

  const toSchema = (attrs?: Attr[]) => {
    const properties: any = {};
    const required: string[] = [];
    for (const a of (attrs || [])) {
      let js = toJsonSchemaType(a.type);
      if (a.enum && a.enum.length) js.enum = a.enum;
      if (a.enum_ref) js.description = ((js.description || '') + ` (enum_ref: ${a.enum_ref})`).trim();
      if (a.example !== undefined) js.description = ((js.description || '') + ` (example: ${a.example})`).trim();
      properties[a.name] = js;
      if (a.required) required.push(a.name);
    }
    const obj: any = { type: 'object', properties };
    if (required.length) obj.required = required;
    return obj;
  };

  for (const v of (domain.valueObjects || [])) defs[v.name] = toSchema(v.attrs);
  for (const e of (domain.entities || [])) defs[e.name] = toSchema(e.attrs);

  const root = {
    $schema: 'https://json-schema.org/draft/2020-12/schema',
    title,
    type: 'object',
    $defs: defs
  };
  return JSON.stringify(root, null, 2);
}

function toJsonSchemaType(t: string): any {
  const m = t.trim();
  if (m === 'Id') return { type: 'string' };
  if (m === 'string') return { type: 'string' };
  if (m === 'number') return { type: 'number' };
  if (m === 'boolean') return { type: 'boolean' };
  if (m === 'timestamp') return { type: 'string', format: 'date-time' };
  if (m === 'timestamp|null') return { type: ['string', 'null'], format: 'date-time' };
  if (m === 'map<string, any>') return { type: 'object', additionalProperties: true };
  const arr = m.match(/^(\w+)\[\]$/);
  if (arr) return { type: 'array', items: toJsonSchemaType(arr[1]) };
  return { $ref: `#/$defs/${m}` };
}
