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

    st.success("Help & User Guide")


# Display page heading
st.title("❓ Help & User Guide")

st.markdown("""
Welcome to the **Google Play Store Analytics using Machine Learning** project.

This guide provides a quick overview of the available modules and how to navigate through the application.
""")

st.divider()


# Project modules
st.header("📂 Project Modules")

col1, col2 = st.columns(2)

with col1:

    st.success("""
### Analytics

🏠 Home

📊 Dashboard

📈 Data Analysis

🤖 Prediction

⭐ Model Performance
""")

with col2:

    st.info("""
### Documentation

💼 Business Insights

⚙️ ETL Pipeline

📥 Download Report

👨‍💻 About Developer
""")

st.divider()


# Workflow section
st.header("🚀 Recommended Workflow")

st.markdown("""

**1️⃣ Home** → Understand the project objective.

**2️⃣ Dashboard** → Explore KPIs and interactive charts.

**3️⃣ Data Analysis** → Discover trends and patterns.

**4️⃣ Prediction** → Predict app ratings using the trained ML model.

**5️⃣ Model Performance** → Evaluate the model using performance metrics.

**6️⃣ Business Insights** → Review key business recommendations.

**7️⃣ ETL Pipeline** → Understand the complete data processing workflow.

""")

st.divider()


# Features section
st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:

    st.success("""
✔ Interactive Dashboard

✔ Exploratory Data Analysis

✔ Machine Learning Prediction

✔ Model Performance Evaluation
""")

with col2:

    st.success("""
✔ Business Insights

✔ ETL Workflow

✔ Download Clean Dataset

✔ User-Friendly Interface
""")

st.divider()


# Technologies
st.header("🛠 Technology Stack")

st.markdown("""

- 🐍 Python

- 🗄 SQL

- 🐼 Pandas

- 🔢 NumPy

- 📊 Matplotlib

- 🤖 Scikit-Learn

- 📈 Streamlit

- 🐙 Git & GitHub

""")

st.divider()


# Tips section
st.header("💡 Tips")

st.info("""

• Start with the Home page before exploring other modules.

• Use the Dashboard to interact with charts and KPIs.

• Visit Model Performance to understand prediction quality.

• Explore ETL Pipeline to see how raw data is transformed into business insights.

""")

st.divider()


# Footer section
st.markdown("---")

st.markdown(
"""
<div style="text-align:center;">

### Google Play Store Analytics using Machine Learning

Help & Documentation

Python | SQL | Machine Learning | Streamlit

</div>
""",
unsafe_allow_html=True
)