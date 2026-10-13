import { chromium } from '../.cache/browser/node_modules/playwright/index.mjs';
import fs from 'node:fs/promises';
const base=process.env.US_PREVIEW_URL || 'http://127.0.0.1:1317';
const report={date:new Date().toISOString(),base,pages:[],searches:[],interactions:[],errors:[]};
const checks='.cache/render';await fs.mkdir(checks,{recursive:true});
const ledger=JSON.parse(await fs.readFile('ops/reviews/acceptance.json','utf8'));
const topicPaths=Object.keys(ledger).map(p=>'/'+p.replace(/^content\//,'').replace(/\.md$/,'/'));
const scope=process.env.US_REVIEW_CONFIG?JSON.parse(await fs.readFile(process.env.US_REVIEW_CONFIG,'utf8')):{};
report.scope_file=process.env.US_REVIEW_CONFIG||null;
const paths=[...new Set(scope.paths||['/','/book/','/docs/routes/','/docs/regions/','/docs/regions/california/','/docs/glossary/','/docs/routes/medical-care/','/docs/routes/tax-preparation/',...topicPaths.map(p=>p.slice(0,p.lastIndexOf('/',p.length-2)+1)),...topicPaths])];
if(paths.some(p=>typeof p!=='string'||!p.startsWith('/')||p.startsWith('//')))throw new Error('Review paths must be local absolute paths');
const queries={...{'EOB':'收到医疗账单','押金':'加州租房押金','信用':'查信用报告','税务居民':'美国税务居民怎样判断','重建':'社区与学校','口译':'预约、查账单和跟进'},...scope.queries};
let browser;
const expect=(x,m)=>{if(!x)report.errors.push(m);};
try {
 for(const viewport of [{width:1440,height:1000},{width:390,height:844}]){
  const mode=viewport.width>700?'desktop':'mobile';
  browser=await chromium.launch({executablePath:process.env.US_CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
  const context=await browser.newContext({viewport,permissions:['clipboard-read','clipboard-write']});
  const page=await context.newPage();page.on('pageerror',e=>report.errors.push(mode+': '+e.message));page.on('response',r=>{if(r.url().startsWith(base)&&r.status()>=400)report.errors.push(mode+': HTTP '+r.status()+' '+r.url());});
  page.on('requestfailed',r=>{if(r.url().startsWith(base)&&r.failure()?.errorText!=='net::ERR_ABORTED')report.errors.push(mode+': '+r.failure()?.errorText+' '+r.url());});
  page.on('crash',()=>report.errors.push(mode+': browser renderer crashed'));
  for(const path of paths){
   const response=await page.goto(base+path);await page.waitForLoadState('networkidle');
   await page.evaluate(()=>Promise.all([...document.images].map(img=>img.decode().catch(()=>{}))));
   const dom=await page.evaluate(()=>({width:document.documentElement.scrollWidth,h1:[...document.querySelectorAll('main h1')].map(x=>x.textContent.trim()),strong:document.querySelectorAll('main strong').length,chars:document.querySelector('main')?.textContent.length,meta:!!document.querySelector('.editorial-meta'),images:[...document.images].filter(x=>!x.complete||x.naturalWidth===0).map(x=>x.currentSrc),tables:[...document.querySelectorAll('main table')].map(x=>({width:x.clientWidth,scroll:x.scrollWidth}))}));
   report.pages.push({mode,path,status:response.status(),...dom});
   expect(response.status()===200,`${mode} ${path}: status`);expect(dom.width<=viewport.width+1,`${mode} ${path}: overflow ${dom.width}`);expect(dom.h1.length===1,`${mode} ${path}: heading count`);expect(dom.images.length===0,`${mode} ${path}: broken images ${dom.images}`);
   if(topicPaths.includes(path))expect(dom.meta,`${mode} ${path}: missing metadata`);
   if(topicPaths.includes(path))await page.screenshot({path:`${checks}/${mode}-topic-${path.split('/').filter(Boolean).at(-1)}.png`});
   if(['/', '/book/people/health/medical-bills/','/docs/routes/medical-care/','/docs/regions/'].includes(path))await page.screenshot({path:`${checks}/${mode}-${path==='/'?'home':path.split('/').filter(Boolean).at(-1)}.png`,fullPage:path!=='/'});
  }
  await page.goto(base+'/');
  const card=page.locator('.us-card').first();await card.focus();await page.keyboard.press('Enter');await page.waitForURL('**/docs/routes/medical-care/');report.interactions.push({mode,keyboard_card:page.url()});
  await page.goto(base+'/book/people/health/medical-bills/');
  const appearance=page.locator('[data-td-appearance-trigger]:visible').first();
  await appearance.click();await page.locator('dialog[open] label').filter({has:page.locator('[data-bs-theme-value="dark"]')}).click();
  await page.keyboard.press('Escape');expect(await page.locator('html').getAttribute('data-bs-theme')==='dark',mode+': dark mode');
  await page.evaluate(()=>Promise.all(document.getAnimations().filter(a=>a.effect?.getTiming().iterations!==Infinity).map(a=>a.finished.catch(()=>{}))));
  await page.screenshot({path:`${checks}/${mode}-bill-dark.png`,fullPage:false});
  await appearance.click();await page.locator('dialog[open] label').filter({has:page.locator('[data-bs-theme-value="light"]')}).click();await page.keyboard.press('Escape');
  await page.locator('[data-td-action="copy_markdown"]:visible').first().click();
  await page.waitForFunction(()=>document.querySelector('[data-td-action="copy_markdown"].td-is-copied'));
  const copied=await page.evaluate(()=>navigator.clipboard.readText());expect(copied.includes('EOB'),mode+': copy content');report.interactions.push({mode,copy_chars:copied.length});
  for(const [query,title] of Object.entries(queries)){
   await page.locator('[data-td-shell-search-open]:visible').first().click();const input=page.locator('.td-shell-search__input');await input.fill(query);
   await page.waitForFunction(expected=>document.querySelector('#td-shell-search-results')?.textContent.includes(expected),title);
   const results=await page.locator('#td-shell-search-results').innerText();report.searches.push({mode,query,results});expect(results.includes(title),mode+': relevant search '+query);
   await page.screenshot({path:`${checks}/${mode}-search-${query}.png`});
   await page.keyboard.press('Escape');await page.locator('#td-shell-search').waitFor({state:'hidden'});expect(await page.locator('#td-shell-search').isHidden(),mode+': search Escape');
  }
  // Search result keyboard navigation must reach an actual topic.
  await page.goto(base+'/book/');
  await page.locator('[data-td-shell-search-open]:visible').first().click();await page.locator('.td-shell-search__input').fill('EOB');await page.waitForFunction(()=>document.querySelector('#td-shell-search-results [role="option"]')?.textContent.includes('收到医疗账单'));await page.keyboard.press('ArrowDown');await page.keyboard.press('ArrowUp');await page.keyboard.press('Enter');await page.waitForURL('**/medical-bills/',{waitUntil:'load'});await page.locator('#td-shell-search').waitFor({state:'hidden'});expect((await page.locator('#td-shell-search').isHidden()),mode+': search Enter');
  {
   await page.goto(base+'/book/people/health/medical-bills/');
   if(mode==='mobile')await page.locator('[data-td-shell-drawer-open]:visible').first().click();
   for(const href of ['/book/life/','/book/life/documents/']){
    const node=page.locator('.td-shell-tree__row').filter({has:page.locator(`a[href="${href}"]`)}).first();
    const toggle=node.locator('[data-td-shell-tree-toggle]');if(await toggle.getAttribute('aria-expanded')==='false'){await toggle.focus();await page.keyboard.press('Enter');}
   }
   const leaf=page.locator('.td-shell-tree__link[href="/book/life/documents/status-documents/"]');expect(await leaf.isVisible(),'unrelated sidebar leaves visible after expand');await leaf.click();await page.waitForURL('**/status-documents/');report.interactions.push({mode,sidebar_noncurrent_expand_and_click:true});
  }
  await page.goto(base+'/_print/book/');
  const print=await page.evaluate(()=>({pages:document.querySelectorAll('.td-book-print-page').length,meta:document.querySelectorAll('.editorial-meta').length,broken:[...document.querySelectorAll('a[href^="#"]')].map(x=>x.getAttribute('href').slice(1)).filter(id=>id&&!document.getElementById(decodeURIComponent(id))),external:document.querySelectorAll('.td-book-print-page a[href^="https://"]').length}));
  expect(print.broken.length===0,mode+': print anchors');expect(print.meta===topicPaths.length,mode+': print metadata count');report.interactions.push({mode,print});
  if(mode==='desktop'){await page.screenshot({path:`${checks}/desktop-print.png`});await page.pdf({path:`${checks}/book-review.pdf`,format:'A4',printBackground:true});}
  await context.close();
  await browser.close();browser=undefined;
 }
} catch(e){report.errors.push(e.stack);} finally {if(browser)await browser.close();await fs.writeFile('.cache/browser-report.json',JSON.stringify(report,null,2)+'\n');}
console.log(JSON.stringify({pages:report.pages.length,searches:report.searches.length,interactions:report.interactions,errors:report.errors},null,2));
process.exitCode=report.errors.length?1:0;
