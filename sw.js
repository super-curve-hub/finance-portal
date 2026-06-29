const CACHE_NAME = 'super-curve-finance-portal-v1';
const ASSETS = ['./','./index.html','./assets/css/style.css','./assets/js/app.js','./assets/js/search.js','./data/glossary.json','./data/modules.json'];
self.addEventListener('install', event => event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS))));
self.addEventListener('fetch', event => event.respondWith(caches.match(event.request).then(res => res || fetch(event.request))));
