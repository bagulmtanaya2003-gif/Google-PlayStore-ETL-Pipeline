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
This page provides a quick guide to navigate and use the Google Play Store
Analytics dashboard.
""")

st.divider()


# How to use section
st.header("🚀 How to Use")

st.markdown("""

1. Open the **Home** page to understand the project.

2. Visit the **Dashboard** to explore KPIs and visualizations.

3. Use **Data Analysis** to understand application trends.

4. Open **Prediction** to predict app ratings.

5. Check **Business Insights** for key findings.

6. Explore the **ETL Pipeline** to understand data processing.

""")

st.divider()


# Troubleshooting section
st.header("⚠ Troubleshooting")

st.info("""

• Ensure all project files are in the correct folder.

• Verify that **playstore_clean.csv** is available.

• Install all required Python libraries before running the project.

• Restart the application if any page fails to load.

""")

st.divider()


# Technologies section
st.header("🛠 Technologies Used")

st.markdown("""

- Python

- SQL

- Pandas

- Matplotlib

- Scikit-Learn

- Streamlit

""")

st.divider()


# Footer section
st.caption(
    "Google Play Store Analytics | Help & Documentation"
)