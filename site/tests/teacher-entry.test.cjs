const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const publicPath = path.join(__dirname, '../public');
const read = name => fs.readFileSync(path.join(publicPath, name), 'utf8');

test('teacher entry pages share navigation and one keyboard skip target', () => {
  const links = ['us-history.html','reading-companions.html','planner-year.html','planner.html','home.html','subscribe.html'];
  for (const file of ['index','us-history','reading-companions','planner-year','planner','home','subscribe','the-giver','progressive-era']) {
    const page = read(file + '.html');
    assert.equal((page.match(/href="#main-content"/g) || []).length, 1, file);
    assert.match(page, /<main\b[^>]*id="main-content"[^>]*tabindex="-1"/, file);
    const nav = page.match(/<nav class="main hcg-main-nav"[^>]*>([\s\S]*?)<\/nav>/);
    assert.ok(nav, file);
    assert.deepEqual([...nav[1].matchAll(/href="([^"]+)"/g)].map(m=>m[1]), links, file);
  }
});

test('the homepage preserves the All-Access and isolated sample paths', () => {
  const page = read('index.html');
  assert.match(page, /href="subscribe\.html">See U\.S\. History All-Access/);
  assert.match(page, /href="planner\.html\?sample=progressive-era-week"/);
  assert.ok(fs.existsSync(path.join(publicPath,'assets/progressive-era-sample-week.webp')));
});

test('resource samples use rendered images and the Giver has no checkout or paid file link', () => {
  const giver = read('the-giver.html');
  const unit = read('progressive-era.html');
  for (const page of [giver,unit]) {
    const assets = [...page.matchAll(/<img src="(assets\/resource-previews\/[^"]+\.png)"/g)].map(m=>m[1]);
    assert.equal(assets.length,2);
    for (const asset of assets) assert.ok(fs.existsSync(path.join(publicPath,asset)), asset);
  }
  assert.doesNotMatch(giver,/href="[^"]*\.(?:pdf|zip|docx)|checkout-btn/);
  assert.match(unit,/<script src="email-gate\.js"/);
});
