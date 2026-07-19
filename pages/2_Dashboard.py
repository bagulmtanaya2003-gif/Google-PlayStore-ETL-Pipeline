import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configure Streamlit page settings
st.set_page_config(
    page_title="Google Play Store Dashboard",
    page_icon="📊",
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
    st.title("Google Play Store Analytics")

    # Display project description
    st.write("Interactive Machine Learning Dashboard")

    # Display trained model information
    st.success("Random Forest Regressor")

    st.divider()

    # Dashboard filters
    st.subheader("🎛 Dashboard Filters")



# Load cleaned dataset
df = pd.read_csv("playstore_clean.csv")


# Category filter
selected_category = st.sidebar.multiselect(
    "Select Category",
    sorted(df["Category"].dropna().unique()),
    default=sorted(df["Category"].dropna().unique())
)

# Type filter
selected_type = st.sidebar.multiselect(
    "Select App Type",
    sorted(df["Type"].dropna().unique()),
    default=sorted(df["Type"].dropna().unique())
)


# Apply filters
filtered_df = df[
    (df["Category"].isin(selected_category)) &
    (df["Type"].isin(selected_type))
]


# Display main dashboard heading
st.title("📊 Google Play Store Analytics Dashboard")


# Dashboard description
st.markdown("""
Analyze Google Play Store applications using interactive visualizations,
business insights and machine learning.

Use the filters from the sidebar to explore different categories and app types.
""")


st.divider()


# Calculate key performance indicators
total_apps = len(filtered_df)

avg_rating = round(
    filtered_df["Rating"].mean(),
    2
)

total_reviews = int(
    filtered_df["Reviews"].sum()
)

categories = filtered_df["Category"].nunique()

free_apps = len(
    filtered_df[
        filtered_df["Type"] == "Free"
    ]
)

paid_apps = len(
    filtered_df[
        filtered_df["Type"] == "Paid"
    ]
)


# Create KPI cards
col1, col2, col3 = st.columns(3)

with col1:

    # Display total number of applications
    st.metric(
        "📱 Total Apps",
        total_apps
    )

with col2:

    # Display average application rating
    st.metric(
        "⭐ Average Rating",
        avg_rating
    )

with col3:

    # Display total reviews
    st.metric(
        "📝 Total Reviews",
        f"{total_reviews:,}"
    )


# Create second KPI row
col4, col5, col6 = st.columns(3)

with col4:

    # Display total categories
    st.metric(
        "📂 Categories",
        categories
    )

with col5:

    # Display free applications
    st.metric(
        "🆓 Free Apps",
        free_apps
    )

with col6:

    # Display paid applications
    st.metric(
        "💰 Paid Apps",
        paid_apps
    )


st.divider()


# Business insights
st.info(
"""
💡 Dashboard Insights

• Use filters to analyze specific categories.

• Compare Free vs Paid applications.

• Identify highly rated categories.

• Discover install trends across the Play Store.
"""
)

# Create first row for charts
col1, col2 = st.columns(2)


with col1:

    # Display rating distribution chart
    st.subheader("⭐ Rating Distribution")

    fig, ax = plt.subplots(
        figsize=(7,5)
    )

    ax.hist(
        filtered_df["Rating"],
        bins=20,
        edgecolor="black"
    )

    ax.set_xlabel(
        "Rating"
    )

    ax.set_ylabel(
        "Number of Applications"
    )

    ax.set_title(
        "Distribution of App Ratings"
    )

    ax.grid(
        alpha=0.3
    )

    st.pyplot(fig)

    st.caption(
        "Most applications have ratings between 4.0 and 4.5."
    )


with col2:

    # Display free and paid application comparison
    st.subheader("💰 Free vs Paid Applications")

    type_count = (
        filtered_df["Type"]
        .value_counts()
    )

    fig, ax = plt.subplots(
        figsize=(7,5)
    )

    ax.pie(
        type_count,
        labels=type_count.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title(
        "Application Type Distribution"
    )

    st.pyplot(fig)

    st.caption(
        "Free applications dominate the Google Play Store."
    )


st.divider()


# Create second row for charts
col1, col2 = st.columns(2)


with col1:

    # Display top application categories
    st.subheader("📂 Top 10 Categories")

    top_category = (
        filtered_df["Category"]
        .value_counts()
        .head(10)
    )

    fig, ax = plt.subplots(
        figsize=(8,5)
    )

    ax.barh(
        top_category.index,
        top_category.values
    )

    ax.set_xlabel(
        "Number of Applications"
    )

    ax.set_title(
        "Most Popular Categories"
    )

    ax.grid(
        alpha=0.3
    )

    st.pyplot(fig)

    st.caption(
        "These categories contain the highest number of applications."
    )


with col2:

    # Display categories with highest installs
    st.subheader("🚀 Top Categories by Installs")

    installs = (
        filtered_df
        .groupby("Category")["Installs"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
    )

    fig, ax = plt.subplots(
        figsize=(8,5)
    )

    ax.bar(
        installs.index,
        installs.values
    )

    plt.xticks(
        rotation=45,
        ha="right"
    )

    ax.set_ylabel(
        "Total Installs"
    )

    ax.set_title(
        "Highest Installed Categories"
    )

    ax.grid(
        alpha=0.3
    )

    st.pyplot(fig)

    st.caption(
        "These categories generate the highest install counts."
    )


st.divider()


# Dashboard insights section
st.subheader("📈 Key Insights")

col1, col2 = st.columns(2)

with col1:

    st.success("""
✅ Most apps belong to the Family and Games categories.

✅ Free applications are significantly more common than paid apps.

✅ Average application ratings remain above 4.0.

""")

with col2:

    st.info("""
📌 Businesses should focus on high-performing categories.

📌 Ratings strongly influence application popularity.

📌 Install trends reveal customer preferences.

""")

st.divider()

# Add separator before dataset section
st.divider()


# Dataset statistics section
st.subheader("📈 Dataset Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Highest Rating",
        round(filtered_df["Rating"].max(), 2)
    )


with col2:

    st.metric(
        "Lowest Rating",
        round(filtered_df["Rating"].min(), 2)
    )


with col3:

    st.metric(
        "Maximum Installs",
        f"{int(filtered_df['Installs'].max()):,}"
    )


with col4:

    st.metric(
        "Average Reviews",
        f"{int(filtered_df['Reviews'].mean()):,}"
    )


st.divider()


# Dataset preview section
st.subheader("📄 Clean Dataset Preview")


st.markdown("""
Explore the cleaned Google Play Store dataset used for
analysis and machine learning.
""")


with st.expander("📂 View Dataset"):

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=400
    )


st.download_button(

    label="📥 Download Clean Dataset",

    data=filtered_df.to_csv(index=False),

    file_name="playstore_clean.csv",

    mime="text/csv"
)


st.divider()


# Project summary section
st.subheader("📋 Dashboard Summary")


st.success("""

✔ Interactive KPI Dashboard

✔ Dynamic Category Filters

✔ Rating Distribution Analysis

✔ Free vs Paid Comparison

✔ Category-wise Install Analysis

✔ Clean Dataset Preview

✔ CSV Download Support

""")


st.info("""

### 💡 Business Recommendation

• Focus on categories with higher average ratings.

• Improve application quality to increase installs.

• Monitor customer reviews for better engagement.

• Free applications attract significantly more users.

""")


st.divider()


# Footer section

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;'>

### 📱 Google Play Store Analytics Dashboard

End-to-End Data Analytics & Machine Learning Project

Developed using ❤️ Python | Pandas | SQL | Machine Learning | Streamlit

</div>
""",
unsafe_allow_html=True
)