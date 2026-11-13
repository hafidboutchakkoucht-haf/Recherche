#!/usr/bin/env python3
"""Génère le site « La norme et le réel » (aucune dépendance).  Usage : python3 build.py
Le contenu se modifie dans contenu.py, la mise en page dans assets/style.css."""
import html, json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from contenu import *  # noqa: E402,F401,F403

e = html.escape
LANGS = ["fr", "en", "es", "ar"]
RTL = {"ar"}
UI = {
    "fr": dict(axes="Axes", library="Bibliothèque", about="À propos", contact="Contact", skip="Aller au contenu", theme="Changer de thème clair ou sombre", other="Read in English",
               kicker="Carnet de recherche · Études et publications", lead="Ce que les frontières font au droit, et ce que les programmes politiques deviennent lorsqu’il faut les exécuter.",
               cta1="Explorer la bibliothèque", cta2="Télécharger le recueil", role="Chercheur en droit pénal comparé et sciences criminelles",
               n_studies="études publiées", n_pages="pages en accès libre", n_videos="vidéos pédagogiques", n_dl="formats de citation", n_axes="axes de recherche",
               axes_k="01 · Axes de recherche", axes_h="Deux terrains, <em>une même question</em> : comment la norme tient-elle face au réel ?",
               lib_k="02 · Bibliothèque", lib_h="Études et <em>commentaires</em>", lib_p="Chaque étude est commentée et se télécharge en PDF. Filtrez par thème ou cherchez un mot.",
               search="Rechercher un titre, un mot-clé…", all="Tout", studies="Études", videos="Vidéos", none="Aucun résultat pour cette recherche.",
               study="Étude", video="Vidéo", minute="1 min", read="Lire la présentation", pdf="Télécharger le PDF", pages="pages", watch="Regarder", download="Télécharger",
               comment="Commentaire", recueil_h="Le recueil des études", recueil_p="Toutes les études réunies en un seul PDF, chacune précédée de son commentaire.", recueil_b="Télécharger le recueil (PDF)",
               about_k="03 · À propos", about_h="L’auteur, <em>en bref</em>", portrait="Télécharger le portrait", orcid="Profil ORCID",
               contact_k="04 · Contact", contact_h="Échanger, <em>citer, inviter</em>", contact_p="Pour réagir à une publication, proposer une collaboration, une intervention ou un entretien :",
               back="← Bibliothèque", author="Auteur", published="Parution", nature="Nature", approach="Approche", language="Langue",
               keyfig="L’étude en chiffres", keyfig_n="Chiffres tirés de l’étude.", takeaways="Ce qu’il faut retenir", readers="À qui s’adresse ce texte", abstract="Résumé", abstract_other="Abstract (English)",
               outline="Plan de l’étude", keywords="Mots-clés", cite="Citer cette étude", copy="Copier la référence", copied="Référence copiée", reader="Lire en ligne", reader_n="Si le lecteur ne s’affiche pas sur votre appareil, utilisez le bouton de téléchargement.",
               write="Écrire à l’auteur", next="Autre étude", rights="Tous droits réservés. Les textes peuvent être cités avec mention de l’auteur et de la source. Site sans cookie ni traceur.", series="Série Erasmus+ décrypté · en français"),
    "en": dict(axes="Research", library="Library", about="About", contact="Contact", skip="Skip to content", theme="Toggle light or dark theme", other="Lire en français",
               kicker="Research notebook · Studies and publications", lead="What borders do to law, and what political programmes become when they have to be implemented.",
               cta1="Explore the library", cta2="Download the collection", role="Researcher in comparative criminal law and criminal sciences",
               n_studies="published studies", n_pages="open-access pages", n_videos="educational videos", n_dl="citation formats", n_axes="research areas",
               axes_k="01 · Research areas", axes_h="Two fields, <em>one question</em>: how does the norm hold up against reality?",
               lib_k="02 · Library", lib_h="Studies and <em>commentary</em>", lib_p="Each study comes with a commentary and a PDF download. Filter by topic or search for a word.",
               search="Search a title or keyword…", all="All", studies="Studies", videos="Videos", none="No result for this search.",
               study="Study", video="Video", minute="1 min", read="Read the overview", pdf="Download the PDF", pages="pages", watch="Watch", download="Download",
               comment="Commentary", recueil_h="The collected studies", recueil_p="All studies in a single PDF, each preceded by its commentary (in French).", recueil_b="Download the collection (PDF)",
               about_k="03 · About", about_h="The author, <em>in brief</em>", portrait="Download the portrait", orcid="ORCID profile",
               contact_k="04 · Contact", contact_h="Discuss, <em>cite, invite</em>", contact_p="To respond to a publication, or to propose a collaboration, a talk or an interview:",
               back="← Library", author="Author", published="Published", nature="Type", approach="Approach", language="Language",
               keyfig="The study in figures", keyfig_n="Figures taken from the study.", takeaways="Key takeaways", readers="Who this text is for", abstract="Abstract", abstract_other="Résumé (français)",
               outline="Outline", keywords="Keywords", cite="Cite this study", copy="Copy the reference", copied="Reference copied", reader="Read online", reader_n="If the reader does not display on your device, use the download button.",
               write="Write to the author", next="Another study", rights="All rights reserved. Texts may be quoted with attribution to the author and source. No cookies, no trackers.", series="Erasmus+ décrypté series · in French"),
}
PUB_DIR = {"fr": "publications", "en": "en/publications", "es": "es/publicaciones", "ar": "ar/publications"}
HOME = {"fr": "", "en": "en", "es": "es", "ar": "ar"}
import traductions  # noqa: E402
traductions.apply(globals())
from videotheque import VID_DIR, UI_V, RUBRIQUES, FILM_URL  # noqa: E402
for _l in LANGS:
    UI[_l]["about_k"] = UI_V[_l]["about_k"]
    UI[_l]["contact_k"] = UI_V[_l]["contact_k"]
    UI[_l]["n_videos"] = {"fr": "vidéos d’analyse", "en": "analysis videos", "es": "vídeos de análisis", "ar": "فيديو تحليلي"}[_l]


def cite_text(p, lang):
    return f"Boutchakkoucht, H. ({p['year']}). <i>{e(p['cite_title'])}</i>. {e(p['cite_tail'][lang])} {SITE}/publications/{p['slug']}/"


def norm_real_svg():
    """Motif du titre : des lignes droites (la norme) qui deviennent des courbes (le réel)."""
    rows = []
    for i in range(9):
        y = 22 + i * 22
        amp = 3 + i * 1.6
        d = f"M0 {y} H150 C190 {y} 200 {y - amp * 2} 235 {y - amp} S290 {y + amp * 2.2} 330 {y + amp * 0.4} S395 {y - amp * 1.8} 440 {y + amp * 0.6}"
        rows.append(f'<path d="{d}" style="animation-delay:{i * .08:.2f}s"/>')
    return f'<svg class="motif" viewBox="0 0 440 220" aria-hidden="true">{"".join(rows)}<path class="axis" d="M150 6V214"/></svg>'


def write(path, content):
    out = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out) or ROOT, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(content)


def page(lang, path, alt_paths, title, desc, body, head_extra=""):
    u = UI[lang]
    depth = len([s for s in path.split("/") if s])
    root = "../" * depth
    home = root + (HOME[lang] + "/" if HOME[lang] else "") or "./"
    url = f"{SITE}/{path + '/' if path else ''}"
    alts = {l: f"{SITE}/{a + '/' if a else ''}" for l, a in alt_paths.items()}
    switch = "".join(f'<a class="tool" href="{root}{alt_paths[l] + "/" if alt_paths[l] else ""}" hreflang="{l}" lang="{l}" aria-label="{UI[l]["lang_name"]}">{UI[l]["lang_label"]}</a>' for l in LANGS if l != lang)
    if path == "": switch = switch.replace('href=""', 'href="./"')
    doc = f"""<!doctype html>
<html lang="{lang}" dir="{'rtl' if lang in RTL else 'ltr'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="author" content="{AUTHOR}">
<link rel="canonical" href="{url}">
{"".join(f'<link rel="alternate" hreflang="{l}" href="{alts[l]}">' + chr(10) for l in LANGS).rstrip()}
<link rel="alternate" hreflang="x-default" href="{alts['fr']}">
<link rel="alternate" type="application/atom+xml" title="{e(SITE_TITLE['fr'])}" href="{SITE}/feed.xml">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(SITE_TITLE[lang])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#7A1F2B">
<link rel="icon" href="{root}assets/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{root}assets/style.css">
<script>document.documentElement.classList.add('js');try{{var t=localStorage.getItem('nr-theme');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
{head_extra}
</head>
<body>
<a class="skip" href="#main">{u['skip']}</a>
<header class="top"><div class="wrap">
  <a class="sig" href="{home}"><span>{e(SITE_TITLE[lang])}</span><b>{AUTHOR}</b></a>
  <nav aria-label="{u['library']}"><a href="{home}#axes">{u['axes']}</a><a href="{home}#bibliotheque">{u['library']}</a><a href="{root}{VID_DIR[lang]}/">{UI_V[lang]['nav']}</a><a href="{home}#a-propos">{u['about']}</a><a href="{home}#contact">{u['contact']}</a></nav>
  <div class="tools">{switch}<button class="tool" type="button" data-theme aria-label="{u['theme']}"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="5"/><path d="M12 1v3M12 20v3M1 12h3M20 12h3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/></svg></button></div>
  <div class="bar" aria-hidden="true"></div>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap">
  <p><strong>{e(SITE_TITLE[lang])}</strong> · {AUTHOR} · ORCID <a href="https://orcid.org/{ORCID}" rel="me">{ORCID}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="{MAIN_SITE}">Cross Borders ↗</a></p>
  <p>{e(DISCLAIMER[lang])}</p>
  <p>© {AUTHOR}. {u['rights']}</p>
</div></footer>
<script src="{root}assets/app.js" defer></script>
</body>
</html>
"""
    write(os.path.join(path, "index.html"), doc)


def home(lang):
    u = UI[lang]
    r = "" if lang == "fr" else "../"
    total_pages = sum(p["pages"] for p in PUBLICATIONS)
    n_videos = sum(len(v) for _, v in VIDEO_THEMES) + count_videos()
    cards = []
    for p in PUBLICATIONS:
        link = f"{r}{PUB_DIR[lang]}/{p['slug']}/"
        hay = " ".join([p["title"][lang], p["subtitle"][lang], " ".join(p["keywords"][lang]), p["type"][lang]])
        cards.append(f"""
    <article class="item study rv" data-item data-kind="study" data-topic="{p['topic']}" data-text="{e(hay.lower())}">
      <div class="meta"><span class="year">{p['year']}</span><span class="label">{e(p['type'][lang])}</span><span class="tag">{e(TOPICS[p['topic']][lang])}</span></div>
      <div>
        <h3><a href="{link}">{e(p['title'][lang])}</a></h3>
        <p class="sub">{e(p['subtitle'][lang])}</p>
        <div class="comment"><p class="label">{u['comment']}</p><p>{e(p['comment'][lang])}</p></div>
        <ul class="kw">{''.join(f'<li>{e(k)}</li>' for k in p['keywords'][lang][:6])}</ul>
        <p class="dl"><a class="chip fill" href="{link}">{u['read']}</a><a class="chip" href="{r}telechargements/{p['pdf']}" download>{u['pdf']} · {p['pages']} {u['pages']}</a></p>
      </div>
    </article>""")
    for theme, eps in VIDEO_THEMES:
        for n, t, d in eps:
            cards.append(f"""
    <article class="item vid rv" data-item data-kind="video" data-topic="europe" data-text="{e((t[lang] + ' ' + d[lang] + ' ' + theme[lang] + ' erasmus').lower())}">
      <video controls playsinline preload="none" poster="{r}videos/erasmus-decrypte-ep{n}.jpg" aria-label="{e(t[lang])}"><source src="{r}videos/erasmus-decrypte-ep{n}.mp4" type="video/mp4"></video>
      <div><p class="label">{u['video']} · {e(theme[lang])}</p><h3>{e(t[lang])}</h3><p class="sub">{e(d[lang])}</p><p class="small">{u['series']} · <a href="{r}videos/erasmus-decrypte-ep{n}.mp4" download>{u['download']}</a></p></div>
    </article>""")
    filters = f'<button class="f" type="button" data-f="all" aria-pressed="true">{u["all"]}</button>' + (f'<button class="f" type="button" data-f="kind:study" aria-pressed="false">{u["studies"]}</button><button class="f" type="button" data-f="kind:video" aria-pressed="false">{u["videos"]}</button>' if n_videos else "") + "".join(
        f'<button class="f" type="button" data-f="topic:{k}" aria-pressed="false">{e(v[lang])}</button>' for k, v in TOPICS.items())
    person = {"@context": "https://schema.org", "@type": "Person", "name": AUTHOR, "url": SITE + "/", "image": SITE + "/assets/portrait.jpg", "jobTitle": UI[lang]["role"],
              "identifier": f"https://orcid.org/{ORCID}", "sameAs": [f"https://orcid.org/{ORCID}"], "description": BIO[lang], "knowsAbout": [a[lang][0] for a in AXES],
              "affiliation": {"@type": "NGO", "name": "Cross Borders", "url": MAIN_SITE}}
    title_html = u["title_html"]
    body = f"""<div class="wrap hero">
  <div>
    <p class="label">{u['kicker']}</p>
    <h1>{title_html}</h1>
    <p class="byline">{AUTHOR}</p>
    <p class="lead">{e(u['lead'])}</p>
    <p class="dl"><a class="chip fill" href="#bibliotheque">{u['cta1']}</a><a class="chip" href="{r}telechargements/boutchakkoucht-recueil-des-etudes.pdf" download>{u['cta2']}</a></p>
  </div>
  <div class="art">{norm_real_svg()}<p class="legend"><span>{u['norm']}</span><span>{u['real']}</span></p></div>
</div>
<div class="wrap"><dl class="stats rv">
  <div><dt>{len(PUBLICATIONS)}</dt><dd>{u['n_studies']}</dd></div><div><dt>{total_pages}</dt><dd>{u['n_pages']}</dd></div>{f"<div><dt>{n_videos}</dt><dd>{u['n_videos']}</dd></div>" if n_videos else f"<div><dt>2</dt><dd>{u['n_dl']}</dd></div>"}<div><dt>{len(AXES)}</dt><dd>{u['n_axes']}</dd></div>
</dl></div>

<section id="axes"><div class="wrap">
  <div class="head"><p class="label">{u['axes_k']}</p><h2>{u['axes_h']}</h2></div>
  <div class="axes">{''.join(f'<article class="rv"><b>{chr(97 + i)}.</b><h3>{e(a[lang][0])}</h3><p>{e(a[lang][1])}</p></article>' for i, a in enumerate(AXES))}</div>
</div></section>

<section id="bibliotheque"><div class="wrap" data-library>
  <div class="head"><p class="label">{u['lib_k']}</p><div><h2>{u['lib_h']}</h2><p class="intro">{u['lib_p']}</p></div></div>
  <div class="toolbar"><input class="search" type="search" placeholder="{u['search']}" aria-label="{u['search']}"><div class="filters">{filters}</div></div>
  <div class="items">{''.join(cards)}
  </div>
  <p class="empty" hidden>{u['none']}</p>
  <aside class="recueil rv"><div><p class="label">PDF · {total_pages + 5} {u['pages']}</p><h3>{u['recueil_h']}</h3><p>{u['recueil_p']}</p></div><a class="chip fill" href="{r}telechargements/boutchakkoucht-recueil-des-etudes.pdf" download>{u['recueil_b']}</a></aside>
</div></section>

{videos_teaser(lang, r)}

<section id="a-propos"><div class="wrap">
  <div class="head"><p class="label">{u['about_k']}</p><h2>{u['about_h']}</h2></div>
  <div class="about rv"><figure><img src="{r}assets/portrait.jpg" alt="{AUTHOR}" width="700" height="700" loading="lazy"></figure>
  <div><p class="role">{e(u['role'])}</p><p>{e(BIO[lang])}</p>
  <p class="dl"><a class="chip" href="https://orcid.org/{ORCID}" rel="me">{u['orcid']} · {ORCID}</a><a class="chip" href="{r}assets/portrait.jpg" download="hafid-boutchakkoucht.jpg">{u['portrait']}</a><a class="chip" href="{MAIN_SITE}">Cross Borders ↗</a></p></div></div>
</div></section>

<section id="contact"><div class="wrap">
  <div class="head"><p class="label">{u['contact_k']}</p><div><h2>{u['contact_h']}</h2><p class="intro">{u['contact_p']} <a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div>
</div></section>"""
    page(lang, HOME[lang], HOME, f"{SITE_TITLE[lang]} — {AUTHOR}", BIO[lang][:158].rsplit(" ", 1)[0] + "…", body,
         head_extra=f'<script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>')


def count_videos():
    n = 0
    for rb in RUBRIQUES:
        for s in rb["series"]:
            n += len(s["items"]) * len(s.get("langs", []))
    return n + 1  # + le film 16:9


def vfile(s, lang, n):
    return s["file"].format(lang=lang, n=n)


def videos_teaser(lang, r):
    v = UI_V[lang]
    n_series = sum(1 for rb in RUBRIQUES for s in rb["series"] if s["items"])
    rubs = "".join(f'<li><a href="{r}{VID_DIR[lang]}/#{rb["id"]}">{e(rb["name"][lang])}</a></li>' for rb in RUBRIQUES)
    return f"""<section id="videos"><div class="wrap">
  <div class="head"><p class="label">{v['home_k']}</p><div><h2>{v['home_h']}</h2><p class="intro">{e(v['home_p'])}</p></div></div>
  <div class="vteaser rv">
    <a class="vfilm" href="{r}{FILM_URL}{'?lang=ar' if lang == 'ar' else ''}"><img src="{r}media/videos/posters/film-interactif.jpg" alt="" width="1032" height="580" loading="lazy"><span class="vplay" aria-hidden="true"></span><span class="vcap"><span class="label">{v['featured']}</span><strong>{e(v['film_h'])}</strong></span></a>
    <div><ul class="vrubs">{rubs}</ul><p class="small">{count_videos()} {v['count_v']} · {n_series} {v['n_series']}</p><p class="dl"><a class="chip fill" href="{r}{VID_DIR[lang]}/">{v['home_b']}</a></p></div>
  </div>
</div></section>"""


def videos_page(lang):
    v = UI_V[lang]
    path = VID_DIR[lang]
    root = "../" * len(path.split("/"))
    first = "ar" if lang == "ar" else "fr"
    jump = "".join(f'<a class="f" href="#{rb["id"]}">{e(rb["name"][lang])}</a>' for rb in RUBRIQUES)
    film = f"""<div class="vfeature rv">
    <a class="vfilm" href="{root}{FILM_URL}{'?lang=ar' if lang == 'ar' else ''}"><img src="{root}media/videos/posters/film-interactif.jpg" alt="" width="1032" height="580" loading="lazy"><span class="vplay" aria-hidden="true"></span></a>
    <div><p class="label">{v['featured']}</p><h3>{e(v['film_h'])}</h3><p>{e(v['film_p'])}</p>
    <p class="dl"><a class="chip fill" href="{root}{FILM_URL}{'?lang=ar' if lang == 'ar' else ''}">{v['film_b']}</a><a class="chip" href="{root}{FILM_URL}{'' if lang == 'ar' else '?lang=ar'}">{v['film_b2']}</a></p></div>
  </div>
  <div class="vwide rv"><video controls playsinline preload="none" poster="{root}media/videos/posters/film-guerre-des-blocus.jpg"><source src="{root}media/videos/iran/film-guerre-des-blocus.mp4" type="video/mp4"></video>
    <div><p class="label">{v['film_v']}</p><p class="small">{e(v['film_v_p'])} · <a href="{root}media/videos/iran/film-guerre-des-blocus.mp4" download>{v['download']}</a></p></div></div>"""
    secs = []
    for i, rb in enumerate(RUBRIQUES):
        blocks = []
        for s in rb["series"]:
            if not s["items"]:
                blocks.append(f'<div class="vseries soon"><h3>{e(s["title"][lang])}</h3><span class="tag">{v["soon"]}</span></div>')
                continue
            langs = s["langs"]
            show = first if first in langs else langs[0]
            toggle = ""
            if len(langs) > 1:
                toggle = '<div class="filters vlang" role="group" aria-label="' + v["version"] + '">' + "".join(
                    f'<button class="f" type="button" data-vl="{l}" aria-pressed="{str(l == show).lower()}" lang="{l}">{v[l]}</button>' for l in langs) + "</div>"
            else:
                toggle = f'<span class="tag">{v["only_ar"]}</span>' if langs == ["ar"] and lang != "ar" else ""
            cards = []
            for l in langs:
                for n, title in s["items"]:
                    f = vfile(s, l, n)
                    src = f"{root}media/videos/{s['dir']}/{f}.mp4"
                    num = f'{v["episode"]} {n} · ' if n else ""
                    cards.append(f"""<article class="vcard" data-l="{l}"{'' if l == show else ' hidden'}><video controls playsinline preload="none" poster="{root}media/videos/posters/{f}.jpg" aria-label="{e(title[l])}"><source src="{src}" type="video/mp4"></video>
        <p class="label">{num.rstrip(' · ') if num else v['special']}</p><h4 lang="{l}" dir="{'rtl' if l == 'ar' else 'ltr'}">{e(title[l])}</h4><p class="small"><a href="{src}" download>{v['download']}</a></p></article>""")
            data = f'<p class="small">{v["data_note"]} : {e(s["data"][lang])}</p>' if s.get("data") else ""
            blocks.append(f"""<div class="vseries" data-series>
      <div class="vs-head"><div><h3>{e(s['title'][lang])}</h3><p>{e(s['about'][lang])}</p>{data}</div>{toggle}</div>
      <div class="vgrid">{''.join(cards)}</div></div>""")
        secs.append(f"""<section id="{rb['id']}"><div class="wrap">
  <div class="head"><p class="label">{i + 1:02d} · {e(rb['name'][lang])}</p><div><h2>{e(rb['name'][lang])}</h2><p class="intro">{e(rb['intro'][lang])}</p></div></div>
  {film if rb.get('film') else ''}
  {''.join(blocks)}
</div></section>""")
    body = f"""<div class="wrap vhero">
  <p class="label">{v['kicker']}</p>
  <h1>{v['h1']}</h1>
  <p class="lead">{e(v['lead'])}</p>
  <nav class="filters vjump" aria-label="{v['jump']}">{jump}</nav>
</div>
{''.join(secs)}"""
    page(lang, path, VID_DIR, f"{v['kicker']} — {AUTHOR} · {SITE_TITLE[lang]}", v["lead"][:155], body)


def publication(lang, p, nxt):
    u = UI[lang]
    other = "en" if lang == "fr" else "fr"
    note = f'<p class="small">{u["abstract_note"]}</p>' if u["abstract_note"] else ""
    path = f"{PUB_DIR[lang]}/{p['slug']}"
    root = "../" * len(path.split("/"))
    pdf = f"{root}telechargements/{p['pdf']}"
    metas = "\n".join([
        f'<meta name="citation_title" content="{e(p["cite_title"])}">', '<meta name="citation_author" content="Boutchakkoucht, Hafid">',
        f'<meta name="citation_author_orcid" content="{ORCID}">', f'<meta name="citation_publication_date" content="{p["date"].replace("-", "/")}">',
        '<meta name="citation_language" content="fr">', f'<meta name="citation_keywords" content="{e("; ".join(p["keywords"][lang]))}">',
        f'<meta name="citation_abstract_html_url" content="{SITE}/publications/{p["slug"]}/">', f'<meta name="citation_pdf_url" content="{SITE}/telechargements/{p["pdf"]}">',
        '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "ScholarlyArticle", "headline": p["title"][lang], "name": p["cite_title"], "inLanguage": "fr",
            "datePublished": p["date"], "abstract": p["abstract"][lang], "keywords": p["keywords"][lang], "url": f"{SITE}/{path}/", "numberOfPages": p["pages"],
            "encoding": {"@type": "MediaObject", "contentUrl": f"{SITE}/telechargements/{p['pdf']}", "encodingFormat": "application/pdf"},
            "author": {"@type": "Person", "name": AUTHOR, "identifier": f"https://orcid.org/{ORCID}", "url": SITE + "/"}}, ensure_ascii=False) + "</script>"])
    subject = f"{p['title'][lang]}".replace(" ", "%20").replace("?", "%3F")
    body = f"""<div class="wrap article">
  <p class="label"><a href="{root}{HOME[lang] + '/' if HOME[lang] else ''}#bibliotheque">{u['back']}</a> · {e(p['type'][lang])} · {e(TOPICS[p['topic']][lang])}</p>
  <h1>{e(p['title'][lang])}</h1>
  <p class="sub">{e(p['subtitle'][lang])}</p>
  <p class="dl"><a class="chip fill" href="{pdf}" download>{u['pdf']} · {p['pages']} {u['pages']}</a><a class="chip" href="#lecteur">{u['reader']}</a><a class="chip" href="#citer">{u['cite']}</a></p>
  <dl class="facts"><div><dt>{u['author']}</dt><dd>{AUTHOR}</dd></div><div><dt>{u['published']}</dt><dd>{e(p['date_txt'][lang])}</dd></div><div><dt>{u['nature']}</dt><dd>{e(p['type'][lang])}</dd></div><div><dt>{u['language']}</dt><dd>{e(p['lang_note'][lang])}</dd></div><div class="wide"><dt>{u['approach']}</dt><dd>{e(p['strap'][lang])}</dd></div></dl>

  <h2 class="sec">{u['keyfig']}</h2>
  <dl class="stats small-stats">{''.join(f'<div><dt>{e(v)}</dt><dd>{e(t[lang])}</dd></div>' for v, t in p['figures'])}</dl>
  <p class="small">{u['keyfig_n']}</p>

  <div class="cols">
    <div class="body">
      <h2 class="sec">{u['comment']}</h2><p class="big">{e(p['comment'][lang])}</p>
      <h2 class="sec">{u['takeaways']}</h2><ol class="points">{''.join(f'<li>{e(x)}</li>' for x in p['points'][lang])}</ol>
      <h2 class="sec">{u['readers']}</h2><p>{e(p['readers'][lang])}</p>
      <h2 class="sec">{u['abstract']}</h2><p>{e(p['abstract'][lang])}</p>{note}
      <details><summary>{u['abstract_other']}</summary><p lang="{other}" dir="ltr">{e(p['abstract'][other])}</p></details>
    </div>
    <aside>
      <h2 class="sec">{u['outline']}</h2><ol class="toc">{''.join(f'<li>{e(x)}</li>' for x in p['outline'][lang])}</ol>
      <h2 class="sec">{u['keywords']}</h2><ul class="kw">{''.join(f'<li>{e(k)}</li>' for k in p['keywords'][lang])}</ul>
    </aside>
  </div>

  <h2 class="sec" id="citer">{u['cite']}</h2>
  <p class="cite" id="ref" dir="ltr" lang="fr">{cite_text(p, 'fr' if lang in RTL else lang)}</p>
  <p class="dl"><button class="chip" type="button" data-copy="#ref" data-done="{u['copied']}">{u['copy']}</button><a class="chip" href="{root}telechargements/{p['slug']}.bib" download>BibTeX</a><a class="chip" href="{root}telechargements/{p['slug']}.ris" download>RIS (Zotero, EndNote)</a></p>

  <h2 class="sec" id="lecteur">{u['reader']}</h2>
  <object class="reader" data="{pdf}#view=FitH" type="application/pdf" aria-label="{e(p['title'][lang])}"><p>{u['reader_n']}</p></object>
  <p class="small">{u['reader_n']}</p>
  <p class="dl"><a class="chip fill" href="{pdf}" download>{u['pdf']}</a><a class="chip" href="mailto:{EMAIL}?subject={subject}">{u['write']}</a></p>

  <a class="next" href="../{nxt['slug']}/"><span class="label">{u['next']}</span><strong>{e(nxt['title'][lang])}</strong></a>
</div>"""
    page(lang, path, {l: f"{PUB_DIR[l]}/{p['slug']}" for l in LANGS}, f"{p['title'][lang]} — {AUTHOR} · {SITE_TITLE[lang]}", p["abstract"][lang][:155].rsplit(" ", 1)[0] + "…", body, head_extra=metas)


for lang in LANGS:
    videos_page(lang)
    home(lang)
    for i, p in enumerate(PUBLICATIONS):
        publication(lang, p, PUBLICATIONS[(i + 1) % len(PUBLICATIONS)])

# Fichiers de citation
for p in PUBLICATIONS:
    key = f"boutchakkoucht{p['year']}{p['slug'].split('-')[0]}"
    kind = "book" if p["type"]["fr"] == "Traité" else "techreport"
    extra = "  publisher = {Hafid Boutchakkoucht},\n" if kind == "book" else "  type = {Note d'analyse stratégique},\n  institution = {Hafid Boutchakkoucht},\n"
    write(f"telechargements/{p['slug']}.bib", f"@{kind}{{{key},\n  author = {{Boutchakkoucht, Hafid}},\n  title = {{{p['cite_title']}}},\n  year = {{{p['year']}}},\n{extra}  language = {{french}},\n  url = {{{SITE}/publications/{p['slug']}/}},\n  note = {{ORCID {ORCID}}}\n}}\n")
    ris = ["TY  - " + ("BOOK" if kind == "book" else "RPRT"), "AU  - Boutchakkoucht, Hafid", f"TI  - {p['cite_title']}", f"PY  - {p['year']}", f"DA  - {p['date'].replace('-', '/')}", "LA  - fr",
           f"AB  - {p['abstract']['fr']}"] + [f"KW  - {k}" for k in p["keywords"]["fr"]] + [f"UR  - {SITE}/publications/{p['slug']}/", f"L1  - {SITE}/telechargements/{p['pdf']}", "ER  - "]
    write(f"telechargements/{p['slug']}.ris", "\n".join(ris) + "\n")

# Fichiers techniques
write("CNAME", SITE.replace("https://", "") + "\n")
write(".nojekyll", "")
write("assets/icon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#7A1F2B"/><path d="M10 20h18c8 0 10-6 16-6s6 6 10 6M10 32h18c8 0 10 7 16 7s6-7 10-7M10 44h18c8 0 10-6 16-6s6 6 10 6" fill="none" stroke="#F6F2EA" stroke-width="3.2" stroke-linecap="round"/></svg>\n')
urls = [f"{SITE}/{HOME[l] + '/' if HOME[l] else ''}" for l in LANGS] + [f"{SITE}/{VID_DIR[l]}/" for l in LANGS] + [f"{SITE}/{FILM_URL}"] + [f"{SITE}/{PUB_DIR[l]}/{p['slug']}/" for l in LANGS for p in PUBLICATIONS]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{x}</loc></url>\n" for x in urls) + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
entries = "".join(f"""  <entry><title>{e(p['title']['fr'])}</title><link href="{SITE}/publications/{p['slug']}/"/><id>{SITE}/publications/{p['slug']}/</id><updated>{p['date'] if len(p['date']) > 4 else p['date'] + '-01-01'}T00:00:00Z</updated><summary>{e(p['comment']['fr'])}</summary></entry>\n""" for p in PUBLICATIONS)
write("feed.xml", f"""<?xml version="1.0" encoding="utf-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom">\n  <title>{e(SITE_TITLE['fr'])} — {AUTHOR}</title><link href="{SITE}/"/><link rel="self" href="{SITE}/feed.xml"/><id>{SITE}/</id><updated>{max(p['date'] for p in PUBLICATIONS if len(p['date']) > 4)}T00:00:00Z</updated><author><name>{AUTHOR}</name></author>\n{entries}</feed>\n""")
print("OK —", len(urls), "pages")
