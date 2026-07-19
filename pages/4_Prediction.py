import streamlit as st
import pandas as pd
import joblib
import io
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Prediction | Google Play Store",
    page_icon="🎯",
    layout="wide"
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/888/888879.png",
        width=80
    )

    st.title("Google Play Store")

    st.write("Machine Learning Analytics")

    st.success("🎯 Prediction Module")

    st.divider()

    st.info(
        """
Predict App Success using

⭐ Rating

📊 Reviews

📱 Category

💾 Size

💰 Price

📅 Last Update
"""
    )

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main-title{
font-size:42px;
font-weight:bold;
text-align:center;
}

.subtitle{
text-align:center;
color:gray;
font-size:18px;
}

.card{

background:#f8f9fa;
padding:25px;
border-radius:15px;
border:1px solid #d9d9d9;

}

.result-card{

background:#eef7ff;
padding:25px;
border-radius:15px;
border:1px solid #99c2ff;

}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.markdown("""

<div class='main-title'>

🎯 Google Play Store Success Prediction

</div>

<div class='subtitle'>

Machine Learning based Application Install Prediction System

</div>

""", unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------
# Introduction
# ---------------------------------------------------

st.markdown("""

<div class="card">

<h3>📌 About Prediction System</h3>

This prediction system uses a trained
<b>Random Forest Machine Learning Model</b>
to estimate whether an application
has high install potential.

<br><br>

The prediction is based on:

<ul>

<li>⭐ Rating</li>

<li>📊 Reviews</li>

<li>📱 Category</li>

<li>💾 App Size</li>

<li>💰 Price</li>

<li>🔞 Content Rating</li>

<li>📅 Last Updated</li>

</ul>

</div>

""", unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------
# PDF Report Generator
# ---------------------------------------------------

def generate_prediction_report(
        category,
        rating,
        reviews,
        size,
        app_type,
        price,
        content_rating,
        year,
        month,
        prediction,
        confidence):

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "Google Play Store Prediction Report",
            styles["Title"]
        )
    )

    story.append(Spacer(1,15))

    story.append(
        Paragraph(
            f"Generated : {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1,15))

    table = Table([

        ["Feature","Value"],

        ["Category",category],

        ["Rating",rating],

        ["Reviews",reviews],

        ["Size (MB)",size],

        ["Type",app_type],

        ["Price",price],

        ["Content Rating",content_rating],

        ["Last Updated",f"{month}/{year}"]

    ])

    table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.darkblue),

        ("TEXTCOLOR",(0,0),(-1,0),colors.white),

        ("GRID",(0,0),(-1,-1),1,colors.grey),

        ("BACKGROUND",(0,1),(-1,-1),colors.beige),

        ("BOTTOMPADDING",(0,0),(-1,0),10)

    ]))

    story.append(table)

    story.append(Spacer(1,20))

        # ---------------------------------------
    # Prediction Result
    # ---------------------------------------

    result = (
        "High Install Potential"
        if prediction == 1
        else
        "Low Install Potential"
    )

    story.append(
        Paragraph(
            "<b>Prediction Result</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            f"<b>{result}</b>",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Model Confidence : <b>{confidence:.2f}%</b>",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,20))

    # ---------------------------------------
    # AI Explanation
    # ---------------------------------------

    story.append(
        Paragraph(
            "<b>AI Explanation</b>",
            styles["Heading2"]
        )
    )

    if prediction == 1:

        explanation = f"""

        The prediction model estimates HIGH INSTALL POTENTIAL because:

        • Rating ({rating}) is good.

        • Reviews ({reviews}) indicate good user engagement.

        • Category ({category}) has positive download behaviour.

        • App size ({size} MB) is reasonable.

        • Type ({app_type}) supports higher user reach.

        """

    else:

        explanation = f"""

        The model estimates LOW INSTALL POTENTIAL because:

        • Current rating is not strong enough.

        • Reviews are comparatively low.

        • User engagement appears limited.

        • App visibility may need improvement.

        """

    story.append(
        Paragraph(
            explanation,
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,20))

    # ---------------------------------------
    # Business Recommendation
    # ---------------------------------------

    story.append(
        Paragraph(
            "<b>Business Recommendations</b>",
            styles["Heading2"]
        )
    )

    recommendation = """

    ✔ Improve app rating above 4.5

    <br/><br/>

    ✔ Encourage more positive user reviews

    <br/><br/>

    ✔ Keep application size optimized

    <br/><br/>

    ✔ Update the application regularly

    <br/><br/>

    ✔ Improve Play Store screenshots and description

    """

    story.append(
        Paragraph(
            recommendation,
            styles["BodyText"]
        )
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
            "<b>Model :</b> Random Forest Classifier",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            "<b>Project :</b> Google Play Store ETL Pipeline",
            styles["BodyText"]
        )
    )

    doc.build(story)

    buffer.seek(0)

    return buffer


# ---------------------------------------------------
# Load Model
# ---------------------------------------------------

try:

    model = joblib.load("best_model.pkl")

    category_encoder = joblib.load(
        "category_encoder.pkl"
    )

    type_encoder = joblib.load(
        "type_encoder.pkl"
    )

    content_encoder = joblib.load(
        "content_encoder.pkl"
    )

except Exception as e:

    st.error(f"Model files not found : {e}")

    st.stop()

    # ---------------------------------------------------
# Input Section
# ---------------------------------------------------

st.header("📱 Application Details")

st.write(
    "Enter the application details below to predict install potential."
)

col1, col2 = st.columns(2)

with col1:

    category = st.selectbox(
        "📂 Category",
        category_encoder.classes_
    )

    rating = st.slider(
        "⭐ Rating",
        1.0,
        5.0,
        4.2
    )

    reviews = st.number_input(
        "📊 Reviews",
        min_value=0,
        value=5000
    )

    size = st.number_input(
        "💾 Size (MB)",
        min_value=1.0,
        value=25.0
    )

with col2:

    app_type = st.selectbox(
        "📱 Type",
        type_encoder.classes_
    )

    price = st.number_input(
        "💰 Price ($)",
        min_value=0.0,
        value=0.0
    )

    content_rating = st.selectbox(
        "🔞 Content Rating",
        content_encoder.classes_
    )

    year = st.number_input(
        "📅 Last Updated Year",
        2010,
        2030,
        2018
    )

    month = st.slider(
        "🗓 Update Month",
        1,
        12,
        7
    )

st.write("")

# ---------------------------------------------------
# Prediction Button
# ---------------------------------------------------

if st.button(
    "🚀 Analyze Application",
    width="stretch"
):

    input_data = pd.DataFrame({

        "Category":[
            category_encoder.transform([category])[0]
        ],

        "Rating":[rating],

        "Reviews":[reviews],

        "Size":[size],

        "Type":[
            type_encoder.transform([app_type])[0]
        ],

        "Price":[price],

        "Content Rating":[
            content_encoder.transform([content_rating])[0]
        ],

        "Year":[year],

        "Month":[month]

    })

    prediction = model.predict(input_data)

    probability = model.predict_proba(input_data)

    confidence = probability[0][1]

    st.divider()

    st.header("📊 Prediction Result")

    if prediction[0] == 1:

        st.success(
            "🎉 High Install Potential Detected"
        )

    else:

        st.error(
            "⚠ Low Install Potential Detected"
        )

    st.metric(
        "🤖 Model Confidence",
        f"{confidence*100:.2f}%"
    )

    st.progress(float(confidence))

    st.write("")

    # ==========================================
    # Probability Metrics
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "🚀 High Install Probability",
            f"{probability[0][1]*100:.2f}%"
        )

    with col2:

        st.metric(
            "⚠ Low Install Probability",
            f"{probability[0][0]*100:.2f}%"
        )

    st.divider()

    # ==========================================
    # AI Explanation
    # ==========================================

    st.subheader("🤖 AI Explanation")

    if prediction[0] == 1:

        st.success(f"""
The model predicts **High Install Potential** because:

✅ Rating ({rating}) is good.

✅ Reviews ({reviews}) indicate strong user engagement.

✅ The selected category ({category}) generally performs well.

✅ The app size ({size} MB) is reasonable.

✅ The application has characteristics similar to successful apps.
""")

    else:

        st.warning(f"""
The model predicts **Low Install Potential** because:

• Current rating is comparatively low.

• User reviews are limited.

• App visibility appears weak.

• Improving ratings and reviews can increase install probability.
""")

    st.divider()

    # ==========================================
    # Business Recommendation
    # ==========================================

    st.subheader("💼 Business Recommendations")

    st.info("""
✔ Improve app rating above **4.5**

✔ Encourage users to leave positive reviews

✔ Keep application size optimized

✔ Release updates regularly

✔ Improve screenshots and Play Store description

✔ Focus on user experience to improve engagement
""")

    st.divider()

    # ==========================================
    # Generate PDF Report
    # ==========================================

    report = generate_prediction_report(

        category,

        rating,

        reviews,

        size,

        app_type,

        price,

        content_rating,

        year,

        month,

        prediction[0],

        confidence * 100

    )

    st.download_button(

        label="📄 Download Prediction Report",

        data=report,

        file_name="Prediction_Report.pdf",

        mime="application/pdf",

        width="stretch"

    )

    # ======================================================
# Footer
# ======================================================

st.divider()

st.markdown("""
<div style="text-align:center;padding:15px;">

<h4>📱 Google Play Store ETL & Machine Learning Dashboard</h4>

Developed using

<b>Python • Pandas • Scikit-learn • Streamlit • MySQL • ReportLab</b>

<br><br>

This prediction is generated using a trained
<b>Random Forest Machine Learning Model</b>.

</div>
""", unsafe_allow_html=True)


st.caption(
    "© 2026 Tanaya Bagul | Data Science Project"
)
