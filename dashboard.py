import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Maternal Health Outcomes Intelligence",
    layout="wide"
)

st.title("Maternal Health Outcomes Intelligence Dashboard")

st.markdown("""
Executive analytics overview of maternal health program outcomes reported by digital maternity care platforms.
These metrics reflect the clinical, financial, and workforce outcomes used by payers and employers to evaluate maternity care programs.
""")

st.divider()

# ================================
# EXECUTIVE KPI PANEL
# ================================

st.subheader("Key Outcome Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Preterm Birth Reduction", "37%")
col2.metric("NICU Admission Reduction", "58%")
col3.metric("Emergency Visit Reduction", "46%")
col4.metric("NICU Length of Stay Reduction", "6.8 days")

col5, col6 = st.columns(2)

col5.metric("Total Cost of Care Reduction", "8.8%")
col6.metric("Payer ROI", "3.9x")

st.caption("Source: Pomelo Care clinical outcomes publications and payer program reporting.")

st.divider()

# ================================
# CLINICAL OUTCOMES
# ================================

st.header("Clinical Outcome Improvements")

clinical_data = pd.DataFrame({
    "Metric":[
        "Preterm Birth Reduction",
        "NICU Admission Reduction",
        "Emergency Department Visits"
    ],
    "Improvement":[37,58,46]
})

fig = go.Figure()

fig.add_trace(go.Bar(
    x=clinical_data["Metric"],
    y=clinical_data["Improvement"],
    marker_color=["#4CAF50","#2196F3","#FF9800"]
))

fig.update_layout(
    template="plotly_dark",
    yaxis_title="Percent Improvement",
    xaxis_title="Clinical Outcome",
    height=450
)

st.plotly_chart(fig,use_container_width=True)

st.caption("Source: Pomelo Care outcomes reporting and SMFM Global Congress clinical presentations.")

st.markdown("""
**Insights**

• Programs providing coordinated maternal care can reduce preterm birth rates by more than one-third.  
• NICU admission reductions significantly decrease neonatal complications and long-term health costs.  
• Reduced emergency department visits indicate improved prenatal care access and care coordination.
""")

st.divider()

# ================================
# COST & ROI
# ================================

st.header("Cost & Payer ROI Impact")

cost_data = pd.DataFrame({
    "Metric":[
        "Total Cost of Care Reduction",
        "Payer ROI"
    ],
    "Value":[
        8.8,
        3.9
    ]
})

fig = go.Figure()

fig.add_trace(go.Bar(
    x=cost_data["Metric"],
    y=cost_data["Value"],
    marker_color=["#673AB7","#00BCD4"]
))

fig.update_layout(
    template="plotly_dark",
    yaxis_title="Value",
    xaxis_title="Financial Outcome",
    height=450
)

st.plotly_chart(fig,use_container_width=True)

st.caption("Source: Pomelo Care payer program outcomes and peer-reviewed analyses.")

st.markdown("""
**Insights**

• Even single-digit percentage reductions in maternal care costs translate into millions in savings for health plans.  
• High-risk pregnancies and NICU utilization represent the largest drivers of maternity healthcare spending.  
• Digital maternal health platforms increasingly demonstrate measurable ROI for payer programs.
""")

st.divider()

# ================================
# EMPLOYER IMPACT
# ================================

st.header("Employer Workforce Impact")

employer_data = pd.DataFrame({
    "Metric":[
        "Employee Retention Likelihood",
        "Mental Health Support Improvement"
    ],
    "Value":[
        74,
        33
    ]
})

fig = go.Figure()

fig.add_trace(go.Bar(
    x=employer_data["Metric"],
    y=employer_data["Value"],
    marker_color=["#E91E63","#9C27B0"]
))

fig.update_layout(
    template="plotly_dark",
    yaxis_title="Percent",
    xaxis_title="Employer Outcome",
    height=450
)

st.plotly_chart(fig,use_container_width=True)

st.caption("Source: Maven Clinic employer benefit outcomes reporting.")

st.markdown("""
**Insights**

• Maternal health benefits are increasingly used as strategic workforce retention tools.  
• Access to maternal mental health resources improves employee productivity and postpartum recovery.  
• Employers are expanding family health programs to improve employee satisfaction and long-term retention.
""")

st.divider()

# ================================
# NICU COST IMPACT (IMPROVED CHART)
# ================================

st.header("NICU Cost Impact Context")

nicu_data = pd.DataFrame({
    "Category":[
        "Average Birth Cost",
        "Preterm Birth Cost",
        "NICU Admission Cost"
    ],
    "Cost":[
        12000,
        35000,
        45000
    ]
})

fig = go.Figure()

fig.add_trace(go.Bar(
    x=nicu_data["Category"],
    y=nicu_data["Cost"],
    marker_color=["#607D8B","#FF5722","#F44336"]
))

fig.update_layout(
    template="plotly_dark",
    yaxis_title="Average Cost (USD)",
    xaxis_title="Maternal Care Cost Category",
    height=450
)

st.plotly_chart(fig,use_container_width=True)

st.caption("Source: March of Dimes maternal health cost studies and U.S. neonatal care expenditure research.")

st.markdown("""
**Insights**

• NICU admissions represent one of the largest cost drivers in maternal healthcare.  
• Preventing preterm births significantly reduces neonatal intensive care utilization.  
• Programs focused on prenatal care coordination can materially lower high-cost neonatal outcomes.
""")

st.divider()

# ================================
# INDUSTRY LANDSCAPE
# ================================

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

st.markdown("""
**Insights**

• Digital maternal health companies are expanding across fertility, pregnancy, and postpartum care.  
• Payers and employers increasingly partner with virtual maternity platforms to improve outcomes and reduce costs.  
• Integrated maternal care ecosystems are becoming a key area of healthcare innovation.
""")

st.divider()

st.caption("Digital Deregulated Labs | Maternal Health Outcomes Intelligence Dashboard")
