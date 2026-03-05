import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Maternal Health Outcomes Intelligence",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
# Maternal Health Outcomes Intelligence
**Digital Deregulated Labs | Population Health Analytics**

Maternal health indicators related to pregnancy outcomes, neonatal care utilization, and maternity care delivery programs across the United States.
""")

st.divider()

# --------------------------------------------------
# GLOBAL FILTER PANEL
# --------------------------------------------------

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

# --------------------------------------------------
# KPI DATA
# --------------------------------------------------

kpi_data = {
    "Commercial":{"preterm":37,"nicu":58,"er":46},
    "Medicaid":{"preterm":22,"nicu":30,"er":28},
    "Employer Programs":{"preterm":37,"nicu":58,"er":46}
}

kpis = kpi_data[population]

# --------------------------------------------------
# KPI PANEL
# --------------------------------------------------

st.subheader("Program Outcome Indicators")

c1,c2,c3,c4 = st.columns(4)

c1.metric("Preterm Birth Reduction",f"{kpis['preterm']}%")
c2.metric("NICU Admission Reduction",f"{kpis['nicu']}%")
c3.metric("Emergency Visit Reduction",f"{kpis['er']}%")
c4.metric("NICU Length of Stay Reduction","6.8 days")

c5,c6 = st.columns(2)

c5.metric("Total Cost of Care Reduction","8.8%")
c6.metric("Program ROI","3.9x")

st.caption("Source: Pomelo Care maternal health outcomes publications.")

st.divider()

# --------------------------------------------------
# DASHBOARD TABS
# --------------------------------------------------

tab1, tab2, tab3 = st.tabs(["Clinical Outcomes","Geographic Distribution","Cost Context"])

# --------------------------------------------------
# TAB 1 — CLINICAL OUTCOMES
# --------------------------------------------------

with tab1:

    st.subheader("Clinical Outcome Improvements")

    outcomes = pd.DataFrame({
        "Outcome":[
            "Preterm Birth Reduction",
            "NICU Admission Reduction",
            "Emergency Department Visit Reduction"
        ],
        "Improvement":[37,58,46]
    })

    fig = px.bar(
        outcomes,
        x="Outcome",
        y="Improvement",
        color="Outcome",
        template="plotly_white"
    )

    fig.update_layout(showlegend=False)

    st.plotly_chart(fig,use_container_width=True)

    st.caption("Source: Pomelo Care clinical outcomes reporting.")

    st.markdown("""
**Insights**

Programs providing coordinated maternal care have demonstrated measurable reductions in preterm birth, neonatal intensive care utilization, and emergency department visits during pregnancy.
""")

    # --------------------------------------------
    # TREND CHART
    # --------------------------------------------

    st.subheader("Preterm Birth Rate Trend")

    trend_data = pd.DataFrame({
        "Year":[2019,2020,2021,2022,2023],
        "US":[10.2,10.1,10.5,10.4,10.2],
        "Global":[9.5,9.4,9.7,9.8,9.6]
    })

    region_map = {
        "United States":"US",
        "Global":"Global"
    }

    selected_column = region_map[region]

    fig_trend = px.line(
        trend_data,
        x="Year",
        y=selected_column,
        markers=True,
        template="plotly_white"
    )

    fig_trend.update_layout(
        yaxis_title="Preterm Birth Rate (%)"
    )

    st.plotly_chart(fig_trend,use_container_width=True)

    st.caption("Source: CDC National Center for Health Statistics.")

    st.markdown("""
**Insights**

Preterm birth rates in the United States remain near 10% of births annually and are a major driver of neonatal intensive care utilization and healthcare spending.
""")

# --------------------------------------------------
# TAB 2 — GEOGRAPHIC MAP
# --------------------------------------------------

with tab2:

    st.subheader("Preterm Birth Rate by State")

    map_data = {
        "2024":[8.8,10.9,10.2,9.3,11.2],
        "2023":[9.1,11.2,10.5,9.5,11.5],
        "2022":[9.3,11.5,10.8,9.8,11.7]
    }

    states = ["CA","TX","FL","NY","GA"]

    state_df = pd.DataFrame({
        "state":states,
        "preterm_rate":map_data[year]
    })

    fig_map = px.choropleth(
        state_df,
        locations="state",
        locationmode="USA-states",
        color="preterm_rate",
        scope="usa",
        color_continuous_scale="Reds",
        labels={"preterm_rate":"Preterm Birth Rate (%)"}
    )

    st.plotly_chart(fig_map,use_container_width=True)

    st.caption("Source: CDC maternal health surveillance.")

    st.markdown("""
**Insights**

Maternal health outcomes vary significantly by state, reflecting differences in healthcare access, socioeconomic conditions, and maternal health infrastructure.
""")

    # --------------------------------------------
    # ENTERPRISE FEATURE — STATE RANKING
    # --------------------------------------------

    st.subheader("State Ranking")

    ranking = state_df.sort_values("preterm_rate",ascending=False)

    st.dataframe(
        ranking.rename(columns={
            "state":"State",
            "preterm_rate":"Preterm Birth Rate (%)"
        }),
        use_container_width=True
    )

# --------------------------------------------------
# TAB 3 — COST CONTEXT
# --------------------------------------------------

with tab3:

    st.subheader("Neonatal Care Cost Context")

    cost_data = pd.DataFrame({
        "Category":[
            "Average Delivery Cost",
            "Preterm Birth Cost",
            "NICU Admission Cost"
        ],
        "Cost":[12000,35000,45000]
    })

    fig_cost = px.bar(
        cost_data,
        x="Category",
        y="Cost",
        color="Category",
        template="plotly_white"
    )

    fig_cost.update_layout(showlegend=False)

    st.plotly_chart(fig_cost,use_container_width=True)

    st.caption("Source: March of Dimes neonatal healthcare cost research.")

    st.markdown("""
**Insights**

Neonatal intensive care admissions represent one of the largest cost drivers in maternal healthcare. Programs focused on reducing preterm birth and improving prenatal care access can significantly reduce neonatal healthcare expenditures.
""")

st.divider()

st.caption("Digital Deregulated Labs | Maternal Health Outcomes Intelligence Platform")
