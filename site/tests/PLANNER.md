# Planner checks

Run the planner regression checks from the repository root with Node:

```sh
node --test site/tests/*planner*.test.cjs site/tests/unit-scheduler.test.cjs
```

These tests use the checked-in curriculum registry with synthetic plans. They
don't require credentials, call Firebase, or use saved teacher data.

- `unit-scheduler.js` assigns ordered items to available meetings. Unit Planner
  and My Day both call it. Keep placement rules in that module so their calendars
  don't disagree.
- Unit Planner tests exercise dates, pins, continuations, lost meetings, imports,
  the sampled week and its separate drafts, and calendar exports.
- Year Planner tests exercise date validation, days off, block scheduling, late
  pins, imports, shared plans, tests, and My Day.
- The sync test uses a fake Firebase backend to check confirmation, offline
  behavior, stale writes, backup, and conflict choices.

Before a production release, check a normal save and a competing edit in two
browsers with an authorized test account. Keep test plans synthetic. Review the
Year Planner, Unit Planner, and My Day views after the conflict is resolved.
