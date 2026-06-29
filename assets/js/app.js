let glossary = [];
let modules = [];
let activeCategory = 'All';
let query = '';
const favKey = 'sc_portal_favorites';
const memoKey = 'sc_portal_memos';
const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];

function loadStore(key, fallback){ try { return JSON.parse(localStorage.getItem(key)) || fallback } catch { return fallback } }
function saveStore(key, value){ localStorage.setItem(key, JSON.stringify(value)) }
function stars(n){ return '★★★★★'.slice(0,n) + '☆☆☆☆☆'.slice(0,5-n) }

async function init(){
  document.documentElement.classList.toggle('light', localStorage.getItem('theme') === 'light');
  $('#themeToggle').textContent = document.documentElement.classList.contains('light') ? '☀' : '☾';
  [glossary, modules] = await Promise.all([
    fetch('data/glossary.json').then(r=>r.json()),
    fetch('data/modules.json').then(r=>r.json())
  ]);
  $('#termCount').textContent = glossary.length;
  renderModules();
  renderCategories();
  renderGlossary();
  if ('serviceWorker' in navigator) navigator.serviceWorker.register('sw.js').catch(()=>{});
}

function renderModules(){
  $('#moduleGrid').innerHTML = modules.map(m => `
    <article class="module" data-module="${m.id}">
      <div class="icon">${m.icon}</div>
      <h3>${m.title}</h3>
      <p>${m.description}</p>
      <span class="status">${m.status === 'active' ? 'active' : 'planned'}</span>
    </article>`).join('');
}

function renderCategories(){
  const cats = ['All', ...new Set(glossary.map(x=>x.category))];
  $('#categoryChips').innerHTML = cats.map(c=>`<button class="chip ${c===activeCategory?'active':''}" data-cat="${c}">${c}</button>`).join('');
  $$('#categoryChips .chip').forEach(btn=>btn.onclick=()=>{activeCategory=btn.dataset.cat;renderCategories();renderGlossary();});
}

function filtered(){
  const favs = loadStore(favKey, []);
  const favOnly = $('#favOnly').checked;
  const q = query.trim().toLowerCase();
  return glossary.filter(t=>{
    const hay = [t.term,t.english,t.katakana,t.category,t.oneLine,t.plainJapanese,...t.related].join(' ').toLowerCase();
    return (activeCategory==='All'||t.category===activeCategory) && (!favOnly||favs.includes(t.id)) && (!q||hay.includes(q));
  });
}

function renderGlossary(){
  const favs = loadStore(favKey, []);
  const arr = filtered();
  $('#resultCount').textContent = `${arr.length} terms`;
  $('#glossaryList').innerHTML = arr.map(t=>`
    <article class="term-card" data-id="${t.id}">
      <div class="term-top">
        <div><span class="pill">${t.category}</span><h3>${t.term}</h3></div>
        <button class="fav" data-fav="${t.id}">${favs.includes(t.id)?'★':'☆'}</button>
      </div>
      <p>${t.oneLine}</p>
      <div class="impact-row">
        <span class="impact bull">Bull ${stars(t.marketImpact.bull)}</span>
        <span class="impact bear">Bear ${stars(t.marketImpact.bear)}</span>
      </div>
    </article>`).join('');
  $$('.term-card').forEach(card=>card.onclick=(e)=>{ if(e.target.dataset.fav) return; openTerm(card.dataset.id); });
  $$('[data-fav]').forEach(btn=>btn.onclick=(e)=>{ e.stopPropagation(); toggleFav(btn.dataset.fav); });
}

function toggleFav(id){
  let favs = loadStore(favKey, []);
  favs = favs.includes(id) ? favs.filter(x=>x!==id) : [...favs, id];
  saveStore(favKey, favs); renderGlossary();
}

function chartSvg(type){
  if(type==='gamma') return `<svg viewBox="0 0 500 140"><path d="M20 85 C140 85 175 40 250 40 C325 40 360 105 480 105" fill="none" stroke="currentColor" stroke-width="4"/><line x1="250" y1="18" x2="250" y2="122" stroke="currentColor" stroke-dasharray="6 6"/><text x="220" y="132" fill="currentColor" font-size="14">Gamma Flip</text></svg>`;
  if(type==='skew') return `<svg viewBox="0 0 500 140"><path d="M25 35 C135 55 250 75 475 105" fill="none" stroke="currentColor" stroke-width="4"/><text x="30" y="125" fill="currentColor" font-size="14">Put IV高 / Call IV低</text></svg>`;
  if(type==='vanna') return `<svg viewBox="0 0 500 140"><path d="M30 100 C130 20 245 115 340 35 C400 -5 450 55 480 30" fill="none" stroke="currentColor" stroke-width="4"/><text x="30" y="125" fill="currentColor" font-size="14">IV変化 → Delta変化 → Hedge</text></svg>`;
  return `<svg viewBox="0 0 500 140"><path d="M20 100 L120 70 L220 88 L320 42 L480 64" fill="none" stroke="currentColor" stroke-width="4"/><text x="30" y="125" fill="currentColor" font-size="14">Market structure</text></svg>`;
}

function openTerm(id){
  const t = glossary.find(x=>x.id===id); if(!t) return;
  const memos = loadStore(memoKey, {});
  $('#dialogCategory').textContent = t.category;
  $('#dialogTitle').textContent = t.term;
  $('#dialogBody').innerHTML = `
    <div class="detail-grid">
      <section class="detail-box"><h3>📖 用語</h3><p>${t.term} / ${t.katakana}</p></section>
      <section class="detail-box"><h3>🇺🇸 英語の意味</h3><p>${t.english}</p></section>
      <section class="detail-box"><h3>🇯🇵 一言でいうと</h3><p>${t.oneLine}</p></section>
      <section class="detail-box"><h3>📈 相場への影響</h3><p>${t.marketImpact.text}</p><p class="bull">Bull ${stars(t.marketImpact.bull)}</p><p class="bear">Bear ${stars(t.marketImpact.bear)}</p></section>
      <section class="detail-box"><h3>📚 詳しい説明</h3><p>${t.plainJapanese}</p></section>
      <section class="detail-box"><h3>💹 ディーラーは何をするか</h3><p>${t.dealerAction}</p></section>
      <section class="detail-box"><h3>🎯 トレーダーは何を見るか</h3><ul>${t.traderChecklist.map(x=>`<li>${x}</li>`).join('')}</ul></section>
      <section class="detail-box"><h3>📈 概念図</h3><div class="mini-chart">${chartSvg(t.chartType)}</div></section>
      <section class="detail-box"><h3>📰 レポート例</h3>${t.reportExamples.map(r=>`<div class="report"><b>${r.source}</b><br>"${r.text}"<br>${r.ja}</div>`).join('')}</section>
      <section class="detail-box"><h3>🔗 関連用語</h3><div class="related">${t.related.map(id=>{const r=glossary.find(x=>x.id===id); return r?`<button class="chip rel" data-rel="${id}">${r.term}</button>`:''}).join('')}</div></section>
      <section class="detail-box" style="grid-column:1/-1"><h3>📝 自分用メモ</h3><textarea class="memo" id="memoArea" placeholder="自分の解説、Bloomberg/GS/JPMリンク、チャートメモを保存">${memos[t.id]||''}</textarea></section>
    </div>`;
  $('#termDialog').showModal();
  $$('.rel').forEach(b=>b.onclick=()=>openTerm(b.dataset.rel));
  $('#memoArea').oninput = e => { const m = loadStore(memoKey, {}); m[t.id]=e.target.value; saveStore(memoKey,m); };
}

$('#searchInput').addEventListener('input', e=>{query=e.target.value;renderGlossary();});
$('#favOnly').addEventListener('change', renderGlossary);
$('#closeDialog').onclick=()=>$('#termDialog').close();
$('#themeToggle').onclick=()=>{document.documentElement.classList.toggle('light'); localStorage.setItem('theme',document.documentElement.classList.contains('light')?'light':'dark'); $('#themeToggle').textContent=document.documentElement.classList.contains('light')?'☀':'☾';};
init();
