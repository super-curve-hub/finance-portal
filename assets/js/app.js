const $ = (s, r=document)=>r.querySelector(s);
const $$ = (s, r=document)=>Array.from(r.querySelectorAll(s));
const base = location.pathname.includes('/finance-portal/') ? '/finance-portal/' : './';

function toggleTheme(){
  const root=document.documentElement; root.classList.toggle('light');
  localStorage.setItem('sc-theme', root.classList.contains('light')?'light':'dark');
}
function initTheme(){ if(localStorage.getItem('sc-theme')==='light') document.documentElement.classList.add('light'); }
async function fetchJson(path){ const res=await fetch(path); if(!res.ok) throw new Error(path); return res.json(); }
function nav(){return `<header class="topbar"><div class="shell nav"><div class="brand">SUPER CURVE TERMINAL</div><nav class="navlinks"><a href="${base}">Home</a><a href="${base}glossary/">Handbook</a><a href="${base}dashboard/gex.html">GEX</a><a href="${base}search/">AI Search</a><button onclick="toggleTheme()">Theme</button></nav></div></header>`}
function footer(){return `<footer class="footer"><div class="shell">Knowledge × Market Data × Research. Built for GitHub Pages.</div></footer>`}
function installShell(){document.body.insertAdjacentHTML('afterbegin',nav());document.body.insertAdjacentHTML('beforeend',footer());initTheme(); if('serviceWorker' in navigator) navigator.serviceWorker.register(`${base}sw.js`).catch(()=>{});}
document.addEventListener('DOMContentLoaded', installShell);
