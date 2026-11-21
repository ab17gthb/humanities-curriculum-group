const { test } = require('node:test');
const a = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const base = process.env.HCG_BASELINE_JS;
const source = fs.readFileSync(base || path.join(__dirname, '../public/year-planner.js'),'utf8');
const registry = fs.readFileSync(process.env.HCG_PLANNER_DATA || path.join(__dirname, '../public/planner-data.js'),'utf8');
const teacherHome = fs.readFileSync(path.join(__dirname, '../public/teacher-home.js'),'utf8');

function boot(storage = {}, hash = '') {
  const local = new Map(Object.entries(storage).map(([k,v]) => [k, JSON.stringify(v)]));
  const elements = new Map(), exports = [], confirmations = [];
  function element() {
    return {
      value: '', textContent: '', innerHTML: '', style:{}, listeners:{}, validity:'',
      addEventListener(event, f) { this.listeners[event] = f; },
      querySelectorAll() { return []; },
      setCustomValidity(message) { this.validity = message; },
      reportValidity() { return !this.validity; },
      click() { if (this.listeners.click) this.listeners.click.call(this); }
    };
  }
  const e = id => {
    if (!elements.has(id)) elements.set(id, element());
    return elements.get(id);
  };
  let blob;
  const window = {
    addEventListener() {},
    confirm(message) { confirmations.push(message); return true; },
  };
  const location = {hash, pathname:'/planner-year.html', search:'', origin:'https://example.test'};
  const history = {replaceState(){ location.hash=''; }};
  const doc = {
    getElementById:e,
    addEventListener() {},
    createElement() {return {click(){exports.push({name:this.download, blob});}};}
  };
  class FileReader {
    readAsText(f) { this.result=f.body; this.onload(); }
  }
  const ctx = vm.createContext({window, location, history, document:doc, navigator:{}, FileReader, Blob,
    localStorage:{getItem:k=>local.get(k)||null, setItem:(k,v)=>local.set(k,v)},
    atob, btoa, setTimeout(){}, URL: class extends URL { static createObjectURL(b){blob=b;return 'blob:dummy';} static revokeObjectURL(){} }});
  vm.runInContext(registry,ctx);
  vm.runInContext(fs.readFileSync(require("node:path").join(__dirname, "../public/unit-scheduler.js"), "utf8"), ctx);
  // Expose only a test probe without changing runtime access or shipping debug hooks.
  vm.runInContext(source.replace(/\n}\)\(\);\s*$/, `
    window.__yearTest = {
      assign, instructionalDays, meetingDays, activeUnits, unitDays, computeFit,
      state: function() { return S; }
    };
  })();`),ctx);
  vm.runInContext(teacherHome,ctx);
  return {e, exports, confirmations, location, p:window.__yearTest, home:window.HCGTeacherHome,
    saved:(k='hcg_year_v1')=>JSON.parse(local.get(k)),
    importFile(value, size=200) { e('import').files=[{body:typeof value==='string'?value:JSON.stringify(value),size}]; e('import').listeners.change.call(e('import')); },
    change(id,value) { e(id).value=value; e(id).listeners.change.call(e(id)); }
  };
}
const basePlan = (plus={}) => Object.assign({
  start:'2026-11-02', end:'2026-11-30', exam:'', course:'early', openingUnit:'',
  daysOff:[], periods:[], reviewDays:0, schedule:{period:45,pattern:'daily'}, unitDays:{}, pinnedStarts:{}
},plus);
const YEAR='hcg_year_v1', LIB='hcg_year_plans_v1';
const copy=x=>JSON.parse(JSON.stringify(x));
const hash=p=>'#plan='+Buffer.from(JSON.stringify(p)).toString('base64url');
test('calendar is weekday-only, handles DST, de-duplicates closed spans, then rotates',()=>{
  const subject=boot({[YEAR]:basePlan({start:'2026-03-05',end:'2026-03-12',schedule:{period:90,pattern:'ab'},
    daysOff:[{from:'2026-03-06',to:'2026-03-09',label:'Spring recess',kind:'break'},{from:'2026-03-09',to:'2026-03-10',label:'Closure',kind:'school'}]})});
  const days=subject.p.instructionalDays();
  a.deepEqual(copy(days),['2026-03-05','2026-03-11','2026-03-12']);
  a.deepEqual(copy(subject.p.meetingDays(days)),['2026-03-05','2026-03-12']);
});
test('term counts reconcile and the modern plan prepends exactly one early unit',()=>{
  const subject=boot({[YEAR]:basePlan({course:'modern',openingUnit:'u6',periods:[{name:'A',end:'2026-11-12'},{name:'B',end:'2026-11-24'}]})});
  const ids=subject.p.activeUnits().map(u=>u.id);
  a.equal(ids[0],'u6'); a.equal(ids[1],'u7'); a.equal(ids.at(-1),'u17');
  a.equal(ids.filter(x=>x==='u6').length,1);
  const counts=[...subject.e('period-summary').innerHTML.matchAll(/>(\d+) days<\/td>/g)].map(m=>Number(m[1]));
  a.equal(counts.reduce((sum,n)=>sum+n,0),subject.p.instructionalDays().length);
  subject.change('y-course','early');
  a.equal(subject.p.activeUnits().map(u=>u.id).at(-1),'u16');
  subject.change('y-course','modern');
  a.equal(subject.p.activeUnits()[0].id,'u6');
});
test('year date validation rejects reversed date/range without rewriting saved plan',()=>{
  const subject=boot({[YEAR]:basePlan()});
  const before=subject.saved();
  subject.change('y-end','2026-10-29');
  a.deepEqual(subject.saved(),before);
  a.match(subject.e('y-end').validity,/before/);
  subject.change('y-end','2026-12-10');
  a.equal(subject.saved().end,'2026-12-10');
  a.equal(subject.e('y-end').validity,'');
});
test('imports normalize legacy records and reject invalid records before saving',()=>{
  const subject=boot({[YEAR]:basePlan()});
  const old=subject.saved();
  for (const bad of ['{bad', {}, {...old,end:'2026-11-01'}, {...old,end:'9999-11-01'},
    {...old,start:'2026-02-29'}, {...old,periods:[null]}, {...old,daysOff:[{}]},
    {...old,unitDays:{u1:'8'}}, {...old,pinnedStarts:{u1:'2026-13-01'}}, {...old,reviewDays:-1}]) {
    subject.importFile(bad);
    a.deepEqual(subject.saved(),old);
    a.match(subject.e('import-note').textContent,/not changed/);
  }
  subject.importFile(old,1_000_000);
  a.match(subject.e('import-note').textContent,/large/);
  subject.importFile({start:'2028-02-29',end:'2028-03-31'});
  a.equal(subject.saved().start,'2028-02-29');
  a.deepEqual(subject.saved().periods,[]);
  a.deepEqual(subject.saved().daysOff,[]);
});
test('opening another shared plan preserves both older named plans and earlier share',()=>{
  const subject=boot({[LIB]:{active:'Shared plan',plans:{'My year plan':basePlan(),'Shared plan':basePlan({course:'modern'})}}},
    hash(basePlan({course:'full'})));
  a.equal(subject.saved(LIB).active,'Shared plan 2');
  a.equal(subject.saved(LIB).plans['Shared plan'].course,'modern');
  a.equal(subject.saved(LIB).plans['Shared plan 2'].course,'full');
  a.equal(subject.location.hash,'');
});
test('invalid shared data does not displace existing active plan',()=>{
  const subject=boot({[LIB]:{active:'Earlier plan',plans:{'Earlier plan':basePlan()}}},hash(basePlan({daysOff:'invalid'})));
  a.equal(subject.saved(LIB).active,'Earlier plan');
  a.match(subject.e('import-note').textContent,/not changed/);
});
test('pin gaps and blocked pins are deterministic',()=>{
  const subject=boot({[YEAR]:basePlan({unitDays:{u1:3,u2:3},pinnedStarts:{u1:'2026-11-07',u2:'2026-11-09'}})});
  const A=subject.p.assign(subject.p.instructionalDays());
  a.equal(A.ranges.u1[0],'2026-11-09'); // Weekend pin advances.
  a.equal(A.ranges.u2[0],'2026-11-12');
  a.equal(A.pinStale.u2,true);
  a.equal(A.unassigned[0],'2026-11-02');
});
test('fit and calendar agree when separate odd block units need more meetings than the aggregate',()=>{
  const units={u1:1,u2:1,u3:1,u4:1,u5:1,u6:1,u16:1};
  const subject=boot({[YEAR]:basePlan({end:'2026-11-06',schedule:{period:90,pattern:'daily'},unitDays:units})});
  const p=subject.p, A=p.assign(p.instructionalDays()), F=p.computeFit();
  a.equal(A.overflowDays,2);
  a.equal(F.fits,false);
  a.equal(F.stillOver,2);
  subject.e('fit-year').click();
  a.doesNotMatch(subject.e('fit-preview').innerHTML,/Everything fits/);
  a.match(subject.e('fit-preview').innerHTML,/2 lesson-days unscheduled/);
});
test('fit previews and applies a usable trim without crossing registry core floors',()=>{
  const subject=boot({[YEAR]:basePlan({start:'2026-11-02',end:'2026-11-20',unitDays:{u1:60,u2:1,u3:1,u4:1,u5:1,u6:1,u16:1}})});
  const p=subject.p, F=p.computeFit();
  a.equal(F.fits,false);
  const row=F.rows.find(r=>r.u.id==='u1');
  a.ok(row.next<60);
  a.ok(row.next>=row.floor);
  a.equal(subject.saved().unitDays.u1,60);
  subject.e('fit-year').click();
  subject.e('fit-apply').click();
  a.equal(subject.saved().unitDays.u1,row.next);
  a.equal(p.assign(p.instructionalDays()).overflowDays,F.stillOver);
});
test('exported JSON round-trips settings, and partial calendar units get no fabricated test', async()=>{
  const subject=boot({[YEAR]:basePlan({end:'2026-11-04',unitDays:{u1:2,u2:5},pinnedStarts:{u1:'2026-11-02'}})});
  subject.e('export').click();
  const json=await subject.exports[0].blob.text();
  const second=boot();
  second.importFile(json);
  a.deepEqual(second.saved(),subject.saved());
  subject.e('ics-year').click();
  const ics=await subject.exports[1].blob.text();
  a.match(ics,/hcg-year-u1-test/);
  a.match(ics,/hcg-year-u2-start/);
  a.doesNotMatch(ics,/hcg-year-u2-test/);
  a.match(subject.confirmations.at(-1),/Only the start is exported for: The Founding/);
});
test('assignment maintains an exact partition across mixed year settings',()=>{
  let state=98231;
  const rnd = n => { state=(state*1664525+1013904223)>>>0; return state%n; };
  // Number of fixtures is fixed; no clock or network influences the generated plans.
  for(let i=0;i<30;i++){
    const chosen=basePlan({course:['early','full','modern'][rnd(3)],openingUnit:'u4',
      end:'2027-01-15', exam:'2026-12-18', reviewDays:rnd(11),
      schedule:{period:rnd(2)?90:45,pattern:rnd(3)?'ab':'daily'},
      pinnedStarts:{u2:'2026-11-16',pe:'2026-12-26'},unitDays:{u1:rnd(20)+1,u2:rnd(15)+1}});
    const env=boot({[YEAR]:chosen});
    const p=env.p, days=p.instructionalDays(), A=p.assign(days);
    const meets=p.meetingDays(days);
    const used=Object.values(A.ranges).flat();
    const held=meets.filter(day=>A.reserved[day]);
    const partition=[...used,...held,...A.unassigned].sort();
    a.deepEqual(copy(partition),copy(meets));
    a.equal(new Set(used).size,used.length);
    a.deepEqual(copy(used),copy(used).sort());
  }
});

test('My Day agrees with Year on the modern opener and suppresses a partial test',()=>{
  const subject=boot({[YEAR]:basePlan({end:'2026-11-04',course:'modern',openingUnit:'u6',unitDays:{u6:2,u7:5}})});
  a.match(subject.home.weekCell('2026-11-02'),/Reconstruction/);
  a.match(subject.home.weekCell('2026-11-03'),/Reconstruction.*Unit test/);
  a.match(subject.home.weekCell('2026-11-04'),/Gilded Age/);
  a.doesNotMatch(subject.home.weekCell('2026-11-04'),/Unit test/);
});
test('My Day evaluates overlapping and broad closures inside the displayed year',()=>{
  const subject=boot({[YEAR]:basePlan({end:'2026-11-04',
    daysOff:[{from:'2026-11-03',to:'2026-11-03',label:'Specified first',kind:'pd'},
      {from:'1500-01-01',to:'9999-12-30',label:'Broad closure',kind:'holiday'}]})});
  a.equal(subject.p.instructionalDays().length,0);
  a.equal(subject.home.weekCell('2026-11-03'),'No school: Specified first');
  a.equal(subject.home.weekCell('2026-11-02'),'No school: Broad closure');
  a.equal(subject.home.weekCell('2026-11-05'),'Nothing planned for this date');
});

const unitFixture = (over = {}) => ({
  selected:{custom_a:true,custom_b:true}, order:['custom_a','custom_b'], splits:{}, active:0,
  customItems:[{id:'custom_a',title:'Two-day lesson',days:2,kind:'own'},
    {id:'custom_b',title:'Pinned lesson',days:1,kind:'own'}],
  sections:[{start:'2026-11-23',test:'2026-11-27',period:45,rotation:'daily',
    pins:{custom_a:'2026-11-23',custom_b:'2026-11-24'},dayTypes:{},subDays:{},homework:{}, ...over}]
});
test('My Day lists the long continuation on the first later meeting with capacity, not on another pinned start',()=>{
  const subject=boot({[YEAR]:basePlan(),'hcg_unit_v1':unitFixture()});
  a.match(subject.home.weekCell('2026-11-23'),/Two-day lesson/);
  a.match(subject.home.weekCell('2026-11-24'),/Pinned lesson/);
  a.doesNotMatch(subject.home.weekCell('2026-11-24'),/continu/);
  a.match(subject.home.weekCell('2026-11-25'),/Two-day lesson \(continued\)/);
  a.match(subject.home.dayHTML('2026-11-25','Wednesday'),/Two-day lesson \(continued\)/);
});
test('My Day shifts conflicting pins and stays off unavailable or blocked test dates',()=>{
  const subject=boot({[YEAR]:basePlan(),'hcg_unit_v1':unitFixture({
    pins:{custom_a:'2026-11-23',custom_b:'2026-11-23'},
    subDays:{'2026-11-24':'Independent work','2026-11-27':''}})});
  a.match(subject.home.weekCell('2026-11-23'),/Two-day lesson/);
  a.doesNotMatch(subject.home.weekCell('2026-11-23'),/Pinned lesson/);
  a.match(subject.home.weekCell('2026-11-24'),/Sub day/);
  a.match(subject.home.weekCell('2026-11-25'),/Pinned lesson/);
  a.match(subject.home.weekCell('2026-11-26'),/continued/);
  a.doesNotMatch(subject.home.weekCell('2026-11-27'),/Unit test/);
});
test('My Day renders resource names without unsafe hyperlinks',()=>{
  const unit=unitFixture();
  unit.customItems[0].link='javascript:alert(1)';
  unit.customItems[1].link='https://example.org/lesson?a=1&b=2';
  const subject=boot({[YEAR]:basePlan(),'hcg_unit_v1':unit});
  a.match(subject.home.dayHTML('2026-11-23','Monday'),/Two-day lesson/);
  a.doesNotMatch(subject.home.dayHTML('2026-11-23','Monday'),/javascript:/);
  a.match(subject.home.dayHTML('2026-11-24','Tuesday'),/https:\/\/example\.org\/lesson\?a=1&amp;b=2/);
});
