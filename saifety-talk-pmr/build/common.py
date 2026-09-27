"""Shared page chrome, theme tokens and chart helpers for the SAiFETY Talk PMR HTML deliverables."""
import html
import json

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800'
         '&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap">')

CSS = r"""
:root{
  color-scheme: light;
  --bg:#f3f4f7; --surface:#ffffff; --surface-2:#eceef3; --ink:#131a2b; --ink-2:#48526a; --muted:#737c90;
  --line:#dde1e9; --line-2:#c7ccd8; --band:#131a2b; --band-ink:#ffffff; --band-ink-2:#aab3c5;
  --accent:#e4531b; --accent-ink:#b5400e; --amber:#f2a100; --amber-ink:#8a5a00;
  --good:#0ca30c; --good-ink:#006300; --warn:#fab219; --warn-ink:#7a5200; --crit:#d03b3b; --crit-ink:#a82424;
  --s1:#2a78d6; --s2:#eb6834; --wash:rgba(42,120,214,.10);
  --shadow:0 1px 2px rgba(19,26,43,.06),0 4px 16px rgba(19,26,43,.05);
  --display:"Archivo","Helvetica Neue",Arial,sans-serif;
  --body:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Menlo,monospace;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    color-scheme: dark;
    --bg:#0d1220; --surface:#151c2d; --surface-2:#1c2437; --ink:#eef1f7; --ink-2:#b4bdcd; --muted:#8a93a7;
    --line:#28324a; --line-2:#36415c; --band:#0a0f1b; --band-ink:#ffffff; --band-ink-2:#9aa4b8;
    --accent:#ff6a2b; --accent-ink:#ff8b57; --amber:#f5a300; --amber-ink:#f5b53d;
    --good-ink:#2fc22f; --warn-ink:#f5c04a; --crit-ink:#f07a7a;
    --s1:#3987e5; --s2:#d95926; --wash:rgba(57,135,229,.14);
    --shadow:0 1px 2px rgba(0,0,0,.3);
  }
}
:root[data-theme="dark"]{
  color-scheme: dark;
  --bg:#0d1220; --surface:#151c2d; --surface-2:#1c2437; --ink:#eef1f7; --ink-2:#b4bdcd; --muted:#8a93a7;
  --line:#28324a; --line-2:#36415c; --band:#0a0f1b; --band-ink:#ffffff; --band-ink-2:#9aa4b8;
  --accent:#ff6a2b; --accent-ink:#ff8b57; --amber:#f5a300; --amber-ink:#f5b53d;
  --good-ink:#2fc22f; --warn-ink:#f5c04a; --crit-ink:#f07a7a;
  --s1:#3987e5; --s2:#d95926; --wash:rgba(57,135,229,.14);
  --shadow:0 1px 2px rgba(0,0,0,.3);
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 var(--body)}
a{color:var(--accent-ink)}
:focus-visible{outline:2px solid var(--s1);outline-offset:2px}
.wrap{max-width:1180px;margin:0 auto;padding-inline:20px}
header.band{background:var(--band);color:var(--band-ink);padding-block:36px 30px}
header.band .eyebrow{font:600 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--band-ink-2);display:flex;gap:10px;flex-wrap:wrap;align-items:center}
header.band .eyebrow .mark{display:inline-block;width:14px;height:14px;border-radius:3px 3px 3px 0;background:var(--accent)}
header.band h1{font:800 clamp(30px,5vw,48px)/1.05 var(--display);letter-spacing:-.01em;margin:14px 0 10px;text-wrap:balance}
header.band h1 em{font-style:normal;color:var(--accent)}
header.band p.lede{max-width:70ch;color:var(--band-ink-2);margin:0;font-size:15.5px}
header.band .meta{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
header.band .meta span{font:500 12px/1 var(--mono);border:1px solid rgba(255,255,255,.18);border-radius:999px;padding:7px 11px;color:var(--band-ink)}
.caveat{display:flex;gap:12px;align-items:flex-start;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--amber);border-radius:8px;padding:14px 16px;margin-block:22px 8px;color:var(--ink-2);font-size:14px}
.caveat b{color:var(--ink)}
.caveat svg{flex:none;margin-top:2px}
nav.toc{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}
nav.toc .wrap{display:flex;gap:4px;overflow-x:auto;padding-block:8px;scrollbar-width:thin}
nav.toc a{flex:none;font:500 12.5px/1 var(--body);color:var(--ink-2);text-decoration:none;padding:8px 10px;border-radius:6px;white-space:nowrap}
nav.toc a:hover{background:var(--surface-2);color:var(--ink)}
main{padding-block:10px 60px}
h2{font:800 26px/1.15 var(--display);margin:48px 0 14px;letter-spacing:-.005em;text-wrap:balance;scroll-margin-top:64px}
h2 .kicker{display:block;font:600 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--accent-ink);margin-bottom:10px}
h3{font:700 19px/1.25 var(--display);margin:34px 0 10px;text-wrap:balance;scroll-margin-top:64px}
h4{font:600 13px/1.3 var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2);margin:26px 0 10px}
p,li{max-width:78ch}
ul{padding-left:20px}
li{margin-block:4px}
hr{border:0;border-top:1px solid var(--line);margin-block:36px}
strong{font-weight:600}
code{font:13px var(--mono);background:var(--surface-2);padding:1px 5px;border-radius:4px}
.tbl{overflow-x:auto;margin-block:12px 18px;border:1px solid var(--line);border-radius:10px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th,td{text-align:left;vertical-align:top;padding:9px 12px;border-bottom:1px solid var(--line)}
th{font:600 11.5px/1.3 var(--mono);letter-spacing:.04em;text-transform:uppercase;color:var(--ink-2);background:var(--surface-2)}
table.wide{min-width:1080px}
table.wide td:last-child{min-width:240px}
tr:last-child td{border-bottom:0}
td{font-variant-numeric:tabular-nums}
blockquote{margin:12px 0;padding:14px 18px;background:var(--surface);border:1px solid var(--line);border-radius:10px;position:relative}
blockquote p{margin:0}
blockquote p:first-child{font-size:15.5px;color:var(--ink)}
blockquote p + p{margin-top:6px;color:var(--muted);font-size:12.5px;font-family:var(--mono)}
.badge{display:inline-flex;align-items:center;gap:6px;font:600 11.5px/1 var(--mono);letter-spacing:.02em;padding:5px 9px 5px 7px;border-radius:999px;white-space:nowrap;border:1px solid}
.badge::before{content:"";width:8px;height:8px;border-radius:50%}
.badge.good{color:var(--good-ink);border-color:color-mix(in srgb,var(--good) 45%,transparent);background:color-mix(in srgb,var(--good) 10%,transparent)}
.badge.good::before{background:var(--good)}
.badge.warn{color:var(--warn-ink);border-color:color-mix(in srgb,var(--warn) 60%,transparent);background:color-mix(in srgb,var(--warn) 14%,transparent)}
.badge.warn::before{background:var(--warn);border-radius:1px;transform:rotate(45deg);width:7px;height:7px}
.badge.crit{color:var(--crit-ink);border-color:color-mix(in srgb,var(--crit) 45%,transparent);background:color-mix(in srgb,var(--crit) 10%,transparent)}
.badge.crit::before{background:var(--crit);border-radius:1px}
.badge.neutral{color:var(--ink-2);border-color:var(--line-2);background:var(--surface-2)}
.badge.neutral::before{background:var(--muted)}
.chip{display:inline-grid;place-items:center;min-width:26px;height:22px;border-radius:5px;font:600 12px/1 var(--mono)}
.chip.V{background:color-mix(in srgb,var(--good) 18%,transparent);color:var(--good-ink)}
.chip.P{background:color-mix(in srgb,var(--warn) 24%,transparent);color:var(--warn-ink)}
.chip.I{background:color-mix(in srgb,var(--crit) 18%,transparent);color:var(--crit-ink)}
.chip.NA{color:var(--muted)}
.card{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:18px 20px;box-shadow:var(--shadow)}
.grid{display:grid;gap:14px}
.kpis{grid-template-columns:repeat(auto-fit,minmax(170px,1fr));margin-block:18px}
.kpi{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}
.kpi .label{font:500 12px/1.3 var(--body);color:var(--ink-2)}
.kpi .value{font:700 30px/1.05 var(--display);color:var(--ink)}
.kpi .sub{font-size:12.5px;color:var(--muted);line-height:1.4}
.kpi .value small{font-size:15px;color:var(--muted);font-weight:600}
.hero{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:14px;margin-block:18px;align-items:start}
@media (max-width:760px){.hero{grid-template-columns:1fr}}
.hero .card h3{margin-top:0}
.need{background:var(--band);color:var(--band-ink);border-color:transparent}
.need .eyebrow{font:600 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
.need p{color:var(--band-ink);font-size:17px;line-height:1.5;margin:10px 0 0;font-family:var(--display);font-weight:600}
.need .n{font:800 44px/1 var(--display);color:var(--amber);margin-top:14px}
.need .n span{font:500 13px var(--body);color:var(--band-ink-2);margin-left:8px}
.chart{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin-block:12px 18px}
.chart .ctitle{font:600 14px/1.3 var(--body);margin:0 0 2px}
.chart .csub{font-size:12.5px;color:var(--muted);margin:0 0 12px}
.legend{display:flex;flex-wrap:wrap;gap:14px;font-size:12.5px;color:var(--ink-2);margin:0 0 10px}
.legend i{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:6px;vertical-align:-2px}
.legend i.line{height:2px;border-radius:1px;vertical-align:3px;width:16px}
.legend i.dot{border-radius:50%}
.bars{display:grid;gap:10px}
.brow{display:grid;grid-template-columns:minmax(120px,260px) minmax(0,1fr) auto;gap:12px;align-items:center}
@media (max-width:620px){.brow{grid-template-columns:1fr auto}.brow .blabel{grid-column:1 / -1}}
.blabel{font-size:13px;color:var(--ink);line-height:1.3}
.blabel b{font-family:var(--mono);font-weight:600;color:var(--ink-2);margin-right:6px}
.track{display:flex;gap:2px;height:14px;border-radius:4px;overflow:hidden;background:var(--surface-2)}
.seg{height:100%;min-width:0;cursor:default}
.seg:hover,.seg:focus{filter:brightness(1.12)}
.seg.V{background:var(--good)} .seg.P{background:var(--warn)} .seg.I{background:var(--crit)} .seg.NA{background:transparent}
.bval{font:500 12.5px/1 var(--mono);color:var(--ink-2);white-space:nowrap;text-align:right}
.hbar{height:12px;border-radius:0 4px 4px 0;background:var(--s1)}
.hbar:hover,.hbar:focus{filter:brightness(1.12)}
svg text{font-family:var(--mono);font-size:11px;fill:var(--muted)}
svg .lbl{fill:var(--ink-2);font-family:var(--body);font-size:12px}
svg .lbl-strong{fill:var(--ink);font-family:var(--body);font-size:12.5px;font-weight:600}
svg .grid{stroke:var(--line);stroke-width:1}
svg .axis{stroke:var(--line-2);stroke-width:1}
svg .ref{stroke:var(--accent);stroke-width:1.5}
svg .reftext{fill:var(--accent-ink);font-weight:500}
svg .range{stroke:var(--line-2);stroke-width:2;stroke-linecap:round}
svg .band{fill:var(--wash)}
svg .m1{fill:var(--s1);stroke:var(--surface);stroke-width:2}
svg .m2{fill:var(--s2);stroke:var(--surface);stroke-width:2}
svg .hollow{fill:var(--surface);stroke:var(--s1);stroke-width:2}
svg .hollow2{fill:var(--surface);stroke:var(--s2);stroke-width:2}
svg .hollow0{fill:var(--surface);stroke:var(--ink);stroke-width:2}
svg .medtick{stroke:var(--ink);stroke-width:2;stroke-linecap:round}
svg .tick{stroke:var(--ink-2);stroke-width:2;stroke-linecap:round}
svg .col{fill:var(--s1)}
svg .hit{fill:transparent;cursor:default}
svg .hit:hover + .col, svg .col:hover{filter:brightness(1.12)}
#tip{position:fixed;z-index:50;pointer-events:none;background:var(--ink);color:var(--surface);padding:8px 10px;border-radius:6px;font:12.5px/1.35 var(--body);max-width:280px;box-shadow:0 4px 18px rgba(0,0,0,.2);opacity:0;transition:opacity .08s}
#tip b{display:block;font:600 14px/1.2 var(--display);margin-bottom:2px}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr));gap:14px}
.muted{color:var(--muted)}
.small{font-size:12.5px}
.foot{border-top:1px solid var(--line);margin-top:40px;padding-block:22px;color:var(--muted);font-size:12.5px}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
@media print{nav.toc{display:none}header.band{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
"""

TIP_JS = r"""
<div id="tip" role="status" aria-live="polite"></div>
<script>
(function(){
  var tip=document.getElementById('tip');
  function show(el,x,y){
    var t=el.getAttribute('data-tip'); if(!t) return;
    var parts=t.split('|'); tip.textContent='';
    var b=document.createElement('b'); b.textContent=parts[0]; tip.appendChild(b);
    if(parts[1]){ tip.appendChild(document.createTextNode(parts.slice(1).join(' · '))); }
    tip.style.opacity='1';
    var w=tip.offsetWidth,h=tip.offsetHeight;
    var left=Math.min(window.innerWidth-w-8,Math.max(8,x+12)), top=y-h-12; if(top<8) top=y+16;
    tip.style.left=left+'px'; tip.style.top=top+'px';
  }
  function hide(){tip.style.opacity='0'}
  document.addEventListener('pointermove',function(e){
    var el=e.target.closest&&e.target.closest('[data-tip]'); if(el) show(el,e.clientX,e.clientY); else hide();
  });
  document.addEventListener('focusin',function(e){
    var el=e.target.closest&&e.target.closest('[data-tip]'); if(!el) return;
    var r=el.getBoundingClientRect(); show(el,r.left+r.width/2,r.top);
  });
  document.addEventListener('focusout',hide);
  document.addEventListener('scroll',hide,{passive:true});
})();
</script>
"""

WARN_ICON = ('<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 2 21h20L12 3z" '
             'fill="none" stroke="var(--amber)" stroke-width="2" stroke-linejoin="round"/><path d="M12 10v5M12 18h.01" '
             'stroke="var(--amber)" stroke-width="2" stroke-linecap="round"/></svg>')

CAVEAT = ("Synthetic primary market research is a rapid simulation tool for stress-testing business assumptions and "
          "refining interview instruments. Because synthetic agents cannot reliably predict real-world human behavior "
          "or purchasing decisions, all findings must be validated through direct interviews with real human stakeholders.")


def esc(s):
    return html.escape(str(s), quote=True)


def caveat_box():
    return f'<div class="caveat" role="note">{WARN_ICON}<div><b>Synthetic research caveat.</b> {esc(CAVEAT)}</div></div>'


def page(title, description, eyebrow, h1_html, lede, meta, toc, body):
    toc_html = ''.join(f'<a href="#{esc(i)}">{esc(t)}</a>' for i, t in toc)
    meta_html = ''.join(f'<span>{esc(m)}</span>' for m in meta)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
{FONTS}
<style>{CSS}</style>
</head>
<body>
<header class="band"><div class="wrap">
<div class="eyebrow"><span class="mark" aria-hidden="true"></span>{esc(eyebrow)}</div>
<h1>{h1_html}</h1>
<p class="lede">{esc(lede)}</p>
<div class="meta">{meta_html}</div>
</div></header>
<nav class="toc" aria-label="Sections"><div class="wrap">{toc_html}</div></nav>
<main><div class="wrap">
{caveat_box()}
{body}
<div class="foot">SAiFETY Talk · A BuiltNOVA platform · Synthetic PMR study, 27 Sept 2026 · N = 10 synthetic respondents. {esc(CAVEAT)}</div>
</div></main>
{TIP_JS}
</body>
</html>
"""


def money(v):
    if v >= 1000:
        k = v / 1000
        return f"${k:,.0f}k" if k == int(k) else f"${k:,.1f}k"
    return f"${v:,.0f}"


VERDICT_CLASS = {"Validated": "good", "Partially Validated": "warn", "Invalidated": "crit"}


def verdict_badge(v):
    return f'<span class="badge {VERDICT_CLASS.get(v, "neutral")}">{esc(v)}</span>'


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
