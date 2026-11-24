# -*- coding: utf-8 -*-
"""替换正式站左上角 logo，并给首屏 Aliya 联系胶囊加上类型标签。"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
PAGES = ['index.html', 'about.html', 'cases.html', 'categories.html']
MARKER = 'brand-contact-20261123'

CSS = """
.brand-mark{object-fit:contain;filter:drop-shadow(0 1px 3px rgba(0,0,0,.22))}
.hero-person-card .hp-label{color:rgba(255,255,255,.56);font-size:8px;line-height:1;font-weight:700;letter-spacing:.05em;text-transform:uppercase}
.hero-person-card .hp-label::after{content:":";margin-right:4px}
.hero-person-card .hp-foot a:hover .hp-label{color:rgba(255,255,255,.78)}
"""

LOGO = ('<img class="brand-mark" src="img/logo-hyjj.png" '
        'srcset="img/logo-hyjj.png 1x, img/logo-hyjj@2x.png 2x" '
        'alt="China Sells" width="160" height="160" decoding="async" fetchpriority="high">')

FOOT = '''<div class="hp-foot">
              <a href="mailto:aliya@chinasells.ru"><span class="hp-label">Почта</span>aliya@chinasells.ru</a>
              <a href="https://wa.me/8619895947232" target="_blank" rel="noopener noreferrer"><span class="hp-label">Мессенджер</span>WhatsApp</a>
              <a href="https://t.me/aliyachinabiz" target="_blank" rel="noopener noreferrer"><span class="hp-label">Мессенджер</span>Telegram</a>
              <a href="https://www.youtube.com/@aliya.chinabiz" target="_blank" rel="noopener noreferrer"><span class="hp-label">Соцсети</span>YouTube</a>
              <a href="https://www.tiktok.com/@aliya.chinabiz" target="_blank" rel="noopener noreferrer"><span class="hp-label">Соцсети</span>TikTok</a>
              <a href="https://vk.com/aliya.chinabiz" target="_blank" rel="noopener noreferrer"><span class="hp-label">Соцсети</span>VK</a>
              <a href="https://www.instagram.com/aliya.chinabiz" target="_blank" rel="noopener noreferrer"><span class="hp-label">Соцсети</span>Instagram</a>
            </div>'''


def inject_css(text):
    start = f'<!--{MARKER}:start-->'
    end = f'<!--{MARKER}:end-->'
    block = f'{start}\n<style id="{MARKER}">{CSS}</style>\n{end}'
    pattern = re.compile(re.escape(start) + r'.*?' + re.escape(end), re.S)
    if pattern.search(text):
        return pattern.sub(block, text)
    return text.replace('</head>', block + '\n</head>', 1)


def replace_brand(text):
    if 'img/logo-hyjj.png' in text:
        return text
    pattern = re.compile(r'<svg class="brand-mark".*?</svg>', re.S)
    if not pattern.search(text):
        raise SystemExit('brand svg not found')
    return pattern.sub(LOGO, text, count=1)


for name in PAGES:
    path = ROOT / name
    text = path.read_text(encoding='utf-8')
    text = replace_brand(text)
    text = inject_css(text)

    if name == 'index.html':
        text, count = re.subn(r'<div class="hp-foot">.*?</div>', FOOT, text, count=1, flags=re.S)
        if count != 1:
            raise SystemExit('hp-foot not found')

    path.write_text(text, encoding='utf-8')
    print(name, 'ok')

