function renderBarChart(el, rows, key='strike', val='gex'){
  if(!el) return;
  const max=Math.max(...rows.map(r=>Math.abs(r[val])));
  el.innerHTML=rows.map(r=>`<div style="display:grid;grid-template-columns:70px 1fr 80px;gap:10px;align-items:center;margin:8px 0"><span class="label">${r[key]}</span><div style="height:12px;background:rgba(148,163,184,.18);border-radius:99px;overflow:hidden"><div style="height:100%;width:${Math.abs(r[val])/max*100}%;background:${r[val]>=0?'var(--good)':'var(--bad)'}"></div></div><b>${r[val]}</b></div>`).join('');
}
