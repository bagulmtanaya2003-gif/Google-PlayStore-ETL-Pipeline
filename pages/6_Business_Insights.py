import streamlit as st
import pandas as pd
import plotly.express as px


# Configure Streamlit page settings
st.set_page_config(
    page_title="Business Insights",
    page_icon="💼",
    layout="wide"
)



# Sidebar section for project branding and information

with st.sidebar:

    # Display project logo image
    st.image(
        "https://cdn-icons-png.flaticon.com/512/888/888879.png",
        width=80
    )

    # Display project title
    st.title("Google Play Store")

    # Display project description
    st.write("Machine Learning Project")

    # Display trained model information
    st.success("Random Forest Model")



# Display page heading
st.title("💼 Business Insights Dashboard")



# Explain purpose of business analysis

st.markdown("""
This dashboard provides business insights from Google Play Store data.
It identifies high-performing categories, user preferences and factors
that influence application success.
""")



# Load cleaned dataset

df = pd.read_csv(
    "playstore_clean.csv"
)



# Calculate KPI values

total_apps = len(df)


average_rating = round(
    df["Rating"].mean(),
    2
)


total_categories = df["Category"].nunique()


free_apps = len(
    df[df["Type"]=="Free"]
)


paid_apps = len(
    df[df["Type"]=="Paid"]
)



# KPI section

st.subheader("📊 Business Overview")


col1, col2, col3, col4 = st.columns(4)



with col1:

    # Display total applications
    st.metric(
        "📱 Total Applications",
        total_apps
    )



with col2:

    # Display average rating
    st.metric(
        "⭐ Average Rating",
        average_rating
    )



with col3:

    # Display number of categories
    st.metric(
        "📂 Categories",
        total_categories
    )



with col4:

    # Display application type ratio
    st.metric(
        "🆓 Free Apps",
        free_apps
    )



st.divider()



# Analyze categories based on installs

st.subheader(
    "🚀 Top 10 Categories by Total Installs"
)



top_installs = (

    df.groupby("Category")["Installs"]

    .sum()

    .sort_values(
        ascending=False
    )

    .head(10)

    .reset_index()

)



fig = px.bar(

    top_installs,

    x="Category",

    y="Installs",

    text="Installs",

    title="Categories Generating Highest Number of Installs"

)



# Display install values on chart

fig.update_traces(

    texttemplate="%{text}",

    textposition="outside"

)



st.plotly_chart(

    fig,

    use_container_width=True

)



st.divider()



# Analyze categories based on rating

st.subheader(
    "⭐ Top Categories Based on Average Rating"
)



rating = (

    df.groupby("Category")["Rating"]

    .mean()

    .sort_values(
        ascending=False
    )

    .head(10)

    .reset_index()

)



fig = px.bar(

    rating,

    x="Category",

    y="Rating",

    text="Rating",

    title="Highest Rated Application Categories"

)



# Format rating values

fig.update_traces(

    texttemplate="%{text:.2f}",

    textposition="outside"

)



st.plotly_chart(

    fig,

    use_container_width=True

)



st.divider()



# Generate automatic business insights

st.subheader(
    "📌 Key Business Insights"
)



highest_install_category = (

    top_installs.iloc[0]["Category"]

)



highest_rating_category = (

    rating.iloc[0]["Category"]

)



col1, col2 = st.columns(2)



with col1:

    # Display highest install category insight
    st.success(
        f"""
        🚀 Highest Install Category

        {highest_install_category}
        """
    )



with col2:

    # Display highest rating category insight
    st.success(
        f"""
        ⭐ Highest Rated Category

        {highest_rating_category}
        """
    )



col3, col4 = st.columns(2)



with col3:

    # Display free application count
    st.info(
        f"🆓 Free Applications : {free_apps}"
    )



with col4:

    # Display paid application count
    st.info(
        f"💰 Paid Applications : {paid_apps}"
    )



st.divider()



# Business recommendations section

st.subheader(
    "💡 Business Recommendations"
)



recommendations = [

    "Focus on categories with higher installation demand.",

    "Maintain application ratings above 4.0 for better user trust.",

    "Increase user engagement through reviews and feedback.",

    "Optimize application size for better user experience.",

    "Regular updates improve application visibility.",

    "Free applications generally attract a larger user base."

]



for recommendation in recommendations:

    st.write(
        "✅ " + recommendation
    )



# Footer section

st.divider()


st.caption(
    "Developed using Python • Data Analytics • Machine Learning • Streamlit"
)