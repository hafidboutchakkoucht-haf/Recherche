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

Ajouter une vidéo : déposer le MP4 dans `media/videos/<série>/` et son affiche JPG (même nom) dans `media/videos/posters/`, ajouter la ligne dans `videotheque.py`, puis lancer `python3 build.py`. Une série sans vidéo s'affiche « Bientôt en ligne ».
