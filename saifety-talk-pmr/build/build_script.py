"""Builds real_user_interview_script.html: the field-ready guide for real-human interviews.

Each question carries the synthetic study's signal and what still needs real-world validation,
pulled from research/synthesis_data.json (script_annotations) so the two cannot drift apart.
"""
import os

from common import esc, load, page

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = load(os.path.join(ROOT, "research", "synthesis_data.json"))
ANN = {a["q"]: a for a in D["script_annotations"]}
KA = {a["id"]: a for a in D["assumptions"]}

# Warm-up questions were not scored by the synthesis agent; their notes summarise corpus-level signals.
WARM_NOTES = {
    "W1": ("Every respondent's day was dominated by coordination and production pressure; safety arrived as interruptions, not as a task.",
           "Whether real crews describe the same shape of day, or whether synthetic agents over-structured it."),
    "W2": ("Coordination runs on radio, crew group chats, KakaoTalk/Zalo and the morning foremen's meeting. 'SIMOPS' was Priya's word alone.",
           "The actual channels per trade and shift, and who is left out of them (nights, travelers, migrants)."),
    "W3": ("KA3 was the only assumption validated 10/10: hazards are handled by walk-over and word of mouth, then vanish.",
           "The ratio of verbal fixes to written reports on a real site; ask to see the last week's written ones."),
    "W4": ("Paper cards and quotas persist only as owner or HQ KPIs. Procore, SafetyCulture and HQ portals are office-side.",
           "Which tool is the system of record for each company on site, and who reconciles them."),
    "W5": ("Managers rely on Monday reconciliation, dashboards and the super's word, and said so openly.",
           "How late information arrives, in hours, from a real log."),
}

GROUP_TAG = {"F": "Frontline", "M": "Site management", "B": "Buyer / budget", "R": "Reviewers", "K": "Korea module"}

SECTIONS = [
    {
        "id": "warm-up", "title": "Section 1 · Warm-up", "time": "≈ 8 min",
        "note": "Say nothing about software, AI, apps or BuiltNOVA. You are here to learn how their day works.",
        "qs": [
            ("W1", "All", "Walk me through yesterday from the moment you got to the gate until you left. What took most of your attention?",
             ["What happened right before that?", "Who did you have to wait on?"], None),
            ("W2", "All", "Who do you have to coordinate with on a normal day, other trades, other contractors or other departments? How does that coordination actually happen?",
             ["Show me the last message or radio call about it, if you can.", "Who gets left out of that loop?"], "KA8"),
            ("W3", "All", "When something on site looks off to you or your crew, what typically happens next? Walk me through the most recent example.",
             ["Who did you tell first?", "Was anything written down? Where?"], "KA3"),
            ("W4", "All", "What do you use day to day to keep track of work, permits, observations or issues: paper, radio, phone, software, anything else? What do you like and dislike about each?",
             ["Which one would you keep if you could keep only one?"], "KA3"),
            ("W5", "M B", "How do you find out what happened on site when you weren't there?",
             ["How many hours later, typically?", "What do you have to rebuild by hand?"], "KA5"),
        ],
    },
    {
        "id": "core", "title": "Section 2 · Core assessment", "time": "≈ 32 min",
        "note": "Riskiest assumptions first. Ask for the last specific time, not general opinions. Accept silence. Never agree or praise.",
        "qs": [
            ("C1", "All", "Tell me about the last time you saw something unsafe that another company created. What did you do, and why that instead of writing it up?",
             ["What would have happened to you if you had written it up?", "Who else knew about it?"], "KA1"),
            ("C2", "All", "When someone raises a hazard that involves another company's crew or their own supervisor, what happens to the person who raised it? Can you share an example, good or bad?",
             ["What did the rest of the crew conclude afterward?", "What did you do differently after that?", "[Stewards] How does the union get involved?"], "KA1"),
            ("C3", "All", "Think of a hazard you or your crew reported in the last month. What did you see or hear back afterward, and how long did it take?",
             ["Did the way that one went change whether you reported the next thing?", "What's the longest you've waited?"], "KA2"),
            ("C4", "All", "What has your site or company tried in the past to get more people to report: cards, quotas, rewards, or other programs? What happened to it after the first few weeks?",
             ["Roughly how many reports in week 1, week 4, week 12?", "Who stopped first? What did people call it in the break room?"], "KA2"),
            ("C5", "All", "Describe the moment you notice a hazard mid-task: where are you, what's in your hands, what's around you, and how much time do you realistically have to tell someone?",
             ["If you reported from exactly where you stood, what would stop you first: phone rules, gloves, noise, language, or who might find out?",
              "When do you actually get to your phone?"], "KA4"),
            ("C6", "All", "When a report does get made, walk me through its journey from the person who saw it to the person who fixes it. Where does it slow down, get lost or go to the wrong place?",
             ["How often is the owner guessed wrong?", "What happens to it at shift change?"], "KA5"),
            ("C7", "M R", "Before we met, I asked you to note how long observation triage took each day last week. Walk me through that log. What information do you need to decide, and what do you get wrong most often?",
             ["What do you rebuild by hand on Mondays?", "Who covers nights and weekends?"], "KA6"),
            ("N4", "M R", "When the number of reports goes up, who absorbs the extra work, and what gives first?",
             ["Has volume ever made you stop reading them carefully?", "Who reviews the reviewer?"], "KA6"),
            ("C8", "All", "[Show the printed mock item: category, owner, severity, 'confirmed by: J. Smith'.] This item arrived for your area. What do you do with it?",
             ["What would make you trust or ignore an item like this?", "After how many wrong ones would you stop looking?",
              "[Stewards] Who should be able to see who sent it?"], "KA7"),
            ("C9", "All", "How many times last week did another crew's work stop yours, or yours stop theirs? Take me through the most recent one.",
             ["How was it discovered, and by whom?", "What did it cost in hours?", "Who owned sorting it out?"], "KA8"),
            ("C10", "All", "Tell me about the most recent stop-work, permit revocation or stand-down you were affected by. What led up to it, and what did it cost the schedule?",
             ["Was the hazard known beforehand? By whom?", "Who could put a dollar figure on that, and where would they look it up?"], "KA9"),
            ("C11", "All", "When a hazard sits on the line between two employers, how does it get closed, and who proves it's closed?",
             ["Can we look at two or three closed items together? What shows they were fixed?", "What would an owner or lawyer ask to see?"], "KA10"),
            ("N5", "M B", "After an incident, what did investigators or lawyers ask for from your records? What would a record need to show so it protects you rather than exposes you?",
             ["Has an open item ever been used against the company?"], "KA10"),
            ("N1", "All", "What happens to an open hazard at shift change or when the night crew takes over the area?",
             ["Who tells nights? How?", "What's the last thing that fell through that gap?"], "KA5"),
            ("N2", "M B", "When an area is handed over to commissioning or operations, what happens to the open safety items and their history?",
             ["Who owns them after turnover?"], "KA10"),
            ("C12", "M B", "How are tools for the site's safety or field coordination paid for today? Whose budget, per what unit (worker, seat, project, month), and who has to sign?",
             ["Is any safety tool written into your subcontract or GC contract requirements? Who writes those?",
              "What was the last safety-related purchase, and how long did security and procurement take?"], "KA11"),
            ("N3", "M B", "When a project demobilizes, what happens to the records in the tools you used on it?",
             ["Who keeps them, for how long, and who pays for that?"], "KA11"),
        ],
    },
    {
        "id": "korea", "title": "Korea module", "time": "≈ 6 min",
        "note": "Insert after C5. Use an interpreter who is not employed by the prime or the subcontractor. Recruit migrant workers through community channels, not the employer.",
        "qs": [
            ("K1", "K", "When a worker who doesn't speak Korean sees a hazard, how does that information reach the prime's safety team today? Walk me through a recent case.",
             ["Who do you tell when your bilingual coworker is not there?", "How many days did it take to reach someone who could fix it?"], None),
            ("K2", "K", "Since the Serious Accidents Punishment Act, how has the way you record hazards and actions changed? What are you most careful about writing down?",
             ["What would a record need to show so it protects rather than exposes the CEO?"], None),
            ("K3", "K", "If the prime's system sent a task directly to a subcontractor's worker, what would legal or the subcontractor say about it?",
             ["Where is the line on direct instruction (불법파견)?"], None),
        ],
    },
    {
        "id": "concept", "title": "Section 3 · Concept and willingness to pay", "time": "≈ 12 min",
        "note": "Only now describe the concept. Read the statement verbatim. State the package before any price. Randomize which price the buyer hears first.",
        "concept": ("Some teams are testing a tool where any worker on site can report a hazard by voice, photo or text in their own language, "
                    "with no app to install and no login, in about the time it takes to send a text. The system suggests a category, severity "
                    "and responsible owner. A named human safety reviewer confirms or edits it before it goes anywhere. The owner sees one queue "
                    "of open items across all employers, and an item only closes when the fix is verified with a time- and location-stamped check. "
                    "The reporter gets a receipt when it's closed, and their identity is hidden from employers by default. It's priced per project, "
                    "with unlimited reporting for every worker."),
        "qs": [
            ("P1", "All", "In your own words, what would this change about your week, if anything? What wouldn't it change?", [], None),
            ("P2", "All", "What worries you about it? Which one of those worries, on its own, would make you or your crew refuse to use it?", [], None),
            ("P3", "All", "Who on your site would use it most, and who would ignore or resist it? Can you introduce me to one of the resisters?", [], None),
            ("P4", "F", "If this showed up on your site next month, what would decide whether you still used it in month three?", [], None),
            ("P5", "M B", "[State the package first] “Unlimited reporting for every worker on site. Licensed users are the reviewers and owners, about 200 people. "
             "Integration with your system of record is [included / not included].” Now imagine two ways to pay: a project subscription at [FIRST PRICE] per "
             "project-year, or per-seat licensing at about $10 per user per month. How would each land with you, and why?",
             ["[Reveal second price] Another version is priced at [SECOND PRICE]. How does that compare?",
              "Price pair: $150,000 full site and $60,000 single area. Randomize the order, and record it."], "KA11"),
            ("P6", "M B", "For the package I just described, at what annual price would this be so cheap you'd doubt it? A bargain? Getting expensive but still worth considering? Too expensive no matter what?",
             ["Would that change if integration were or weren't included?"], "KA12"),
            ("P6b", "M B", "On a scale of 1 to 5, how likely would you be to fund a 12-week pilot at $35,000? At $60,000? What about a full site-year at $95,000, $120,000 or $150,000? What drives the difference?",
             ["Randomize the order of the price points and record it."], "KA12"),
            ("P7", "M B", "Which budget line would it come from, and what would it need to replace or prove to get funded? What evidence after a 12-week pilot would get you to sign?",
             ["Who else has to say yes: legal, IT security, union, procurement, the owner?"], "KA12"),
            ("P8", "F", "If the company could buy this or hire one more safety person for your area, which would help you more, and why?", [], None),
            ("P9", "All", "Anything I should have asked but didn't? Who else should I talk to?", [], None),
        ],
    },
]


def annotation(qid):
    if qid in ANN:
        a = ANN[qid]
        return a["synthetic_signal"], a["needs_real_validation"]
    if qid in WARM_NOTES:
        return WARM_NOTES[qid]
    extra = {
        "N1": ("New in v2. Night and handover gaps were raised unprompted by Elena, Carlos, Marcus, Priya and Park.",
               "Whether night crews experience a different reporting reality; interview night foremen directly."),
        "N2": ("New in v2. Construction-to-operations turnover surfaced in P9 answers as a gap nobody owns.",
               "Who actually receives open items at turnover, and whether owners' operations teams would pay for the history."),
        "N3": ("New in v2. Data at demob was raised by Carlos, Marcus, Park and Tommy.",
               "Real retention obligations and who pays for them; confirm with legal and records teams."),
        "N4": ("New in v2. The reviewer bottleneck was raised by 9 of 10. KA6 scored 0 of 4 Validated.",
               "Actual reviewer capacity, especially nights and weekends, from a timed log."),
        "N5": ("New in v2. Discoverability was raised by 7 of 10 (deposition, SAPA 'exhibit A', controlling employer).",
               "Counsel's view in each market; what record design actually reduces exposure."),
        "P6b": ("New in v2. Replaces open-ended price probing with defined price points. Synthetic median WTP point was $95k; bargain median $37.5k.",
                "Purchase likelihood by price with n ≥ 30 buyers per segment; the synthetic sample of 6 cannot set a price."),
        "K3": ("New in v2. Park raised the illegal-dispatch constraint on prime-to-worker routing.",
               "Korean labor counsel's view and whether other yards share the concern."),
    }
    return extra.get(qid, ("", ""))


def q_card(q):
    qid, who, text, probes, ka = q
    sig, val = annotation(qid)
    tags = ''.join(f'<span class="tag">{esc(GROUP_TAG.get(t, "All roles"))}</span>' for t in who.split()) if who != "All" else '<span class="tag">All roles</span>'
    ka_html = ''
    if ka:
        a = KA[ka]
        cls = {"Validated": "good", "Partially Validated": "warn", "Invalidated": "crit"}[a["verdict"]]
        ka_html = f'<span class="badge {cls}" title="{esc(a["full"])}">{esc(ka)} · {esc(a["verdict"])} · {a["pctV"]:.0f}% V</span>'
    new = '<span class="tag new">New in v2</span>' if qid.startswith("N") or qid in ("P6b", "K3") else ''
    rewritten = '<span class="tag rew">Reworded</span>' if qid in ANN and ANN[qid].get("suggested_rewrite") and ANN[qid]["suggested_rewrite"] not in ("", "–") else ''
    probes_html = ''.join(f'<li>{esc(p)}</li>' for p in probes)
    probes_html = f'<ul class="probes">{probes_html}</ul>' if probes else ''
    notes = ''
    if sig or val:
        notes = (f'<div class="notes"><div class="note syn"><div class="nh">Synthetic study suggests</div><p>{esc(sig)}</p></div>'
                 f'<div class="note real"><div class="nh">Validate with real humans</div><p>{esc(val)}</p></div></div>')
    return (f'<article class="q" id="{esc(qid.lower())}"><div class="qhead"><span class="qid">{esc(qid)}</span>{tags}{ka_html}{new}{rewritten}</div>'
            f'<p class="qtext">{esc(text)}</p>{probes_html}{notes}</article>')


EXTRA_CSS = """
<style>
.q{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin-block:12px}
.qhead{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-bottom:8px}
.qid{font:700 15px/1 var(--display);background:var(--band);color:var(--band-ink);border-radius:6px;padding:6px 8px;min-width:40px;text-align:center}
.tag{font:500 11.5px/1 var(--mono);color:var(--ink-2);border:1px solid var(--line-2);border-radius:999px;padding:5px 9px}
.tag.new{color:var(--accent-ink);border-color:color-mix(in srgb,var(--accent) 50%,transparent)}
.tag.rew{color:var(--s1);border-color:color-mix(in srgb,var(--s1) 50%,transparent)}
.qtext{font:600 16.5px/1.45 var(--body);margin:4px 0 6px;max-width:75ch}
.probes{margin:4px 0 8px;color:var(--ink-2);font-size:14px}
.probes li::marker{content:"↳  ";color:var(--muted)}
.notes{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:10px;margin-top:10px}
.note{border-radius:8px;padding:10px 12px;font-size:13.5px}
.note p{margin:4px 0 0}
.note .nh{font:600 11px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase}
.note.syn{background:color-mix(in srgb,var(--s1) 9%,var(--surface));border:1px solid color-mix(in srgb,var(--s1) 30%,transparent)}
.note.syn .nh{color:var(--s1)}
.note.real{background:color-mix(in srgb,var(--accent) 8%,var(--surface));border:1px solid color-mix(in srgb,var(--accent) 30%,transparent)}
.note.real .nh{color:var(--accent-ink)}
.secthead{display:flex;flex-wrap:wrap;align-items:baseline;gap:12px;justify-content:space-between}
.secthead .time{font:500 12.5px var(--mono);color:var(--muted)}
.concept{background:var(--band);color:var(--band-ink);border-radius:12px;padding:18px 20px;margin-block:14px}
.concept .eyebrow{font:600 11px/1 var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--accent)}
.concept p{font:500 16px/1.55 var(--body);margin:10px 0 0;max-width:80ch}
.rules{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:12px}
.rules .card h3{margin:0 0 6px;font-size:16px}
.rules .card ul{margin:0;padding-left:18px;font-size:14px}
</style>
"""


def build():
    body = EXTRA_CSS
    body += """
<h2 id="how-to-use"><span class="kicker">Before you go to site</span>How to use this guide</h2>
<p>This is version 2 of the SAiFETY Talk interview instrument, rewritten after a 10-persona synthetic study. Each question shows two notes.
<b>Synthetic study suggests</b> is what the simulation produced, and it is a hypothesis only. <b>Validate with real humans</b> is what this interview has to establish.
Score each key assumption from what the respondent volunteers before Section 3, using the grid at the end.</p>
<div class="rules">
<div class="card"><h3>Who to recruit (Step 21)</h3><ul>
<li>Forepersons and 반장, 8–10</li><li>Crew: apprentices, travelers, migrant subcontracted workers, 8–10</li>
<li>GC safety coordinators who triage reports, 5–6</li><li>Union stewards or business agents, 3–4</li>
<li>Night-shift foremen, 3</li><li>Site safety managers, EHS directors, owner PDs, 6–8</li>
<li>Korea: HSE team leads and prime purchasing or IT security, 3–4</li></ul></div>
<div class="card"><h3>Consent and protection</h3><ul>
<li>Recruit frontline and migrant workers through the union hall or community groups, never through their employer.</li>
<li>Don't record names for frontline respondents. Use a code such as F-03.</li>
<li>Say plainly: “Nothing you say goes to your employer. You can skip any question.”</li>
<li>Use an interpreter who has no tie to the prime or the subcontractor.</li>
<li>Meet off site or at break, away from supervisors.</li></ul></div>
<div class="card"><h3>Interviewer rules</h3><ul>
<li>No product, AI, app or BuiltNOVA mention before Section 3.</li>
<li>Ask about the last specific time, not “would you…”.</li><li>Don't say “problem”, “pain” or “solution” first.</li>
<li>Follow up with: What happened next? Why? Can you show me?</li><li>Don't agree, praise or explain. Accept silence.</li></ul></div>
<div class="card"><h3>Bring with you</h3><ul>
<li>A printed mock routed item for C8, with no brand.</li><li>A pre-interview request to log triage time for one week (C7).</li>
<li>A request to show two or three recently closed cross-employer items (C11).</li>
<li>A randomized price-order card for P5 and P6b.</li></ul></div>
</div>
"""
    toc = [("how-to-use", "How to use")]
    for s in SECTIONS:
        body += (f'<div class="secthead"><h2 id="{s["id"]}"><span class="kicker">{esc(s["time"])}</span>{esc(s["title"])}</h2></div>'
                 f'<p class="muted">{esc(s["note"])}</p>')
        if s.get("concept"):
            body += f'<div class="concept"><div class="eyebrow">Concept statement · read verbatim</div><p>{esc(s["concept"])}</p></div>'
        body += ''.join(q_card(q) for q in s["qs"])
        toc.append((s["id"], s["title"].split(" · ")[-1]))

    # scoring grid
    rows = ''.join(f'<tr><td><b>{esc(a["id"])}</b></td><td>{esc(a["label"])}</td><td>{esc(a["verdict"])} ({a["pctV"]:.0f}% V)</td>'
                   f'<td class="blank"></td><td class="blank"></td><td class="blank"></td></tr>' for a in D["assumptions"])
    new_kas = [
        ("KA13", "Technical anonymity is achievable in small crews (voice, photo and location don't identify the reporter)"),
        ("KA14", "Reviewers have night and weekend capacity without rubber-stamping"),
        ("KA15", "An owner-held cross-employer queue is legally acceptable (controlling employer, 불법파견)"),
        ("KA16", "“Project” is the purchasing unit in each market (Korea buys per division-year)"),
    ]
    rows += ''.join(f'<tr><td><b>{k}</b></td><td>{esc(t)}</td><td>New in v2, untested</td><td class="blank"></td><td class="blank"></td><td class="blank"></td></tr>'
                    for k, t in new_kas)
    body += f"""
<h2 id="scoring"><span class="kicker">After each interview</span>Scoring grid</h2>
<p>Mark V (volunteered with a specific recent example before the concept), P (conditional, secondhand or only after probing), I (contradicted), or N/A.
Write the verbatim quote that justifies the score. KA4 is now phrased consequence first and seconds second.</p>
<div class="tbl"><table class="wide"><thead><tr><th>KA</th><th>Assumption</th><th>Synthetic result</th><th>Score</th><th>Verbatim evidence</th><th>Q-id</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<style>.blank{{min-width:80px;height:34px}} table.wide td.blank:nth-child(5){{min-width:280px}}</style>
"""
    toc.append(("scoring", "Scoring grid"))
    out = page(
        title="SAiFETY Talk Field Interview Guide",
        description="Field-ready interview guide for real stakeholders, annotating what the synthetic study suggests versus what still needs human validation.",
        eyebrow="A BuiltNOVA platform · Real-user interview guide · v2",
        h1_html="Ask the crew. <em>Then ask again.</em>",
        lede=("A 50-minute, non-leading interview guide for forepersons, crews, safety reviewers, stewards and buyers on mega industrial projects "
              "and Korean shipyards. It tests the 12 Step 20 key assumptions plus four new ones the synthetic study surfaced."),
        meta=["≈ 50–55 min", f"{sum(len(s['qs']) for s in SECTIONS)} questions", "16 key assumptions", "EN · KO · VI interpreter notes", "v2 · 27 Sept 2026"],
        toc=toc, body=body)
    with open(os.path.join(ROOT, "real_user_interview_script.html"), "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote real_user_interview_script.html", len(out))


if __name__ == "__main__":
    build()
