"""Questionnaire « Jeunesses et engagement » (anonyme, réservé aux 18-30 ans), en quatre langues.

POUR L'ACTIVER : coller ci-dessous l'adresse de réception des réponses (par exemple une adresse Formspree
du type https://formspree.io/f/xxxxxxx), puis relancer build.py.  Tant que ENDPOINT est vide, la page est
générée en mode « aperçu » : elle n'est pas liée depuis le site, pas indexée, et l'envoi est désactivé."""

ENDPOINT = ""          # adresse qui reçoit les réponses
TOOL_NAME = ""         # nom de l'outil de collecte, affiché dans la notice (ex. « Formspree »)

Q_DIR = {"fr": "questionnaire", "en": "en/questionnaire", "es": "es/cuestionario", "ar": "ar/questionnaire"}
L = ("fr", "en", "es", "ar")
t = lambda *v: dict(zip(L, v))

TXT = {
    "kicker": t("Enquête · Jeunesses et engagement", "Survey · Youth and engagement", "Encuesta · Juventudes y compromiso", "استطلاع · الشباب والالتزام"),
    "h1": t("Votre voix <em>compte</em>", "Your voice <em>matters</em>", "Tu voz <em>cuenta</em>", "صوتك <em>مهم</em>"),
    "lead": t("Vous avez entre 18 et 30 ans ? Ce questionnaire anonyme prend cinq minutes. Il nourrit une recherche sur la manière dont les jeunes s’informent, s’engagent et se mobilisent, au Maroc et en Europe.",
              "Are you between 18 and 30? This anonymous questionnaire takes five minutes. It feeds research on how young people get informed, get involved and mobilise, in Morocco and in Europe.",
              "¿Tienes entre 18 y 30 años? Este cuestionario anónimo dura cinco minutos. Alimenta una investigación sobre cómo los jóvenes se informan, se comprometen y se movilizan, en Marruecos y en Europa.",
              "هل عمرك بين 18 و30 سنة؟ هذا الاستطلاع المجهول الهوية يستغرق خمس دقائق. يغذّي بحثًا حول الطريقة التي يطّلع بها الشباب ويلتزمون ويتعبّؤون، في المغرب وفي أوروبا."),
    "facts": [t("5 minutes", "5 minutes", "5 minutos", "5 دقائق"), t("Anonyme", "Anonymous", "Anónimo", "مجهول الهوية"), t("18 – 30 ans", "Ages 18–30", "18 – 30 años", "18 – 30 سنة"), t("Aucune donnée personnelle", "No personal data", "Ningún dato personal", "بلا معطيات شخصية")],
    "notice_k": t("Avant de commencer", "Before you start", "Antes de empezar", "قبل البدء"),
    "notice": t("Ce questionnaire est mené par Hafid Boutchakkoucht dans le cadre de ses recherches personnelles sur les jeunesses et l’engagement. Il est anonyme : aucun nom, aucune adresse électronique et aucun numéro de téléphone ne sont demandés. N’écrivez rien qui permette de vous identifier. Les réponses sont utilisées uniquement à des fins de recherche et présentées sous forme de résultats d’ensemble. Vous pouvez arrêter à tout moment : rien n’est envoyé tant que vous n’avez pas validé.",
                "This questionnaire is run by Hafid Boutchakkoucht as part of his personal research on youth and engagement. It is anonymous: no name, email address or phone number is requested. Do not write anything that could identify you. Answers are used for research purposes only and presented as aggregate results. You can stop at any time: nothing is sent until you submit.",
                "Este cuestionario lo realiza Hafid Boutchakkoucht en el marco de sus investigaciones personales sobre las juventudes y el compromiso. Es anónimo: no se pide nombre, correo electrónico ni número de teléfono. No escribas nada que permita identificarte. Las respuestas se utilizan únicamente con fines de investigación y se presentan como resultados de conjunto. Puedes parar en cualquier momento: no se envía nada hasta que valides.",
                "يُجري هذا الاستطلاع حفيظ بوتشكوشت في إطار أبحاثه الشخصية حول الشباب والالتزام. وهو مجهول الهوية: لا يُطلب اسم ولا بريد إلكتروني ولا رقم هاتف. لا تكتب ما يمكن أن يعرّف بك. تُستعمل الأجوبة لأغراض البحث فقط، وتُعرض في شكل نتائج إجمالية. يمكنك التوقف في أي لحظة: لا يُرسل أي شيء قبل أن تؤكد."),
    "tool": t("Les réponses sont collectées au moyen de l’outil {tool}.", "Answers are collected with the {tool} tool.", "Las respuestas se recogen mediante la herramienta {tool}.", "تُجمع الأجوبة بواسطة أداة {tool}."),
    "c_age": t("J’ai 18 ans ou plus.", "I am 18 or older.", "Tengo 18 años o más.", "عمري 18 سنة أو أكثر."),
    "c_ok": t("J’accepte que mes réponses anonymes soient utilisées à des fins de recherche.", "I agree that my anonymous answers may be used for research purposes.", "Acepto que mis respuestas anónimas se utilicen con fines de investigación.", "أوافق على استعمال أجوبتي المجهولة الهوية لأغراض البحث."),
    "send": t("Envoyer mes réponses", "Send my answers", "Enviar mis respuestas", "إرسال أجوبتي"),
    "sending": t("Envoi en cours…", "Sending…", "Enviando…", "جارٍ الإرسال…"),
    "thanks_h": t("Merci.", "Thank you.", "Gracias.", "شكرًا."),
    "thanks": t("Vos réponses ont bien été enregistrées. Partagez ce questionnaire autour de vous : chaque réponse compte.", "Your answers have been recorded. Share this questionnaire: every answer counts.", "Tus respuestas se han registrado. Comparte este cuestionario: cada respuesta cuenta.", "تم تسجيل أجوبتك. شارك هذا الاستطلاع مع من حولك: كل جواب مهم."),
    "error": t("L’envoi a échoué. Vérifiez votre connexion et réessayez.", "Sending failed. Check your connection and try again.", "El envío ha fallado. Comprueba tu conexión e inténtalo de nuevo.", "تعذّر الإرسال. تحقق من الاتصال وحاول من جديد."),
    "preview": t("Aperçu : le questionnaire n’est pas encore ouvert. Les réponses ne sont pas enregistrées.", "Preview: the questionnaire is not open yet. Answers are not recorded.", "Vista previa: el cuestionario aún no está abierto. Las respuestas no se registran.", "معاينة: الاستطلاع لم يُفتح بعد. الأجوبة لا تُسجَّل."),
    "optional": t("facultatif", "optional", "opcional", "اختياري"),
    "multi": t("plusieurs réponses possibles", "several answers possible", "varias respuestas posibles", "يمكن اختيار أكثر من جواب"),
    "max3": t("trois réponses au maximum", "up to three answers", "tres respuestas como máximo", "ثلاثة أجوبة على الأكثر"),
    "scale": t("1 = aucune confiance · 5 = confiance totale", "1 = no trust · 5 = full trust", "1 = ninguna confianza · 5 = confianza total", "1 = لا ثقة · 5 = ثقة تامة"),
    "progress": t("question", "question", "pregunta", "سؤال"),
    "cta_k": t("Enquête en cours", "Survey in progress", "Encuesta en curso", "استطلاع جارٍ"),
    "cta_h": t("Vous avez entre 18 et 30 ans ?", "Are you between 18 and 30?", "¿Tienes entre 18 y 30 años?", "هل عمرك بين 18 و30 سنة؟"),
    "cta_p": t("Cinq minutes, anonyme : dites comment vous vous informez et vous engagez.", "Five minutes, anonymous: tell us how you get informed and get involved.", "Cinco minutos, anónimo: cuenta cómo te informas y te comprometes.", "خمس دقائق، دون ذكر الهوية: أخبرنا كيف تطّلع وكيف تلتزم."),
    "cta_b": t("Répondre au questionnaire", "Take the questionnaire", "Responder al cuestionario", "المشاركة في الاستطلاع"),
}

SECTIONS = [
    t("Vous", "About you", "Sobre ti", "عنك"),
    t("S’informer", "Getting informed", "Informarse", "الاطلاع"),
    t("S’engager", "Getting involved", "Comprometerse", "الالتزام"),
    t("Confiance", "Trust", "Confianza", "الثقة"),
    t("Et après ?", "What next?", "¿Y después?", "وماذا بعد؟"),
]

# (identifiant, section, type, question, options, drapeau)   type : radio | check | scale | text
QUESTIONS = [
    ("age", 0, "radio", t("Quel âge avez-vous ?", "How old are you?", "¿Qué edad tienes?", "كم عمرك؟"),
     [t("18 – 20 ans", "18–20", "18 – 20 años", "18 – 20 سنة"), t("21 – 24 ans", "21–24", "21 – 24 años", "21 – 24 سنة"), t("25 – 30 ans", "25–30", "25 – 30 años", "25 – 30 سنة")], ""),
    ("pays", 0, "radio", t("Dans quel pays vivez-vous ?", "Which country do you live in?", "¿En qué país vives?", "في أي بلد تعيش؟"),
     [t("Maroc", "Morocco", "Marruecos", "المغرب"), t("France", "France", "Francia", "فرنسا"), t("Espagne", "Spain", "España", "إسبانيا"), t("Autre pays d’Europe", "Another European country", "Otro país de Europa", "بلد أوروبي آخر"), t("Autre", "Other", "Otro", "بلد آخر")], ""),
    ("situation", 0, "radio", t("Quelle est votre situation ?", "What is your situation?", "¿Cuál es tu situación?", "ما هي وضعيتك؟"),
     [t("En études", "Studying", "Estudiando", "أدرس"), t("En emploi", "Working", "Trabajando", "أشتغل"), t("En recherche d’emploi", "Looking for work", "Buscando empleo", "أبحث عن شغل"), t("Autre", "Other", "Otra", "وضعية أخرى")], ""),
    ("genre", 0, "radio", t("Vous êtes…", "You are…", "Eres…", "أنت…"),
     [t("Une femme", "A woman", "Mujer", "امرأة"), t("Un homme", "A man", "Hombre", "رجل"), t("Je préfère ne pas répondre", "I prefer not to say", "Prefiero no responder", "أفضّل عدم الإجابة")], "optional"),
    ("sources", 1, "check", t("Par où vous informez-vous sur la politique et l’actualité ?", "Where do you get your news about politics and current affairs?", "¿Por dónde te informas sobre política y actualidad?", "من أين تستقي أخبار السياسة والأحداث؟"),
     [t("TikTok", "TikTok", "TikTok", "تيك توك"), t("Instagram", "Instagram", "Instagram", "إنستغرام"), t("YouTube", "YouTube", "YouTube", "يوتيوب"), t("Discord", "Discord", "Discord", "ديسكورد"), t("Facebook", "Facebook", "Facebook", "فيسبوك"), t("X (Twitter)", "X (Twitter)", "X (Twitter)", "إكس (تويتر)"),
      t("WhatsApp ou Telegram", "WhatsApp or Telegram", "WhatsApp o Telegram", "واتساب أو تيليغرام"), t("Télévision ou radio", "Television or radio", "Televisión o radio", "التلفزيون أو الإذاعة"), t("Presse en ligne ou papier", "Online or print press", "Prensa digital o en papel", "الصحافة الإلكترونية أو الورقية"), t("Famille et amis", "Family and friends", "Familia y amigos", "العائلة والأصدقاء")], "multi"),
    ("temps", 1, "radio", t("Combien de temps passez-vous chaque jour sur les réseaux sociaux ?", "How much time do you spend on social media each day?", "¿Cuánto tiempo pasas cada día en las redes sociales?", "كم من الوقت تقضي يوميًّا على شبكات التواصل؟"),
     [t("Moins d’une heure", "Less than an hour", "Menos de una hora", "أقل من ساعة"), t("1 à 3 heures", "1 to 3 hours", "De 1 a 3 horas", "من ساعة إلى 3 ساعات"), t("3 à 5 heures", "3 to 5 hours", "De 3 a 5 horas", "من 3 إلى 5 ساعات"), t("Plus de 5 heures", "More than 5 hours", "Más de 5 horas", "أكثر من 5 ساعات")], ""),
    ("actions", 2, "check", t("Au cours des douze derniers mois, avez-vous…", "Over the past twelve months, have you…", "En los últimos doce meses, ¿has…", "خلال الاثني عشر شهرًا الأخيرة، هل…"),
     [t("Partagé un contenu politique en ligne", "Shared political content online", "Compartido contenido político en línea", "شاركت محتوى سياسيًّا على الإنترنت"), t("Signé une pétition en ligne", "Signed an online petition", "Firmado una petición en línea", "وقّعت عريضة إلكترونية"),
      t("Rejoint un groupe ou un serveur de discussion", "Joined a discussion group or server", "Entrado en un grupo o servidor de debate", "انضممت إلى مجموعة أو خادم للنقاش"), t("Participé à une manifestation", "Taken part in a demonstration", "Participado en una manifestación", "شاركت في مظاهرة"),
      t("Adhéré à une association", "Joined an association", "Entrado en una asociación", "انخرطت في جمعية"), t("Adhéré à un parti ou à un syndicat", "Joined a party or a trade union", "Entrado en un partido o un sindicato", "انخرطت في حزب أو نقابة"),
      t("Voté à une élection", "Voted in an election", "Votado en unas elecciones", "صوّتت في انتخابات"), t("Rien de tout cela", "None of these", "Nada de esto", "لا شيء مما سبق")], "multi"),
    ("canal", 2, "radio", t("Si vous avez manifesté, comment en avez-vous entendu parler ?", "If you demonstrated, how did you hear about it?", "Si te manifestaste, ¿cómo te enteraste?", "إذا شاركت في مظاهرة، كيف علمت بها؟"),
     [t("Par un réseau social", "Through social media", "Por una red social", "عبر شبكة للتواصل الاجتماعي"), t("Par des amis ou des proches", "Through friends or relatives", "Por amigos o personas cercanas", "عن طريق الأصدقاء أو الأقارب"), t("Par une association ou un syndicat", "Through an association or a union", "Por una asociación o un sindicato", "عن طريق جمعية أو نقابة"),
      t("Par les médias", "Through the media", "Por los medios de comunicación", "عبر وسائل الإعلام"), t("Je n’ai pas manifesté", "I did not demonstrate", "No me manifesté", "لم أشارك في أي مظاهرة")], "optional"),
    ("declencheur", 2, "radio", t("Qu’est-ce qui vous pousserait le plus à descendre dans la rue ?", "What would most push you to take to the streets?", "¿Qué te empujaría más a salir a la calle?", "ما الذي قد يدفعك أكثر إلى النزول إلى الشارع؟"),
     [t("Un événement qui me choque", "An event that shocks me", "Un hecho que me indigne", "حدث يصدمني"), t("La dégradation de ma situation économique", "My economic situation getting worse", "El empeoramiento de mi situación económica", "تدهور وضعيتي الاقتصادية"),
      t("L’appel de personnes que je connais", "A call from people I know", "El llamamiento de personas que conozco", "دعوة من أشخاص أعرفهم"), t("L’appel d’une organisation", "A call from an organisation", "El llamamiento de una organización", "دعوة من تنظيم"), t("Rien ne me ferait manifester", "Nothing would make me demonstrate", "Nada me haría manifestarme", "لا شيء يدفعني إلى التظاهر")], ""),
    ("confiance", 3, "scale", t("Quelle confiance accordez-vous à…", "How much do you trust…", "¿Cuánta confianza tienes en…", "ما مدى ثقتك في…"),
     [t("Les partis politiques", "Political parties", "Los partidos políticos", "الأحزاب السياسية"), t("Les syndicats", "Trade unions", "Los sindicatos", "النقابات"), t("Le gouvernement", "The government", "El gobierno", "الحكومة"),
      t("Le Parlement", "Parliament", "El Parlamento", "البرلمان"), t("Les associations", "Associations", "Las asociaciones", "الجمعيات"), t("Les médias", "The media", "Los medios de comunicación", "وسائل الإعلام")], ""),
    ("effets", 4, "radio", t("Selon vous, les mobilisations récentes de jeunes ont-elles changé quelque chose ?", "In your view, have recent youth mobilisations changed anything?", "En tu opinión, ¿han cambiado algo las movilizaciones juveniles recientes?", "في رأيك، هل غيّرت تعبئات الشباب الأخيرة شيئًا؟"),
     [t("Oui, beaucoup", "Yes, a lot", "Sí, mucho", "نعم، كثيرًا"), t("Un peu", "A little", "Un poco", "قليلًا"), t("Non", "No", "No", "لا"), t("Je ne sais pas", "I don’t know", "No lo sé", "لا أعرف")], ""),
    ("priorites", 4, "check", t("Quelles sont vos priorités ?", "What are your priorities?", "¿Cuáles son tus prioridades?", "ما هي أولوياتك؟"),
     [t("La santé", "Health", "La salud", "الصحة"), t("L’éducation", "Education", "La educación", "التعليم"), t("L’emploi", "Jobs", "El empleo", "الشغل"), t("Le logement", "Housing", "La vivienda", "السكن"), t("Le coût de la vie", "The cost of living", "El coste de la vida", "غلاء المعيشة"),
      t("La lutte contre la corruption", "Fighting corruption", "La lucha contra la corrupción", "محاربة الفساد"), t("Les libertés", "Freedoms", "Las libertades", "الحريات"), t("Le climat", "The climate", "El clima", "المناخ")], "max3"),
    ("libre", 4, "text", t("Souhaitez-vous ajouter quelque chose ?", "Would you like to add anything?", "¿Quieres añadir algo?", "هل تودّ إضافة شيء؟"), [], "optional"),
]
