(function () {
  "use strict";

  // Shared unit placement. Inputs are chronologically ordered meeting slots,
  // ordered assignment entries, pin dates by entry key, and lesson-day
  // capacity per meeting. Build new buckets and copies; do not modify inputs.
  function allocate(usable, orderedEntries, pins, cap) {
    var entries = orderedEntries.map(function (entry) { return Object.assign({}, entry); });
    var buckets = usable.map(function (slot) {
      return { iso: slot.iso, date: slot.date, entries: [], load: 0, continuations: [] };
    });
    var idx = Object.create(null), placedOn = Object.create(null), overflow = [];
    buckets.forEach(function (bucket, i) { idx[bucket.iso] = i; });
    function baseId(key) { return key.replace(/#[ab]$/, ""); }

    // Reserve every pinned start before placing any long item's
    // continuation. A continuation may skip an occupied date instead of
    // overfilling it or disappearing from the remaining work.
    function placeStart(e, startAt) {
      var cost = Math.min(e.days, cap);
      for (var j = startAt; j < buckets.length; j++) {
        var first = buckets[j];
        if (first.load + cost > cap + 0.001) continue;
        first.entries.push(e);
        first.load += cost;
        e.placedIso = first.iso;
        placedOn[e.key] = first.iso;
        return j;
      }
      overflow.push(Object.assign({}, e, { remainingDays: e.days }));
      return -1;
    }
    function placeTail(e, startAt) {
      var rem = e.days - cap, last = startAt;
      for (var j = startAt + 1; j < buckets.length && rem > 0.001; j++) {
        var cost = Math.min(rem, cap), b = buckets[j];
        if (b.load + cost > cap + 0.001) continue;
        b.load += cost;
        b.continuations.push(e);
        rem -= cost;
        last = j;
      }
      if (rem > 0.001) overflow.push(Object.assign({}, e, { remainingDays: rem }));
      return last;
    }

    var pinnedTails = [];
    entries.filter(function (e) { return !!pins[e.key]; }).sort(function (a, b) {
      return pins[a.key].localeCompare(pins[b.key]);
    }).forEach(function (e) {
      var pin = pins[e.key];
      var startAt = buckets.findIndex(function (b) { return b.iso >= pin; });
      var placed = placeStart(e, startAt === -1 ? buckets.length : startAt);
      if (placed < 0) return;
      if (buckets[placed].iso !== pin) e.pinMovedFrom = pin;
      if (e.days > cap) pinnedTails.push({ entry: e, dateIndex: placed });
    });
    pinnedTails.forEach(function (t) { placeTail(t.entry, t.dateIndex); });

    var p = 0;
    entries.forEach(function (e) {
      if (pins[e.key]) return;
      if (e.days === 0) {
        placeStart(e, Math.max(0, Math.min(p, buckets.length - 1)));
        return;
      }
      var placed = placeStart(e, p);
      if (placed >= 0) p = placeTail(e, placed);
    });

    // A zero-day entry (guided notes) runs with the entry above it, so it
    // belongs wherever that entry landed. If the entry above overflowed,
    // the rider overflows too, named in the overflow note, instead of
    // piling onto the last teaching day. Days then list their entries in
    // plan order, and the overflow list reads in plan order as well.
    var entryIndex = {};
    entries.forEach(function (e, i) { entryIndex[e.key] = i; });
    var overflowedKeys = {};
    overflow.forEach(function (e) { overflowedKeys[e.key] = true; });
    function riderAnchor(e) {
      var i, c, sib;
      for (i = entryIndex[e.key] - 1; i >= 0; i--) {
        c = entries[i];
        if (c.days <= 0) continue;
        if (!overflowedKeys[c.key]) return c;
        sib = entries.filter(function (x) {
          return baseId(x.key) === baseId(c.key) && !overflowedKeys[x.key] && x.placedIso;
        })[0];
        return sib || c;
      }
      for (i = entryIndex[e.key] + 1; i < entries.length; i++) {
        c = entries[i];
        if (c.days > 0) return c;
      }
      return null;
    }
    entries.forEach(function (e) {
      if (e.days !== 0 || pins[e.key] || overflowedKeys[e.key]) return;
      var anchor = riderAnchor(e);
      if (!anchor) return;
      var from = e.placedIso ? buckets[idx[e.placedIso]] : null;
      if (overflowedKeys[anchor.key]) {
        if (from) from.entries = from.entries.filter(function (x) { return x !== e; });
        delete e.placedIso;
        delete placedOn[e.key];
        overflow.push(e);
        overflowedKeys[e.key] = true;
      } else if (anchor.placedIso && e.placedIso !== anchor.placedIso) {
        if (from) from.entries = from.entries.filter(function (x) { return x !== e; });
        var to = buckets[idx[anchor.placedIso]];
        if (to) {
          to.entries.push(e);
          e.placedIso = anchor.placedIso;
          placedOn[e.key] = anchor.placedIso;
        }
      }
    });
    overflow.sort(function (a, b) { return entryIndex[a.key] - entryIndex[b.key]; });
    buckets.forEach(function (b) {
      b.entries.sort(function (a, c) { return entryIndex[a.key] - entryIndex[c.key]; });
    });

    var usedDays = buckets.filter(function (b) { return b.entries.length || b.load > 0; }).length;
    // Lesson-days the placed entries span at 45-minute pacing: each used
    // meeting counts the lesson-days packed into it (a meeting holding
    // only a same-day item still spans one lesson-day). At capacity 1 this
    // equals usedDays exactly, so 45-minute plans are unchanged.
    var lessonDays = 0;
    buckets.forEach(function (b) {
      if (b.entries.length || b.load > 0) lessonDays += Math.max(1, Math.ceil(b.load - 1e-9));
    });
    return { buckets: buckets, overflow: overflow, placedOn: placedOn, usedDays: usedDays, usableCount: usable.length, lessonDays: lessonDays };
  }

  window.HCGUnitSchedule = { allocate: allocate };
})();
