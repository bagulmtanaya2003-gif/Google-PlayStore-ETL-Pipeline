import streamlit as st

# Configure Streamlit page settings
st.set_page_config(
    page_title="Help",
    page_icon="❓",
    layout="wide"
)


# Sidebar section
with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/888/888879.png",
        width=85
    )

    st.title("Google Play Store")

    st.write("Machine Learning Project")

    st.success("Help")


# Display page heading
st.title("❓ Help & User Guide")

st.markdown("""
Welcome to the **Google Play Store Analytics Dashboard**.

This page provides a quick overview of how to navigate and use each module of the project.
""")

st.divider()


# Navigation guide section
st.header("🧭 Project Navigation")

col1, col2 = st.columns(2)

with col1:

    st.success("""
### Main Pages

🏠 Home

📊 Dashboard

📈 Data Analysis

🤖 Prediction

⭐ Model Performance

""")

with col2:

    st.info("""
### Additional Pages

💼 Business Insights

⚙️ ETL Pipeline

📥 Download Report

👩‍💻 About Developer

""")


st.divider()


# How to use section
st.header("🚀 How to Use")

st.markdown("""

**Step 1:** Start with the **Home** page to understand the project.

**Step 2:** Open the **Dashboard** to explore KPIs and visualizations.

**Step 3:** Visit **Data Analysis** to identify trends and patterns.

**Step 4:** Use **Prediction** to estimate application ratings.

**Step 5:** Review **Model Performance** to evaluate the Machine Learning model.

**Step 6:** Explore **Business Insights** and **ETL Pipeline** for business recommendations and data workflow.

""")


st.divider()


# Project features section
st.header("✨ Project Features")

st.markdown("""

✅ Interactive Dashboard

✅ Data Analysis

✅ Machine Learning Prediction

✅ Model Performance Evaluation

✅ Business Insights

✅ ETL Workflow

✅ Clean Dataset Download

""")


st.divider()


# Technologies section
st.header("🛠 Technologies Used")

col1, col2 = st.columns(2)

with col1:

    st.success("""
• Python

• SQL

• Pandas

• NumPy

""")

with col2:

    st.info("""
• Matplotlib

• Scikit-Learn

• Streamlit

• GitHub

""")


st.divider()


# Need help section
st.header("📌 Need Assistance?")

st.info("""
If a page does not load correctly, verify that all required project files,
including the cleaned dataset and trained model, are available in the project directory.
""")


st.divider()


# Footer section
st.caption(
    "Google Play Store Analytics using Machine Learning | Help & Documentation"
)