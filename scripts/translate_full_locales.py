"""Translate the full English locale into every requested locale.

This is a maintenance helper, not part of ordinary CI. It fills every locale
with every placeholder key from en.json. Existing Japanese copy is left intact
because it has been manually curated.
"""

from __future__ import annotations

import json
import re
import time
from pathlib import Path

from deep_translator import GoogleTranslator


ROOT = Path(__file__).resolve().parents[1]
LOCALES_DIR = ROOT / "locales"

TARGETS = {
    "aa": None,
    "af": "af",
    "ar": "ar",
    "bg": "bg",
    "ca": "ca",
    "cs": "cs",
    "da": "da",
    "de": "de",
    "el": "el",
    "es": "es",
    "et": "et",
    "fa": "fa",
    "fi": "fi",
    "fil": "tl",
    "fr": "fr",
    "he": "iw",
    "hi": "hi",
    "hr": "hr",
    "hu": "hu",
    "hy": "hy",
    "id": "id",
    "is": "is",
    "it": "it",
    "jv": "jw",
    "kl": None,
    "ko": "ko",
    "lt": "lt",
    "lv": "lv",
    "ms": "ms",
    "mn": "mn",
    "nb": "no",
    "ne": "ne",
    "nl": "nl",
    "pl": "pl",
    "pt-BR": "pt",
    "pt-PT": "pt",
    "ro": "ro",
    "ru": "ru",
    "sk": "sk",
    "sl": "sl",
    "sr-BA": "sr",
    "sv": "sv",
    "sw": "sw",
    "th": "th",
    "tr": "tr",
    "uk": "uk",
    "ur": "ur",
    "vi": "vi",
    "yi": "yi",
    "zh-CN": "zh-CN",
    "zh-TW": "zh-TW",
}

PROTECT_PATTERNS = [
    re.compile(r"\[[^\]]+\]\([^)]+\)"),
    re.compile(r"`[^`]+`"),
    re.compile(r"https?://\S+"),
    re.compile(r'"[^"]+"'),
    re.compile(r"\bGoogle Colab\b"),
    re.compile(r"\bGoogle Drive\b"),
    re.compile(r"\bHF Transformers\b"),
    re.compile(r"\bVibeVoice-ASR\b"),
    re.compile(r"\bVibeVoiceAcousticTokenizerEncoderModel\b"),
    re.compile(r"\bBitsAndBytesConfig\b"),
    re.compile(r"\bBatchEncoding\.to\(device, dtype\)\b"),
    re.compile(r"\bflash_attention_2\b"),
    re.compile(r"\bflash-attn\b"),
    re.compile(r"\bQwen2\b"),
    re.compile(r"\bCUDA\b"),
    re.compile(r"\bSDPA\b"),
    re.compile(r"\bNF4\b"),
    re.compile(r"\bGPU\b"),
    re.compile(r"\bJSON\b"),
    re.compile(r"\bTXT\b"),
    re.compile(r"\bCSV\b"),
    re.compile(r"\bSRT\b"),
    re.compile(r"\bZIP\b"),
    re.compile(r"\b[A-Z][A-Z0-9_]{2,}\b"),
    re.compile(r"\b[a-z]+_[a-z0-9_]+\b"),
]
PROTECT_RE = re.compile("|".join(f"(?:{pattern.pattern})" for pattern in PROTECT_PATTERNS))
COMMENT_PREFIX_PATTERNS = [
    re.compile(r"^(# @title \d+\. )(.*)$", re.S),
    re.compile(r"^(# \d+\. )(.*)$", re.S),
    re.compile(r"^(# @markdown #{2,3} )(.*)$", re.S),
    re.compile(r"^(# @markdown - )(.*)$", re.S),
    re.compile(r"^(# ## )(.*)$", re.S),
    re.compile(r"^(# - )(.*)$", re.S),
    re.compile(r"^(# )(.*)$", re.S),
]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def protect(text: str) -> tuple[str, dict[str, str]]:
    tokens: dict[str, str] = {}

    def add_token(match: re.Match[str]) -> str:
        token = f"@@P{len(tokens):04d}@@"
        tokens[token] = match.group(0)
        return token

    return PROTECT_RE.sub(add_token, text), tokens


def restore(text: str, tokens: dict[str, str]) -> str:
    restored = text
    for token, value in tokens.items():
        restored = restored.replace(token, value)
    return restored


def split_comment_prefix(text: str) -> tuple[str, str]:
    for pattern in COMMENT_PREFIX_PATTERNS:
        match = pattern.match(text)
        if match:
            return match.group(1), match.group(2)
    return "", text


def translate_block(translator: GoogleTranslator, items: list[str]) -> list[str]:
    block = "\n".join(f"@@ITEM{i:03d}@@\n{item}" for i, item in enumerate(items))
    for attempt in range(4):
        try:
            translated = translator.translate(block)
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(2 * (attempt + 1))

    result: list[str] = [""] * len(items)
    matches = list(re.finditer(r"@@ITEM(\d{3})@@\s*(.*?)(?=\n?@@ITEM\d{3}@@|$)", translated, re.S))
    if len(matches) != len(items):
        translated_items: list[str] = []
        for item in items:
            for attempt in range(4):
                try:
                    translated_items.append(translator.translate(item))
                    break
                except Exception:
                    if attempt == 3:
                        raise
                    time.sleep(2 * (attempt + 1))
            time.sleep(0.1)
        return translated_items
    for match in matches:
        result[int(match.group(1))] = match.group(2).strip()
    return result


def chunk_items(items: list[tuple[str, str, dict[str, str]]], limit: int = 3500):
    chunk: list[tuple[str, str, dict[str, str]]] = []
    size = 0
    for item in items:
        item_size = len(item[2]) + 20
        if chunk and size + item_size > limit:
            yield chunk
            chunk = []
            size = 0
        chunk.append(item)
        size += item_size
    if chunk:
        yield chunk


def translate_locale(code: str, target: str, base: dict[str, str]) -> dict[str, str]:
    translator = GoogleTranslator(source="en", target=target)
    prepared: list[tuple[str, str, str, dict[str, str]]] = []
    for key, value in base.items():
        prefix, body = split_comment_prefix(value)
        protected, tokens = protect(body)
        prepared.append((key, prefix, protected, tokens))

    translated: dict[str, str] = {}
    for chunk in chunk_items(prepared):
        texts = [item[2] for item in chunk]
        translated_texts = translate_block(translator, texts)
        for (key, prefix, _protected, tokens), translated_text in zip(chunk, translated_texts):
            translated[key] = prefix + restore(translated_text, tokens)
        time.sleep(0.2)
    return translated


def main() -> None:
    base = load_json(LOCALES_DIR / "en.json")["placeholders"]
    for path in sorted(LOCALES_DIR.glob("*.json")):
        code = path.stem
        if code in {"en", "ja"}:
            continue
        if code not in TARGETS:
            raise KeyError(f"No translation target configured for {code}")

        data = load_json(path)
        target = TARGETS[code]
        if target is None:
            print(f"Copying English fallback for {code} ...", flush=True)
            data["placeholders"] = dict(base)
            data["translation_source"] = "english fallback; translation target unavailable"
        else:
            print(f"Translating {code} -> {target} ...", flush=True)
            data["placeholders"] = translate_locale(code, target, base)
            data["translation_source"] = "machine-translated from en"
        write_json(path, data)


if __name__ == "__main__":
    main()
