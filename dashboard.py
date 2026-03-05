import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Maternal Health Industry Intelligence",
    layout="wide"
)

st.title("Maternal Health Industry Intelligence Dashboard")

st.markdown("""
Executive overview of maternal health outcomes reported by digital maternity care platforms.
Metrics reflect publicly reported outcomes used by payers and employers to evaluate maternal care programs.
""")

st.divider()

# ====================================
# KPI PANEL
# ====================================

st.header("Industry Outcome Highlights")

col1, col2, col3 = st.columns(3)

col1.metric("Preterm Birth Reduction", "37%")
col1.metric("NICU Admission Reduction", "58%")

col2.metric("ER Visit Reduction", "46%")
col2.metric("NICU Length of Stay Reduction", "6.8 days")

col3.metric("Cost of Care Reduction", "15%")
col3.metric("Payer ROI", "3-5x")

st.caption("Source: Pomelo Care clinical outcomes and peer-reviewed program data.")

st.divider()

# ====================================
# CLINICAL OUTCOMES
# ====================================

st.header("Clinical Outcome Improvements")

clinical = pd.DataFrame({
    "Metric":[
        "Preterm Birth Reduction",
        "NICU Admission Reduction",
        "ER Visit Reduction"
    ],
    "Improvement":[37,58,46]
})

fig = px.bar(
    clinical,
    x="Metric",
    y="Improvement",
    color="Metric",
    title="Maternal Program Clinical Outcomes"
)

st.plotly_chart(fig,use_container_width=True)

st.caption("""
Sources: Pomelo Care clinical outcomes publications and peer-reviewed analyses demonstrating reductions in preterm birth,
NICU admissions, and emergency department utilization.
""")

st.divider()

# ====================================
# COST IMPACT
# ====================================

st.header("Cost & Payer ROI Impact")

cost = pd.DataFrame({
    "Metric":[
        "Total Cost Reduction",
        "Payer ROI"
    ],
    "Value":[
        15,
        3.9
    ]
})

fig = px.bar(
    cost,
    x="Metric",
    y="Value",
    color="Metric",
    title="Maternal Care Financial Impact"
)

st.plotly_chart(fig,use_container_width=True)

st.caption("""
Sources: Pomelo Care peer-reviewed outcomes reporting reduced cost of care and
~3–5x return on investment for payer programs.
""")

st.divider()

# ====================================
# EMPLOYER IMPACT
# ====================================

st.header("Employer & Workforce Outcomes")

employer = pd.DataFrame({
    "Metric":[
        "Employee Retention Impact",
        "Productivity Increase",
        "Mental Health Improvement"
    ],
    "Value":[
        74,
        83,
        33
    ]
})

fig = px.bar(
    employer,
    x="Metric",
    y="Value",
    color="Metric",
    title="Employer Impact Metrics"
)

st.plotly_chart(fig,use_container_width=True)

st.caption("""
Sources: Maven Clinic employer benefit outcomes reporting improved employee retention,
productivity, and maternal mental health outcomes.
""")

st.divider()

# ====================================
# INDUSTRY PROVIDER LANDSCAPE
# ====================================

st.header("Digital Maternal Health Platform Landscape")

providers = pd.DataFrame({
    "Company":[
        "Pomelo Care",
        "Maven Clinic",
        "Carrot Fertility",
        "Progyny",
        "Wildflower Health"
    ],
    "Focus":[
        "Virtual maternity care",
        "Women's and family health platform",
        "Global fertility and family benefits",
        "Fertility and maternity benefits",
        "Digital maternal care coordination"
    ]
})

st.table(providers)

st.caption("""
Sources: company websites and industry reports describing maternal and family health platforms.
""")

st.divider()

st.caption("Digital Deregulated Labs | Maternal Health Industry Intelligence Dashboard")
