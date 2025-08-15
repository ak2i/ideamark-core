export type LlmClient = {
  chat: (messages: {role: 'system'|'user'|'assistant', content: string}[], opts?: {json?: boolean}) => Promise<string>;
};

export function buildOpenAiClient(): LlmClient | null {
  const key = process.env.OPENAI_API_KEY;
  if (!key) return null;
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const { OpenAI } = require('openai');
  const client = new OpenAI({ apiKey: key });
  return {
    async chat(messages, opts) {
      const model = process.env.IMC_OPENAI_MODEL || 'gpt-4o-mini';
      const response = await client.chat.completions.create({
        model,
        messages,
        temperature: 0,
        response_format: opts?.json ? { type: 'json_object' } : undefined
      } as any);
      return response.choices[0]?.message?.content || '';
    }
  };
}

import { existsSync, readFileSync } from 'fs';
import { join } from 'path';
export function systemPromptFromAbout(root: string, aboutOpt?: string) {
  const paths = aboutOpt ? [aboutOpt] : [
    join(root, 'schema', 'AboutSchema.md'),
    join(root, 'docs', 'AboutSchema.md')
  ];
  const hit = paths.find(p => existsSync(p));
  if (!hit) throw new Error('AboutSchema.md not found under /schema or /docs. Pass --about to specify explicitly.');
  return `You are an IdeaMark design compiler.\n\n` + readFileSync(hit, 'utf-8');
}

export function resolveSchemaPath(root: string, schemaOpt?: string) {
  if (schemaOpt) return schemaOpt;
  const p = require('path').join(root, 'schema', 'ideamark.schema.yaml');
  if (!require('fs').existsSync(p)) {
    throw new Error('ideamark.schema.yaml not found under /schema. Pass --schema to specify explicitly.');
  }
  return p;
}
