# -*- coding: utf-8 -*-
"""副本视觉 v2：暖纸色 + 深海军蓝 + 铜金，照片化品类、深色资料区和验货报告样本区。

只在 chinasells-white 副本运行；所有页面内容与链接不改，仅补视觉层和新展示模块。
"""
from pathlib import Path
import re

ROOT = Path(r"C:\Users\Administrator\Doubao\chats\2026-11-17\new-chat-1\chinasells-white")
START = "<!--visual-v2:start-->"
END = "<!--visual-v2:end-->"
PROOF_START = "<!--visual-v2-proof:start-->"
PROOF_END = "<!--visual-v2-proof:end-->"
ROUTE_START = "<!--visual-v2-route:start-->"
ROUTE_END = "<!--visual-v2-route:end-->"

CSS = r"""
<!--visual-v2:start-->
<style id="visual-v2">
/* =========================================================
   V2 · 工业档案感：暖纸底色、海军蓝结构、铜金标记、照片化目录
   不加入区块渐变换色，不使用发光 AI 渐变
   ========================================================= */
:root{
  --paper:#f2eee5;
  --white:#fffdf7;
  --ink:#0b1a26;
  --navy:#071a2b;
  --navy-2:#0b2439;
  --line:#dcd4c5;
  --muted:#656d6b;
  --gold:#b98732;
  --gold-2:#e2b969;
  --soft-border:#d6cebf;
  --soft-blue:#ede8dd;
  --shadow:0 16px 44px rgba(10,24,36,.065);
}
html,body{background:var(--paper);color:var(--ink)}
body{counter-reset:sec}
.section{background:transparent}
.section-white{background:var(--white)}
.section-title{letter-spacing:-.032em}
.btn{border-radius:2px;text-transform:uppercase;letter-spacing:.055em;font-size:12px;font-weight:800;padding-left:22px;padding-right:22px}
.nav-links a.nav-cta{border-radius:2px}
.cta,.case-mini,.case-card,.problem,.cat-block,.value-card,.cred-card,.capability-grid,.cred-grid,.cat-grid,.stats-grid,.timeline,.role-grid,#process .process-list,#manager .aliya-item,#manager .aliya-tag,.cat-more{border-radius:2px}
.cta,.cred-card,.case-mini,.capability-card,.cat-card,.cat-block{box-shadow:none}

/* 章节编号：01 / 02 / 03 ... */
.section-kicker{counter-increment:sec;display:inline-flex;align-items:center;gap:9px;letter-spacing:.13em;color:var(--gold)}
.section-kicker::before{content:counter(sec,decimal-leading-zero);display:inline-flex;align-items:center;justify-content:center;min-width:25px;height:20px;padding:0 4px;
  border:1px solid rgba(11,26,38,.22);background:var(--white);color:var(--ink);font-size:9px;line-height:1;letter-spacing:.06em;font-weight:800}
.section-dark .section-kicker::before,#guarantee .section-kicker::before,#contact .section-kicker::before{background:transparent;border-color:rgba(226,185,105,.42);color:var(--gold-2)}

/* 首屏下的订单一句话路线条 */
.route-bar-wrap{background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.route-bar{display:grid;grid-template-columns:180px minmax(0,1fr) 128px;align-items:center;gap:34px;min-height:88px}
.route-caption{font-size:9px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);line-height:1.6}
.route-caption b{display:block;margin-top:4px;color:var(--ink);font-size:12px;letter-spacing:.06em}
.route-flow{position:relative;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));align-items:start}
.route-flow::before{content:"";position:absolute;left:5%;right:5%;top:9px;height:1px;background:var(--line)}
.route-step{position:relative;padding-top:27px;text-align:center;font-size:11.5px;font-weight:700;color:var(--ink)}
.route-step::before{content:"";position:absolute;top:4px;left:50%;width:9px;height:9px;margin-left:-4.5px;border:1px solid var(--gold);background:var(--white);border-radius:50%}
.route-step:first-child::before{background:var(--gold)}
.route-step small{display:block;margin-bottom:4px;color:var(--gold);font-size:9px;letter-spacing:.14em}
.route-coord{text-align:right;font-size:9.5px;line-height:1.7;letter-spacing:.08em;color:var(--muted)}
.route-coord b{display:block;color:var(--ink);font-size:11px;letter-spacing:.04em}

/* 首屏右侧：工作现场照片框，主动去掉悬浮 AI 人像 */
.hero-person-glow{display:none}
.hero-person-photo{width:min(340px,100%);aspect-ratio:3/4;overflow:hidden;border:1px solid rgba(226,185,105,.42);
  background:#0a1b2a;box-shadow:0 26px 56px rgba(0,0,0,.36)}
.hero-person-photo img{width:100%;height:100%;object-fit:cover;object-position:center 54%;filter:none}
.hero-person-photo::before{content:"НА СКЛАДЕ · НАНЬТУН";position:absolute;z-index:2;left:0;top:0;padding:7px 10px;
  background:rgba(7,26,43,.9);border-right:1px solid rgba(226,185,105,.4);border-bottom:1px solid rgba(226,185,105,.4);
  color:var(--gold-2);font-size:8.5px;letter-spacing:.14em;font-weight:800}
.hero-person-photo::after{content:"";position:absolute;inset:0;pointer-events:none;box-shadow:inset 0 0 0 1px rgba(255,255,255,.06)}

/* 数据档案板：首页 2×2，关于页 3×2；统一深底照片背景 */
.about-metrics{position:relative;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1px;padding:62px 0 0;overflow:hidden;
  border:1px solid #1b3348;background:linear-gradient(180deg,rgba(7,26,43,.48),rgba(7,26,43,.9)),url("img/ru-hero.webp") center/cover no-repeat;
  box-shadow:0 24px 54px rgba(7,26,43,.18)}
.about-metrics::before{content:"HUYING JUJIN  ·  NANTONG / JIANGSU";position:absolute;z-index:1;left:20px;right:20px;top:20px;
  color:rgba(255,255,255,.54);font-size:8.5px;letter-spacing:.18em;text-transform:uppercase}
.about-metrics .about-metric{padding:24px 22px;background:rgba(7,26,43,.72);border:0}
.about-metrics .about-metric strong{color:var(--gold-2);font-size:25px;letter-spacing:-.02em}
.about-metrics .about-metric span{color:rgba(255,255,255,.67);font-size:11.5px}

/* 关于页 3×2 指标板 */
.metric-panel{position:relative;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1px;padding:62px 0 0;overflow:hidden;
  border:1px solid #1b3348;background:linear-gradient(180deg,rgba(7,26,43,.5),rgba(7,26,43,.92)),url("img/ru-hero.webp") center/cover no-repeat;
  box-shadow:0 24px 54px rgba(7,26,43,.18)}
.metric-panel::before{content:"HUYING JUJIN  ·  NANTONG / JIANGSU";position:absolute;z-index:1;left:20px;right:20px;top:20px;
  color:rgba(255,255,255,.54);font-size:8.5px;letter-spacing:.18em;text-transform:uppercase}
.metric{padding:23px 20px;background:rgba(7,26,43,.72);border:0}
.metric strong{color:var(--gold-2);font-size:24px;margin-bottom:9px}
.metric span{color:rgba(255,255,255,.66);font-size:11.5px}

/* 关于：深色数据档案板 */
#about{background:var(--white);border-bottom:1px solid var(--line)}
#about .about-home{gap:44px;align-items:center}
#about .about-home-text .section-title{max-width:650px}
#about .about-metrics{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:1px;padding:62px 0 0;overflow:hidden;
  border:1px solid #1b3348;background:linear-gradient(180deg,rgba(7,26,43,.48),rgba(7,26,43,.9)),url("img/ru-hero.webp") center/cover no-repeat;box-shadow:0 24px 54px rgba(7,26,43,.18)}
#about .about-metrics::before{content:"HUYING JUJIN  ·  NANTONG / JIANGSU";position:absolute;z-index:1;left:20px;right:20px;top:20px;
  color:rgba(255,255,255,.54);font-size:8.5px;letter-spacing:.18em;text-transform:uppercase}
#about .about-metric{padding:24px 22px;background:rgba(7,26,43,.72);border:0}
#about .about-metric strong{color:var(--gold-2);font-size:25px;letter-spacing:-.02em}
#about .about-metric span{color:rgba(255,255,255,.67);font-size:11.5px}

/* 能力：四张档案卡，第一张深色，右上角大号序号 */
#capability{background:var(--white);border-bottom:1px solid var(--line)}
#capability .capability-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;counter-reset:cap;border:0;background:none;box-shadow:none}
#capability .capability-card{position:relative;min-height:292px;padding:30px 25px 28px;overflow:hidden;counter-increment:cap;
  border:1px solid var(--line);border-top:2px solid var(--ink);background:var(--paper)}
#capability .capability-card:first-child{background:var(--navy);border-color:var(--navy);border-top-color:var(--gold)}
#capability .capability-card::after{content:counter(cap,decimal-leading-zero);position:absolute;right:18px;top:14px;color:rgba(11,26,38,.12);font-size:54px;line-height:1;font-weight:900;letter-spacing:-.06em}
#capability .capability-card:first-child::after{color:rgba(255,255,255,.12)}
#capability .capability-icon{width:42px;height:42px;margin-bottom:28px;padding:10px;border:1px solid rgba(185,135,50,.58);background:rgba(185,135,50,.07);color:var(--gold)}
#capability .capability-card h3{font-size:18px;line-height:1.28;letter-spacing:-.02em}
#capability .capability-card:first-child h3{color:#fff8eb}
#capability .capability-card:first-child p{color:rgba(255,255,255,.66)}
#capability .capability-card:first-child .capability-icon{color:var(--gold-2);border-color:rgba(226,185,105,.35)}
#capability .capability-card:hover{transform:translateY(-3px);box-shadow:0 16px 38px rgba(10,24,36,.08)}

/* 保证与文件：深色资料带 + 验货报告样本 */
#guarantee{position:relative;overflow:hidden;background:var(--navy);color:#f7f0e2;padding-top:92px;padding-bottom:92px}
#guarantee::before{content:"";position:absolute;inset:0;pointer-events:none;opacity:.55;
  background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:44px 44px}
#guarantee .container{position:relative;z-index:1}
#guarantee .section-title{color:#fff8eb}
#guarantee .section-copy{color:rgba(255,255,255,.66)}
#guarantee .cred-grid{grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;counter-reset:cred;
  border:1px solid rgba(255,255,255,.15);background:rgba(255,255,255,.14)}
#guarantee .cred-card{position:relative;counter-increment:cred;padding:30px 22px 32px;border:0;background:rgba(8,25,41,.76)}
#guarantee .cred-card::before{content:counter(cred,decimal-leading-zero);display:block;margin-bottom:26px;color:var(--gold-2);font-size:10px;letter-spacing:.14em;font-weight:800}
#guarantee .cred-card h3{color:#fff8eb;font-size:17px;line-height:1.42}
#guarantee .cred-card p{color:rgba(255,255,255,.62);font-size:12.8px}
#guarantee .party-note{margin-top:18px;color:rgba(255,255,255,.72);background:rgba(185,135,50,.09);border-left:2px solid var(--gold)}
#guarantee .party-note strong{color:var(--gold-2)}

.inspection-proof{display:grid;grid-template-columns:minmax(0,.82fr) minmax(0,1.18fr);gap:58px;align-items:center;margin-top:58px;padding-top:52px;border-top:1px solid rgba(255,255,255,.13)}
.report-visual{position:relative;justify-self:stretch;padding:12px;border:1px solid #b8ac96;background:#e9e1d3;box-shadow:0 30px 70px rgba(0,0,0,.35);transform:rotate(-1.1deg)}
.report-visual img{display:block;width:100%;height:auto}
.report-stamp{position:absolute;right:-17px;top:20px;padding:8px 11px;border:1px solid var(--gold-2);background:var(--navy);color:var(--gold-2);
  font-size:9px;letter-spacing:.14em;font-weight:800;transform:rotate(3deg);box-shadow:0 8px 20px rgba(0,0,0,.24)}
.proof-kicker{color:var(--gold-2);font-size:9px;letter-spacing:.16em;text-transform:uppercase;font-weight:800}
.inspection-proof h3{margin:12px 0 14px;max-width:500px;color:#fff8eb;font-size:33px;line-height:1.18;letter-spacing:-.035em}
.inspection-proof p{max-width:560px;margin:0;color:rgba(255,255,255,.65);font-size:14px;line-height:1.85}
.proof-facts{display:grid;grid-template-columns:1fr 1fr;gap:0 22px;margin:28px 0 24px;padding:0;list-style:none}
.proof-facts li{padding:12px 0;border-top:1px solid rgba(255,255,255,.13);color:rgba(255,255,255,.72);font-size:12px;line-height:1.6}
.proof-facts li b{display:block;color:#fff8eb;font-size:12.5px;margin-bottom:3px}
.proof-actions{display:flex;flex-wrap:wrap;align-items:center;gap:14px}
.proof-note{margin:14px 0 0;color:rgba(255,255,255,.44)!important;font-size:10.5px!important;line-height:1.6!important}

/* 品类：照片化目录卡 */
#offer{background:var(--paper);border-bottom:1px solid var(--line)}
.cat-grid{grid-template-columns:repeat(5,minmax(0,1fr));gap:14px;counter-reset:cat;border:0;background:none;box-shadow:none}
.cat-card{position:relative;display:flex;flex-direction:column;padding:0;overflow:hidden;counter-increment:cat;
  border:1px solid var(--line);background:var(--white);text-decoration:none;transition:transform .24s ease,box-shadow .24s ease,border-color .24s ease}
.cat-photo{position:relative;aspect-ratio:4/3;overflow:hidden;background:#d9d2c4}
.cat-photo img{display:block;width:100%;height:100%;object-fit:cover;transition:transform .55s cubic-bezier(.2,.7,.2,1)}
.cat-photo::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,26,43,.02),rgba(7,26,43,.3));pointer-events:none}
.cat-card::before{content:counter(cat,decimal-leading-zero);position:absolute;z-index:2;left:12px;top:12px;display:grid;place-items:center;
  min-width:30px;height:22px;padding:0 6px;background:rgba(7,26,43,.86);border:1px solid rgba(226,185,105,.55);color:var(--gold-2);font-size:9.5px;letter-spacing:.12em;font-weight:800}
.cat-ico{display:none}
.cat-card h3{margin:0;padding:18px 17px 0;color:var(--ink);font-size:14px;line-height:1.36}
.cat-card p{flex:1;margin:0;padding:7px 17px 0;color:var(--muted);font-size:11px;line-height:1.68}
.cat-arrow{margin:0;padding:15px 17px 17px;color:var(--gold);font-size:14px}
.cat-card:hover{transform:translateY(-4px);border-color:rgba(185,135,50,.62);box-shadow:0 18px 42px rgba(10,24,36,.11)}
.cat-card:hover .cat-photo img{transform:scale(1.045)}
.cat-card:hover .cat-arrow{transform:translateX(4px)}

/* 案例：编辑式拼版，首案横向占据两列 */
#cases{background:var(--white);border-bottom:1px solid var(--line)}
.cases-home-grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;counter-reset:case}
.case-mini{counter-increment:case;border:1px solid var(--line);background:var(--white)}
.case-mini::before{content:counter(case,decimal-leading-zero);position:absolute;z-index:3;left:12px;top:12px;display:grid;place-items:center;
  min-width:30px;height:22px;padding:0 6px;background:rgba(7,26,43,.86);border:1px solid rgba(226,185,105,.5);color:var(--gold-2);font-size:9.5px;letter-spacing:.12em;font-weight:800}
.case-mini img{height:190px}
.case-mini:first-child{grid-column:span 2;flex-direction:row;min-height:330}
.case-mini:first-child img{width:58%;height:100%;min-height:330;flex:0 0 58%}
.case-mini:first-child .case-mini-body{width:42%;padding:30px 28px;justify-content:center}
.case-mini:first-child h3{font-size:24px;line-height:1.2;letter-spacing:-.03em}
.case-mini:first-child p{font-size:13.5px;line-height:1.8}
.case-mini h3{font-size:15px;line-height:1.3;color:var(--ink)}
.case-mini-tag{color:var(--gold);font-size:9.5px;letter-spacing:.08em;font-weight:800}
.case-mini p{color:var(--muted);font-size:12px;line-height:1.7}
.case-mini::after,.case-card .case-play,.case-mini .case-play{display:none!important}

/* 内页首屏：统一为中性海军蓝，不再偏冷蓝 */
.page-hero{background:
  linear-gradient(90deg,rgba(4,15,26,.97) 0%,rgba(6,21,35,.88) 42%,rgba(6,21,35,.28) 72%,rgba(6,21,35,.12) 100%),
  linear-gradient(180deg,rgba(4,15,26,.2),rgba(4,15,26,.78)),
  url("img/ru-hero.webp") right 50% / cover no-repeat}

/* 案例页：统计条改为深色档案带，流程区回到暖纸色 */
.v2-cases .stats{padding:0;background:var(--navy)}
.v2-cases .stats .container{width:100%;max-width:none}
.v2-cases .stats-grid{grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;border:0;background:rgba(255,255,255,.15);
  box-shadow:none;border-radius:0;overflow:visible}
.v2-cases .stat-cell{padding:34px 36px;border:0;background:rgba(8,25,41,.84)}
.v2-cases .stat-cell b{color:var(--gold-2)}
.v2-cases .stat-cell small{color:rgba(255,255,255,.62)}
.v2-cases #process{background:var(--paper);color:var(--ink);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.v2-cases #process .section-title{color:var(--ink)}
.v2-cases #process .section-copy{color:var(--muted)}
.v2-cases #process .role-grid{background:var(--line);border-color:var(--line)}
.v2-cases #process .role-item{background:var(--white);border-color:var(--line)}
.v2-cases #process .role-item h4{color:var(--gold)}
.v2-cases #process .role-item p{color:var(--muted)}
.v2-cats .cat-hero::after{content:"16 / 172";position:absolute;right:38px;bottom:30px;color:rgba(255,255,255,.075);
  font-size:88px;line-height:1;font-weight:900;letter-spacing:-.06em;pointer-events:none}
.v2-cats .cat-search{background:#f2eee5;border-bottom:1px solid #ded6c6}
.v2-cats .cs-box{border-color:#ded6c6}
.v2-cats .cs-box:focus-within{border-color:#b8893f}

/* 人物：档案式职责行，不再一排圆角小卡 */
#manager.aliya-sec{background:radial-gradient(720px 460px at 12% 48%,rgba(185,135,50,.09),transparent 68%),var(--paper);border-bottom:1px solid var(--line);padding:96px 0}
#manager .aliya-name{letter-spacing:-.04em}
#manager .aliya-role{display:inline-block;padding:6px 0 6px 12px;border-left:2px solid var(--gold);color:var(--blue)}
#manager .aliya-photo{position:relative;aspect-ratio:3/4;overflow:hidden;border:1px solid rgba(185,135,50,.44);background:#0a1b2a;box-shadow:0 28px 58px rgba(10,24,36,.16)}
#manager .aliya-photo img{position:relative;z-index:2;width:100%;height:100%;object-fit:cover;object-position:center 52%;filter:none}
#manager .aliya-photo::after{content:"ПРОВЕРКА ПАРТИИ · НАНЬТУН";position:absolute;z-index:4;left:0;bottom:0;padding:8px 11px;
  background:rgba(7,26,43,.9);border-top:1px solid rgba(226,185,105,.35);border-right:1px solid rgba(226,185,105,.35);
  color:var(--gold-2);font-size:8.5px;letter-spacing:.14em;font-weight:800}
#manager .aliya-ring,#manager .aliya-ring-2{display:none}
#manager .aliya-list{gap:0 34px}
#manager .aliya-item{padding:17px 0 17px 18px;border:0;border-left:2px solid rgba(185,135,50,.44);border-bottom:1px solid var(--line);background:transparent}
#manager .aliya-item:first-child{border-top:1px solid var(--line)}
#manager .aliya-item:nth-child(2){border-top:1px solid var(--line)}
#manager .aliya-tag{background:var(--white);border:1px solid var(--line);border-left:2px solid var(--gold);box-shadow:none}
#manager .aliya-chip{background:var(--white);border-color:var(--line)}

/* 流程：浅底上保留一张深色重点卡（仅首页，避免覆盖内页同名区块） */
.v2-home #process{background:var(--white);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.v2-home #process .supplier-panel{border-radius:2px;box-shadow:0 24px 58px rgba(7,26,43,.18)}
.v2-home #process .process-list{box-shadow:none;border-color:var(--line)}
.v2-home #process .process-step{border-bottom:1px solid var(--line)}
.v2-home #process .process-num{color:var(--gold)}

/* 联系：深色收尾，视觉上与首屏呼应 */
#contact{background:var(--paper);padding-top:92px;padding-bottom:92px}
#contact .contact-band{border:1px solid #193850;border-radius:2px;align-items:center;background:linear-gradient(135deg,#0b263d,#061726);box-shadow:0 28px 70px rgba(7,26,43,.2)}
#contact .contact-band h2{color:#fff8eb}
#contact .contact-band p{color:rgba(255,255,255,.64)}
#contact .contact-list{border-color:rgba(255,255,255,.19);background:rgba(255,255,255,.17);border-radius:2px}
#contact .contact-item{background:var(--white)}
#contact .contact-label{color:var(--gold)}
#contact .contact-value a{color:var(--ink)}
#contact .btn-secondary{color:#fff8eb;border-color:rgba(255,255,255,.3);background:transparent}
#contact .btn-secondary:hover{color:var(--gold-2);border-color:var(--gold-2)}

/* 内页：深色模块回归深色，CTA 统一收尾 */
.section-dark{color:#f7f0e2;background:var(--navy)}
.section-dark .section-title,.section-dark h2{color:#fff8eb}
.section-dark .section-copy{color:rgba(255,255,255,.65)}
.timeline{background:rgba(255,255,255,.12);border-color:rgba(255,255,255,.14);box-shadow:none}
.timeline-step{background:rgba(8,25,41,.82)}
.timeline-index{border-right-color:rgba(255,255,255,.14);background:rgba(255,255,255,.03);color:var(--gold-2)}
.timeline-text strong{color:#fff8eb}.timeline-text span{color:rgba(255,255,255,.64)}
.value-card{background:rgba(255,255,255,.045);border-color:rgba(255,255,255,.14)}
.value-card h3{color:var(--gold-2)}.value-card p{color:rgba(255,255,255,.66)}
.role-grid{border-color:rgba(255,255,255,.14);box-shadow:none}
.role-item{background:rgba(255,255,255,.045);border-color:rgba(255,255,255,.14)}
.role-item h4{color:var(--gold-2)}.role-item p{color:rgba(255,255,255,.64)}
.cta{color:#fff8eb;border:1px solid #193850;background:var(--navy);box-shadow:0 22px 54px rgba(7,26,43,.18)}
.cta h2{color:#fff8eb}.cta p{color:rgba(255,255,255,.65)}.cta .section-kicker{color:var(--gold-2)}
.cta .btn-secondary{color:#fff8eb;border-color:rgba(255,255,255,.3);background:transparent}
.cat-block{border-color:var(--line);background:var(--white);box-shadow:none}
.cat-tail{background:var(--paper)}
.about-page,.cases-page,.cat-body-wrap{background:var(--paper)}
.about-page .section-white,.cases-page .section-white{background:var(--white)}

@media(max-width:1180px){
  .route-bar{grid-template-columns:160px minmax(0,1fr);gap:26px}
  .route-coord{display:none}
}
@media(max-width:1080px){
  .cases-home-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .case-mini:first-child{grid-column:span 2}
  .cat-grid{grid-template-columns:repeat(3,minmax(0,1fr))}
  #guarantee .cred-grid{grid-template-columns:1fr 1fr}
  .inspection-proof{grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:36px}
}
@media(max-width:900px){
  #capability .capability-grid{grid-template-columns:1fr 1fr}
  #about .about-metrics{padding-top:58px}
  .metric-panel{grid-template-columns:1fr 1fr;padding-top:58px}
  .v2-cats .cat-hero::after{display:none}
  .route-bar{min-height:82px}
  .hero-person-photo{display:none}
  .hero-person-photo::before{display:none}
  .hero-person-card{padding:18px 18px;min-height:0}
}
@media(max-width:640px){
  .route-bar{grid-template-columns:1fr;gap:18px;padding:22px 0}
  .route-flow{grid-template-columns:repeat(2,1fr);gap:8px 18px}
  .route-flow::before{display:none}
  .route-step{padding-top:20px;padding-left:20px;text-align:left}
  .route-step::before{left:6px;margin:0}
  .route-step small{margin-bottom:3px}
  .hero-person-photo::before{display:none}
  .hero-person-photo{display:none;position:absolute;width:104px;right:8px;bottom:10px;margin:0;z-index:4;aspect-ratio:5/6;border-color:rgba(226,185,105,.32)}
  .hero-person-card{padding:16px 16px;min-height:0}
  #capability .capability-grid{grid-template-columns:1fr}
  #capability .capability-card{min-height:0}
  #guarantee{padding-top:66px;padding-bottom:66px}
  #guarantee .cred-grid{grid-template-columns:1fr}
  .inspection-proof{grid-template-columns:1fr;gap:34px;margin-top:42px;padding-top:38px}
  .inspection-proof h3{font-size:27px}
  .report-visual{transform:none}
  .report-stamp{right:4px;top:10px;transform:rotate(2deg)}
  .proof-facts{grid-template-columns:1fr}
  .proof-facts li{padding:10px 0}
  .cat-grid{grid-template-columns:1fr 1fr;gap:10px}
  .cases-home-grid{grid-template-columns:1fr}
  .cat-card h3{font-size:13px;padding:14px 13px 0}
  .cat-card p{padding:6px 13px 0;font-size:10.5px}
  .cat-arrow{padding:12px 13px 14px}
  .case-mini:first-child{grid-column:auto;flex-direction:column;min-height:0}
  .case-mini:first-child img{width:100%;height:190px;min-height:0;flex:none}
  .case-mini:first-child .case-mini-body{width:100%;padding:20px 16px 22px}
  .case-mini:first-child h3{font-size:18px}
  #manager .aliya-list{gap:0}
  #manager .aliya-item{padding:15px 0 15px 14px}
  #contact{padding-top:64px;padding-bottom:64px}
  #contact .hero-actions{display:grid;grid-template-columns:1fr;gap:9px}
  #contact .hero-actions .btn{width:100%}
}
</style>
<!--visual-v2:end-->
"""

ROUTE = r"""
    <!--visual-v2-route:start-->
    <div class="route-bar-wrap" aria-label="Маршрут заказа China Sells">
      <div class="container">
        <div class="route-bar">
          <div class="route-caption">Маршрут одного заказа<b>Наньтун → Россия</b></div>
          <div class="route-flow">
            <div class="route-step"><small>01</small>Запрос и образцы</div>
            <div class="route-step"><small>02</small>Фабрика и производство</div>
            <div class="route-step"><small>03</small>Инспекция и документы</div>
            <div class="route-step"><small>04</small>Склад и доставка</div>
          </div>
          <div class="route-coord"><b>NANTONG</b>31.98°N / 120.89°E</div>
        </div>
      </div>
    </div>
    <!--visual-v2-route:end-->
"""

PROOF = r"""
        <!--visual-v2-proof:start-->
        <div class="inspection-proof">
          <div class="report-visual">
            <img src="docs/inspection-report-preview.webp" alt="Образец отчёта об инспекции партии" width="760" height="511" loading="lazy" decoding="async">
            <span class="report-stamp">ДЕМО-ОБРАЗЕЦ</span>
          </div>
          <div class="proof-copy">
            <div class="proof-kicker">Отчёт о проверке партии</div>
            <h3>Что вы видите до оплаты партии</h3>
            <p>Перед отправкой фиксируем фото и видео с фабрики, замеры, дефекты, комплектацию и упаковку. Итог — понятный PDF-отчёт, по которому можно принимать решение, а не только слова переписки.</p>
            <ul class="proof-facts">
              <li><b>Фото и видео</b>С производства и готовой партии</li>
              <li><b>Замеры и дефекты</b>По согласованным критериям приёмки</li>
              <li><b>Упаковка и маркировка</b>Проверка перед консолидацией</li>
              <li><b>PDF-отчёт</b>Единый документ по партии</li>
            </ul>
            <div class="proof-actions">
              <a class="btn btn-primary" href="docs/inspection-report-sample.pdf" target="_blank" rel="noreferrer">Посмотреть образец отчёта</a>
            </div>
            <p class="proof-note">Демонстрационный образец структуры отчёта. Не является записью реальной поставки.</p>
          </div>
        </div>
        <!--visual-v2-proof:end-->
"""

# ---------------- index ----------------
p = ROOT / "index.html"
html = p.read_text(encoding="utf-8")

if '<body class="v2-home">' not in html:
    html = html.replace("<body>", '<body class="v2-home">', 1)

# 首屏改为工作现场照片，保留 Aliya 联系卡；负责人板块改用可核查的验货现场照片
hero_photo = '''<div class="hero-person-photo">
              <img src="img/work/warehouse.webp" alt="Работа на складе в Наньтуне" width="1881" height="1254" decoding="async">
            </div>'''
html = re.sub(r'<div class="hero-person-photo">[\s\S]*?</div>', hero_photo, html, count=1)

manager_photo = '''<img src="img/work/textile-inspection.webp" alt="Проверка домашнего текстиля на фабрике в Наньтуне" width="1881" height="1254" loading="lazy" decoding="async">'''
html = re.sub(
    r'<img src="img/aliya\.webp"[\s\S]*?decoding="async">',
    manager_photo,
    html,
    count=1,
)

# remove previous markers + generated category photos for idempotency
html = re.sub(r"\n?" + re.escape(START) + r"[\s\S]*?" + re.escape(END) + r"\n?", "\n", html)
html = re.sub(r"\n?" + re.escape(ROUTE_START) + r"[\s\S]*?" + re.escape(ROUTE_END) + r"\n?", "\n", html)
html = re.sub(r"\n?" + re.escape(PROOF_START) + r"[\s\S]*?" + re.escape(PROOF_END) + r"\n?", "\n", html)
html = re.sub(r'<div class="cat-photo">[\s\S]*?</div>\n?', "", html)

# insert route strip after hero
html, route_anchor_count = re.subn(
    r'</section>\s*\n\s*<section class="section" id="about">',
    '</section>\n' + ROUTE + '\n    <section class="section" id="about">',
    html,
    count=1,
)
if route_anchor_count != 1:
    raise RuntimeError("hero/about anchor missing")

# insert photo into every home category card
def add_photo(match):
    prefix, cat_id, ico = match.group(1), match.group(2), match.group(3)
    return (
        prefix
        + f'<div class="cat-photo"><img src="img/cat-{cat_id}.webp" '
          f'alt="{cat_id} — категория поставок China Sells" width="380" height="285" '
          f'loading="lazy" decoding="async"></div>\n            '
        + ico
    )

html, count = re.subn(
    r'(<a class="cat-card" href="categories.html#([\w-]+)">\s*)(<div class="cat-ico">)',
    add_photo,
    html,
)
if count != 10:
    raise RuntimeError(f"expected 10 cat cards, inserted photos for {count}")

# insert inspection report module after guarantee note
proof_pattern = re.compile(
    r'(<div class="party-note">[\s\S]*?</div>)(\s*</div>\s*</section>\s*<section class="section" id="offer">)'
)
html, proof_count = proof_pattern.subn(lambda m: m.group(1) + PROOF + m.group(2), html, count=1)
if proof_count != 1:
    raise RuntimeError("guarantee proof insertion failed")

html = html.replace("</head>", CSS + "\n</head>", 1)
p.write_text(html, encoding="utf-8")
print("index.html visual-v2 inserted, cat photos:", count)

# ---------------- other pages ----------------
for name, body_class in (("about.html", "v2-about"), ("cases.html", "v2-cases"), ("categories.html", "v2-cats")):
    p = ROOT / name
    html = p.read_text(encoding="utf-8")
    if f'<body class="{body_class}">' not in html:
        html = html.replace("<body>", f'<body class="{body_class}">', 1)
    html = re.sub(r"\n?" + re.escape(START) + r"[\s\S]*?" + re.escape(END) + r"\n?", "\n", html)
    if "</head>" not in html:
        raise RuntimeError(f"</head> missing in {name}")
    html = html.replace("</head>", CSS + "\n</head>", 1)
    p.write_text(html, encoding="utf-8")
    print(name, "visual-v2 inserted")
