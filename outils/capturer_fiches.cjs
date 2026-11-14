const { chromium } = require('playwright'); const fs = require('fs'); const [dir, out] = process.argv.slice(2);
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 794, height: 1123 }, deviceScaleFactor: 2 });
  fs.mkdirSync(out, { recursive: true });
  for (const f of fs.readdirSync(dir).filter(x => x.endsWith('.html')).sort()) { const n = f.replace('.html', '');
    await p.goto('file://' + dir + '/' + f); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(250);
    const over = await p.evaluate(() => { const r = document.body.firstElementChild; return [r.scrollHeight, r.clientHeight, [...document.fonts].filter(x => x.status === 'loaded').length]; });
    await p.screenshot({ path: `${out}/${n}.png`, clip: { x: 0, y: 0, width: 794, height: 1123 } });
    await p.pdf({ path: `${out}/${n}.pdf`, width: '794px', height: '1123px', printBackground: true, pageRanges: '1' });
    console.log(n, over.join(' ')); }
  await b.close(); })();
