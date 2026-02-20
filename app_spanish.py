import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# ============================================================================
# CONFIGURACIÓN DE PÁGINA
# ============================================================================
st.set_page_config(
    page_title="GFI Informe de Fuga de Beneficios™",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🔍"
)

# ============================================================================
# ENLACES DE PAGO STRIPE
# ============================================================================
STRIPE_LINK_999 = "https://buy.stripe.com/8x25kFbp0dM4gQl0fB3VC00"
STRIPE_LINK_4999 = "https://buy.stripe.com/7sYcN764GdM4arX0fB3VC01"

# ============================================================================
# CSS PERSONALIZADO
# ============================================================================
st.markdown("""
<style>
    /* Sección hero */
    .hero-section {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Tarjeta de precio */
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
    
    /* Botón CTA */
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
    
    /* Visualización de resultados */
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
    
    /* Insignia de garantía */
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
# INICIALIZACIÓN DEL ESTADO DE SESIÓN
# ============================================================================
if 'assessment_complete' not in st.session_state:
    st.session_state.assessment_complete = False
if 'calculated_leak' not in st.session_state:
    st.session_state.calculated_leak = 0
if 'risk_score' not in st.session_state:
    st.session_state.risk_score = 0

# ============================================================================
# SECCIÓN HERO CON LOGO Y NUEVO POSICIONAMIENTO
# ============================================================================
col_logo, col_hero = st.columns([1, 3])

with col_logo:
    st.image("GFILOGO.png", width=200)

with col_hero:
    st.markdown("""
    <div style="padding: 1rem 0;">
        <h1 style="color: #1e40af; margin-bottom: 0.5rem;">GFI: Inteligencia de Flujo</h1>
        <h2 style="margin-top: 0.5rem; font-weight: 500; color: #1e40af; font-size: 1.3rem;">
            Motor de Inteligencia de Ejecución Pre y Post Transformación
        </h2>
        <p style="font-size: 1.1rem; margin-top: 1rem; color: #475569; line-height: 1.6;">
            <strong>Mida la ejecución antes de la transformación.</strong><br>
            <strong>Demuestre la ejecución después de la transformación.</strong>
        </p>
        <p style="font-size: 1rem; margin-top: 1rem; color: #64748b;">
            Diagnóstico gratuito disponible → Cuantifique la fricción estructural en 12 minutos
        </p>
    </div>
    """, unsafe_allow_html=True)

# Banner debajo del hero
st.image("banner.png", use_container_width=True)

# ============================================================================
# SECCIÓN DE POSICIONAMIENTO DEL MARCO GFI
# ============================================================================
st.markdown("""
<div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); 
     padding: 2rem; border-radius: 15px; margin: 2rem 0;">
    <h3 style="color: #0c4a6e; text-align: center; margin-bottom: 1.5rem;">
        GFI = Capa de Inteligencia Estructural para la Transformación Institucional
    </h3>
    <p style="color: #075985; text-align: center; font-size: 1.1rem; line-height: 1.6;">
        La mayoría de los compromisos de consultoría terminan en la implementación.<br>
        <strong>GFI mide el riesgo estructural antes de la transformación y demuestra la mejora estructural después.</strong><br>
        Esto crea una defensa de ROI medible.
    </p>
</div>
""", unsafe_allow_html=True)

# Propuesta de valor de doble fase
col_pre, col_post = st.columns(2)

with col_pre:
    st.markdown("""
    <div style="background: white; border: 2px solid #3b82f6; border-radius: 12px; 
         padding: 1.5rem; height: 100%;">
        <h4 style="color: #1e40af; margin-bottom: 1rem;">
            Ⅰ. Fase Pre-Transformación
        </h4>
        <p style="color: #475569; font-weight: 600; margin-bottom: 1rem;">
            Propósito: Cuantificar el riesgo de ejecución estructural antes de que comience la transformación
        </p>
        <ul style="color: #64748b; line-height: 1.8; margin-left: 1rem;">
            <li>Mapeo de densidad de latencia de decisiones</li>
            <li>Modelado de coeficiente de fricción organizacional</li>
            <li>Medición de línea base de pérdida de capacidad</li>
            <li>Índice de preparación para la ejecución</li>
        </ul>
        <p style="background: #dbeafe; padding: 0.75rem; border-radius: 8px; 
             margin-top: 1rem; color: #1e40af; font-weight: 600;">
            📊 Resultado: Cuadro de Mando de Preparación para la Ejecución Ejecutiva
        </p>
        <p style="color: #64748b; margin-top: 1rem; font-style: italic;">
            Garantiza que la transformación comience con claridad estructural, no con suposiciones. Reduce la exposición al riesgo de capital.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col_post:
    st.markdown("""
    <div style="background: white; border: 2px solid #10b981; border-radius: 12px; 
         padding: 1.5rem; height: 100%;">
        <h4 style="color: #059669; margin-bottom: 1rem;">
            Ⅱ. Fase Post-Transformación
        </h4>
        <p style="color: #475569; font-weight: 600; margin-bottom: 1rem;">
            Propósito: Medir si la transformación realmente mejoró la capacidad de ejecución
        </p>
        <ul style="color: #64748b; line-height: 1.8; margin-left: 1rem;">
            <li>Análisis delta de reducción de fricción</li>
            <li>Medición de compresión de latencia</li>
            <li>Tasa de expansión de capacidad de ejecución</li>
            <li>Índice de resiliencia institucional</li>
        </ul>
        <p style="background: #d1fae5; padding: 0.75rem; border-radius: 8px; 
             margin-top: 1rem; color: #059669; font-weight: 600;">
            ✅ Resultado: Informe de Certificación de Impacto de Transformación
        </p>
        <p style="color: #64748b; margin-top: 1rem; font-style: italic;">
            Cuantifique el delta de rendimiento real, no las promesas de presentaciones. Demuestre la mejora de ejecución con datos.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Posicionamiento Big 4
st.markdown("""
<div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); 
     padding: 2rem; border-radius: 15px; margin: 2rem 0; border-left: 5px solid #f59e0b;">
    <h4 style="color: #92400e; margin-bottom: 1rem;">
        🎯 Posicionamiento en el Ecosistema de Consultoría
    </h4>
    <p style="color: #78350f; font-size: 1.05rem; line-height: 1.7;">
        GFI opera como:<br>
        • <strong>Escáner de riesgo pre-compromiso</strong> — Identifique vulnerabilidades de ejecución antes de la transformación<br>
        • <strong>Capa de validación post-compromiso</strong> — Certifique la mejora real vs. los resultados prometidos<br>
        • <strong>Módulo de aseguramiento a nivel de junta directiva</strong> — Proporcione confianza ejecutiva con resultados cuantificados
    </p>
    <p style="color: #92400e; margin-top: 1rem; font-weight: 600;">
        Esto aumenta la credibilidad del proyecto y la confianza ejecutiva durante todo el ciclo de vida de la transformación.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# CONTENIDO PRINCIPAL
# ============================================================================

# Pestañas de navegación
tab1, tab2, tab3 = st.tabs(["💰 Evaluación Gratuita", "📊 Informe de Muestra", "🎁 Precios y Paquetes"])

# ============================================================================
# PESTAÑA 1: EVALUACIÓN GRATUITA (Generación de leads)
# ============================================================================
with tab1:
    st.header("Calculadora Gratuita de Fuga de Beneficios")
    st.markdown("**Responda 12 preguntas rápidas para estimar su fuga de beneficios anual**")
    
    with st.form("assessment_form"):
        st.subheader("Información de la Empresa")
        
        col1, col2 = st.columns(2)
        
        with col1:
            company_name = st.text_input("Nombre de la Empresa", placeholder="Empresa Ejemplo")
            
            employee_count = st.selectbox(
                "Número de Empleados",
                ["1-10", "11-50", "51-200", "201-500", "501-1000", "1000+"]
            )
            
            industry = st.selectbox(
                "Industria",
                ["Tecnología/SaaS", "Servicios Profesionales", "Finanzas", 
                 "Salud", "Manufactura", "Retail", "Otro"]
            )
            
            avg_salary = st.number_input(
                "Salario Anual Promedio de Empleado ($)",
                min_value=30000,
                value=75000,
                step=5000,
                help="Aproximado promedio en todos los empleados"
            )
            
            revenue_per_employee = st.number_input(
                "Ingresos Anuales por Empleado ($)",
                min_value=50000,
                value=150000,
                step=10000,
                help="Ingresos anuales totales / empleados totales"
            )
            
            meeting_hours_per_week = st.slider(
                "Horas Promedio en Reuniones por Empleado por Semana",
                0, 40, 15,
                help="Incluya todas las reuniones programadas, reuniones rápidas, revisiones"
            )
        
        with col2:
            approval_layers = st.slider(
                "Capas de Aprobación Promedio para Decisiones Clave",
                1, 10, 3,
                help="¿Cuántas personas deben aprobar decisiones importantes?"
            )
            
            project_delay_pct = st.slider(
                "Tasa de Retraso de Proyectos (%)",
                0, 100, 30,
                help="¿Qué % de proyectos terminan tarde?"
            )
            
            rework_pct = st.slider(
                "Retrabajo Debido a Falta de Comunicación (%)",
                0, 50, 15,
                help="% de trabajo que necesita rehacerse"
            )
            
            decision_time_days = st.slider(
                "Días Promedio para Tomar Decisiones Estratégicas",
                1, 90, 14,
                help="Desde la propuesta hasta la aprobación"
            )
            
            turnover_rate = st.slider(
                "Tasa de Rotación Anual de Empleados (%)",
                0, 50, 15,
                help="% de empleados que se van cada año"
            )
            
            customer_complaint_rate = st.slider(
                "Tasa de Quejas de Clientes (por 100 clientes)",
                0, 50, 5,
                help="¿Cuántos clientes se quejan de retrasos o problemas de calidad?"
            )
        
        submitted = st.form_submit_button("🔍 Calcular Mi Fuga de Beneficios Ocultos", use_container_width=True)
        
        if submitted:
            # MOTOR DE CÁLCULO
            emp_count_map = {
                "1-10": 5,
                "11-50": 30,
                "51-200": 125,
                "201-500": 350,
                "501-1000": 750,
                "1000+": 1500
            }
            employees = emp_count_map[employee_count]
            
            hourly_rate = avg_salary / 2080
            
            # CÁLCULO DE FRICCIÓN
            wasted_meeting_hours = meeting_hours_per_week * 0.4 * 50 * employees
            meeting_cost = wasted_meeting_hours * hourly_rate
            
            delay_factor = project_delay_pct / 100
            avg_project_value = revenue_per_employee * 0.3
            delay_cost = delay_factor * avg_project_value * employees * 0.2
            
            rework_factor = rework_pct / 100
            rework_cost = rework_factor * avg_salary * employees * 0.15
            
            decision_delay_weeks = decision_time_days / 7
            decision_opportunity_cost = (decision_delay_weeks - 1) * 500 * employees * 10
            
            turnover_factor = turnover_rate / 100
            avg_turnover_cost = avg_salary * 1.5
            turnover_total_cost = turnover_factor * employees * avg_turnover_cost
            
            complaint_factor = customer_complaint_rate / 100
            avg_customer_value = revenue_per_employee * 2
            customer_friction_cost = complaint_factor * employees * avg_customer_value * 0.1
            
            total_leak = (
                meeting_cost + 
                delay_cost + 
                rework_cost + 
                decision_opportunity_cost + 
                turnover_total_cost + 
                customer_friction_cost
            )
            
            risk_factors = [
                (approval_layers - 1) * 10,
                project_delay_pct * 0.5,
                rework_pct * 1.5,
                (decision_time_days / 30) * 20,
                turnover_rate,
                customer_complaint_rate * 1.5
            ]
            risk_score = min(sum(risk_factors) / len(risk_factors), 100)
            
            st.session_state.assessment_complete = True
            st.session_state.calculated_leak = total_leak
            st.session_state.risk_score = risk_score
            st.session_state.company_name = company_name
            st.session_state.employees = employees
            
            st.session_state.breakdown = {
                "Sobrecarga de Reuniones": meeting_cost,
                "Retrasos de Proyectos": delay_cost,
                "Retrabajo y Falta de Comunicación": rework_cost,
                "Cuellos de Botella en Decisiones": decision_opportunity_cost,
                "Costos de Rotación": turnover_total_cost,
                "Fricción con Clientes": customer_friction_cost
            }
    
    # VISUALIZACIÓN DE RESULTADOS
    if st.session_state.assessment_complete:
        st.success("✅ ¡Evaluación Completa!")
        
        st.markdown("---")
        
        st.markdown(f"""
        <div style="text-align: center; background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%); 
             padding: 3rem; border-radius: 15px; margin: 2rem 0;">
            <h3 style="color: #7f1d1d; margin-bottom: 1rem;">
                Fuga de Beneficios Anual Estimada de {st.session_state.company_name}
            </h3>
            <div class="big-number">
                ${st.session_state.calculated_leak:,.0f}
            </div>
            <p style="font-size: 1.2rem; color: #991b1b; margin-top: 1rem;">
                Eso es <strong>${st.session_state.calculated_leak/st.session_state.employees:,.0f} por empleado</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            risk_color = "#dc2626" if st.session_state.risk_score > 70 else "#f59e0b" if st.session_state.risk_score > 40 else "#10b981"
            
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=st.session_state.risk_score,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Puntuación de Riesgo de Fricción Operacional"},
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
            st.markdown("### 🎯 Su Perfil de Riesgo")
            
            if st.session_state.risk_score > 70:
                st.error("**🔴 ALTO RIESGO** - Se recomienda acción inmediata")
                st.markdown("""
                Su organización muestra múltiples signos de fricción operacional severa:
                - Cuellos de botella críticos en la toma de decisiones
                - Altas tasas de fallo/retraso de proyectos
                - Rotación elevada que indica problemas sistémicos
                """)
            elif st.session_state.risk_score > 40:
                st.warning("**🟡 RIESGO MODERADO** - Existen oportunidades de optimización")
                st.markdown("""
                Varios puntos de fricción están impactando el rendimiento:
                - Ineficiencias de coordinación
                - Oportunidades de mejora de procesos
                - Retrasos y retrabajo evitables
                """)
            else:
                st.success("**🟢 BAJO RIESGO** - Operaciones bien gestionadas")
                st.markdown("""
                Su organización demuestra una salud operacional sólida:
                - Procesos de decisión eficientes
                - Baja fricción en los flujos de trabajo
                - Oportunidad de ganancias incrementales
                """)
        
        st.markdown("### 💸 ¿Dónde Se Está Fugando Su Dinero?")
        
        breakdown_df = pd.DataFrame({
            'Categoría': list(st.session_state.breakdown.keys()),
            'Costo Anual': list(st.session_state.breakdown.values())
        })
        
        fig = go.Bar(
            x=breakdown_df['Categoría'],
            y=breakdown_df['Costo Anual'],
            marker=dict(
                color=breakdown_df['Costo Anual'],
                colorscale='Reds'
            )
        )
        
        fig = go.Figure(data=fig)
        fig.update_layout(
            showlegend=False,
            height=400,
            yaxis_title="Costo Anual ($)"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        
        st.markdown("""
        <div class="insight-box">
            <h3>🎯 Lo Que Acaba de Ver Es Solo el Comienzo</h3>
            <p style="font-size: 1.1rem;">
                Esta calculadora gratuita le da una <strong>estimación aproximada</strong>.
                Pero las fugas de beneficios reales están ocultas en los detalles:
            </p>
            <ul style="font-size: 1.05rem; margin-top: 1rem;">
                <li>¿Qué equipos específicos están sangrando más?</li>
                <li>¿Cuáles son sus 3 principales cuellos de botella solucionables?</li>
                <li>¿Qué valdría una reducción del 50% de la fricción?</li>
                <li>¿Cómo se compara con sus pares de la industria?</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🚀 Obtenga Su Informe Completo")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="price-card">
                <h3>📊 Informe Profesional</h3>
                <div class="price-tag">$999</div>
                <p style="font-size: 1.1rem; margin: 1.5rem 0;">
                    <strong>Análisis PDF Completo de 12 Páginas</strong>
                </p>
                <ul style="text-align: left; font-size: 1rem; line-height: 1.8;">
                    <li>✅ Desglose Detallado de Fuga de Beneficios</li>
                    <li>✅ Los 3 Principales Cuellos de Botella Operacionales</li>
                    <li>✅ Evaluación de Exposición al Riesgo</li>
                    <li>✅ Recomendaciones de Victoria Rápida</li>
                    <li>✅ Comparación de Referencia de la Industria</li>
                    <li>✅ Plan de Acción de 30 Días</li>
                </ul>
                <a href="{}" target="_blank" class="cta-button" style="margin-top: 1.5rem;">
                    Obtener Informe Profesional →
                </a>
                <p style="margin-top: 1rem; color: #64748b; font-size: 0.9rem;">
                    Entregado en 48 horas
                </p>
            </div>
            """.format(STRIPE_LINK_999), unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="price-card price-card-premium">
                <div style="background: #fbbf24; color: #7c2d12; padding: 0.5rem; 
                     border-radius: 5px; margin-bottom: 1rem; font-weight: bold;">
                    🔥 MÁS POPULAR
                </div>
                <h3>🎯 Análisis Profundo Ejecutivo</h3>
                <div class="price-tag price-tag-premium">$4,999</div>
                <p style="font-size: 1.1rem; margin: 1.5rem 0;">
                    <strong>Análisis Integral + Sesión de Estrategia</strong>
                </p>
                <ul style="text-align: left; font-size: 1rem; line-height: 1.8;">
                    <li>✅ Todo en el Informe Profesional</li>
                    <li>✅ Mapa de Calor de Fricción Personalizado</li>
                    <li>✅ Análisis Equipo por Equipo</li>
                    <li>✅ Calculadora de ROI para Intervenciones</li>
                    <li>✅ Hoja de Ruta de Implementación de 90 Días</li>
                    <li>✅ <strong>Llamada de Estrategia de 2 Horas con el Fundador</strong></li>
                    <li>✅ Soporte por Correo Electrónico de 30 Días</li>
                </ul>
                <a href="{}" target="_blank" class="cta-button" style="margin-top: 1.5rem; background: white; color: #7c3aed;">
                    Obtener Paquete Ejecutivo →
                </a>
                <p style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.9;">
                    Limitado a 5 clientes por mes
                </p>
            </div>
            """.format(STRIPE_LINK_4999), unsafe_allow_html=True)
        
        st.markdown("""
        <div class="guarantee-badge">
            <h3>💚 Garantía de Devolución del 100%</h3>
            <p style="margin-top: 0.5rem; font-size: 1.05rem;">
                Si no descubre al menos <strong>5 veces</strong> el costo del informe en fugas de beneficios ocultos,
                le reembolsaremos en su totalidad. Sin preguntas.
            </p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PESTAÑA 2: INFORME DE MUESTRA
# ============================================================================
with tab2:
    st.header("📊 Qué Obtendrá: Vista Previa del Informe de Muestra")
    
    st.info("**Nota:** Esta es una vista previa simplificada. Su informe real estará completamente personalizado con los datos de su empresa.")
    
    with st.expander("📄 Página 1: Resumen Ejecutivo", expanded=True):
        st.markdown("""
        ---
        **INFORME DE FUGA DE BENEFICIOS OCULTOS™**  
        *Preparado para: [Nombre de Su Empresa]*  
        *Fecha: [Fecha del Informe]*  
        *Analista: Ping Xu, Creador del Marco GFI*
        
        ---
        
        ### Resumen Ejecutivo
        
        Nuestro análisis revela que **[Nombre de la Empresa]** está experimentando una **$[X]** estimada
        en fuga de beneficios anual debido a la fricción operacional en múltiples dimensiones.
        
        **Hallazgos Clave:**
        
        🔴 **Fuente Principal de Fuga:** [Categoría de mayor costo]  
        💰 **Impacto Anual Total:** $[X]  
        ⚠️ **Puntuación de Riesgo:** [X]/100 - [Nivel de Riesgo]  
        📈 **Potencial de Recuperación:** $[X] (primeros 90 días)
        
        **Perspectiva Crítica:**  
        A diferencia de los costos visibles (salarios, gastos generales), estas fugas de beneficios están *ocultas*
        en su tejido operacional. Se acumulan silenciosamente, erosionando los márgenes y el posicionamiento competitivo.
        
        Este informe proporciona una hoja de ruta para recuperar este beneficio perdido.
        """)
    
    with st.expander("💸 Páginas 2-3: Análisis Detallado de Fuga de Beneficios"):
        st.markdown("""
        ### Fuga de Beneficios Anual por Categoría
        
        | Categoría | Costo Anual | % del Total | Severidad |
        |----------|-------------|-------------|-----------|
        | Sobrecarga de Reuniones | $[X] | [X]% | 🔴 Alto |
        | Retrasos de Proyectos | $[X] | [X]% | 🟡 Medio |
        | Retrabajo y Errores | $[X] | [X]% | 🔴 Alto |
        | Cuellos de Botella en Decisiones | $[X] | [X]% | 🟡 Medio |
        | Costos de Rotación | $[X] | [X]% | 🔴 Alto |
        | Fricción con Clientes | $[X] | [X]% | 🟢 Bajo |
        
        **Análisis Detallado:**
        
        Cada categoría se desglosa con:
        - Identificación de causa raíz
        - Metodología de cálculo de costos
        - Comparación de referencia de la industria
        - Ejemplos específicos de sus datos
        """)
    
    with st.expander("🎯 Páginas 4-5: Los 3 Principales Cuellos de Botella Operacionales"):
        st.markdown("""
        ### Cuello de Botella #1: [Problema Específico]
        
        **Descripción:** [Lo que está sucediendo]  
        **Impacto de Costo Anual:** $[X]  
        **Equipos Afectados:** [Equipos]  
        **Causa Raíz:** [Problema estructural]
        
        **Solución Recomendada:**  
        1. [Acción específica]
        2. [Acción específica]
        3. [Acción específica]
        
        **Recuperación Esperada:** $[X] dentro de [plazo]
        
        ---
        
        *(Los cuellos de botella #2 y #3 siguen el mismo formato)*
        """)
    
    with st.expander("📊 Páginas 6-7: Exposición al Riesgo y Referencias de la Industria"):
        st.markdown("""
        ### Su Perfil de Riesgo vs. Industria
        
        [Mostrando gráficos visuales:]
        - Su puntuación de riesgo vs. mediana de la industria
        - Intensidad de fricción por departamento
        - Análisis de tendencias (si hay múltiples evaluaciones)
        
        ### Posicionamiento Competitivo
        
        Las empresas en su industria con niveles de fricción similares crecen [X]% más lento que
        sus pares de baja fricción y experimentan [X]% mayor rotación de empleados.
        """)
    
    with st.expander("✅ Páginas 8-9: Recomendaciones de Victoria Rápida"):
        st.markdown("""
        ### 3 Victorias de Alto Impacto y Bajo Esfuerzo
        
        **Victoria Rápida #1: [Acción]**
        - **Qué hacer:** [Pasos específicos]
        - **Tiempo de implementación:** [X días]
        - **Ahorros esperados:** $[X]/año
        - **Dificultad:** Baja/Media/Alta
        
        **Victoria Rápida #2: [Acción]**  
        *(Mismo formato)*
        
        **Victoria Rápida #3: [Acción]**  
        *(Mismo formato)*
        
        ### Plan de Acción de 30 Días
        
        Semana 1: [Acciones]  
        Semana 2: [Acciones]  
        Semana 3: [Acciones]  
        Semana 4: [Acciones]
        """)
    
    with st.expander("🚀 Páginas 10-12: Próximos Pasos y Metodología"):
        st.markdown("""
        ### Hoja de Ruta de Implementación
        
        **Fase 1 (0-30 días):** Victorias rápidas  
        **Fase 2 (30-90 días):** Mejoras estructurales  
        **Fase 3 (90-180 días):** Incorporación cultural
        
        ### Metodología y Validación
        
        - Descripción general del marco
        - Fuentes de datos y suposiciones
        - Metodología de cálculo
        - Limitaciones e intervalos de confianza
        
        ### Acerca del Marco GFI
        
        [Descripción breve del marco y creador]
        """)
    
    st.markdown("---")
    
    st.success("""
    **👆 Esta vista previa muestra la estructura.** Su informe real incluirá:
    - Los números específicos de su empresa
    - Recomendaciones personalizadas
    - Perspectivas específicas de la industria
    - Próximos pasos accionables
    """)

# ============================================================================
# PESTAÑA 3: PRECIOS Y PAQUETES
# ============================================================================
with tab3:
    st.header("🎁 Elija Su Paquete")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="price-card">
            <h3>📊 Informe Profesional</h3>
            <div class="price-tag">$999</div>
            <p style="font-size: 1.2rem; margin: 1.5rem 0; font-weight: 600;">
                Informe de Diagnóstico Completo
            </p>
            <hr style="margin: 1.5rem 0;">
            <ul style="text-align: left; font-size: 1.05rem; line-height: 2;">
                <li>✅ Informe PDF de 12 Páginas</li>
                <li>✅ Análisis Detallado de Fuga de Beneficios</li>
                <li>✅ Identificación de los 3 Principales Cuellos de Botella</li>
                <li>✅ Puntuación de Exposición al Riesgo</li>
                <li>✅ Comparación de Referencia de la Industria</li>
                <li>✅ Recomendaciones de Victoria Rápida</li>
                <li>✅ Plan de Acción de 30 Días</li>
                <li>✅ Entregado en 48 horas</li>
            </ul>
            <a href="{}" target="_blank" class="cta-button" style="margin-top: 2rem;">
                Comprar Ahora →
            </a>
        </div>
        """.format(STRIPE_LINK_999), unsafe_allow_html=True)
        
        st.info("""
        **Perfecto para:**
        - Empresas medianas (50-500 empleados)
        - Equipos que exploran mejoras de eficiencia
        - CFO/COO que buscan datos para la toma de decisiones
        """)
    
    with col2:
        st.markdown("""
        <div class="price-card price-card-premium">
            <div style="background: #fbbf24; color: #7c2d12; padding: 0.5rem; 
                 border-radius: 5px; margin-bottom: 1rem; font-weight: bold;">
                ⭐ MEJOR VALOR
            </div>
            <h3>🎯 Análisis Profundo Ejecutivo</h3>
            <div class="price-tag price-tag-premium">$4,999</div>
            <p style="font-size: 1.2rem; margin: 1.5rem 0; font-weight: 600;">
                Análisis Completo + Sesión de Estrategia
            </p>
            <hr style="margin: 1.5rem 0; border-color: rgba(255,255,255,0.3);">
            <ul style="text-align: left; font-size: 1.05rem; line-height: 2;">
                <li>✅ Todo en el Informe Profesional</li>
                <li>✅ Mapa de Calor de Fricción Personalizado</li>
                <li>✅ Desglose Equipo por Equipo</li>
                <li>✅ Herramienta Calculadora de ROI</li>
                <li>✅ Hoja de Ruta de Implementación de 90 Días</li>
                <li>✅ <strong>Llamada de Estrategia de 2 Horas con el Fundador</strong></li>
                <li>✅ Plan de Acción Personalizado</li>
                <li>✅ Soporte por Correo Electrónico de 30 Días</li>
                <li>✅ Entrega Prioritaria (24 horas)</li>
            </ul>
            <a href="{}" target="_blank" class="cta-button" 
               style="margin-top: 2rem; background: white; color: #7c3aed;">
                Reserve Su Lugar →
            </a>
            <p style="margin-top: 1rem; font-size: 0.95rem; opacity: 0.95;">
                ⚠️ Limitado a 5 clientes por mes
            </p>
        </div>
        """.format(STRIPE_LINK_4999), unsafe_allow_html=True)
        
        st.info("""
        **Perfecto para:**
        - Equipos de liderazgo comprometidos con la transformación
        - Empresas con más de $10M en ingresos
        - Organizaciones que planean cambios operacionales importantes
        """)
    
    st.markdown("---")
    
    st.markdown("### ❓ Preguntas Frecuentes")
    
    with st.expander("¿Qué hace que esto sea diferente de un compromiso de consultoría típico?"):
        st.markdown("""
        **Consultoría tradicional:**
        - Honorarios de $50K-$200K+
        - Compromisos de 3-6 meses
        - Fuerte compromiso de tiempo de su equipo
        - Marcos generalizados
        
        **Informe de Fuga de Beneficios Ocultos:**
        - Precios fijos y transparentes
        - Entregado en 24-48 horas
        - Inversión mínima de tiempo (evaluación de 12 minutos)
        - Centrado específicamente en la fricción operacional
        - Accionable desde el primer día
        """)
    
    with st.expander("¿Cómo se calcula el informe?"):
        st.markdown("""
        El informe utiliza el **Marco GFI (Inteligencia de Flujo de Gobernanza)**, desarrollado por Ping Xu
        a través de una extensa investigación en economía organizacional y dinámica de sistemas.
        
        Entradas clave:
        - Sus respuestas de evaluación
        - Referencias de la industria
        - Multiplicadores de ingresos/costos
        - Modelos de intensidad de fricción
        
        Todos los cálculos son transparentes y se explican en la sección de metodología.
        """)
    
    with st.expander("¿Qué pasa si no descubro fugas de beneficios ocultos?"):
        st.markdown("""
        **Garantía de Devolución del 100%**
        
        Si su informe no identifica al menos **5 veces el costo del informe** en posibles ahorros/recuperación,
        le reembolsaremos en su totalidad. Sin preguntas.
        
        En 3 años de diagnósticos, nunca hemos tenido una solicitud de reembolso. Las organizaciones típicamente
        descubren de 10 a 50 veces el costo del informe en fugas ocultas.
        """)
    
    with st.expander("¿Qué tan rápido veré resultados?"):
        st.markdown("""
        **Cronología:**
        - **Inmediato:** Conciencia de la magnitud de la fuga de beneficios
        - **Semana 1:** Comienzan las implementaciones de victoria rápida
        - **30 Días:** Primeras mejoras medibles
        - **90 Días:** Impacto total de los cambios estructurales
        
        La mayoría de los clientes informan que recuperan el costo del informe en el primer mes solo con victorias rápidas.
        """)
    
    with st.expander("¿Ofrecen planes de pago?"):
        st.markdown("""
        Actualmente, solo ofrecemos pagos únicos a través de Stripe.
        
        Sin embargo, para el paquete **Análisis Profundo Ejecutivo**, podemos organizar un plan de pago caso por caso.
        Contáctenos después de comprar el Informe Profesional para discutir opciones.
        """)
    
    st.markdown("""
    <div class="guarantee-badge" style="margin-top: 3rem;">
        <h3>💚 Nuestra Promesa Para Usted</h3>
        <p style="font-size: 1.1rem; margin-top: 1rem; line-height: 1.6;">
            Estamos tan seguros de que descubrirá fugas de beneficios ocultos significativas que ofrecemos
            una <strong>garantía de devolución del 100%</strong> incondicional. Si no encuentra al menos
            <strong>5 veces el costo del informe</strong> en ahorros accionables, le reembolsaremos inmediatamente.
        </p>
        <p style="margin-top: 1rem; font-size: 0.95rem; color: #064e3b;">
            ✅ Sin riesgo. Sin complicaciones. Solo resultados.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PIE DE PÁGINA
# ============================================================================
st.markdown("---")

footer_col1, footer_col2 = st.columns([1, 3])

with footer_col1:
    st.image("GFILOGO.png", width=120)

with footer_col2:
    st.markdown("""
    <div style="padding-top: 1rem;">
        <p style="font-size: 1.1rem; font-weight: 600; color: #1e40af;">
            GFI: Inteligencia de Flujo
        </p>
        <p style="color: #64748b; margin-top: 0.5rem;">
            Impulsado por el Marco GFI
        </p>
        <p style="margin-top: 0.5rem; color: #64748b;">
            Creado por Ping Xu | Boston, Massachusetts
        </p>
        <p style="font-size: 0.9rem; margin-top: 1rem; color: #94a3b8;">
            © 2026 Todos los Derechos Reservados | <a href="mailto:support@gfi.com" style="color: #3b82f6;">Contactar Soporte</a>
        </p>
    </div>
    """, unsafe_allow_html=True)
