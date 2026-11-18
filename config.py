"""VELOCITY JAPANESE - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY GERMAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "GERMAN"
HANDLE = "@velocitygerman"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "de",
    "name": "German",
    "native_name": "Deutsch",
    "history_key": "german",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "de-DE-KatjaNeural",
    "native_fallback_voice": "de-DE-ConradNeural",
    "native_engine": "edge",
    "native_lang_code": "de",
    "english_rate": "-4%",
    "native_rate": "-10%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "DEUTSCH",
    "translit_label": "SAY IT LIKE",
    "flag": "de",
    "greeting": "Hallo!",
    "encouragement": "Fantastisch!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
    "glyphs": "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜäöüß",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Greetings", "Begrüßungen", "hand", "#1CB0F6"),
    ("Basic Phrases", "Grundlegende Sätze", "chat", "#58CC02"),
    ("Common Expressions", "Häufige Ausdrücke", "chat", "#1CB0F6"),
    ("Travel", "Reisen", "plane", "#1CB0F6"),
    ("Restaurant", "Restaurant", "fork", "#FF7A00"),
    ("Shopping", "Einkaufen", "bag", "#E056A0"),
    ("Emergency", "Notfall", "siren", "#FF4B4B"),
    ("Family Terms", "Familienbegriffe", "heart", "#E056A0"),
    ("Numbers", "Zahlen", "hash", "#A560E8"),
    ("Time", "Zeit", "clock", "#00A889"),
    ("Motivation", "Motivation", "rocket", "#A560E8"),
    ("Love", "Liebe", "heart", "#FF4B4B"),
    ("Success", "Erfolg", "trophy", "#F5A700"),
    ("Wisdom", "Weisheit", "book", "#A560E8"),
    ("Happiness", "Glück", "smile", "#F5A700"),
    ("Self Improvement", "Selbstverbesserung", "leaf", "#58CC02"),
    ("Gratitude", "Dankbarkeit", "heart", "#FF7A00"),
    ("Friendship", "Freundschaft", "users", "#00A889"),
    ("Hope", "Hoffnung", "sun", "#FF7A00"),
    ("Creativity", "Kreativität", "palette", "#E056A0"),
    ("Inner Peace", "Innere Ruhe", "lotus", "#00A889"),
    ("Confidence", "Selbstvertrauen", "shield", "#1CB0F6"),
    ("Perseverance", "Ausdauer", "mountain", "#FF7A00"),
    ("Inspiration", "Inspiration", "sparkles", "#A560E8"),
    ("Positive Life", "Positives Leben", "sun", "#58CC02"),
    ("Courage", "Mut", "shield", "#FF4B4B"),
    ("Kindness", "Freundlichkeit", "heart", "#E056A0"),
    ("Patience", "Geduld", "hourglass", "#00A889"),
    ("Forgiveness", "Vergebung", "hands", "#FF7A00"),
    ("Strength", "Stärke", "dumbbell", "#FF4B4B"),
    ("Joy", "Freude", "smile", "#F5A700"),
    ("Balance", "Balance", "scale", "#00A889"),
    ("Growth", "Wachstum", "sprout", "#58CC02"),
    ("Purpose", "Ziel", "target", "#A560E8"),
    ("Mindfulness", "Achtsamkeit", "lotus", "#00A889"),
    ("Daily Routine", "Alltag", "calendar", "#1CB0F6"),
    ("Weather", "Wetter", "cloud", "#1CB0F6"),
    ("Feelings", "Gefühle", "smile", "#E056A0"),
    ("Food", "Essen", "fork", "#FF7A00"),
    ("Health", "Gesundheit", "heart", "#58CC02"),
    ("Work", "Arbeit", "briefcase", "#1CB0F6"),
    ("Technology", "Technologie", "chip", "#A560E8"),
    ("Nature", "Natur", "leaf", "#58CC02"),
    ("Animals", "Tiere", "paw", "#FF7A00"),
    ("Colors", "Farben", "palette", "#E056A0"),
    ("Directions", "Wegbeschreibung", "compass", "#1CB0F6"),
    ("Body Parts", "Körperteile", "hand", "#00A889"),
    ("Clothes", "Kleidung", "shirt", "#E056A0"),
    ("Music", "Musik", "music", "#A560E8"),
    ("Sports", "Sport", "ball", "#FF7A00"),
    ("Holidays", "Feiertage", "gift", "#FF4B4B"),
    ("Education", "Bildung", "book", "#1CB0F6"),
    ("Culture", "Kultur", "globe", "#00A889"),
    ("Finance", "Finanzen", "coin", "#58CC02"),
    ("Relationships", "Beziehungen", "users", "#E056A0"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learngerman",
    "#germanlessons",
    "#germanforbeginners",
    "#languagelearning",
    "#germanvocabulary",
    "#velocitygerman",
    "#dailygerman",
    "#german",
    "#learnlanguages",
    "#speakgerman",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
