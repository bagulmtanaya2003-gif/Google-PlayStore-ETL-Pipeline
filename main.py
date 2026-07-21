import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import pymysql

from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "root"
password = quote_plus("Tanaya@2003")

host = "localhost"
database = "google_playstore_db"


engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

df = pd.read_csv("googleplaystore.csv")

print(df.head())
print(df.shape)

df.to_sql(
    "playstore",
    engine,
    if_exists="replace",
    index=False
)
print("Data Loaded Successfully")

sql_data = pd.read_sql(
    "SELECT * FROM playstore",
    engine
)
print(sql_data.head())
print(sql_data.shape)

print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())
df = df.drop_duplicates()
print(df.shape)

df.isnull().sum()

# Handle Missing Values
df["Rating"] = df["Rating"].fillna(df["Rating"].median())
df["Type"] = df["Type"].fillna(df["Type"].mode()[0])
df["Content Rating"] = df["Content Rating"].fillna(df["Content Rating"].mode()[0])
df["Current Ver"] = df["Current Ver"].fillna("Unknown")
df["Android Ver"] = df["Android Ver"].fillna("Unknown")
print(df.isnull().sum())

# Remove Invalid Ratings
df = df[df["Rating"] <= 5]
print(df["Rating"].describe())

# Clean Reviews Column
df["Reviews"] = pd.to_numeric(df["Reviews"], errors="coerce")

df = df.dropna(subset=["Reviews"])
df["Reviews"] = df["Reviews"].astype(int)
df.info()
print(df["Reviews"].dtype)

# Clean Size Column
def clean_size(size):
    if size == "Varies with device":
        return np.nan
    elif "M" in size:
        return float(size.replace("M",""))
    elif "k" in size:
        return float(size.replace("k",""))/1024
    else:
        return np.nan

# Applying cleaning function on Size column
df["Size"] = df["Size"].apply(clean_size)
# Filling missing values with median value
df["Size"] = df["Size"].fillna(df["Size"].median())
print(df["Size"].head())

# Clean Installs Column
df["Installs"] = (
    df["Installs"]
    .str.replace(",","",regex=False)
    .str.replace("+","",regex=False)
)
df["Installs"] = pd.to_numeric(df["Installs"])
print(df["Installs"].dtype)

# 
df["Price"] = (
    df["Price"]
    .str.replace("$","",regex=False)
)
df["Price"] = pd.to_numeric(df["Price"])
print(df["Price"].dtype)

# Convert Last Updated Date
df["Last Updated"] = pd.to_datetime(df["Last Updated"])
# Creating Year feature from date
df["Year"] = df["Last Updated"].dt.year
# Creating Month feature from date
df["Month"] = df["Last Updated"].dt.month
print(df[["Year","Month"]].head())

# Load Clean Data into MySQL
df.to_sql(
    "playstore_clean",
    engine,
    if_exists="replace",
    index=False
)
print("Clean Data Loaded Successfully")

# Saving cleaned dataset as CSV file
df.to_csv("playstore_clean.csv", index=False)
print("Clean CSV File Saved Successfully")

# Exploratory Data Analysis

# Plot distribution of app ratings
plt.figure(figsize=(8,5))
sns.histplot(df["Rating"], bins=20)
plt.title("Distribution of App Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Apps")
plt.show()

# Display number of apps in each category
plt.figure(figsize=(12,6))
sns.countplot(
    y="Category",
    data=df,
    order=df["Category"].value_counts().index
)
plt.title("Applications by Category")
plt.show()

# Display total installs for each category
top_installs = df.groupby("Category")["Installs"].sum().sort_values(ascending=False)
plt.figure(figsize=(12,6))
top_installs.plot(kind="bar")
plt.title("Total Installs by Category")
plt.xlabel("Category")
plt.ylabel("Installs")
plt.show()

# Analyze relationship between reviews and ratings
plt.figure(figsize=(8,5))
sns.scatterplot(
    x="Reviews",
    y="Rating",
    data=df
)
plt.title("Reviews vs Rating")
plt.show()

# Analyze relationship between app size and rating
plt.figure(figsize=(8,5))
sns.scatterplot(
    x="Size",
    y="Rating",
    data=df
)
plt.title("App Size vs Rating")
plt.show()

# Compare Free and Paid applications
plt.figure(figsize=(6,5))
sns.countplot(
    x="Type",
    data=df
)
plt.title("Free vs Paid Applications")
plt.show()

# Display price distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], bins=20)
plt.title("Price Distribution")
plt.show()

# Display correlation between numerical features
plt.figure(figsize=(8,6))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()

# Display applications updated each year
plt.figure(figsize=(10,5))
sns.countplot(
    x="Year",
    data=df
)
plt.title("Applications Updated Every Year")
plt.show()

# Create target variable for machine learning
df["High_Install"] = np.where(df["Installs"] >= 1000000, 1, 0)
print(df[["Installs", "High_Install"]].head())
print(df["High_Install"].value_counts())

# Select important features
features = [
    "Category",
    "Rating",
    "Reviews",
    "Size",
    "Type",
    "Price",
    "Content Rating",
    "Year",
    "Month"
]
X = df[features]
y = df["High_Install"]

# Display selected features
print(X.head())
print(y.head())

# Convert categorical values into numerical values
from sklearn.preprocessing import LabelEncoder

# Create separate encoders for each categorical column
category_encoder = LabelEncoder()
type_encoder = LabelEncoder()
content_encoder = LabelEncoder()
# Encode Category column
X["Category"] = category_encoder.fit_transform(
    X["Category"]
)
# Encode Type column
X["Type"] = type_encoder.fit_transform(
    X["Type"]
)
# Encode Content Rating column
X["Content Rating"] = content_encoder.fit_transform(
    X["Content Rating"]
)

# Display feature datatypes
print(X.dtypes)

# Display final dataset shape
print(X.shape)
print(y.shape)

# Split dataset into training and testing sets
# Import train-test split
from sklearn.model_selection import train_test_split
# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)
# Display dataset shape
print("Training Features :", X_train.shape)
print("Testing Features  :", X_test.shape)
print("Training Target   :", y_train.shape)
print("Testing Target    :", y_test.shape)

# Standardize numerical features for machine learning
# Import StandardScaler
from sklearn.preprocessing import StandardScaler
# Create StandardScaler object
scaler = StandardScaler()
# Scale training features
X_train_scaled = scaler.fit_transform(X_train)
# Scale testing features
X_test_scaled = scaler.transform(X_test)
# Display scaled dataset shape
print("Scaled Training Data :", X_train_scaled.shape)
print("Scaled Testing Data  :", X_test_scaled.shape)

# Import machine learning algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# Train Logistic Regression model
log_model = LogisticRegression(max_iter=1000)
# Train model using scaled training data
log_model.fit(X_train_scaled, y_train)
# Predict using scaled testing data
log_prediction = log_model.predict(X_test_scaled)

# Train Decision Tree model
tree_model = DecisionTreeClassifier(random_state=42)
tree_model.fit(X_train, y_train)
tree_prediction = tree_model.predict(X_test)

# Train Random Forest model
forest_model = RandomForestClassifier(
    random_state=42
)
forest_model.fit(X_train, y_train)
forest_prediction = forest_model.predict(X_test)

# Import model evaluation metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Evaluate Logistic Regression model
log_accuracy = accuracy_score(y_test, log_prediction)
print("Logistic Regression Accuracy :",
      round(log_accuracy * 100, 2), "%")

# Evaluate Decision Tree model
tree_accuracy = accuracy_score(
    y_test,
    tree_prediction
)
print("Decision Tree Accuracy :",
      round(tree_accuracy * 100,2),"%")

# Evaluate Random Forest model
forest_accuracy = accuracy_score(
    y_test,
    forest_prediction
)
print("Random Forest Accuracy :",
      round(forest_accuracy * 100,2),"%")

# Display confusion matrix for all models
print("Logistic Regression Confusion Matrix")
print(confusion_matrix(
    y_test,
    log_prediction
))

print("Decision Tree Confusion Matrix")
print(confusion_matrix(
    y_test,
    tree_prediction
))

print("Random Forest Confusion Matrix")
print(confusion_matrix(
    y_test,
    forest_prediction
))

# Display classification report

print("Logistic Regression Report")
print(classification_report(
    y_test,
    log_prediction
))

print("Decision Tree Report")
print(classification_report(
    y_test,
    tree_prediction
))

print("Random Forest Report")
print(classification_report(
    y_test,
    forest_prediction
))

# Compare model accuracy
print("\nModel Accuracy Comparison")
print("-" * 40)
print("Logistic Regression :",
      round(log_accuracy * 100,2),"%")
print("Decision Tree       :",
      round(tree_accuracy * 100,2),"%")
print("Random Forest       :",
      round(forest_accuracy * 100,2),"%")

# Select best machine learning model
accuracy_scores = {
    "Logistic Regression": log_accuracy,
    "Decision Tree": tree_accuracy,
    "Random Forest": forest_accuracy
}
best_model_name = max(
    accuracy_scores,
    key=accuracy_scores.get
)
print("\nBest Model :", best_model_name)

comparison = pd.DataFrame({

    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest"
    ],

    "Accuracy": [
        log_accuracy,
        tree_accuracy,
        forest_accuracy
    ]

})
comparison.to_csv(
    "model_comparison.csv",
    index=False
)

# Save the best trained model
import joblib
# Save Random Forest model
joblib.dump(forest_model, "best_model.pkl")
# Save scaler
joblib.dump(scaler, "scaler.pkl")
# Save category encoder
joblib.dump(category_encoder, "category_encoder.pkl")
# Save type encoder
joblib.dump(type_encoder, "type_encoder.pkl")
# Save content rating encoder
joblib.dump(content_encoder, "content_encoder.pkl")
print("Model Saved Successfully")

# Create sample data for a new application
# Create sample data for prediction
new_app = pd.DataFrame({
    "Category": ["GAME"],
    "Rating": [4.8],
    "Reviews": [5000000],
    "Size": [45],
    "Type": ["Free"],
    "Price": [0],
    "Content Rating": ["Everyone"],
    "Year": [2018],
    "Month": [7]
})
print(new_app)

# Encode categorical features
new_app["Category"] = category_encoder.transform(
    new_app["Category"]
)
new_app["Type"] = type_encoder.transform(
    new_app["Type"]
)
new_app["Content Rating"] = content_encoder.transform(
    new_app["Content Rating"]
)

# Predict app success using Random Forest

# Predict using original features (No Scaling Required)
prediction = forest_model.predict(new_app)

print("Prediction :", prediction[0])

# Display prediction probabilities
probability = forest_model.predict_proba(new_app)

print("Prediction Probability :", probability)
print("Low Install Probability :", probability[0][0])
print("High Install Probability :", probability[0][1])

# Display prediction result
if prediction[0] == 1:
    print("This application is likely to achieve High Installs.")
else:
    print("This application is unlikely to achieve High Installs.")

# Display feature importance from Random Forest model
feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": forest_model.feature_importances_
})
print(feature_importance)
feature_importance.to_csv(
    "feature_importance.csv",
    index=False
)

# Plot feature importance
plt.figure(figsize=(10,6))
sns.barplot(
    data=feature_importance,
    x="Importance",
    y="Feature"
)
plt.title("Feature Importance - Random Forest")
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.show()

# Display top 5 important features
print("Top 5 Important Features")
print(feature_importance.head())

# Display business insights
print("\nBusiness Insight")
for index, row in feature_importance.head().iterrows():
    print(
        f"{row['Feature']} : {round(row['Importance']*100,2)} % importance"
    )

