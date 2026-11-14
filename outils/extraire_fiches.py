import re, json, sys, glob, os
from bs4 import BeautifulSoup
D = sys.argv[1]
out = []
for f in sorted(glob.glob(D + '/project/F*.dc.html')):
    s = open(f, encoding='utf-8').read()
    body = s[s.index('<x-dc>') + 6: s.index('</x-dc>')]
    soup = BeautifulSoup(body, 'html.parser')
    for h in soup.find_all('helmet'): h.decompose()
    txt = lambda el: re.sub(r'\s+', ' ', el.get_text(' ', strip=True)) if el else ''
    h1 = soup.find('h1')
    head = h1.parent
    kick = [sp for sp in head.find_all('span') if 'Fiche' in sp.get_text()][0]
    m = re.match(r'Fiche (\d+) / 12 · (.+)', txt(kick))
    ar = head.find(attrs={'lang': 'ar', 'dir': 'rtl'})
    pills = [txt(sp) for sp in head.find_all('span') if '999px' in (sp.get('style') or '')]
    def labelled(prefix):
        for d in soup.find_all('div'):
            t = d.get_text(strip=True)
            if t.startswith(prefix) and 'uppercase' in (d.get('style') or '') and len(t) < 60:
                sib = d.find_next_sibling('div')
                return txt(d), txt(sib)
        return '', ''
    off_l, off_t = labelled('Texte officiel')
    if not off_t: off_l, off_t = labelled("L'essentiel")
    _, cas = labelled('Cas pratique')
    _, piege = labelled('Piège')
    q = r = ''
    for d in soup.find_all('div'):
        t = txt(d)
        if t.startswith('Q.') and len(d.find_all('div')) == 0: q = t[2:].strip()
        if t.startswith('R.') and len(d.find_all('div')) == 0: r = t[2:].strip()
    sec = [txt(d.find('span')) for d in soup.find_all('div') if 'Space Grotesk' in (d.get('style') or '') and 'uppercase' in (d.get('style') or '') and d.find('span')]
    src = [txt(d) for d in soup.find_all('div') if txt(d).startswith('Source vérifiable') and not d.find('div')]
    out.append(dict(n=int(m.group(1)), part=m.group(2), title=txt(h1), ar=txt(ar), pills=pills, off_label=off_l, off_text=off_t, cas=cas, piege=piege, q=q, r=r, sections=sec, source=src[0] if src else '', text=txt(soup)))
json.dump(out, open(D + '/fiches.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for o in out:
    print(o['n'], '|', o['part'], '|', o['title'], '|', o['ar'], '|', o['pills'], '|', o['sections'])
    print('   OFF:', o['off_label'], '::', o['off_text'][:90]); print('   Q:', o['q'][:100], '|| R:', o['r'][:80]); print('   CAS:', o['cas'][:80], '|| PIEGE:', o['piege'][:60]); print('   SRC:', o['source'][:120])
