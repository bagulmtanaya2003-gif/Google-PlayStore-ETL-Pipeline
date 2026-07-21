import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(
    page_title="Feature Importance",
    page_icon="⭐",
    layout="wide"
)

# Load Feature Importance Data

feature_df = pd.read_csv("feature_importance.csv")

# Page Title

st.title("⭐ Feature Importance")

st.write(
    "This page shows the importance of each feature used by the Random Forest model for predicting app ratings."
)

st.divider()

# Feature Importance Chart

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(
    feature_df["Feature"],
    feature_df["Importance"]
)

ax.set_xlabel("Importance Score")
ax.set_ylabel("Features")
ax.set_title("Feature Importance")

st.pyplot(fig)

st.divider()

# Top Features Table

st.subheader("📋 Feature Importance Values")

st.dataframe(
    feature_df.sort_values("Importance", ascending=False),
    use_container_width=True
)

st.divider()

# Key Insight

st.success("""
### 💡 Key Insight

• Features with higher importance have a greater influence on model predictions.

• These features help identify the factors that contribute most to application ratings.

• Understanding feature importance supports better business decisions and app optimization.
""")