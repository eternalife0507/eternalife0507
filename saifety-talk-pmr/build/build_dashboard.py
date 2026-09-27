"""Builds synthetic_pmr_dashboard.html from synthetic_pmr_dashboard.md + research/synthesis_data.json.

The HTML carries the full Markdown content (so the two stay identical) and adds visual cards,
metric badges and charts drawn from the same JSON the Markdown tables were written from.
"""
import os
import re

import markdown

from common import esc, load, money, page, verdict_badge

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = load(os.path.join(ROOT, "research", "synthesis_data.json"))
MD = open(os.path.join(ROOT, "synthetic_pmr_dashboard.md"), encoding="utf-8").read()


# ---------------------------------------------------------------- components
def kpis():
    a = D["assumptions"]
    nv = sum(x["verdict"] == "Validated" for x in a)
    npv = sum(x["verdict"] == "Partially Validated" for x in a)
    ni = sum(x["verdict"] == "Invalidated" for x in a)
    w = D["wtp"]
    acc = w["accept150"]
    tiles = [
        ("Assumptions validated", f"{nv}<small> / {len(a)}</small>", "Problem side: KA1, KA3, KA5, KA8, KA10, KA11"),
        ("Partially validated", f"{npv}<small> / {len(a)}</small>", "KA6, KA7 and KA12 have zero full validations"),
        ("Invalidated", f"{ni}<small> / {len(a)}</small>", "No assumption failed outright"),
        ("Median WTP point", money(w["all_median"]), f"“Getting expensive” figure, 6 buyers · mean {money(w['all_mean'])}"),
        ("Accept $150k as-is", f"{acc['accept']}<small> / 6</small>", f"{acc['conditional']} conditional · {acc['reject']} reject"),
        ("Prefer project pricing", f"{w['per_seat']['prefer_project']}<small> / 6</small>", "Per-seat rejected by every buyer"),
    ]
    cells = ''.join(f'<div class="kpi"><div class="label">{esc(l)}</div><div class="value">{v}</div>'
                    f'<div class="sub">{esc(s)}</div></div>' for l, v, s in tiles)
    return f'<div class="grid kpis">{cells}</div>'


def need_card():
    u = D["unmet_need"]
    return (f'<div class="card need"><div class="eyebrow">Single biggest unmet operational need</div>'
            f'<p>{esc(u["statement"])}</p>'
            f'<div class="n">{u["evidence_count"]}/10<span>respondents described it, across every role and both markets</span></div></div>')


def verdict_mix_card():
    a = D["assumptions"]
    rows = []
    for x in sorted(a, key=lambda r: -r["pctV"]):
        rows.append(f'<div class="brow"><div class="blabel"><b>{esc(x["id"])}</b>{esc(x["label"])}</div>'
                    f'<div class="track" aria-hidden="true"><div class="seg V" style="width:{x["pctV"]}%"></div></div>'
                    f'<div class="bval">{x["pctV"]:.0f}% V</div></div>')
    return (f'<div class="card"><h3>Share fully validated, by assumption</h3>'
            f'<p class="small muted">Validated respondents ÷ applicable n. Verdict line is 60%.</p>'
            f'<div class="bars">{"".join(rows)}</div></div>')


def at_a_glance():
    return (f'<h2 id="at-a-glance"><span class="kicker">Summary</span>At a glance</h2>{kpis()}'
            f'<div class="hero">{verdict_mix_card()}{need_card()}</div>')


def scorecard_chart():
    rows = []
    for x in D["assumptions"]:
        n = x["n"]
        segs = ''
        for k, name in (("V", "Validated"), ("P", "Partially validated"), ("I", "Invalidated")):
            c = x[k]
            if c:
                pct = 100 * c / n
                segs += (f'<div class="seg {k}" tabindex="0" style="width:{pct:.2f}%" '
                         f'data-tip="{c} of {n}|{esc(x["id"])} · {name} · {pct:.0f}%"></div>')
        na = f' · N/A {x["NA"]}' if x["NA"] else ''
        rows.append(f'<div class="brow"><div class="blabel"><b>{esc(x["id"])}</b>{esc(x["label"])}</div>'
                    f'<div class="track">{segs}</div>'
                    f'<div class="bval">n={n}{na} &nbsp;{verdict_badge(x["verdict"])}</div></div>')
    return (f'<div class="chart"><p class="ctitle">Scoring mix per key assumption</p>'
            f'<p class="csub">Each bar is 100% of applicable respondents (N/A excluded). Hover or focus a segment for counts.</p>'
            f'<div class="legend"><span><i style="background:var(--good)"></i>Validated</span>'
            f'<span><i style="background:var(--warn)"></i>Partially validated</span>'
            f'<span><i style="background:var(--crit)"></i>Invalidated</span></div>'
            f'<div class="bars">{"".join(rows)}</div></div>')


def van_westendorp_chart():
    buyers = D["wtp"]["buyers"]
    vw = D["wtp"]["van_westendorp_medians"]
    W, L, R, rowh, top = 920, 118, 24, 44, 40
    xmax = 350000
    rows = buyers + [{"short": "Median", "too_cheap": vw["too_cheap"], "bargain": vw["bargain"],
                      "getting_expensive": vw["getting_expensive"], "too_expensive": vw["too_expensive"],
                      "anchor": "", "median": True}]
    H = top + rowh * len(rows) + 30
    x = lambda v: L + (W - L - R) * v / xmax
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{W}px" role="img" aria-label="Van Westendorp price ladder per buyer">']
    for t in range(0, xmax + 1, 50000):
        out.append(f'<line class="grid" x1="{x(t):.1f}" x2="{x(t):.1f}" y1="{top-8}" y2="{H-26}"/>')
        out.append(f'<text x="{x(t):.1f}" y="{H-10}" text-anchor="middle">{money(t) if t else "$0"}</text>')
    for v, lab in ((24000, "$24k deck"), (150000, "$150k brief")):
        out.append(f'<line class="ref" x1="{x(v):.1f}" x2="{x(v):.1f}" y1="{top-14}" y2="{H-26}"/>')
        out.append(f'<text class="reftext" x="{x(v)+4:.1f}" y="{top-18}">{lab}</text>')
    for i, b in enumerate(rows):
        cy = top + rowh * i + rowh / 2
        cls = "m1" if b.get("anchor") == "A" else "m2"
        if b.get("median"):
            out.append(f'<line class="axis" x1="{L-110}" x2="{W-R}" y1="{cy-rowh/2:.1f}" y2="{cy-rowh/2:.1f}"/>')
        name = b["short"] + (f"  ·  {b['anchor']}" if b.get("anchor") else "")
        out.append(f'<text class="{"lbl-strong" if b.get("median") else "lbl"}" x="{L-12}" y="{cy+4:.1f}" text-anchor="end">{esc(name)}</text>')
        out.append(f'<rect class="band" x="{x(b["bargain"]):.1f}" y="{cy-7:.1f}" width="{x(b["getting_expensive"])-x(b["bargain"]):.1f}" height="14" rx="3"/>')
        out.append(f'<line class="range" x1="{x(b["too_cheap"]):.1f}" x2="{x(b["too_expensive"]):.1f}" y1="{cy:.1f}" y2="{cy:.1f}"/>')
        for v in (b["too_cheap"], b["too_expensive"]):
            out.append(f'<line class="tick" x1="{x(v):.1f}" x2="{x(v):.1f}" y1="{cy-6:.1f}" y2="{cy+6:.1f}"/>')
        hcls = "hollow0" if b.get("median") else ("hollow" if b.get("anchor") == "A" else "hollow2")
        out.append(f'<circle class="{hcls}" cx="{x(b["bargain"]):.1f}" cy="{cy:.1f}" r="5"/>')
        if b.get("median"):
            out.append(f'<circle cx="{x(b["getting_expensive"]):.1f}" cy="{cy:.1f}" r="6" style="fill:var(--ink);stroke:var(--surface);stroke-width:2"/>')
        else:
            out.append(f'<circle class="{cls}" cx="{x(b["getting_expensive"]):.1f}" cy="{cy:.1f}" r="6"/>')
        tip = (f'{b["short"]}: WTP {money(b["getting_expensive"])}|too cheap {money(b["too_cheap"])}|bargain {money(b["bargain"])}'
               f'|getting expensive {money(b["getting_expensive"])}|too expensive {money(b["too_expensive"])}')
        out.append(f'<rect class="hit" tabindex="0" x="{L-110}" y="{cy-rowh/2:.1f}" width="{W-R-L+110}" height="{rowh}" data-tip="{esc(tip)}"/>')
    out.append('</svg>')
    return (f'<div class="chart"><p class="ctitle">Price ladder per buyer, annual (USD)</p>'
            f'<p class="csub">Line runs from “too cheap” to “too expensive”; shaded band is bargain → getting expensive. '
            f'The filled dot is each buyer’s WTP point. Park’s figures are per division-year, converted from KRW.</p>'
            f'<div class="legend"><span><i class="dot" style="background:var(--s1)"></i>Anchor A (heard $150k first)</span>'
            f'<span><i class="dot" style="background:var(--s2)"></i>Anchor B (heard $24k first)</span>'
            f'<span><i class="dot" style="background:var(--surface);border:2px solid var(--ink-2)"></i>Bargain (hollow, arm color)</span>'
            f'<span><i class="line" style="background:var(--accent)"></i>Tested price points</span></div>'
            f'<div style="overflow-x:auto">{"".join(out)}</div></div>')


def tiers_chart():
    tiers = D["wtp"]["tiers"]
    W, H, L, B, top = 820, 230, 34, 44, 20
    ymax = 4
    cw = (W - L - 10) / len(tiers)
    y = lambda v: top + (H - top - B) * (1 - v / ymax)
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{W}px" role="img" aria-label="WTP tier distribution">']
    for t in range(0, ymax + 1):
        out.append(f'<line class="{"axis" if t == 0 else "grid"}" x1="{L}" x2="{W-10}" y1="{y(t):.1f}" y2="{y(t):.1f}"/>')
        out.append(f'<text x="{L-8}" y="{y(t)+4:.1f}" text-anchor="end">{t}</text>')
    for i, t in enumerate(tiers):
        cx = L + cw * i + cw / 2
        c = t["count"]
        if c:
            h = y(0) - y(c)
            bw = 24
            x0 = cx - bw / 2
            out.append(f'<path class="col" d="M{x0:.1f},{y(0):.1f} V{y(c)+4:.1f} Q{x0:.1f},{y(c):.1f} {x0+4:.1f},{y(c):.1f} '
                       f'H{x0+bw-4:.1f} Q{x0+bw:.1f},{y(c):.1f} {x0+bw:.1f},{y(c)+4:.1f} V{y(0):.1f} Z"/>')
            out.append(f'<text class="lbl-strong" x="{cx:.1f}" y="{y(c)-8:.1f}" text-anchor="middle">{c}</text>')
        else:
            out.append(f'<text x="{cx:.1f}" y="{y(0)-8:.1f}" text-anchor="middle">0</text>')
        who = ", ".join(t.get("who", [])) or "nobody"
        out.append(f'<rect class="hit" tabindex="0" x="{cx-cw/2+2:.1f}" y="{top}" width="{cw-4:.1f}" height="{y(0)-top:.1f}" '
                   f'data-tip="{esc(t["tier"])}: {c} of 6|{esc(who)}"/>')
        out.append(f'<text class="lbl" x="{cx:.1f}" y="{H-20}" text-anchor="middle">{esc(re.sub(r" / won.t buy", "", t["tier"]))}</text>')
    out.append(f'<text x="{L + cw*0 + cw/2:.1f}" y="{H-5}" text-anchor="middle">won’t buy</text>')
    out.append('</svg>')
    return (f'<div class="chart"><p class="ctitle">Buyers by WTP tier (count of 6)</p>'
            f'<p class="csub">WTP point = “getting expensive but still worth considering.” Only Bob reaches the $150k–$225k band.</p>'
            f'<div style="overflow-x:auto">{"".join(out)}</div></div>')


def acceptance_chart():
    w = D["wtp"]
    rows = [("$150,000 / project-year (full site)", w["accept150"]),
            ("$24,000 / project-year (~200 residents)", w["accept24"]),
            ("$10 / user / month (per seat)", {"accept": 0, "conditional": 0, "reject": w["per_seat"]["prefer_project"]})]
    html = []
    for lab, r in rows:
        segs = ''
        for k, cls, name in (("accept", "V", "Accept as-is"), ("conditional", "P", "Conditional"), ("reject", "I", "Reject")):
            c = r[k]
            if c:
                segs += f'<div class="seg {cls}" tabindex="0" style="width:{100*c/6:.2f}%" data-tip="{c} of 6|{esc(lab)} · {name}"></div>'
        html.append(f'<div class="brow"><div class="blabel">{esc(lab)}</div><div class="track">{segs}</div>'
                    f'<div class="bval">{r["accept"]} · {r["conditional"]} · {r["reject"]}</div></div>')
    return (f'<div class="chart"><p class="ctitle">Reaction to each price point (6 buyers)</p>'
            f'<p class="csub">Numbers at right: accept · conditional · reject.</p>'
            f'<div class="legend"><span><i style="background:var(--good)"></i>Accept as-is</span>'
            f'<span><i style="background:var(--warn)"></i>Conditional</span><span><i style="background:var(--crit)"></i>Reject</span></div>'
            f'<div class="bars">{"".join(html)}</div></div>')


def anchor_chart():
    buyers = D["wtp"]["buyers"]
    W, L, R, top, rowh = 900, 150, 24, 22, 50
    xmax = 225000
    x = lambda v: L + (W - L - R) * v / xmax
    H = top + rowh * 2 + 30
    arms = [("A", "A · $150k first", "m1", D["wtp"]["anchorA_median"]), ("B", "B · $24k first", "m2", D["wtp"]["anchorB_median"])]
    out = [f'<svg viewBox="0 0 {W} {H}" width="100%" style="max-width:{W}px" role="img" aria-label="WTP points by anchor arm">']
    for t in range(0, xmax + 1, 25000):
        out.append(f'<line class="grid" x1="{x(t):.1f}" x2="{x(t):.1f}" y1="{top}" y2="{H-26}"/>')
        if t % 50000 == 0:
            out.append(f'<text x="{x(t):.1f}" y="{H-10}" text-anchor="middle">{money(t) if t else "$0"}</text>')
    for i, (arm, lab, cls, med) in enumerate(arms):
        cy = top + rowh * i + rowh / 2
        out.append(f'<text class="lbl" x="{L-12}" y="{cy+4:.1f}" text-anchor="end">{esc(lab)}</text>')
        for b in [b for b in buyers if b["anchor"] == arm]:
            out.append(f'<circle class="{cls}" cx="{x(b["wtp_point"]):.1f}" cy="{cy:.1f}" r="6"/>')
            out.append(f'<circle class="hit" tabindex="0" cx="{x(b["wtp_point"]):.1f}" cy="{cy:.1f}" r="13" '
                       f'data-tip="{esc(b["short"])}: {money(b["wtp_point"])}|anchor {arm}"/>')
        out.append(f'<line class="medtick" x1="{x(med):.1f}" x2="{x(med):.1f}" y1="{cy-15:.1f}" y2="{cy+15:.1f}"/>')
        out.append(f'<text x="{x(med)+6:.1f}" y="{cy-10:.1f}">median {money(med)}</text>')
    out.append('</svg>')
    return (f'<div class="chart"><p class="ctitle">WTP points by anchor arm</p>'
            f'<p class="csub">n = 3 per arm, so this is directional only. The gap runs opposite to a classic anchoring lift and tracks budget authority instead.</p>'
            f'<div class="legend"><span><i class="dot" style="background:var(--s1)"></i>Anchor A</span>'
            f'<span><i class="dot" style="background:var(--s2)"></i>Anchor B</span>'
            f'<span><i class="line" style="background:var(--ink-2)"></i>Arm median</span></div>'
            f'<div style="overflow-x:auto">{"".join(out)}</div></div>')


def objections_chart():
    rows = []
    for o in D["objections"]:
        c = o["count"]
        rows.append(f'<div class="brow"><div class="blabel"><b>#{o["rank"]}</b>{esc(o["theme"])}</div>'
                    f'<div class="track" style="background:transparent"><div class="hbar" tabindex="0" style="width:{10*c}%" '
                    f'data-tip="{c} of 10|{esc(", ".join(o["who"]))}"></div></div>'
                    f'<div class="bval">{c}/10</div></div>')
    return (f'<div class="chart"><p class="ctitle">Objections by number of respondents raising them</p>'
            f'<p class="csub">Each respondent counted once per theme. Hover or focus a bar to see who.</p>'
            f'<div class="bars">{"".join(rows)}</div></div>')


# ---------------------------------------------------------------- markdown → html
def md_sections(text):
    parts = re.split(r'(?m)^## ', text)
    head, secs = parts[0], {}
    order = []
    for p in parts[1:]:
        title = p.split('\n', 1)[0].strip()
        secs[title] = '## ' + p
        order.append(title)
    return head, secs, order


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def convert(md_text):
    h = markdown.markdown(md_text, extensions=["tables", "sane_lists"])
    def tbl(m):
        t = m.group(0)
        cols = t.split('</thead>')[0].count('<th')
        return ('<div class="tbl"><table class="wide">' if cols >= 8 else '<div class="tbl"><table>') + t[len('<table>'):]
    h = re.sub(r'<table>.*?</table>', tbl, h, flags=re.S)
    h = h.replace('</table>', '</table></div>')
    for k in ("V", "P", "I"):
        h = h.replace(f'<td>{k}</td>', f'<td><span class="chip {k}">{k}</span></td>')
    h = h.replace('<td>–</td>', '<td><span class="chip NA">–</span></td>')
    for v in ("Partially Validated", "Validated", "Invalidated"):
        h = h.replace(f'<strong>{v}</strong>', verdict_badge(v))
    h = re.sub(r'<blockquote>\s*<p>(.*?)\n— (.*?)</p>\s*</blockquote>',
               lambda m: f'<blockquote><p>{m.group(1)}</p><p>— {m.group(2)}</p></blockquote>', h, flags=re.S)

    def h_ids(m):
        tag, txt = m.group(1), m.group(2)
        return f'<{tag} id="{slug(re.sub("<.*?>", "", txt))}">{txt}</{tag}>'
    h = re.sub(r'<(h[234])>(.*?)</\1>', h_ids, h)
    return h


def insert_after(h, heading_text, block):
    pat = re.compile(r'(<h[34] id="[^"]*">' + re.escape(heading_text) + r'</h[34]>)')
    new, n = pat.subn(lambda m: m.group(1) + block, h, count=1)
    assert n == 1, f"heading not found: {heading_text}"
    return new


def build():
    head, secs, order = md_sections(MD)
    wanted = ["Executive Summary", "Study Design Summary", "(a) Quantitative Synthesis", "(b) Qualitative Synthesis", "Implications"]
    assert set(wanted) <= set(order), order
    kickers = {"Executive Summary": "Headlines", "Study Design Summary": "Method",
               "(a) Quantitative Synthesis": "Scores", "(b) Qualitative Synthesis": "Voices", "Implications": "What to do next"}
    body = at_a_glance()
    toc = [("at-a-glance", "At a glance")]
    for t in wanted:
        h = convert(secs[t])
        sid = slug(t)
        h = re.sub(r'<h2 id="[^"]*">(.*?)</h2>', lambda m: f'<h2 id="{sid}"><span class="kicker">{kickers[t]}</span>{m.group(1)}</h2>', h, count=1)
        if t == "(a) Quantitative Synthesis":
            h = insert_after(h, "A1. Key Assumption Scorecard", scorecard_chart())
            h = insert_after(h, "Van Westendorp ladder by buyer", van_westendorp_chart())
            h = insert_after(h, "WTP tier distribution", tiers_chart())
            h = insert_after(h, "Price-point acceptance", acceptance_chart())
            h = insert_after(h, "Anchor A vs Anchor B", anchor_chart())
            h = insert_after(h, "A4. Objections Ranked", objections_chart())
        if t == "(b) Qualitative Synthesis":
            h = insert_after(h, "B3. The Single Biggest Unmet Operational Need", need_card())
        body += h
        toc.append((sid, {"(a) Quantitative Synthesis": "Quantitative", "(b) Qualitative Synthesis": "Qualitative",
                          "Study Design Summary": "Study design"}.get(t, t)))
    # sub-navigation for the densest sections
    toc += [("a1-key-assumption-scorecard", "A1 Scorecard"), ("a3-willingness-to-pay-buyer-grade-respondents-only", "A3 WTP"),
            ("a4-objections-ranked", "A4 Objections"), ("b2-recurring-field-language-and-trade-jargon", "B2 Jargon")]
    for i, _ in toc:
        assert f'id="{i}"' in body, i
    intro = re.sub(r'^# .*\n', '', head).strip()
    out = page(
        title="SAiFETY Talk PMR Dashboard",
        description="Synthetic primary market research dashboard: 10 persona interviews scored against 12 Step 20 key assumptions, WTP and objections.",
        eyebrow="A BuiltNOVA platform · Synthetic PMR · Step 20 test",
        h1_html="Crew speaks up. <em>Does the buyer pay?</em>",
        lede=intro,
        meta=["N = 10 synthetic interviews", "12 key assumptions", "6 buyer-grade WTP ladders", "Split-anchor pricing", "27 Sept 2026"],
        toc=toc, body=body)
    with open(os.path.join(ROOT, "synthetic_pmr_dashboard.html"), "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote synthetic_pmr_dashboard.html", len(out))


if __name__ == "__main__":
    build()
