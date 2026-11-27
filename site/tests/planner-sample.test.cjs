const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const vm=require('node:vm');
const root=require('node:path').resolve(__dirname,'../public')+'/';
const code=fs.readFileSync(root+'planner.js','utf8');
const data=fs.readFileSync(process.env.HCG_PLANNER_DATA || root+'planner-data.js','utf8');
const html=fs.readFileSync(root+'planner.html','utf8');
const bootstrap=html.match(/<script>\s*\/\/ Do not even initialize[\s\S]*?<\/script>/)[0].slice(8,-9);
const sample='?sample=progressive-era-week';
const samplePrefix='hcg_sample_progressive_week_v1:';
const regularKey='hcg_unit_v1';
const yearKey='hcg_year_v1';
const stale='-another-draft-1234';
const uuid='b9265234-4732-4bd6-8e0a-161366ab74f1';
const seed={
  [regularKey]:JSON.stringify({selected:{'l3-reading':true},sections:[{name:'Original Regular Class',start:'2026-11-30',test:'2026-12-09'}]}),
  [yearKey]:JSON.stringify({daysOff:[{from:'2026-11-30',to:'2026-11-30',label:'Year plan closure'}]}),
  [samplePrefix+stale]:'preserve unrelated copy'
};
function setup(search, { storage={...seed}, hash='', failWrites=false, failReads=false }={}) {
  const log=[], requests=[], eventHandlers={}, elements={};
  let href;
  function node(id) {
    return elements[id] ||= {
      id, innerHTML:'', textContent:'', value:'', style:{}, hidden:false, dataset:{}, classList:{add(){},toggle(){}},
      querySelectorAll(){return [];}, className:'',
      parentNode:{insertBefore(child,before){ this.lastInsert=[child.id,before.id]; }},
      addEventListener(t,fn){eventHandlers[id+':'+t]=fn;},
      getAttribute(key){return this.dataset[key] || null;},
      scrollIntoView(){},
    };
  }
  node('list').dataset['data-view']='list'; node('week').dataset['data-view']='week';
  const document={
    getElementById:node,
    querySelectorAll(selector){return selector==='[data-view]'?[node('list'),node('week')]:[];},
    documentElement:node('html'),
    createElement(){return {};},
    head:{appendChild(el){ requests.push([el.src,el.async]); }},
  };
  const localStorage={
    getItem(key){log.push(['get',key]); if(failReads)throw Error('blocked'); return storage[key] ?? null;},
    setItem(key,val){log.push(['set',key]); if(failWrites)throw Error('quota'); storage[key]=val;},
  };
  const window={ addEventListener(){},print(){} };
  const context=vm.createContext({window,document,localStorage,URLSearchParams,crypto:{randomUUID(){return uuid;}},
    location:{search,hash,pathname:'/planner.html',assign(route){href=route;}},
    atob, escape, history:{replaceState(){throw Error('did not expect a share to load');}}
  });
  vm.runInContext(data,context);
  vm.runInContext(fs.readFileSync(require("node:path").join(__dirname, "../public/unit-scheduler.js"), "utf8"), context);
  vm.runInContext(code,context);
  vm.runInContext(bootstrap,context);
  return {node,log,requests,storage,href:()=>href, event(id,type,value){
    if(value!==undefined)node(id).value=value;
    eventHandlers[id+':'+type].call(node(id),{preventDefault(){}});
  }};
}
const count=(html,token)=>html.split(token).length-1;
test('demo is five actual planner meetings, ignores regular/year/share data, and adjusts coverage/date without any storage or auth access',()=>{
  const hash='#plan='+Buffer.from(JSON.stringify({unit:'ga',selected:{},start:'2020-01-01'})).toString('base64');
  const run=setup(sample+'&unit=ga',{hash});
  assert.equal(run.node('planner-heading').textContent,'Try the Progressive Era sample week');
  assert.equal(run.node('start').value,'2026-11-30');
  assert.equal(count(run.node('weekview').innerHTML,'data-dropday='),5);
  assert.match(run.node('weekview').innerHTML,/Dec 4[\s\S]+Reforming Government/);
  assert.doesNotMatch(run.node('weekview').innerHTML,/Unit test|Year plan closure/);
  assert.match(run.node('covtext').textContent,/6 of 15/);
  run.event('sample-swap','change','l3-activity');
  assert.match(run.node('weekview').innerHTML,/Dec 4[\s\S]+Ballot simulation/);
  assert.match(run.node('covtext').textContent,/4 of 15/);
  run.event('start','change','2026-12-08');
  assert.equal(count(run.node('weekview').innerHTML,'data-dropday='),5);
  assert.match(run.node('weekview').innerHTML,/Dec 14[\s\S]+Ballot simulation/);
  run.event('list','click');
  assert.equal(count(run.node('schedule').innerHTML,'data-dropday='),5);
  run.event('print-week','click');
  assert.match(run.node('printArea').innerHTML,/Dec 14[\s\S]+Ballot simulation/);
  assert.doesNotMatch(run.node('printArea').innerHTML,/Unit test/);
  assert.deepEqual(run.log,[]);
  assert.deepEqual(run.requests,[]);
});
test('explicit save creates a fresh device-only copy that survives reload; normal and other saved copies are untouched',()=>{
  const run=setup(sample);
  run.event('start','change','2026-12-10');
  run.event('sample-swap','change','l3-activity');
  run.event('sample-copy','click');
  assert.match(run.href(),new RegExp('draft='+uuid+'$'));
  assert.ok(run.log.every(([,key])=>key===samplePrefix+uuid));
  const draft=setup(sample+'&draft='+uuid,{storage:run.storage});
  assert.equal(draft.node('planner-heading').textContent,'Your Progressive Era sample copy');
  assert.equal(draft.node('start').value,'2026-12-10');
  assert.equal(draft.node('sample-swap').value,'l3-activity');
  assert.ok(draft.node('sample-copy').hidden);
  draft.event('sample-swap','change','l3-reading');
  assert.ok(draft.log.every(([,key])=>key===samplePrefix+uuid));
  assert.deepEqual(draft.requests,[]);
  assert.equal(setup(sample+'&draft='+uuid,{storage:run.storage}).node('sample-swap').value,'l3-reading');
  for (const [k,v] of Object.entries(seed)) assert.equal(run.storage[k],v);
});
test('wrong, absent, or blocked copy is never written implicitly; failed explicit save leaves edited page open',()=>{
  const missing=setup(sample+'&draft='+uuid);
  assert.equal(missing.node('planner-heading').textContent,'Try the Progressive Era sample week');
  assert.deepEqual(missing.log,[['get',samplePrefix+uuid]]);
  const invalid=setup(sample+'&draft='+regularKey);
  assert.deepEqual(invalid.log,[]);
  const blocked=setup(sample,{failWrites:true});
  blocked.event('sample-swap','change','l3-activity');
  blocked.event('sample-copy','click');
  assert.equal(blocked.href(),undefined);
  assert.match(blocked.node('sample-copy-status').textContent,/couldn’t save/);
  assert.equal(blocked.node('sample-swap').value,'l3-activity');
  assert.equal(blocked.storage[regularKey],seed[regularKey]);
});
test('regular planner still restores unit and year data and loads integrations in order',()=>{
  const regular=setup('');
  assert.match(regular.node('sections').innerHTML,/Original Regular Class/);
  assert.equal(regular.node('start').value,'2026-11-30');
  assert.doesNotMatch(regular.node('schedule').innerHTML,/data-dropday='2026-11-30'/);
  assert.match(regular.node('schedule').innerHTML,/Unit test/);
  assert.deepEqual(regular.requests,[['firebase-config.js',false],['auth.js',false],['stats.js',false]]);
  assert.ok(regular.log.some(([op,k])=>op==='get'&&k===regularKey));
  assert.ok(regular.log.some(([op,k])=>op==='get'&&k===yearKey));
  assert.ok(regular.log.every(([,k])=>!k.startsWith(samplePrefix)));
});
