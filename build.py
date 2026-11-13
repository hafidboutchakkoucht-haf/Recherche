#!/usr/bin/env python3
"""Génère le site Recherche (aucune dépendance).  Usage : python3 build.py

Pour ajouter une publication : ajouter un bloc dans PUBLICATIONS ci-dessous, puis relancer.
"""
import html, json, os

SITE = "https://recherche.crossborders.ngo"
AUTHOR = "Hafid Boutchakkoucht"
ORCID = "0009-0007-3785-5570"
EMAIL = "hafidboutchakkoucht@gmail.com"
MAIN_SITE = "https://www.crossborders.ngo"

PUBLICATIONS = [
    {
        "slug": "ingenierie-des-promesses",
        "year": "2026", "date": "2026-10-02", "date_fr": "2 octobre 2026",
        "type": "Note d’analyse stratégique", "field": "Politiques publiques",
        "title": "De l’ingénierie des promesses à l’ingénierie de l’État",
        "subtitle": "La faisabilité du programme du Parti Authenticité et Modernité pour la législature 2027–2031",
        "strap": "Économie politique, gouvernance de coalition et théorie de la mise en œuvre des politiques publiques",
        "resume": "La présente étude évalue la faisabilité du programme du Parti Authenticité et Modernité (PAM) pour la législature 2027–2031, à la lumière de la théorie de la mise en œuvre des politiques publiques (Pressman et Wildavsky, Lipsky, Tsebelis, Matland, Barber). En s’appuyant sur le programme officiel, sur le cadrage macroéconomique du projet de loi de finances 2027 et sur les séries du Haut-Commissariat au Plan, elle montre que le « dividende de croissance » de 300 milliards de dirhams suppose une croissance de référence de 1,3 % à 2 % seulement, et que l’objectif d’un million d’emplois nets repose sur une élasticité huit fois supérieure à celle observée en 2022–2025. Elle propose une architecture d’exécution et quatre scénarios à l’horizon 2031.",
        "abstract": "This study assesses the implementability of the Authenticity and Modernity Party’s (PAM) 2027–2031 programme in Morocco through the lens of implementation theory. Drawing on the party’s official programme, the 2027 budget framework and High Commission for Planning data, it finds that the claimed MAD 300 billion growth dividend implies a counterfactual growth rate of only 1.3–2%, and that the one-million-net-jobs target assumes an employment elasticity eight times higher than observed in 2022–2025. It proposes a delivery architecture and four scenarios for 2031.",
        "keywords": ["Maroc", "politiques publiques", "mise en œuvre", "gouvernement de coalition", "finances publiques", "test de résistance budgétaire", "emploi", "unité de mise en œuvre"],
        "toc": ["Problématique et thèse", "Le mandat du 23 septembre 2026 en chiffres", "Le laboratoire 2021–2026", "Cadre théorique", "L’ingénierie de coalition", "L’architecture constitutionnelle des compétences", "Test de résistance budgétaire", "Un million d’emplois", "Tests sectoriels", "L’ingénierie de l’exécution", "Calendrier, matrice des risques et tableau de bord", "Quatre scénarios à l’horizon 2031"],
        "pdf": "boutchakkoucht-2026-ingenierie-des-promesses.pdf", "pages": 41,
        "comment": "Cette note ne juge pas le programme sur ses intentions mais sur sa capacité à être exécuté. Sa thèse tient en une formule, le « paradoxe du mandat étroit et du programme large » : un programme conçu pour une majorité absolue devra être mis en œuvre par une coalition, avec un mandat électoral restreint et un premier budget préparé par le gouvernement sortant.",
        "points": ["Le coût annuel du programme (70 milliards de dirhams) dépasse à lui seul le déficit autorisé : chaque dépense nouvelle suppose une ressource nouvelle.",
                   "Le « dividende de croissance » de 300 milliards n’est atteint que si l’on suppose une économie quasi stagnante sans le programme.",
                   "L’objectif d’un million d’emplois repose sur une élasticité huit fois supérieure à celle que les chiffres du programme font eux-mêmes apparaître pour 2022–2025.",
                   "Tout se joue dans les cent premiers jours : un pacte de majorité conçu comme un contrat d’exécution, une annexe financière publique en trois scénarios, et une unité de mise en œuvre resserrée sur dix engagements."],
        "readers": "Décideurs publics, journalistes économiques, chercheurs en politiques publiques et étudiants en science politique.",
        "cite": "Boutchakkoucht, H. (2026). <i>De l’ingénierie des promesses à l’ingénierie de l’État : la faisabilité du programme du Parti Authenticité et Modernité pour la législature 2027–2031</i>. Note d’analyse stratégique, 2 octobre 2026.",
    },
    {
        "slug": "droit-penal-post-national",
        "year": "2025", "date": "2025", "date_fr": "Édition 2025",
        "type": "Traité", "field": "Droit pénal comparé",
        "title": "Traité de droit pénal comparé. Vers un droit pénal post-national ?",
        "subtitle": "Crise de la souveraineté territoriale et recomposition des cadres normatifs à l’ère des criminalités transnationales",
        "strap": "Analyse doctrinale, jurisprudentielle et comparée",
        "resume": "Ce traité part d’un constat que l’on formule rarement avec franchise dans la littérature académique : le droit pénal que nous enseignons, que nous appliquons et que nous réformons sans relâche depuis deux siècles est profondément inadapté au monde dans lequel nous vivons. Construit autour de la souveraineté territoriale de l’État, il se trouve confronté à des formes de criminalité qui ignorent les frontières, exploitent les failles de la coopération internationale et colonisent l’espace numérique avec une agilité que le droit ne possède pas encore. Ce travail est une tentative de penser le droit pénal à la hauteur de ces transformations — en partant des fondements philosophiques des grandes écoles pénales, en traversant le droit positif comparé et la jurisprudence européenne, pour aboutir à une thèse : celle de l’émergence nécessaire d’un paradigme post-national, fondé non sur la disparition de l’État mais sur la recomposition de sa souveraineté pénale dans un cadre multi-niveaux.",
        "abstract": "This treatise departs from a candour rarely found in academic writing: the criminal law we have taught, applied, and relentlessly reformed for two centuries is profoundly ill-adapted to the world we actually inhabit. Built around state territorial sovereignty, it confronts forms of criminality that ignore borders, exploit gaps in international cooperation, and colonise digital space with an agility the law has yet to match. This work is an attempt to think criminal law equal to these transformations — moving from the philosophical foundations of the major penal schools, through comparative positive law and European jurisprudence, toward a thesis: the necessary emergence of a post-national paradigm, grounded not in the disappearance of the state but in the recomposition of its penal sovereignty within a multi-level framework.",
        "keywords": ["droit pénal post-national", "souveraineté territoriale", "criminalités transnationales", "écoles pénales", "CEDH", "légalité criminelle", "procédure pénale comparée", "espace pénal européen", "intelligence artificielle", "Luhmann", "Delmas-Marty"],
        "toc": [],
        "pdf": "boutchakkoucht-2025-traite-droit-penal-compare.pdf", "pages": 24,
        "comment": "Ce texte prend le contre-pied d’un enseignement qui présente encore le droit pénal comme un édifice national achevé. Il part des grandes écoles pénales pour montrer que la territorialité, pilier du droit pénal moderne, ne suffit plus face à des criminalités qui se jouent entre plusieurs continents et dans l’espace numérique.",
        "points": ["Une partie préliminaire consacrée aux grandes écoles de pensée pénale, avec une leçon : se méfier des systèmes qui prétendent tout expliquer.",
                   "Un diagnostic : la crise structurelle d’un droit pénal bâti sur la souveraineté territoriale.",
                   "Un détour par le droit positif comparé et par l’espace pénal européen, jurisprudence de la CEDH à l’appui.",
                   "Une thèse : le droit pénal post-national n’est pas un droit pénal sans État, mais un droit où l’État devient un acteur parmi d’autres dans un cadre à plusieurs niveaux."],
        "readers": "Étudiants et chercheurs en droit pénal et en sciences criminelles, magistrats, avocats, praticiens de la coopération judiciaire.",
        "cite": "Boutchakkoucht, H. (2025). <i>Traité de droit pénal comparé. Vers un droit pénal post-national ? Crise de la souveraineté territoriale et recomposition des cadres normatifs à l’ère des criminalités transnationales</i>. Édition 2025.",
    },
]

AXES = [
    ("Droit pénal comparé et sciences criminelles", "Souveraineté territoriale, criminalités transnationales, espace pénal européen et jurisprudence de la Cour européenne des droits de l’homme."),
    ("Politiques publiques et mise en œuvre", "Faisabilité des programmes de gouvernement, gouvernance de coalition, finances publiques et architecture d’exécution."),
]

# Vidéos classées par thématique : (titre du thème, présentation, [(numéro d'épisode, titre, résumé)])
THEMES = [
    ("Comprendre le programme", "Ce qu’est Erasmus+, à qui il s’adresse et par où y entrer.", [
        (1, "Ce n’est pas que pour les étudiants", "Erasmus+ en chiffres : qui part, combien, et pourquoi les jeunes hors université sont concernés."),
        (2, "Trois portes pour partir", "Échanges de jeunes, mobilité des animateurs de jeunesse, DiscoverEU.")]),
    ("Inclusion et égalité des chances", "Ce que le programme prévoit pour celles et ceux qui partent le moins.", [
        (3, "Erasmus+ pour toutes et tous", "Les jeunes ayant moins d’opportunités, les quatre priorités du programme, et ce que cela donne sur le terrain.")]),
    ("Ingénierie de projet", "La méthode pour une association qui veut porter son premier projet européen.", [
        (4, "Monter un projet en 6 étapes", "Du besoin de départ à la diffusion des résultats, et les erreurs à éviter.")]),
    ("Retours de terrain", "Ce que les projets produisent concrètement.", [
        (5, "Cross Borders en action", "Les rendez-vous de 2025 et 2026, ce que les jeunes ont produit, et la suite.")]),
]

e = html.escape
DISCLAIMER = "Travaux personnels de Hafid Boutchakkoucht. Les analyses et opinions exprimées sur ce site n’engagent que leur auteur et ne sauraient être attribuées à l’association Cross Borders."


def page(path, title, desc, body, head_extra="", root=""):
    url = f"{SITE}/{path}"
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="{AUTHOR}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/portrait.jpg">
<meta name="theme-color" content="#7A1F2B">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='10' fill='%237A1F2B'/%3E%3Ctext x='50%25' y='57%25' text-anchor='middle' dominant-baseline='middle' font-family='Georgia,serif' font-style='italic' font-size='34' fill='%23F6F2EA'%3EHB%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="{root}assets/style.css">
{head_extra}
</head>
<body>
<header class="top"><div class="wrap">
  <a class="sig" href="{root or './'}">Hafid <b>Boutchakkoucht</b></a>
  <nav aria-label="Navigation principale"><a href="{root or './'}#axes">Axes</a><a href="{root or './'}#publications">Publications</a><a href="{root or './'}#videos">Vidéos</a><a href="{root or './'}#contact">Contact</a><a href="{MAIN_SITE}">Cross Borders ↗</a></nav>
</div></header>
<main>
{body}
</main>
<footer><div class="wrap">
  <p><strong>{AUTHOR}</strong> · ORCID <a href="https://orcid.org/{ORCID}" rel="me">{ORCID}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p>{DISCLAIMER}</p>
  <p>© {AUTHOR}. Tous droits réservés. Les textes peuvent être cités avec mention de l’auteur et de la source. Site sans cookie ni traceur.</p>
</div></footer>
</body>
</html>
"""
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), path, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)


def kw(p):
    return '<ul class="kw" aria-label="Mots-clés">' + "".join(f"<li>{e(k)}</li>" for k in p["keywords"]) + "</ul>"


# ── Accueil
pubs = "".join(f"""
  <article class="pub">
    <div class="meta"><span class="year">{p['year']}</span><span class="label">{e(p['type'])}</span><span class="label">{e(p['field'])}</span></div>
    <div>
      <h3><a href="publications/{p['slug']}/">{e(p['title'])}</a></h3>
      <p class="sub">{e(p['subtitle'])}</p>
      <p>{e(p['resume'])}</p>
      {kw(p)}
      <div class="comment"><p class="label">Commentaire</p><p>{e(p['comment'])}</p></div>
      <details><summary>Abstract (English)</summary><p lang="en">{e(p['abstract'])}</p></details>
      <details><summary>Citer cette publication</summary><p class="cite">{p['cite']}</p></details>
      <p class="dl"><a class="chip fill" href="telechargements/{p['pdf']}" download>Télécharger le PDF · {p['pages']} pages</a><a class="chip" href="publications/{p['slug']}/">Lire la présentation</a></p>
    </div>
  </article>""" for p in PUBLICATIONS)

reels = "".join(f"""
  <div class="theme">
    <div class="meta"><p class="label">Thème {n}</p><h3>{e(t)}</h3><p>{e(d)}</p></div>
    <div class="reels">""" + "".join(f"""
      <figure><video controls playsinline preload="none" poster="videos/erasmus-decrypte-ep{i}.jpg" aria-label="Épisode {i} : {e(tt)}"><source src="videos/erasmus-decrypte-ep{i}.mp4" type="video/mp4"></video><figcaption><strong>Épisode {i} · {e(tt)}</strong>{e(dd)}<a href="videos/erasmus-decrypte-ep{i}.mp4" download>Télécharger</a></figcaption></figure>""" for i, tt, dd in eps) + """
    </div>
  </div>""" for n, (t, d, eps) in enumerate(THEMES, 1))

person = {"@context": "https://schema.org", "@type": "Person", "name": AUTHOR, "url": SITE + "/", "image": SITE + "/assets/portrait.jpg",
          "jobTitle": "Chercheur en droit pénal comparé et sciences criminelles", "identifier": f"https://orcid.org/{ORCID}",
          "sameAs": [f"https://orcid.org/{ORCID}"], "knowsAbout": [a for a, _ in AXES], "affiliation": {"@type": "NGO", "name": "Cross Borders", "url": MAIN_SITE}}

page("", f"{AUTHOR} — Recherche, publications et vidéos",
     "Travaux de recherche de Hafid Boutchakkoucht : droit pénal comparé, sciences criminelles, politiques publiques. Publications, résumés et vidéos.",
     f"""<div class="wrap">
  <div class="hero">
    <div>
      <p class="label">Recherche · Publications · Vidéos</p>
      <h1>Hafid <em class="t">Boutchakkoucht</em></h1>
      <p class="lead">Chercheur en droit pénal comparé et sciences criminelles. J’étudie ce que les frontières font au droit, et ce que les programmes politiques deviennent lorsqu’il faut les exécuter.</p>
      <div class="ids"><a class="chip fill" href="#publications">Publications</a><a class="chip" href="https://orcid.org/{ORCID}" rel="me">ORCID {ORCID}</a><a class="chip" href="#contact">Contact</a></div>
    </div>
    <figure><img src="assets/portrait.jpg" alt="Portrait de Hafid Boutchakkoucht" width="700" height="700"><figcaption>Fondateur et président de l’association <a href="{MAIN_SITE}">Cross Borders</a></figcaption></figure>
  </div>
</div>

<section id="axes"><div class="wrap">
  <div class="head"><p class="label">01 · Axes de recherche</p><h2>Deux terrains, <em class="t">une même question</em> : comment la norme tient-elle face au réel ?</h2></div>
  <div class="axes">{''.join(f'<article><b>{chr(97 + i)}.</b><h3>{e(a)}</h3><p>{e(d)}</p></article>' for i, (a, d) in enumerate(AXES))}</div>
</div></section>

<section id="publications"><div class="wrap">
  <div class="head"><p class="label">02 · Études et publications</p><div><h2>Travaux <em class="t">récents</em></h2>
  <p style="color:var(--muted);margin-top:1em;max-width:40rem">Chaque étude est présentée avec un commentaire et se télécharge en PDF. Le recueil réunit l’ensemble en un seul fichier.</p>
  <p class="dl"><a class="chip fill" href="telechargements/boutchakkoucht-recueil-des-etudes.pdf" download>Télécharger le recueil complet (PDF)</a></p></div></div>{pubs}
</div></section>

<section id="videos"><div class="wrap">
  <div class="head"><p class="label">03 · Vidéos</p><div><h2>Erasmus+ décrypté, <em class="t">en une minute</em></h2><p style="color:var(--muted);margin-top:1em;max-width:40rem">Une série de cinq épisodes courts réalisée pour l’association Cross Borders, pour expliquer le programme Erasmus+ sans jargon. Les épisodes sont classés par thématique.</p></div></div>{reels}
</div></section>

<section id="contact"><div class="wrap">
  <div class="head"><p class="label">04 · Contact</p><div><h2>Échanger, <em class="t">citer, inviter</em></h2>
  <p style="margin-top:1em;max-width:40rem">Pour réagir à une publication, proposer une collaboration, une intervention ou un entretien : <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></div>
</div></section>""",
     head_extra=f'<script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>')

# ── Une page par publication (balises citation_* pour Google Scholar)
for p in PUBLICATIONS:
    full = f"{p['title']} : {p['subtitle']}" if not p['title'].endswith("?") else f"{p['title']} {p['subtitle']}"
    metas = "\n".join([
        f'<meta name="citation_title" content="{e(full)}">', f'<meta name="citation_author" content="Boutchakkoucht, Hafid">',
        f'<meta name="citation_author_orcid" content="{ORCID}">', f'<meta name="citation_publication_date" content="{p["date"].replace("-", "/")}">',
        f'<meta name="citation_language" content="fr">', f'<meta name="citation_keywords" content="{e("; ".join(p["keywords"]))}">',
        f'<meta name="citation_abstract_html_url" content="{SITE}/publications/{p["slug"]}/">', f'<meta name="citation_pdf_url" content="{SITE}/telechargements/{p["pdf"]}">',
        '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "ScholarlyArticle", "headline": full, "name": full, "inLanguage": "fr",
            "datePublished": p["date"], "abstract": p["resume"], "keywords": p["keywords"], "url": f"{SITE}/publications/{p['slug']}/",
            "author": {"@type": "Person", "name": AUTHOR, "identifier": f"https://orcid.org/{ORCID}", "url": SITE + "/"}}, ensure_ascii=False) + "</script>"])
    toc = ('<h2>Sommaire</h2><ol class="toc">' + "".join(f"<li>{e(t)}</li>" for t in p["toc"]) + "</ol>") if p["toc"] else ""
    subject = f"À propos de : {p['title']}".replace(" ", "%20")
    page(f"publications/{p['slug']}", f"{p['title']} — {AUTHOR}", p["resume"][:155].rsplit(" ", 1)[0] + "…",
         f"""<div class="wrap article">
  <p class="label"><a href="../../#publications">← Publications</a> · {e(p['type'])} · {e(p['field'])}</p>
  <h1 style="margin-top:.5em">{e(p['title'])}</h1>
  <p class="sub">{e(p['subtitle'])}</p>
  <dl class="facts"><div><dt>Auteur</dt><dd>{AUTHOR}</dd></div><div><dt>Parution</dt><dd>{e(p['date_fr'])}</dd></div><div><dt>Nature</dt><dd>{e(p['type'])}</dd></div><div><dt>Approche</dt><dd>{e(p['strap'])}</dd></div></dl>
  <div class="body">
    <p class="dl" style="margin-top:0"><a class="chip fill" href="../../telechargements/{p['pdf']}" download>Télécharger le PDF · {p['pages']} pages</a></p>
    <h2>Commentaire</h2><p>{e(p['comment'])}</p>
    <h2>Ce qu’il faut retenir</h2><ul class="points">{''.join(f'<li>{e(x)}</li>' for x in p['points'])}</ul>
    <h2>À qui s’adresse ce texte</h2><p>{e(p['readers'])}</p>
    <h2>Résumé</h2><p>{e(p['resume'])}</p>
    <h2>Abstract</h2><p lang="en">{e(p['abstract'])}</p>
    {kw(p)}
    {toc}
    <h2>Citer cette publication</h2><p class="cite">{p['cite']}</p>
    <h2>Texte intégral</h2>
    <p class="dl"><a class="chip fill" href="../../telechargements/{p['pdf']}" download>Télécharger le PDF · {p['pages']} pages</a><a class="chip" href="mailto:{EMAIL}?subject={subject}">Écrire à l’auteur</a></p>
  </div>
</div>""", head_extra=metas, root="../../")

root = os.path.dirname(os.path.abspath(__file__))
open(os.path.join(root, "CNAME"), "w").write("recherche.crossborders.ngo\n")
open(os.path.join(root, ".nojekyll"), "w").write("")
urls = [SITE + "/"] + [f"{SITE}/publications/{p['slug']}/" for p in PUBLICATIONS]
open(os.path.join(root, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
open(os.path.join(root, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
print("OK —", len(urls), "pages")
