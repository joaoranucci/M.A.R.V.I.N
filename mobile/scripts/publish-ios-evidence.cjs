// Publishes only fresh, unpaired simulator screenshots for visual inspection.
// Git blobs do not move branches or alter user data. The full evidence also remains in the CI artifact.
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const directory = process.argv[2];
const repository = process.env.GITHUB_REPOSITORY;
if (repository !== 'joaoranucci/M.A.R.V.I.N') throw new Error('Unexpected repository.');
const result = {};
const previews = {};
for (const relative of fs.readdirSync(directory, { recursive: true })) {
  const name = path.basename(relative);
  if (!/^0[0-8]-[a-z-]+\.png$/.test(name)) continue;
  const file = path.join(directory, relative);
  if (!fs.statSync(file).isFile()) continue;
  if (result[name]) throw new Error('Duplicate screenshot name: ' + name);
  const content = fs.readFileSync(file).toString('base64');
  const response = JSON.parse(execFileSync('gh', ['api', '--method', 'POST', 'repos/' + repository + '/git/blobs', '--input', '-'], {
    input: JSON.stringify({ content, encoding: 'base64' }), encoding: 'utf8',
  }));
  result[name] = response.sha;
  // Text-only review clients can read this exact PNG as base64 without changing its pixels.
  const preview = JSON.parse(execFileSync('gh', ['api', '--method', 'POST', 'repos/' + repository + '/git/blobs', '--input', '-'], {
    input: JSON.stringify({ content, encoding: 'utf-8' }), encoding: 'utf8',
  }));
  previews[name] = preview.sha;
}
fs.writeFileSync(path.join(directory, 'screenshots.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({ screenshots: result, previews }));
