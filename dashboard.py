import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Maternal Health Outcomes Intelligence",
    layout="wide"
)

# --------------------------------------
# HEADER BRANDING
# --------------------------------------

st.markdown("""
# Maternal Health Outcomes Intelligence Platform
**Digital Deregulated Labs | Population Health Analytics**

This platform presents selected indicators related to maternal health outcomes, neonatal care utilization, and maternity care delivery programs across the United States.
""")

st.divider()

# --------------------------------------
# GLOBAL FILTER PANEL
# --------------------------------------

st.sidebar.header("Data Filters")

region = st.sidebar.selectbox(
    "Region",
    ["United States","Global"]
)

year = st.sidebar.selectbox(
    "Year",
    ["2024","2023","2022"]
)

population = st.sidebar.selectbox(
    "Population Segment",
    ["Commercial","Medicaid","Employer Programs"]
)

st.caption(f"Region: {region} | Year: {year} | Population Segment: {population}")

st.divider()

# --------------------------------------
# KEY INDICATORS
# --------------------------------------

st.subheader("Maternal Health Program Indicators")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Preterm Birth Reduction","37%")
col2.metric("NICU Admission Reduction","58%")
col3.metric("Emergency Visit Reduction","46%")
col4.metric("NICU Length of Stay Reduction","6.8 days")

col5,col6 = st.columns(2)

col5.metric("Total Cost of Care Reduction","8.8%")
col6.metric("Program Return on Investment","3.9x")

st.caption("Source: Pomelo Care maternal health outcomes publications.")

st.divider()

# --------------------------------------
# CLINICAL OUTCOME CHART
# --------------------------------------

st.subheader("Clinical Outcome Improvements")

clinical_data = pd.DataFrame({
    "Outcome":[
        "Preterm Birth Reduction",
        "NICU Admission Reduction",
        "Emergency Department Visit Reduction"
    ],
    "Improvement":[37,58,46]
})

fig = px.bar(
    clinical_data,
    x="Outcome",
    y="Improvement",
    color="Outcome",
    template="plotly_white"
)

fig.update_layout(
    showlegend=False,
    yaxis_title="Percent Reduction",
    xaxis_title=""
)

st.plotly_chart(fig,use_container_width=True)

st.caption("Source: Pomelo Care clinical outcomes reporting.")

st.divider()

# --------------------------------------
# US MATERNAL HEALTH MAP
# --------------------------------------

st.subheader("Maternal Health Outcomes by State")

state_data = pd.DataFrame({
    "state":[
        "CA","TX","FL","NY","GA","NC","IL","PA","OH","MI"
    ],
    "preterm_rate":[
        8.8,10.9,10.2,9.3,11.2,10.4,9.7,9.8,10.1,10.3
    ]
})

fig_map = px.choropleth(
    state_data,
    locations="state",
    locationmode="USA-states",
    color="preterm_rate",
    scope="usa",
    color_continuous_scale="Reds",
    labels={"preterm_rate":"Preterm Birth Rate (%)"}
)

fig_map.update_layout(
    margin=dict(l=0,r=0,t=0,b=0)
)

st.plotly_chart(fig_map,use_container_width=True)

st.caption("Source: CDC National Center for Health Statistics preterm birth surveillance.")

st.divider()

# --------------------------------------
# COST CONTEXT
# --------------------------------------

st.subheader("Neonatal Care Cost Context")

cost_data = pd.DataFrame({
    "Category":[
        "Average Delivery Cost",
        "Preterm Birth Cost",
        "NICU Admission Cost"
    ],
    "Cost":[
        12000,
        35000,
        45000
    ]
})

fig_cost = px.bar(
    cost_data,
    x="Category",
    y="Cost",
    color="Category",
    template="plotly_white"
)

fig_cost.update_layout(
    showlegend=False,
    yaxis_title="Average Cost (USD)",
    xaxis_title=""
)

st.plotly_chart(fig_cost,use_container_width=True)

st.caption("Source: March of Dimes maternal and neonatal healthcare cost research.")

st.divider()

# --------------------------------------
# FOOTER
# --------------------------------------

st.caption("Digital Deregulated Labs | Maternal Health Outcomes Intelligence Platform")
