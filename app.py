import streamlit as st

st.set_page_config(page_title="GFI Flow Intelligence", page_icon="🛡️", layout="wide")
st.title("GFI Flow Intelligence")
st.caption("Independent Diagnostic Reports · Confidential · Non-Political")

NAV = {
    "EN": [
        st.Page("app_pages/en_overview.py", title="Overview"),
        st.Page("app_pages/en_methodology.py", title="Methodology"),
        st.Page("app_pages/en_case_studies.py", title="Case Studies"),
        st.Page("app_pages/en_founder.py", title="Founder"),
        st.Page("app_pages/en_contact.py", title="Contact"),
    ],
    "中文": [
        st.Page("app_pages/cn_overview.py", title="概覽"),
        st.Page("app_pages/cn_methodology.py", title="方法論"),
        st.Page("app_pages/cn_case_studies.py", title="案例研究"),
        st.Page("app_pages/cn_founder.py", title="創辦人"),
        st.Page("app_pages/cn_contact.py", title="聯絡"),
    ],
}

pg = st.navigation(NAV)
pg.run()
