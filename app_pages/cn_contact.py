import streamlit as st
import textwrap
from datetime import datetime

st.title("聯絡 / 提交問卷")
st.caption("提交問卷結果以取得 999 美元自助診斷報告，或申請升級方案（升級需先付押金）。")

# -------------------------
# LINKS (edit here)
# -------------------------
GOOGLE_FORM_URL = "https://forms.gle/96rG6e4PTAJgDkcJ9"
EMAIL = "pingshyu0@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/ping-shyu/"

# -------------------------
# Top Contact Block
# -------------------------
c1, c2 = st.columns([1.2, 1])
with c1:
    st.subheader("直接聯絡")
    st.markdown(f"- Email：**{EMAIL}**")
    st.markdown(f"- LinkedIn：**{LINKEDIN}**")

with c2:
    st.subheader("最快路徑")
    st.markdown(
        "- **自助（999 美元）**：付款 → 提交問卷 → **48 小時**交付報告\n"
        "- **升級**：先付 **4,999 美元押金** → 範疇界定 → 客製合作"
    )

st.divider()

# -------------------------
# Section 1: Submit via Google Form
# -------------------------
st.subheader("A) 用 Google Form 提交問卷（主通道）")
st.write("此表單是標準化收件入口。優先使用這個方式提交。")

st.link_button("開啟 Google Form — 提交問卷", GOOGLE_FORM_URL)

st.caption("若你的機構限制外部表單，請使用下方的上傳 + Email 方式。")

st.divider()

# -------------------------
# Section 2: Pay $999 via Stripe Buy Button
# -------------------------
st.subheader("B) 付款 999（Stripe）")
st.write("付款後，請用上方 Google Form 提交問卷（或用下方上傳 + Email 備援）。")

st.markdown(
    """
<script async src="https://js.stripe.com/v3/buy-button.js"></script>

<str
