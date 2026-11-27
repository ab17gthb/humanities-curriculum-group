const { test } = require('node:test');
const a = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const source = file => fs.readFileSync(path.join(__dirname, '../public', file), 'utf8');
const html = source('reading-companions.html');

function boot() {
  const controls = { 'rc-search': {value:''}, 'rc-grade': {value:''}, 'rc-count': {}, 'rc-empty': {} };
  const filter = {hidden:true};
  const sections = [...html.matchAll(/<section class="rc-section"[^>]*>([\s\S]*?)<\/section>/g)].map(([,body]) => {
    const cards = [...body.matchAll(/<article class="rc-card[^"]*" data-lo="(\d+)" data-hi="(\d+)"[^>]*>([\s\S]*?)<\/article>/g)]
      .map(([,lo,hi,card]) => {
        const title = card.match(/<cite>([^<]+)<\/cite>/)[1].replace(/&amp;/g,'&');
        const author = card.match(/<p class="rc-author">([^<]+)<\/p>/)[1];
        return { title, author, dataset:{lo,hi}, querySelector:s=>({textContent:s==='h3'?title:author}) };
      });
    return {cards,querySelectorAll:()=>cards};
  });
  const cards = sections.flatMap(s=>s.cards);
  for(const x of Object.values(controls)) x.addEventListener=function(evt, cb){this['on'+evt]=cb;};
  vm.runInNewContext(source('reading-companions.js'),{
    document:{querySelector:()=>filter,getElementById:id=>controls[id],querySelectorAll:()=>sections},
    window:{addEventListener(){}}
  });
  function show(q, g='') {
    controls['rc-search'].value=q;
    controls['rc-grade'].value=g;
    controls['rc-search'].oninput();
    return cards.filter(c=>!c.hidden).map(c=>c.title);
  }
  return {cards,sections,controls,filter,show};
}

test('catalog contains 39 unique static titles and no buyer downloads',()=>{
  const b=boot();
  a.equal(b.cards.length,39); a.equal(new Set(b.cards.map(c=>c.title)).size,39);
  a.equal(b.filter.hidden,false);
  a.equal(b.controls['rc-count'].textContent,'39 companions');
  a.doesNotMatch(html, /href="[^"]+\.(?:pdf|zip|docx)|Buyer Download|Muse Listing|Checkout/i);
});

test('title or author search and grade filtering work together',()=>{
  const b=boot();
  a.deepEqual(b.show('winn dixie'),['Because of Winn-Dixie']);
  a.deepEqual(b.show('shakespeare','9'),['Romeo and Juliet']);
  a.deepEqual(b.show('shakespeare','5'),[]);
  a.equal(b.controls['rc-empty'].hidden,false);
  a.ok(b.sections.every(s=>s.hidden));
  for(let i=3;i<=12;i++) {
    a.equal(b.show('',String(i)).length,b.cards.filter(c=>+c.dataset.lo<=i&&i<=+c.dataset.hi).length);
  }
  a.equal(b.show('').length,39);
});
