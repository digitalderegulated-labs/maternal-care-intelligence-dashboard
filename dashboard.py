import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Maternal Care Intelligence Dashboard", layout="wide")

st.title("Maternal Care Population Intelligence Dashboard")

st.markdown("Synthetic dataset modeling maternal care outcomes, operational metrics, and population risk.")

df = pd.read_csv("maternal_population_data.csv")

# KPI CARDS
col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Patients", len(df))
col2.metric("High Risk Pregnancies", df[df["risk_level"]=="high"].shape[0])
col3.metric("Preterm Births", df["preterm_birth"].sum())
col4.metric("NICU Admissions", df["nicu_admission"].sum())

st.divider()

tab1,tab2,tab3,tab4 = st.tabs(["Risk Distribution","Outcomes","Operations","Cost"])

with tab1:

    fig = px.histogram(
        df,
        x="risk_level",
        title="Pregnancy Risk Distribution"
    )

    st.plotly_chart(fig,use_container_width=True)

    fig = px.scatter(
        df,
        x="age",
        y="messages_sent",
        color="risk_level",
        title="Patient Engagement by Age"
    )

    st.plotly_chart(fig,use_container_width=True)

with tab2:

    fig = px.histogram(
        df,
        x="preterm_birth",
        title="Preterm Births"
    )

    st.plotly_chart(fig,use_container_width=True)

    fig = px.histogram(
        df,
        x="nicu_admission",
        title="NICU Admissions"
    )

    st.plotly_chart(fig,use_container_width=True)

with tab3:

    fig = px.box(
        df,
        x="risk_level",
        y="response_time_hours",
        title="Response Time by Risk Level"
    )

    st.plotly_chart(fig,use_container_width=True)

    fig = px.histogram(
        df,
        x="no_show",
        title="Appointment No Shows"
    )

    st.plotly_chart(fig,use_container_width=True)

with tab4:

    fig = px.box(
        df,
        x="risk_level",
        y="cost_of_care",
        title="Cost of Care by Risk Level"
    )

    st.plotly_chart(fig,use_container_width=True)

st.caption("Digital Deregulated Labs | Maternal Care Intelligence Demo")
