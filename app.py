

import streamlit as st

# =========================
# STRIPE LINKS (SET HERE)
# =========================
QUICK_PAY_URL = "https://buy.stripe.com/8x25kFbp0dM4gQl0fB3VC00"
DEEP_PAY_URL  = "https://buy.stripe.com/7sYcN764GdM4arX0fB3VC01"

# =========================
# OPTIONAL CONTACT FORM
# =========================
CONTACT_FORM_URL = ""  # Google Form link, or leave blank

# =========================
# ASSETS (UPLOAD TO REPO ROOT)
# =========================
BANNER_IMG = "banner.png"     # upload your new banner as banner.png (same folder as app.py)
LOGO_IMG   = "GFILOGO.png"    # upload your logo as GFILOGO.png (same folder as app.py)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="GFI Flow Intelligence — AI Impact Audit",
    page_icon="🧪",
    layout="wide"
)

# =========================
# SIMPLE CSS (CLEANER, LESS “BUSY”)
# =========================
st.markdown("""
<style>
.block-container {padding-top: 1.2rem; padding-bottom: 2.2rem; max-width: 1200px;}
.small-note {opacity: 0.75; font-size: 0.92rem;}
.kicker {letter-spacing: 0.08em; text-transform: uppercase; font-size: 0.85rem; opacity: 0.75;}
.hero {font-size: 2.2rem; font-weight: 850; line-height: 1.05; margin: 0.2rem 0 0.4rem 0;}
.subhero {font-size: 1.05rem; opacity: 0.85; max-width: 70ch;}
.card {
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 18px;
    padding: 1.0rem 1.1rem;
    background: rgba(255,255,255,0.03);
}
.hr {height: 1px; background: rgba(255,255,255,0.12); margin: 1.0rem 0;}
</style>
""", unsafe_allow_html=True)

# =========================
# TOP BRAND (CLEAN) + BANNER
# =========================
top1, top2 = st.columns([1, 6], gap="medium")
with top1:
    try:
        st.image(LOGO_IMG, width=90)
    except:
        pass
with top2:
    st.markdown("<div style='font-size:1.55rem; font-weight:800; line-height:1.1;'>GFI Flow Intelligence</div>", unsafe_allow_html=True)
    st.markdown("<div style='opacity:0.75; font-size:0.95rem;'>Structural Audit of AI & Automation Impact</div>", unsafe_allow_html=True)

st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

# Banner as a clean visual only (no extra text around it)
try:
    st.image(BANNER_IMG, use_container_width=600)
except:
    pass

st.markdown("<div style='height:18px;'></div>", unsafe_allow_html=True)

# =========================
# HERO (KEEP TEXT — BUT SHORT)
# =========================
left, right = st.columns([2, 1], gap="large")

with left:
    st.markdown('<div class="kicker">AI Implementation Impact Audit</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero">We Audit Your AI Investment.</div>', unsafe_allow_html=True)
    st.markdown("""
<div class="subhero">
<b>Not by hype.</b> By measurable performance shift.
</div>
""", unsafe_allow_html=True)

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

    st.markdown("""
Most organizations deploy AI.  
Very few can prove it **reduced friction**.

We measure:

- **Speed gained**
- **Friction created**
- **Net operational impact**
""")

    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

    st.markdown("### Quick reality check")
    st.markdown("""
- Did processing time decrease?
- Did manual review increase?
- Did error correction workload rise?
- Did hidden workflow steps multiply?

If you can’t answer cleanly — you don’t know your AI ROI.
""")

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### What you get")
    st.markdown("""
- Baseline vs Post-Implementation comparison  
- Net Impact Index (ANI) = ΔFlow − ΔFriction  
- Risk classification (Green / Yellow / Red)  
- Executive-ready PDF report  
""")
    st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
    st.markdown("#### Typical outcomes")
    st.markdown("""
- Throughput improved, but hidden rework increased  
- Cycle time dropped, but approval layers grew  
- Cost decreased, but compliance exposure rose  
""")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# OFFERING / PRICING
# =========================
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
st.markdown("## Engagement Options")

c1, c2 = st.columns(2, gap="large")

with c1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🔎 AI Impact Quick Diagnostic — **$999**")
    st.markdown("""
**48-hour performance review** using your operational baseline + post-AI metrics.

**Deliverables**
- ANI score (ΔFlow − ΔFriction)  
- Risk classification (Green / Yellow / Red)  
- 6–8 page PDF report
""")
    st.markdown('<div class="small-note">Best for: teams needing an immediate leadership answer.</div>', unsafe_allow_html=True)
    st.link_button("Start Diagnostic — $999", QUICK_PAY_URL)
    st.markdown('</div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🔬 AI Friction Deep Audit — **$4,999**")
    st.markdown("""
**Workflow mapping** to locate where AI created or shifted friction.

**Deliverables**
- Process map + bottleneck analysis  
- Latency breakdown & shadow labor detection  
- 15–25 page Governance Impact Report
""")
    st.markdown('<div class="small-note">Best for: organizations seeing mixed results after AI deployment.</div>', unsafe_allow_html=True)
    st.link_button("Request Deep Audit — $4,999", DEEP_PAY_URL)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# TRUST / METHOD
# =========================
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)

t1, t2, t3 = st.columns([1.2, 1.2, 1.6], gap="large")

with t1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Method (simple)")
    st.markdown("""
**ANI = ΔFlow − ΔFriction**
- ΔFlow: speed / throughput  
- ΔFriction: rework / manual review / added steps  
""")
    st.markdown('</div>', unsafe_allow_html=True)

with t2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### What we don’t do")
    st.markdown("""
- No hype decks  
- No vague transformation claims  
- No vendor marketing language  
""")
    st.markdown('</div>', unsafe_allow_html=True)

with t3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Who this is for")
    st.markdown("""
Public agencies modernizing services  
Healthcare / education ops teams  
Compliance-heavy organizations  
Teams under pressure to justify AI spend  
""")
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FOOTER CTA
# =========================
st.markdown('<div class="hr"></div>', unsafe_allow_html=True)
f1, f2 = st.columns([2, 1], gap="large")

with f1:
    st.markdown("### Ready to measure real AI ROI?")
    st.markdown("Stop guessing. Get a measurable performance shift summary — fast.")

with f2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Contact / Intake")
    st.markdown("""
After payment, you will be redirected to the intake form to submit your baseline + post-AI metrics.  
We’ll confirm scope and delivery timeline by email.
""")
    if CONTACT_FORM_URL:
        st.link_button("Contact / General Inquiry", CONTACT_FORM_URL)
    st.markdown('</div>', unsafe_allow_html=True)
