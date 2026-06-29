async function initSearch(){
  const input=document.querySelector('#searchInput'); const out=document.querySelector('#results');
  if(!input||!out) return;
  const data=await fetchJson('../api/search.json');
  function render(q=''){
    const s=q.trim().toLowerCase();
    const rows=data.objects.filter(x=>!s || [x.title,x.summary,x.type,...(x.tags||[])].join(' ').toLowerCase().includes(s)).slice(0,80);
    out.innerHTML=rows.map(x=>`<article class="result"><span class="tag">${x.type}</span><h3>${x.title}</h3><p>${x.summary||''}</p><div class="tags">${(x.tags||[]).map(t=>`<span class="tag">${t}</span>`).join('')}</div>${x.url?`<p><a class="btn" href="../${x.url}">Open</a></p>`:''}</article>`).join('') || '<p>該当なし</p>';
  }
  input.addEventListener('input',e=>render(e.target.value)); render();
}
document.addEventListener('DOMContentLoaded', initSearch);
