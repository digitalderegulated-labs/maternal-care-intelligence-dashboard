import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.title("Maternity and Delivery Outcomes")

st.markdown("""
Indicators related to pregnancy outcomes and neonatal care utilization.
""")

data = pd.DataFrame({
    "Outcome": [
        "Preterm Birth Reduction",
        "NICU Admission Reduction",
        "Emergency Department Visit Reduction"
    ],
    "Improvement": [37, 58, 46]
})

fig = go.Figure()

fig.add_trace(go.Bar(
    x=data["Outcome"],
    y=data["Improvement"],
    marker_color=["#27AE60", "#3498DB", "#E67E22"]
))

fig.update_layout(
    template="plotly_dark",
    yaxis_title="Percent Improvement",
    xaxis_title="Clinical Outcome"
)

st.plotly_chart(fig, use_container_width=True)

st.caption("Source: Pomelo Care clinical outcomes publications.")
