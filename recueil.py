#!/usr/bin/env python3
"""Fabrique le recueil des études : pages de présentation + PDF des études, en un seul fichier.
Usage : python3 recueil.py   (nécessite node + playwright pour les pages de présentation, et pdfunite)"""
import html, os, subprocess, tempfile, runpy
ROOT = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(ROOT, "contenu.py"))
AUTHOR, ORCID, SITE, e = g["AUTHOR"], g["ORCID"], g["SITE"], html.escape
# Le recueil est en français : on aplatit les champs bilingues.
P = [dict(p, type=p["type"]["fr"], date_fr=p["date_txt"]["fr"], title=p["title"]["fr"], subtitle=p["subtitle"]["fr"], comment=p["comment"]["fr"], points=p["points"]["fr"],
          readers=p["readers"]["fr"], resume=p["abstract"]["fr"], cite=f"Boutchakkoucht, H. ({p['year']}). <i>{html.escape(p['cite_title'])}</i>. {p['cite_tail']['fr']}") for p in g["PUBLICATIONS"]]
css = """@page{size:A4;margin:24mm 22mm}body{font:11.5pt/1.6 Georgia,'Times New Roman',serif;color:#1B1A17;margin:0}
h1{font:400 34pt/1.05 Georgia,serif;margin:0}h1 i{color:#7A1F2B}h2{font:400 20pt/1.15 Georgia,serif;margin:0 0 6pt}h3{font:700 8pt Arial,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#7A1F2B;margin:18pt 0 4pt}
.l{font:700 8pt Arial,sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#5F5A50}.sub{font-style:italic;color:#5F5A50;margin:0 0 10pt}
.cover{height:238mm;display:flex;flex-direction:column;justify-content:space-between;}.rule{border-top:1pt solid #7A1F2B;width:60mm;margin:14pt 0}
.toc td{padding:6pt 0;border-bottom:.5pt solid #ccc;vertical-align:top}.toc{width:100%;border-collapse:collapse}
.cite{font:9.5pt/1.5 Arial,sans-serif;border-left:2pt solid #B8862B;padding:6pt 10pt;background:#FAF6EE}li{margin:4pt 0}.small{font:9pt/1.5 Arial,sans-serif;color:#5F5A50}"""
def study(i, p):
    return f"""<div><p class="l">Étude {i} · {e(p['type'])} · {e(p['date_fr'])}</p><h2>{e(p['title'])}</h2><p class="sub">{e(p['subtitle'])}</p>
<h3>Commentaire</h3><p>{e(p['comment'])}</p><h3>Ce qu’il faut retenir</h3><ul>{''.join(f'<li>{e(x)}</li>' for x in p['points'])}</ul>
<h3>À qui s’adresse ce texte</h3><p>{e(p['readers'])}</p><h3>Résumé de l’auteur</h3><p>{e(p['resume'])}</p>
<h3>Pour citer</h3><p class="cite">{p['cite']}</p><p class="small">Le texte intégral ({p['pages']} pages) suit cette présentation.</p></div>"""
cover = f"""<div class="cover"><div><p class="l">Recueil des études</p><div class="rule"></div><h1>La norme <i>et le réel</i></h1><p class="sub" style="font-size:14pt;margin-top:10pt">Hafid Boutchakkoucht · Études et publications, avec commentaires</p></div>
<div><table class="toc">{''.join(f"<tr><td style='width:14mm' class='l'>{i}</td><td><b>{e(p['title'])}</b><br><span class='small'>{e(p['type'])} · {e(p['date_fr'])} · {p['pages']} pages</span></td></tr>" for i, p in enumerate(P, 1))}</table>
<p class="small" style="margin-top:14pt">ORCID {ORCID} · {SITE.replace('https://', '')}<br>Travaux personnels de l’auteur. Les analyses et opinions exprimées n’engagent que lui et ne sauraient être attribuées à l’association Cross Borders.<br>© {AUTHOR}. Tous droits réservés.</p></div></div>"""
js = "const{chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage();for(let i=1;i<process.argv.length;i+=2){await p.goto('file://'+process.argv[i]);await p.pdf({path:process.argv[i+1],format:'A4',printBackground:true})}await b.close()})()"
out = os.path.join(ROOT, "telechargements", "boutchakkoucht-recueil-des-etudes.pdf")
with tempfile.TemporaryDirectory() as d:
    blocks = [cover] + [study(i, p) for i, p in enumerate(P, 1)]
    args, pdfs = [], []
    for k, b in enumerate(blocks):
        h, f = os.path.join(d, f"{k}.html"), os.path.join(d, f"{k}.pdf")
        open(h, "w", encoding="utf-8").write(f'<meta charset="utf-8"><style>{css}</style>{b}')
        args += [h, f]; pdfs.append(f)
    subprocess.run(["node", "-e", js, *args], check=True)
    seq = [pdfs[0]]
    for i, p in enumerate(P, 1): seq += [pdfs[i], os.path.join(ROOT, "telechargements", p["pdf"])]
    subprocess.run(["pdfunite", *seq, out], check=True)
print("Recueil :", subprocess.run(["pdfinfo", out], capture_output=True, text=True).stdout.split("Pages:")[1].split()[0], "pages")
