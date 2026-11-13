"""Contenu du site « La norme et le réel ».  Tout le texte modifiable est ici, en français (fr) et en anglais (en).
Pour ajouter une étude : copier un bloc de PUBLICATIONS, déposer le PDF dans telechargements/, puis lancer build.py."""

SITE = "https://hafidboutchakkoucht.crossborders.ngo"
SITE_TITLE = {"fr": "La norme et le réel", "en": "Norm and Reality"}
AUTHOR = "Hafid Boutchakkoucht"
ORCID = "0009-0007-3785-5570"
EMAIL = "hafidboutchakkoucht@gmail.com"
MAIN_SITE = "https://www.crossborders.ngo"

BIO = {
    "fr": "Chercheur en droit pénal comparé et sciences criminelles, Hafid Boutchakkoucht travaille sur ce que les frontières font au droit et sur ce que les programmes politiques deviennent lorsqu’il faut les exécuter. Il est le fondateur et le président de l’association Cross Borders, qui conduit des projets européens de mobilité et d’inclusion.",
    "en": "A researcher in comparative criminal law and criminal sciences, Hafid Boutchakkoucht studies what borders do to law, and what political programmes become when they have to be implemented. He is the founder and president of Cross Borders, a non-profit running European mobility and inclusion projects.",
}

AXES = [
    {"fr": ("Droit pénal comparé et sciences criminelles", "Souveraineté territoriale, criminalités transnationales, espace pénal européen et jurisprudence de la Cour européenne des droits de l’homme."),
     "en": ("Comparative criminal law and criminal sciences", "Territorial sovereignty, transnational crime, the European criminal law area and the case law of the European Court of Human Rights.")},
    {"fr": ("Politiques publiques et mise en œuvre", "Faisabilité des programmes de gouvernement, gouvernance de coalition, finances publiques et architecture d’exécution."),
     "en": ("Public policy and implementation", "Feasibility of government programmes, coalition governance, public finance and delivery architecture.")},
]

# Thèmes de la bibliothèque (filtres)
TOPICS = {
    "droit": {"fr": "Droit pénal", "en": "Criminal law"},
    "politiques": {"fr": "Politiques publiques", "en": "Public policy"},
}

PUBLICATIONS = [
    {
        "slug": "ingenierie-des-promesses", "topic": "politiques", "year": "2026", "date": "2026-10-02", "pages": 41,
        "pdf": "boutchakkoucht-2026-ingenierie-des-promesses.pdf", "lang_note": {"fr": "Texte en français", "en": "Full text in French"},
        "date_txt": {"fr": "2 octobre 2026", "en": "2 October 2026"},
        "type": {"fr": "Note d’analyse stratégique", "en": "Strategic policy note"},
        "title": {"fr": "De l’ingénierie des promesses à l’ingénierie de l’État", "en": "From the Engineering of Promises to the Engineering of the State"},
        "subtitle": {"fr": "La faisabilité du programme du Parti Authenticité et Modernité pour la législature 2027–2031", "en": "The feasibility of the Authenticity and Modernity Party’s programme for the 2027–2031 legislature"},
        "strap": {"fr": "Économie politique, gouvernance de coalition et théorie de la mise en œuvre des politiques publiques", "en": "Political economy, coalition governance and public policy implementation theory"},
        "abstract": {
            "fr": "La présente étude évalue la faisabilité du programme du Parti Authenticité et Modernité (PAM) pour la législature 2027–2031, à la lumière de la théorie de la mise en œuvre des politiques publiques (Pressman et Wildavsky, Lipsky, Tsebelis, Matland, Barber). En s’appuyant sur le programme officiel, sur le cadrage macroéconomique du projet de loi de finances 2027 et sur les séries du Haut-Commissariat au Plan, elle montre que le « dividende de croissance » de 300 milliards de dirhams suppose une croissance de référence de 1,3 % à 2 % seulement, et que l’objectif d’un million d’emplois nets repose sur une élasticité huit fois supérieure à celle observée en 2022–2025. Elle propose une architecture d’exécution et quatre scénarios à l’horizon 2031.",
            "en": "This study assesses the implementability of the Authenticity and Modernity Party’s (PAM) 2027–2031 programme in Morocco through the lens of implementation theory. Drawing on the party’s official programme, the 2027 budget framework and High Commission for Planning data, it finds that the claimed MAD 300 billion growth dividend implies a counterfactual growth rate of only 1.3–2%, and that the one-million-net-jobs target assumes an employment elasticity eight times higher than observed in 2022–2025. It proposes a delivery architecture and four scenarios for 2031."},
        "comment": {
            "fr": "Cette note ne juge pas le programme sur ses intentions mais sur sa capacité à être exécuté. Sa thèse tient en une formule, le « paradoxe du mandat étroit et du programme large » : un programme conçu pour une majorité absolue devra être mis en œuvre par une coalition, avec un mandat électoral restreint et un premier budget préparé par le gouvernement sortant.",
            "en": "This note does not judge the programme on its intentions but on its capacity to be delivered. Its thesis fits in one phrase, the “paradox of the narrow mandate and the broad programme”: a programme designed for an absolute majority will have to be implemented by a coalition, on a limited electoral mandate and with a first budget prepared by the outgoing government."},
        "points": {
            "fr": ["Le coût annuel du programme (70 milliards de dirhams) dépasse à lui seul le déficit autorisé : chaque dépense nouvelle suppose une ressource nouvelle.",
                   "Le « dividende de croissance » de 300 milliards n’est atteint que si l’on suppose une économie quasi stagnante sans le programme.",
                   "L’objectif d’un million d’emplois repose sur une élasticité huit fois supérieure à celle que les chiffres du programme font eux-mêmes apparaître pour 2022–2025.",
                   "Tout se joue dans les cent premiers jours : un pacte de majorité conçu comme un contrat d’exécution, une annexe financière publique en trois scénarios, et une unité de mise en œuvre resserrée sur dix engagements."],
            "en": ["The programme’s annual cost (MAD 70 billion) alone exceeds the authorised deficit: every new expense requires a new resource.",
                   "The MAD 300 billion “growth dividend” is only reached if one assumes a near-stagnant economy without the programme.",
                   "The one-million-jobs target relies on an elasticity eight times higher than the one the programme’s own figures show for 2022–2025.",
                   "Everything is decided in the first hundred days: a majority pact designed as a delivery contract, a public financial annex in three scenarios, and a delivery unit focused on ten commitments."]},
        "readers": {"fr": "Décideurs publics, journalistes économiques, chercheurs en politiques publiques et étudiants en science politique.",
                    "en": "Policy-makers, economic journalists, public policy researchers and political science students."},
        "figures": [("350", {"fr": "milliards de dirhams de coût additionnel sur la législature", "en": "billion dirhams of additional cost over the legislature"}),
                    ("× 8", {"fr": "l’écart entre l’élasticité emploi supposée et celle observée", "en": "the gap between assumed and observed employment elasticity"}),
                    ("4", {"fr": "scénarios à l’horizon 2031", "en": "scenarios for 2031"}),
                    ("10", {"fr": "recommandations", "en": "recommendations"})],
        "outline": {
            "fr": ["Problématique et thèse", "Le mandat du 23 septembre 2026 en chiffres", "Le laboratoire 2021–2026", "Cadre théorique", "L’ingénierie de coalition", "L’architecture constitutionnelle des compétences", "Test de résistance budgétaire", "Un million d’emplois", "Tests sectoriels", "L’ingénierie de l’exécution", "Calendrier, matrice des risques et tableau de bord", "Quatre scénarios à l’horizon 2031", "Conclusion générale et dix recommandations"],
            "en": ["Research question and thesis", "The 23 September 2026 mandate in figures", "The 2021–2026 laboratory", "Theoretical framework", "Coalition engineering", "The constitutional architecture of powers", "Fiscal stress test", "One million jobs", "Sector tests", "Delivery engineering", "Timeline, risk matrix and dashboard", "Four scenarios for 2031", "General conclusion and ten recommendations"]},
        "keywords": {"fr": ["Maroc", "politiques publiques", "mise en œuvre", "gouvernement de coalition", "finances publiques", "test de résistance budgétaire", "emploi", "unité de mise en œuvre"],
                     "en": ["Morocco", "public policy", "implementation", "coalition government", "public finance", "fiscal stress test", "employment", "delivery unit"]},
        "cite_title": "De l’ingénierie des promesses à l’ingénierie de l’État : la faisabilité du programme du Parti Authenticité et Modernité pour la législature 2027–2031",
        "cite_tail": {"fr": "Note d’analyse stratégique, 2 octobre 2026.", "en": "Strategic policy note, 2 October 2026."},
    },
    {
        "slug": "droit-penal-post-national", "topic": "droit", "year": "2025", "date": "2025", "pages": 24,
        "pdf": "boutchakkoucht-2025-traite-droit-penal-compare.pdf", "lang_note": {"fr": "Texte en français, titres et résumé bilingues", "en": "Full text in French, bilingual headings and abstract"},
        "date_txt": {"fr": "Édition 2025", "en": "2025 edition"},
        "type": {"fr": "Traité", "en": "Treatise"},
        "title": {"fr": "Traité de droit pénal comparé. Vers un droit pénal post-national ?", "en": "Treatise on Comparative Criminal Law. Toward a Post-National Criminal Law?"},
        "subtitle": {"fr": "Crise de la souveraineté territoriale et recomposition des cadres normatifs à l’ère des criminalités transnationales", "en": "Crisis of territorial sovereignty and the reconfiguration of normative frameworks in the age of transnational crime"},
        "strap": {"fr": "Analyse doctrinale, jurisprudentielle et comparée", "en": "Doctrinal, jurisprudential and comparative analysis"},
        "abstract": {
            "fr": "Ce traité part d’un constat que l’on formule rarement avec franchise dans la littérature académique : le droit pénal que nous enseignons, que nous appliquons et que nous réformons sans relâche depuis deux siècles est profondément inadapté au monde dans lequel nous vivons. Construit autour de la souveraineté territoriale de l’État, il se trouve confronté à des formes de criminalité qui ignorent les frontières, exploitent les failles de la coopération internationale et colonisent l’espace numérique avec une agilité que le droit ne possède pas encore. Ce travail est une tentative de penser le droit pénal à la hauteur de ces transformations — en partant des fondements philosophiques des grandes écoles pénales, en traversant le droit positif comparé et la jurisprudence européenne, pour aboutir à une thèse : celle de l’émergence nécessaire d’un paradigme post-national, fondé non sur la disparition de l’État mais sur la recomposition de sa souveraineté pénale dans un cadre multi-niveaux.",
            "en": "This treatise departs from a candour rarely found in academic writing: the criminal law we have taught, applied, and relentlessly reformed for two centuries is profoundly ill-adapted to the world we actually inhabit. Built around state territorial sovereignty, it confronts forms of criminality that ignore borders, exploit gaps in international cooperation, and colonise digital space with an agility the law has yet to match. This work is an attempt to think criminal law equal to these transformations — moving from the philosophical foundations of the major penal schools, through comparative positive law and European jurisprudence, toward a thesis: the necessary emergence of a post-national paradigm, grounded not in the disappearance of the state but in the recomposition of its penal sovereignty within a multi-level framework."},
        "comment": {
            "fr": "Ce texte prend le contre-pied d’un enseignement qui présente encore le droit pénal comme un édifice national achevé. Il part des grandes écoles pénales pour montrer que la territorialité, pilier du droit pénal moderne, ne suffit plus face à des criminalités qui se jouent entre plusieurs continents et dans l’espace numérique.",
            "en": "This text runs counter to a teaching tradition that still presents criminal law as a finished national edifice. It starts from the major schools of penal thought to show that territoriality, the pillar of modern criminal law, is no longer enough when crime plays out across several continents and in digital space."},
        "points": {
            "fr": ["Une partie préliminaire consacrée aux grandes écoles de pensée pénale, avec une leçon : se méfier des systèmes qui prétendent tout expliquer.",
                   "Un diagnostic : la crise structurelle d’un droit pénal bâti sur la souveraineté territoriale.",
                   "Un détour par le droit positif comparé et par l’espace pénal européen, jurisprudence de la CEDH à l’appui.",
                   "Une thèse : le droit pénal post-national n’est pas un droit pénal sans État, mais un droit où l’État devient un acteur parmi d’autres dans un cadre à plusieurs niveaux."],
            "en": ["A preliminary part on the major schools of penal thought, with one lesson: be wary of systems that claim to explain everything.",
                   "A diagnosis: the structural crisis of a criminal law built on territorial sovereignty.",
                   "A journey through comparative positive law and the European criminal law area, backed by ECtHR case law.",
                   "A thesis: post-national criminal law is not criminal law without the state, but a law in which the state becomes one actor among others within a multi-level framework."]},
        "readers": {"fr": "Étudiants et chercheurs en droit pénal et en sciences criminelles, magistrats, avocats, praticiens de la coopération judiciaire.",
                    "en": "Students and researchers in criminal law and criminal sciences, judges, lawyers and judicial cooperation practitioners."},
        "figures": [("5", {"fr": "parties, des écoles pénales au paradigme post-national", "en": "parts, from the penal schools to the post-national paradigm"}),
                    ("2", {"fr": "siècles de droit pénal territorial remis en question", "en": "centuries of territorial criminal law called into question"}),
                    ("24", {"fr": "pages", "en": "pages"}),
                    ("FR · EN", {"fr": "titres et résumé dans les deux langues", "en": "headings and abstract in both languages"})],
        "outline": {
            "fr": ["Partie préliminaire — Les grandes écoles de pensée pénale : fondements et pertinence", "Partie I — Crise structurelle du paradigme territorial", "Partie II — Le droit pénal positif face aux transformations : résistances et adaptations", "Partie III — L’espace pénal européen : construction inachevée et promesses réelles", "Partie IV — Vers un droit pénal post-national : fondements d’une reconstruction", "Conclusion générale"],
            "en": ["Preliminary part — The major schools of penal thought: foundations and relevance", "Part I — Structural crisis of the territorial paradigm", "Part II — Positive criminal law facing change: resistance and adaptation", "Part III — The European criminal law area: unfinished construction, real promise", "Part IV — Toward a post-national criminal law: foundations of a reconstruction", "General conclusion"]},
        "keywords": {"fr": ["droit pénal post-national", "souveraineté territoriale", "criminalités transnationales", "écoles pénales", "CEDH", "légalité criminelle", "procédure pénale comparée", "espace pénal européen", "intelligence artificielle", "Luhmann", "Delmas-Marty"],
                     "en": ["post-national criminal law", "territorial sovereignty", "transnational crime", "schools of criminal thought", "ECHR", "legality principle", "comparative criminal procedure", "European criminal area", "artificial intelligence", "Luhmann", "Delmas-Marty"]},
        "cite_title": "Traité de droit pénal comparé. Vers un droit pénal post-national ? Crise de la souveraineté territoriale et recomposition des cadres normatifs à l’ère des criminalités transnationales",
        "cite_tail": {"fr": "Édition 2025.", "en": "2025 edition."},
    },
]

# Vidéos : (numéro, thème de série, titre, résumé). Liste vide = aucune vidéo sur le site.
VIDEO_THEMES = []

DISCLAIMER = {
    "fr": "Travaux personnels de Hafid Boutchakkoucht. Les analyses et opinions exprimées sur ce site n’engagent que leur auteur et ne sauraient être attribuées à l’association Cross Borders.",
    "en": "Personal work by Hafid Boutchakkoucht. The analyses and opinions expressed on this site are the author’s own and cannot be attributed to the Cross Borders association.",
}
