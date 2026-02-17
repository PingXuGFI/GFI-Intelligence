import streamlit as st
import textwrap
from datetime import datetime

st.title("Contact / Submit Survey")
st.caption("Submit survey results for the $999 self-serve diagnostic report (48-hour turnaround).")

GOOGLE_FORM_URL = "https://forms.gle/96rG6e4PTAJgDkcJ9"
EMAIL = "pingshyu0@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/ping-shyu/"

c1, c2 = st.columns([1.2, 1])
with c1:
    st.subheader("Direct Contact")
    st.markdown(f"- Email: **{EMAIL}**")
    st.markdown(f"- LinkedIn: **{LINKEDIN}**")
with c2:
    st.subheader("Engagement")
    st.markdown(
        "- **$999 Self-Serve:** pay → submit survey → report in **48 hours**\n"
        "- **Upgrade:** deposit **$4,999** → scoping + working sessions"
    )

st.divider()

st.subheader("A) Submit Survey (Google Form)")
st.link_button("Open Google Form — Submit Survey", GOOGLE_FORM_URL)

st.divider()

st.subheader("B) Pay $999 (Stripe)")
st.markdown(
    """
<script async src="https://js.stripe.com/v3/buy-button.js"></script>
<stripe-buy-button
  buy-button-id="buy_btn_1T1sUvRw9CVw8oC7f8G5G2UR"
  publishable-key="pk_live_51SzplSRw9CVw8oC78qxLy57eZRzWrELB0tBzLJa9FWOkxijGMyDDxrr1si3LdzdOEkoNxY4k5pXwCGAshI5iJ1ul00QnZ6DdJQ">
</stripe-buy-button>
""",
    unsafe_allow_html=True
)

st.divider()

st.subheader("C) Upload (Fallback)")
uploaded = st.file_uploader(
    "Upload survey exports (CSV / XLSX / PDF). Multiple files allowed.",
    type=["csv", "xlsx", "pdf"],
    accept_multiple_files=True
)

org = st.text_input("Organization / Team (optional)")
contact_name = st.text_input("Your name (optional)")
contact_email = st.text_input("Your email (optional)")
notes = st.text_area("Notes (optional)")

st.divider()

st.subheader("D) Email Submission (Most Reliable)")
now = datetime.now().strftime("%Y-%m-%d %H:%M")
file_list = "\n".join([f"- {f.name}" for f in uploaded]) if uploaded else "- (no files uploaded here)"
intake_text = f"""
GFI $999 Self-Serve — Survey Submission

Timestamp: {now}
Organization/Team: {org or "(not provided)"}
Contact Name: {contact_name or "(not provided)"}
Contact Email: {contact_email or "(not provided)"}

Files:
{file_list}

Notes:
{notes or "(none)"}

Request:
- $999 self-serve diagnostic report (48-hour turnaround after survey receipt)
"""

st.markdown(f"Send to: **{EMAIL}**")
st.text_area("Copy/Paste Intake Summary (email body)", value=textwrap.dedent(intake_text).strip(), height=220)
