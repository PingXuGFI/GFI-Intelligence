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

<stripe-buy-button
  buy-button-id="buy_btn_1T1sUvRw9CVw8oC7f8G5G2UR"
  publishable-key="pk_live_51SzplSRw9CVw8oC78qxLy57eZRzWrELB0tBzLJa9FWOkxijGMyDDxrr1si3LdzdOEkoNxY4k5pXwCGAshI5iJ1ul00QnZ6DdJQ"
>
</stripe-buy-button>
""",
    unsafe_allow_html=True
)

st.divider()

# -------------------------
# Section 3: Upload Strategy
# -------------------------
st.subheader("C) 上傳問卷檔案（備援）")
st.write(
    "若你無法使用 Google Form，可先在此上傳檔案作為**臨時備援**。"
    "為了隱私與穩定交付，正式提交仍建議使用 Google Form 或 Email。"
)

uploaded = st.file_uploader(
    "上傳問卷匯出檔（CSV / XLSX / PDF），可多檔上傳。",
    type=["csv", "xlsx", "pdf"],
    accept_multiple_files=True
)

org = st.text_input("機構 / 單位（選填）")
contact_name = st.text_input("姓名（選填）")
contact_email = st.text_input("Email（選填）")
notes = st.text_area("補充說明（選填）", placeholder="背景、限制、期限、你想要回答的核心問題…")

if uploaded:
    st.success(f"本次工作階段已收到 {len(uploaded)} 份檔案。")
    st.info(
        "重要：Streamlit Cloud 不會永久保存上傳檔案（除非你另外接儲存服務）。"
        "所以請同時用 Email 提交（下方提供可直接複製的內容）。"
    )

st.divider()

# -------------------------
# Section 4: Email Template
# -------------------------
st.subheader("D) Email 提交（最可靠）")
st.write("若你要最穩的交付路徑：Email 附檔 + 貼上以下摘要。")

now = datetime.now().strftime("%Y-%m-%d %H:%M")
file_list = "\n".join([f"- {f.name} ({getattr(f, 'type', 'file')})" for f in uploaded]) if uploaded else "-（此頁未上傳檔案）"
intake_text = f"""
GFI 自助診斷收件摘要

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
st.text_area("可直接複製貼上（Email 內文）", value=textwrap.dedent(intake_text).strip(), height=260)
st.caption("建議信件標題：『GFI 999 自助診斷 — 問卷提交』")

st.divider()

# -------------------------
# Section 5: Upgrade path
# -------------------------
st.subheader("E) 升級合作（需先付押金）")
st.write(
    "升級不是免費諮詢。為避免浪費時間，升級路徑需先付押金，才進入範疇界定與工作會議。"
)

st.markdown(
    "- 押金：**4,999 美元**（升級範疇界定前必須）\n"
    "- 產出：確認範疇、時間線、以及依複雜度決定的報價"
)

st.warning("若你要走升級路徑，請在『補充說明』或 Email 明確寫：『我要升級（押金後談範疇）』。")
