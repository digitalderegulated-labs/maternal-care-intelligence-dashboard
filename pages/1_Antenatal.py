import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.title("Antenatal Care Indicators")

st.markdown("""
Antenatal care indicators describe prenatal care engagement and early screening for pregnancy-related risks.
""")

data = pd.DataFrame({
    "Indicator": [
        "Prenatal Care Engagement",
        "Pregnancy Risk Screening",
        "Gestational Diabetes Detection"
    ],
    "Rate": [85, 92, 15]
})

fig = go.Figure()

fig.add_trace(go.Bar(
    x=data["Indicator"],
    y=data["Rate"],
    marker_color=["#2E86AB", "#3CB371", "#F39C12"]
))

fig.update_layout(
    template="plotly_dark",
    yaxis_title="Percent",
    xaxis_title="Indicator"
)

st.plotly_chart(fig, use_container_width=True)

st.caption("Source: CDC prenatal care indicators and maternal health surveillance reports.")
