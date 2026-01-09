import { readFileSync } from 'node:fs';
import { Command } from 'commander';
import { parse, validate } from '@ideamark/core';

const program = new Command();

program.name('ideamark').description('IdeaMark CLI');

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
    if (!parsed.ok) {
      const result = { ok: false, errors: parsed.errors };
      console.error(JSON.stringify(result, null, 2));
      process.exitCode = 1;
      return;
    }

    const validated = validate(parsed.document);
    if (!validated.ok) {
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

program.parse();
