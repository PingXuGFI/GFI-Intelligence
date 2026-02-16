import streamlit as st
import plotly.graph_objects as go

# 1. 設置
st.set_page_config(page_title="GFI Hidden Profit Leak Report", layout="wide")

# 2. 強力視覺 CSS
st.markdown("""
<style>
    .main-title { font-size: 3.5rem; font-weight: 800; color: #1e3a8a; text-align: center; margin-bottom: 0.5rem; }
    .hero-box { background: #f1f5f9; padding: 2.5rem; border-radius: 15px; text-align: center; margin-bottom: 2rem; border: 1px solid #cbd5e1; }
    .value-card { background: white; padding: 1.5rem; border-radius: 10px; border-top: 5px solid #1e3a8a; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); height: 100%; }
</style>
""", unsafe_allow_html=True)

# 3. 價值說明區 (讓老闆看懂這是幹嘛的)
st.markdown('<h1 class="main-title">GFI Hidden Profit Leak Audit™</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:1.2rem; color:#475569;'>Detect and quantify the 'Efficiency Tax' draining your company's net profit.</p>", unsafe_allow_html=True)

st.write("---")

col_v1, col_v2, col_v3 = st.columns(3)
with col_v1:
    st.markdown('<div class="value-card"><h4>🚫 Stop Rework</h4><p>Identify how much capital is wasted on doing the same task twice due to poor process design.</p></div>', unsafe_allow_html=True)
with col_v2:
    st.markdown('<div class="value-card"><h4>⚡ Accelerate Decisions</h4><p>Quantify the financial cost of administrative delays and approval bottlenecks.</p></div>', unsafe_allow_html=True)
with col_v3:
    st.markdown('<div class="value-card"><h4>📉 Reduce Churn</h4><p>Measure the link between internal friction and lost customer lifetime value.</p></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# 4. 診斷區
st.subheader("🔍 Preliminary Risk Assessment")
with st.container():
    with st.form("audit_form"):
        c1, c2 = st.columns(2)
        with c1:
            n_emp = st.number_input("Headcount (Full-Time Equivalents)", value=50)
            avg_rate = st.number_input("Avg. Fully-Loaded Hourly Rate ($)", value=85)
            rework_rate = st.slider("Estimated Rework/Revision Rate (%)", 0, 100, 20)
        with c2:
            delay_hrs = st.slider("Weekly Delay per Employee (Hours)", 0, 20, 5)
            multiplier = st.selectbox("Revenue Multiplier (Value generated per $1 of cost)", [3.0, 5.0, 8.0, 10.0])
        
        submitted = st.form_submit_button("GENERATE FINANCIAL IMPACT PREVIEW")

if submitted:
    # 這裡加入圖表，讓它看起來像「分析報告」而非「計算機」
    leak_total = n_emp * avg_rate * delay_hrs * 52 * multiplier
    
    st.markdown(f"""
    <div style="background: #fff1f2; padding: 2rem; border-radius: 12px; border: 2px solid #be123c; margin-top: 2rem;">
        <h3 style="color: #be123c; margin: 0;">AUDIT ALERT: CRITICAL LEAKAGE DETECTED</h3>
        <p style="font-size: 1.1rem; color: #475569;">Your organization is leaking approximately:</p>
        <h1 style="color: #be123c; font-size: 4.5rem; margin: 10px 0;">${leak_total:,.0f} / Year</h1>
    </div>
    """, unsafe_allow_html=True)

    # 用 Plotly 畫一個簡單的 Waterfall 圖，展示錢是怎麼沒的
    fig = go.Figure(go.Waterfall(
        name = "Profit Leak", orientation = "v",
        measure = ["relative", "relative", "total"],
        x = ["Direct Labor Loss", "Opportunity Cost", "Total Leakage"],
        textposition = "outside",
        text = [f"-{leak_total*0.3:,.0f}", f"-{leak_total*0.7:,.0f}", f"{leak_total:,.0f}"],
        y = [-leak_total*0.3, -leak_total*0.7, 0],
        connector = {"line":{"color":"rgb(63, 63, 63)"}},
    ))
    fig.update_layout(title="Breakdown of Identified Losses", showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.write("### 📄 Get the Full Audit & Action Plan")
    st.write("This preview only covers 15% of the GFI Diagnostic. The full report provides a department-by-department breakdown and 3 immediate fixes.")
    st.link_button("🔥 DOWNLOAD FULL REPORT ($299)", "https://buy.stripe.com/your_link")

# 5. 側邊欄
st.sidebar.markdown("### GFI Intelligence")
st.sidebar.write("Institutional Risk Auditing")
st.sidebar.caption("© 2026 GFI Intelligence | Boston, MA")
