# -*- coding: utf-8 -*-
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
FILES = ("index.html", "about.html", "cases.html", "categories.html")

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.refs = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if data.get("id"):
            self.ids.append(data["id"])
        for key in ("src", "href", "poster"):
            value = data.get(key, "")
            if value:
                self.refs.append((tag, key, value))

missing = []
duplicates = []
for name in FILES:
    html = (ROOT / name).read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(html)
    counts = Counter(parser.ids)
    duplicates.extend((name, item) for item, count in counts.items() if count > 1)
    for tag, key, value in parser.refs:
        if value.startswith(("#", "http:", "https:", "mailto:", "tel:", "javascript:", "data:")):
            continue
        path = unquote(urlsplit(value).path)
        if path and not (ROOT / path).exists():
            missing.append((name, tag, key, value))
    markers = html.count('id="white-polish"')
    print(f"{name}: white-polish={markers}, local refs OK so far")
    if markers != 1:
        duplicates.append((name, f"white-polish count={markers}"))

print("MISSING_LOCAL_RESOURCES:", missing)
print("DUPLICATE_IDS_OR_STYLE_MARKERS:", duplicates)
raise SystemExit(1 if missing or duplicates else 0)
