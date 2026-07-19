import streamlit as st

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="Resources",
    page_icon="📚",
    layout="wide"
)

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/888/888879.png",
        width=80
    )

    st.title("Google Play Store")

    st.success("📚 Project Resources")

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title("📚 Project Resources")

st.markdown("""
This page provides useful information about the project,
technologies used, ETL workflow and Machine Learning model.
""")

st.divider()

# ----------------------------------------------------
# Dataset
# ----------------------------------------------------

st.subheader("📊 Dataset")

st.info("""
Dataset Used

• Google Play Store Apps Dataset

Source

• Kaggle

Records

• 10,000+ Applications

Purpose

• Analyze app performance and predict install potential.
""")

# ----------------------------------------------------
# Technology Stack
# ----------------------------------------------------

st.subheader("🛠 Technology Stack")

col1, col2 = st.columns(2)

with col1:

    st.success("""
Programming

✔ Python

✔ SQL

✔ Streamlit

✔ Pandas

✔ NumPy
""")

with col2:

    st.success("""
Machine Learning

✔ Scikit-learn

✔ Random Forest

✔ Label Encoding

✔ Joblib

✔ ReportLab
""")

st.divider()

# ----------------------------------------------------
# ETL Pipeline
# ----------------------------------------------------

st.subheader("🔄 ETL Pipeline")

st.markdown("""
### Extract

Collected Google Play Store dataset.

### Transform

• Removed missing values

• Cleaned inconsistent data

• Encoded categorical columns

• Feature Engineering

### Load

Processed data stored and used for Machine Learning prediction.
""")

st.divider()

# ----------------------------------------------------
# Machine Learning
# ----------------------------------------------------

st.subheader("🤖 Machine Learning Model")

st.info("""
Algorithm

Random Forest Classifier

Purpose

Predict whether an application has High Install Potential
or Low Install Potential based on application features.
""")

st.divider()

# ----------------------------------------------------
# Prediction Report
# ----------------------------------------------------

st.subheader("📄 Prediction Report")

st.success("""
A professional PDF report is generated automatically
from the Prediction page.

The report contains:

✔ Application Details

✔ Prediction Result

✔ Model Confidence

✔ AI Explanation

✔ Business Recommendations

✔ Report Generation Date
""")

st.divider()

# ----------------------------------------------------
# Project Features
# ----------------------------------------------------

st.subheader("✨ Project Features")

c1, c2 = st.columns(2)

with c1:

    st.markdown("""
✅ Interactive Dashboard

✅ Data Visualization

✅ Exploratory Data Analysis

✅ Machine Learning Prediction
""")

with c2:

    st.markdown("""
✅ PDF Report Generation

✅ Business Insights

✅ Streamlit Interface

✅ Professional UI
""")

st.divider()

# ----------------------------------------------------
# Footer
# ----------------------------------------------------

st.caption(
    "Google Play Store ETL Pipeline | Python | SQL | Machine Learning | Streamlit"
)