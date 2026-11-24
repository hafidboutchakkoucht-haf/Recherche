# Consignes de travail sur ce dépôt

Site « La norme et le réel », carnet de recherche de Hafid Boutchakkoucht,
publié sur https://hafidboutchakkoucht.crossborders.ngo (GitHub Pages, branche `main`).

**À lire aussi avant toute tâche : `JOURNAL.md`** (décisions déjà prises, travail en cours).
À la fin de chaque tâche, ajouter en tête de `JOURNAL.md` une entrée datée de 3 à 6 lignes.

## Comment répondre à l'auteur

- En français simple, ton professionnel, réponses courtes.
- Proposer les modifications importantes avant de les appliquer ; les petites corrections se font directement.
- Donner un avis honnête, sans flatterie.
- Tout doit rester gratuit : aucun service, domaine ou outil payant.

## Construire, vérifier, publier

1. `git fetch origin main` puis repartir de la version en ligne : une autre conversation peut travailler en même temps. Ne jamais forcer une publication.
2. Modifier les modules Python ou `assets/`, jamais les `index.html` générés (exceptions : `films/la-guerre-des-blocus/index.html`, `enquete/index.html`).
3. `PYTHONDONTWRITEBYTECODE=1 python3 build.py`.
4. Vérifier les pages modifiées à 390 px et 1280 px, en français et en arabe, ainsi que les liens internes.
5. Commit au nom de l'auteur : `git -c user.name="Hafid Boutchakkoucht" -c user.email="hafidboutchakkoucht@users.noreply.github.com" commit`. Le message de commit ne contient aucune mention d'outil ou d'assistant, ni co-auteur, ni lien de session.
6. `git push origin main`.

## Où se trouve quoi

| Quoi | Où |
| --- | --- |
| Accueil (parcours, ressources, libellés) et page des fiches, 4 langues | `accueil.py` |
| Textes des études, biographie | `contenu.py` ; traductions espagnol et arabe : `traductions.py` |
| Jeunesses, travaux en cours, page « Autres engagements » | `sections.py` |
| Vidéothèque | `videotheque.py`, fichiers dans `media/videos/` |
| Lexique, questionnaire, fiches France | `lexique.py`, `questionnaire.py`, `fiches_fr.py` |
| Mise en page, polices intégrées (licence OFL) | `assets/style.css`, `assets/fonts/` |

Quatre langues : français (racine), `en/`, `es/`, `ar/` (droite à gauche). Tout texte ajouté existe dans les quatre.
Conserver la ligne `goatcounter` en bas de chaque page. Conserver les compteurs de l'accueil.

## Présentation de l'auteur

- Titre : « chercheur » uniquement. Jamais « docteur », « Dr », « PhD », « professeur ».
- Ne mentionner aucun projet personnel d'études ou de candidature ; parler de « recherches sur les jeunesses ».
- Service public : s'en tenir à « membre de la fonction publique ». Aucun employeur, grade ni organisme national de formation.
- Presse : « auteur d'articles » dans DairaNews, Casanews et sur EasyChair, sans aucune fonction dans un média.
- Cyclad Consulting : « expérience du conseil au sein du cabinet », jamais « consultant ».
- N'ajouter aucun titre, fonction, employeur ou projet personnel sans l'accord de l'auteur.
- Aucune mention d'un outil ou d'un assistant d'intelligence artificielle sur le site ni dans les documents.
- Pas de vidéos de l'association Cross Borders (Erasmus+) sur ce site.

## Style du site

Sobre et universitaire, pour des chercheurs, des journalistes et des décideurs : fond blanc, un seul accent bordeaux.
À éviter : sections numérotées « 01 / 02 », rangées de cases identiques, mots en italique coloré dans les titres,
bandeaux défilants, animations au défilement, gadgets. Portrait en haut de l'accueil, sans cadre ni cercle.
