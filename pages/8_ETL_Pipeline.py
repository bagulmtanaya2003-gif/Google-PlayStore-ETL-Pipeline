import streamlit as st

# Configure Streamlit page settings
st.set_page_config(
    page_title="ETL Pipeline",
    page_icon="⚙️",
    layout="wide"
)


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
    st.success("ETL Pipeline")

    st.divider()

    st.info("""
📌 End-to-End Data Analytics

• Extract

• Transform

• Load

• Machine Learning

• Dashboard
""")


# Display page heading
st.title("⚙️ ETL Pipeline")

st.markdown("""
### End-to-End Data Processing Workflow
""")

st.info("""
This page explains how raw Google Play Store data is converted into
clean, structured information and finally used to build a Machine Learning
model and interactive dashboard.
""")

st.divider()


# ETL overview section
st.header("📖 ETL Overview")

st.markdown("""

ETL stands for **Extract, Transform and Load**.

It is a process used to collect raw data, clean and transform it into
a structured format, and make it ready for analysis and Machine Learning.

""")

st.divider()


# Extract section
st.header("📥 Extract")

left, right = st.columns([2,1])

with left:

    st.markdown("""

### Data Source

The project uses the **Google Play Store Dataset** containing information
about Android applications.

The extracted dataset includes:

- Application Name

- Category

- Rating

- Reviews

- Installs

- Size

- Price

- Content Rating

- Genres

""")

with right:

    st.success("""

### Extract Output

✔ CSV Dataset

✔ Raw Data

✔ 10,000+ Applications

✔ Multiple Categories

""")

st.divider()


# Dataset information
st.header("📊 Raw Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Source",
        "CSV File"
    )

with col2:

    st.metric(
        "Dataset",
        "Google Play Store"
    )

with col3:

    st.metric(
        "Status",
        "Raw Data"
    )

st.divider()

# Transform section
st.header("🔄 Transform")

st.markdown("""
The extracted raw dataset is cleaned and transformed before analysis
and Machine Learning. This ensures better data quality and reliable results.
""")

col1, col2 = st.columns(2)

with col1:

    st.info("""

### Data Cleaning

✔ Removed missing values

✔ Removed duplicate records

✔ Corrected data types

✔ Standardized column values

✔ Handled inconsistent data

""")

with col2:

    st.info("""

### Feature Engineering

✔ Converted installs to numeric values

✔ Converted price to numeric

✔ Converted reviews to integer

✔ Created clean dataset

✔ Prepared data for ML

""")

st.divider()


# Data transformation workflow
st.header("📊 Data Transformation Workflow")

st.code("""

Raw CSV Dataset

        │

        ▼

Remove Missing Values

        │

        ▼

Remove Duplicate Records

        │

        ▼

Convert Data Types

        │

        ▼

Feature Engineering

        │

        ▼

Clean Dataset

""")

st.divider()


# Load section
st.header("📤 Load")

left, right = st.columns([2,1])

with left:

    st.markdown("""

After preprocessing, the cleaned dataset is stored for
analysis and Machine Learning.

The processed data is:

• Ready for SQL

• Ready for Visualization

• Ready for Machine Learning

• Ready for Business Analysis

""")

with right:

    st.success("""

### Load Output

✔ Clean Dataset

✔ SQL Database

✔ Dashboard

✔ ML Ready Data

""")

st.divider()


# Machine Learning pipeline
st.header("🤖 Machine Learning Pipeline")

st.markdown("""

The cleaned dataset is used to train a Machine Learning model
for predicting application ratings.

""")

col1, col2, col3 = st.columns(3)

with col1:

    st.success("""

### Input

✔ Clean Dataset

✔ Features

✔ Target Variable

""")

with col2:

    st.success("""

### Model

🌳 Random Forest

Training

Prediction

Evaluation

""")

with col3:

    st.success("""

### Output

Predicted Rating

Performance Metrics

Business Insights

""")

st.divider()

# End-to-End workflow section
st.header("🔁 End-to-End Workflow")

st.markdown("""
The following workflow illustrates the complete lifecycle of the project,
starting from raw data collection to business insights generation.
""")

st.code("""

Google Play Store Dataset
            │
            ▼
        Data Extraction
            │
            ▼
       Data Cleaning
            │
            ▼
    Data Transformation
            │
            ▼
   Exploratory Data Analysis
            │
            ▼
    Feature Engineering
            │
            ▼
 Machine Learning Model
(Random Forest Regressor)
            │
            ▼
 Rating Prediction
            │
            ▼
 Business Insights
            │
            ▼
 Streamlit Dashboard

""")

st.divider()


# Technology stack section
st.header("🛠 Technology Stack")

col1, col2 = st.columns(2)

with col1:

    st.success("""

### Programming

🐍 Python

🗄 SQL

🐼 Pandas

🔢 NumPy

""")

    st.success("""

### Visualization

📊 Matplotlib

📈 Streamlit

""")

with col2:

    st.info("""

### Machine Learning

🌳 Random Forest

📉 Model Evaluation

Feature Engineering

""")

    st.info("""

### Development

💻 VS Code

🐙 GitHub

CSV Dataset

""")


st.divider()


# Business benefits section
st.header("💼 Business Benefits")

col1, col2 = st.columns(2)

with col1:

    st.success("""

✔ Understand App Performance

✔ Discover Popular Categories

✔ Analyze User Ratings

✔ Compare Free vs Paid Apps

""")


with col2:

    st.success("""

✔ Support Business Decisions

✔ Improve Marketing Strategy

✔ Predict Future Ratings

✔ Identify Growth Opportunities

""")

st.divider()


# Project outcome section
st.header("🏆 Project Outcome")

st.markdown("""

The ETL pipeline successfully converts raw Google Play Store data into
a clean and structured dataset suitable for analysis and Machine Learning.

### Final Deliverables

✅ Clean Dataset

✅ SQL Database

✅ Interactive Dashboard

✅ Machine Learning Prediction

✅ Business Insights

""")


st.divider()


# Key learnings section
st.header("📚 Key Learnings")

st.info("""

During this project, the following skills were applied:

• Data Collection

• Data Cleaning

• SQL

• Exploratory Data Analysis

• Feature Engineering

• Machine Learning

• Dashboard Development

• Business Analytics

""")


st.divider()


# Footer section
st.markdown("---")

st.markdown(
"""
<div style="text-align:center;">

## ⚙️ ETL Pipeline

Google Play Store Analytics using Machine Learning

Developed using

<b>Python | SQL | Pandas | Scikit-Learn | Streamlit</b>

⭐ End-to-End Data Analytics Workflow ⭐

</div>
""",
unsafe_allow_html=True
)