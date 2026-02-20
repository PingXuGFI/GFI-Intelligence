
import streamlit as st
from pathlib import Path

# ============================================================
# Page config
# ============================================================
st.set_page_config(
    page_title="GFI Flow Intelligence | 中文 / EN",
    page_icon="🔷",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# Config
# ============================================================
LOGO_PATHS = ["GFILOGO.png", "assets/GFILOGO.png", "images/GFILOGO.png"]
CN_SITE = "https://gfi-intel-cn.streamlit.app/"
EN_SITE = "https://gfi-intelligence.streamlit.app/"
CN_FORM = "https://forms.gle/KmFdjdu97bC43CYL6"  # 你给的中文快筛
CONTACT_EMAIL = "pingshyu@gmail.com"

# Stripe (optional - keep placeholders or paste yours)
STRIPE_999 = "https://buy.stripe.com/8x25kFbp0dM4gQl0fB3VC00"
STRIPE_4999 = "https://buy.stripe.com/7sYcN764GdM4arX0fB3VC01"


# ============================================================
# Helpers
# ============================================================
def load_logo():
    for p in LOGO_PATHS:
        if Path(p).exists():
            return p
    return None


def pill(label: str):
    st.markdown(
        f"""
        <span style="
            display:inline-block;
            padding:6px 10px;
            border-radius:999px;
            border:1px solid rgba(255,255,255,.16);
            background: rgba(255,255,255,.06);
            font-size:12px;
            letter-spacing:.2px;
            margin-right:8px;
        ">{label}</span>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# CSS (consulting-grade, minimal)
# ============================================================
st.markdown(
    """
<style>
/* --- Base --- */
.block-container { padding-top: 1.2rem; padding-bottom: 2.2rem; max-width: 1200px; }
h1,h2,h3 { letter-spacing: -0.4px; }
p { line-height: 1.6; }

/* --- Hero Card --- */
.hero {
    border: 1px solid rgba(255,255,255,.12);
    background: linear-gradient(135deg, rgba(0,85,255,.16), rgba(0,255,215,.08));
    border-radius: 18px;
    padding: 22px 22px;
}
.hero-title {
    font-size: 34px;
    font-weight: 800;
    margin: 0 0 6px 0;
}
.hero-subtitle {
    font-size: 16px;
    opacity: .92;
    margin: 0 0 12px 0;
}
.hero-kicker {
    font-size: 13px;
    opacity: .85;
    margin: 0;
}
.hr {
    height: 1px;
    background: rgba(255,255,255,.10);
    margin: 18px 0;
}
.card {
    border: 1px solid rgba(255,255,255,.12);
    background: rgba(255,255,255,.04);
    border-radius: 16px;
    padding: 16px 16px;
}
.small { font-size: 13px; opacity: .9; }
.muted { opacity: .85; }
.badge {
    display:inline-block;
    padding: 4px 10px;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,.14);
    background: rgba(255,255,255,.05);
    font-size: 12px;
    margin-right: 8px;
}
.list ul { margin: 0.2rem 0 0 1.2rem; }
.cta-row a { text-decoration: none; }
.footer {
    opacity: .75;
    font-size: 12px;
    margin-top: 18px;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# Header (logo + brand)
# ============================================================
logo = load_logo()

top_l, top_r = st.columns([1.2, 1])
with top_l:
    if logo:
        st.image(logo, width=84)
    st.markdown("## GFI Flow Intelligence")

with top_r:
    # Language switch (sidebar-like control but stays top)
    lang = st.radio("Language / 语言", ["中文", "EN"], horizontal=True, label_visibility="collapsed")

st.markdown("---")

# ============================================================
# Content dictionaries (CN + EN)
# ============================================================
CN = {
    "hero_title": "用数学量化执行能力",
    "hero_subtitle": "把“流程摩擦”从不可见成本，变成可计算、可对比、可优化的结构指标。",
    "hero_kicker": "GFI 是执行层的量化引擎：不是主观评价、不是泛泛建议，而是可落地的诊断框架。",
    "what_is": "什么是 GFI？",
    "what_is_body": """
GFI（Governance Flow Index）是一套 **执行效能量化引擎**。

它用可观察的结构变量，计算组织在执行层面的：

- 摩擦强度（Friction Load）
- 延迟累积（Latency / Waiting）
- 结构冗余风险（Redundancy / Loops）
- 隐性成本蒸发（Invisible Capacity Loss）
""",
    "why": "为什么这很重要？",
    "why_body": """
在组织规模扩大后，**结构复杂度会上升**，审批、协调、等待会累积成“执行税”。

没有量化工具，管理层只能依赖感觉。  
感觉无法优化结构。数学可以。
""",
    "two_stage": "两种应用场景",
    "before": "转型前：结构诊断",
    "before_list": [
        "识别瓶颈与审批堆叠点",
        "量化执行阻力与等待成本",
        "确定优先优化路径（先拆哪里）",
    ],
    "after": "转型后：效果验证",
    "after_list": [
        "验证改革是否真正减少摩擦",
        "避免“形式数字化、实质不变”",
        "建立可持续执行基线（Benchmark）",
    ],
    "big4": "Big 4 可销售模块（产品化包装）",
    "big4_body": """
下面四个模块，直接对应咨询交付结构：**可打包、可复用、可扩张**。
""",
    "modules": [
        ("Module A | Executive Snapshot（快筛）", "5–10 分钟获取“结构摩擦信号”，用于线索转化与优先级判断。"),
        ("Module B | Workflow Friction Map（流程摩擦图谱）", "把审批、等待、返工、跨部门传递映射成可视化结构图与瓶颈清单。"),
        ("Module C | Quantified Impact & Risk（量化影响与风险）", "把摩擦转化为可沟通的：延迟成本、产能损耗、合规风险、失败概率。"),
        ("Module D | Intervention Playbook（干预手册）", "低成本、可执行的结构改造建议：减少层级、缩短路径、清除循环。"),
    ],
    "cta_title": "立即行动",
    "cta_body": "先用快筛建立信号，再决定是否进入诊断合作。",
    "btn_scan": "开始中文快筛（Google Form）",
    "btn_cn_site": "打开中文版主页",
    "btn_en_site": "打开英文版主页",
    "partnership": "机构合作入口（政府 / 国企 / 大型机构 / 咨询团队）",
    "partnership_body": """
如果你代表机构，想把 GFI 用作“执行诊断 / 改革验证 / 转型评估”的标准工具：  
请直接通过以下入口联系（支持 NDA / 保密范围 / 定制指标口径）。
""",
    "contact": f"联系邮箱：{CONTACT_EMAIL}",
    "offer": "合作形式（示例）",
    "offer_list": [
        "机构试点（Pilot）：选 1–2 条关键服务/流程，快速建立基线与瓶颈清单",
        "诊断合作（Engagement）：流程图谱 + 量化影响 + 风险分级 + 干预手册",
        "授权与培训（License/Enablement）：把 GFI 变成你们内部标准方法（可复制交付）",
    ],
    "pricing": "标准产品入口（可选）",
    "disclaimer": "免责声明：本工具用于结构诊断与执行改进，不构成法律/财务建议。",
}

EN = {
    "hero_title": "Quantify Execution. Reduce Structural Friction.",
    "hero_subtitle": "Turn invisible process drag into measurable indicators you can benchmark, compare, and improve.",
    "hero_kicker": "GFI is an execution-layer diagnostic engine — not opinions, not generic advice, but a structured measurement framework.",
    "what_is": "What is GFI?",
    "what_is_body": """
The Governance Flow Index (GFI) is a **quantitative execution diagnostic engine**.

Using observable structural signals, it measures:

- Friction load
- Latency accumulation (waiting / handoffs)
- Redundancy risk (loops / rework)
- Invisible capacity loss
""",
    "why": "Why this matters",
    "why_body": """
As organizations scale, complexity compounds — approvals, handoffs, and waiting become a hidden execution tax.

Without measurement, leaders rely on intuition.  
Intuition doesn’t optimize structures. Math does.
""",
    "two_stage": "Two-phase applicability",
    "before": "Pre-transformation: Structural Diagnosis",
    "before_list": [
        "Identify bottlenecks and approval stacking",
        "Quantify execution drag and waiting cost",
        "Prioritize interventions (where to remove friction first)",
    ],
    "after": "Post-transformation: Outcome Verification",
    "after_list": [
        "Verify whether friction actually decreased",
        "Prevent ‘digitalization without real change’",
        "Establish an execution baseline benchmark",
    ],
    "big4": "Big 4-ready Product Modules",
    "big4_body": "Four modular deliverables aligned with consulting packaging — reusable, scalable, and sellable.",
    "modules": [
        ("Module A | Executive Snapshot", "A fast signal scan for pipeline qualification and prioritization."),
        ("Module B | Workflow Friction Map", "A structural map of approvals, waits, loops, and cross-team handoffs."),
        ("Module C | Quantified Impact & Risk", "Translate friction into cost, capacity loss, compliance risk, and failure probability."),
        ("Module D | Intervention Playbook", "Low-cost structural fixes: reduce layers, shorten paths, remove loops."),
    ],
    "cta_title": "Start Here",
    "cta_body": "Use the snapshot to establish signal first — then decide whether to upgrade into a full diagnostic engagement.",
    "btn_scan": "Run the Chinese Snapshot (Google Form)",
    "btn_cn_site": "Open CN Site",
    "btn_en_site": "Open EN Site",
    "partnership": "Institutional Partnership Intake",
    "partnership_body": """
If you represent a public agency, SOE, enterprise, or consulting team and want GFI as a standard tool for
execution diagnostics / reform verification / transformation audit — reach out below (NDA-supported).
""",
    "contact": f"Email: {CONTACT_EMAIL}",
    "offer": "Engagement Options (examples)",
    "offer_list": [
        "Pilot: 1–2 critical workflows to establish baseline and top bottlenecks",
        "Engagement: mapping + quantified impact + risk tiering + playbook",
        "License/Enablement: make GFI an internal standard methodology",
    ],
    "pricing": "Product Links (optional)",
    "disclaimer": "Disclaimer: Diagnostic and execution-improvement purposes only. Not legal/financial advice.",
}

T = CN if lang == "中文" else EN

# ============================================================
# HERO
# ============================================================
hero_left, hero_right = st.columns([2.1, 1])

with hero_left:
    st.markdown(
        f"""
<div class="hero">
  <div class="hero-title">{T["hero_title"]}</div>
  <div class="hero-subtitle">{T["hero_subtitle"]}</div>
  <div class="hero-kicker">{T["hero_kicker"]}</div>
  <div class="hr"></div>
  <span class="badge">GFI</span>
  <span class="badge">Execution Measurement</span>
  <span class="badge">Friction → Cost</span>
  <span class="badge">Benchmark</span>
</div>
""",
        unsafe_allow_html=True,
    )

with hero_right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"### {T['cta_title']}")
    st.write(T["cta_body"])
    st.markdown('<div class="cta-row">', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.link_button(T["btn_scan"], CN_FORM, use_container_width=True)
    with c2:
        st.link_button(T["btn_cn_site"], CN_SITE, use_container_width=True)

    st.link_button(T["btn_en_site"], EN_SITE, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("")

# ============================================================
# Main blocks
# ============================================================
left, right = st.columns([1.2, 1])

with left:
    st.markdown(f"### {T['what_is']}")
    st.markdown(f"<div class='card'>{T['what_is_body']}</div>", unsafe_allow_html=True)

    st.markdown("")
    st.markdown(f"### {T['why']}")
    st.markdown(f"<div class='card'>{T['why_body']}</div>", unsafe_allow_html=True)

with right:
    st.markdown(f"### {T['two_stage']}")
    st.markdown("<div class='card list'>", unsafe_allow_html=True)
    st.markdown(f"**{T['before']}**")
    st.markdown("- " + "\n- ".join(T["before_list"]))
    st.markdown("")
    st.markdown(f"**{T['after']}**")
    st.markdown("- " + "\n- ".join(T["after_list"]))
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("")

# ============================================================
# Big 4 modules
# ============================================================
st.markdown(f"### {T['big4']}")
st.markdown(f"<div class='card'><div class='small muted'>{T['big4_body']}</div></div>", unsafe_allow_html=True)

m1, m2 = st.columns(2)
for i, (title, desc) in enumerate(T["modules"]):
    col = m1 if i % 2 == 0 else m2
    with col:
        st.markdown(
            f"""
<div class="card">
  <div style="font-weight:700; font-size:15px; margin-bottom:6px;">{title}</div>
  <div class="small">{desc}</div>
</div>
""",
            unsafe_allow_html=True,
        )

st.markdown("")

# ============================================================
# Institutional partnership intake
# ============================================================
st.markdown(f"### {T['partnership']}")
st.markdown(f"<div class='card'>{T['partnership_body']}</div>", unsafe_allow_html=True)

p1, p2 = st.columns([1.4, 1])
with p1:
    st.markdown("<div class='card list'>", unsafe_allow_html=True)
    st.markdown(f"**{T['offer']}**")
    st.markdown("- " + "\n- ".join(T["offer_list"]))
    st.markdown("</div>", unsafe_allow_html=True)

with p2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"**{T['contact']}**")
    st.write("")
    st.markdown(f"**{T['pricing']}**")
    st.link_button("USD $999", STRIPE_999, use_container_width=True)
    st.link_button("USD $4,999", STRIPE_4999, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown(f"<div class='footer'>{T['disclaimer']}</div>", unsafe_allow_html=True)
