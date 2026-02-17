import streamlit as st
import textwrap
from datetime import datetime

st.title("聯絡 / 提交問卷")
st.caption("提交問卷以取得 999 美元自助診斷報告（收到問卷後 48 小時交付）。")

GOOGLE_FORM_URL = "https://forms.gle/96rG6e4PTAJgDkcJ9"
EMAIL = "pingshyu0@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/ping-shyu/"

c1, c2 = st.columns([1.2, 1])
with c1:
    st.subheader("直接聯絡")
    st.markdown(f"- Email：**{EMAIL}**")
    st.markdown(f"- LinkedIn：**{LINKEDIN}**")
with c2:
    st.subheader("合作模式")
    st.markdown(
        "- **999 自助：**付款 → 提交問卷 → **48 小時**交付\n"
        "- **升級：**先付 **4,999 押金** → 範疇界定 + 工作會議"
    )

st.divider()

st.subheader("A) 用 Google Form 提交（主通道）")
st.link_button("開啟 Google Form — 提交問卷", GOOGLE_FORM_URL)

st.divider()

st.subheader("B) 付款 999（Stripe）")
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

st.subheader("C) 上傳檔案（備援）")
uploaded = st.file_uploader(
    "上傳問卷匯出檔（CSV / XLSX / PDF），可多檔。",
    type=["csv", "xlsx", "pdf"],
    accept_multiple_files=True
)

org = st.text_input("機構 / 單位（選填）")
contact_name = st.text_input("姓名（選填）")
contact_email = st.text_input("Email（選填）")
notes = st.text_area("補充說明（選填）")

st.divider()

st.subheader("D) Email 提交（最可靠）")
now = datetime.now().strftime("%Y-%m-%d %H:%M")
file_list = "\n".join([f"- {f.name}" for f in uploaded]) if uploaded else "-（此頁未上傳檔案）"
intake_text = f"""
GFI 999 自助診斷 — 問卷提交

時間：{now}
機構/單位：{org or "（未填）"}
姓名：{contact_name or "（未填）"}
Email：{contact_email or "（未填）"}

檔案：
{file_list}

補充說明：
{notes or "（無）"}

需求：
- 999 美元自助診斷報告（收到問卷後 48 小時交付）
"""

st.markdown(f"收件信箱：**{EMAIL}**")
st.text_area("可直接複製貼上（Email 內文）", value=textwrap.dedent(intake_text).strip(), height=220)

