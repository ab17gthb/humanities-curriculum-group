const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const root=require('node:path').resolve(__dirname,'../public')+'/';
const code=fs.readFileSync(root+'planner.js','utf8');
const data=fs.readFileSync(process.env.HCG_PLANNER_DATA || root+'planner-data.js','utf8');
const html=fs.readFileSync(root+'planner.html','utf8');
const bootstrap=html.match(/<script>\s*\/\/ Do not even initialize[\s\S]*?<\/script>/)[0].slice(8,-9);
const regularKey='hcg_unit_v1';
const yearKey='hcg_year_v1';
const uuid='b9265234-4732-4bd6-8e0a-161366ab74f1';
const seed={
  [regularKey]:JSON.stringify({selected:{'l3-reading':true},sections:[{name:'Original Regular Class',start:'2026-11-30',test:'2026-12-09'}]}),
  [yearKey]:JSON.stringify({daysOff:[{from:'2026-11-30',to:'2026-11-30',label:'Year plan closure'}]}),
};
function setup(search, { storage={...seed}, hash='', failWrites=false, failReads=false, confirm=true }={}) {
  const log=[], requests=[], eventHandlers={}, elements={};
  let href, hrefReplaced, downloaded, exportBlob;
  const notices=[];
  function node(id) {
    return elements[id] ||= {
      id, innerHTML:'', textContent:'', value:'', style:{}, hidden:false, dataset:{}, classList:{add(){},toggle(){}},
      querySelectorAll(){return [];}, className:'',
      parentNode:{insertBefore(child,before){ this.lastInsert=[child.id,before.id]; }},
      addEventListener(t,fn){eventHandlers[id+':'+t]=fn;},
      getAttribute(key){return this.dataset[key] || null;},
      scrollIntoView(){}, insertAdjacentHTML(_where, text){this.innerHTML+=text;},
    };
  }
  node('list').dataset['data-view']='list'; node('week').dataset['data-view']='week';
  const document={
    getElementById:node,
    querySelectorAll(selector){return selector==='[data-view]'?[node('list'),node('week')]:[];},
    documentElement:node('html'),
    createElement(){ return {click(){ downloaded=this.download; }}; },
    head:{appendChild(el){ requests.push([el.src,el.async]); }},
  };
  const localStorage={
    getItem(key){log.push(['get',key]); if(failReads)throw Error('blocked'); return storage[key] ?? null;},
    setItem(key,val){log.push(['set',key]); if(failWrites)throw Error('quota'); storage[key]=val;},
  };
  const window={ addEventListener(){},print(){},confirm(msg){notices.push(msg);return confirm;},alert(msg){notices.push(msg);} };
  const context=vm.createContext({window,document,localStorage,URLSearchParams,crypto:{randomUUID(){return uuid;}},
    location:{search,hash,pathname:'/planner.html',assign(route){href=route;}},
    atob, escape, Blob, URL:class extends URL { static createObjectURL(b){exportBlob=b;return 'blob:unit-qa';} static revokeObjectURL(){} },
    FileReader:class{readAsText(file){this.result=file.text;this.onload();}},
    history:{replaceState(_state,_title,url){hrefReplaced=url;}}
  });
  vm.runInContext(data,context);
  vm.runInContext(fs.readFileSync(require("node:path").join(__dirname, "../public/unit-scheduler.js"), "utf8"), context);
  // Test the real render model as well as generated content, without making this a public API.
  const harness=code.replace(/\n}\)\(\);\s*$/, `
    window.__fixture = {
      model:function(){return L;}, state:function(){return state;}, dates:candidateDays,
      changeDay:function(date,type){SEC().dayTypes[date]=type;render();},
      reflow:render, split:toggleSplit, move:moveEntryToDay, cloneSection:newSection
    };
  })();`);
  vm.runInContext(harness,context);
  vm.runInContext(bootstrap,context);
  return {node,log,requests,storage,notices,api:window.__fixture,exportFile:()=>({downloaded,exportBlob}),hrefReplaced:()=>hrefReplaced,href:()=>href, event(id,type,value){
    if(value!==undefined)node(id).value=value;
    eventHandlers[id+':'+type].call(node(id),{preventDefault(){}});
  }};
}
const id='x-project', custom={id,title:'Primary source project',days:2,kind:'own',link:'https://example.test',note:'Compare accounts',bp:[15]};
function fixture({start='2026-11-23',end='2026-11-26',period=45,rotation='daily',pins={},dayTypes={},subDays={},homework={},splits={},selected,extraSections=[],order,view='list'}={}, extra={}) {
  const plan={selected:selected||{[id]:true},customItems:[custom],splits,order:order||[id],view,
              sections:[{name:'Period 1',start,test:end,period,rotation,pins,dayTypes,subDays,homework},...extraSections]};
  const storage={ [regularKey]:JSON.stringify(plan) };
  if (extra.year) storage[yearKey]=JSON.stringify(extra.year);
  return setup('',{storage,...extra});
}
function slot(model,date) { return model.buckets.find(b=>b.iso===date); }

test('single remaining 45-minute meeting keeps the start and reports one day left out of coverage',()=>{
  const r=fixture({end:'2026-11-24'});
  const m=r.api.model();
  assert.equal(slot(m,'2026-11-23').entries[0].key,id);
  assert.equal(slot(m,'2026-11-23').load,1);
  assert.equal(m.overflow.length,1);
  assert.equal(m.overflow[0].remainingDays,1);
  assert.match(r.node('overflow').innerHTML,/1 lesson-day remaining/);
  assert.match(r.node('covplaced').textContent,/0 of 15/);
  r.event('print-week','click');
  assert.match(r.node('printArea').innerHTML,/1 lesson-day remaining/);
  assert.match(r.node('printArea').innerHTML,/Primary source project/);
});

test('a two-day pin on Nov 23 skips a fully pinned Nov 24 and continues on Nov 25 across actual display and exports',async()=>{
  const r=fixture({pins:{[id]:'2026-11-23','l1-activity':'2026-11-24'},
    selected:{[id]:true,'l1-activity':true},order:[id,'l1-activity']});
  const m=r.api.model();
  assert.equal(slot(m,'2026-11-23').entries[0].key,id);
  assert.equal(slot(m,'2026-11-24').entries[0].key,'l1-activity');
  assert.equal(slot(m,'2026-11-24').continuations.length,0);
  assert.equal(slot(m,'2026-11-25').continuations[0].key,id);
  for (const b of m.buckets) assert.equal(b.load,1);
  assert.equal(m.overflow.length,0);
  assert.match(r.node('schedule').innerHTML,/Nov 25[\s\S]*Primary source project \(continued\)/);
  r.event('week','click');
  assert.match(r.node('weekview').innerHTML,/Nov 25[\s\S]*Primary source project \(continued\)/);
  r.event('print-week','click');
  assert.match(r.node('printArea').innerHTML,/Nov 25[\s\S]*Primary source project \(continued\)/);
  r.event('print-sub','click');
  assert.match(r.node('printArea').innerHTML,/Nov 25[\s\S]*Primary source project \(continued\)/);
  r.event('export-ics','click');
  const {downloaded,exportBlob}=r.exportFile();
  assert.match(downloaded,/\.ics$/);
  const ics=await exportBlob.text();
  assert.match(ics,/DTSTART;VALUE=DATE:20261125\r\n[\s\S]*SUMMARY:[^\r]+Primary source project \(continued\)/);
});

test('no class, substitute and unnamed year holiday reflow; unavailable assessments do not export',async()=>{
  const r=fixture({end:'2026-11-28',pins:{[id]:'2026-11-23'},dayTypes:{'2026-11-23':'No class'},
    subDays:{'2026-11-25':'Read alternate text'},view:'week'},
    {year:{daysOff:[{from:'2026-11-26',to:'2026-11-26',label:''}]}});
  const m=r.api.model();
  assert.equal(slot(m,'2026-11-23'),undefined);
  assert.equal(slot(m,'2026-11-25'),undefined);
  assert.equal(slot(m,'2026-11-26'),undefined);
  assert.equal(slot(m,'2026-11-24').entries[0].key,id);
  assert.equal(slot(m,'2026-11-27').continuations[0].key,id);
  assert.match(r.node('weekview').innerHTML,/original pin: Mon, Nov 23/);
  assert.match(r.node('weekview').innerHTML,/selected test date is a weekend/);
  assert.doesNotMatch(r.node('weekview').innerHTML,/testday/);
  r.event('export-ics','click');
  assert.doesNotMatch(await r.exportFile().exportBlob.text(),/Unit test|DTSTART;VALUE=DATE:20261128\r\n/);
  r.event('test','change','2026-11-30');
  assert.match(r.node('weekview').innerHTML,/testday/);
  const a=fixture({end:'2026-11-24',rotation:'ab'});
  assert.match(a.api.dates().testIssue,/does not meet/);
  const huge=fixture({end:'2200-01-01'});
  assert.match(huge.api.dates().rangeIssue,/366 days/);
  assert.equal(huge.api.model().buckets.length,0);
});

test('split/unsplit keeps position, moving pins a real date, reset only affects active section, maps are independent',()=>{
  const r=fixture({pins:{'l1-activity':'2026-11-24'},order:['l1-activity','l2-activity'],selected:{'l1-activity':true,'l2-activity':true},
    end:'2026-11-27',extraSections:[{name:'Other',start:'2026-11-23',test:'2026-11-27',pins:{'l1-activity':'2026-11-25'}}]});
  const s=r.api.state();
  r.api.split('l1-activity');
  assert.equal(s.order.join('|'),'l1-activity#a|l1-activity#b|l2-activity');
  r.api.split('l1-activity');
  assert.equal(s.order.join('|'),'l1-activity|l2-activity');
  assert.equal(s.sections[0].pins['l1-activity'],'2026-11-24');
  r.api.move('l2-activity','2026-11-26');
  assert.equal(r.api.model().placedOn['l2-activity'],'2026-11-26');
  assert.equal(s.sections[0].pins['l2-activity'],'2026-11-26');
  r.event('reset-pins','click');
  assert.equal(Object.keys(s.sections[0].pins).length,0);
  assert.equal(s.sections[1].pins['l1-activity'],'2026-11-25');
  const next=r.api.cloneSection('Clone',s.sections[1]);
  next.dayTypes['2026-11-24']='No class';
  next.pins['l1-activity']='2026-11-24';
  assert.equal(s.sections[1].dayTypes['2026-11-24'],undefined);
  assert.equal(s.sections[1].pins['l1-activity'],'2026-11-25');
});

test('portable export/import round trip keeps incoming dates; malformed, wrong-unit and declined imports leave originals',async()=>{
  const original=fixture({start:'2026-11-23',end:'2026-11-30',pins:{[id]:'2026-11-23'},homework:{'2026-11-24':'Read paragraph two'}});
  original.event('export-plan','click');
  const exported=await original.exportFile().exportBlob.text();
  const maybe=fixture({start:'2027-01-04',end:'2027-01-14'});
  const old=maybe.storage[regularKey];
  function importText(r,text) { r.node('import-plan').files=[{text,size:text.length}];r.event('import-plan','change'); }
  importText(maybe,'not JSON');
  importText(maybe,JSON.stringify({unit:'ga',selected:{},sections:[{start:'2026-11-23',test:'2026-11-30'}]}));
  importText(maybe,JSON.stringify({unit:'pe',selected:{},sections:[{start:'2026-02-31',test:'2026-03-01'}]}));
  assert.equal(maybe.storage[regularKey],old);
  assert.ok(maybe.notices.every(m=>/did not contain/.test(m)));
  importText(maybe,exported);
  assert.equal(maybe.node('start').value,'2026-11-23');
  assert.equal(maybe.node('test').value,'2026-11-30');
  assert.equal(maybe.api.state().sections[0].homework['2026-11-24'],'Read paragraph two');
  const declined=fixture({}, {confirm:false});
  const before=declined.storage[regularKey];
  importText(declined,exported);
  assert.equal(declined.storage[regularKey],before);
  const damaged=setup('',{storage:{[regularKey]:'{damaged'}});
  assert.equal(damaged.storage[regularKey],'{damaged');
  assert.match(damaged.node('save-note').textContent,/not been overwritten/);
  const hash='#plan='+Buffer.from(exported).toString('base64');
  const canceled=setup('',{hash,confirm:false});
  assert.match(canceled.node('sections').innerHTML,/Original Regular Class/);
  const accepted=setup('',{hash});
  assert.equal(accepted.node('start').value,'2026-11-23');
  assert.equal(accepted.hrefReplaced(),'/planner.html');
});

test('256 deterministic capacity, split, pin and date combinations account for every lesson-day',()=>{
  const start='2026-11-23';
  for (let i=0;i<256;i++) {
    const picks={[id]:true,'l1-activity':true,'l2-activity':true,'l3-reading':true};
    const isSplit=!!(i&4);
    const order=[...(isSplit?[id+'#a',id+'#b']:[id]),'l1-activity','l2-activity','l3-reading'];
    const splitMap=isSplit?{[id]:true}:{};
    const reqPins={};
    if(i&8)reqPins[order[0]]='2026-11-23';
    if(i&16)reqPins['l1-activity']='2026-11-24';
    if(i&32)reqPins['l2-activity']='2026-11-24';
    const r=fixture({ start, end:(i&1)?'2026-12-02':'2026-11-26',period:(i&2)?90:45,
      rotation:(i&64)?'ab':'daily',pins:reqPins,dayTypes:(i&128)?{'2026-11-23':'Assembly'}:{},splits:splitMap,selected:picks,order });
    const m=r.api.model(); const cap=(i&2)?2:1;
    const unplaced=m.overflow.reduce((v,o)=>v+o.remainingDays,0);
    const placed=m.buckets.reduce((v,b)=>v+b.load,0);
    assert.equal(placed+unplaced,5,'duration unaccounted for in case '+i);
    for(const b of m.buckets) assert.ok(b.load<=cap,'overfilled '+b.iso+' in case '+i);
    for (const [key,date] of Object.entries(reqPins)) {
      const actual=m.placedOn[key];
      if (!actual) assert.ok(m.overflow.some(o=>o.key===key));
      else if(actual!==date) assert.equal(slot(m,actual).entries.find(e=>e.key===key).pinMovedFrom,date);
      assert.equal(r.api.state().sections[0].pins[key],date);
    }
  }
});
