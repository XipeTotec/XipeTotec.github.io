const CACHE='nightcliff-v11';
const ASSETS=['/','/tides.html','/logo.png','/banner.png'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(
  caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE).map(k=>caches.delete(k))))
  .then(()=>self.clients.claim())
  .then(()=>self.clients.matchAll({type:'window'}).then(cls=>cls.forEach(c=>c.postMessage({type:'SW_UPDATED',version:CACHE}))))
));
function stash(req,res){
  if(res&&res.status===200&&res.type==='basic'){const clone=res.clone();caches.open(CACHE).then(c=>c.put(req,clone));}
  return res;
}
self.addEventListener('fetch',e=>{
  if(e.request.method!=='GET'||!e.request.url.startsWith(self.location.origin))return;
  // Pages: try the network first so updates show straight away, fall back to the cache offline.
  if(e.request.mode==='navigate'){
    e.respondWith(fetch(e.request).then(res=>stash(e.request,res)).catch(()=>caches.match(e.request).then(r=>r||caches.match('/'))));
    return;
  }
  // Everything else: cache first, then network.
  e.respondWith(caches.match(e.request).then(r=>r||fetch(e.request).then(res=>stash(e.request,res))));
});
