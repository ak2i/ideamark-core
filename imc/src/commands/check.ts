import { join, resolve } from 'path';
import { execSync } from 'child_process';
import { existsSync } from 'fs';

export async function cmdCheck(opts: { root: string; project: string }) {
  const root = resolve(opts.root);
  const project = opts.project;
  const prettier = existsSync(join(root, 'node_modules', '.bin', 'prettier')) ? join(root, 'node_modules', '.bin', 'prettier') : 'prettier';
  try {
    execSync(`${prettier} -w "${join(root, 'projects', project)}"`, {
      stdio: 'inherit',
    });
  } catch {
    console.warn('Prettier not found or failed. Skipping format.');
  }
  console.log('check: done');
}
