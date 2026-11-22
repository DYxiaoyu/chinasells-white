# -*- coding: utf-8 -*-
"""副本专用：四页统一浅色层次与质感。不会影响 chinasells-ru 主站仓库。"""
from pathlib import Path
import re

ROOT = Path(r"C:\Users\Administrator\Doubao\chats\2026-11-17\new-chat-1\chinasells-white")
START = "<!--white-polish:start-->"
END = "<!--white-polish:end-->"
CSS = r"""
<!--white-polish:start-->
<style id="white-polish">
/* 副本统一风格：浅灰蓝层次 + 少量深蓝重点卡，不加 section 过渡带 */
:root{--soft-blue:#edf3f7;--soft-blue-2:#e3edf3;--soft-border:#d5e0e8;--soft-shadow:0 18px 46px rgba(8,35,60,.07)}
.btn{border-radius:7px}.nav-links a.nav-cta{border-radius:7px}
.hero-proof,.capability-grid,.cred-grid,.cat-grid,.stats-grid{border-radius:14px;overflow:hidden}
.hero-person-card{border-radius:14px}.party-note{border-radius:10px}
.case-mini,.case-card,.problem{border:1px solid var(--line);border-radius:13px;overflow:hidden}
.case-mini{box-shadow:0 12px 32px rgba(8,35,60,.05)}
.cat-more{border:0;border-radius:13px;box-shadow:0 16px 38px rgba(6,24,45,.13)}

/* 关于页 / 案例页：原整块深色区改为浅灰蓝，文字和卡片同步换色 */
.section-dark{color:var(--ink);background:radial-gradient(900px 420px at 90% 0%,rgba(20,80,143,.07),transparent 66%),var(--soft-blue)}
.section-dark .section-title,.section-dark h2{color:var(--ink)}
.section-dark .section-copy{color:var(--muted)}
.section-dark .section-kicker{color:var(--gold)}
.timeline{background:var(--line);border-color:var(--line);border-radius:14px;overflow:hidden;box-shadow:var(--soft-shadow)}
.timeline-step{background:#fff}.timeline-index{border-right-color:var(--line);color:var(--gold);background:#f8fafc}
.timeline-text strong{color:var(--ink)}.timeline-text span{color:var(--muted)}
.value-card{background:#fff;border:1px solid var(--line);border-radius:13px;box-shadow:0 12px 30px rgba(8,35,60,.05)}
.value-card h3{color:var(--blue)}.value-card p{color:var(--muted)}
.role-grid{border-color:var(--line);border-radius:14px;overflow:hidden;box-shadow:var(--soft-shadow)}
.role-item{background:#fff;border-color:var(--line)}.role-item h4{color:var(--blue)}.role-item p{color:var(--muted)}
.cta{color:var(--ink);border:1px solid var(--soft-border);border-radius:16px;background:linear-gradient(135deg,#e7eff5,#f7fafc);box-shadow:var(--soft-shadow)}
.cta h2{color:var(--ink)}.cta p{color:var(--muted)}.cta .section-kicker{color:var(--gold)}
.cta .btn-secondary{color:var(--ink);border-color:rgba(9,32,60,.22);background:#fff}

/* 首页人物区：浅色衬底 + 人像圆底 + 四项职责小卡 */
#manager.aliya-sec{padding:92px 0;color:var(--ink);background:radial-gradient(900px 460px at 8% 42%,rgba(20,80,143,.09),transparent 64%),linear-gradient(180deg,#f3f6f9,#eaf1f5)}
#manager .aliya-photo{background:radial-gradient(circle at 50% 43%,#dce7ee 0 42%,rgba(220,231,238,0) 42.4%)}
#manager .aliya-photo img{filter:drop-shadow(0 20px 38px rgba(9,32,60,.18))}
#manager .aliya-ring{border-color:rgba(20,80,143,.14)}#manager .aliya-ring-2{border-color:rgba(215,168,79,.25)}
#manager .aliya-list{gap:14px 16px}
#manager .aliya-item{padding:17px 18px;border:1px solid rgba(213,224,232,.9);border-radius:11px;background:rgba(255,255,255,.74)}
#manager .aliya-item h4{color:var(--ink)}#manager .aliya-item p{color:var(--muted)}
#manager .aliya-tag{border:1px solid var(--soft-border);border-left:2px solid var(--gold);border-radius:6px;background:#fff;box-shadow:0 8px 20px rgba(8,35,60,.06);color:var(--ink)}
#manager .aliya-chip{background:#fff;border-color:var(--soft-border)}

/* 首页流程：仅含 supplier-panel 的首页用此背景，避免覆盖案例页浅色职责区 */
#process:has(.supplier-panel){color:var(--ink);background:#f8fafc}
#process .section-title{color:var(--ink)}#process .section-copy{color:var(--muted)}
#process .supplier-panel{border:0;border-radius:14px;background:linear-gradient(145deg,#0a2c50,#071f3b);box-shadow:0 22px 46px rgba(6,24,45,.17)}
#process .supplier-panel h3{color:var(--gold-2)}
#process .supplier-row{border-top-color:rgba(255,255,255,.13)}
#process .supplier-row strong{color:#fff}#process .supplier-row span{color:rgba(255,255,255,.7)}
#process .process-list{border-color:var(--line);border-radius:14px;background:var(--line);overflow:hidden;box-shadow:var(--soft-shadow)}
#process .process-step{background:#fff}#process .process-num{border-right-color:var(--line);color:var(--gold);background:#fbfcfd}
#process .process-text{color:#405268}

/* 首页联系大卡：浅蓝灰而非整块深蓝 */
#contact{background:var(--paper)}
#contact .contact-band{border:1px solid var(--soft-border);border-radius:16px;background:linear-gradient(135deg,#e8f0f6,#f8fafc);box-shadow:var(--soft-shadow)}
#contact .contact-band .section-kicker{color:var(--gold)}
#contact .contact-list{border-color:var(--line);border-radius:12px;background:var(--line);overflow:hidden}
#contact .contact-item{background:#fff}#contact .contact-label{color:var(--gold)}#contact .contact-value{color:var(--ink)}
#contact .btn-secondary{color:var(--ink);border-color:rgba(9,32,60,.22);background:#fff}
#contact .btn-secondary:hover{color:var(--blue);border-color:var(--gold)}

/* 品类页：目录块统一成轻卡，图片与子类胶囊更柔和 */
.cat-block{padding:32px;margin-bottom:28px;border:1px solid var(--line);border-radius:16px;background:#fff;box-shadow:0 14px 36px rgba(8,35,60,.055);overflow:hidden}
.cat-block:last-child{margin-bottom:0;border-bottom:1px solid var(--line)}
.cat-thumb{border-radius:10px;overflow:hidden}.sub-pill{border-color:#d9e3ea;background:#f1f5f8}

@media(max-width:900px){
 #manager.aliya-sec{padding:70px 0}
 #manager .aliya-item{padding:15px 16px}
}
@media(max-width:640px){
 #manager.aliya-sec{padding:56px 0}
 #manager .aliya-list{gap:12px}
 .cat-block{padding:20px;border-radius:13px}.cta,.cat-more{border-radius:12px}
}
</style>
<!--white-polish:end-->
"""

for name in ("index.html", "categories.html", "cases.html", "about.html"):
    p = ROOT / name
    html = p.read_text(encoding="utf-8")
    html = re.sub(r"\n?" + re.escape(START) + r"[\s\S]*?" + re.escape(END) + r"\n?", "\n", html)
    if "</head>" not in html:
        raise RuntimeError(f"</head> missing in {name}")
    html = html.replace("</head>", CSS + "\n</head>", 1)
    p.write_text(html, encoding="utf-8")
    print(name, "polish inserted")
