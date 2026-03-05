import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.title("Postnatal Care Indicators")

st.markdown("""
Postnatal indicators reflect maternal recovery, mental health support, and workforce reintegration following childbirth.
""")

data = pd.DataFrame({
    "Indicator": [
        "Postpartum Mental Health Support",
        "Return to Work Readiness",
        "Employee Retention Likelihood"
    ],
    "Rate": [33, 68, 74]
})

fig = go.Figure()

fig.add_trace(go.Bar(
    x=data["Indicator"],
    y=data["Rate"],
    marker_color=["#E91E63", "#673AB7", "#9C27B0"]
))

fig.update_layout(
    template="plotly_dark",
    yaxis_title="Percent",
    xaxis_title="Postnatal Indicator"
)

st.plotly_chart(fig, use_container_width=True)

st.caption("Source: Maven Clinic employer maternal health outcomes reporting.")
