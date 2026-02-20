
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="GFI Hidden Profit Leak Report™",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🔍"
)

# ============================================================================
# STRIPE PAYMENT LINKS
# ============================================================================
STRIPE_LINK_999 = "https://buy.stripe.com/8x25kFbp0dM4gQl0fB3VC00"
STRIPE_LINK_4999 = "https://buy.stripe.com/7sYcN764GdM4arX0fB3VC01"

# ============================================================================
# CUSTOM CSS
# ============================================================================
st.markdown("""
<style>
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Price card */
    .price-card {
        background: white;
        border: 3px solid #3b82f6;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .price-card-premium {
        background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
        border: 3px solid #7c3aed;
        color: white;
    }
    
    .price-tag {
        font-size: 3.5rem;
        font-weight: bold;
        color: #1e40af;
        margin: 1rem 0;
    }
    
    .price-tag-premium {
        color: white;
    }
    
    /* CTA Button */
    .cta-button {
        background: #10b981;
        color: white;
        padding: 1rem 2rem;
        border-radius: 10px;
        font-size: 1.3rem;
        font-weight: bold;
        text-decoration: none;
        display: inline-block;
        margin: 1rem 0;
        transition: all 0.3s;
    }
    
    .cta-button:hover {
        background: #059669;
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(16, 185, 129, 0.3);
    }
    
    /* Results display */
    .big-number {
        font-size: 4rem;
        font-weight: bold;
        color: #dc2626;
        text-align: center;
        margin: 2rem 0;
    }
    
    .insight-box {
        background: #fef3c7;
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0;
    }
    
    /* Guarantee badge */
    .guarantee-badge {
        background: #dcfce7;
        border: 2px solid #10b981;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
if 'assessment_complete' not in st.session_state:
    st.session_state.assessment_complete = False
if 'calculated_leak' not in st.session_state:
    st.session_state.calculated_leak = 0
if 'risk_score' not in st.session_state:
    st.session_state.risk_score = 0

# ============================================================================
# HERO SECTION WITH LOGO
# ============================================================================
col_logo, col_hero = st.columns([1, 3])

with col_logo:
    st.image("GFILOGO.png", width=200)

with col_hero:
    st.markdown("""
    <div style="padding: 1rem 0;">
        <h1 style="color: #1e40af; margin-bottom: 0.5rem;">Hidden Profit Leak Report™</h1>
        <h2 style="margin-top: 0.5rem; font-weight: 300; color: #475569;">
            Discover Where Your Company Is Silently Losing Money
        </h2>
        <p style="font-size: 1.2rem; margin-top: 1rem; color: #64748b;">
            12-minute assessment → Uncover $50K-$2M in hidden operational costs
        </p>
    </div>
    """, unsafe_allow_html=True)

# Banner image below hero
st.image("banner.png", use_container_width=True)

# ============================================================================
# MAIN CONTENT
# ============================================================================

# Navigation
tab1, tab2, tab3 = st.tabs(["💰 Free Assessment", "📊 Sample Report", "🎁 Pricing & Packages"])

# ============================================================================
# TAB 1: FREE ASSESSMENT (Lead Generation)
# ============================================================================
with tab1:
    st.header("Free Profit Leak Calculator")
    st.markdown("**Answer 12 quick questions to estimate your annual profit leakage**")
    
    with st.form("assessment_form"):
        st.subheader("Company Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            company_name = st.text_input("Company Name", placeholder="Acme Corp")
            
            employee_count = st.selectbox(
                "Number of Employees",
                ["1-10", "11-50", "51-200", "201-500", "501-1000", "1000+"]
            )
            
            industry = st.selectbox(
                "Industry",
                ["Technology/SaaS", "Professional Services", "Finance", 
                 "Healthcare", "Manufacturing", "Retail", "Other"]
            )
            
            avg_salary = st.number_input(
                "Average Employee Annual Salary ($)",
                min_value=30000,
                value=75000,
                step=5000,
                help="Approximate average across all employees"
            )
            
            revenue_per_employee = st.number_input(
                "Annual Revenue per Employee ($)",
                min_value=50000,
                value=150000,
                step=10000,
                help="Total annual revenue / total employees"
            )
            
            meeting_hours_per_week = st.slider(
                "Average Hours in Meetings per Employee per Week",
                0, 40, 15,
                help="Include all scheduled meetings, standups, reviews"
            )
        
        with col2:
            approval_layers = st.slider(
                "Average Approval Layers for Key Decisions",
                1, 10, 3,
                help="How many people must approve important decisions?"
            )
            
            project_delay_pct = st.slider(
                "Project Delay Rate (%)",
                0, 100, 30,
                help="What % of projects finish late?"
            )
            
            rework_pct = st.slider(
                "Rework Due to Miscommunication (%)",
                0, 50, 15,
                help="% of work that needs to be redone"
            )
            
            decision_time_days = st.slider(
                "Average Days to Make Strategic Decisions",
                1, 90, 14,
                help="From proposal to approval"
            )
            
            turnover_rate = st.slider(
                "Annual Employee Turnover Rate (%)",
                0, 50, 15,
                help="% of employees who leave each year"
            )
            
            customer_complaint_rate = st.slider(
                "Customer Complaint Rate (per 100 customers)",
                0, 50, 5,
                help="How many customers complain about delays or quality issues?"
            )
        
        submitted = st.form_submit_button("🔍 Calculate My Hidden Profit Leak", use_container_width=True)
        
        if submitted:
            # ============================================================================
            # CALCULATION ENGINE
            # ============================================================================
            
            # Employee count mapping
            emp_count_map = {
                "1-10": 5,
                "11-50": 30,
                "51-200": 125,
                "201-500": 350,
                "501-1000": 750,
                "1000+": 1500
            }
            employees = emp_count_map[employee_count]
            
            # Calculate hourly rate
            hourly_rate = avg_salary / 2080  # Annual hours
            
            # FRICTION CALCULATION
            # 1. Meeting overhead (assume 40% of meetings are low-value)
            wasted_meeting_hours = meeting_hours_per_week * 0.4 * 50 * employees
            meeting_cost = wasted_meeting_hours * hourly_rate
            
            # 2. Delay costs
            delay_factor = project_delay_pct / 100
            avg_project_value = revenue_per_employee * 0.3  # Assume 30% of revenue tied to projects
            delay_cost = delay_factor * avg_project_value * employees * 0.2
            
            # 3. Rework costs
            rework_factor = rework_pct / 100
            rework_cost = rework_factor * avg_salary * employees * 0.15
            
            # 4. Decision delay opportunity cost
            decision_delay_weeks = decision_time_days / 7
            decision_opportunity_cost = (decision_delay_weeks - 1) * 500 * employees * 10
            
            # 5. Turnover costs
            turnover_factor = turnover_rate / 100
            avg_turnover_cost = avg_salary * 1.5  # Cost to replace = 150% of salary
            turnover_total_cost = turnover_factor * employees * avg_turnover_cost
            
            # 6. Customer friction
            complaint_factor = customer_complaint_rate / 100
            avg_customer_value = revenue_per_employee * 2
            customer_friction_cost = complaint_factor * employees * avg_customer_value * 0.1
            
            # TOTAL ANNUAL LEAK
            total_leak = (
                meeting_cost + 
                delay_cost + 
                rework_cost + 
                decision_opportunity_cost + 
                turnover_total_cost + 
                customer_friction_cost
            )
            
            # RISK SCORE (0-100)
            risk_factors = [
                (approval_layers - 1) * 10,
                project_delay_pct * 0.5,
                rework_pct * 1.5,
                (decision_time_days / 30) * 20,
                turnover_rate,
                customer_complaint_rate * 1.5
            ]
            risk_score = min(sum(risk_factors) / len(risk_factors), 100)
            
            # Store in session state
            st.session_state.assessment_complete = True
            st.session_state.calculated_leak = total_leak
            st.session_state.risk_score = risk_score
            st.session_state.company_name = company_name
            st.session_state.employees = employees
            
            # Breakdown for display
            st.session_state.breakdown = {
                "Meeting Overhead": meeting_cost,
                "Project Delays": delay_cost,
                "Rework & Miscommunication": rework_cost,
                "Decision Bottlenecks": decision_opportunity_cost,
                "Turnover Costs": turnover_total_cost,
                "Customer Friction": customer_friction_cost
            }
    
    # ============================================================================
    # RESULTS DISPLAY
    # ============================================================================
    if st.session_state.assessment_complete:
        st.success("✅ Assessment Complete!")
        
        st.markdown("---")
        
        # Big number reveal
        st.markdown(f"""
        <div style="text-align: center; background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%); 
             padding: 3rem; border-radius: 15px; margin: 2rem 0;">
            <h3 style="color: #7f1d1d; margin-bottom: 1rem;">
                {st.session_state.company_name}'s Estimated Annual Profit Leak
            </h3>
            <div class="big-number">
                ${st.session_state.calculated_leak:,.0f}
            </div>
            <p style="font-size: 1.2rem; color: #991b1b; margin-top: 1rem;">
                That's <strong>${st.session_state.calculated_leak/st.session_state.employees:,.0f} per employee</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Risk score
        col1, col2 = st.columns(2)
        
        with col1:
            # Risk gauge
            risk_color = "#dc2626" if st.session_state.risk_score > 70 else "#f59e0b" if st.session_state.risk_score > 40 else "#10b981"
            
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=st.session_state.risk_score,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Operational Friction Risk Score"},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': risk_color},
                    'steps': [
                        {'range': [0, 40], 'color': "#dcfce7"},
                        {'range': [40, 70], 'color': "#fef3c7"},
                        {'range': [70, 100], 'color': "#fee2e2"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 85
                    }
                }
            ))
            
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 🎯 Your Risk Profile")
            
            if st.session_state.risk_score > 70:
                st.error("**🔴 HIGH RISK** - Immediate action recommended")
                st.markdown("""
                Your organization shows multiple signs of severe operational friction:
                - Critical bottlenecks in decision-making
                - High project failure/delay rates
                - Elevated turnover indicating systemic issues
                """)
            elif st.session_state.risk_score > 40:
                st.warning("**🟡 MODERATE RISK** - Optimization opportunities exist")
                st.markdown("""
                Several friction points are impacting performance:
                - Coordination inefficiencies
                - Process improvement opportunities
                - Preventable delays and rework
                """)
            else:
                st.success("**🟢 LOW RISK** - Well-managed operations")
                st.markdown("""
                Your organization demonstrates strong operational health:
                - Efficient decision processes
                - Low friction across workflows
                - Opportunity for incremental gains
                """)
        
        # Breakdown chart
        st.markdown("### 💸 Where Is Your Money Leaking?")
        
        breakdown_df = pd.DataFrame({
            'Category': list(st.session_state.breakdown.keys()),
            'Annual Cost': list(st.session_state.breakdown.values())
        })
        
        fig = px.bar(
            breakdown_df,
            x='Category',
            y='Annual Cost',
            color='Annual Cost',
            color_continuous_scale='Reds'
        )
        
        fig.update_layout(
            showlegend=False,
            height=400,
            yaxis_title="Annual Cost ($)"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Call to action
        st.markdown("---")
        
        st.markdown("""
        <div class="insight-box">
            <h3>🎯 What You Just Saw Is Only the Beginning</h3>
            <p style="font-size: 1.1rem;">
                This free calculator gives you a <strong>rough estimate</strong>. 
                But the real profit leaks are hidden in the details:
            </p>
            <ul style="font-size: 1.05rem; margin-top: 1rem;">
                <li>Which specific teams are bleeding the most?</li>
                <li>What are your top 3 fixable bottlenecks?</li>
                <li>What would a 50% friction reduction be worth?</li>
                <li>How do you compare to your industry peers?</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🚀 Get Your Complete Report")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="price-card">
                <h3>📊 Professional Report</h3>
                <div class="price-tag">$999</div>
                <p style="font-size: 1.1rem; margin: 1.5rem 0;">
                    <strong>Complete 12-Page PDF Analysis</strong>
                </p>
                <ul style="text-align: left; font-size: 1rem; line-height: 1.8;">
                    <li>✅ Detailed Profit Leak Breakdown</li>
                    <li>✅ Top 3 Operational Bottlenecks</li>
                    <li>✅ Risk Exposure Assessment</li>
                    <li>✅ Quick-Win Recommendations</li>
                    <li>✅ Industry Benchmark Comparison</li>
                    <li>✅ 30-Day Action Plan</li>
                </ul>
                <a href="{}" target="_blank" class="cta-button" style="margin-top: 1.5rem;">
                    Get Professional Report →
                </a>
                <p style="margin-top: 1rem; color: #64748b; font-size: 0.9rem;">
                    Delivered within 48 hours
                </p>
            </div>
            """.format(STRIPE_LINK_999), unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="price-card price-card-premium">
                <div style="background: #fbbf24; color: #7c2d12; padding: 0.5rem; 
                     border-radius: 5px; margin-bottom: 1rem; font-weight: bold;">
                    🔥 MOST POPULAR
                </div>
                <h3>🎯 Executive Deep Dive</h3>
                <div class="price-tag price-tag-premium">$4,999</div>
                <p style="font-size: 1.1rem; margin: 1.5rem 0;">
                    <strong>Comprehensive Analysis + Strategy Session</strong>
                </p>
                <ul style="text-align: left; font-size: 1rem; line-height: 1.8;">
                    <li>✅ Everything in Professional Report</li>
                    <li>✅ Custom Friction Heat Map</li>
                    <li>✅ Team-by-Team Analysis</li>
                    <li>✅ ROI Calculator for Interventions</li>
                    <li>✅ 90-Day Implementation Roadmap</li>
                    <li>✅ <strong>2-Hour Strategy Call with Founder</strong></li>
                    <li>✅ 30-Day Email Support</li>
                </ul>
                <a href="{}" target="_blank" class="cta-button" style="margin-top: 1.5rem; background: white; color: #7c3aed;">
                    Get Executive Package →
                </a>
                <p style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.9;">
                    Limited to 5 clients per month
                </p>
            </div>
            """.format(STRIPE_LINK_4999), unsafe_allow_html=True)
        
        # Guarantee
        st.markdown("""
        <div class="guarantee-badge">
            <h3>💚 100% Money-Back Guarantee</h3>
            <p style="margin-top: 0.5rem; font-size: 1.05rem;">
                If you don't discover at least <strong>5x</strong> the report cost in hidden profit leaks, 
                we'll refund you in full. No questions asked.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# TAB 2: SAMPLE REPORT
# ============================================================================
with tab2:
    st.header("📊 What You'll Get: Sample Report Preview")
    
    st.info("**Note:** This is a simplified preview. Your actual report will be fully customized with your company's data.")
    
    # Report preview sections
    with st.expander("📄 Page 1: Executive Summary", expanded=True):
        st.markdown("""
        ---
        **HIDDEN PROFIT LEAK REPORT™**  
        *Prepared for: [Your Company Name]*  
        *Date: [Report Date]*  
        *Analyst: Ping Xu, GFI Framework Creator*
        
        ---
        
        ### Executive Summary
        
        Our analysis reveals that **[Company Name]** is experiencing an estimated **$[X]** in annual 
        profit leakage due to operational friction across multiple dimensions.
        
        **Key Findings:**
        
        🔴 **Primary Leak Source:** [Largest cost category]  
        💰 **Total Annual Impact:** $[X]  
        ⚠️ **Risk Score:** [X]/100 - [Risk Level]  
        📈 **Recovery Potential:** $[X] (first 90 days)
        
        **Critical Insight:**  
        Unlike visible costs (salaries, overhead), these profit leaks are *hidden* in your 
        operational fabric. They compound silently, eroding margins and competitive positioning.
        
        This report provides a roadmap to recover this lost profit.
        """)
    
    with st.expander("💸 Page 2-3: Detailed Profit Leak Analysis"):
        st.markdown("""
        ### Annual Profit Leakage by Category
        
        | Category | Annual Cost | % of Total | Severity |
        |----------|-------------|------------|----------|
        | Meeting Overhead | $[X] | [X]% | 🔴 High |
        | Project Delays | $[X] | [X]% | 🟡 Medium |
        | Rework & Errors | $[X] | [X]% | 🔴 High |
        | Decision Bottlenecks | $[X] | [X]% | 🟡 Medium |
        | Turnover Costs | $[X] | [X]% | 🔴 High |
        | Customer Friction | $[X] | [X]% | 🟢 Low |
        
        **Detailed Analysis:**
        
        Each category is broken down with:
        - Root cause identification
        - Cost calculation methodology
        - Industry benchmark comparison
        - Specific examples from your data
        """)
    
    with st.expander("🎯 Page 4-5: Top 3 Operational Bottlenecks"):
        st.markdown("""
        ### Bottleneck #1: [Specific Issue]
        
        **Description:** [What's happening]  
        **Annual Cost Impact:** $[X]  
        **Affected Teams:** [Teams]  
        **Root Cause:** [Structural issue]
        
        **Recommended Fix:**  
        1. [Specific action]
        2. [Specific action]
        3. [Specific action]
        
        **Expected Recovery:** $[X] within [timeframe]
        
        ---
        
        *(Bottlenecks #2 and #3 follow same format)*
        """)
    
    with st.expander("📊 Page 6-7: Risk Exposure & Industry Benchmarks"):
        st.markdown("""
        ### Your Risk Profile vs. Industry
        
        [Visual charts showing:]
        - Your risk score vs. industry median
        - Friction intensity by department
        - Trend analysis (if multiple assessments)
        
        ### Competitive Positioning
        
        Companies in your industry with similar friction levels grow [X]% slower than 
        low-friction peers and experience [X]% higher employee turnover.
        """)
    
    with st.expander("✅ Page 8-9: Quick-Win Recommendations"):
        st.markdown("""
        ### 3 High-Impact, Low-Effort Wins
        
        **Quick Win #1: [Action]**
        - **What to do:** [Specific steps]
        - **Implementation time:** [X days]
        - **Expected savings:** $[X]/year
        - **Difficulty:** Low/Medium/High
        
        **Quick Win #2: [Action]**  
        *(Same format)*
        
        **Quick Win #3: [Action]**  
        *(Same format)*
        
        ### 30-Day Action Plan
        
        Week 1: [Actions]  
        Week 2: [Actions]  
        Week 3: [Actions]  
        Week 4: [Actions]
        """)
    
    with st.expander("🚀 Page 10-12: Next Steps & Methodology"):
        st.markdown("""
        ### Implementation Roadmap
        
        **Phase 1 (0-30 days):** Quick wins  
        **Phase 2 (30-90 days):** Structural improvements  
        **Phase 3 (90-180 days):** Cultural embedding
        
        ### Methodology & Validation
        
        - Framework overview
        - Data sources and assumptions
        - Calculation methodology
        - Limitations and confidence intervals
        
        ### About the GFI Framework
        
        [Brief description of the framework and creator]
        """)
    
    st.markdown("---")
    
    st.success("""
    **👆 This preview shows the structure.** Your actual report will include:
    - Your company's specific numbers
    - Custom recommendations
    - Industry-specific insights
    - Actionable next steps
    """)

# ============================================================================
# TAB 3: PRICING & PACKAGES
# ============================================================================
with tab3:
    st.header("🎁 Choose Your Package")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="price-card">
            <h3>📊 Professional Report</h3>
            <div class="price-tag">$999</div>
            <p style="font-size: 1.2rem; margin: 1.5rem 0; font-weight: 600;">
                Complete Diagnostic Report
            </p>
            <hr style="margin: 1.5rem 0;">
            <ul style="text-align: left; font-size: 1.05rem; line-height: 2;">
                <li>✅ 12-Page PDF Report</li>
                <li>✅ Detailed Profit Leak Analysis</li>
                <li>✅ Top 3 Bottleneck Identification</li>
                <li>✅ Risk Exposure Score</li>
                <li>✅ Industry Benchmark Comparison</li>
                <li>✅ Quick-Win Recommendations</li>
                <li>✅ 30-Day Action Plan</li>
                <li>✅ Delivered within 48 hours</li>
            </ul>
            <a href="{}" target="_blank" class="cta-button" style="margin-top: 2rem;">
                Purchase Now →
            </a>
        </div>
        """.format(STRIPE_LINK_999), unsafe_allow_html=True)
        
        st.info("""
        **Perfect for:**
        - Mid-sized companies (50-500 employees)
        - Teams exploring efficiency improvements
        - CFOs/COOs seeking data for decision-making
        """)
    
    with col2:
        st.markdown("""
        <div class="price-card price-card-premium">
            <div style="background: #fbbf24; color: #7c2d12; padding: 0.5rem; 
                 border-radius: 5px; margin-bottom: 1rem; font-weight: bold;">
                ⭐ BEST VALUE
            </div>
            <h3>🎯 Executive Deep Dive</h3>
            <div class="price-tag price-tag-premium">$4,999</div>
            <p style="font-size: 1.2rem; margin: 1.5rem 0; font-weight: 600;">
                Complete Analysis + Strategy Session
            </p>
            <hr style="margin: 1.5rem 0; border-color: rgba(255,255,255,0.3);">
            <ul style="text-align: left; font-size: 1.05rem; line-height: 2;">
                <li>✅ Everything in Professional Report</li>
                <li>✅ Custom Friction Heat Map</li>
                <li>✅ Team-by-Team Breakdown</li>
                <li>✅ ROI Calculator Tool</li>
                <li>✅ 90-Day Implementation Roadmap</li>
                <li>✅ <strong>2-Hour Strategy Call with Founder</strong></li>
                <li>✅ Personalized Action Plan</li>
                <li>✅ 30-Day Email Support</li>
                <li>✅ Priority Delivery (24 hours)</li>
            </ul>
            <a href="{}" target="_blank" class="cta-button" 
               style="margin-top: 2rem; background: white; color: #7c3aed;">
                Reserve Your Spot →
            </a>
            <p style="margin-top: 1rem; font-size: 0.95rem; opacity: 0.95;">
                ⚠️ Limited to 5 clients per month
            </p>
        </div>
        """.format(STRIPE_LINK_4999), unsafe_allow_html=True)
        
        st.info("""
        **Perfect for:**
        - Leadership teams committed to transformation
        - Companies with >$10M revenue
        - Organizations planning major operational changes
        """)
    
    st.markdown("---")
    
    # FAQ Section
    st.markdown("### ❓ Frequently Asked Questions")
    
    with st.expander("What makes this different from a typical consulting engagement?"):
        st.markdown("""
        **Traditional consulting:**
        - $50K-$200K+ fees
        - 3-6 month engagements
        - Heavy time commitment from your team
        - Generalized frameworks
        
        **Hidden Profit Leak Report:**
        - Fixed, transparent pricing
        - Delivered in 24-48 hours
        - Minimal time investment (12-minute assessment)
        - Focused specifically on operational friction
        - Actionable from day one
        """)
    
    with st.expander("How is the report calculated?"):
        st.markdown("""
        The report uses the **GFI (Governance Flow Intelligence) Framework**, developed by Ping Xu 
        through extensive research in organizational economics and systems dynamics.
        
        Key inputs:
        - Your assessment responses
        - Industry benchmarks
        - Revenue/cost multipliers
        - Friction intensity models
        
        All calculations are transparent and explained in the methodology section.
        """)
    
    with st.expander("What if I don't find hidden profit leaks?"):
        st.markdown("""
        **100% Money-Back Guarantee**
        
        If your report doesn't identify at least **5x the report cost** in potential savings/recovery, 
        we'll refund you completely. No questions asked.
        
        In 3 years of diagnostics, we've never had a refund request. Organizations typically 
        discover 10-50x the report cost in hidden leaks.
        """)
    
    with st.expander("How quickly will I see results?"):
        st.markdown("""
        **Timeline:**
        - **Immediate:** Awareness of profit leak magnitude
        - **Week 1:** Quick-win implementations begin
        - **30 Days:** First measurable improvements
        - **90 Days:** Full impact of structural changes
        
        Most clients report recovering the report cost within the first month through quick wins alone.
        """)
    
    with st.expander("Do you offer payment plans?"):
        st.markdown("""
        Currently, we only offer one-time payments via Stripe.
        
        However, for the **Executive Deep Dive** package, we can arrange a payment plan on a case-by-case basis. 
        Contact us after purchasing the Professional Report to discuss options.
        """)
    
    # Guarantee section
    st.markdown("""
    <div class="guarantee-badge" style="margin-top: 3rem;">
        <h3>💚 Our Promise to You</h3>
        <p style="font-size: 1.1rem; margin-top: 1rem; line-height: 1.6;">
            We're so confident you'll discover significant hidden profit leaks that we offer an 
            unconditional <strong>100% money-back guarantee</strong>. If you don't find at least 
            <strong>5x the report cost</strong> in actionable savings, we'll refund you immediately.
        </p>
        <p style="margin-top: 1rem; font-size: 0.95rem; color: #064e3b;">
            ✅ No risk. No hassle. Just results.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# FOOTER WITH LOGO
# ============================================================================
st.markdown("---")

footer_col1, footer_col2 = st.columns([1, 3])

with footer_col1:
    st.image("GFILOGO.png", width=120)

with footer_col2:
    st.markdown("""
    <div style="padding-top: 1rem;">
        <p style="font-size: 1.1rem; font-weight: 600; color: #1e40af;">
            GFI: Flow Intelligence
        </p>
        <p style="color: #64748b; margin-top: 0.5rem;">
            Powered by the GFI Framework
        </p>
        <p style="margin-top: 0.5rem; color: #64748b;">
            Created by Ping Xu | Boston, MA
        </p>
        <p style="font-size: 0.9rem; margin-top: 1rem; color: #94a3b8;">
            © 2026 All Rights Reserved | <a href="mailto:support@gfi.com" style="color: #3b82f6;">Contact Support</a>
        </p>
    </div>
    """, unsafe_allow_html=True)
