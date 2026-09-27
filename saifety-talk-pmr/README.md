# SAiFETY Talk — Synthetic Primary Market Research (Sept 2026)

> Synthetic primary market research is a rapid simulation tool for stress-testing business assumptions and refining interview instruments. Because synthetic agents cannot reliably predict real-world human behavior or purchasing decisions, all findings must be validated through direct interviews with real human stakeholders.

## Deliverables

| File | What it is |
|---|---|
| [`synthetic_pmr_dashboard.md`](synthetic_pmr_dashboard.md) | Full quantitative and qualitative synthesis, formatted for NotebookLM |
| [`synthetic_pmr_dashboard.html`](synthetic_pmr_dashboard.html) | The same dashboard with visual cards, verdict badges, scoring tables and charts |
| [`real_user_interview_script.html`](real_user_interview_script.html) | Field-ready v2 interview guide; each question shows the synthetic signal next to what still needs human validation |
| [`business_plan_revisions.html`](business_plan_revisions.html) | Recommended revisions to End User Profile, Value Proposition, Beachhead TAM and Business Model, organized by Disciplined Entrepreneurship step |

## Research trail (`research/`)

- `00_pitch_deck_extract.txt`: text of the upgraded pitch deck used as the baseline
- `01_synthetic_personas.md`: 10 synthetic end users, each with 30 characteristics and a backstory (Step 1; Park Ji-hoon replaced Susan Whitfield at the human gate)
- `02_key_assumptions_and_interview_script.md`: 12 Step 20 key assumptions and the non-leading script with a split-anchor WTP design (Step 2)
- `transcripts/`: 10 simulated interview transcripts (Step 3)
- `synthesis_data.json`: machine-readable scores, WTP, objections, quotes and recommendations (Step 4)

## Rebuilding the HTML

```bash
pip install markdown
cd build && python3 build_dashboard.py && python3 build_script.py && python3 build_revisions.py
```

All three HTML files are generated from `research/synthesis_data.json` (and, for the dashboard, `synthetic_pmr_dashboard.md`), so the numbers stay in sync.
