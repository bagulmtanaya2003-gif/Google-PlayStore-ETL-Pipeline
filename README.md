# 📱 Google Play Store Analytics using Machine Learning

An End-to-End ETL Pipeline and Machine Learning project that analyzes Google Play Store applications to identify the factors influencing app success and predicts whether an application has **High Install Potential** using a Random Forest Classifier.

---

# 📌 Project Overview

The Google Play Store contains thousands of applications across multiple categories. This project performs an end-to-end data analysis pipeline, including data extraction, cleaning, transformation, visualization, machine learning, and business insights.

The final solution is deployed as an interactive **Streamlit Dashboard** that allows users to explore data, visualize trends, and predict app success.

---

# 🎯 Business Problem

Developers and businesses often struggle to understand:

- Which app categories perform best
- What factors influence application installs
- How ratings, reviews, price, and app size affect popularity
- Whether a new application has the potential to achieve high installs

This project provides data-driven insights and a prediction system to support better business decisions.

---

# 🎯 Project Objectives

- Build an End-to-End ETL Pipeline
- Clean and preprocess raw Google Play Store data
- Perform Exploratory Data Analysis (EDA)
- Train multiple Machine Learning models
- Select the best-performing model
- Predict High Install Potential
- Build an interactive Streamlit Dashboard
- Generate downloadable prediction reports

---

# 🔄 ETL Pipeline

### Extract
- Load Google Play Store dataset
- Connect with MySQL database

### Transform
- Remove duplicates
- Handle missing values
- Clean Reviews, Price, Size, and Installs columns
- Convert date columns
- Feature Engineering
- Encode categorical variables

### Load
- Store cleaned dataset in MySQL
- Export cleaned dataset as CSV

---

# 📊 Exploratory Data Analysis

The dashboard includes:

- App Rating Distribution
- Top Categories
- Total Installs by Category
- Reviews vs Rating
- App Size vs Rating
- Free vs Paid Applications
- Price Distribution
- Correlation Heatmap
- Applications Updated by Year

---

# 🤖 Machine Learning

### Algorithms Used

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier

### Best Model

Random Forest Classifier

The trained model predicts whether an application has **High Install Potential** based on multiple application features.

---

# 📈 Features Used

- Category
- Rating
- Reviews
- Size
- Type
- Price
- Content Rating
- Year
- Month

---

# 🖥️ Streamlit Modules

- 🏠 Home
- 📊 Dashboard
- 📈 Data Analysis
- 🎯 Prediction
- ⭐ Model Performance
- 💼 Business Insights
- ⚙️ ETL Pipeline
- 📥 Download Report
- 👨‍💻 About Developer
- ❓ Help

---

# 🛠️ Technology Stack

### Programming

- Python

### Database

- MySQL

### Libraries

- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- SQLAlchemy
- PyMySQL
- Joblib
- ReportLab
- Streamlit

### Tools

- VS Code
- Git
- GitHub
- MySQL Workbench

---

# 📂 Project Structure

```
Google_PlayStore_ETL_Project
│
├── app.py
├── requirements.txt
├── README.md
├── playstore_clean.csv
├── best_model.pkl
├── category_encoder.pkl
├── type_encoder.pkl
├── content_encoder.pkl
│
├── SQL
│   ├── database_creation.sql
│   ├── table_creation.sql
│   └── data_analysis_queries.sql
│
├── pages
│   ├── Dashboard.py
│   ├── Data_Analysis.py
│   ├── Prediction.py
│   ├── Model_Performance.py
│   ├── Business_Insights.py
│   ├── ETL_Pipeline.py
│   ├── Download_Report.py
│   ├── About_Developer.py
│   └── Help.py
│
└── screenshots
```

---

# 🚀 How to Run the Project

## Clone Repository

```bash
git clone https://github.com/bagulmtanaya2003-gif
```

## Open Project

```bash
cd Google-PlayStore-ETL-Pipeline
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Streamlit

```bash
streamlit run app.py
```

---

# 📸 Project Screenshots

Add screenshots of:

- Home
- Dashboard
- Prediction
- Model Performance
- Business Insights

inside the **screenshots/** folder.

---

# 💡 Business Insights

- Higher ratings generally lead to increased installs.
- Reviews strongly influence application popularity.
- Free applications dominate the Google Play Store.
- Regular updates improve user engagement.
- Category selection impacts install potential.

---

# 📥 Prediction Report

The application can generate a downloadable PDF report containing:

- User Inputs
- Prediction Result
- Model Confidence
- AI Explanation
- Business Recommendations

---

# 👨‍💻 Developer

**Tanaya Bagul**

Aspiring Data Analyst | Data Scientist

Skills:
- Python
- SQL
- Machine Learning
- Data Analytics
- Streamlit
- MySQL
- Git & GitHub

---

# ⭐ Future Improvements

- Deep Learning Models
- Hyperparameter Tuning
- Model Deployment on Cloud
- Live Data Integration
- Interactive Power BI Dashboard

---

# 📄 License

This project is developed for educational and portfolio purposes.