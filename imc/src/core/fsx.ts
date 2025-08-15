import { existsSync, mkdirSync, readFileSync, writeFileSync, copyFileSync, readdirSync } from 'fs';
import { dirname, join, resolve } from 'path';
import * as YAML from 'yaml';

export function ensureDir(p: string) { if (!existsSync(p)) mkdirSync(p, { recursive: true }); }
export function readText(p: string) { return readFileSync(p, 'utf-8'); }
export function writeText(p: string, s: string) { ensureDir(dirname(p)); writeFileSync(p, s, 'utf-8'); }
export function listFiles(dir: string) { return readdirSync(dir, { withFileTypes: true }).map(d => ({ name: d.name, isDir: d.isDirectory() })); }
export function loadYaml<T=any>(p: string): T { return YAML.parse(readText(p)) as T; }
export function saveYaml(p: string, obj: any) { writeText(p, YAML.stringify(obj)); }
export function copyIfMissing(src: string, dst: string) { ensureDir(dirname(dst)); if (!existsSync(dst)) copyFileSync(src, dst); }
export function fileExists(p: string) { return existsSync(p); }
export function resolvePath(...x: string[]) { return resolve(join(...x)); }
