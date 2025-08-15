import { join, resolve } from 'path';
import { ensureDir, writeText, copyIfMissing, fileExists } from '../core/fsx.js';

export async function cmdInit(opts: { root: string; project: string }) {
  const root = resolve(opts.root);
  const project = opts.project;

  // repo skeleton
  ['schema','docs','templates','projects','examples'].forEach(d => ensureDir(join(root, d)));

  // copy schema/docs if missing (prefer root/schema maintained by repo)
  const assetRoot = new URL('../../', import.meta.url).pathname;
  const bundledSchema = join(assetRoot, 'assets', 'ideamark.schema.yaml');
  const bundledAbout  = join(assetRoot, 'assets', 'AboutSchema.md');
  const schemaPath = join(root, 'schema', 'ideamark.schema.yaml');
  const aboutPath  = join(root, 'schema', 'AboutSchema.md');
  if (!fileExists(schemaPath) && fileExists(bundledSchema)) copyIfMissing(bundledSchema, schemaPath);
  if (!fileExists(aboutPath)  && fileExists(bundledAbout))  copyIfMissing(bundledAbout,  aboutPath);

  // template
  const adrTpl = join(assetRoot, 'assets', 'templates', 'adr-0001.mustache');
  const tplDst = join(root, 'templates', 'adr-0001.mustache');
  if (fileExists(adrTpl)) copyIfMissing(adrTpl, tplDst);

  // project skeleton
  const proj = join(root, 'projects', project);
  ['design','adr','generated','briefs'].forEach(d => ensureDir(join(proj, d)));
  writeText(join(proj, 'briefs', `${project}.brief.md`), `# ${project} Brief\n\nDescribe business context, scope, constraints...\n`);

  // .genrc.json (example)
  const genrc = {
    version: '1',
    validate: { schema: 'schema/ideamark.schema.yaml', failOnWarning: true },
    inputs: [ `projects/${project}/design/${project}.designdoc.yaml` ],
    targets: {
      typescript: { outDir: `projects/${project}/generated`, fileName: `${project}.types.ts` },
      jsonSchema: { outDir: `projects/${project}/generated`, fileName: `${project}.schema.json` },
      adr: { outDir: `projects/${project}/adr`, fileName: `${project}.ADR-0001.md` }
    }
  };
  writeText(join(root, '.genrc.json'), JSON.stringify(genrc, null, 2));

  console.log('Initialized repo at', root);
  console.log('Project:', project);
}
