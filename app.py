import streamlit as st
import pandas as pd

# Configure Streamlit page settings
st.set_page_config(
    page_title="Google Play Store Analytics",
    page_icon="📱",
    layout="wide"
)


# Load cleaned dataset
df = pd.read_csv("playstore_clean.csv")


# Sidebar section for project branding and information
with st.sidebar:

    # Display project logo image
    st.image(
        "https://cdn-icons-png.flaticon.com/512/888/888879.png",
        width=85
    )

    # Display project title
    st.title("Google Play Store")

    # Display project description
    st.write("Machine Learning Project")

    # Display trained model information
    st.success("Random Forest Model")

    st.divider()

    st.subheader("📌 Project Pages")

    st.write("🏠 Home")
    st.write("📊 Dashboard")
    st.write("📈 Data Analysis")
    st.write("🤖 Prediction")
    st.write("⭐ Feature Importance")
    st.write("💼 Business Insights")
    st.write("⚙ ETL Pipeline")
    st.write("📄 Download Report")
    st.write("👨‍💻 About Developer")
    st.write("❓ Help")


# Display main heading
st.title("📱 Google Play Store Analytics using Machine Learning")

st.markdown("""
### Transforming App Store Data into Business Insights
""")

st.info("""
This project analyzes Google Play Store applications to identify the key
factors influencing app success. It combines Data Analytics, Machine Learning,
SQL, and interactive visualization to help understand application performance
and support data-driven decision making.
""")

# Display project banner image
st.image(
    "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1400",
    use_container_width=True
)

st.divider()


# Business problem section
st.header("🎯 Business Problem")

left, right = st.columns([2,1])

with left:

    st.markdown("""
The Google Play Store contains millions of applications across different
categories. Developers and businesses often struggle to understand what makes
an application successful.

This project addresses the following business questions:

- Which categories have the highest number of applications?
- What factors influence application ratings?
- Which app types receive more installs?
- Can Machine Learning predict application ratings?
- How can businesses use data to improve app performance?
""")

with right:

    st.success("""
### Project Goal

✔ Analyze App Performance

✔ Discover Hidden Patterns

✔ Build Prediction Model

✔ Generate Business Insights

✔ Support Better Decisions
""")


st.divider()


# Project objective section
st.header("🎯 Project Objectives")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### 📊 Data Analysis

• Clean raw dataset

• Perform exploratory analysis

• Understand rating trends

• Compare app categories
""")


with col2:

    st.info("""
### 🤖 Machine Learning

• Prepare training data

• Train Random Forest Model

• Predict application ratings

• Evaluate model performance
""")

st.divider()

# Solution workflow section
st.header("⚙ Solution Workflow")

st.markdown("""
This project follows a complete Data Analytics and Machine Learning pipeline
to transform raw Google Play Store data into meaningful business insights.
""")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("""
### 📥 Extract

• Google Play Store Dataset

• CSV File

• Raw Application Data

""")

with col2:

    st.warning("""
### 🔄 Transform

• Data Cleaning

• Missing Value Handling

• Feature Engineering

• Data Preprocessing

""")

with col3:

    st.info("""
### 📤 Load

• Machine Learning Model

• Interactive Dashboard

• Business Insights

""")

st.divider()


# Dataset summary section
st.header("📊 Dataset Summary")

total_apps = len(df)

avg_rating = round(
    df["Rating"].mean(),
    2
)

categories = df["Category"].nunique()

total_reviews = int(
    df["Reviews"].sum()
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "📱 Total Apps",
        total_apps
    )

with col2:

    st.metric(
        "📂 Categories",
        categories
    )

with col3:

    st.metric(
        "⭐ Average Rating",
        avg_rating
    )

with col4:

    st.metric(
        "📝 Total Reviews",
        f"{total_reviews:,}"
    )

st.divider()


# Technology stack section
st.header("🛠 Technology Stack")

col1, col2 = st.columns(2)

with col1:

    st.success("""
### Programming

🐍 Python

🐼 Pandas

🔢 NumPy

🗄 SQL

""")

    st.success("""
### Visualization

📊 Matplotlib

📈 Streamlit

""")

with col2:

    st.info("""
### Machine Learning

🤖 Scikit-Learn

🌳 Random Forest

📉 Model Evaluation

""")

    st.info("""
### Development

💻 VS Code

🐙 GitHub

🗂 CSV Dataset

""")

st.divider()


# Project highlights section
st.header("✨ Project Highlights")

col1, col2 = st.columns(2)

with col1:

    st.success("""
✔ End-to-End Data Analytics Project

✔ Interactive Dashboard

✔ Machine Learning Prediction

✔ Feature Importance Analysis

""")

with col2:

    st.success("""
✔ Business Insights

✔ ETL Pipeline

✔ SQL Integration

✔ Professional Streamlit Application

""")

st.divider()

# Quick navigation section
st.header("🧭 Quick Navigation")

st.markdown("""
Explore different modules of the project using the navigation menu available
on the left sidebar.
""")

col1, col2, col3 = st.columns(3)

with col1:

    st.info("""
### 📊 Dashboard

• Interactive KPIs

• Visual Analysis

• Charts & Insights

""")


with col2:

    st.info("""
### 🤖 Prediction

• Predict App Rating

• Machine Learning

• Model Output

""")


with col3:

    st.info("""
### 💼 Business Insights

• Market Trends

• Recommendations

• Decision Support

""")

st.divider()


# Business impact section
st.header("💼 Business Impact")

col1, col2 = st.columns(2)

with col1:

    st.success("""
### 📈 Benefits for Developers

✔ Understand user preferences

✔ Improve application quality

✔ Increase ratings

✔ Analyze competitors

""")


with col2:

    st.success("""
### 🏢 Benefits for Businesses

✔ Make data-driven decisions

✔ Identify high-growth categories

✔ Improve market strategy

✔ Understand install patterns

""")

st.divider()


# Key outcomes section
st.header("🏆 Project Outcome")

st.markdown("""

This project successfully demonstrates an end-to-end Data Analytics and
Machine Learning workflow using real-world Google Play Store data.

### Achievements

✅ Cleaned and transformed raw data

✅ Performed Exploratory Data Analysis (EDA)

✅ Identified important business trends

✅ Built a Machine Learning prediction model

✅ Developed an interactive Streamlit dashboard

✅ Generated business insights for decision making

""")


st.divider()


# About project section
st.header("📌 About This Project")

st.info("""

This project showcases practical skills in:

• Python Programming

• SQL

• Data Cleaning

• Data Visualization

• Machine Learning

• Business Analytics

• Streamlit Dashboard Development

It is designed as a portfolio project to demonstrate the complete
Data Analytics workflow from raw data to business insights.

""")


st.divider()


# Footer section

st.markdown("---")

st.markdown(
"""
<div style="text-align:center;">

## 📱 Google Play Store Analytics using Machine Learning

End-to-End Data Analytics & Machine Learning Project

Developed using

<b>Python | Pandas | SQL | Scikit-Learn | Streamlit | Matplotlib</b>

⭐ Designed for Learning • Portfolio • Recruiter Demonstration ⭐

</div>
""",
unsafe_allow_html=True
)