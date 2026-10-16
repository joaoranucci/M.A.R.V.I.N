const fs = require('node:fs');
const { execFileSync } = require('node:child_process');
const app = process.argv[2];
if (!app || !fs.existsSync(app)) throw new Error('Pass the compiled simulator .app path.');
const xcrun = (args, options = {}) => execFileSync('xcrun', args, { encoding: 'utf8', ...options });
const list = JSON.parse(xcrun(['simctl', 'list', 'devices', 'available', '--json']));
const runtime = Object.keys(list.devices).filter((key) => key.includes('.iOS-'))
  .sort((a, b) => b.localeCompare(a, 'en', { numeric: true }))
  .find((key) => list.devices[key].some((device) => device.isAvailable && device.name.startsWith('iPhone')));
if (!runtime) throw new Error('No available iOS Simulator runtime.');
const phones = list.devices[runtime].filter((device) => device.isAvailable && device.name.startsWith('iPhone'));
const device = phones.find((device) => /^iPhone \d+$/.test(device.name)) || phones[0];
console.log(JSON.stringify({ simulator: device.name, runtime, udid: device.udid }));
if (device.state !== 'Booted') xcrun(['simctl', 'boot', device.udid], { stdio: 'inherit' });
xcrun(['simctl', 'bootstatus', device.udid, '-b'], { stdio: 'inherit' });
xcrun(['simctl', 'ui', device.udid, 'appearance', 'dark']);
xcrun(['simctl', 'install', device.udid, app], { stdio: 'inherit' });
if (process.env.GITHUB_ENV) fs.appendFileSync(process.env.GITHUB_ENV, 'IOS_SIMULATOR_UDID=' + device.udid + '\n');
