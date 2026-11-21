const assert = require("node:assert/strict"), fs = require("node:fs"), vm = require("node:vm");
const root = require("node:path").resolve(__dirname, "../public") + "/";
const rawAuth = fs.readFileSync(root + "auth.js", "utf8");
const KEY = "hcg_unit_v1";

function optionSet(d, target, value) { if (d === target) throw Error("quota"); return value; }
function env({local = {}, cloud = null, quota = null, serverError = false} = {}) {
  let backing = new Map(Object.entries(local).map(([k,v])=>[k,JSON.stringify(v)]));
  let session = new Map(), log = [], timers = new Map(), tid = 0, writes = [], reloadCount = 0;
  const ls = {getItem:k=>backing.get(k)??null, setItem:(k,v)=>backing.set(k,optionSet(k,quota,String(v))), removeItem:k=>backing.delete(k)};
  const ss = {getItem:k=>session.get(k)??null,setItem:(k,v)=>session.set(k,v), removeItem:k=>session.delete(k)};
  const win = {sessionStorage:ss, dispatchEvent:v=>log.push(v.type), confirm:()=>true};
  const db = {doc: null, collection(n) { assert.equal(n,"hcgUsers"); return this; },
    doc(uid) { assert.equal(uid,"tester");return this; },
    get(opts) { assert(["server","cache"].includes(opts.source)); if(serverError && opts.source==="server") return Promise.reject(Error("offline"));return Promise.resolve({exists:!!cloud,data:()=>cloud}); },
    set(data,o) { writes.push([data,o]); return (db.waitForSet || Promise.resolve()).then(()=>{cloud={...cloud,...data};}); },
    async runTransaction(action) {
      let commit;
      const answer = await action({get: ()=>db.get({source:"server"}), set:(_ref,data,o)=>{commit=()=>db.set(data,o);}});
      if(commit) await commit();
      return answer;
    }
  };
  const context = {localStorage:ls, window:win, document:{readyState:"loading",addEventListener:()=>{},getElementById:()=>null},
    location:{reload:()=>reloadCount++}, CustomEvent:class{constructor(type){this.type=type;}}, console:{warn:()=>{}},
    setTimeout:(fn,ms)=>{timers.set(++tid,{fn,ms});return tid;}, clearTimeout:id=>timers.delete(id)};
  const code = rawAuth.replace("  // ---------------- boot",`  window.__test = {
    keys: PLAN_KEYS, backup: saveBackup, validate: validatePortable, apply: applyPlansToLocal, read: readLocalPlans,
    readBackups: readBackups, resolve: resolveOnSignIn, pause: pauseSync,
    update: uploadPlans, generation: function(){return syncGeneration;},
    install: function(dataRef){db=dataRef;user={uid:"tester"};}, choose: function(fn){choosePlanCopy=fn;}
  };
  // ---------------- boot`);
  vm.runInNewContext(code,context);
  const t=win.__test;t.install(db);
  return {t,ls,ss,win,db,log,timers,writes,reloads:()=>reloadCount, changeCloud:x=>{cloud=x;},readDevice: k=>JSON.parse(ls.getItem(k))};
}
const planned = n => ({ selected:{[n]:true} });
const account = (p,at="2026-10-10T11:00:00.000Z") => ({plans:{[KEY]:p},plansUpdatedAt:at,entitlement:{allAccess:true,status:"active"}});
async function run() {
  let e=env({local:{[KEY]:planned("a")},cloud:account(planned("a"))});
  await e.t.resolve(e.t.generation());
  assert.match(e.win.HCGAuth.plannerSaveStatus(),/and synced/);
  assert.equal(e.writes.length,0);
  e.ls.setItem(KEY,JSON.stringify(planned("a")));
  assert.equal(e.timers.size,0,"same render is not a fresh save");
  let finish;
  e.db.waitForSet = new Promise(resolve=>finish=resolve);
  e.ls.setItem(KEY,JSON.stringify(planned("b")));
  assert.match(e.win.HCGAuth.plannerSaveStatus(),/Syncing/);
  const timer = [...e.timers.values()].find(t=>t.ms===1500);
  assert(timer); timer.fn();
  await new Promise(setImmediate);
  assert.equal(e.writes.length,1);
  e.ls.setItem(KEY,JSON.stringify(planned("c")));
  finish(); await new Promise(setImmediate);
  assert.match(e.win.HCGAuth.plannerSaveStatus(),/Syncing/,"older cloud acknowledgment must not confirm later edit");
  e.db.waitForSet = null;
  assert(await e.t.update());
  assert.match(e.win.HCGAuth.plannerSaveStatus(),/and synced/);
  assert(!("entitlement" in e.writes[1][0]));
  assert.equal(e.writes[1][1].merge,true);

  e=env({local:{[KEY]:planned("a")},cloud:account(planned("a"))});
  await e.t.resolve(e.t.generation());
  e.changeCloud(account(planned("other-device"),"2026-10-11"));
  e.ls.setItem(KEY,JSON.stringify(planned("my-edit")));
  assert.equal(await e.t.update(),false,"normal upload refuses a newer device copy");
  assert.equal(e.writes.length,0);
  assert.match(e.win.HCGAuth.plannerSaveStatus(),/Plans changed/);

  e=env({local:{[KEY]:planned("start")},cloud:null});
  const originalTx = e.db.runTransaction.bind(e.db);
  e.db.runTransaction=async fn=>{e.changeCloud(account(planned("populated-elsewhere")));return originalTx(fn);};
  await e.t.resolve(e.t.generation());
  assert.equal(e.writes.length,0,"initial empty-account check protects a newer account");
  assert.match(e.win.HCGAuth.plannerSaveStatus(),/Plans changed/);

  e=env({local:{[KEY]:planned("a")},cloud:account(planned("z")),serverError:true});
  await e.t.resolve(e.t.generation());
  assert.match(e.win.HCGAuth.plannerSaveStatus(),/could not finish/);
  assert.equal(e.writes.length,0);

  e=env({local:{[KEY]:planned("a")},cloud:account(planned("z"))});
  e.t.choose(async (a,at,b,bt,safe)=>{assert(safe);assert.equal(e.t.readBackups().length,1); return "pause";});
  await e.t.resolve(e.t.generation());
  assert.match(e.win.HCGAuth.plannerSaveStatus(),/paused/);
  assert.equal(e.writes.length,0);
  assert.deepEqual(e.readDevice(KEY),planned("a"));
  let backup=e.t.readBackups()[0];
  assert.deepEqual(JSON.parse(JSON.stringify(backup.account.plans[KEY])),planned("z"));
  let portable={format:"hcg-planner-backup",version:1,savedAt:backup.account.savedAt,plans:backup.account.plans};
  assert(e.t.validate(portable));
  assert(!e.t.validate({...portable,plans:{...portable.plans,unexpected:{}}}));
  assert(!e.t.validate({...portable,plans:{...portable.plans,[KEY]:{selected:{},sections:[{start:"<tag>",test:"2026-11-02"}]}}}));
  assert(e.t.apply(backup.account.plans,backup.account.savedAt));
  assert.deepEqual(e.readDevice(KEY),planned("z"));
  assert.equal(e.ss.getItem("hcg_plan_sync_paused_v1"),"1");
  assert.equal(e.writes.length,0);

  e=env({local:{[KEY]:planned("a")},cloud:account(planned("z")),quota:"hcg_plan_backups_v1"});
  e.t.choose(async (...a)=>{assert.equal(a[4],false); return "account";});
  await e.t.resolve(e.t.generation());
  assert.equal(e.reloads(),0); assert.equal(e.writes.length,0);
  assert.deepEqual(e.readDevice(KEY),planned("a"));

  e=env({local:{[KEY]:planned("a")},cloud:account(planned("z"))});
  e.t.choose(async()=>{e.changeCloud(account(planned("z-new"),"2026-10-11"));return "device";});
  await e.t.resolve(e.t.generation());
  assert.match(e.win.HCGAuth.plannerSaveStatus(),/Plans changed/);
  assert.equal(e.writes.length,0);

  e=env({local:{[KEY]:planned("a")},cloud:account(planned("z"))});
  e.t.choose(async()=>"device");
  await e.t.resolve(e.t.generation());
  assert.equal(e.writes.length,1);
  assert.deepEqual(JSON.parse(JSON.stringify(e.writes[0][0].plans[KEY])),planned("a"));
  assert.deepEqual(JSON.parse(JSON.stringify(e.t.readBackups()[0].account.plans[KEY])),planned("z"));
  assert.match(e.win.HCGAuth.plannerSaveStatus(),/and synced/);

  e=env({local:{[KEY]:planned("a")},cloud:account(planned("z"))});
  e.t.choose(async()=>"account");
  await e.t.resolve(e.t.generation());
  assert.equal(e.reloads(),1); assert.equal(e.writes.length,0);
  assert.deepEqual(e.readDevice(KEY),planned("z"));

  for (const f of ["planner.js","year-planner.js"]) {
    const src = fs.readFileSync(root+f,"utf8");
    const saving=src.slice(src.indexOf("  function save()"),src.indexOf("\n  }",src.indexOf("  function save()")));
    assert.match(saving,/localStorage\.setItem[\s\S]*?deviceSaved = true/);
    assert.match(saving,/catch[^;]+deviceSaved = false/);
    assert(!src.includes("Saved and synced to your account ·"));
    assert(src.includes('window.addEventListener("hcgplansync", paintSaveNote)'));
    new vm.Script(src);
  }
  console.log("PASS: server-confirmed and offline status; unchanged render; pending and stale ack; both backups and pause; portable validation; local restore only; quota refusal; compare-and-replace transaction; both conflict choices; planner status contracts.");
}
run().catch(err=>{console.error(err);process.exitCode=1;});
