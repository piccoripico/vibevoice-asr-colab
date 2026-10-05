"""Build localized Colab notebooks from the template notebook.

The template contains placeholders for localized Colab-facing copy. Locale
files provide the language-specific placeholder values.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "notebook_template" / "VibeVoice_ASR_Colab.template.ipynb"
LOCALES_DIR = ROOT / "locales"
OUTPUT_DIR = ROOT / "notebooks"


def source_to_text(source: object) -> str:
    if isinstance(source, list):
        return "".join(str(part) for part in source)
    return str(source or "")


def text_to_source(text: str) -> list[str]:
    return text.splitlines(keepends=True)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def clear_outputs(nb: dict) -> None:
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            cell["execution_count"] = None
            cell["outputs"] = []


def render_locale(template: dict, locale: dict) -> dict:
    nb = copy.deepcopy(template)
    language = locale["language"]
    placeholders = locale.get("placeholders", {})

    for cell in nb.get("cells", []):
        text = source_to_text(cell.get("source", []))
        for key, value in placeholders.items():
            text = text.replace(
                f'"{{{{{key}}}}}"',
                json.dumps(str(value), ensure_ascii=False),
            )
            text = text.replace(f"{{{{{key}}}}}", str(value))
        cell["source"] = text_to_source(text)

    metadata = nb.setdefault("metadata", {})
    metadata["vibevoice_asr_colab_language"] = language
    metadata["vibevoice_asr_colab_source_template"] = str(
        TEMPLATE_PATH.relative_to(ROOT).as_posix()
    )
    metadata.setdefault("colab", {})["name"] = f"VibeVoice_ASR_Colab_{language}.ipynb"
    clear_outputs(nb)
    return nb


def remove_stale_notebooks() -> None:
    for path in OUTPUT_DIR.glob("VibeVoice_ASR_Colab_*.ipynb"):
        path.unlink()


def build() -> list[Path]:
    template = load_json(TEMPLATE_PATH)
    base_locale = load_json(LOCALES_DIR / "en.json")
    base_placeholders = base_locale.get("placeholders", {})
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    remove_stale_notebooks()
    written: list[Path] = []

    for locale_path in sorted(LOCALES_DIR.glob("*.json")):
        locale = load_json(locale_path)
        locale["placeholders"] = {
            **base_placeholders,
            **locale.get("placeholders", {}),
        }
        language = locale["language"]
        nb = render_locale(template, locale)
        output_path = OUTPUT_DIR / f"VibeVoice_ASR_Colab_{language}.ipynb"
        output_path.write_text(
            json.dumps(nb, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
        written.append(output_path)

    return written


if __name__ == "__main__":
    for path in build():
        print(path.relative_to(ROOT).as_posix())
