const state = { data: null, selected: null };

const fmt = (n, suffix = '') => Number.isFinite(n) ? `${n.toLocaleString()}${suffix}` : '-';
const signed = (n) => Number.isFinite(n) ? `${n > 0 ? '+' : ''}${n.toFixed(2)}` : '-';

async function loadGexData(){
  const res = await fetch('../data/gex-dashboard.json');
  state.data = await res.json();
  state.selected = state.data.markets[0].id;
  initMarketSelect();
  renderAll();
}

function initMarketSelect(){
  const select = document.getElementById('marketSelect');
  select.innerHTML = state.data.markets.map(m => `<option value="${m.id}">${m.name}</option>`).join('');
  select.addEventListener('change', e => { state.selected = e.target.value; renderAll(); });
  document.getElementById('refreshBtn')?.addEventListener('click', renderAll);
}

function getSelected(){ return state.data.markets.find(m => m.id === state.selected) || state.data.markets[0]; }

function renderAll(){
  renderMarketCards();
  renderSelected();
  renderRules();
  drawGexChart();
}

function renderMarketCards(){
  const root = document.getElementById('marketCards');
  root.innerHTML = state.data.markets.map(m => `
    <article class="card market-tile ${m.id === state.selected ? 'active' : ''}" data-id="${m.id}">
      <span class="badge">${m.regime}</span>
      <h3>${m.name}</h3>
      <p class="muted">Spot ${fmt(m.spot)} / Flip ${fmt(m.gammaFlip)}</p>
      <div class="kpi-grid">
        <div class="kpi"><span>Net GEX</span><b class="${m.netGex >= 0 ? 'bull' : 'bear'}">${signed(m.netGex)}</b></div>
        <div class="kpi"><span>Risk</span><b>${m.riskScore}</b><div class="riskbar"><i style="width:${m.riskScore}%"></i></div></div>
      </div>
    </article>`).join('');
  root.querySelectorAll('.market-tile').forEach(el => el.addEventListener('click', () => {
    state.selected = el.dataset.id;
    document.getElementById('marketSelect').value = state.selected;
    renderAll();
  }));
}

function renderSelected(){
  const m = getSelected();
  document.getElementById('selectedTitle').textContent = m.name;
  document.getElementById('regimeBadge').textContent = m.regime;
  document.getElementById('marketSummary').textContent = m.summary;
  document.getElementById('kpiGrid').innerHTML = [
    ['Spot', fmt(m.spot)],
    ['Gamma Flip', fmt(m.gammaFlip)],
    ['Net GEX', signed(m.netGex)],
    ['Vanna', signed(m.vanna)],
    ['Charm', signed(m.charm)],
    ['Call Wall', fmt(m.callWall)],
    ['Put Wall', fmt(m.putWall)],
    ['0DTE Share', fmt(m.zeroDteShare, '%')],
    ['IV Rank', fmt(m.ivRank, '%')],
    ['Risk Score', fmt(m.riskScore)]
  ].map(([k,v]) => `<div class="kpi"><span>${k}</span><b>${v}</b></div>`).join('');
  document.getElementById('watchList').innerHTML = m.watch.map(x => `<li>${x}</li>`).join('');
}

function renderRules(){
  const root = document.getElementById('ruleGrid');
  root.innerHTML = state.data.regimeRules.map(r => `
    <article class="card term-card">
      <span class="badge">${r.condition}</span>
      <h3>${r.name}</h3>
      <div class="field"><b>ディーラー</b><span>${r.dealerAction}</span></div>
      <div class="field"><b>トレード含意</b><span>${r.tradeImplication}</span></div>
    </article>`).join('');
}

function drawGexChart(){
  const canvas = document.getElementById('gexChart');
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const cssW = canvas.clientWidth || 900;
  const cssH = Math.max(360, cssW * 0.52);
  canvas.width = cssW * dpr; canvas.height = cssH * dpr;
  ctx.scale(dpr, dpr);
  ctx.clearRect(0,0,cssW,cssH);
  const data = state.data.strikeMap;
  const pad = {l:78,r:28,t:28,b:42};
  const w = cssW - pad.l - pad.r;
  const h = cssH - pad.t - pad.b;
  const maxAbs = Math.max(...data.map(x => Math.abs(x.netGex))) || 1;
  const zeroX = pad.l + w/2;
  ctx.strokeStyle = getCss('--line'); ctx.lineWidth = 1;
  ctx.beginPath(); ctx.moveTo(zeroX,pad.t); ctx.lineTo(zeroX,pad.t+h); ctx.stroke();
  ctx.font = '12px system-ui'; ctx.fillStyle = getCss('--muted');
  ctx.fillText('Negative GEX', pad.l, 18); ctx.fillText('Positive GEX', zeroX + 10, 18);
  data.forEach((row,i) => {
    const y = pad.t + (i + .5) * h / data.length;
    const barW = (Math.abs(row.netGex) / maxAbs) * (w/2 - 18);
    const x = row.netGex >= 0 ? zeroX : zeroX - barW;
    ctx.fillStyle = row.netGex >= 0 ? getCss('--good') : getCss('--bad');
    roundRect(ctx, x, y-12, barW, 24, 8); ctx.fill();
    ctx.fillStyle = getCss('--text'); ctx.textAlign = 'right'; ctx.fillText(row.strike.toLocaleString(), pad.l - 12, y + 4);
    ctx.textAlign = row.netGex >= 0 ? 'left' : 'right';
    ctx.fillText(signed(row.netGex), row.netGex >= 0 ? x + barW + 8 : x - 8, y + 4);
    ctx.strokeStyle = getCss('--line'); ctx.beginPath(); ctx.moveTo(pad.l, y+18); ctx.lineTo(pad.l+w, y+18); ctx.stroke();
  });
  ctx.textAlign = 'center'; ctx.fillStyle = getCss('--muted'); ctx.fillText('Strike', pad.l - 38, cssH - 14); ctx.fillText('Net Gamma Exposure', zeroX, cssH - 14);
}

function getCss(name){ return getComputedStyle(document.documentElement).getPropertyValue(name).trim(); }
function roundRect(ctx,x,y,w,h,r){
  const rr = Math.min(r, Math.abs(w)/2, h/2); ctx.beginPath();
  ctx.moveTo(x+rr,y); ctx.lineTo(x+w-rr,y); ctx.quadraticCurveTo(x+w,y,x+w,y+rr);
  ctx.lineTo(x+w,y+h-rr); ctx.quadraticCurveTo(x+w,y+h,x+w-rr,y+h);
  ctx.lineTo(x+rr,y+h); ctx.quadraticCurveTo(x,y+h,x,y+h-rr);
  ctx.lineTo(x,y+rr); ctx.quadraticCurveTo(x,y,x+rr,y); ctx.closePath();
}

window.addEventListener('resize', () => { if(state.data) drawGexChart(); });
loadGexData().catch(err => {
  console.error(err);
  document.getElementById('marketCards').innerHTML = `<article class="card"><b>データ読込エラー</b><p class="muted">${err.message}</p></article>`;
});
