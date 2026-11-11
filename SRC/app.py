import html

import streamlit as st

from search import search, search_bert, df
from dupe_detector import get_dupes

st.set_page_config(page_title="ScentSync", page_icon="🌸", layout="centered")


def md(s):
    st.markdown("\n".join(l.strip() for l in s.splitlines() if l.strip()), unsafe_allow_html=True)


md(
    """
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #faf7f2; --card: #ffffff; --ink: #2b2420; --muted: #8a7f76;
  --line: #ece4d9; --accent: #b0876b; --accent-soft: #f3e9df; --dupe: #6f8a72; --dupe-soft: #e8efe6;
  --field: #ffffff; --placeholder: #b9aea4; --pill-ink: #7a5a44; --dupe-ink: #4d6450;
}
.stApp { background: var(--bg); }
html, body, [class*="css"], .stApp, p, label, input { font-family: 'Inter', sans-serif; color: var(--ink); }
#MainMenu, footer, header [data-testid="stToolbar"] { visibility: hidden; }
.block-container { padding-top: 2rem; max-width: 760px; }
header[data-testid="stHeader"] { background: transparent; }
div[data-testid="stTextInput"] > div, div[data-testid="stTextInput"] div[data-baseweb="input"],
div[data-testid="stTextInput"] div[data-baseweb="base-input"] { background: var(--field) !important; border-radius: 12px; border: none; }
div[data-testid="stTextInput"] input { color: var(--ink) !important; -webkit-text-fill-color: var(--ink); caret-color: var(--ink) !important; }
div[data-testid="stTextInput"] input::placeholder { color: var(--placeholder); -webkit-text-fill-color: var(--placeholder); }
div[data-baseweb="select"] > div, div[data-baseweb="select"] * { color: var(--ink) !important; }
div[data-baseweb="select"] svg { fill: var(--muted); }
ul[role="listbox"], div[data-baseweb="popover"] li { background: var(--field) !important; color: var(--ink) !important; }
div[data-testid="stWidgetLabel"] p { color: var(--muted) !important; font-size: .8rem; text-transform: uppercase; letter-spacing: .08em; }

.hero { text-align: center; margin-bottom: 2rem; }
.hero .eyebrow { letter-spacing: .28em; font-size: .72rem; text-transform: uppercase; color: var(--accent); font-weight: 600; }
.hero h1 { font-family: 'Cormorant Garamond', serif; font-size: 4rem; font-weight: 600; margin: .2rem 0 .2rem; color: var(--ink); line-height: 1; }
.hero p { color: var(--muted); font-size: 1.02rem; margin: 0; }

div[data-testid="stTextInput"] input {
  border-radius: 12px; border: 1px solid var(--line); background: var(--field); padding: .85rem 1rem; font-size: 1rem;
}
div[data-testid="stTextInput"] input:focus { border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-soft); }
div[data-baseweb="select"] > div { border-radius: 12px; border: 1px solid var(--line); background: var(--field) !important; }
div[data-testid="stCheckbox"] p, div[data-testid="stToggle"] p { color: var(--muted) !important; font-size: .8rem; }
label[data-baseweb="checkbox"] > div:first-child { background: var(--line) !important; border: 1px solid var(--muted); }
label[data-baseweb="checkbox"] > div:first-child > div { background: var(--muted) !important; box-shadow: none !important; }
label[data-baseweb="checkbox"]:has(input:checked) > div:first-child { background: var(--accent) !important; border-color: var(--accent); }
label[data-baseweb="checkbox"]:has(input:checked) > div:first-child > div { background: var(--bg) !important; }
.stApp, .card, div[data-baseweb="select"] > div, div[data-testid="stTextInput"] input { transition: background-color .25s, color .25s, border-color .25s; }

.section { display: flex; align-items: baseline; justify-content: space-between; margin: 2.4rem 0 .9rem; border-bottom: 1px solid var(--line); padding-bottom: .5rem; }
.section .h2 { font-family: 'Cormorant Garamond', serif !important; font-size: 1.9rem !important; font-weight: 600 !important; margin: 0; padding: 0 !important; color: var(--ink) !important; }
.section span { color: var(--muted); font-size: .82rem; }

.card { background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 1.1rem 1.3rem; margin-bottom: .75rem;
        display: grid; grid-template-columns: 2.4rem 1fr auto; gap: 1rem; align-items: center; box-shadow: 0 1px 2px rgba(43,36,32,.04); }
.rank { font-family: 'Cormorant Garamond', serif; font-size: 1.7rem; color: var(--accent); text-align: center; }
.name { font-weight: 600; font-size: 1.05rem; }
.brand { color: var(--muted); font-size: .85rem; text-transform: uppercase; letter-spacing: .08em; margin-top: .1rem; }
.pills { margin-top: .55rem; display: flex; flex-wrap: wrap; gap: .35rem; }
.pill { background: var(--accent-soft); color: var(--pill-ink); border-radius: 999px; padding: .15rem .6rem; font-size: .74rem; }
.notes { color: var(--muted); font-size: .8rem; margin-top: .5rem; line-height: 1.45; }
.notes b { color: var(--ink); font-weight: 500; }
.score { text-align: right; min-width: 92px; }
.score .pct { font-weight: 600; font-size: 1.1rem; }
.score .lbl { color: var(--muted); font-size: .7rem; text-transform: uppercase; letter-spacing: .08em; }
.bar { height: 4px; background: var(--line); border-radius: 4px; margin-top: .35rem; overflow: hidden; }
.bar > div { height: 100%; background: var(--accent); border-radius: 4px; }
.card.dupe .rank, .card.dupe .score .pct { color: var(--dupe); }
.card.dupe .pill { background: var(--dupe-soft); color: var(--dupe-ink); }
.card.dupe .bar > div { background: var(--dupe); }
.empty { color: var(--muted); text-align: center; padding: 1.5rem; border: 1px dashed var(--line); border-radius: 16px; }
.foot { text-align: center; color: var(--muted); font-size: .75rem; margin-top: 3rem; }
@media (max-width: 600px) {
  .hero h1 { font-size: 3rem; }
  .card { grid-template-columns: 1.8rem 1fr; }
  .score { grid-column: 2; text-align: left; }
}
</style>
"""
)


def pretty(slug):
    return str(slug).replace("-", " ").title()


def card(row, i, idx, dupe=False):
    info = df.loc[idx] if idx in df.index else row
    accords = [info.get(c) for c in ("mainaccord1", "mainaccord2", "mainaccord3")]
    pills = "".join(f'<span class="pill">{html.escape(str(a))}</span>' for a in accords if isinstance(a, str) and a)
    notes = []
    for label, col in (("Top", "Top"), ("Heart", "Middle"), ("Base", "Base")):
        v = info.get(col)
        if isinstance(v, str) and v and v != "unknown":
            notes.append(f"<b>{label}</b> {html.escape(v)}")
    pct = max(0.0, min(1.0, float(row["similarity"])))
    return f"""
<div class="card{' dupe' if dupe else ''}">
  <div class="rank">{i}</div>
  <div>
    <div class="name">{html.escape(pretty(row["Perfume"]))}</div>
    <div class="brand">{html.escape(pretty(row["Brand"]))}</div>
    <div class="pills">{pills}</div>
    <div class="notes">{' · '.join(notes)}</div>
  </div>
  <div class="score">
    <div class="pct">{pct*100:.0f}%</div>
    <div class="lbl">match</div>
    <div class="bar"><div style="width:{pct*100:.0f}%"></div></div>
  </div>
</div>"""


def render(results, dupe=False):
    if results is None or len(results) == 0:
        st.markdown('<div class="empty">No matches found for this description.</div>', unsafe_allow_html=True)
        return
    md("".join(card(r, i, idx, dupe) for i, (idx, r) in enumerate(results.iterrows(), 1)))


_, theme_col = st.columns([5, 1])
with theme_col:
    dark = st.toggle("🌙 Dark", key="dark_mode")

if dark:
    md(
        """
<style>
:root {
  --bg: #15120f; --card: #1f1b17; --ink: #f1ebe4; --muted: #a39689;
  --line: #342d27; --accent: #d1a687; --accent-soft: #3a2e25; --dupe: #93b096; --dupe-soft: #26302a;
  --field: #1f1b17; --placeholder: #6f655c; --pill-ink: #e6c9b2; --dupe-ink: #bcd3bd;
}
.card { box-shadow: none; }
</style>
"""
    )

md(
    """
<div class="hero">
  <div class="eyebrow">AI Fragrance Discovery</div>
  <h1>ScentSync</h1>
  <p>AI-Powered Fragrance Recommendation Engine</p>
</div>
"""
)

col1, col2 = st.columns([3, 1])
with col1:
    query = st.text_input(
        "Describe a fragrance you want:",
        placeholder="e.g. warm cozy date night fragrance",
    )
with col2:
    model_choice = st.selectbox("Choose Model", ["TF-IDF", "BERT"])

if query:

    # Select model
    if model_choice == "TF-IDF":
        results = search(query)
    else:
        results = search_bert(query)

    st.markdown(
        f'<div class="section"><div class="h2">Top Recommendations</div><span>via {model_choice}</span></div>',
        unsafe_allow_html=True,
    )
    render(results)

    # Dupes
    dupes = get_dupes(query)

    st.markdown(
        '<div class="section"><div class="h2">Affordable Alternatives</div><span>clone-house dupes</span></div>',
        unsafe_allow_html=True,
    )
    render(dupes, dupe=True)

st.markdown('<div class="foot">ScentSync · 24,000+ fragrances from Fragrantica</div>', unsafe_allow_html=True)
