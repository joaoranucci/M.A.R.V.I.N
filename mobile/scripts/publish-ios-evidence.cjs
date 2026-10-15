// Publishes only fresh, unpaired simulator screenshots for visual inspection.
// Git blobs do not move branches or alter user data. The full evidence also remains in the CI artifact.
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const directory = process.argv[2];
const repository = process.env.GITHUB_REPOSITORY;
if (repository !== 'joaoranucci/M.A.R.V.I.N') throw new Error('Unexpected repository.');
const result = {};
for (const name of fs.readdirSync(directory).filter((name) => /^\d\d-[a-z-]+\.png$/.test(name))) {
  const content = fs.readFileSync(path.join(directory, name)).toString('base64');
  const response = JSON.parse(execFileSync('gh', ['api', '--method', 'POST', 'repos/' + repository + '/git/blobs', '--input', '-'], {
    input: JSON.stringify({ content, encoding: 'base64' }), encoding: 'utf8',
  }));
  result[name] = response.sha;
}
fs.writeFileSync(path.join(directory, 'screenshots.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify({ screenshots: result }));
