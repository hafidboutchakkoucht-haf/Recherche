"""Vidéothèque « Analyses en vidéo » : rubriques, séries et vidéos, en quatre langues.
Pour ajouter une vidéo : déposer le MP4 dans media/videos/<série>/, l'affiche JPG dans media/videos/posters/
(même nom de fichier), ajouter une ligne dans la série concernée, puis lancer build.py.
Une série sans vidéo (items vide) s'affiche « Bientôt en ligne »."""

VID_DIR = {"fr": "videos", "en": "en/videos", "es": "es/videos", "ar": "ar/videos"}
FILM_URL = "films/la-guerre-des-blocus/"

UI_V = {
    "fr": dict(special="Épisode spécial", nav="Vidéos", kicker="Analyses en vidéo", h1="Les guerres, l'État et les idées, <em>en images</em>",
               lead="Des réels courts et des films d'analyse, rangés par rubrique. Chaque vidéo s'appuie sur des sources vérifiables, citées dans la description de la série.",
               home_k="03 · Analyses en vidéo", home_h="Des réels et des films, <em>par rubrique</em>", home_p="Géopolitique, politique nationale, science politique, Europe : toutes les analyses vidéo sont réunies dans la vidéothèque.",
               home_b="Ouvrir la vidéothèque", about_k="04 · À propos", contact_k="05 · Contact",
               featured="Film interactif", film_h="La guerre des blocus", film_p="Six chapitres sur la guerre Iran–États-Unis, avec mon analyse scène par scène, les sources de chaque scène et une version arabe.",
               film_b="Lancer le film interactif", film_b2="Version arabe", film_v="Le film en vidéo (16:9)", film_v_p="La même série montée en un film de 7 min 37, avec musique, en arabe.",
               episodes="épisodes", episode="Épisode", soon="Bientôt en ligne", version="Version", fr="Français", ar="العربية", only_ar="En arabe",
               jump="Rubriques", count_v="vidéos", download="Télécharger", data_note="Données", n_series="séries", min="min"),
    "en": dict(special="Special episode", nav="Videos", kicker="Video analysis", h1="Wars, the state and ideas, <em>on screen</em>",
               lead="Short reels and analysis films, arranged by section. Every video relies on verifiable sources, listed with each series. Most videos are in French or Arabic.",
               home_k="03 · Video analysis", home_h="Reels and films, <em>by section</em>", home_p="Geopolitics, Moroccan politics, political science, Europe: every video analysis is gathered in the video library.",
               home_b="Open the video library", about_k="04 · About", contact_k="05 · Contact",
               featured="Interactive film", film_h="The War of Blockades", film_p="Six chapters on the Iran–United States war, with my analysis of each scene and its sources. In French and Arabic.",
               film_b="Start the interactive film", film_b2="Arabic version", film_v="The film as a video (16:9)", film_v_p="The same series cut into a 7 min 37 film with music (in Arabic).",
               episodes="episodes", episode="Episode", soon="Coming soon", version="Version", fr="Français", ar="العربية", only_ar="In Arabic",
               jump="Sections", count_v="videos", download="Download", data_note="Data", n_series="series", min="min"),
    "es": dict(special="Episodio especial", nav="Vídeos", kicker="Análisis en vídeo", h1="Las guerras, el Estado y las ideas, <em>en imágenes</em>",
               lead="Reels breves y películas de análisis, ordenados por sección. Cada vídeo se apoya en fuentes verificables, citadas en cada serie. La mayoría están en francés o en árabe.",
               home_k="03 · Análisis en vídeo", home_h="Reels y películas, <em>por sección</em>", home_p="Geopolítica, política marroquí, ciencia política, Europa: todos los análisis en vídeo están reunidos en la videoteca.",
               home_b="Abrir la videoteca", about_k="04 · Sobre el autor", contact_k="05 · Contacto",
               featured="Película interactiva", film_h="La guerra de los bloqueos", film_p="Seis capítulos sobre la guerra entre Irán y Estados Unidos, con mi análisis de cada escena y sus fuentes. En francés y en árabe.",
               film_b="Ver la película interactiva", film_b2="Versión árabe", film_v="La película en vídeo (16:9)", film_v_p="La misma serie montada en una película de 7 min 37, con música (en árabe).",
               episodes="episodios", episode="Episodio", soon="Próximamente", version="Versión", fr="Français", ar="العربية", only_ar="En árabe",
               jump="Secciones", count_v="vídeos", download="Descargar", data_note="Datos", n_series="series", min="min"),
    "ar": dict(special="حلقة خاصة", nav="الفيديو", kicker="تحليلات مصوّرة", h1="الحروب والدولة والأفكار، <em>بالصورة</em>",
               lead="ريلز قصيرة وأفلام تحليلية مرتّبة حسب المحاور. كل فيديو يستند إلى مصادر قابلة للتحقق، مذكورة مع كل سلسلة.",
               home_k="03 · تحليلات مصوّرة", home_h="ريلز وأفلام، <em>حسب المحاور</em>", home_p="الجيوسياسة، السياسة الوطنية، العلوم السياسية، أوروبا: كل التحليلات المصوّرة مجموعة في مكتبة الفيديو.",
               home_b="فتح مكتبة الفيديو", about_k="04 · نبذة", contact_k="05 · تواصل",
               featured="فيلم تفاعلي", film_h="حرب الحصارين", film_p="ستة فصول عن الحرب بين إيران والولايات المتحدة، مع تحليلي لكل مشهد ومصادره. بالعربية والفرنسية.",
               film_b="شاهد الفيلم التفاعلي", film_b2="النسخة الفرنسية", film_v="الفيلم بصيغة فيديو (16:9)", film_v_p="السلسلة نفسها في فيلم مدته 7 دقائق و37 ثانية مع موسيقى، بالعربية.",
               episodes="حلقات", episode="الحلقة", soon="قريبًا", version="النسخة", fr="Français", ar="العربية", only_ar="بالعربية",
               jump="المحاور", count_v="فيديو", download="تحميل", data_note="البيانات", n_series="سلاسل", min="د"),
}

def t4(fr, en, es, ar):
    return {"fr": fr, "en": en, "es": es, "ar": ar}

IRAN = [
    ("1", t4("Frappe ou accord ?", "Strike or deal?", "¿Ataque o acuerdo?", "ضربة أم صفقة")),
    ("2", t4("240 jours", "240 days", "240 días", "240 يومًا")),
    ("3", t4("Le théâtre des opérations", "The theatre of operations", "El teatro de operaciones", "مسرح العمليات")),
    ("4", t4("Le prix", "The toll", "El precio", "الثمن")),
    ("5", t4("La guerre des blocus", "The war of blockades", "La guerra de los bloqueos", "حرب الحصارين")),
    ("6", t4("Et maintenant ?", "What next?", "¿Y ahora qué?", "إلى أين")),
]
UKRAINE = [
    ("1", t4("Le prix humain", "The human cost", "El coste humano", "الثمن البشري")),
    ("2", t4("La guerre des chiffres", "The war of numbers", "La guerra de las cifras", "حرب الأرقام")),
    ("3", t4("L'équation de l'usure", "The attrition equation", "La ecuación del desgaste", "معادلة الاستنزاف")),
    ("4", t4("Le coût silencieux", "The silent cost", "El coste silencioso", "الكلفة الصامتة")),
    ("5", t4("À la table des négociations", "At the negotiating table", "En la mesa de negociación", "على طاولة التفاوض")),
    ("6", t4("Où va la guerre ?", "Where is the war heading?", "¿Hacia dónde va la guerra?", "الحرب إلى أين")),
]

# Chaque série : id, titre, présentation, langues disponibles (fr/ar), date des données, dossier, épisodes.
RUBRIQUES = [
    {"id": "geopolitique", "name": t4("Géopolitique et conflits", "Geopolitics and conflict", "Geopolítica y conflictos", "الجيوسياسة والنزاعات"),
     "intro": t4("Les guerres en cours lues par les chiffres, les cartes et les rapports de force.", "Ongoing wars read through figures, maps and the balance of power.",
                 "Las guerras en curso leídas a través de cifras, mapas y relaciones de fuerza.", "الحروب الجارية بقراءة الأرقام والخرائط وموازين القوى."),
     "film": True,
     "series": [
        {"id": "iran", "title": t4("Équilibre des puissances · Iran – États-Unis", "Balance of Power · Iran – United States", "Equilibrio de poderes · Irán – Estados Unidos", "ميزان القوى · إيران وأمريكا"),
         "about": t4("Six épisodes sur la guerre ouverte le 28 février 2026 : la décision de frapper, la chronologie, les fronts, le bilan humain, la guerre des blocus et les scénarios de sortie.",
                     "Six episodes on the war that began on 28 February 2026: the decision to strike, the timeline, the fronts, the human toll, the war of blockades and the ways out.",
                     "Seis episodios sobre la guerra iniciada el 28 de febrero de 2026: la decisión de atacar, la cronología, los frentes, el balance humano, la guerra de los bloqueos y las salidas posibles.",
                     "ست حلقات عن الحرب التي اندلعت في 28 فبراير 2026: قرار الضربة، والتسلسل الزمني، والجبهات، والحصيلة البشرية، وحرب الحصارين، وسيناريوهات الخروج."),
         "data": t4("Épisodes 1 à 5 : données au 24 octobre 2026 · épisode 6 mis à jour au 10 novembre 2026", "Episodes 1–5: data as of 24 October 2026 · episode 6 updated on 10 November 2026",
                    "Episodios 1 a 5: datos al 24 de octubre de 2026 · episodio 6 actualizado el 10 de noviembre de 2026", "الحلقات 1 إلى 5: بيانات إلى 24 أكتوبر 2026 · الحلقة 6 محدَّثة إلى 10 نوفمبر 2026"),
         "langs": ["fr", "ar"], "dir": "iran", "file": "iran-{lang}-{n}", "items": IRAN},
        {"id": "ukraine", "title": t4("Le compte de la guerre · Russie – Ukraine", "The War Ledger · Russia – Ukraine", "La cuenta de la guerra · Rusia – Ucrania", "حساب الحرب · روسيا وأوكرانيا"),
         "about": t4("Six épisodes sur le coût de la guerre : les pertes humaines, la bataille des chiffres, l'usure, le coût pour les civils, la négociation et les perspectives.",
                     "Six episodes on the cost of the war: human losses, the battle over figures, attrition, the cost to civilians, negotiation and prospects.",
                     "Seis episodios sobre el coste de la guerra: las pérdidas humanas, la batalla de las cifras, el desgaste, el coste para los civiles, la negociación y las perspectivas.",
                     "ست حلقات عن كلفة الحرب: الخسائر البشرية، ومعركة الأرقام، والاستنزاف، وكلفة المدنيين، والتفاوض، والآفاق."),
         "data": None, "langs": ["ar"], "dir": "ukraine", "file": "ukraine-ar-{n}", "items": UKRAINE},
        {"id": "ormuz", "title": t4("Ormuz · le détroit qui étrangle le monde", "Hormuz · the strait that chokes the world", "Ormuz · el estrecho que estrangula al mundo", "هرمز · المضيق الذي يخنق العالم"),
         "about": t4("Épisode spécial sur le détroit d'Ormuz, son poids dans le commerce pétrolier mondial et l'usage qu'en fait Téhéran.",
                     "A special episode on the Strait of Hormuz, its weight in world oil trade and how Tehran uses it.",
                     "Episodio especial sobre el estrecho de Ormuz, su peso en el comercio mundial de petróleo y el uso que hace de él Teherán.",
                     "حلقة خاصة عن مضيق هرمز ووزنه في تجارة النفط العالمية واستعمال طهران له."),
         "data": None, "langs": ["ar"], "dir": "ormuz", "file": "ormuz-ar", "items": [("", t4("Ormuz", "Hormuz", "Ormuz", "هرمز"))]},
     ]},
    {"id": "maroc", "name": t4("Politique nationale · Maroc", "Moroccan politics", "Política nacional · Marruecos", "السياسة الوطنية · المغرب"),
     "intro": t4("Le gouvernement, le budget et les grands dossiers de l'État marocain, examinés à l'aune de leur mise en œuvre.", "Morocco's government, budget and major state files, examined through their implementation.",
                 "El gobierno, el presupuesto y los grandes expedientes del Estado marroquí, examinados a la luz de su ejecución.", "الحكومة والميزانية والملفات الكبرى للدولة المغربية، من زاوية التنفيذ."),
     "series": [
        {"id": "gouv", "title": t4("Gouvernement 2026 – 2031", "Government 2026 – 2031", "Gobierno 2026 – 2031", "حكومة 2026 – 2031"), "items": []},
        {"id": "plf", "title": t4("Loi de finances 2027", "2027 Finance Act", "Ley de Finanzas 2027", "قانون المالية 2027"), "items": []},
        {"id": "compensation", "title": t4("La Caisse de compensation", "The Compensation Fund", "La Caja de Compensación", "صندوق المقاصة"), "items": []},
        {"id": "sahara", "title": t4("Sahara marocain · le dossier", "Moroccan Sahara · the file", "Sáhara marroquí · el expediente", "الصحراء المغربية · الملف"), "items": []},
     ]},
    {"id": "idees", "name": t4("Science politique et idées", "Political science and ideas", "Ciencia política e ideas", "العلوم السياسية والأفكار"),
     "intro": t4("Les livres qui expliquent le monde et les générations qui le transforment.", "The books that explain the world and the generations that are changing it.",
                 "Los libros que explican el mundo y las generaciones que lo transforman.", "الكتب التي تفسّر العالم والأجيال التي تغيّره."),
     "series": [
        {"id": "bibliotheque", "title": t4("La bibliothèque géopolitique", "The geopolitical library", "La biblioteca geopolítica", "المكتبة الجيوسياسية"), "items": []},
        {"id": "jeunesses", "title": t4("Jeunesses en mouvement · Europe et Maroc", "Youth on the move · Europe and Morocco", "Juventudes en movimiento · Europa y Marruecos", "شباب في حراك · أوروبا والمغرب"), "items": []},
     ]},
    {"id": "europe", "name": t4("Europe et jeunesse", "Europe and youth", "Europa y juventud", "أوروبا والشباب"),
     "intro": t4("Les dispositifs européens expliqués simplement, pour les jeunes et les associations.", "European programmes explained simply, for young people and associations.",
                 "Los programas europeos explicados de forma sencilla, para jóvenes y asociaciones.", "البرامج الأوروبية بشرح مبسّط للشباب والجمعيات."),
     "series": [
        {"id": "erasmus", "title": t4("Erasmus+ décrypté", "Erasmus+ explained", "Erasmus+ explicado", "إيراسموس+ بوضوح"), "items": []},
     ]},
]
