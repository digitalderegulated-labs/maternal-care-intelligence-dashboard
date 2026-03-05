import streamlit as st
import pandas as pd

st.title("Maternal Health Provider Landscape")

st.markdown("""
Overview of selected organizations providing maternity care services, fertility support, and maternal health platforms.
""")

providers = pd.DataFrame({
    "Company": [
        "Pomelo Care",
        "Maven Clinic",
        "Carrot Fertility",
        "Progyny",
        "Wildflower Health"
    ],
    "Primary Service": [
        "Virtual maternity care programs",
        "Women's health platform",
        "Global fertility benefits",
        "Fertility and maternity benefits",
        "Maternal care coordination technology"
    ]
})

st.dataframe(providers, use_container_width=True)

st.caption("Sources: Company websites and public program descriptions.")
