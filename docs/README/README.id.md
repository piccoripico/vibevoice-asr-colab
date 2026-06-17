# VibeVoice-ASR Buku Catatan Colab

Buku catatan ini mentranskripsikan file audio atau video.

## Fitur

- **Gratis untuk digunakan:** Notebook ini menggunakan [VibeVoice-ASR](https://github.com/microsoft/VibeVoice), yang dijadikan sumber terbuka Microsoft pada 21 Januari 2026, bersama dengan runtime gratis Google Colab GPU. Agar model dapat digunakan pada GPU gratis, notebook ini menggunakan model VibeVoice-ASR terkuantisasi.
- **Tidak ada batasan ukuran file sisi buku catatan tetap:** File audio dan video berukuran besar dapat diproses dengan membaginya menjadi beberapa segmen.
- **Pemrosesan batch:** Beberapa file audio dan video dapat diproses sekaligus.
- **Google Drive dukungan:** File dapat diunggah secara langsung, atau file audio/video yang disimpan di Google Drive dapat diproses.
- **Sepenuhnya online:** Pengunduhan dan pemrosesan dilakukan di Google Colab. Tidak ada sumber daya komputasi lokal yang digunakan.
- **Berbagai format keluaran:** Notebook ini mengeluarkan transkrip JSON asli dan file subjudul TXT, CSV, Markdown, Excel, dan SRT.

## Bahasa

| Bahasa | README | Buku catatan |
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

## Tata Letak Repositori

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

Buku catatan templat adalah buku catatan sumber dan berisi placeholder seperti
`{{settings.input_mode_help}}`. File lokal memberikan nilai khusus bahasa
untuk salinan yang berhubungan dengan Colab seperti `# @title`, `# @markdown`, komentar, dan dipilih
pesan pengguna. Setiap lokal berisi kumpulan placeholder lengkap dari
Sumber lokal berbahasa Inggris.

Notebook yang dihasilkan dikomit sehingga link Colab tetap stabil.

## Membangun

```bash
python scripts/build_readmes.py
python scripts/build_notebooks.py
```

## Segarkan Terjemahan

```bash
python scripts/translate_full_locales.py
python scripts/build_readmes.py
python scripts/build_notebooks.py
python scripts/check_notebooks.py
```

`translate_full_locales.py` mesin-menerjemahkan bahasa Inggris lengkap ke dalam
file lokal lainnya sambil mempertahankan token kode seperti `INPUT_MODE`,
`Google Drive`, `# @markdown`, dan pengidentifikasi model. Tinjau salinan terjemahan
sebelum rilis resmi.

## Cek

```bash
python scripts/check_notebooks.py
```

Alur kerja CI memeriksa apakah buku catatan yang dihasilkan adalah yang terbaru, belum disimpan
keluaran sel, diurai sebagai JSON, tidak mengandung placeholder yang belum terselesaikan, dan kode itu
sel adalah sintaksis Python yang valid.

## Apa yang Dapat Diuji oleh CI

Repositori ini dapat menguji notebook sebagai artefak yang dapat didistribusikan:

- pembuatan dari templat dan file lokal
- buku catatan JSON validitas
- keluaran eksekusi kosong
- Sintaks Python dalam sel kode
- rahasia yang jelas dan tidak disengaja
- buku catatan yang dihasilkan berkomitmen dan cocok dengan templat

Jalur transkripsi lengkap memerlukan API khusus Colab, download model besar,
GPU ketersediaan, dan file media yang disediakan pengguna. Itu harus diperlakukan sebagai a
uji asap manual atau alur kerja validasi GPU/Colab yang terpisah.

## Lisensi

Perancah buku catatan dan skrip pembuatan repositori ini dirilis di bawah
MIT Lisensi. VibeVoice-ASR, bobot model, dan dependensi pihak ketiga
diatur oleh izinnya masing-masing.
