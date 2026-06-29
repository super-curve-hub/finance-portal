const CACHE_NAME = 'sc-finance-portal-v1';
const ASSETS = [
  './', './index.html', './assets/css/style.css', './assets/js/app.js', './api/search.json'
];
self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS)));
});
self.addEventListener('fetch', event => {
  event.respondWith(caches.match(event.request).then(resp => resp || fetch(event.request)));
});
