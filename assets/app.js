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
  // Bibliothèques (études, fiches) : recherche et filtres
  d.querySelectorAll('[data-library]').forEach(lib => {
    const items = [...lib.querySelectorAll('[data-item]')], fs = [...lib.querySelectorAll('.f')], search = lib.querySelector('.search'), empty = lib.querySelector('.empty');
    const norm = s => s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    let f = 'all';
    const apply = () => {
      const q = search ? norm(search.value.trim()) : ''; let n = 0;
      items.forEach(it => {
        const [k, v] = f.split(':');
        const ok = (f === 'all' || it.dataset[k] === v) && (!q || norm(it.dataset.text).includes(q));
        it.hidden = !ok; if (ok) { n++; it.classList.add('in'); }
      });
      if (empty) empty.hidden = n > 0;
    };
    if (search) search.addEventListener('input', apply);
    fs.forEach(b => b.addEventListener('click', () => { f = b.dataset.f; fs.forEach(x => x.setAttribute('aria-pressed', x === b)); apply(); }));
  });
  // Test éclair
  d.querySelectorAll('[data-quiz]').forEach(box => {
    const data = JSON.parse(box.querySelector('script').textContent), items = data.items;
    const qn = box.querySelector('.qn'), qq = box.querySelector('.qq'), qr = box.querySelector('.qr'), show = box.querySelector('[data-show]'), next = box.querySelector('[data-next]'), link = box.querySelector('[data-link]');
    let i = Math.floor(Math.random() * items.length);
    const draw = () => { const it = items[i]; qn.textContent = data.fiche + ' ' + String(it.n).padStart(2, '0') + ' · ' + it.t; qq.textContent = it.q; qr.textContent = it.r; qr.hidden = true; link.hidden = true; link.href = it.u; show.hidden = false; };
    show.addEventListener('click', () => { qr.hidden = false; link.hidden = false; show.hidden = true; });
    next.addEventListener('click', () => { i = (i + 1) % items.length; draw(); });
    draw();
  });
  // Questionnaire : limite de choix, contrôle, envoi
  d.querySelectorAll('[data-survey]').forEach(form => {
    const qs = [...form.querySelectorAll('[data-q]')], prog = form.querySelector('.prog'), err = form.querySelector('.serr'), btn = form.querySelector('[type=submit]');
    const answered = q => { const i = [...q.querySelectorAll('input,textarea')]; if (q.querySelector('.scales')) { const names = [...new Set(i.map(n => n.name))]; return names.every(n => form.querySelector(`[name="${n}"]:checked`)); } return i.some(n => n.type === 'textarea' ? n.value.trim() : n.checked); };
    const upd = () => { if (prog) prog.textContent = qs.filter(answered).length + ' / ' + qs.length + ' · ' + prog.dataset.label; };
    form.addEventListener('change', ev => {
      const q = ev.target.closest('[data-max]');
      if (q) { const on = q.querySelectorAll('input:checked'); if (on.length > +q.dataset.max) ev.target.checked = false; }
      const box = ev.target.closest('[data-q]'); if (box) box.classList.remove('miss');
      upd();
    });
    upd();
    form.addEventListener('submit', async ev => {
      ev.preventDefault(); err.hidden = true;
      const need = qs.filter(q => q.querySelector('[required]') && !answered(q));
      const consent = [...form.querySelectorAll('.notice input')].filter(c => !c.checked);
      qs.forEach(q => q.classList.toggle('miss', need.includes(q)));
      if (consent.length) { consent[0].focus(); consent[0].closest('.notice').scrollIntoView({ block: 'center' }); return; }
      if (need.length) { need[0].scrollIntoView({ block: 'center' }); return; }
      if (!form.dataset.endpoint) return;
      const label = btn.textContent; btn.disabled = true; btn.textContent = form.dataset.sending;
      const fd = new FormData(form), out = new FormData();
      for (const k of new Set(fd.keys())) out.append(k, fd.getAll(k).join(' | '));
      try {
        const r = await fetch(form.dataset.endpoint, { method: 'POST', body: out, headers: { Accept: 'application/json' } });
        if (!r.ok) throw new Error(r.status);
        form.hidden = true; const t = form.parentElement.querySelector('.sthanks'); t.hidden = false; t.focus(); t.scrollIntoView({ block: 'center' });
      } catch (e2) { err.hidden = false; btn.disabled = false; btn.textContent = label; }
    });
  });
  // Copier la référence
  d.querySelectorAll('[data-copy]').forEach(b => b.addEventListener('click', async () => {
    const t = d.querySelector(b.dataset.copy).innerText, label = b.textContent;
    try { await navigator.clipboard.writeText(t); } catch (e) { const r = d.createRange(); r.selectNode(d.querySelector(b.dataset.copy)); getSelection().removeAllRanges(); getSelection().addRange(r); d.execCommand('copy'); }
    b.textContent = b.dataset.done; setTimeout(() => { b.textContent = label; }, 1800);
  }));
  // Vidéothèque : choix de la langue par série
  d.querySelectorAll('[data-series]').forEach(s => {
    const bs = [...s.querySelectorAll('[data-vl]')];
    bs.forEach(b => b.addEventListener('click', () => {
      bs.forEach(x => x.setAttribute('aria-pressed', x === b));
      s.querySelectorAll('[data-l]').forEach(c => { const on = c.dataset.l === b.dataset.vl; c.hidden = !on; if (!on) { const v = c.querySelector('video'); if (v) v.pause(); } });
    }));
  });
  // Une seule vidéo à la fois
  const vids = [...d.querySelectorAll('video')];
  vids.forEach(v => v.addEventListener('play', () => vids.forEach(o => { if (o !== v) o.pause(); })));
})();
