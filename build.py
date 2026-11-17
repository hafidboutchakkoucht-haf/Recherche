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
               write="Écrire à l’auteur", next="Autre étude", rights="Tous droits réservés. Les textes peuvent être cités avec mention de l’auteur et de la source. Site sans cookie ; mesure d’audience anonyme.", series="Série Erasmus+ décrypté · en français"),
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
               write="Write to the author", next="Another study", rights="All rights reserved. Texts may be quoted with attribution to the author and source. No cookies; anonymous audience measurement.", series="Erasmus+ décrypté series · in French"),
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
from sections import S, PARTS  # noqa: E402
FICHES = json.load(open(os.path.join(ROOT, "fiches.json"), encoding="utf-8"))
for _l in LANGS:
    UI[_l].update(S[_l])
AXES.append({l: S[l]["axe3"] for l in LANGS})
import questionnaire as QZ  # noqa: E402
import lexique as LX  # noqa: E402
import zlib  # noqa: E402
from fiches_fr import FICHES_FR, UI as FR_UI, SOURCE as FR_SOURCE  # noqa: E402
for _f in FICHES_FR:
    _f["source"] = FR_SOURCE
PARTS["Peines"] = {"fr": "Peines", "en": "Penalties", "es": "Penas", "ar": "العقوبات"}
FR_BY_N = {f["n"]: f for f in FICHES_FR}
MA_BY_N = {f["n"]: f for f in FICHES}
_FX = {
    "f_k": ("Droit pénal comparé", "Comparative criminal law", "Derecho penal comparado", "القانون الجنائي المقارن"),
    "f_h": ("Maroc et France <em>en vingt-quatre fiches</em>", "Morocco and France <em>in twenty-four sheets</em>", "Marruecos y Francia <em>en veinticuatro fichas</em>", "المغرب وفرنسا <em>في أربع وعشرين بطاقة</em>"),
    "f_p": ("Deux séries en miroir : Qanoun Clair pour le droit pénal marocain, Droit Clair pour le droit pénal français. Chaque fiche donne le texte officiel, les règles à connaître, un cas pratique, le piège à éviter et un test de dix secondes, puis renvoie à la fiche équivalente de l’autre droit.",
            "Two mirrored series: Qanoun Clair for Moroccan criminal law, Droit Clair for French criminal law. Each sheet gives the official text, the rules to know, a worked case, the trap to avoid and a ten-second test, then points to the equivalent sheet in the other system.",
            "Dos series en espejo: Qanoun Clair para el derecho penal marroquí, Droit Clair para el derecho penal francés. Cada ficha ofrece el texto oficial, las reglas, un caso práctico, la trampa que evitar y un test de diez segundos, y remite a la ficha equivalente del otro derecho.",
            "سلسلتان متقابلتان: «قانون واضح» للقانون الجنائي المغربي و«Droit Clair» للقانون الجنائي الفرنسي. تقدّم كل بطاقة النص الرسمي والقواعد الأساسية وحالة تطبيقية والفخ الواجب تجنبه واختباراً من عشر ثوانٍ، ثم تحيل على البطاقة المقابلة في القانون الآخر."),
    "n_fiches": ("fiches de droit pénal comparé", "comparative criminal law sheets", "fichas de derecho penal comparado", "بطاقة في القانون الجنائي المقارن"),
    "f_ma": ("Maroc", "Morocco", "Marruecos", "المغرب"), "f_fr": ("France", "France", "Francia", "فرنسا"),
    "f_pack_ma": ("Fiches Maroc (PDF)", "Morocco sheets (PDF)", "Fichas Marruecos (PDF)", "بطاقات المغرب (PDF)"),
    "f_pack_fr": ("Fiches France (PDF)", "France sheets (PDF)", "Fichas Francia (PDF)", "بطاقات فرنسا (PDF)"),
    "f_updated_fr": ("Fiches France : codes en vigueur consultés sur Légifrance, rédaction du 14 novembre 2026.", "France sheets: codes in force consulted on Légifrance, written on 14 November 2026.",
                     "Fichas Francia: códigos vigentes consultados en Légifrance, redacción del 14 de noviembre de 2026.", "بطاقات فرنسا: المدونات السارية كما هي منشورة على موقع Légifrance، حُرّرت في 14 نونبر 2026."),
}
for _i, _l in enumerate(LANGS):
    UI[_l].update({k: v[_i] for k, v in _FX.items()})
strip_no = lambda k: k.split(" · ", 1)[1] if " · " in k and k[:2].isdigit() else k


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


def page(lang, path, alt_paths, title, desc, body, head_extra="", alternates=True, og_type="website", og_image="assets/og.png"):
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
{"".join(f'<link rel="alternate" hreflang="{l}" href="{alts[l]}">' + chr(10) for l in LANGS).rstrip() if alternates else ""}
{f'<link rel="alternate" hreflang="x-default" href="{alts["fr"]}">' if alternates else ""}
<link rel="alternate" type="application/atom+xml" title="{e(SITE_TITLE['fr'])}" href="{SITE}/feed.xml">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{e(SITE_TITLE[lang])}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
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
  <nav aria-label="{u['library']}"><a href="{home}#axes">{u['axes']}</a><a href="{home}#jeunesses">{u['nav_doc']}</a><a href="{home}#bibliotheque">{u['nav_etudes']}</a><a href="{home}#fiches">{u['nav_fiches']}</a><a href="{root}{LX.L_DIR[lang]}/">{LX.TXT['nav'][lang]}</a><a href="{root}{VID_DIR[lang]}/">{UI_V[lang]['nav']}</a><a href="{home}#parcours">{u['nav_parcours']}</a><a href="{home}#contact">{u['contact']}</a></nav>
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
<script data-goatcounter="https://hafid.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>
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
    parts = list(dict.fromkeys(f["part"] for f in FICHES))
    allf = [("ma", "fiches", f) for f in FICHES] + [("fr", "fiches-france", f) for f in FICHES_FR]
    fcards = "".join(f"""
    <a class="fcard rv" data-item data-sys="{sy}" data-part="{sy}{parts.index(f['part']) if f['part'] in parts else 9}" data-text="{e((f['title'] + ' ' + f['ar'] + ' ' + ' '.join(f['pills']) + ' ' + f['q'] + ' ' + u['f_' + sy]).lower())}" href="{r}{fd}/{f['slug']}/" hreflang="fr">
      <span class="fnum">{f['n']:02d}</span><span class="tag sys-{sy}">{e(u['f_' + sy])} · {e(PARTS[f['part']][lang])}</span>
      <strong lang="fr" dir="ltr">{e(f['title'])}</strong><span class="far" lang="ar" dir="rtl">{e(f['ar'])}</span>
      <span class="fpills" dir="ltr">{''.join(f'<i>{e(x)}</i>' for x in f['pills'])}</span>
    </a>""" for sy, fd, f in allf)
    ffilters = f'<button class="f" type="button" data-f="all" aria-pressed="true">{u["f_all"]}</button>' + "".join(f'<button class="f" type="button" data-f="sys:{sy}" aria-pressed="false">{e(u["f_" + sy])}</button>' for sy in ("ma", "fr"))
    quiz = [{"n": f["n"], "q": f["q"], "r": f["r"], "t": u["f_" + sy] + " · " + f["title"], "u": f"{r}{fd}/{f['slug']}/"} for sy, fd, f in allf]
    k = lambda i, label: f"{i:02d} · {strip_no(label)}"
    body = f"""<div class="wrap hero">
  <div>
    <p class="label">{u['kicker']}</p>
    <h1>{title_html}</h1>
    <p class="byline">{AUTHOR}</p>
    <p class="rolehero">{e(u['role'])}</p>
    <p class="lead">{e(u['tagline'])}</p>
    <p class="dl"><a class="chip fill" href="#bibliotheque">{u['cta1']}</a><a class="chip" href="{r}telechargements/boutchakkoucht-recueil-des-etudes.pdf" download>{u['cta2']}</a></p>
  </div>
  <div class="art">{norm_real_svg()}<p class="legend"><span>{u['norm']}</span><span>{u['real']}</span></p></div>
</div>
<div class="wrap"><dl class="stats rv">
  <div><dt>{len(PUBLICATIONS)}</dt><dd>{u['n_studies']}</dd></div><div><dt>{total_pages}</dt><dd>{u['n_pages']}</dd></div><div><dt>{len(FICHES) + len(FICHES_FR)}</dt><dd>{u['n_fiches']}</dd></div><div><dt>{n_videos}</dt><dd>{u['n_videos']}</dd></div>
</dl></div>

<section id="axes"><div class="wrap">
  <div class="head"><p class="label">{k(1, u['axes_k'])}</p><h2>{u['axes_h']}</h2></div>
  <div class="axes">{''.join(f'<article class="rv"><b>{chr(97 + i)}.</b><h3>{e(a[lang][0])}</h3><p>{e(a[lang][1])}</p></article>' for i, a in enumerate(AXES))}</div>
</div></section>

<section id="jeunesses"><div class="wrap">
  <div class="head"><p class="label">{k(2, u['doc_k'])}</p><div><h2>{u['doc_h']}</h2><p class="sub big-sub">{e(u['doc_sub'])}</p><p class="intro">{e(u['doc_p'])}</p></div></div>
  <div class="axes three">{''.join(f'<article class="rv"><b>{['I', 'II', 'III'][i]}</b><h3>{e(t)}</h3><p>{e(d)}</p></article>' for i, (t, d) in enumerate(u['doc_cards']))}</div>
  <ul class="kw">{''.join(f'<li>{e(x)}</li>' for x in u['doc_kw'])}</ul>
  {jeunesses_affiche(lang, r)}
  {survey_cta(lang, r)}
</div></section>

<section id="bibliotheque"><div class="wrap" data-library>
  <div class="head"><p class="label">{k(3, u['lib_k'])}</p><div><h2>{u['lib_h']}</h2><p class="intro">{u['lib_p']}</p></div></div>
  <div class="toolbar"><input class="search" type="search" placeholder="{u['search']}" aria-label="{u['search']}"><div class="filters">{filters}</div></div>
  <div class="items">{''.join(cards)}
  </div>
  <p class="empty" hidden>{u['none']}</p>
  <aside class="recueil rv"><div><p class="label">PDF · {total_pages + 5} {u['pages']}</p><h3>{u['recueil_h']}</h3><p>{u['recueil_p']}</p></div><a class="chip fill" href="{r}telechargements/boutchakkoucht-recueil-des-etudes.pdf" download>{u['recueil_b']}</a></aside>
</div></section>

<div class="wrap works"><div class="head" style="margin-top:clamp(40px,6vw,72px)"><p class="label">{e(u['works_k'])}</p><h2 class="h2s">{u['works_h']}</h2></div>
  <ol class="worklist">{''.join(f'<li class="rv"><div><h3>{e(t)}</h3><p>{e(d)}</p></div><span class="tag">{e(st)}</span></li>' for t, d, st in u['works'])}</ol>
</div>

<section id="fiches"><div class="wrap" data-library>
  <div class="head"><p class="label">{k(4, u['f_k'])}</p><div><h2>{u['f_h']}</h2><p class="intro">{e(u['f_p'])}</p><p class="small">{e(u['f_note'])}</p>
  <p class="dl"><a class="chip fill" href="{r}telechargements/qanoun-clair-pack-1.pdf" download>{e(u['f_pack_ma'])}</a><a class="chip fill" href="{r}telechargements/droit-clair-france.pdf" download>{e(u['f_pack_fr'])}</a></p></div></div>
  <div class="toolbar"><input class="search" type="search" placeholder="{e(u['f_search'])}" aria-label="{e(u['f_search'])}"><div class="filters">{ffilters}</div></div>
  <div class="fgrid">{fcards}
  </div>
  <p class="empty" hidden>{e(u['f_none'])}</p>
  <div class="quiz rv" data-quiz><div><p class="label">{e(u['quiz_k'])}</p><h3>{u['quiz_h']}</h3></div>
    <div class="qcard" lang="fr" dir="ltr"><p class="qn"></p><p class="qq"></p><p class="qr" hidden></p>
    <p class="dl"><button class="chip fill" type="button" data-show>{e(u['quiz_show'])}</button><button class="chip" type="button" data-next>{e(u['quiz_next'])}</button><a class="chip" data-link href="#" hidden>{e(u['quiz_link'])}</a></p></div>
    <script type="application/json">{json.dumps({"fiche": u["f_fiche"], "items": quiz}, ensure_ascii=False).replace("<", "\\u003c")}</script>
  </div>
  <p class="small" style="margin-top:18px">{e(u['f_updated'])} {e(u['f_updated_fr'])} {e(u['f_disc'])}</p>
</div></section>

{lex_teaser(lang, r)}

{videos_teaser(lang, r)}

<section id="parcours"><div class="wrap">
  <div class="head"><p class="label">{k(7, u['par_k'])}</p><h2>{u['par_h']}</h2></div>
  <div class="about rv"><figure><img src="{r}assets/portrait.jpg" alt="{AUTHOR}" width="700" height="700" loading="lazy"></figure>
  <div><p class="role">{e(u['role'])}</p><p>{e(BIO[lang])}</p>
  <p class="dl"><a class="chip" href="https://orcid.org/{ORCID}" rel="me">{u['orcid']} · {ORCID}</a><a class="chip" href="{r}assets/portrait.jpg" download="hafid-boutchakkoucht.jpg">{u['portrait']}</a><a class="chip" href="{MAIN_SITE}">Cross Borders ↗</a></p></div></div>
  <div class="axes three">{''.join(f'<article class="rv"><b>{i + 1}</b><h3>{e(t)}</h3><p>{e(d)}</p></article>' for i, (t, d) in enumerate(u['par_cards'][:3]))}</div>
  <div class="cv rv">
    <div><p class="label">{e(u['edu_k'])}</p>{''.join(f'<p class="cvl"><strong>{e(t)}</strong><br>{e(d)}</p>' for t, d in (u['edu'][0], u['edu'][3]))}<p class="label" style="margin-top:1.6em">{e(u['lang_k'])}</p><p class="cvl">{e(u['langs'])}</p></div>
    <div><p class="label">{e(u['val_k'])}</p>{''.join(f'<p class="cvl"><strong>{e(t)}</strong><br>{e(d)}</p>' for t, d in (u['vals'][0], u['vals'][3]))}</div>
  </div>
  <p class="dl rv"><a class="chip" href="{r}{AB_DIR[lang]}/">{e(u['ab_link'])} →</a></p>
</div></section>

<section id="contact"><div class="wrap">
  <div class="head"><p class="label">{k(8, u['contact_k'])}</p><div><h2>{u['contact_h']}</h2><p class="intro">{u['contact_p']} <a href="mailto:{EMAIL}">{EMAIL}</a></p></div></div>
</div></section>"""
    page(lang, HOME[lang], HOME, f"{SITE_TITLE[lang]} — {AUTHOR}", BIO[lang][:158].rsplit(" ", 1)[0] + "…", body,
         head_extra=f'<script type="application/ld+json">{json.dumps(person, ensure_ascii=False)}</script>')


JV = {"fr": dict(watch="Voir les épisodes", study="Lire l'étude", survey="Répondre à l'enquête", series="Voir la série", film="La série en un film (16:9)"),
      "en": dict(watch="Watch the episodes", study="Read the study", survey="Take the survey", series="Watch the series", film="The series as one film (16:9)"),
      "es": dict(watch="Ver los episodios", study="Leer el estudio", survey="Responder a la encuesta", series="Ver la serie", film="La serie en una película (16:9)"),
      "ar": dict(watch="شاهد الحلقات", study="اقرأ الدراسة", survey="شارك في الاستبيان", series="شاهد السلسلة", film="السلسلة في فيلم واحد (16:9)")}


AB_DIR = {"fr": "a-propos", "en": "en/about", "es": "es/acerca-de", "ar": "ar/about"}


def about_page(lang):
    u = UI[lang]
    path = AB_DIR[lang]
    root = "../" * len(path.split("/"))
    home = root + (HOME[lang] + "/" if HOME[lang] else "")
    t, d = u['par_cards'][3]
    body = f"""<div class="wrap article">
  <p class="label"><a href="{home}#parcours">{e(u['ab_back'])}</a></p>
  <h1>{u['ab_h']}</h1>
  <p class="lead">{e(u['ab_lead'])}</p>
  <div class="axes three"><article><h3>{e(t)}</h3><p>{e(d)}</p></article></div>
  <div class="cv">
    <div><p class="label">{e(u['edu_k'])}</p>{''.join(f'<p class="cvl"><strong>{e(a)}</strong><br>{e(c)}</p>' for a, c in (u['edu'][1], u['edu'][2], u['edu'][4]))}<p class="label" style="margin-top:1.6em">{e(u['mandate_k'])}</p><p class="cvl"><strong>{e(u['mandate'][0])}</strong><br>{e(u['mandate'][1])}</p></div>
    <div><p class="label">{e(u['val_k'])}</p>{''.join(f'<p class="cvl"><strong>{e(a)}</strong><br>{e(c)}</p>' for a, c in (u['vals'][1], u['vals'][2]))}</div>
  </div>
</div>"""
    page(lang, path, AB_DIR, f"{strip_tags(u['ab_h'])} — {AUTHOR} · {SITE_TITLE[lang]}", u["ab_lead"], body)


def featured_series():
    for rb in RUBRIQUES:
        for s in rb["series"]:
            if s.get("feature"):
                return rb, s
    return None, None


def jeunesses_affiche(lang, r):
    """Affiche de la série vidéo, mise en avant sur l'accueil."""
    rb, s = featured_series()
    if not s:
        return ""
    f, v, j = s["feature"], UI_V[lang], JV[lang]
    pl = "ar" if lang == "ar" else "fr"
    href = f"{r}{VID_DIR[lang]}/#{rb['id']}"
    return f"""<div class="vfeature jaffiche rv">
    <a class="vfilm" href="{href}"><img src="{r}media/videos/posters/{f['poster'].format(lang=pl)}" alt="{e(f['h'][lang])}" width="1920" height="1080" loading="lazy"><span class="vplay" aria-hidden="true"></span></a>
    <div><p class="label">{e(f['kicker'][lang])}</p><h3>{e(f['h'][lang])}</h3><p>{e(s['about'][lang])}</p>
    <p class="dl"><a class="chip fill" href="{href}">{j['series']}</a><a class="chip" href="{r}{PUB_DIR[lang]}/{f['study']}/">{j['study']}</a></p></div>
  </div>"""


def series_chip(lang, p, root):
    rb, s = featured_series()
    if not s or s["feature"].get("study") != p["slug"]:
        return ""
    return f'<a class="chip" href="{root}{VID_DIR[lang]}/#{rb["id"]}">{JV[lang]["series"]}</a>'


def count_videos():
    n = 0
    for rb in RUBRIQUES:
        for s in rb["series"]:
            n += len(s["items"]) * len(s.get("langs", []))
    return n + 1 + sum(len(s.get('langs', [])) for rb in RUBRIQUES for s in rb['series'] if s.get('feature'))  # + films 16:9


def vfile(s, lang, n):
    return s["file"].format(lang=lang, n=n)


def live_rubs():
    return [rb for rb in RUBRIQUES if any(s["items"] for s in rb["series"])]


def videos_teaser(lang, r):
    v = UI_V[lang]
    n_series = sum(1 for rb in RUBRIQUES for s in rb["series"] if s["items"])
    rubs = "".join(f'<li><a href="{r}{VID_DIR[lang]}/#{rb["id"]}">{e(rb["name"][lang])}</a></li>' for rb in live_rubs())
    return f"""<section id="videos"><div class="wrap">
  <div class="head"><p class="label">06 · {strip_no(v['home_k'])}</p><div><h2>{v['home_h']}</h2><p class="intro">{e(v['home_p'])}</p></div></div>
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
    jump = "".join(f'<a class="f" href="#{rb["id"]}">{e(rb["name"][lang])}</a>' for rb in live_rubs())
    film = f"""<div class="vfeature rv">
    <a class="vfilm" href="{root}{FILM_URL}{'?lang=ar' if lang == 'ar' else ''}"><img src="{root}media/videos/posters/film-interactif.jpg" alt="" width="1032" height="580" loading="lazy"><span class="vplay" aria-hidden="true"></span></a>
    <div><p class="label">{v['featured']}</p><h3>{e(v['film_h'])}</h3><p>{e(v['film_p'])}</p>
    <p class="dl"><a class="chip fill" href="{root}{FILM_URL}{'?lang=ar' if lang == 'ar' else ''}">{v['film_b']}</a><a class="chip" href="{root}{FILM_URL}{'' if lang == 'ar' else '?lang=ar'}">{v['film_b2']}</a></p></div>
  </div>
  <div class="vwide rv"><video controls playsinline preload="none" poster="{root}media/videos/posters/film-guerre-des-blocus.jpg"><source src="{root}media/videos/iran/film-guerre-des-blocus.mp4" type="video/mp4"></video>
    <div><p class="label">{v['film_v']}</p><p class="small">{e(v['film_v_p'])} · <a href="{root}media/videos/iran/film-guerre-des-blocus.mp4" download>{v['download']}</a></p></div></div>"""
    secs = []
    for i, rb in enumerate(live_rubs()):
        blocks = []
        for s in rb["series"]:
            if not s["items"]:
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
            feat = ""
            if s.get("feature"):
                ft, j = s["feature"], JV[lang]
                for l in langs:
                    fsrc = f"{root}media/videos/{s['dir']}/{ft['film'].format(lang=l)}"
                    feat += f"""<div class="vwide jfeat" data-l="{l}"{'' if l == show else ' hidden'}><video controls playsinline preload="none" poster="{root}media/videos/posters/{ft['poster'].format(lang=l)}" aria-label="{e(ft['h'][l])}"><source src="{fsrc}" type="video/mp4"></video>
        <div><p class="label">{e(ft['kicker'][lang])}</p><h3 lang="{l}" dir="{'rtl' if l == 'ar' else 'ltr'}">{e(ft['h'][l])}</h3><p>{e(ft['p'][lang])}</p>
        <p class="dl"><a class="chip fill" href="#ep-{s['id']}">{j['watch']}</a><a class="chip" href="{root}{PUB_DIR[lang]}/{ft['study']}/">{j['study']}</a><a class="chip" href="{root}enquete/#repondre">{j['survey']}</a></p>
        <p class="small">{j['film']} · <a href="{fsrc}" download>{v['download']}</a></p></div></div>"""
            blocks.append(f"""<div class="vseries" data-series>
      <div class="vs-head"><div><h3>{e(s['title'][lang])}</h3><p>{e(s['about'][lang])}</p>{data}</div>{toggle}</div>
      {feat}<div class="vgrid" id="ep-{s['id']}">{''.join(cards)}</div></div>""")
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
  <p class="dl"><a class="chip fill" href="{pdf}" download>{u['pdf']} · {p['pages']} {u['pages']}</a><a class="chip" href="#lecteur">{u['reader']}</a><a class="chip" href="#citer">{u['cite']}</a>{series_chip(lang, p, root)}</p>
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
    page(lang, path, {l: f"{PUB_DIR[l]}/{p['slug']}" for l in LANGS}, f"{p['title'][lang]} — {AUTHOR} · {SITE_TITLE[lang]}", p["abstract"][lang][:155].rsplit(" ", 1)[0] + "…", body, head_extra=metas,
         og_type="article", og_image=f"assets/og/{p['slug']}.png" if os.path.exists(f"assets/og/{p['slug']}.png") else "assets/og.png")


def fiche_page(f, prev, nxt):
    u = UI["fr"]
    path = f"fiches/{f['slug']}"
    root = "../../"
    pdf = f"{root}telechargements/fiches/qanoun-clair-fiche-{f['n']:02d}.pdf"
    img = f"{root}fiches/img/fiche-{f['n']:02d}.webp"
    blocks = ""
    if f["off_text"]:
        blocks += f'<h2 class="sec">{e(f["off_label"] or u["fp_text"])}</h2><blockquote class="official">{e(f["off_text"])}</blockquote>'
    blocks += f'<h2 class="sec">{u["fp_case"]}</h2><p>{e(f["cas"])}</p><h2 class="sec">{u["fp_trap"]}</h2><p class="trap">{e(f["piege"])}</p>'
    blocks += f'<h2 class="sec">{u["fp_test"]}</h2><div class="qcard"><p class="qq">{e(f["q"])}</p><details><summary>{u["quiz_show"]}</summary><p class="qr">{e(f["r"])}</p></details></div>'
    fr = FR_BY_N.get(f["n"])
    if fr:
        blocks += f'<h2 class="sec">{FR_UI["cross_ma"]}</h2><p class="cross">{e(fr["croise"])} <a href="{root}fiches-france/{fr["slug"]}/">{FR_UI["cross_b_ma"]} →</a></p>'
    blocks += f'<h2 class="sec">{u["fp_source"]}</h2><p class="small">{e(f["source"].replace("Source vérifiable :", "").strip())}</p>'
    ld = {"@context": "https://schema.org", "@type": "LearningResource", "name": f["title"], "alternateName": f["ar"], "inLanguage": ["fr", "ar"], "learningResourceType": "Fiche de révision",
          "about": "Droit pénal marocain", "url": f"{SITE}/{path}/", "image": f"{SITE}/fiches/img/fiche-{f['n']:02d}.webp", "isPartOf": {"@type": "CreativeWorkSeries", "name": "Qanoun Clair"},
          "author": {"@type": "Person", "name": AUTHOR, "url": SITE + "/"}}
    body = f"""<div class="wrap article fiche">
  <p class="label"><a href="{root}#fiches">{u['fp_back']}</a> · Qanoun Clair · {u['f_fiche']} {f['n']:02d} / {len(FICHES)} · {e(f['part'])}</p>
  <h1>{e(f['title'])}</h1>
  <p class="far-title" lang="ar" dir="rtl">{e(f['ar'])}</p>
  <ul class="kw">{''.join(f'<li>{e(x)}</li>' for x in f['pills'])}</ul>
  <p class="dl"><a class="chip fill" href="{pdf}" download>{u['fp_pdf']}</a><a class="chip" href="{img}">{u['fp_zoom']}</a><a class="chip" href="{root}telechargements/qanoun-clair-pack-1.pdf" download>{u['f_pack']}</a></p>
  <div class="cols fiche-cols">
    <a class="sheet" href="{img}"><img src="{img}" alt="{e('Fiche ' + str(f['n']) + ' : ' + f['title'] + '. ' + ' · '.join(f['sections']))}" width="1588" height="2246"></a>
    <aside class="body">{blocks}</aside>
  </div>
  <p class="small">{e(u['f_disc'])}</p>
  <nav class="pager" aria-label="Fiches"><a href="../{prev['slug']}/"><span class="label">{u['fp_prev']}</span><strong>{prev['n']:02d} · {e(prev['title'])}</strong></a><a href="../{nxt['slug']}/"><span class="label">{u['fp_next']}</span><strong>{nxt['n']:02d} · {e(nxt['title'])}</strong></a></nav>
</div>"""
    page("fr", path, HOME, f"{f['title']} — Qanoun Clair, fiche {f['n']:02d} · {AUTHOR}", (f["off_text"] or f["cas"])[:155].rsplit(" ", 1)[0] + "…", body,
         head_extra=f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>', alternates=False)


def sheet_fr(f, tag="h2"):
    """La fiche française, composée en HTML (écran et impression)."""
    return f"""<article class="sheet-fr">
    <header><p class="label">{FR_UI['serie']} · {UI['fr']['f_fiche']} {f['n']:02d} / {len(FICHES_FR)} · {e(f['part'])}</p><{tag}>{e(f['title'])}</{tag}><p class="far" lang="ar" dir="rtl">{e(f['ar'])}</p></header>
    <h3>{FR_UI['rules']}</h3><ol>{''.join(f'<li>{e(x)}</li>' for x in f['regles'])}</ol>
    <h3>{FR_UI['figures']}</h3><dl>{''.join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in f['chiffres'])}</dl>
  </article>"""


def fiche_fr_page(f, prev, nxt):
    u = UI["fr"]
    path = f"fiches-france/{f['slug']}"
    root = "../../"
    ma = MA_BY_N.get(f["n"])
    blocks = f'<h2 class="sec">{e(f["off_label"])}</h2><blockquote class="official">{e(f["off_text"])}</blockquote>'
    blocks += f'<h2 class="sec">{u["fp_case"]}</h2><p>{e(f["cas"])}</p><h2 class="sec">{u["fp_trap"]}</h2><p class="trap">{e(f["piege"])}</p>'
    blocks += f'<h2 class="sec">{u["fp_test"]}</h2><div class="qcard"><p class="qq">{e(f["q"])}</p><details><summary>{u["quiz_show"]}</summary><p class="qr">{e(f["r"])}</p></details></div>'
    if ma:
        blocks += f'<h2 class="sec">{FR_UI["cross"]}</h2><p class="cross">{e(f["croise"])} <a href="{root}fiches/{ma["slug"]}/">{FR_UI["cross_b"]} →</a></p>'
    blocks += f'<h2 class="sec">{u["fp_source"]}</h2><p class="small">{e(f["source"].replace("Source vérifiable :", "").strip())}</p>'
    ld = {"@context": "https://schema.org", "@type": "LearningResource", "name": f["title"], "alternateName": f["ar"], "inLanguage": "fr", "learningResourceType": "Fiche de révision",
          "about": "Droit pénal français", "url": f"{SITE}/{path}/", "isPartOf": {"@type": "CreativeWorkSeries", "name": FR_UI["serie"]}, "author": {"@type": "Person", "name": AUTHOR, "url": SITE + "/"}}
    body = f"""<div class="wrap article fiche">
  <p class="label"><a href="{root}#fiches">{u['fp_back']}</a> · {FR_UI['serie']} · {u['f_fiche']} {f['n']:02d} / {len(FICHES_FR)} · {e(f['part'])}</p>
  <h1>{e(f['title'])}</h1>
  <p class="far-title" lang="ar" dir="rtl">{e(f['ar'])}</p>
  <ul class="kw">{''.join(f'<li>{e(x)}</li>' for x in f['pills'])}</ul>
  <p class="dl"><a class="chip fill" href="{root}telechargements/droit-clair-france.pdf" download>{FR_UI['pack']}</a><button class="chip" type="button" data-print>{FR_UI['print']}</button></p>
  <div class="cols fiche-cols">
    {sheet_fr(f)}
    <aside class="body">{blocks}</aside>
  </div>
  <p class="small">{e(u['f_disc'])}</p>
  <nav class="pager" aria-label="Fiches"><a href="../{prev['slug']}/"><span class="label">{u['fp_prev']}</span><strong>{prev['n']:02d} · {e(prev['title'])}</strong></a><a href="../{nxt['slug']}/"><span class="label">{u['fp_next']}</span><strong>{nxt['n']:02d} · {e(nxt['title'])}</strong></a></nav>
</div>"""
    page("fr", path, HOME, f"{f['title']} — {FR_UI['serie']}, fiche {f['n']:02d} · {AUTHOR}", f["off_text"][:155].rsplit(" ", 1)[0] + "…", body,
         head_extra=f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>', alternates=False)


def print_fr():
    """Document A4 autonome (une fiche par page) servant à produire le PDF."""
    u = UI["fr"]
    pages = "".join(f"""<section class="pg">{sheet_fr(f)}
  <div class="two"><div><h3>{e(f['off_label'])}</h3><blockquote>{e(f['off_text'])}</blockquote><h3>{u['fp_case']}</h3><p>{e(f['cas'])}</p></div>
  <div><h3>{u['fp_trap']}</h3><p class="trap">{e(f['piege'])}</p><h3>{u['fp_test']}</h3><p><b>{e(f['q'])}</b><br>→ {e(f['r'])}</p><h3>{FR_UI['cross']}</h3><p>{e(f['croise'])}</p></div></div>
  <footer>{e(f['source'])} · {AUTHOR} · {SITE.replace('https://', '')}</footer></section>""" for f in FICHES_FR)
    toc = "".join(f"<li><span>{f['n']:02d}</span>{e(f['title'])}</li>" for f in FICHES_FR)
    css = """@page{size:A4;margin:0}*{box-sizing:border-box}body{margin:0;font:10.4pt/1.42 Georgia,'Times New Roman',serif;color:#1B1A17}
.pg{width:210mm;height:297mm;padding:15mm 16mm 12mm;page-break-after:always;position:relative;overflow:hidden;background:#FFFDF8}
.label{font:700 7.6pt Arial,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#7A1F2B;margin:0 0 3mm}
h1{font-size:34pt;font-weight:500;line-height:1.08;margin:0}h1 em{color:#7A1F2B}h2{font-size:19pt;font-weight:500;line-height:1.15;margin:0}
.far{font:700 13pt 'Noto Naskh Arabic','Noto Sans Arabic',serif;color:#B8862B;margin:1.5mm 0 0}
.sheet-fr header{border-bottom:2px solid #7A1F2B;padding-bottom:4mm;margin-bottom:4mm}
h3{font:700 7.8pt Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#7A1F2B;margin:4.5mm 0 1.6mm}
ol{margin:0;padding:0;list-style:none;counter-reset:r}ol li{counter-increment:r;padding:1.3mm 0 1.3mm 9mm;position:relative;border-bottom:.3pt solid #1B1A1722}
ol li::before{content:counter(r);position:absolute;left:0;top:.4mm;font-size:15pt;font-style:italic;color:#B8862B}
dl{margin:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(40mm,1fr));gap:2mm}dl div{background:#F1EADB;padding:2.4mm 3mm}dt{font:700 7.4pt Arial,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:#5F5A50}dd{margin:.6mm 0 0;font-size:10.6pt}
.two{display:grid;grid-template-columns:1fr 1fr;gap:7mm}blockquote{margin:0;padding:2.4mm 3.4mm;border-left:2.4pt solid #7A1F2B;background:#F6F2EA;font-style:italic}p{margin:0}
.trap{border-left:2.4pt solid #B8862B;padding-left:3mm}footer{position:absolute;left:16mm;right:16mm;bottom:8mm;font:6.6pt/1.35 Arial,sans-serif;color:#5F5A50;border-top:.3pt solid #1B1A1733;padding-top:1.6mm}
.cover{display:flex;flex-direction:column;justify-content:center}.cover ol{margin-top:10mm;columns:2;column-gap:10mm}.cover li{border:0;padding:1mm 0 1mm 9mm;break-inside:avoid}.cover li span{position:absolute;left:0;color:#B8862B;font-style:italic}.cover li::before{content:none}
.lead{font-size:13pt;color:#5F5A50;margin-top:6mm;max-width:150mm}"""
    doc = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{FR_UI['serie']} — {AUTHOR}</title><style>{css}</style></head><body>
<section class="pg cover"><p class="label">{FR_UI['serie']} · {AUTHOR}</p><h1>{FR_UI['h']}</h1><p class="lead">Douze fiches d’une page, en miroir des fiches Qanoun Clair consacrées au droit pénal marocain : règles, repères chiffrés, texte officiel, cas pratique, piège, test et regard croisé.</p><ol>{toc}</ol>
<footer>{e(FR_SOURCE)} · {SITE.replace('https://', '')}</footer></section>{pages}</body></html>"""
    write("outils/droit-clair-france-impression.html", doc)


def star_xy(tid, i):
    h = zlib.crc32(tid.encode())
    col, row = i % 3, i // 3
    return 78 + col * 122 + (h % 25 - 12), 52 + row * 106 + (col % 2) * 24 + ((h >> 8) % 21 - 10)


def star_label(s):
    if len(s) <= 14 or " " not in s:
        return [s]
    cuts = [i for i, c in enumerate(s) if c == " "]
    c = min(cuts, key=lambda i: abs(i - len(s) / 2))
    return [s[:c], s[c + 1:]]


def lex_data():
    out = {}
    for di, (dk, _) in enumerate(LX.DOMAINS):
        for tid, names, defs, links in LX.TERMS[dk]:
            out[tid] = {"d": di, "t": names, "x": defs, "l": links}
    for tid, v in out.items():
        for l in v["l"]:
            assert l in out, (tid, l)
    return out


def lex_teaser(lang, r):
    T = LX.TXT
    li = LANGS.index(lang)
    sample = "".join(f'<a class="wstar d{di}" href="{r}{LX.L_DIR[lang]}/#t-{tid}">{e(names[li])}</a>' for di, (dk, _) in enumerate(LX.DOMAINS) for tid, names, _d, _l in LX.TERMS[dk][:4])
    n = sum(len(v) for v in LX.TERMS.values())
    return f"""<section id="lexique"><div class="wrap">
  <div class="head"><p class="label">05 · {e(T['home_k'][lang])}</p><div><h2>{T['home_h'][lang]}</h2><p class="intro">{e(T['home_p'][lang])}</p></div></div>
  <div class="lex-teaser rv"><div class="wcloud">{sample}</div>
  <div class="lt-foot"><p>{n} {e(T['count'][lang])} · {len(LX.DOMAINS)} {e(T['domains'][lang])} · {len(LANGS)} {e(T['langs'][lang])}</p><a class="chip fill" href="{r}{LX.L_DIR[lang]}/">{e(T['home_b'][lang])}</a></div></div>
</div></section>"""


def lex_page(lang):
    T, li, data = LX.TXT, LANGS.index(lang), lex_data()
    x = lambda key: T[key][lang]
    deg = {k: len(v["l"]) + sum(1 for o in data.values() if k in o["l"]) for k, v in data.items()}
    skies = ""
    for di, (dk, dname) in enumerate(LX.DOMAINS):
        pos = {tid: star_xy(tid, i) for i, (tid, *_r) in enumerate(LX.TERMS[dk])}
        seen, lines, stars = set(), "", ""
        for tid, names, _d, links in LX.TERMS[dk]:
            for l in links:
                if l in pos and (l, tid) not in seen:
                    seen.add((tid, l))
                    lines += f'<line x1="{pos[tid][0]}" y1="{pos[tid][1]}" x2="{pos[l][0]}" y2="{pos[l][1]}" data-a="{tid}" data-b="{l}"/>'
        for tid, names, _d, links in LX.TERMS[dk]:
            px, py = pos[tid]
            lab = "".join(f'<tspan x="{px}" dy="{0 if j == 0 else 14}">{e(s)}</tspan>' for j, s in enumerate(star_label(names[li])))
            stars += f'<a class="star" href="#t-{tid}" data-star="{tid}" data-text="{e(" ".join(names).lower())}"><circle class="hit" cx="{px}" cy="{py + 8}" r="30"/><circle class="s" cx="{px}" cy="{py}" r="{3.2 + min(deg[tid], 8) * 0.55:.1f}" style="animation-delay:{(zlib.crc32(tid.encode()) % 40) / 10}s"/><text x="{px}" y="{py + 22}" text-anchor="middle">{lab}</text></a>'
        skies += f"""<figure class="sky d{di}" id="{dk}"><figcaption><span>{di + 1:02d}</span><h2>{e(dname[lang])}</h2><small>{len(LX.TERMS[dk])} {e(x('count'))}</small></figcaption>
    <svg viewBox="0 0 400 480" role="group" aria-label="{e(dname[lang])}"><g class="links">{lines}</g>{stars}</svg></figure>"""
    order = sorted(data.items(), key=lambda kv: kv[1]["t"][li].lower().replace("é", "e").replace("É", "e"))
    index = "".join(f"""<div class="lex-item" id="t-{tid}" data-item data-text="{e(' '.join(v['t']).lower())}"><dt><button type="button" data-open="{tid}">{e(v['t'][li])}</button><span class="tag d{v['d']}">{e(LX.DOMAINS[v['d']][1][lang])}</span></dt>
    <dd><p>{e(v['x'][li])}</p><p class="eq">{' · '.join(f'<span lang="{l}" dir="{"rtl" if l in RTL else "ltr"}">{e(v["t"][j])}</span>' for j, l in enumerate(LANGS) if l != lang)}</p></dd></div>""" for tid, v in order)
    tabs = "".join(f'<button type="button" data-lg="{l}" aria-pressed="{"true" if l == lang else "false"}" lang="{l}">{UI[l]["lang_name"]}</button>' for l in LANGS)
    payload = json.dumps({"lang": lang, "langs": LANGS, "domains": [[d[1][l] for l in LANGS] for d in LX.DOMAINS], "terms": data}, ensure_ascii=False).replace("<", "\\u003c")
    body = f"""<div class="wrap article lex" data-lex>
  <p class="label">{e(x('kicker'))}</p>
  <h1>{x('h1')}</h1>
  <p class="lead">{e(x('lead'))}</p>
  <div class="toolbar lex-tools"><input class="search" type="search" placeholder="{e(x('search'))}" aria-label="{e(x('search'))}"><div class="filters">{''.join(f'<a class="f d{di}" href="#{dk}">{e(dn[lang])}</a>' for di, (dk, dn) in enumerate(LX.DOMAINS))}<button class="f" type="button" data-random>✦ {e(x('random'))}</button></div></div>
  <div class="skies">{skies}</div>
  <div class="head lex-head"><p class="label">{e(x('index'))}</p><div><p class="intro">{e(x('index_p'))}</p></div></div>
  <dl class="lex-index">{index}</dl>
  <p class="empty" hidden>{e(x('none'))}</p>
  <p class="small">{e(x('note'))}</p>
  <div class="lex-sheet" hidden role="dialog" aria-modal="false" aria-labelledby="ls-term" tabindex="-1">
    <div class="ls-top"><span class="tag ls-dom"></span><div class="ls-tabs" role="group">{tabs}</div><button class="ls-close" type="button" aria-label="{e(x('close'))}">×</button></div>
    <h2 id="ls-term"></h2><p class="ls-def"></p><p class="eq ls-eq"></p>
    <p class="label">{e(x('see'))}</p><div class="ls-see"></div>
  </div>
  <script type="application/json">{payload}</script>
</div>"""
    ld = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": f"{strip_tags(x('h1'))} — {AUTHOR}", "inLanguage": lang, "url": f"{SITE}/{LX.L_DIR[lang]}/",
          "hasDefinedTerm": [{"@type": "DefinedTerm", "name": v["t"][li], "description": v["x"][li]} for _k, v in order]}
    page(lang, LX.L_DIR[lang], LX.L_DIR, f"{strip_tags(x('h1'))} — {AUTHOR} · {SITE_TITLE[lang]}", x("lead")[:155].rsplit(" ", 1)[0] + "…", body,
         head_extra=f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>')


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


def survey_cta(lang, r):
    """Encart d'appel à l'enquête « Partir, rester ou se faire entendre » (dossier enquete/)."""
    T = {
        "fr": ("Enquête en cours", "Vous avez entre 18 et 35 ans ?", "Vingt minutes, de façon anonyme : dites ce que vous vivez, ce que vous attendez des responsables publics et comment vous voyez votre avenir, au Maroc ou en Europe.", "Répondre à l’enquête", "Résultats et étude"),
        "en": ("Survey in progress", "Are you between 18 and 35?", "Twenty minutes, anonymous, in French: tell us what you experience, what you expect from public authorities and how you see your future, in Morocco or in Europe.", "Take the survey", "Results and study"),
        "es": ("Encuesta en curso", "¿Tienes entre 18 y 35 años?", "Veinte minutos, de forma anónima y en francés: cuenta lo que vives, lo que esperas de los responsables públicos y cómo ves tu futuro, en Marruecos o en Europa.", "Responder a la encuesta", "Resultados y estudio"),
        "ar": ("استطلاع جارٍ", "هل عمرك بين 18 و35 سنة؟", "عشرون دقيقة، دون ذكر الهوية وباللغة الفرنسية: أخبرنا بما تعيشه، وبما تنتظره من المسؤولين العموميين، وكيف ترى مستقبلك، في المغرب أو في أوروبا.", "المشاركة في الاستطلاع", "النتائج والدراسة"),
    }[lang]
    return f"""<aside class="recueil survey-cta rv"><div><p class="label">{e(T[0])}</p><h3>{e(T[1])}</h3><p>{e(T[2])}</p></div><p class="dl"><a class="chip fill" href="{r}enquete/#repondre">{e(T[3])}</a><a class="chip" href="{r}enquete/#resultats">{e(T[4])}</a></p></aside>"""


def survey_page(lang):
    T, live = QZ.TXT, bool(QZ.ENDPOINT)
    x = lambda key: T[key][lang]
    fields, cur = [], -1
    for n, (qid, sec, kind, label, opts, flag) in enumerate(QZ.QUESTIONS, 1):
        if sec != cur:
            if cur >= 0:
                fields.append("</fieldset>")
            cur = sec
            fields.append(f'<fieldset class="qsec"><legend><span>{sec + 1:02d}</span>{e(QZ.SECTIONS[sec][lang])}</legend>')
        hint = {"optional": x("optional"), "multi": x("multi"), "max3": x("max3"), "": ""}[flag]
        if kind == "scale":
            hint = x("scale")
        head = f'<p class="qlabel" id="q-{qid}"><b>{n}.</b> {e(label[lang])}{f" <small>{e(hint)}</small>" if hint else ""}</p>'
        req = "" if flag == "optional" or kind in ("check", "text") else " required"
        if kind == "radio":
            inner = "".join(f'<label class="opt"><input type="radio" name="{qid}" value="{e(o["fr"])}"{req}><span>{e(o[lang])}</span></label>' for o in opts)
        elif kind == "check":
            inner = "".join(f'<label class="opt"><input type="checkbox" name="{qid}" value="{e(o["fr"])}"><span>{e(o[lang])}</span></label>' for o in opts)
        elif kind == "scale":
            inner = '<div class="scales">' + "".join(
                f'<div class="scale"><span>{e(o[lang])}</span><div role="radiogroup" aria-label="{e(o[lang])}">' + "".join(f'<label><input type="radio" name="{qid}_{k}" value="{v}" required><span>{v}</span></label>' for v in range(1, 6)) + "</div></div>"
                for k, o in enumerate(opts, 1)) + "</div>"
        else:
            inner = f'<textarea name="{qid}" rows="4" maxlength="1200" aria-labelledby="q-{qid}"></textarea>'
        fields.append(f'<div class="q" data-q{" data-max=\"3\"" if flag == "max3" else ""}>{head}<div class="opts{" two" if len(opts) > 5 and kind != "scale" else ""}">{inner}</div></div>' if kind != "scale" and kind != "text" else f'<div class="q" data-q>{head}{inner}</div>')
    fields.append("</fieldset>")
    tool = f' {e(x("tool").format(tool=QZ.TOOL_NAME))}' if QZ.TOOL_NAME else ""
    body = f"""<div class="wrap article survey">
  <p class="label">{e(x('kicker'))}</p>
  <h1>{x('h1')}</h1>
  <p class="lead">{e(x('lead'))}</p>
  <ul class="kw big-kw">{''.join(f'<li>{e(f[lang])}</li>' for f in T['facts'])}</ul>
  {'' if live else f'<p class="preview" role="status">{e(x("preview"))}</p>'}
  <form class="sform" data-survey data-endpoint="{e(QZ.ENDPOINT)}" data-sending="{e(x('sending'))}" novalidate>
    <input type="hidden" name="langue" value="{lang}">
    <div class="notice"><p class="label">{e(x('notice_k'))}</p><p>{e(x('notice'))}{tool}</p>
      <label class="opt"><input type="checkbox" name="majeur" value="oui" required><span>{e(x('c_age'))}</span></label>
      <label class="opt"><input type="checkbox" name="consentement" value="oui" required><span>{e(x('c_ok'))}</span></label></div>
    {''.join(fields)}
    <p class="hp" aria-hidden="true"><label>Ne pas remplir <input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></label></p>
    <p class="serr" role="alert" hidden>{e(x('error'))}</p>
    <p class="dl"><button class="chip fill big" type="submit"{'' if live else ' disabled'}>{e(x('send'))}</button><span class="small prog" aria-live="polite" data-label="{e(x('progress'))}"></span></p>
  </form>
  <div class="sthanks" hidden tabindex="-1"><h2>{e(x('thanks_h'))}</h2><p class="lead">{e(x('thanks'))}</p></div>
</div>"""
    page(lang, QZ.Q_DIR[lang], QZ.Q_DIR, f"{x('kicker')} — {AUTHOR} · {SITE_TITLE[lang]}", x("lead")[:155], body,
         head_extra="" if live else '<meta name="robots" content="noindex">')


for i, f in enumerate(FICHES):
    fiche_page(f, FICHES[i - 1], FICHES[(i + 1) % len(FICHES)])

for i, f in enumerate(FICHES_FR):
    fiche_fr_page(f, FICHES_FR[i - 1], FICHES_FR[(i + 1) % len(FICHES_FR)])
print_fr()

for lang in LANGS:
    lex_page(lang)
    survey_page(lang)
    videos_page(lang)
    about_page(lang)
    home(lang)
    for i, p in enumerate(PUBLICATIONS):
        publication(lang, p, PUBLICATIONS[(i + 1) % len(PUBLICATIONS)])

# Fichiers de citation
for p in PUBLICATIONS:
    key = f"boutchakkoucht{p['year']}{p['slug'].split('-')[0]}"
    kind = "techreport"
    extra = "  publisher = {Hafid Boutchakkoucht},\n" if kind == "book" else f"  type = {{{p['type']['fr']}}},\n  institution = {{Hafid Boutchakkoucht}},\n"
    write(f"telechargements/{p['slug']}.bib", f"@{kind}{{{key},\n  author = {{Boutchakkoucht, Hafid}},\n  title = {{{p['cite_title']}}},\n  year = {{{p['year']}}},\n{extra}  language = {{french}},\n  url = {{{SITE}/publications/{p['slug']}/}},\n  note = {{ORCID {ORCID}}}\n}}\n")
    ris = ["TY  - " + ("BOOK" if kind == "book" else "RPRT"), "AU  - Boutchakkoucht, Hafid", f"TI  - {p['cite_title']}", f"PY  - {p['year']}", f"DA  - {p['date'].replace('-', '/')}", "LA  - fr",
           f"AB  - {p['abstract']['fr']}"] + [f"KW  - {k}" for k in p["keywords"]["fr"]] + [f"UR  - {SITE}/publications/{p['slug']}/", f"L1  - {SITE}/telechargements/{p['pdf']}", "ER  - "]
    write(f"telechargements/{p['slug']}.ris", "\n".join(ris) + "\n")

# Fichiers techniques
write("CNAME", SITE.replace("https://", "") + "\n")
write(".nojekyll", "")
write("assets/icon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#7A1F2B"/><path d="M10 20h18c8 0 10-6 16-6s6 6 10 6M10 32h18c8 0 10 7 16 7s6-7 10-7M10 44h18c8 0 10-6 16-6s6 6 10 6" fill="none" stroke="#F6F2EA" stroke-width="3.2" stroke-linecap="round"/></svg>\n')
urls = [f"{SITE}/{HOME[l] + '/' if HOME[l] else ''}" for l in LANGS] + [f"{SITE}/{VID_DIR[l]}/" for l in LANGS] + [f"{SITE}/{FILM_URL}"] + [f"{SITE}/{PUB_DIR[l]}/{p['slug']}/" for l in LANGS for p in PUBLICATIONS] + [f"{SITE}/fiches/{f['slug']}/" for f in FICHES] + [f"{SITE}/fiches-france/{f['slug']}/" for f in FICHES_FR] + [f"{SITE}/{LX.L_DIR[l]}/" for l in LANGS] + [f"{SITE}/{AB_DIR[l]}/" for l in LANGS] + [f"{SITE}/enquete/"] + ([f"{SITE}/{QZ.Q_DIR[l]}/" for l in LANGS] if QZ.ENDPOINT else [])
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{x}</loc></url>\n" for x in urls) + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
entries = "".join(f"""  <entry><title>{e(p['title']['fr'])}</title><link href="{SITE}/publications/{p['slug']}/"/><id>{SITE}/publications/{p['slug']}/</id><updated>{p['date'] if len(p['date']) > 4 else p['date'] + '-01-01'}T00:00:00Z</updated><summary>{e(p['comment']['fr'])}</summary></entry>\n""" for p in PUBLICATIONS)
write("feed.xml", f"""<?xml version="1.0" encoding="utf-8"?>\n<feed xmlns="http://www.w3.org/2005/Atom">\n  <title>{e(SITE_TITLE['fr'])} — {AUTHOR}</title><link href="{SITE}/"/><link rel="self" href="{SITE}/feed.xml"/><id>{SITE}/</id><updated>{max(p['date'] for p in PUBLICATIONS if len(p['date']) > 4)}T00:00:00Z</updated><author><name>{AUTHOR}</name></author>\n{entries}</feed>\n""")
print("OK —", len(urls), "pages")
