import streamlit as st

st.set_page_config(page_title="Enterprise Structural Risk Audit", layout="wide")

st.title("Enterprise Structural Risk Audit")
st.caption("Post-Automation Independent Review")

st.markdown("""
### Automation improves speed. We measure what it changes structurally.

When organizations deploy AI, workflow automation, or operational restructuring, performance metrics often improve.

What is rarely measured is structural load:
- Has decision density increased?
- Have review layers expanded?
- Has exception handling intensified?
- Has friction shifted downstream?

We conduct independent structural audits to assess how automation has altered institutional load.
""")

st.divider()

st.subheader("What We Evaluate")
st.markdown("""
- Decision latency shifts  
- Escalation and exception density  
- Review layer expansion  
- Rework amplification  
- Customer/user friction redistribution  
- Risk concentration nodes  
""")

st.subheader("What You Receive")
st.markdown("""
- Pre- and post-deployment structural comparison  
- Load redistribution analysis  
- Risk concentration mapping  
- Executive-level impact summary  
- Targeted structural adjustment recommendations  
""")

st.subheader("When This Is Relevant")
st.markdown("""
- After major AI deployment  
- After workflow automation  
- After digital transformation initiatives  
- When performance improved but complexity increased  
- When escalation, complaints, or internal pressure rise unexpectedly  
""")

st.subheader("Our Position")
st.markdown("""
We do not implement systems.  
We do not sell software.  
We do not alter your architecture.  

**We provide independent structural assessment.**
""")

st.divider()

st.subheader("Request a Confidential Briefing")

# Replace with your real form or scheduling link
CTA_URL = "https://forms.gle/REPLACE_WITH_YOUR_FORM"
st.link_button("Request a Confidential Briefing", CTA_URL)

st.caption("Prefer email? contact: REPLACE_WITH_YOUR_EMAIL")
