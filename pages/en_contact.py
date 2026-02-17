import streamlit as st

st.title("Contact")
st.subheader("Request the $999 Self-Service Friction Scan")

st.divider()

FORM_URL = "https://forms.gle/96rG6e4PTAJgDkcJ9"

st.markdown("## Intake Form")
st.markdown(FORM_URL)

st.info("Delivery: **within 48 hours** after your team completes the questionnaire.")
