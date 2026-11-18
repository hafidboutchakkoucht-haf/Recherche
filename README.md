# La norme et le réel — Hafid Boutchakkoucht

Carnet de recherche publié sur `hafidboutchakkoucht.crossborders.ngo` (français, anglais, espagnol et arabe).

| Quoi | Où |
| --- | --- |
| Textes, études, biographie en français et en anglais | `contenu.py` |
| Traductions espagnole et arabe | `traductions.py` |
| Mise en page | `assets/style.css` |
| Filtres, thème, copie de référence | `assets/app.js` |
| PDF des études, fichiers BibTeX et RIS | `telechargements/` |
| Vidéothèque : rubriques, séries et vidéos (4 langues) | `videotheque.py` |
| Fichiers vidéo (MP4 720p) et affiches | `media/videos/` |
| Film interactif « La guerre des blocus » | `films/la-guerre-des-blocus/` |

Après une modification :

```bash
python3 build.py
```

Pour refaire le recueil PDF (nécessite node, playwright et pdfunite) :

```bash
python3 recueil.py
```

Mise en ligne : Settings → Pages → « Deploy from a branch », branche `main`, dossier `/ (root)`.

Ajouter une vidéo : déposer le MP4 dans `media/videos/<série>/` et son affiche JPG (même nom) dans `media/videos/posters/`, ajouter la ligne dans `videotheque.py`, puis lancer `python3 build.py`. Une série ou une rubrique sans vidéo reste masquée jusqu'à l'ajout de sa première vidéo.

## Fiches, jeunesses et parcours

| Quoi | Où |
| --- | --- |
| Recherches sur les jeunesses, travaux en cours, parcours, libellés des fiches (4 langues) | `sections.py` |
| Fiches de droit pénal français « Droit Clair · France » (12 fiches, regard croisé Maroc) | `fiches_fr.py` |
| Lexique « La constellation des mots » (48 notions, 4 langues) | `lexique.py` |
| Questionnaire « Jeunesses et engagement » (questions, adresse de collecte) | `questionnaire.py` |
| Contenu des 12 fiches Qanoun Clair | `fiches.json`, images dans `fiches/img/` |

Les scripts de `outils/` servent à réimporter les fiches après une mise à jour du pack :
`extraire_fiches.py` (texte), `rendre_fiches.py` et `capturer_fiches.cjs` (images et PDF).

Images de partage des études (réseaux sociaux) : `python3 outils/images_partage.py` (nécessite node et playwright), à relancer après l'ajout d'une étude, puis `python3 build.py`.

## Notes de maintenance

- Site statique généré par `python3 build.py`, sans dépendance. Ne pas modifier à la main les `index.html` générés : modifier les modules, puis relancer le générateur. Exceptions écrites à la main : `films/la-guerre-des-blocus/index.html` et `enquete/index.html`.
- Quatre langues : français (racine), `en/`, `es/`, `ar/` (droite à gauche). Tout texte ajouté doit exister dans les quatre langues, sauf les fiches de droit (français, titres en arabe).
- Tout doit rester gratuit : aucun service ni domaine payant. Publication directe sur `main`.
- Conserver la ligne `goatcounter` en bas de chaque page (mesure d'audience anonyme).
- Avant toute modification, repartir de la version en ligne (`git fetch origin main`) ; ne jamais écraser un travail en cours ni forcer une publication sans accord.
- Avant de publier : `python3 build.py`, contrôle des pages modifiées sur téléphone (390 px) et sur ordinateur (1280 px), y compris en arabe ; vérification des liens internes.
- Ton : professionnel, sobre, universitaire. Lecteurs visés : chercheurs, journalistes, responsables publics.
- Présentation de l'auteur : s'en tenir aux formulations présentes dans `sections.py` et `contenu.py` ; n'ajouter aucun titre, fonction, employeur ou projet personnel sans accord de l'auteur.
- Contenus juridiques : citer les articles, indiquer la source et la date de vérification, garder l'avertissement « support pédagogique ».
- Les vidéos de l'association Cross Borders (Erasmus+) n'ont pas leur place sur ce site.
- Aucune mention d'un outil ou d'un assistant d'intelligence artificielle sur le site, dans les documents ou dans l'historique des modifications.
