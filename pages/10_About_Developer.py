import streamlit as st

st.set_page_config(
    page_title="About Developer",
    page_icon="👩‍💻",
    layout="wide"
)

st.title("👩‍💻 About the Developer")

st.markdown("""
## Tanaya Bagul

Aspiring **Data Scientist** and **Data Analyst** with a strong interest in
Machine Learning, Data Analytics, SQL, Python, and Business Intelligence.

This project demonstrates an end-to-end ETL pipeline using the Google Play Store
dataset. It includes data cleaning, SQL integration, exploratory data analysis,
machine learning prediction, feature importance analysis, business insights,
and an interactive Streamlit dashboard.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("🛠️ Technical Skills")

    st.markdown("""
- Python
- SQL
- Machine Learning
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- MySQL
- Git & GitHub
""")

with col2:
    st.subheader("📌 Project")

    st.info("""
Google Play Store ETL Pipeline with Machine Learning

• Data Cleaning
• SQL Integration
• Data Analysis
• Prediction Model
• Feature Importance
• Business Insights
• Interactive Dashboard
""")

st.divider()

st.subheader("🔗 Connect with Me")

st.link_button(
    "💼 LinkedIn",
    "https://www.linkedin.com/in/tanaya-bagul-b21354285/"
)

st.link_button(
    "💻 GitHub",
    "https://github.com/bagulmtanaya2003-gif"
)

st.link_button(
    "📧 Email",
    "bagulmtanaya2003@gmail.com"
)

st.divider()

st.success("Thank you for visiting my project!")