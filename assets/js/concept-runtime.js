
async function loadJSON(path){ const r=await fetch(path); if(!r.ok) throw new Error(path); return await r.json(); }
function chips(arr,base='../glossary/'){return (arr||[]).map(x=>`<a class="chip" href="${base}${x}.html">${x}</a>`).join('')}
async function renderConcept(){
 const root=document.getElementById('concept-root'); if(!root)return; const id=root.dataset.id; const c=await loadJSON(`../data/concepts/${id}.json`);
 root.innerHTML=`<section class="hero compact"><p class="eyebrow">OPTION HANDBOOK</p><h1>${c.title}</h1><p>${c.summary}</p></section>
 <section class="panel wide"><div class="panel-title">わかりやすい説明</div><p>${c.description}</p></section>
 <section class="metric-grid"><article class="metric-card"><div class="metric-key">Category</div><div class="metric-value small">${c.category}</div></article><article class="metric-card"><div class="metric-key">Bull</div><div class="metric-value">${'★'.repeat(c.bullBear?.bull||0)}</div></article><article class="metric-card"><div class="metric-key">Bear</div><div class="metric-value">${'★'.repeat(c.bullBear?.bear||0)}</div></article></section>
 <section class="panel"><div class="panel-title">Dealer Action</div><p>${c.dealerAction}</p></section>
 <section class="panel"><div class="panel-title">Trader Watch</div><ul>${(c.traderWatch||[]).map(x=>`<li>${x}</li>`).join('')}</ul></section>
 <section class="panel"><div class="panel-title">Report Examples</div><p><b>Bloomberg:</b> ${c.reportExamples?.Bloomberg||''}</p><p><b>Goldman Sachs:</b> ${c.reportExamples?.['Goldman Sachs']||''}</p><p><b>JPMorgan:</b> ${c.reportExamples?.JPMorgan||''}</p></section>
 <section class="panel"><div class="panel-title">Related</div><div class="chips">${chips(c.related)}</div></section>`;
}
renderConcept().catch(e=>{document.getElementById('concept-root').innerHTML=`<p>Concept load error: ${e.message}</p>`});
