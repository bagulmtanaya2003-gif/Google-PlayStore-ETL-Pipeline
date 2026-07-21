import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff


# Configure Streamlit page settings
st.set_page_config(
    page_title="Data Analysis",
    page_icon="📈",
    layout="wide"
)

# Sidebar section for project branding and information
with st.sidebar:

# Display project logo
    st.image(
        "https://cdn-icons-png.flaticon.com/512/888/888879.png",
        width=80
    )

# Display project title
    st.title("Google Play Store")

# Display project description
    st.write("Machine Learning Project")

# Display model information
    st.success("Random Forest Model")



# Display page title
st.title("📈 Exploratory Data Analysis")


# Explain purpose of analysis page
st.markdown("""
This section performs exploratory data analysis on Google Play Store applications.
It analyzes ratings, categories, reviews, pricing, application size and relationships
between different features.
""")

# Load cleaned dataset
df = pd.read_csv("playstore_clean.csv")

# Calculate dataset information
rows = df.shape[0]
columns = df.shape[1]

missing_values = int(
    df.isnull().sum().sum()
)

duplicates = int(
    df.duplicated().sum()
)

# Dataset overview section
st.subheader("📊 Dataset Overview")

# Create information cards
col1, col2, col3, col4 = st.columns(4)

with col1:

# Display total rows
    st.metric(
        "Total Records",
        rows
    )

with col2:

# Display total columns
    st.metric(
        "Features",
        columns
    )

with col3:

# Display missing values
    st.metric(
        "Missing Values",
        missing_values
    )

with col4:

# Display duplicate records
    st.metric(
        "Duplicate Rows",
        duplicates
    )

st.divider()

# Rating distribution analysis
st.subheader("⭐ Distribution of App Ratings")

fig = px.histogram(
    df,
    x="Rating",
    nbins=20,
    title="Distribution of Application Ratings",
    labels={
        "Rating":"App Rating"
    }
)

# Display interactive histogram
st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()

# Top categories analysis
st.subheader("📂 Top 10 Google Play Store Categories")

category = (
    df["Category"]
    .value_counts()
    .head(10)
    .reset_index()
)

category.columns = [
    "Category",
    "Applications"
]

fig = px.bar(
    category,
    x="Category",
    y="Applications",
    text="Applications",
    title="Top Categories Based on Number of Applications"
)

# Show values on bars
fig.update_traces(
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()

# Reviews and rating relationship

st.subheader("📝 Reviews vs Rating Relationship")

fig = px.scatter(
    df,
    x="Reviews",
    y="Rating",
    title="Relationship Between Reviews and App Ratings",
    labels={
        "Reviews":"Number of Reviews",
        "Rating":"App Rating"
    },
    hover_data=[
        "App",
        "Category"
    ]
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()

# App size and rating relationship
st.subheader("📦 App Size vs Rating")

fig = px.scatter(
    df,
    x="Size",
    y="Rating",
    title="Impact of Application Size on Rating",
    labels={
        "Size":"App Size (MB)",
        "Rating":"Rating"
    },
    hover_data=[
        "App"
    ]
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()

# Free and paid application comparison
st.subheader("💰 Free vs Paid Applications")

type_count = (
    df["Type"]
    .value_counts()
    .reset_index()
)

type_count.columns=[
    "Type",
    "Count"
]

fig = px.pie(
    type_count,
    names="Type",
    values="Count",
    title="Distribution of Free and Paid Applications",
    hole=0.4
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()

# Price distribution analysis

st.subheader("💲 Price Distribution")

fig = px.histogram(
    df,
    x="Price",
    nbins=20,
    title="Distribution of Application Prices"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# Correlation heatmap
st.subheader("🔥 Feature Correlation Heatmap")

corr = df.corr(
    numeric_only=True
)

fig = ff.create_annotated_heatmap(
    z=corr.values,
    x=list(corr.columns),
    y=list(corr.columns),
    annotation_text=corr.round(2).values,
    colorscale="Viridis"
)

fig.update_layout(
    title="Correlation Between Numerical Features",
    height=600
)

# Display heatmap with correlation values
st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()

# Dataset preview section
st.subheader("📄 Clean Dataset")

with st.expander("View Dataset Preview"):

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

# Footer section

st.divider()
st.caption(
    "Developed using Python • Data Analysis • Machine Learning • Streamlit"
)