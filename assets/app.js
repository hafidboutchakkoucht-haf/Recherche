(() => {
  const d = document, root = d.documentElement;
  // Thème clair / sombre
  const tb = d.querySelector('[data-theme]');
  if (tb) tb.addEventListener('click', () => {
    const dark = root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
    root.dataset.theme = dark ? 'light' : 'dark';
    try { localStorage.setItem('nr-theme', root.dataset.theme); } catch (e) {}
  });
  // Barre de progression de lecture
  const bar = d.querySelector('.bar');
  if (bar) { const up = () => { const h = d.documentElement.scrollHeight - innerHeight; bar.style.transform = `scaleX(${h > 0 ? scrollY / h : 0})`; }; addEventListener('scroll', up, { passive: true }); up(); }
  // Apparition au défilement
  const io = 'IntersectionObserver' in window ? new IntersectionObserver(es => es.forEach(x => { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } }), { rootMargin: '0px 0px -6% 0px' }) : null;
  d.querySelectorAll('.rv').forEach(el => io ? io.observe(el) : el.classList.add('in'));
  // Bibliothèque : recherche et filtres
  const lib = d.querySelector('[data-library]');
  if (lib) {
    const items = [...lib.querySelectorAll('[data-item]')], fs = [...lib.querySelectorAll('.f')], search = lib.querySelector('.search'), empty = lib.querySelector('.empty');
    const norm = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
    let f = 'all';
    const apply = () => {
      const q = norm(search.value.trim()); let n = 0;
      items.forEach(it => {
        const [k, v] = f.split(':');
        const ok = (f === 'all' || it.dataset[k] === v) && (!q || norm(it.dataset.text).includes(q));
        it.hidden = !ok; if (ok) { n++; it.classList.add('in'); }
      });
      empty.hidden = n > 0;
    };
    search.addEventListener('input', apply);
    fs.forEach(b => b.addEventListener('click', () => { f = b.dataset.f; fs.forEach(x => x.setAttribute('aria-pressed', x === b)); apply(); }));
  }
  // Copier la référence
  d.querySelectorAll('[data-copy]').forEach(b => b.addEventListener('click', async () => {
    const t = d.querySelector(b.dataset.copy).innerText, label = b.textContent;
    try { await navigator.clipboard.writeText(t); } catch (e) { const r = d.createRange(); r.selectNode(d.querySelector(b.dataset.copy)); getSelection().removeAllRanges(); getSelection().addRange(r); d.execCommand('copy'); }
    b.textContent = b.dataset.done; setTimeout(() => { b.textContent = label; }, 1800);
  }));
  // Une seule vidéo à la fois
  const vids = [...d.querySelectorAll('video')];
  vids.forEach(v => v.addEventListener('play', () => vids.forEach(o => { if (o !== v) o.pause(); })));
})();
