# VibeVoice-ASR Colab Notebook

Den här anteckningsboken transkriberar ljud- eller videofiler.

## Funktioner

- **Fritt att använda:** Den här anteckningsboken använder [VibeVoice-ASR](https://github.com/microsoft/VibeVoice), som Microsoft skapade med öppen källkod den 21 januari 2026, tillsammans med Google Colabs gratis körtid GPU. För att göra modellen användbar på gratis GPU:er använder den här bärbara datorn en kvantifierad VibeVoice-ASR-modell.
- **Ingen fast filstorleksgräns på notebook-sidan:** Stora ljud- och videofiler kan bearbetas genom att dela upp dem i segment.
- **Batchbearbetning:** Flera ljud- och videofiler kan bearbetas i en körning.
- **Google Drive support:** Filer kan laddas upp direkt, eller ljud-/videofiler lagrade i Google Drive kan bearbetas.
- **Helt online:** Nedladdningar och bearbetning utförs på Google Colab. Inga lokala datorresurser används.
- **Flera utdataformat:** Anteckningsboken matar ut den ursprungliga JSON transkriptionen och härledda TXT, CSV, Markdown, Excel och SRT undertextfiler.

## Språk

| Språk | README | Anteckningsbok |
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

## Förvarslayout

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

Mallanteckningsboken är källanteckningsboken och innehåller platshållare som t.ex
`{{settings.input_mode_help}}`. Lokalfiler ger språkspecifika värden
för Colab-vända kopior som `# @title`, `# @markdown`, kommentarer och valda
användarmeddelanden. Varje språk innehåller den kompletta platshållaruppsättningen från
Engelsk källa.

Genererade anteckningsböcker är engagerade så att Colab-länkarna förblir stabila.

## Bygga

```bash
python scripts/build_readmes.py
python scripts/build_notebooks.py
```

## Uppdatera översättningar

```bash
python scripts/translate_full_locales.py
python scripts/build_readmes.py
python scripts/build_notebooks.py
python scripts/check_notebooks.py
```

`translate_full_locales.py` maskinöversätter hela engelska språket till
andra språkfiler samtidigt som du bevarar kodtokens som `INPUT_MODE`,
`Google Drive`, `# @markdown` och modellidentifierare. Granska översatt kopia
innan en formell frigivning.

## Checkar

```bash
python scripts/check_notebooks.py
```

CI-arbetsflödeskontrollerna att genererade anteckningsböcker är uppdaterade, har inga sparade
cellutdata, tolka som JSON, innehåller inga olösta platshållare och den koden
celler är giltig Python-syntax.

## Vad CI kan testa

Det här arkivet kan testa anteckningsboken som en distribuerbar artefakt:

- generering från mall- och språkfilerna
- anteckningsbok JSON giltighet
- tomma exekveringsutgångar
- Python-syntax i kodceller
- uppenbara oavsiktliga hemligheter
- engagerade genererade anteckningsböcker som matchar mallen

Den fullständiga transkriptionsvägen kräver Colab-specifika API:er, nedladdningar av stora modeller,
GPU tillgänglighet och mediefiler som tillhandahålls av användaren. Det bör behandlas som en
manuellt röktest eller ett separat GPU/Colab valideringsarbetsflöde.

## Licens

Det här förvarets anteckningsbokställningar och byggskript släpps under
MIT Licens. VibeVoice-ASR, modellvikter och tredjepartsberoenden är
regleras av deras respektive licenser.
