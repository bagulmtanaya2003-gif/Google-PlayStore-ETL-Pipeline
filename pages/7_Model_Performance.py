import streamlit as st
import pandas as pd

# Page Configuration

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
    layout="wide"
)

# Load Data

performance_df = pd.read_csv("model_comparison.csv")


# Title

st.title("📈 Model Performance")

st.write(
    "This page compares the performance of different Machine Learning models used for app rating prediction."
)

st.divider()

# Model Comparison Table

st.subheader("📊 Model Comparison")

st.dataframe(
    performance_df,
    use_container_width=True
)

st.divider()

# Summary

st.subheader("📋 Performance Summary")

st.success("""
✔ Multiple Machine Learning models were evaluated.

✔ The comparison table displays the performance of each model.

✔ The best-performing model was selected for the final prediction system.
""")

st.divider()

# Key Insight

st.info("""
### 💡 Key Insight

• Comparing multiple models helps identify the most reliable algorithm.

• Better model performance improves prediction accuracy.

• The selected model is used in the Prediction page of this application.
""")

st.divider()

st.caption("📱 Google Play Store Analytics | Model Performance")