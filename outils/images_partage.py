#!/usr/bin/env python3
"""Fabrique une image de partage (1200 x 630) par étude, dans assets/og/<slug>.png.
Usage : python3 outils/images_partage.py   (nécessite node + playwright). Relancer après l'ajout d'une étude."""
import html, os, runpy, subprocess, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
g = runpy.run_path(os.path.join(ROOT, "contenu.py"))
e = html.escape
OUT = os.path.join(ROOT, "assets", "og")
os.makedirs(OUT, exist_ok=True)
CSS = """*{box-sizing:border-box}body{margin:0;width:1200px;height:630px;background:#F6F2EA;color:#1B1A17;font-family:'Iowan Old Style','Palatino Linotype',Palatino,'TeX Gyre Pagella',Georgia,serif;position:relative;overflow:hidden}
.band{position:absolute;left:0;top:0;bottom:0;width:14px;background:#7A1F2B}
.in{position:absolute;left:84px;right:84px;top:64px;bottom:58px;display:flex;flex-direction:column}
.k{font:600 17px/1.4 system-ui,'Inter','DejaVu Sans',sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#7A1F2B}
h1{font-weight:500;font-size:58px;line-height:1.08;margin:26px 0 0;letter-spacing:-.01em}
.s{font-style:italic;font-size:26px;line-height:1.35;color:#5F5A50;margin:22px 0 0}
.f{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;border-top:1.5px solid #B8862B;padding-top:20px}
.a{font-size:28px}.a small{display:block;font:500 16px/1.5 system-ui,'Inter','DejaVu Sans',sans-serif;color:#5F5A50;letter-spacing:.04em;margin-top:4px}
.m{font:600 16px/1.4 system-ui,'Inter','DejaVu Sans',sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#5F5A50;text-align:right}"""
js = "const{chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630}});for(let i=1;i<process.argv.length;i+=2){await p.goto('file://'+process.argv[i]);await p.screenshot({path:process.argv[i+1]})}await b.close()})()"
with tempfile.TemporaryDirectory() as d:
    args = []
    for p in g["PUBLICATIONS"]:
        t = p["title"]["fr"]
        size = 58 if len(t) < 70 else 50
        doc = f"""<meta charset="utf-8"><style>{CSS}</style><div class="band"></div><div class="in">
<p class="k">{e(p['type']['fr'])} · {e(p['date_txt']['fr'])}</p><h1 style="font-size:{size}px">{e(t)}</h1><p class="s">{e(p['subtitle']['fr'])}</p>
<div class="f"><div class="a">{g['AUTHOR']}<small>ORCID {g['ORCID']}</small></div><div class="m">La norme et le réel<br>{p['pages']} pages · PDF</div></div></div>"""
        h = os.path.join(d, p["slug"] + ".html")
        open(h, "w", encoding="utf-8").write(doc)
        args += [h, os.path.join(OUT, p["slug"] + ".png")]
    subprocess.run(["node", "-e", js, *args], check=True)
print("Images :", ", ".join(sorted(os.listdir(OUT))))
