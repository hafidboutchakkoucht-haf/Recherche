# La norme et le réel — Hafid Boutchakkoucht

Carnet de recherche publié sur `hafidboutchakkoucht.crossborders.ngo` (français et anglais).

| Quoi | Où |
| --- | --- |
| Textes, études, vidéos, biographie (FR et EN) | `contenu.py` |
| Mise en page | `assets/style.css` |
| Filtres, thème, copie de référence | `assets/app.js` |
| PDF des études, fichiers BibTeX et RIS | `telechargements/` |

Après une modification :

```bash
python3 build.py
```

Pour refaire le recueil PDF (nécessite node, playwright et pdfunite) :

```bash
python3 recueil.py
```

Mise en ligne : Settings → Pages → « Deploy from a branch », branche `main`, dossier `/ (root)`.
