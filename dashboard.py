import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(
    page_title="Maternal Care Intelligence Platform",
    layout="wide"
)

st.title("Maternal Care Population Intelligence Platform")

st.markdown(
"""
Synthetic population analytics dashboard modeling maternal health
program performance, clinical outcomes, operational efficiency,
and payer ROI.
"""
)

# Load dataset
df = pd.read_csv("maternal_population_data.csv")

# ================================
# TRAIN RISK MODEL
# ================================

features = df[
    [
        "age",
        "gestational_diabetes",
        "hypertension",
        "therapy_sessions",
        "nutrition_visits",
        "messages_sent",
        "response_time_hours",
        "no_show"
    ]
]

target = df["preterm_birth"]

X_train, X_test, y_train, y_test = train_test_split(
    features,
    target,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

# ================================
# KPI PANEL
# ================================

st.header("Program Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patients", len(df))
col2.metric("High Risk Pregnancies", df[df["risk_level"]=="high"].shape[0])
col3.metric("Preterm Births", df["preterm_birth"].sum())
col4.metric("NICU Admissions", df["nicu_admission"].sum())

st.divider()

# ================================
# TABS
# ================================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "Population Risk",
        "Clinical Outcomes",
        "Care Operations",
        "Cost Analytics",
        "Payer ROI Simulator",
        "AI Risk Prediction"
    ]
)

# ================================
# POPULATION RISK
# ================================

with tab1:

    st.subheader("Pregnancy Risk Distribution")

    fig = px.histogram(
        df,
        x="risk_level",
        color="risk_level"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Patient Engagement by Age")

    fig = px.scatter(
        df,
        x="age",
        y="messages_sent",
        color="risk_level"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Cost of Care by Risk Tier")

    fig = px.box(
        df,
        x="risk_level",
        y="cost_of_care",
        color="risk_level"
    )

    st.plotly_chart(fig, use_container_width=True)

# ================================
# CLINICAL OUTCOMES
# ================================

with tab2:

    st.subheader("Outcome Rates by Risk Tier")

    outcomes = df.groupby("risk_level")[["preterm_birth","nicu_admission"]].mean().reset_index()

    fig = px.bar(
        outcomes,
        x="risk_level",
        y=["preterm_birth","nicu_admission"],
        barmode="group"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Preterm Birth Distribution")

    fig = px.histogram(
        df,
        x="preterm_birth"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("NICU Admissions")

    fig = px.histogram(
        df,
        x="nicu_admission"
    )

    st.plotly_chart(fig, use_container_width=True)

# ================================
# CARE OPERATIONS
# ================================

with tab3:

    st.subheader("Response Time by Risk Level")

    fig = px.box(
        df,
        x="risk_level",
        y="response_time_hours",
        color="risk_level"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Appointment No-Show Rate")

    fig = px.histogram(
        df,
        x="no_show"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Patient Messaging Volume")

    fig = px.histogram(
        df,
        x="messages_sent"
    )

    st.plotly_chart(fig, use_container_width=True)

# ================================
# COST ANALYTICS
# ================================

with tab4:

    st.subheader("Cost of Care Distribution")

    fig = px.histogram(
        df,
        x="cost_of_care"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Average Cost by Risk Tier")

    avg_cost = df.groupby("risk_level")["cost_of_care"].mean().reset_index()

    fig = px.bar(
        avg_cost,
        x="risk_level",
        y="cost_of_care",
        color="risk_level"
    )

    st.plotly_chart(fig, use_container_width=True)

# ================================
# ROI SIMULATOR
# ================================

with tab5:

    st.subheader("Payer ROI Simulator")

    members = st.slider(
        "Pregnant Members Enrolled",
        100,
        10000,
        2000
    )

    nicu_rate = df["nicu_admission"].mean()

    nicu_cost = 45000

    estimated_nicu_cases = members * nicu_rate

    estimated_nicu_cost = estimated_nicu_cases * nicu_cost

    estimated_savings = estimated_nicu_cost * 0.15

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Estimated NICU Cases",
        int(estimated_nicu_cases)
    )

    col2.metric(
        "Estimated NICU Cost",
        f"${int(estimated_nicu_cost):,}"
    )

    col3.metric(
        "Estimated Program Savings",
        f"${int(estimated_savings):,}"
    )

# ================================
# AI RISK PREDICTION
# ================================

with tab6:

    st.subheader("Maternal Risk Prediction Model")

    age = st.slider("Age",18,45,30)
    gdm = st.selectbox("Gestational Diabetes",[0,1])
    hypertension = st.selectbox("Hypertension",[0,1])
    therapy_sessions = st.slider("Therapy Sessions",0,10,1)
    nutrition_visits = st.slider("Nutrition Visits",0,10,2)
    messages = st.slider("Messages Sent",0,20,5)
    response_time = st.slider("Response Time (hours)",1,10,3)
    no_show = st.selectbox("Missed Appointments",[0,1])

    patient_data = pd.DataFrame(
        [[
            age,
            gdm,
            hypertension,
            therapy_sessions,
            nutrition_visits,
            messages,
            response_time,
            no_show
        ]],
        columns=features.columns
    )

    prediction = model.predict(patient_data)[0]
    probability = model.predict_proba(patient_data)[0][1]

    if prediction == 1:

        st.error(f"High Risk of Preterm Birth ({probability:.2%})")

    else:

        st.success(f"Low Risk of Preterm Birth ({probability:.2%})")

st.divider()

st.caption("Digital Deregulated Labs | Maternal Care Intelligence Demo")
