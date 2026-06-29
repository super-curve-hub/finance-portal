const CACHE = 'sc-finance-portal-v1';
const ASSETS = ['./','index.html','assets/css/style.css','assets/js/app.js','data/glossary.json','data/modules.json','data/research-links.json','manifest.webmanifest'];
self.addEventListener('install', event => event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(ASSETS))));
self.addEventListener('fetch', event => event.respondWith(caches.match(event.request).then(res => res || fetch(event.request))));
