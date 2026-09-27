"""Builds business_plan_revisions.html from research/synthesis_data.json recommendations,
organised by Disciplined Entrepreneurship step and grouped into the four plan areas."""
import os
import re

from common import esc, load, money, page

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = load(os.path.join(ROOT, "research", "synthesis_data.json"))

# What the upgraded deck (Sept 2026) says today, per DE step. Quoted or closely paraphrased from the slides.
DECK_TODAY = {
    "Step 2 — Beachhead": "Beachhead: North America mega industrial construction (semiconductor fabs, data centers, battery & advanced mfg., energy). Slide 12.",
    "Step 2 — Beachhead (Korea pilot)": "Planned paid pilot in Korean shipbuilding, target start Nov 2026 (slide 10; slide 14 still says Oct 2026). Priced per project-year.",
    "Step 3 — End User Profile": "End user: frontline foreperson. “Must be effortless and trusted.” Slide 3.",
    "Step 4 — TAM": "300–800 serviceable project organizations (base 520). Follow-on markets $5.3B–$15B/yr. Slide 12.",
    "Step 5 — Persona": "Persona: Elena, electrical foreperson. Top fears: crew member hurt 25%, slow response and SIMOPS 18%, blame for reporting 12%. Slide 3.",
    "Step 6 — Full Life Cycle Use Case": "Report by voice, photo or text in your own language; Ask for the applicable rule; Recognize a peer. Slides 4–5.",
    "Step 7 — High-Level Product Spec": "Report, Ask (cited IOGP, client rules, KOSHA, OSH Act), Recognize (points exchange, misuse limits). “AI is labeled. A person always reviews.” Slides 4–5.",
    "Step 8 — Quantified Value Proposition": "“Safety is the shortest lever on the schedule.” Fewer stoppages and schedule certainty. Pilot floors: W12 retention ≥40%, acceptance ≥95%, closure ≥60% in 14 days. Slides 3, 7, 10.",
    "Step 9 — Next 10 Customers": "Founder’s EPC network; Korean shipbuilding paid pilot; NA beachhead pilots in 2027. Slides 12, 14.",
    "Step 12 — Decision-Making Unit": "End user: foreperson. Champion: site safety / EHS manager. Economic buyer: project director, VP Construction, EHS director. Slide 3.",
    "Step 13 — Customer Acquisition Process": "Not specified. “Security readiness program” scheduled for 2027. Slide 14.",
    "Step 15 — Business Model": "“Priced per project against avoided disruption, not per seat.” Enterprise multi-project agreements $200,000+/yr. Slide 9.",
    "Step 16 — Pricing Framework": "$24,000 per project-year (200 residents × $10/user/mo), framed as 32% of a $150,000 two-year discretionary HSE budget. The founder brief tests $150,000/yr base. Slide 9.",
    "Step 17 — Lifetime Value": "Not specified.",
    "Step 19/20 — Key Assumptions (identify)": "H1–H4 tested first: friction down, participation, signal quality, ownership & action. Links 5–7 follow only if 1–4 hold. Slide 11.",
    "Step 21 — Test Key Assumptions": "The paid pilot measures three floors by Dec 2026. Slide 10.",
    "Step 22 — MVBP": "Prototype built: Report, Ask, Recognize, plus the Command queue. Slide 14.",
}

AREAS = [
    ("end-user-profile", "End User Profile", "Who the product is for, and who decides.", ["End User Profile"]),
    ("value-proposition", "Value Proposition", "What the product must do and how its value is measured.", ["Value Proposition"]),
    ("beachhead-tam", "Beachhead & TAM", "Where to win first and how big it really is.", ["Beachhead TAM"]),
    ("business-model", "Business Model", "How it is priced, sold and renewed.", ["Business Model"]),
    ("supporting-steps", "Supporting steps", "DMU, customers, assumptions and testing that the four areas depend on.", ["Other"]),
]

CONF = {"High": "good", "Medium": "warn", "Low": "neutral"}


def step_num(s):
    m = re.search(r"Step (\d+)", s)
    return int(m.group(1)) if m else 99


def rec_card(r):
    today = DECK_TODAY.get(r["step"], "Not specified in the deck.")
    return (f'<article class="rec"><div class="rhead"><span class="step">{esc(r["step"])}</span>'
            f'<span class="badge {CONF[r["confidence"]]}">{esc(r["confidence"])} confidence</span></div>'
            f'<div class="cmp"><div class="col today"><div class="nh">Deck today</div><p>{esc(today)}</p></div>'
            f'<div class="col rev"><div class="nh">Revise to</div><p>{esc(r["recommendation"])}</p></div></div>'
            f'<p class="ev"><b>Synthetic evidence:</b> {esc(r["evidence"])}</p></article>')


def tam_table():
    orgs = [300, 520, 800]
    prices = [(24000, "Deck price"), (60000, "Low end of revised range"), (95000, "Median WTP point"), (150000, "Brief base price")]
    head = ''.join(f'<th>{o} orgs</th>' for o in orgs)
    rows = ''
    for p, lab in prices:
        cells = ''.join(f'<td>${o * p / 1e6:,.1f}M</td>' for o in orgs)
        hl = ' class="hl"' if p == 95000 else ''
        rows += f'<tr{hl}><td><b>{money(p)}</b> · {esc(lab)}</td>{cells}</tr>'
    return (f'<div class="tbl"><table><thead><tr><th>Price per project-year</th>{head}</tr></thead><tbody>{rows}</tbody></table></div>'
            f'<p class="small muted">Annual beachhead revenue if every serviceable organization bought one project-year. The deck’s own org range (slide 12) × price. '
            f'This is illustrative. It assumes one active project per organization and 100% capture, and it has not been checked against owner-led programs (Step 4 recommendation).</p>')


EXTRA_CSS = """
<style>
.rec{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin-block:12px}
.rhead{display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between;margin-bottom:10px}
.step{font:700 16px/1.2 var(--display)}
.cmp{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:10px}
.cmp .col{border-radius:8px;padding:10px 12px;font-size:14px}
.cmp .col p{margin:4px 0 0}
.cmp .nh{font:600 11px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase}
.cmp .today{background:var(--surface-2);color:var(--ink-2)}
.cmp .today .nh{color:var(--muted)}
.cmp .rev{background:color-mix(in srgb,var(--accent) 8%,var(--surface));border:1px solid color-mix(in srgb,var(--accent) 30%,transparent)}
.cmp .rev .nh{color:var(--accent-ink)}
.cmp .rev p{color:var(--ink);font-weight:500}
.ev{font-size:13px;color:var(--ink-2);margin:10px 0 0}
.sub-h{font:600 12px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:22px 0 4px}
.kv{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:12px;margin-block:14px}
.kv .card h3{margin:0 0 6px;font-size:16px}
.kv .card ul{margin:0;padding-left:18px;font-size:14px}
.kv .keep{border-top:3px solid var(--good)}
.kv .change{border-top:3px solid var(--accent)}
.kv .add{border-top:3px solid var(--s1)}
tr.hl td{background:color-mix(in srgb,var(--amber) 12%,transparent)}
</style>
"""


def build():
    recs = D["recommendations"]
    nh = sum(r["confidence"] == "High" for r in recs)
    body = EXTRA_CSS
    body += f"""
<h2 id="summary"><span class="kicker">Summary</span>What the synthetic study says to keep, change and add</h2>
<p>{len(recs)} recommendations from the synthesis, {nh} of them high confidence. “High” means the signal was consistent across roles and both markets in this simulation.
It does not mean validated. Every row needs confirmation in real interviews (Step 21), using the field guide.</p>
<div class="kv">
<div class="card keep"><h3>Keep</h3><ul>
<li>The problem framing. Signals stay verbal (KA3, 10/10), nobody owns cross-contract closure (KA10, 9/10), lag and mis-routing (KA5, 7/10).</li>
<li>Flat project pricing with no per-seat charge (KA11, 6/6 buyers).</li>
<li>The pilot’s “publish the miss” discipline and its week-12 retention floor.</li></ul></div>
<div class="card change"><h3>Change</h3><ul>
<li>Price. 0 of 6 accept $150k as-is, and $24k reads as “the craft aren’t covered.” The median WTP point is $95k.</li>
<li>Lead value. Lead with verified cross-employer closure and triage hours, not stoppage or LD avoidance (KA9, 50%).</li>
<li>The AI story. “A person always reviews” is table stakes (KA7, 0/10 fully validated). The reviewer is a persona.</li></ul></div>
<div class="card add"><h3>Add</h3><ul>
<li>Vetoes to the DMU: labor, legal, IT security, procurement, owner contracts (10/10 named one).</li>
<li>A reporter-identity model and no-login reporting (8/10 and 9/10).</li>
<li>Four new key assumptions: anonymity, reviewer capacity, legality of an owner-held queue, and the purchasing unit.</li></ul></div>
</div>
<h3 id="step-index">Step index</h3>
<div class="tbl"><table><thead><tr><th>DE step</th><th>Area</th><th>Confidence</th></tr></thead><tbody>
{''.join(f'<tr><td>{esc(r["step"])}</td><td>{esc(r["area"])}</td><td><span class="badge {CONF[r["confidence"]]}">{esc(r["confidence"])}</span></td></tr>' for r in sorted(recs, key=lambda r: step_num(r["step"])))}
</tbody></table></div>
"""
    toc = [("summary", "Summary")]
    for aid, title, sub, keys in AREAS:
        rs = sorted([r for r in recs if r["area"] in keys], key=lambda r: step_num(r["step"]))
        if not rs:
            continue
        body += f'<h2 id="{aid}"><span class="kicker">{esc(sub)}</span>{esc(title)}</h2>'
        high = [r for r in rs if r["confidence"] == "High"]
        rest = [r for r in rs if r["confidence"] != "High"]
        if high:
            body += '<div class="sub-h">High confidence</div>' + ''.join(rec_card(r) for r in high)
        if rest:
            body += '<div class="sub-h">Directional (medium or low confidence)</div>' + ''.join(rec_card(r) for r in rest)
        if aid == "beachhead-tam":
            body += '<h3 id="tam-recompute">Beachhead revenue at the prices buyers actually signaled</h3>' + tam_table()
        toc.append((aid, title))
    out = page(
        title="SAiFETY Talk Plan Revisions",
        description="Recommended revisions to End User Profile, Value Proposition, Beachhead TAM and Business Model, organized by Disciplined Entrepreneurship step.",
        eyebrow="A BuiltNOVA platform · Disciplined Entrepreneurship · Plan revisions",
        h1_html="The problem holds. <em>The price and the promise move.</em>",
        lede=("Recommendations from a 10-persona synthetic study, mapped to Bill Aulet’s 24 Steps. Each card compares what the September 2026 deck says "
              "today with the proposed revision and the synthetic evidence behind it."),
        meta=[f"{len(recs)} recommendations", f"{nh} high confidence", "Steps 2–22", "Deck: Upgraded, Sept 2026", "27 Sept 2026"],
        toc=toc, body=body)
    with open(os.path.join(ROOT, "business_plan_revisions.html"), "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote business_plan_revisions.html", len(out))


if __name__ == "__main__":
    build()
