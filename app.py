
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta, timezone
import base64
import io

# =========================
# PDF + DB + Email deps
# =========================
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

from supabase import create_client, Client

# SendGrid (recommended for Streamlit Cloud)
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, Email, To, Content, Attachment, FileContent, FileName, FileType, Disposition
)

# ============================================================================
# 0. SETTINGS (Secrets Required)
# ============================================================================
# Streamlit Secrets (Streamlit Cloud -> Settings -> Secrets)
# [SUPABASE]
# URL = "https://xxxxx.supabase.co"
# SERVICE_ROLE_KEY = "xxxxx"   # use Service Role for inserts (server-side only)
#
# [SENDGRID]
# API_KEY = "SG.xxxxx"
# FROM_EMAIL = "you@yourdomain.com"

SUPABASE_URL = st.secrets.get("SUPABASE", {}).get("URL", "")
SUPABASE_KEY = st.secrets.get("SUPABASE", {}).get("SERVICE_ROLE_KEY", "")
SENDGRID_API_KEY = st.secrets.get("SENDGRID", {}).get("API_KEY", "")
SENDGRID_FROM_EMAIL = st.secrets.get("SENDGRID", {}).get("FROM_EMAIL", "")

SUPABASE_TABLE = "gfi_leads"  # create this table in Supabase (schema below)

STRIPE_999 = "https://buy.stripe.com/8x25kFbp0dM4gQl0fB3VC00"
STRIPE_4999 = "https://buy.stripe.com/7sYcN764GdM4arX0fB3VC01"

# ============================================================================
# 1. PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="GFI Diagnostic Platform",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "About": "GFI: Governance Fitness Index (GFI Flow Intelligence) — diagnosing institutional friction."
    },
)

# ============================================================================
# 2. CUSTOM CSS STYLING
# ============================================================================
st.markdown(
    """
<style>
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    .metric-card {
        background: #f8fafc;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .warning-box {
        background: #fef3c7;
        border-left: 4px solid #f59e0b;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .case-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }
    .big-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #dc2626;
    }
    .section-divider {
        height: 2px;
        background: linear-gradient(to right, #3b82f6, transparent);
        margin: 2rem 0;
    }
    div[data-testid="stMetricValue"] { font-size: 1.35rem; }
    div[data-testid="stMetricDelta"] { font-size: 0.95rem; }
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# 3. BRAND HEADER
# ============================================================================
st.markdown(
    """
<div class="main-header">
    <h1>🔍 GFI: Governance Fitness Index</h1>
    <h3>A Structural Framework for Diagnosing Institutional Friction</h3>
    <p style="margin-top: 1rem; opacity: 0.92;">
        <strong>Prepared by:</strong> Ping Xu | Massachusetts, USA | 2026
    </p>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================================
# 4. UTILS — Supabase / PDF / Email
# ============================================================================

@st.cache_resource(show_spinner=False)
def get_supabase() -> Client | None:
    if not SUPABASE_URL or not SUPABASE_KEY:
        return None
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def format_money(x: float) -> str:
    return f"${x:,.0f}"

def classify_risk(total_friction: float) -> tuple[str, str]:
    # (risk_level, recommended_tier)
    if total_friction < 100000:
        return "🟢 Low Friction", "Operational Optimization (Self-guided)"
    if total_friction < 1000000:
        return "🟡 Moderate Risk", "$999 Executive Diagnostic"
    if total_friction < 5000000:
        return "🟠 Severe Structural Friction", "$999 Executive Diagnostic (Recommended) — consider Structural Audit"
    return "🔴 Critical Governance Breakdown", "$4,999 Structural Audit (Recommended)"

def build_snapshot_pdf_bytes(payload: dict) -> bytes:
    """
    3-page executive snapshot PDF (ReportLab).
    payload keys: name, email, org, role, industry, org_size, pd_hours, affected_people,
                  hourly_rate, multiplier, total_delay, weeks_lost, efficiency_loss,
                  direct_leak, opp_loss, total_friction, risk_level, rec_tier, created_at
    """
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    def header(title: str):
        c.setFillColor(colors.HexColor("#1e3a8a"))
        c.rect(0, height - 1.0 * inch, width, 1.0 * inch, fill=1, stroke=0)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(0.75 * inch, height - 0.65 * inch, title)
        c.setFont("Helvetica", 10)
        c.setFillColor(colors.white)
        c.drawRightString(width - 0.75 * inch, height - 0.65 * inch, "GFI Flow Intelligence")

    def footer(page_num: int):
        c.setFillColor(colors.HexColor("#64748b"))
        c.setFont("Helvetica", 9)
        c.drawString(0.75 * inch, 0.5 * inch, f"© 2026 Ping Xu | Governance Fitness Index (GFI)  |  Page {page_num}/3")

    # Page 1 — Executive Summary
    header("Executive Snapshot — Governance Fitness Index (GFI)")
    c.setFillColor(colors.black)
    y = height - 1.45 * inch

    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75 * inch, y, "Client / Organization")
    y -= 0.25 * inch
    c.setFont("Helvetica", 11)
    c.drawString(0.75 * inch, y, f"Name: {payload['name']}")
    y -= 0.2 * inch
    c.drawString(0.75 * inch, y, f"Email: {payload['email']}")
    y -= 0.2 * inch
    c.drawString(0.75 * inch, y, f"Organization: {payload['org']}")
    y -= 0.2 * inch
    c.drawString(0.75 * inch, y, f"Role/Title: {payload.get('role','') or '-'}")
    y -= 0.2 * inch
    c.drawString(0.75 * inch, y, f"Industry: {payload.get('industry','-')} | Size: {payload.get('org_size','-')}")
    y -= 0.35 * inch

    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75 * inch, y, "Headline Findings")
    y -= 0.30 * inch

    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.HexColor("#dc2626"))
    c.drawString(0.75 * inch, y, f"Annual Friction Exposure: {format_money(payload['total_friction'])}")
    y -= 0.28 * inch

    c.setFillColor(colors.black)
    c.setFont("Helvetica", 12)
    c.drawString(0.75 * inch, y, f"Risk Level: {payload['risk_level']}")
    y -= 0.22 * inch
    c.drawString(0.75 * inch, y, f"Capacity Loss Estimate: {payload['efficiency_loss']:.1f}%")
    y -= 0.22 * inch
    c.drawString(0.75 * inch, y, f"Recommended Engagement: {payload['rec_tier']}")
    y -= 0.35 * inch

    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75 * inch, y, "Interpretation (Decision-Grade)")
    y -= 0.28 * inch
    c.setFont("Helvetica", 11)
    lines = [
        "This snapshot converts hidden coordination delay into measurable economic exposure.",
        "It is an initial signal review (not a compliance audit).",
        "Paid tiers produce a structured report and intervention blueprint tailored to your system design.",
    ]
    for line in lines:
        c.drawString(0.75 * inch, y, f"• {line}")
        y -= 0.20 * inch

    footer(1)
    c.showPage()

    # Page 2 — Inputs & Breakdown
    header("Snapshot Inputs & Cost Breakdown")
    c.setFillColor(colors.black)
    y = height - 1.45 * inch

    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75 * inch, y, "Inputs Used")
    y -= 0.28 * inch
    c.setFont("Helvetica", 11)

    inputs = [
        ("Process Delay (hours/person/year)", f"{payload['pd_hours']:,.1f}"),
        ("Affected Personnel", f"{payload['affected_people']:,.0f}"),
        ("Average Hourly Cost", f"{format_money(payload['hourly_rate'])}"),
        ("Value Multiplier", f"{payload['multiplier']:.1f}x"),
        ("Total Hours Lost", f"{payload['total_delay']:,.0f} hrs"),
        ("Weeks Lost (40-hr)", f"{payload['weeks_lost']:.1f} weeks"),
    ]
    for k, v in inputs:
        c.drawString(0.75 * inch, y, f"{k}:")
        c.drawRightString(width - 0.75 * inch, y, v)
        y -= 0.20 * inch

    y -= 0.20 * inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75 * inch, y, "Cost Composition")
    y -= 0.28 * inch
    c.setFont("Helvetica", 11)

    costs = [
        ("Direct Payroll Leak", format_money(payload["direct_leak"])),
        ("Opportunity Loss", format_money(payload["opp_loss"])),
        ("Total Friction Exposure", format_money(payload["total_friction"])),
    ]
    for k, v in costs:
        c.drawString(0.75 * inch, y, f"{k}:")
        c.drawRightString(width - 0.75 * inch, y, v)
        y -= 0.20 * inch

    y -= 0.25 * inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75 * inch, y, "What This Typically Signals")
    y -= 0.28 * inch
    c.setFont("Helvetica", 11)
    signals = [
        "Decision latency: too many gates or unclear decision ownership",
        "Rework loops: misalignment and late-stage corrections",
        "Coordination tax: meetings, escalations, and context switching",
        "Structural ambiguity: accountability diluted across multiple pathways",
    ]
    for s in signals:
        c.drawString(0.75 * inch, y, f"• {s}")
        y -= 0.20 * inch

    footer(2)
    c.showPage()

    # Page 3 — Next Steps / Offers
    header("Next Step Options")
    c.setFillColor(colors.black)
    y = height - 1.45 * inch

    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75 * inch, y, "Option 1 — $999 Executive Diagnostic (48-hour turnaround)")
    y -= 0.28 * inch
    c.setFont("Helvetica", 11)
    opt1 = [
        "Structured report with friction mapping + root-cause pattern",
        "Top 3 structural interventions with expected impact ranges",
        "Leadership-ready summary for internal alignment",
    ]
    for s in opt1:
        c.drawString(0.75 * inch, y, f"• {s}")
        y -= 0.20 * inch

    y -= 0.20 * inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75 * inch, y, "Option 2 — $4,999 Structural Audit (deep redesign)")
    y -= 0.28 * inch
    c.setFont("Helvetica", 11)
    opt2 = [
        "Cross-team workflow mapping + governance redesign blueprint",
        "Benchmark positioning memo (comparative narrative)",
        "Executive briefing for alignment and implementation planning",
    ]
    for s in opt2:
        c.drawString(0.75 * inch, y, f"• {s}")
        y -= 0.20 * inch

    y -= 0.35 * inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.75 * inch, y, "Payment Links")
    y -= 0.25 * inch
    c.setFont("Helvetica", 11)
    c.drawString(0.75 * inch, y, f"$999: {STRIPE_999}")
    y -= 0.18 * inch
    c.drawString(0.75 * inch, y, f"$4,999: {STRIPE_4999}")

    y -= 0.35 * inch
    c.setFillColor(colors.HexColor("#64748b"))
    c.setFont("Helvetica", 10)
    c.drawString(0.75 * inch, y, "Prepared by Ping Xu | Creator, Governance Fitness Index (GFI) | GFI Flow Intelligence")

    footer(3)
    c.showPage()

    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf

def supabase_insert_lead(supabase: Client, row: dict) -> tuple[bool, str]:
    try:
        # Ensure created_at is ISO
        if "created_at" not in row:
            row["created_at"] = datetime.now(timezone.utc).isoformat()
        supabase.table(SUPABASE_TABLE).insert(row).execute()
        return True, "OK"
    except Exception as e:
        return False, str(e)

def sendgrid_send_with_attachment(to_email: str, subject: str, text: str, pdf_bytes: bytes, send_at_epoch: int | None = None) -> tuple[bool, str]:
    try:
        if not SENDGRID_API_KEY or not SENDGRID_FROM_EMAIL:
            return False, "SendGrid secrets missing"

        sg = SendGridAPIClient(SENDGRID_API_KEY)

        message = Mail(
            from_email=Email(SENDGRID_FROM_EMAIL),
            to_emails=To(to_email),
            subject=subject,
            plain_text_content=Content("text/plain", text),
        )

        encoded = base64.b64encode(pdf_bytes).decode()
        attachment = Attachment(
            FileContent(encoded),
            FileName("GFI_Executive_Snapshot.pdf"),
            FileType("application/pdf"),
            Disposition("attachment"),
        )
        message.attachment = attachment

        # Schedule send (SendGrid supports send_at in personalizations)
        if send_at_epoch is not None:
            # attach send_at to personalization
            message.personalizations[0].send_at = send_at_epoch

        resp = sg.send(message)
        if 200 <= resp.status_code < 300:
            return True, f"OK ({resp.status_code})"
        return False, f"SendGrid error ({resp.status_code})"
    except Exception as e:
        return False, str(e)

# ============================================================================
# 5. NAVIGATION TABS
# ============================================================================
tabs = st.tabs(
    [
        "🎯 Risk Diagnostic",
        "📊 Methodology",
        "📚 Case Library",
        "👤 Founder & Architect",
        "📈 Benchmark Data",
    ]
)

# ============================================================================
# TAB 1: DIAGNOSTIC ENGINE + ENGINE UPGRADE
# ============================================================================
with tabs[0]:
    st.header("Institutional Friction Diagnostic Model")
    st.markdown("*Quantify the invisible cost of organizational inefficiency*")

    col_input, col_display = st.columns([1, 1.5], gap="large")

    with col_input:
        st.subheader("📋 Input Parameters")

        with st.expander("🏢 Organization Context", expanded=True):
            org_size = st.selectbox(
                "Organization Size",
                ["Small (1–50)", "Medium (51–200)", "Large (201–1000)", "Enterprise (1000+)"],
            )
            industry = st.selectbox(
                "Industry",
                [
                    "Technology/SaaS",
                    "Finance",
                    "Healthcare",
                    "Manufacturing",
                    "Professional Services",
                    "Retail",
                    "Public Sector / Agency",
                    "Other",
                ],
            )

        st.divider()
        st.markdown("#### Core Friction Metrics")

        pd_hours = st.number_input(
            "Process Delay (hours/person/year)",
            min_value=0.0,
            value=150.0,
            step=10.0,
            help="Total hours lost per person per year due to systemic friction (delays, rework, coordination overhead).",
        )

        affected_people = st.number_input(
            "Affected Personnel",
            min_value=1,
            value=5,
            help="Number of people impacted by this friction.",
        )

        hourly_rate = st.number_input(
            "Average Hourly Cost ($)",
            min_value=0.0,
            value=65.0,
            step=5.0,
            help="Fully burdened hourly rate (salary + benefits + overhead).",
        )

        st.divider()
        st.markdown("#### 💰 Value Multiplier")

        multiplier_presets = {
            "Administrative/Support": 1.5,
            "Operations/Manufacturing": 2.0,
            "Engineering/Product": 5.0,
            "Sales/Revenue": 8.0,
            "Executive/Strategic": 10.0,
            "Public Sector / Service Delivery": 3.0,
            "Custom": 3.0,
        }

        role_type = st.selectbox("Role Type", list(multiplier_presets.keys()))
        if role_type == "Custom":
            multiplier = st.slider(
                "Custom Value Multiplier",
                1.0,
                15.0,
                3.0,
                0.5,
                help="How many times their cost does this role generate in value?",
            )
        else:
            multiplier = multiplier_presets[role_type]
            st.info(f"💡 Recommended multiplier for {role_type}: **{multiplier}x**")

    with col_display:
        st.subheader("📊 Diagnostic Results")

        total_delay = pd_hours * affected_people
        direct_leak = total_delay * hourly_rate
        opp_loss = direct_leak * multiplier
        total_friction = direct_leak + opp_loss

        weeks_lost = total_delay / 40.0
        efficiency_loss = (weeks_lost / 52.0) * 100.0 if weeks_lost > 0 else 0.0

        m1, m2, m3 = st.columns(3)
        m1.metric("Total Hours Lost", f"{total_delay:,.0f} hrs", delta=f"{weeks_lost:.1f} weeks", delta_color="inverse")
        m2.metric("Direct Payroll Leak", f"{format_money(direct_leak)}")
        m3.metric("Opportunity Loss", f"{format_money(opp_loss)}", delta="Hidden Cost", delta_color="inverse")

        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

        st.markdown(
            f"""
        <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%); border-radius: 12px; margin: 1rem 0;">
            <div style="font-size: 1.05rem; color: #7f1d1d; margin-bottom: 0.5rem;">
                TOTAL INSTITUTIONAL FRICTION COST (ANNUAL)
            </div>
            <div class="big-number" style="color: #dc2626;">
                {format_money(total_friction)}
            </div>
            <div style="margin-top: 0.8rem; font-size: 1.0rem; color: #991b1b;">
                Estimated impact for the affected team
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        fig = go.Figure(
            data=[
                go.Bar(name="Direct Cost", x=["Friction Impact"], y=[direct_leak], marker_color="#3b82f6"),
                go.Bar(name="Opportunity Cost", x=["Friction Impact"], y=[opp_loss], marker_color="#ef4444"),
            ]
        )
        fig.update_layout(
            title="Cost Composition",
            barmode="stack",
            height=300,
            showlegend=True,
            yaxis_title="Cost ($)",
            template="plotly_white",
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### 🎯 GFI Strategic Insights")
        st.warning(
            f"""
**Performance Impact:** This friction represents an estimated **{efficiency_loss:.1f}%** reduction in annual capacity.  
You're not just losing money — you're losing **execution velocity**.

**What this usually signals:** decision latency, rework loops, coordination tax, accountability dilution.
"""
        )

        with st.expander("💡 Friction Elimination ROI Calculator"):
            reduction_pct = st.slider("Expected Friction Reduction (%)", 0, 100, 50)
            savings = total_friction * (reduction_pct / 100.0)
            implementation_cost = st.number_input("Implementation Cost ($)", min_value=0, value=50000, step=5000)
            roi = ((savings - implementation_cost) / implementation_cost) * 100 if implementation_cost > 0 else 0
            payback_months = (implementation_cost / (savings / 12)) if savings > 0 else 0
            c1, c2, c3 = st.columns(3)
            c1.metric("Annual Savings", format_money(savings))
            c2.metric("ROI", f"{roi:,.0f}%")
            c3.metric("Payback Period", f"{payback_months:.1f} months")

        # ============================================================
        # ✅ ENGINE UPGRADE: DB SAVE + PDF DOWNLOAD + EMAIL NOW + EMAIL +24H
        # ============================================================
        st.markdown("---")
        st.subheader("🔐 Unlock Executive Snapshot (Lead Capture)")

        lead_col1, lead_col2 = st.columns(2)
        with lead_col1:
            lead_name = st.text_input("Full Name *", placeholder="Jane Doe")
            lead_email = st.text_input("Work Email *", placeholder="jane@company.com")
        with lead_col2:
            lead_org = st.text_input("Organization *", placeholder="Company / Agency")
            lead_role = st.text_input("Role / Title", placeholder="CFO / Director / PM / etc.")

        unlock = st.button("Generate Executive Snapshot", type="primary")

        if unlock:
            if not (lead_name.strip() and lead_email.strip() and lead_org.strip()):
                st.warning("Please complete the required fields (Name, Work Email, Organization).")
            else:
                created_at = datetime.now(timezone.utc).isoformat()
                risk_level, rec_tier = classify_risk(total_friction)

                snapshot_payload = {
                    "created_at": created_at,
                    "name": lead_name.strip(),
                    "email": lead_email.strip(),
                    "org": lead_org.strip(),
                    "role": lead_role.strip(),
                    "industry": industry,
                    "org_size": org_size,
                    "pd_hours": float(pd_hours),
                    "affected_people": int(affected_people),
                    "hourly_rate": float(hourly_rate),
                    "multiplier": float(multiplier),
                    "total_delay": float(total_delay),
                    "weeks_lost": float(weeks_lost),
                    "efficiency_loss": float(efficiency_loss),
                    "direct_leak": float(direct_leak),
                    "opp_loss": float(opp_loss),
                    "total_friction": float(total_friction),
                    "risk_level": risk_level,
                    "rec_tier": rec_tier,
                }

                # 1) Build PDF
                pdf_bytes = build_snapshot_pdf_bytes(snapshot_payload)

                # 2) Save to Supabase
                supabase = get_supabase()
                db_ok, db_msg = (False, "Supabase secrets missing")
                if supabase is not None:
                    db_ok, db_msg = supabase_insert_lead(supabase, snapshot_payload)

                # 3) Email Now (with PDF)
                email_now_ok, email_now_msg = (False, "SendGrid secrets missing")
                if SENDGRID_API_KEY and SENDGRID_FROM_EMAIL:
                    subject_now = "Your GFI Executive Snapshot (PDF Attached)"
                    body_now = (
                        "Attached is your GFI Executive Snapshot.\n\n"
                        "This snapshot is an initial signal review. Paid tiers produce a structured report and intervention blueprint.\n\n"
                        f"$999 Executive Diagnostic: {STRIPE_999}\n"
                        f"$4,999 Structural Audit: {STRIPE_4999}\n\n"
                        "— Ping Xu | Creator, Governance Fitness Index (GFI)\n"
                    )
                    email_now_ok, email_now_msg = sendgrid_send_with_attachment(
                        to_email=lead_email.strip(),
                        subject=subject_now,
                        text=body_now,
                        pdf_bytes=pdf_bytes,
                        send_at_epoch=None
                    )

                # 4) Schedule Email +24H (SendGrid send_at)
                email_24h_ok, email_24h_msg = (False, "SendGrid secrets missing")
                if SENDGRID_API_KEY and SENDGRID_FROM_EMAIL:
                    send_at = int((datetime.now(timezone.utc) + timedelta(hours=24)).timestamp())
                    subject_24 = "Follow-up: Next Step Options for Your GFI Snapshot"
                    body_24 = (
                        "Quick follow-up on your GFI Executive Snapshot.\n\n"
                        "If you want a decision-grade report with interventions, choose:\n"
                        f"• $999 Executive Diagnostic (48-hour): {STRIPE_999}\n"
                        f"• $4,999 Structural Audit: {STRIPE_4999}\n\n"
                        "Reply to this email if you want a short scoping call.\n\n"
                        "— Ping Xu | GFI Flow Intelligence\n"
                    )
                    email_24h_ok, email_24h_msg = sendgrid_send_with_attachment(
                        to_email=lead_email.strip(),
                        subject=subject_24,
                        text=body_24,
                        pdf_bytes=pdf_bytes,
                        send_at_epoch=send_at
                    )

                # UI Output
                st.success("Executive Snapshot Unlocked.")

                snap_c1, snap_c2, snap_c3 = st.columns(3)
                snap_c1.metric("Risk Level", risk_level)
                snap_c2.metric("Capacity Loss", f"{efficiency_loss:.1f}%")
                snap_c3.metric("Annual Friction Exposure", format_money(total_friction))

                st.info(f"**Recommended Engagement Level:** {rec_tier}")

                # Downloadable PDF
                st.download_button(
                    label="⬇️ Download Executive Snapshot (PDF)",
                    data=pdf_bytes,
                    file_name="GFI_Executive_Snapshot.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )

                # Status indicators (silent but clear)
                status_cols = st.columns(3)
                status_cols[0].metric("DB Save", "OK" if db_ok else "FAIL")
                status_cols[1].metric("Email (Now)", "OK" if email_now_ok else "FAIL")
                status_cols[2].metric("Email (+24h)", "OK" if email_24h_ok else "FAIL")

                # Paid CTAs
                st.markdown("### 🚀 Next Step (Paid Options)")
                opt1, opt2 = st.columns(2)
                with opt1:
                    st.markdown(
                        """
**Option 1 — $999 Executive Diagnostic**  
• 48-hour structured report  
• Friction mapping + root cause pattern  
• Top 3 structural interventions  
• Leadership-ready summary  
"""
                    )
                    st.markdown(f"➡️ **Pay $999:** [Proceed to Payment]({STRIPE_999})")

                with opt2:
                    st.markdown(
                        """
**Option 2 — $4,999 Structural Audit**  
• Deep system redesign blueprint  
• Cross-team workflow mapping  
• Benchmark positioning memo  
• Executive briefing  
"""
                    )
                    st.markdown(f"➡️ **Pay $4,999:** [Proceed to Payment]({STRIPE_4999})")

# ============================================================================
# TAB 2: METHODOLOGY
# ============================================================================
with tabs[1]:
    st.header("📊 GFI Methodology")
    st.markdown("*A rigorous framework for institutional friction analysis*")

    st.markdown(
        """
### 🧠 Theoretical Foundation

The GFI framework synthesizes insights from:

- **Transaction Cost Economics**: friction as organizational transaction costs  
- **Institutional Theory**: how rules shape behavior  
- **Systems Dynamics**: feedback loops and latency  
- **Behavioral Economics**: cognitive load and decision bottlenecks  
"""
    )

    st.divider()
    st.markdown(
        """
### 🔬 The GFI Diagnostic Model

