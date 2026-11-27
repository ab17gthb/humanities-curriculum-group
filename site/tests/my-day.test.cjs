const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const publicDir = path.join(__dirname, '../public');
const source = name => fs.readFileSync(path.join(publicDir, name), 'utf8');
function fixture(values = {}, paid = false) {
  const reads = [], minted = [], events = {}, domEvents = {};
  const status = {textContent: ''};
  const window = {
    addEventListener: (type, event) => { events[type] = event; },
    HCGAuth: {entitlement: () => ({paid})},
    HCGFiles: {url: async name => { minted.push(name); return 'https://example.test/download'; }},
    location: {href: '/home.html'},
  };
  const document = {
    addEventListener: (type, action) => { domEvents[type] = action; },
    getElementById: id => id === 'home-download-status' ? status : null,
  };
  const localStorage = {
    getItem(key) { reads.push(key); return values[key] ? JSON.stringify(values[key]) : null; },
    setItem() { assert.fail('My Day must not write plans'); }
  };
  const context = vm.createContext({window, document, localStorage, URL});
  ['planner-data.js', 'unit-scheduler.js', 'teacher-home.js'].forEach(name => vm.runInContext(source(name), context));
  return {window, status, minted, reads, plans: values, events, domEvents};
}
const unit = (start, test, picked, extras = {}) => ({
  selected: {[picked]: true}, order: [picked], sections: [{name:'Period 2', start, test, ...extras}]
});

test('empty state does not read an isolated sample and links to the sample in the page', () => {
  const f = fixture({'hcg_sample_progressive_week_v1:private-sample': unit('2026-11-23','2026-11-27','l1-reading')});
  assert.equal(f.window.HCGTeacherHome.hasData, false);
  assert(!f.reads.some(k => k.startsWith('hcg_sample')));
  assert.match(source('home.html'), /id="home-pitch"[\s\S]*?planner\.html\?sample=progressive-era-week/);
  assert.match(source('home.html'), /scope='row'/);
});

test('next dated lesson and assessment derive independently from active saved sections; public files remain public', () => {
  const pe = unit('2026-11-23', '2026-11-27', 'l1-reading');
  pe.active = 1;
  pe.sections.push({name: 'Period 4', start: '2026-11-25', test: '2026-11-30'});
  const f = fixture({'hcg_unit_v1': pe});
  const next = f.window.HCGTeacherHome.upcomingHTML('2026-11-21');
  assert.match(next.lesson, /2026-11-25/);
  assert.match(next.lesson, /Period 4/);
  assert.match(next.lesson, /The Problems Progressives Faced/);
  assert.match(next.lesson, /href='files\/lesson-01-reading.pdf'/);
  assert.match(next.assessment, /2026-11-30/);
  assert.match(next.assessment, /href='files\/unit-test.pdf'/);
});

test('paid materials are clearly labeled without publishing a storage path; an entitled click mints the saved exact path', async () => {
  const blank = fixture();
  const ga = blank.window.HCG_UNITS.ga;
  const first = ga.items.find(i => i.storage && i.days === 1);
  const plans = {'hcg_unit_ga_v1': unit('2026-11-23', '2026-11-27', first.id)};
  const unpaid = fixture(plans);
  const next = unpaid.window.HCGTeacherHome.upcomingHTML('2026-11-21');
  assert.match(next.lesson, /All-Access/);
  assert.match(next.assessment, /All-Access/);
  assert.doesNotMatch(next.lesson + next.assessment, /data-storage|hcg\/gilded-age\//);
  const entitled = fixture(plans, true);
  const allowed = entitled.window.HCGTeacherHome.upcomingHTML('2026-11-21');
  assert(allowed.lesson.includes("data-storage='" + first.storage + "'"));
  assert(allowed.assessment.includes("data-storage='" + ga.testStorage + "'"));
  assert.equal(entitled.minted.length, 0);
  const button = {disabled:false, textContent:ga.testName, getAttribute: () => ga.testStorage};
  entitled.domEvents.click({preventDefault(){}, target:{closest: () => button}});
  await new Promise(setImmediate);
  assert.deepEqual(entitled.minted,[ga.testStorage]);
  assert.equal(button.disabled,false);
  assert.equal(entitled.window.location.href,'https://example.test/download');
});

test('simultaneous assessment and another unit lesson both survive; unavailable test is not shown', () => {
  const blank = fixture();
  const ga = blank.window.HCG_UNITS.ga;
  const first = ga.items.find(i => i.storage && i.days === 1);
  const plans = {'hcg_unit_v1': unit('2026-11-23', '2026-11-25', 'l1-reading'),
    'hcg_unit_ga_v1': unit('2026-11-25', '2026-11-28', first.id)};
  const f = fixture(plans), th = f.window.HCGTeacherHome;
  const html = th.dayHTML('2026-11-25','Today');
  assert.match(html,/Unit assessment/);
  assert.match(html,/Progressive Era/);
  assert.match(html,/Gilded Age/);
  assert.match(th.weekCell('2026-11-25'),/Assessment[\s\S]+Gilded Age/);
  assert.doesNotMatch(th.upcomingHTML('2026-11-26').assessment,/November 28/);
});

test('year-only schedule labels projected dates; a different tab’s new local plan refreshes without reload', () => {
  const f = fixture({'hcg_year_v1':{start:'2026-11-23',end:'2026-12-11',course:'early',unitDays:{u1:5},daysOff:[]}});
  let next = f.window.HCGTeacherHome.upcomingHTML('2026-11-22');
  assert.match(next.lesson,/Year Planner only/);
  assert.match(next.lesson,/planner\.html\?unit=ca/);
  assert.match(next.assessment,/Projected by the Year Planner/);
  let reRendered = 0;
  f.window.HCGHomeRender = () => { reRendered++; };
  f.plans.hcg_unit_v1 = unit('2026-11-25', '2026-11-27', 'l1-reading');
  f.events.storage({key:'hcg_unit_v1'});
  assert.equal(reRendered, 1);
  next = f.window.HCGTeacherHome.upcomingHTML('2026-11-25');
  assert.match(next.lesson,/The Problems Progressives Faced/);
  assert.match(next.assessment,/2026-11-27.*Progressive Era/);
  f.events.storage({key:'hcg_sample_progressive_week_v1:isolated'});
  assert.equal(reRendered, 1);
});

test('earlier year projections are not hidden by a later detailed plan for a different unit', () => {
  const f = fixture({
    hcg_year_v1: {start:'2026-11-23', end:'2026-11-25', course:'early', unitDays:{u1:3}, daysOff:[]},
    hcg_unit_v1: unit('2026-12-07', '2026-12-10', 'l1-reading')
  });
  const next = f.window.HCGTeacherHome.upcomingHTML('2026-11-23');
  assert.match(next.lesson, /2026-11-23.*Colonial America.*Year Planner only/);
  assert.match(next.assessment, /2026-11-25.*Colonial America.*Projected by the Year Planner/);
});

test('cards pick dates independently and prefer detailed materials and assessment on ties', () => {
  const f = fixture({
    hcg_year_v1: {start:'2026-11-23', end:'2026-11-25', course:'early', unitDays:{u1:3}, daysOff:[]},
    hcg_unit_v1: unit('2026-11-24', '2026-11-25', 'l1-reading')
  });
  let next = f.window.HCGTeacherHome.upcomingHTML('2026-11-23');
  assert.match(next.lesson, /2026-11-23.*Colonial America/);
  assert.match(next.assessment, /2026-11-25.*Progressive Era.*files\/unit-test.pdf/);
  next = f.window.HCGTeacherHome.upcomingHTML('2026-11-24');
  assert.match(next.lesson, /2026-11-24.*Progressive Era.*files\/lesson-01-reading.pdf/);
  assert.doesNotMatch(next.lesson + next.assessment, /Colonial America|Projected/);
});

test('a detailed plan replaces earlier Year Planner estimates for that same unit', () => {
  const ca = fixture().window.HCG_UNITS.ca;
  const pick = ca.items.find(i => i.storage && i.days === 1);
  const f = fixture({
    hcg_year_v1: {start:'2026-11-23', end:'2026-11-25', course:'early', unitDays:{u1:3}, daysOff:[]},
    hcg_unit_ca_v1: unit('2026-12-07', '2026-12-10', pick.id)
  });
  const next = f.window.HCGTeacherHome.upcomingHTML('2026-11-23');
  assert.match(next.lesson, /2026-12-07.*Colonial America/);
  assert.match(next.assessment, /2026-12-10.*Colonial America/);
  assert.doesNotMatch(next.lesson + next.assessment, /Year Planner only|Projected/);
});
