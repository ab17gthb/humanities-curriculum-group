const { test } = require('node:test');
const a = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const window = {};
vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../public/unit-scheduler.js'), 'utf8'), { window });
const allocate = window.HCGUnitSchedule.allocate;
const dates = ['2026-11-23', '2026-11-24', '2026-11-25'].map(iso => Object.freeze({ iso }));
const entry = (key, days) => Object.freeze({ key, days, name: key });

test('shared allocator preserves input and assigns a long tail after a full pinned day', () => {
  const entries = Object.freeze([entry('long', 2), entry('pin', 1)]);
  const pins = Object.freeze({ long: dates[0].iso, pin: dates[1].iso });
  const before = JSON.stringify([dates, entries, pins]);
  const result = allocate(dates, entries, pins, 1);
  a.equal(JSON.stringify([dates, entries, pins]), before);
  a.equal(result.buckets[0].entries[0].key, 'long');
  a.equal(result.buckets[1].entries[0].key, 'pin');
  a.equal(result.buckets[2].continuations[0].key, 'long');
  a.equal(result.buckets[1].load, 1);
  a.equal(result.overflow.length, 0);
});

test('shared allocator reports duration unavailable at the end of a short calendar', () => {
  const result = allocate(dates.slice(0, 1), [entry('long', 2)], {}, 1);
  a.equal(result.usedDays, 1);
  a.equal(result.overflow.length, 1);
  a.equal(result.overflow[0].remainingDays, 1);
});
