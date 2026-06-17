# VibeVoice-ASR Carnet Colab

Ce carnet retranscrit des fichiers audio ou vidéo.

## Fonctionnalités

- **Utilisation gratuite :** Ce bloc-notes utilise [VibeVoice-ASR](https://github.com/microsoft/VibeVoice), que Microsoft a publié en open source le 21 janvier 2026, ainsi que le runtime gratuit GPU de Google Colab. Pour rendre le modèle utilisable sur des GPU gratuits, ce notebook utilise un modèle VibeVoice-ASR quantifié.
- **Aucune limite fixe de taille de fichier côté ordinateur portable :** Les fichiers audio et vidéo volumineux peuvent être traités en les divisant en segments.
- **Traitement par lots :** Plusieurs fichiers audio et vidéo peuvent être traités en une seule fois.
- Prise en charge **Google Drive :** Les fichiers peuvent être téléchargés directement ou les fichiers audio/vidéo stockés dans Google Drive peuvent être traités.
- **Entièrement en ligne :** Les téléchargements et le traitement sont effectués sur Google Colab. Aucune ressource informatique locale n'est utilisée.
- **Plusieurs formats de sortie :** Le bloc-notes génère la transcription originale JSON et les fichiers de sous-titres dérivés TXT, CSV, Markdown, Excel et SRT.

## Langues

| Langue | README | Carnet |
| --- | --- | --- |
| English (United States) | [`README.md`](../../README.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_en.ipynb) |
| 中文 (簡体字) | [`README.zh-CN.md`](README.zh-CN.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_zh-CN.ipynb) |
| 中文 (繁体字) | [`README.zh-TW.md`](README.zh-TW.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_zh-TW.ipynb) |
| Español | [`README.es.md`](README.es.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_es.ipynb) |
| Português | [`README.pt-PT.md`](README.pt-PT.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_pt-PT.ipynb) |
| português | [`README.pt-BR.md`](README.pt-BR.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_pt-BR.ipynb) |
| Deutsch | [`README.de.md`](README.de.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_de.ipynb) |
| 日本語 | [`README.ja.md`](README.ja.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_ja.ipynb) |
| 한국어 | [`README.ko.md`](README.ko.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_ko.ipynb) |
| français | [`README.fr.md`](README.fr.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_fr.ipynb) |
| русский | [`README.ru.md`](README.ru.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_ru.ipynb) |
| Bahasa Indonesia | [`README.id.md`](README.id.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_id.ipynb) |
| svenska | [`README.sv.md`](README.sv.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_sv.ipynb) |
| italiano | [`README.it.md`](README.it.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_it.ipynb) |
| עברית | [`README.he.md`](README.he.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_he.ipynb) |
| Nederlands | [`README.nl.md`](README.nl.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_nl.ipynb) |
| polski | [`README.pl.md`](README.pl.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_pl.ipynb) |
| norsk, bokmål | [`README.nb.md`](README.nb.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_nb.ipynb) |
| Türkçe | [`README.tr.md`](README.tr.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_tr.ipynb) |
| ไทย | [`README.th.md`](README.th.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_th.ipynb) |
| العربية | [`README.ar.md`](README.ar.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_ar.ipynb) |
| magyar | [`README.hu.md`](README.hu.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_hu.ipynb) |
| Català | [`README.ca.md`](README.ca.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_ca.ipynb) |
| čeština | [`README.cs.md`](README.cs.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_cs.ipynb) |
| dansk | [`README.da.md`](README.da.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_da.ipynb) |
| فارسی | [`README.fa.md`](README.fa.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_fa.ipynb) |
| Afrikaans | [`README.af.md`](README.af.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_af.ipynb) |
| हिंदी | [`README.hi.md`](README.hi.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_hi.ipynb) |
| suomi | [`README.fi.md`](README.fi.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_fi.ipynb) |
| eesti | [`README.et.md`](README.et.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_et.ipynb) |
| Qafar af | [`README.aa.md`](README.aa.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_aa.ipynb) |
| Ελληνικά | [`README.el.md`](README.el.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_el.ipynb) |
| română | [`README.ro.md`](README.ro.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_ro.ipynb) |
| Tiếng Việt | [`README.vi.md`](README.vi.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_vi.ipynb) |
| български | [`README.bg.md`](README.bg.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_bg.ipynb) |
| íslenska | [`README.is.md`](README.is.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_is.ipynb) |
| slovenski | [`README.sl.md`](README.sl.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_sl.ipynb) |
| slovenčina | [`README.sk.md`](README.sk.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_sk.ipynb) |
| lietuvių | [`README.lt.md`](README.lt.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_lt.ipynb) |
| Kiswahili | [`README.sw.md`](README.sw.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_sw.ipynb) |
| українська | [`README.uk.md`](README.uk.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_uk.ipynb) |
| kalaallisut | [`README.kl.md`](README.kl.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_kl.ipynb) |
| latviešu | [`README.lv.md`](README.lv.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_lv.ipynb) |
| hrvatski | [`README.hr.md`](README.hr.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_hr.ipynb) |
| नेपाली | [`README.ne.md`](README.ne.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_ne.ipynb) |
| српски (Босна и Херцеговина) | [`README.sr-BA.md`](README.sr-BA.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_sr-BA.ipynb) |
| Filipino | [`README.fil.md`](README.fil.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_fil.ipynb) |
| ייִדיש | [`README.yi.md`](README.yi.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_yi.ipynb) |
| Bahasa Melayu | [`README.ms.md`](README.ms.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_ms.ipynb) |
| اردو | [`README.ur.md`](README.ur.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_ur.ipynb) |
| монгол | [`README.mn.md`](README.mn.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_mn.ipynb) |
| հայերեն | [`README.hy.md`](README.hy.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_hy.ipynb) |
| Basa Jawa | [`README.jv.md`](README.jv.md) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/vibevoice-asr-colab/blob/main/notebooks/VibeVoice_ASR_Colab_jv.ipynb) |

## Disposition du référentiel

```text
notebook_template/
  VibeVoice_ASR_Colab.template.ipynb
locales/
  *.json
notebooks/
  VibeVoice_ASR_Colab_<language-code>.ipynb
docs/
  README/
    README.<language-code>.md
scripts/
  build_readmes.py
  build_notebooks.py
  check_notebooks.py
  translate_full_locales.py
```

Le bloc-notes modèle est le bloc-notes source et contient des espaces réservés tels que
`{{settings.input_mode_help}}`. Les fichiers de paramètres régionaux fournissent des valeurs spécifiques à la langue
pour la copie orientée Colab telle que `# @title`, `# @markdown`, les commentaires et les éléments sélectionnés
messages des utilisateurs. Chaque locale contient l'ensemble complet d'espaces réservés du
Langue source anglaise.

Les notebooks générés sont validés afin que les liens Colab restent stables.

## Construire

```bash
python scripts/build_readmes.py
python scripts/build_notebooks.py
```

## Actualiser les traductions

```bash
python scripts/translate_full_locales.py
python scripts/build_readmes.py
python scripts/build_notebooks.py
python scripts/check_notebooks.py
```

`translate_full_locales.py` traduit automatiquement les paramètres régionaux anglais complets en
d'autres fichiers de paramètres régionaux tout en préservant les jetons de code tels que `INPUT_MODE`,
`Google Drive`, `# @markdown` et identifiants de modèle. Réviser la copie traduite
avant une libération officielle.

## Chèques

```bash
python scripts/check_notebooks.py
```

Le workflow CI vérifie que les blocs-notes générés sont à jour et n'ont pas été enregistrés
les sorties de cellule, analysées comme JSON, ne contiennent aucun espace réservé non résolu et ce code
les cellules sont une syntaxe Python valide.

## Ce que CI peut tester

Ce référentiel peut tester le notebook en tant qu'artefact distribuable :

- génération à partir des fichiers de modèle et de paramètres régionaux
- carnet JSON validité
- sorties d'exécution vides
- Syntaxe Python dans les cellules de code
- secrets accidentels évidents
- cahiers générés par commit correspondant au modèle

Le chemin de transcription complet nécessite des API spécifiques à Colab, des téléchargements de modèles volumineux,
GPU disponibilité et fichiers multimédias fournis par l'utilisateur. Cela devrait être traité comme un
test de fumée manuel ou un workflow de validation GPU/Colab distinct.

## Licence

L'échafaudage de bloc-notes et les scripts de construction de ce référentiel sont publiés sous le
MIT Licence. VibeVoice-ASR, les poids du modèle et les dépendances tierces sont
régis par leurs licences respectives.
