import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Maternal Health Outcomes Intelligence",
    layout="wide"
)

st.title("Maternal Health Outcomes Intelligence Dashboard")

st.markdown(
"""
Executive analytics view of maternal health program outcomes reported by leading digital maternity care providers.
"""
)

st.divider()

# ======================================
# EXECUTIVE KPI TILES
# ======================================

st.subheader("Industry Outcome Highlights")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Preterm Birth Reduction", "37%")
col2.metric("NICU Admission Reduction", "58%")
col3.metric("Emergency Visit Reduction", "46%")
col4.metric("NICU Length of Stay Reduction", "6.8 days")

col5, col6 = st.columns(2)

col5.metric("Total Cost Reduction", "8.8%")
col6.metric("Payer Return on Investment", "3.9x")

st.caption("Source: Pomelo Care clinical outcomes publications and payer program reports.")

st.divider()

# ======================================
# CLINICAL OUTCOMES
# ======================================

st.header("Clinical Outcome Improvements")

clinical_metrics = {
    "Metric":[
        "Preterm Birth Reduction",
        "NICU Admission Reduction",
        "Emergency Department Reduction"
    ],
    "Improvement (%)":[
        37,
        58,
        46
    ]
}

df_clinical = pd.DataFrame(clinical_metrics)

fig = go.Figure()

fig.add_trace(go.Bar(
    x=df_clinical["Metric"],
    y=df_clinical["Improvement (%)"],
    marker_color=["#1f77b4","#2ca02c","#ff7f0e"]
))

fig.update_layout(
    template="plotly_dark",
    yaxis_title="Improvement Percentage",
    xaxis_title="Clinical Metric",
    height=450
)

st.plotly_chart(fig,use_container_width=True)

st.caption("Source: Pomelo Care outcomes study and SMFM Global Congress presentations.")

st.divider()

# ======================================
# COST IMPACT
# ======================================

st.header("Cost & Payer Impact")

cost_metrics = {
    "Metric":[
        "Total Cost of Care Reduction",
        "Return on Investment"
    ],
    "Value":[
        8.8,
        3.9
    ]
}

df_cost = pd.DataFrame(cost_metrics)

fig = go.Figure()

fig.add_trace(go.Bar(
    x=df_cost["Metric"],
    y=df_cost["Value"],
    marker_color=["#9467bd","#17becf"]
))

fig.update_layout(
    template="plotly_dark",
    yaxis_title="Value",
    xaxis_title="Financial Metric",
    height=450
)

st.plotly_chart(fig,use_container_width=True)

st.caption("Source: Pomelo Care payer program analysis and peer-reviewed outcomes reporting.")

st.divider()

# ======================================
# EMPLOYER IMPACT
# ======================================

st.header("Employer Workforce Outcomes")

employer_metrics = {
    "Metric":[
        "Employee Retention Likelihood",
        "Mental Health Support Improvement"
    ],
    "Value":[
        74,
        33
    ]
}

df_employer = pd.DataFrame(employer_metrics)

fig = go.Figure()

fig.add_trace(go.Bar(
    x=df_employer["Metric"],
    y=df_employer["Value"],
    marker_color=["#e377c2","#bcbd22"]
))

fig.update_layout(
    template="plotly_dark",
    yaxis_title="Percentage",
    xaxis_title="Employer Outcome Metric",
    height=450
)

st.plotly_chart(fig,use_container_width=True)

st.caption("Source: Maven Clinic employer benefits outcomes reporting.")

st.divider()

# ======================================
# NICU COST CONTEXT
# ======================================

st.header("NICU Cost Impact Context")

nicu_data = {
    "Metric":[
        "Average NICU Cost Per Infant"
    ],
    "Value":[
        45000
    ]
}

df_nicu = pd.DataFrame(nicu_data)

fig = go.Figure()

fig.add_trace(go.Bar(
    x=df_nicu["Metric"],
    y=df_nicu["Value"],
    marker_color="#d62728"
))

fig.update_layout(
    template="plotly_dark",
    yaxis_title="Cost (USD)",
    xaxis_title="Healthcare Cost Metric",
    height=450
)

st.plotly_chart(fig,use_container_width=True)

st.caption("Source: March of Dimes and U.S. maternal healthcare cost analyses.")

st.divider()

# ======================================
# INDUSTRY LANDSCAPE
# ======================================

st.header("Digital Maternal Health Platform Landscape")

providers = pd.DataFrame({
    "Company":[
        "Pomelo Care",
        "Maven Clinic",
        "Carrot Fertility",
        "Progyny",
        "Wildflower Health"
    ],
    "Primary Focus":[
        "Virtual maternity care programs",
        "Women's and family health platform",
        "Global fertility and family benefits",
        "Fertility and maternity benefits",
        "Digital maternal care coordination"
    ]
})

st.dataframe(providers,use_container_width=True)

st.caption("Sources: Company websites and public investor materials.")

st.divider()

st.caption("Digital Deregulated Labs | Maternal Health Outcomes Intelligence")
