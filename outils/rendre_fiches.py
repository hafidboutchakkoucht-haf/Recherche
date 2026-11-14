import re, glob, os, sys
SRC, OUT = sys.argv[1], sys.argv[2]
F = 'file://' + os.path.abspath('node_modules/@fontsource')
faces = []
for fam, pkg, subs, ws in [('Cairo', 'cairo', ['arabic', 'latin'], [600, 700]), ('Inter', 'inter', ['latin'], [400, 600, 700]), ('Space Grotesk', 'space-grotesk', ['latin'], [500, 700])]:
    for sub in subs:
        for w in ws:
            rng = 'unicode-range:U+0600-06FF,U+0750-077F,U+0870-088E,U+0890-0891,U+0897-08E1,U+08E3-08FF,U+200C-200E,U+2010-2011,U+204F,U+2E41,U+FB50-FDFF,U+FE70-FE74,U+FE76-FEFC;' if sub == 'arabic' else ''
            faces.append(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url({F}/{pkg}/files/{pkg}-{sub}-{w}-normal.woff2) format('woff2');{rng}}}")
css = '\n'.join(faces) + '\nbody{margin:0;background:#F6F1E6}a{color:#0E4A43}'
os.makedirs(OUT, exist_ok=True)
for f in sorted(glob.glob(SRC + '/project/*.dc.html')):
    s = open(f, encoding='utf-8').read()
    body = s[s.index('<x-dc>') + 6: s.index('</x-dc>')]
    body = re.sub(r'<helmet>.*?</helmet>', '', body, flags=re.S)
    name = os.path.basename(f).replace('.dc.html', '')
    open(f'{OUT}/{name}.html', 'w', encoding='utf-8').write(f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>')
print(len(glob.glob(OUT + '/*.html')), 'pages')
