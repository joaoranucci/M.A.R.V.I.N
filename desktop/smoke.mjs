import { chromium, expect } from '@playwright/test';
import fs from 'node:fs';
const session=JSON.parse(fs.readFileSync(new URL('../data/presence-test/presence-session.json',import.meta.url),'utf8'));
const browser=await chromium.launch({channel:'msedge',headless:true});
try {
const page=await browser.newPage({viewport:{width:1440,height:940}});
const errors=[];page.on('pageerror',e=>errors.push(e.message));
await page.goto(session.url);await page.waitForSelector('.connection-dot.online');
await page.keyboard.press('Control+Space');await expect(page.getByRole('textbox',{name:'Mensagem para o MARVIN'})).toBeVisible();
await page.keyboard.press('Escape');
await page.getByRole('button',{name:'Projetos',exact:true}).first().click();
await page.getByRole('textbox',{name:'Nome do projeto'}).fill('interface-validada');
await page.locator('form').getByRole('button').click();
await expect(page.locator('.file-tree h3')).toHaveText('interface-validada');
await page.screenshot({path:'../data/presence-focus.png'});
for(const name of ['Tarefas','Agenda','Conhecimento','Pesquisa','Sistema']){
 await page.locator('.sidebar').getByRole('button',{name,exact:true}).click();
 await page.waitForTimeout(150);
}
await page.getByRole('button',{name:'Recolher',exact:true}).click();
await expect(page.getByRole('button',{name:'Expandir MARVIN'})).toBeVisible();
await page.getByRole('button',{name:'Expandir MARVIN'}).click();
await page.locator('.sidebar').getByRole('button',{name:'Início',exact:true}).click();
await page.setViewportSize({width:700,height:850});
await page.screenshot({path:'../data/presence-small.png'});
expect(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth)).toBe(false);
expect(errors).toEqual([]);
console.log('PASS: keyboard, project creation, Focus, all panels, compact, responsive, no JavaScript errors');
} finally {await browser.close();}
