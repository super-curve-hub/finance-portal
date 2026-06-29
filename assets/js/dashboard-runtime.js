
async function loadJSON(path){ const r=await fetch(path); if(!r.ok) throw new Error(path); return await r.json(); }
function metricCard(k,v){ return `<article class="metric-card"><div class="metric-key">${k}</div><div class="metric-value">${v}</div></article>`; }
function stars(n){ return '★'.repeat(Math.max(0,Math.min(5,Number(n)||0))) + '☆'.repeat(5-Math.max(0,Math.min(5,Number(n)||0))); }
async function renderDashboard(){
 const root=document.getElementById('dashboard-root'); if(!root) return;
 const id=root.dataset.dashboard; const short=id.replace('-dashboard','');
 const dash=await loadJSON(`../data/dashboards/${id}.json`);
 const market=await loadJSON(`../data/market/${short}.json`);
 root.innerHTML = `
  <section class="panel wide"><div class="panel-title">Today's Regime</div><h2>${market.regime||dash.title}</h2><p>${dash.summary}</p><p class="muted">as of ${market.asOf||'manual update'}</p></section>
  <section class="metric-grid">${Object.entries(market).filter(([k])=>!['asOf','note'].includes(k)).map(([k,v])=>metricCard(k,v)).join('')}</section>
  <section class="panel"><div class="panel-title">Trader Watch</div><ul>${dash.metrics.map(x=>`<li>${x}</li>`).join('')}</ul></section>
  <section class="panel"><div class="panel-title">Related Concepts</div><div class="chips">${dash.related.map(x=>`<a class="chip" href="../glossary/${x}.html">${x}</a>`).join('')}</div></section>
  <section class="panel wide"><div class="panel-title">Implementation Note</div><p>${dash.interpretation}</p><p>${market.note||'このJSONを外部データ更新スクリプトで置き換えると、GitHub Pages上の画面も更新される。'}</p></section>`;
}
renderDashboard().catch(e=>{document.getElementById('dashboard-root').innerHTML=`<p>Dashboard load error: ${e.message}</p>`});
