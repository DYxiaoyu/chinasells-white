# -*- coding: utf-8 -*-
"""把 chinasells-white 上已验收的暖色背景、照片品类卡和编辑式案例拼版
安全地移植到正式站。脚本幂等，CSS 以 warm-home-20261123 为标记。"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

PALETTE = """
:root{
  --paper:#f2eee5;
  --white:#fffdf7;
  --ink:#0b1a26;
  --navy:#071a2b;
  --line:#dcd4c5;
  --muted:#656d6b;
  --gold:#b98732;
  --gold-2:#e2b969;
}
html,body{background:var(--paper);color:var(--ink)}
.section-white{background:var(--white)}
section.section:not(.section-white):not(.section-dark){background:var(--paper)}
.hero::after{background:linear-gradient(180deg,rgba(242,238,229,0),var(--paper))}
.v2-cats .cat-search,.cat-search{background:#f2eee5;border-color:#ded6c6}
.cat-search .cs-box,.cs-box{border-color:#ded6c6}
"""

HOME_CSS = """
#offer{background:var(--paper);border-bottom:1px solid var(--line)}
.cat-grid{grid-template-columns:repeat(5,minmax(0,1fr));gap:14px;counter-reset:cat;border:0;background:none;box-shadow:none}
.cat-card{position:relative;display:flex;flex-direction:column;padding:0;overflow:hidden;counter-increment:cat;
  border:1px solid var(--line);background:var(--white);text-decoration:none;
  transition:transform .24s ease,box-shadow .24s ease,border-color .24s ease;box-shadow:none}
.cat-photo{position:relative;aspect-ratio:4/3;overflow:hidden;background:#d9d2c4}
.cat-photo img{display:block;width:100%;height:100%;object-fit:cover;transition:transform .55s cubic-bezier(.2,.7,.2,1)}
.cat-photo::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,26,43,.02),rgba(7,26,43,.3));pointer-events:none}
.cat-card::before{content:counter(cat,decimal-leading-zero);position:absolute;z-index:2;left:12px;top:12px;display:grid;place-items:center;
  min-width:30px;height:22px;padding:0 6px;background:rgba(7,26,43,.86);border:1px solid rgba(226,185,105,.55);
  color:var(--gold-2);font-size:9.5px;letter-spacing:.12em;font-weight:800}
.cat-ico{display:none}
.cat-card h3{margin:0;padding:18px 17px 0;color:var(--ink);font-size:14px;line-height:1.36}
.cat-card p{flex:1;margin:0;padding:7px 17px 0;color:var(--muted);font-size:11px;line-height:1.68}
.cat-arrow{margin:0;padding:15px 17px 17px;color:var(--gold);font-size:14px}
.cat-card:hover{transform:translateY(-4px);border-color:rgba(185,135,50,.62);box-shadow:0 18px 42px rgba(10,24,36,.11);background:var(--white)}
.cat-card:hover .cat-photo img{transform:scale(1.045)}
.cat-card:hover .cat-arrow{transform:translateX(4px)}
.cat-omitted{margin-top:16px;padding:22px 26px;background:var(--white);border:1px dashed #c8bdab}
.cat-omitted-plus{border-color:rgba(185,135,50,.55);background:rgba(185,135,50,.07);color:var(--gold)}
.cat-omitted p{color:var(--ink)}
.cat-omitted .cat-omitted-note{color:var(--muted)}

#cases{background:var(--white);border-bottom:1px solid var(--line)}
.cases-home-grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;counter-reset:case}
.case-mini{position:relative;counter-increment:case;border:1px solid var(--line);background:var(--white);box-shadow:none}
.case-mini::before{content:counter(case,decimal-leading-zero);position:absolute;z-index:3;left:12px;top:12px;display:grid;place-items:center;
  min-width:30px;height:22px;padding:0 6px;background:rgba(7,26,43,.86);border:1px solid rgba(226,185,105,.5);
  color:var(--gold-2);font-size:9.5px;letter-spacing:.12em;font-weight:800}
.case-mini img{height:190px}
.case-mini:first-child{grid-column:span 2;flex-direction:row;min-height:330}
.case-mini:first-child img{width:58%;height:100%;min-height:330;flex:0 0 58%}
.case-mini:first-child .case-mini-body{width:42%;padding:30px 28px;justify-content:center}
.case-mini:first-child h3{font-size:24px;line-height:1.2;letter-spacing:-.03em}
.case-mini:first-child p{font-size:13.5px;line-height:1.8}
.case-mini h3{font-size:15px;line-height:1.3;color:var(--ink)}
.case-mini-tag{color:var(--gold);font-size:9.5px;letter-spacing:.08em;font-weight:800}
.case-mini p{color:var(--muted);font-size:12px;line-height:1.7}
.case-mini::after{display:none!important}
.case-mini:hover{transform:translateY(-4px);box-shadow:0 18px 40px rgba(10,24,36,.1);border-color:rgba(185,135,50,.55)}

@media(max-width:1080px){
  .cat-grid{grid-template-columns:repeat(3,minmax(0,1fr))}
  .cases-home-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .case-mini:first-child{grid-column:span 2}
  .case-mini:last-child{grid-column:auto}
}
@media(max-width:720px){
  .cat-grid{grid-template-columns:1fr 1fr;gap:10px}
  .cat-card h3{font-size:13px;padding:14px 13px 0}
  .cat-card p{padding:6px 13px 0;font-size:10.5px}
  .cat-card::before{left:9px;top:9px;min-width:27px;height:20px}
  .cases-home-grid{grid-template-columns:1fr}
  .case-mini:first-child{grid-column:auto;flex-direction:column;min-height:0}
  .case-mini:first-child img{width:100%;height:190px;min-height:0;flex:none}
  .case-mini:first-child .case-mini-body{width:100%;padding:20px 16px 22px}
  .case-mini:first-child h3{font-size:18px}
}
"""

PHOTO_ALT = {
    'clothing': 'Одежда и обувь',
    'textile': 'Домашний текстиль и ткани',
    'home': 'Товары для дома',
    'electronics': 'Электроника и бытовая техника',
    'furniture': 'Мебель и фурнитура',
    'sport': 'Спорт и фитнес',
    'tools': 'Инструмент и оборудование',
    'medical': 'Медицина и уход',
    'packaging': 'Упаковка и расходники',
    'auto': 'Авто и мото',
}


def replace_block(text, marker, body):
    start = f'<!--{marker}:start-->'
    end = f'<!--{marker}:end-->'
    block = f'{start}\n<style id="{marker}">{body}</style>\n{end}'
    pattern = re.compile(re.escape(start) + r'.*?' + re.escape(end), re.S)
    if pattern.search(text):
        return pattern.sub(block, text)
    return text.replace('</head>', block + '\n</head>', 1)


def apply_palette(name):
    path = ROOT / name
    text = path.read_text(encoding='utf-8')
    text = replace_block(text, 'warm-palette-20261123', PALETTE)
    path.write_text(text, encoding='utf-8')
    print(name, 'palette ok')


def apply_home():
    path = ROOT / 'index.html'
    text = path.read_text(encoding='utf-8')
    text = replace_block(text, 'warm-home-20261123', PALETTE + HOME_CSS)

    # 移除旧的照片节点，保证脚本可重复执行
    text = re.sub(r'\s*<div class="cat-photo">.*?</div>', '', text, flags=re.S)

    for cid, alt in PHOTO_ALT.items():
        needle = f'<a class="cat-card" href="categories.html#{cid}">'
        if needle not in text:
            raise SystemExit(f'cat-card not found: {cid}')
        photo = (f'\n            <div class="cat-photo"><img src="img/cat-{cid}.webp" '
                 f'alt="{alt}" width="380" height="285" loading="lazy" decoding="async"></div>')
        text = text.replace(needle, needle + photo, 1)

    path.write_text(text, encoding='utf-8')
    print('index.html home ok')


if __name__ == '__main__':
    for name in ('index.html', 'about.html', 'cases.html', 'categories.html'):
        if name != 'index.html':
            apply_palette(name)
    apply_home()
