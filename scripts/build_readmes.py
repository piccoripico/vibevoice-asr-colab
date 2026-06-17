"""Build README files for all locales.

The English README lives at the repository root. Localized README files are
generated under docs/README so the root stays tidy while links remain stable.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOCALES_DIR = ROOT / "locales"
DOCS_README_DIR = ROOT / "docs" / "README"
REPO = "piccoripico/vibevoice-asr-colab"

LANGUAGES: list[tuple[str, str]] = [
    ("en", "English (United States)"),
    ("zh-CN", "中文 (簡体字)"),
    ("zh-TW", "中文 (繁体字)"),
    ("es", "Español"),
    ("pt-PT", "Português"),
    ("pt-BR", "português"),
    ("de", "Deutsch"),
    ("ja", "日本語"),
    ("ko", "한국어"),
    ("fr", "français"),
    ("ru", "русский"),
    ("id", "Bahasa Indonesia"),
    ("sv", "svenska"),
    ("it", "italiano"),
    ("he", "עברית"),
    ("nl", "Nederlands"),
    ("pl", "polski"),
    ("nb", "norsk, bokmål"),
    ("tr", "Türkçe"),
    ("th", "ไทย"),
    ("ar", "العربية"),
    ("hu", "magyar"),
    ("ca", "Català"),
    ("cs", "čeština"),
    ("da", "dansk"),
    ("fa", "فارسی"),
    ("af", "Afrikaans"),
    ("hi", "हिंदी"),
    ("fi", "suomi"),
    ("et", "eesti"),
    ("aa", "Qafar af"),
    ("el", "Ελληνικά"),
    ("ro", "română"),
    ("vi", "Tiếng Việt"),
    ("bg", "български"),
    ("is", "íslenska"),
    ("sl", "slovenski"),
    ("sk", "slovenčina"),
    ("lt", "lietuvių"),
    ("sw", "Kiswahili"),
    ("uk", "українська"),
    ("kl", "kalaallisut"),
    ("lv", "latviešu"),
    ("hr", "hrvatski"),
    ("ne", "नेपाली"),
    ("sr-BA", "српски (Босна и Херцеговина)"),
    ("fil", "Filipino"),
    ("yi", "ייִדיש"),
    ("ms", "Bahasa Melayu"),
    ("ur", "اردو"),
    ("mn", "монгол"),
    ("hy", "հայերեն"),
    ("jv", "Basa Jawa"),
]

DEFAULT_LABELS = {
    "languages": "Languages",
    "language": "Language",
    "readme": "README",
    "notebook": "Notebook",
    "repository_layout": "Repository Layout",
    "build": "Build",
    "refresh_translations": "Refresh Translations",
    "checks": "Checks",
    "what_ci_can_test": "What CI Can Test",
    "license": "License",
}

LANGUAGE_SECTION_LABELS: dict[str, dict[str, str]] = {
    "aa": {"languages": "Qafar afitte", "language": "Qafar af", "notebook": "Notebook"},
    "af": {"languages": "Tale", "language": "Taal", "notebook": "Notaboek"},
    "ar": {"languages": "اللغات", "language": "اللغة", "notebook": "دفتر الملاحظات"},
    "bg": {"languages": "Езици", "language": "Език", "notebook": "Бележник"},
    "ca": {"languages": "Idiomes", "language": "Idioma", "notebook": "Quadern"},
    "cs": {"languages": "Jazyky", "language": "Jazyk", "notebook": "Poznámkový blok"},
    "da": {"languages": "Sprog", "language": "Sprog", "notebook": "Notesbog"},
    "de": {"languages": "Sprachen", "language": "Sprache", "notebook": "Notizbuch"},
    "el": {"languages": "Γλώσσες", "language": "Γλώσσα", "notebook": "Σημειωματάριο"},
    "en": {"languages": "Languages", "language": "Language", "notebook": "Notebook"},
    "es": {"languages": "Idiomas", "language": "Idioma", "notebook": "Cuaderno"},
    "et": {"languages": "Keeled", "language": "Keel", "notebook": "Märkmik"},
    "fa": {"languages": "زبان‌ها", "language": "زبان", "notebook": "دفترچه"},
    "fi": {"languages": "Kielet", "language": "Kieli", "notebook": "Muistikirja"},
    "fil": {"languages": "Mga Wika", "language": "Wika", "notebook": "Kuwaderno"},
    "fr": {"languages": "Langues", "language": "Langue", "notebook": "Carnet"},
    "he": {"languages": "שפות", "language": "שפה", "notebook": "מחברת"},
    "hi": {"languages": "भाषाएँ", "language": "भाषा", "notebook": "नोटबुक"},
    "hr": {"languages": "Jezici", "language": "Jezik", "notebook": "Bilježnica"},
    "hu": {"languages": "Nyelvek", "language": "Nyelv", "notebook": "Jegyzetfüzet"},
    "hy": {"languages": "Լեզուներ", "language": "Լեզու", "notebook": "Նոթատետր"},
    "id": {"languages": "Bahasa", "language": "Bahasa", "notebook": "Buku catatan"},
    "is": {"languages": "Tungumál", "language": "Tungumál", "notebook": "Minnisbók"},
    "it": {"languages": "Lingue", "language": "Lingua", "notebook": "Taccuino"},
    "ja": {"languages": "言語", "language": "言語", "notebook": "ノートブック"},
    "jv": {"languages": "Basa", "language": "Basa", "notebook": "Cathetan"},
    "kl": {"languages": "Oqaatsit", "language": "Oqaatsit", "notebook": "Allattaavik"},
    "ko": {"languages": "언어", "language": "언어", "notebook": "노트북"},
    "lt": {"languages": "Kalbos", "language": "Kalba", "notebook": "Užrašinė"},
    "lv": {"languages": "Valodas", "language": "Valoda", "notebook": "Piezīmju grāmatiņa"},
    "ms": {"languages": "Bahasa", "language": "Bahasa", "notebook": "Buku nota"},
    "mn": {"languages": "Хэлнүүд", "language": "Хэл", "notebook": "Дэвтэр"},
    "nb": {"languages": "Språk", "language": "Språk", "notebook": "Notatbok"},
    "ne": {"languages": "भाषाहरू", "language": "भाषा", "notebook": "नोटबुक"},
    "nl": {"languages": "Talen", "language": "Taal", "notebook": "Notitieboek"},
    "pl": {"languages": "Języki", "language": "Język", "notebook": "Notatnik"},
    "pt-BR": {"languages": "Idiomas", "language": "Idioma", "notebook": "Caderno"},
    "pt-PT": {"languages": "Idiomas", "language": "Idioma", "notebook": "Bloco de notas"},
    "ro": {"languages": "Limbi", "language": "Limbă", "notebook": "Caiet"},
    "ru": {"languages": "Языки", "language": "Язык", "notebook": "Блокнот"},
    "sk": {"languages": "Jazyky", "language": "Jazyk", "notebook": "Poznámkový blok"},
    "sl": {"languages": "Jeziki", "language": "Jezik", "notebook": "Beležnica"},
    "sr-BA": {"languages": "Језици", "language": "Језик", "notebook": "Бележница"},
    "sv": {"languages": "Språk", "language": "Språk", "notebook": "Anteckningsbok"},
    "th": {"languages": "ภาษา", "language": "ภาษา", "notebook": "สมุดบันทึก"},
    "tr": {"languages": "Diller", "language": "Dil", "notebook": "Not defteri"},
    "uk": {"languages": "Мови", "language": "Мова", "notebook": "Блокнот"},
    "ur": {"languages": "زبانیں", "language": "زبان", "notebook": "نوٹ بک"},
    "vi": {"languages": "Ngôn ngữ", "language": "Ngôn ngữ", "notebook": "Sổ tay"},
    "sw": {"languages": "Lugha", "language": "Lugha", "notebook": "Daftari"},
    "yi": {"languages": "שפּראַכן", "language": "שפּראַך", "notebook": "העפט"},
    "zh-CN": {"languages": "语言", "language": "语言", "notebook": "笔记本"},
    "zh-TW": {"languages": "語言", "language": "語言", "notebook": "筆記本"},
}

EN_TEXT = {
    "subtitle": (
        "Multilingual Google Colab notebooks for transcribing audio and video files with\n"
        "VibeVoice-ASR."
    ),
    "template_note": (
        "The template notebook is the source notebook and contains placeholders such as\n"
        "`{{settings.input_mode_help}}`. Locale files provide language-specific values\n"
        "for Colab-facing copy such as `# @title`, `# @markdown`, comments, and selected\n"
        "user messages. Every locale contains the complete placeholder set from the\n"
        "English source locale."
    ),
    "generated_note": "Generated notebooks are committed so Colab links stay stable.",
    "refresh_note": (
        "`translate_full_locales.py` machine-translates the full English locale into the\n"
        "other locale files while preserving code tokens such as `INPUT_MODE`,\n"
        "`Google Drive`, `# @markdown`, and model identifiers. Review translated copy\n"
        "before a formal release."
    ),
    "checks_note": (
        "The CI workflow checks that generated notebooks are up to date, have no saved\n"
        "cell outputs, parse as JSON, contain no unresolved placeholders, and that code\n"
        "cells are valid Python syntax."
    ),
    "ci_intro": "This repository can test the notebook as a distributable artifact:",
    "ci_items": [
        "generation from the template and locale files",
        "notebook JSON validity",
        "empty execution outputs",
        "Python syntax in code cells",
        "obvious accidental secrets",
        "committed generated notebooks matching the template",
    ],
    "ci_limit": (
        "The full transcription path requires Colab-specific APIs, large model downloads,\n"
        "GPU availability, and user-provided media files. That should be treated as a\n"
        "manual smoke test or a separate GPU/Colab validation workflow."
    ),
    "license_note": (
        "This repository's notebook scaffolding and build scripts are released under the\n"
        "MIT License. VibeVoice-ASR, model weights, and third-party dependencies are\n"
        "governed by their respective licenses."
    ),
}


def read_locale(code: str) -> dict:
    return json.loads((LOCALES_DIR / f"{code}.json").read_text(encoding="utf-8"))


def output_path(code: str) -> Path:
    if code == "en":
        return ROOT / "README.md"
    return DOCS_README_DIR / f"README.{code}.md"


def readme_link(code: str, current_code: str) -> str:
    if current_code == "en":
        return "README.md" if code == "en" else f"docs/README/README.{code}.md"
    return "../../README.md" if code == "en" else f"README.{code}.md"


def colab_badge(code: str) -> str:
    notebook = f"notebooks/VibeVoice_ASR_Colab_{code}.ipynb"
    url = f"https://colab.research.google.com/github/{REPO}/blob/main/{notebook}"
    return f"[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)]({url})"


def labels_for(code: str) -> dict[str, str]:
    return {**DEFAULT_LABELS, **LANGUAGE_SECTION_LABELS.get(code, {})}


def readme_text_for(locale: dict) -> dict:
    merged = {**DEFAULT_LABELS, **EN_TEXT}
    readme = locale.get("readme", {})
    for key, value in readme.items():
        merged[key] = value
    return merged


def language_table(current_code: str, labels: dict[str, str]) -> str:
    lines = [
        f"| {labels['language']} | {labels['readme']} | {labels['notebook']} |",
        "| --- | --- | --- |",
    ]
    for code, name in LANGUAGES:
        link = readme_link(code, current_code)
        label = "README.md" if code == "en" else f"README.{code}.md"
        lines.append(f"| {name} | [`{label}`]({link}) | {colab_badge(code)} |")
    return "\n".join(lines)


def split_intro(intro: str) -> tuple[str, str, str, str]:
    lines = intro.strip().splitlines()
    title = lines[0].lstrip("#").strip()
    subtitle_lines: list[str] = []
    feature_lines: list[str] = []
    feature_heading = "Features"
    in_features = False

    for line in lines[1:]:
        if re.match(r"^##\s*", line):
            if in_features:
                break
            feature_heading = re.sub(r"^##\s*", "", line).strip()
            in_features = True
            continue
        if in_features:
            feature_lines.append(line)
        elif line.strip():
            subtitle_lines.append(line)

    return (
        title,
        "\n".join(subtitle_lines).strip(),
        feature_heading,
        "\n".join(feature_lines).strip(),
    )


def repository_sections(text: dict) -> str:
    ci_items = "\n".join(f"- {item}" for item in text["ci_items"])
    return f"""## {text['repository_layout']}

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

{text['template_note']}

{text['generated_note']}

## {text['build']}

```bash
python scripts/build_readmes.py
python scripts/build_notebooks.py
```

## {text['refresh_translations']}

```bash
python scripts/translate_full_locales.py
python scripts/build_readmes.py
python scripts/build_notebooks.py
python scripts/check_notebooks.py
```

{text['refresh_note']}

## {text['checks']}

```bash
python scripts/check_notebooks.py
```

{text['checks_note']}

## {text['what_ci_can_test']}

{text['ci_intro']}

{ci_items}

{text['ci_limit']}

## {text['license']}

{text['license_note']}
"""


def build_readme(code: str) -> str:
    locale = read_locale(code)
    labels = labels_for(code)
    readme_text = readme_text_for(locale)
    title, locale_subtitle, feature_heading, features = split_intro(
        locale["placeholders"]["intro_markdown"]
    )
    if code == "en":
        title = "VibeVoice-ASR Colab"
        subtitle = EN_TEXT["subtitle"]
    else:
        subtitle = locale_subtitle

    markdown = f"""# {title}

{subtitle}

## {feature_heading}

{features}

## {labels['languages']}

{language_table(code, labels)}

{repository_sections(readme_text)}
"""
    return markdown.rstrip() + "\n"


def remove_stale_readmes() -> None:
    for path in ROOT.glob("README.*.md"):
        path.unlink()
    for path in DOCS_README_DIR.glob("README.*.md"):
        path.unlink()


def main() -> None:
    DOCS_README_DIR.mkdir(parents=True, exist_ok=True)
    remove_stale_readmes()
    for code, _name in LANGUAGES:
        path = output_path(code)
        path.write_text(build_readme(code), encoding="utf-8", newline="\n")
        print(path.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
