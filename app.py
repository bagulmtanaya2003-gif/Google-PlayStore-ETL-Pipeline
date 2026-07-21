import streamlit as st


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Google Play Store Analytics",
    page_icon="📱",
    layout="wide"
)

# HOME PAGE

st.image(
    "https://cdn-icons-png.flaticon.com/512/888/888879.png",
    width=120
)

st.title("📱 Google Play Store Analytics")

st.subheader("End-to-End ETL Pipeline & Machine Learning Project")

st.write(
    """
    An interactive analytics platform designed to explore Google Play Store 
    application data, understand app performance factors, and generate 
    meaningful insights using data-driven approaches.
    """
)

st.divider()

st.subheader("🚀 Project Overview")

st.info(
    """
    This project focuses on analyzing real-world Google Play Store data 
    to discover patterns, trends, and factors that influence application success.

    It provides an interactive dashboard experience for exploring app insights
    and supporting better business decisions.
    """
)

st.divider()

st.subheader("🎯 Objective")

st.write(
    """
    ✓ Analyze Google Play Store applications using real-world data.

    ✓ Clean and preprocess raw datasets.

    ✓ Perform Exploratory Data Analysis (EDA).
    """
)

st.divider()

# FOOTER

st.caption("Developed by Tanaya Bagul | Data Analytics & Machine Learning Project")